"""
Style Fingerprint — per-account style signatures.

For each account with enough tweets, computes:
- Statistical profile of 55 text features (mean, std, p25, p75)
- Centroid embedding (384-dim) for semantic positioning
- Engagement stats (median likes, retweets, bookmarks)
- Top hooks (first 80 chars of highest-liked tweets)
- Content pillars (most common keywords)

Used by orchestrator to find best reference accounts for each draft.
Persisted to: knowledge-graph/style_fingerprints.json
"""
import numpy as np
import sqlite3
import json
from pathlib import Path
from datetime import datetime
from collections import Counter
import re

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import KG, DB_PATH
from pipeline.features import extract, FEATURE_NAMES

FINGERPRINTS_PATH = KG / "style_fingerprints.json"
MIN_TWEETS_PER_ACCOUNT = 20
EMBEDDING_DIM = 384


def _load_account_tweets(handle: str) -> list[dict]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT text, embedding, likes, retweets, bookmarks, created_at
        FROM feed_tweets
        WHERE author_handle = ?
          AND is_retweet = 0
          AND text IS NOT NULL
          AND length(text) > 20
        ORDER BY likes DESC
    """, (handle,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def _compute_fingerprint(handle: str, tweets: list[dict]) -> dict:
    """Compute the full style fingerprint for an account."""
    texts = [t["text"] for t in tweets]
    created_ats = [t.get("created_at") or "" for t in tweets]

    # Feature matrix
    feat_matrix = np.stack([extract(t, ca) for t, ca in zip(texts, created_ats)])

    # Embedding centroid
    emb_list = []
    for t in tweets:
        blob = t.get("embedding")
        if blob and len(blob) == EMBEDDING_DIM * 4:
            emb_list.append(np.frombuffer(blob, dtype=np.float32))
    centroid = np.mean(emb_list, axis=0).tolist() if emb_list else [0.0] * EMBEDDING_DIM

    # Feature stats
    feature_stats = {}
    for i, name in enumerate(FEATURE_NAMES):
        col = feat_matrix[:, i]
        feature_stats[name] = {
            "mean": round(float(np.mean(col)), 4),
            "std": round(float(np.std(col)), 4),
            "p25": round(float(np.percentile(col, 25)), 4),
            "p75": round(float(np.percentile(col, 75)), 4),
        }

    # Engagement stats
    likes_list = [t.get("likes") or 0 for t in tweets]
    rt_list = [t.get("retweets") or 0 for t in tweets]
    bm_list = [t.get("bookmarks") or 0 for t in tweets]

    # Top hooks (first 80 chars of top 10 most-liked tweets)
    sorted_by_likes = sorted(tweets, key=lambda x: x.get("likes") or 0, reverse=True)
    top_hooks = [t["text"][:80].strip() for t in sorted_by_likes[:10]]

    # Content pillars: most common content words
    all_words = []
    for t in texts:
        words = re.findall(r'\b[a-zA-Z]{4,}\b', t.lower())
        all_words.extend(words)
    stopwords = {"this", "that", "with", "have", "been", "will", "from", "they",
                 "your", "what", "when", "just", "about", "dont", "more", "like",
                 "some", "also", "into", "were", "their", "than", "then", "much",
                 "https", "http", "twitter", "tweet", "retweet", "follow", "link",
                 "quot", "amp", "com", "www", "here", "there", "know", "make",
                 "time", "good", "great", "need", "want", "think", "really", "very"}
    content_words = Counter(w for w in all_words if w not in stopwords)
    top_words = [w for w, _ in content_words.most_common(20)]

    return {
        "handle": handle,
        "n_tweets": len(tweets),
        "updated_at": datetime.now().isoformat(),
        "centroid": centroid,
        "feature_stats": feature_stats,
        "engagement": {
            "median_likes": round(float(np.median(likes_list)), 1),
            "p75_likes": round(float(np.percentile(likes_list, 75)), 1),
            "p90_likes": round(float(np.percentile(likes_list, 90)), 1),
            "median_rt": round(float(np.median(rt_list)), 1),
            "median_bm": round(float(np.median(bm_list)), 1),
        },
        "top_hooks": top_hooks,
        "content_pillars": top_words,
    }


def build_fingerprints(min_tweets: int = MIN_TWEETS_PER_ACCOUNT) -> dict:
    """Build fingerprints for all accounts with enough tweets."""
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("""
        SELECT author_handle, COUNT(*) as n
        FROM feed_tweets
        WHERE is_retweet = 0 AND text IS NOT NULL
        GROUP BY author_handle
        HAVING n >= ?
        ORDER BY n DESC
    """, (min_tweets,)).fetchall()
    conn.close()

    handles = [r[0] for r in rows if r[0]]
    print(f"[style_fingerprint] Building fingerprints for {len(handles)} accounts...")

    fingerprints = {}
    for i, handle in enumerate(handles, 1):
        tweets = _load_account_tweets(handle)
        if len(tweets) < min_tweets:
            continue
        fp = _compute_fingerprint(handle, tweets)
        # Drop centroid from JSON to keep file manageable — store separately
        fingerprints[handle] = {k: v for k, v in fp.items() if k != "centroid"}
        if i % 10 == 0:
            print(f"  {i}/{len(handles)} done...")

    # Store centroid embeddings separately (binary would be better but json is fine for now)
    result = {
        "built_at": datetime.now().isoformat(),
        "n_accounts": len(fingerprints),
        "fingerprints": fingerprints,
    }
    FINGERPRINTS_PATH.write_text(json.dumps(result, indent=2))
    print(f"[style_fingerprint] Done — {len(fingerprints)} fingerprints → {FINGERPRINTS_PATH}")
    return result


def get_fingerprints() -> dict:
    """Load all fingerprints. Returns {handle: fingerprint_dict}."""
    if not FINGERPRINTS_PATH.exists():
        return {}
    data = json.loads(FINGERPRINTS_PATH.read_text())
    return data.get("fingerprints", {})


def get_fingerprint(handle: str) -> dict | None:
    return get_fingerprints().get(handle)


def get_best_accounts(n: int = 10, metric: str = "p90_likes") -> list[dict]:
    """
    Return top N accounts sorted by engagement metric.
    metric: 'median_likes', 'p75_likes', 'p90_likes', 'median_rt'
    """
    fps = get_fingerprints()
    accounts = []
    for handle, fp in fps.items():
        eng = fp.get("engagement", {})
        score = eng.get(metric, 0)
        accounts.append({
            "handle": handle,
            "n_tweets": fp.get("n_tweets", 0),
            "score": score,
            "content_pillars": fp.get("content_pillars", [])[:5],
            "top_hooks": fp.get("top_hooks", [])[:3],
            "engagement": eng,
        })
    return sorted(accounts, key=lambda x: -x["score"])[:n]


def get_style_exemplars(
    style_type: str = "list",
    n: int = 5,
) -> list[str]:
    """
    Return example hooks from top accounts matching a style type.
    style_type: 'list', 'hot_take', 'prediction', 'question', 'observation'
    """
    feature_map = {
        "list": "is_list_tweet",
        "hot_take": "is_hot_take",
        "prediction": "is_prediction",
        "question": "is_question_tweet",
        "observation": "is_observation",
        "builder": "is_builder_flex",
        "thread": "is_thread_opener",
    }
    feat = feature_map.get(style_type, "is_observation")

    fps = get_fingerprints()
    matching_hooks = []

    for handle, fp in fps.items():
        eng = fp.get("engagement", {})
        if eng.get("p90_likes", 0) < 50:
            continue
        fs = fp.get("feature_stats", {}).get(feat, {})
        if fs.get("mean", 0) > 0.3:  # account frequently uses this style
            hooks = fp.get("top_hooks", [])
            matching_hooks.extend(hooks[:2])

    return matching_hooks[:n]


def get_status() -> str:
    if not FINGERPRINTS_PATH.exists():
        return "not built"
    data = json.loads(FINGERPRINTS_PATH.read_text())
    return (
        f"built — {data.get('n_accounts', 0)} accounts, "
        f"at {data.get('built_at', '?')[:10]}"
    )


if __name__ == "__main__":
    result = build_fingerprints()
    print(f"Accounts: {result['n_accounts']}")
    best = get_best_accounts(5)
    for a in best:
        print(f"  @{a['handle']}: p90_likes={a['score']}")
