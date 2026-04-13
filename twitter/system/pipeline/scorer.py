"""
Unified Draft Scorer — combines all signals into a single score.

Score components:
  1. engagement_net prediction (PyTorch, predicted likes/rt/bm)
  2. semantic similarity to top-performing tweets (FAISS)
  3. topic relevance (BERTopic — is this a popular topic?)
  4. feature quality (structural + hook strength)
  5. style diversity (vs recently posted content)

Output: {
    "total": 0.0-1.0,
    "engagement": 0.0-1.0,
    "similarity": 0.0-1.0,
    "topic_relevance": 0.0-1.0,
    "feature_quality": 0.0-1.0,
    "breakdown": {...},
    "predicted_likes": int,
    "similar_tweets": [...],
}
"""
import numpy as np
from pathlib import Path
from datetime import datetime

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))


def score_draft(
    text: str,
    embedding: np.ndarray = None,
    created_at: str = None,
    recently_posted: list[str] = None,
) -> dict:
    """
    Full scoring pipeline for a draft tweet.

    Args:
        text: tweet text to score
        embedding: precomputed 384-dim embedding (optional, will compute if None)
        created_at: ISO datetime string for temporal features
        recently_posted: list of recent tweet texts (for diversity check)

    Returns:
        dict with scores and metadata
    """
    from pipeline.features import extract
    from pipeline.vector_store import embed_text, search

    # 1. Compute embedding if not provided
    if embedding is None:
        embedding = embed_text(text)

    # 2. Feature extraction
    feats = extract(text, created_at or "")

    # 3. Engagement prediction
    engagement_score, engagement_details = _score_engagement(text, embedding, created_at)

    # 4. Semantic similarity to top tweets
    similar = search(text, top_k=5, min_likes=100)
    similarity_score = 0.0
    if similar:
        similarity_score = min(1.0, float(similar[0].get("similarity", 0)))

    # 5. Topic relevance
    topic_score = _score_topic_relevance(embedding)

    # 6. Feature quality (hook + structure)
    feature_score = _score_features(feats)

    # 7. Diversity vs recently posted
    diversity_score = _score_diversity(embedding, recently_posted or [])

    # Weighted composite
    weights = {
        "engagement": 0.35,
        "similarity": 0.20,
        "topic": 0.15,
        "features": 0.20,
        "diversity": 0.10,
    }
    total = (
        weights["engagement"] * engagement_score +
        weights["similarity"] * similarity_score +
        weights["topic"] * topic_score +
        weights["features"] * feature_score +
        weights["diversity"] * diversity_score
    )

    return {
        "total": round(total, 3),
        "engagement": round(engagement_score, 3),
        "similarity": round(similarity_score, 3),
        "topic_relevance": round(topic_score, 3),
        "feature_quality": round(feature_score, 3),
        "diversity": round(diversity_score, 3),
        "breakdown": engagement_details,
        "similar_tweets": [
            {"text": t["text"][:100], "likes": t.get("likes", 0), "handle": t.get("author_handle", "")}
            for t in similar[:3]
        ],
    }


def _score_engagement(
    text: str,
    embedding: np.ndarray,
    created_at: str = None,
) -> tuple[float, dict]:
    """Use engagement_net to predict engagement."""
    try:
        from models.engagement_net import predict
        pred = predict(text, embedding, created_at)
        score = pred.get("score", 0.0)
        return float(score), {
            "predicted_likes": pred.get("predicted_likes", 0),
            "predicted_rt": pred.get("predicted_rt", 0),
            "predicted_bookmarks": pred.get("predicted_bookmarks", 0),
        }
    except Exception:
        return 0.5, {}


def _score_topic_relevance(embedding: np.ndarray) -> float:
    """Check if this embedding falls in a popular topic cluster."""
    try:
        from models.topic_model import assign_topic, get_topics
        tid, prob = assign_topic(embedding)
        if tid == -1:
            return 0.3  # outlier — could be novel content, not totally bad
        topics = get_topics()
        if not topics:
            return 0.5
        # Normalize by max count
        topic_map = {t["id"]: t for t in topics}
        if tid not in topic_map:
            return 0.4
        max_count = max(t["count"] for t in topics)
        count_score = topic_map[tid]["count"] / max_count
        return min(1.0, 0.4 + count_score * 0.6) * (0.5 + prob * 0.5)
    except Exception:
        return 0.5


def _score_features(feats: np.ndarray) -> float:
    """
    Heuristic feature quality score based on patterns that correlate
    with engagement in text features.
    """
    from pipeline.features import FEATURE_NAMES
    f = {name: float(feats[i]) for i, name in enumerate(FEATURE_NAMES)}

    score = 0.5

    # Hook strength
    hook_len = f.get("hook_length", 0)
    if 5 <= hook_len <= 15:
        score += 0.1  # punchy hook
    if f.get("hook_has_number", 0):
        score += 0.05
    if f.get("hook_has_question", 0):
        score += 0.05

    # Structure
    if f.get("is_list_tweet", 0):
        score += 0.05
    if f.get("has_numbered_list", 0):
        score += 0.05
    if f.get("line_breaks", 0) >= 2:
        score += 0.03  # scannable

    # Length sweet spot
    char_len = f.get("char_len", 0)
    if 100 <= char_len <= 250:
        score += 0.05
    elif char_len > 280:
        score -= 0.1  # too long for a regular tweet

    # Content signals
    if f.get("has_numbers", 0):
        score += 0.03
    if f.get("specific_numbers", 0):
        score += 0.03

    # Penalize
    if f.get("has_url", 0):
        score -= 0.05  # urls reduce organic reach
    if f.get("has_mention", 0):
        score -= 0.03

    return max(0.0, min(1.0, score))


def _score_diversity(embedding: np.ndarray, recently_posted: list[str]) -> float:
    """
    Score 1.0 if topic is totally fresh, 0.0 if very similar to recent posts.
    """
    if not recently_posted:
        return 0.8  # unknown — assume ok

    try:
        from pipeline.vector_store import embed_text
        recent_embs = [embed_text(t) for t in recently_posted[:10]]
        similarities = [float(np.dot(embedding, e)) for e in recent_embs]
        max_sim = max(similarities)
        # max_sim near 1.0 = very similar = low diversity
        diversity = 1.0 - max(0.0, (max_sim - 0.3) / 0.7)
        return max(0.0, min(1.0, diversity))
    except Exception:
        return 0.7


def score_batch(
    drafts: list[str],
    embeddings: list[np.ndarray] = None,
    created_at: str = None,
    recently_posted: list[str] = None,
) -> list[dict]:
    """Score multiple drafts, returns sorted by total score desc."""
    if embeddings is None:
        embeddings = [None] * len(drafts)

    results = []
    for i, (text, emb) in enumerate(zip(drafts, embeddings)):
        s = score_draft(text, emb, created_at, recently_posted)
        s["draft_index"] = i
        s["text"] = text
        results.append(s)

    return sorted(results, key=lambda x: -x["total"])


if __name__ == "__main__":
    import json
    test = "I built a fully autonomous agent in 48h using Claude + Python. Here's what I learned:"
    result = score_draft(test)
    print(json.dumps(result, indent=2))
