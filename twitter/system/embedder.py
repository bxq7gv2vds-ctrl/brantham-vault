"""
Embedder — embeds all tweets using sentence-transformers.
Stores embeddings in SQLite as BLOBs.
Provides semantic similarity search: find tweets similar to a given text.

Model: all-MiniLM-L6-v2 (80MB, fast on Apple Silicon)
"""
import sqlite3
import json
import sys
import numpy as np
from pathlib import Path
from typing import List, Tuple

from config import DB_PATH, KG

EMBEDDING_DIM = 384  # all-MiniLM-L6-v2
MODEL_NAME = "all-MiniLM-L6-v2"

_model = None


def get_model():
    global _model
    if _model is None:
        print(f"[embedder] Loading {MODEL_NAME}...")
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(MODEL_NAME)
        print(f"[embedder] Model loaded.")
    return _model


def ensure_embedding_column():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("ALTER TABLE feed_tweets ADD COLUMN embedding BLOB")
        conn.commit()
    except sqlite3.OperationalError:
        pass  # Column already exists
    conn.close()


def get_unembedded_tweets(limit: int = 500) -> list[dict]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT id, text FROM feed_tweets
        WHERE embedding IS NULL
          AND text IS NOT NULL
          AND length(text) > 20
        LIMIT ?
    """, (limit,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def embed_batch(texts: list[str]) -> np.ndarray:
    model = get_model()
    return model.encode(texts, batch_size=64, show_progress_bar=True, normalize_embeddings=True)


def save_embeddings(id_embedding_pairs: list[tuple]):
    conn = sqlite3.connect(DB_PATH)
    for tweet_id, emb in id_embedding_pairs:
        blob = emb.astype(np.float32).tobytes()
        conn.execute(
            "UPDATE feed_tweets SET embedding = ? WHERE id = ?",
            (blob, tweet_id)
        )
    conn.commit()
    conn.close()


def load_embedding(blob: bytes) -> np.ndarray:
    return np.frombuffer(blob, dtype=np.float32)


def embed_all(batch_size: int = 500):
    """Embed all tweets that don't have embeddings yet."""
    ensure_embedding_column()

    total_embedded = 0
    while True:
        tweets = get_unembedded_tweets(batch_size)
        if not tweets:
            break

        print(f"[embedder] Embedding {len(tweets)} tweets...")
        texts = [t["text"] for t in tweets]
        embeddings = embed_batch(texts)

        pairs = [(tweets[i]["id"], embeddings[i]) for i in range(len(tweets))]
        save_embeddings(pairs)
        total_embedded += len(tweets)
        print(f"[embedder] {total_embedded} tweets embedded so far")

    print(f"[embedder] Done. Total embedded: {total_embedded}")
    return total_embedded


def similarity_search(query: str, top_k: int = 10, min_likes: int = 50) -> list[dict]:
    """Find tweets most semantically similar to query."""
    model = get_model()
    q_emb = model.encode([query], normalize_embeddings=True)[0].astype(np.float32)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Load all embedded tweets with enough engagement
    rows = conn.execute("""
        SELECT id, text, author_handle, likes, retweets, bookmarks, views,
               engagement_rate, topic, hook_type, tweet_url, embedding
        FROM feed_tweets
        WHERE embedding IS NOT NULL
          AND likes >= ?
          AND is_retweet = 0
    """, (min_likes,)).fetchall()
    conn.close()

    if not rows:
        return []

    # Compute cosine similarities
    results = []
    for row in rows:
        emb = load_embedding(row["embedding"])
        score = float(np.dot(q_emb, emb))  # normalized → dot = cosine sim
        results.append({
            **dict(row),
            "similarity": score,
        })

    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results[:top_k]


def find_reply_inspiration(tweet_text: str, top_k: int = 5) -> list[dict]:
    """Find high-engagement tweets similar to a given tweet — for reply inspiration."""
    return similarity_search(tweet_text, top_k=top_k, min_likes=100)


def get_embedding_stats() -> dict:
    conn = sqlite3.connect(DB_PATH)
    total = conn.execute("SELECT COUNT(*) FROM feed_tweets").fetchone()[0]
    embedded = conn.execute("SELECT COUNT(*) FROM feed_tweets WHERE embedding IS NOT NULL").fetchone()[0]
    conn.close()
    return {"total": total, "embedded": embedded, "pending": total - embedded}


if __name__ == "__main__":
    if "--stats" in sys.argv:
        stats = get_embedding_stats()
        print(f"Tweets: {stats['total']:,} total, {stats['embedded']:,} embedded, {stats['pending']:,} pending")
    elif "--search" in sys.argv:
        idx = sys.argv.index("--search")
        query = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else "AI agents autonomous"
        results = similarity_search(query, top_k=5)
        print(f"\nTop 5 similar to: '{query}'")
        for i, r in enumerate(results, 1):
            print(f"\n{i}. @{r['author_handle']} [{r['likes']}L] sim={r['similarity']:.3f}")
            print(f"   {r['text'][:200]}")
    else:
        embed_all()
