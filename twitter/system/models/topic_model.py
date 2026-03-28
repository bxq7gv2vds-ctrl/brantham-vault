"""
Topic Model — BERTopic clustering of the tweet corpus.

Discovers content niches (clusters) in the 384-dim embedding space.
Identifies trending topics, content gaps, topic velocity.

Persisted to: knowledge-graph/topic_model/
"""
import numpy as np
import sqlite3
import json
import pickle
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import KG, DB_PATH

MODEL_DIR = KG / "topic_model"
TOPIC_MODEL_PATH = MODEL_DIR / "bertopic_model"
TOPICS_CACHE_PATH = MODEL_DIR / "topics_cache.json"
EMBEDDING_DIM = 384
MIN_CLUSTER_SIZE = 10


def _ensure_dir():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)


def load_corpus() -> tuple[list[str], list[np.ndarray], list[dict]]:
    """Load all embedded tweets. Returns (texts, embeddings, metadata)."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT id, text, embedding, likes, retweets, author_handle,
               created_at, topic
        FROM feed_tweets
        WHERE embedding IS NOT NULL
          AND text IS NOT NULL
          AND length(text) > 20
          AND is_retweet = 0
    """).fetchall()
    conn.close()

    texts, embeddings, meta = [], [], []
    for r in rows:
        emb_blob = r["embedding"]
        if emb_blob and len(emb_blob) == EMBEDDING_DIM * 4:
            emb = np.frombuffer(emb_blob, dtype=np.float32)
            texts.append(r["text"])
            embeddings.append(emb)
            meta.append(dict(r))

    return texts, embeddings, meta


def train(min_cluster_size: int = MIN_CLUSTER_SIZE) -> dict:
    """Train BERTopic on the full corpus."""
    _ensure_dir()

    texts, embeddings, meta = load_corpus()
    if len(texts) < 50:
        return {"error": f"need 50+ tweets, got {len(texts)}"}

    print(f"[topic_model] Training on {len(texts):,} tweets...")

    from bertopic import BERTopic
    from umap import UMAP
    from hdbscan import HDBSCAN
    from sklearn.feature_extraction.text import CountVectorizer

    matrix = np.stack(embeddings).astype(np.float32)

    umap_model = UMAP(
        n_neighbors=15,
        n_components=5,
        min_dist=0.0,
        metric="cosine",
        random_state=42,
    )
    hdbscan_model = HDBSCAN(
        min_cluster_size=min_cluster_size,
        min_samples=5,
        metric="euclidean",
        cluster_selection_method="eom",
        prediction_data=True,
    )
    vectorizer = CountVectorizer(
        ngram_range=(1, 2),
        stop_words="english",
        min_df=2,
        max_features=5000,
    )

    topic_model = BERTopic(
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        vectorizer_model=vectorizer,
        top_n_words=10,
        verbose=False,
    )

    topics, probs = topic_model.fit_transform(texts, embeddings=matrix)

    # Save model
    topic_model.save(str(TOPIC_MODEL_PATH), serialization="pickle", save_ctfidf=True)

    # Build topics cache
    topic_info = topic_model.get_topic_info()
    topics_data = []
    for _, row in topic_info.iterrows():
        tid = int(row["Topic"])
        if tid == -1:
            continue  # skip outliers
        words = topic_model.get_topic(tid)
        if not words:
            continue
        # Collect meta for this cluster
        indices = [i for i, t in enumerate(topics) if t == tid]
        likes_list = [meta[i].get("likes") or 0 for i in indices]
        handles = [meta[i].get("author_handle") or "" for i in indices]
        topics_data.append({
            "id": tid,
            "count": int(row["Count"]),
            "name": row.get("Name", ""),
            "keywords": [w for w, _ in words[:10]],
            "avg_likes": round(float(np.mean(likes_list)), 1) if likes_list else 0,
            "top_handles": [h for h, _ in Counter(handles).most_common(5)],
        })

    cache = {
        "trained_at": datetime.now().isoformat(),
        "n_docs": len(texts),
        "n_topics": len(topics_data),
        "topics": sorted(topics_data, key=lambda x: -x["count"]),
    }
    TOPICS_CACHE_PATH.write_text(json.dumps(cache, indent=2))

    print(f"[topic_model] {len(topics_data)} topics found. Saved → {MODEL_DIR}")
    return cache


def load_model():
    """Load persisted BERTopic model."""
    if not TOPIC_MODEL_PATH.exists():
        return None
    from bertopic import BERTopic
    try:
        return BERTopic.load(str(TOPIC_MODEL_PATH))
    except Exception:
        return None


def get_topics() -> list[dict]:
    """Return cached topic list."""
    if not TOPICS_CACHE_PATH.exists():
        return []
    data = json.loads(TOPICS_CACHE_PATH.read_text())
    return data.get("topics", [])


def assign_topic(embedding: np.ndarray) -> tuple[int, float]:
    """
    Predict topic for a given embedding.
    Returns (topic_id, confidence). topic_id=-1 means outlier.
    """
    model = load_model()
    if model is None:
        return -1, 0.0
    topics, probs = model.transform([""], embeddings=embedding.reshape(1, -1))
    tid = int(topics[0])
    prob = float(probs[0]) if probs is not None and len(probs) > 0 else 0.0
    return tid, prob


def get_trending_topics(days: int = 7, top_n: int = 5) -> list[dict]:
    """
    Topics that are trending in recent N days vs baseline.
    Returns top_n topics by recency velocity.
    """
    since = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%S")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    recent = conn.execute("""
        SELECT text, embedding, likes, created_at
        FROM feed_tweets
        WHERE embedding IS NOT NULL
          AND created_at >= ?
          AND is_retweet = 0
    """, (since,)).fetchall()
    conn.close()

    if len(recent) < 5:
        return get_topics()[:top_n]

    model = load_model()
    if model is None:
        return get_topics()[:top_n]

    texts = [r["text"] for r in recent]
    embs = []
    for r in recent:
        blob = r["embedding"]
        if blob and len(blob) == EMBEDDING_DIM * 4:
            embs.append(np.frombuffer(blob, dtype=np.float32))
        else:
            embs.append(np.zeros(EMBEDDING_DIM, dtype=np.float32))

    matrix = np.stack(embs).astype(np.float32)
    topics, _ = model.transform(texts, embeddings=matrix)

    topic_counts = Counter(t for t in topics if t != -1)
    all_topics = get_topics()
    topic_map = {t["id"]: t for t in all_topics}

    trending = []
    for tid, recent_count in topic_counts.most_common(top_n * 2):
        if tid in topic_map:
            t = dict(topic_map[tid])
            t["recent_count"] = recent_count
            trending.append(t)

    return trending[:top_n]


def get_content_gaps(posted_texts: list[str], top_n: int = 3) -> list[dict]:
    """
    Find topics that are popular in the feed but underrepresented in posted_texts.
    """
    if not posted_texts:
        return get_topics()[:top_n]

    model = load_model()
    if model is None:
        return []

    from pipeline.vector_store import embed_text
    posted_embs = [embed_text(t) for t in posted_texts]
    posted_matrix = np.stack(posted_embs).astype(np.float32)
    posted_topics, _ = model.transform(posted_texts, embeddings=posted_matrix)
    posted_topic_set = set(t for t in posted_topics if t != -1)

    all_topics = get_topics()
    gaps = [t for t in all_topics if t["id"] not in posted_topic_set]
    return sorted(gaps, key=lambda x: -x["count"])[:top_n]


def get_status() -> str:
    if not TOPICS_CACHE_PATH.exists():
        return "not trained"
    data = json.loads(TOPICS_CACHE_PATH.read_text())
    return (
        f"trained — {data.get('n_topics', 0)} topics, "
        f"{data.get('n_docs', 0):,} docs, "
        f"at {data.get('trained_at', '?')[:10]}"
    )


if __name__ == "__main__":
    result = train()
    print(json.dumps(result, indent=2, default=str))
