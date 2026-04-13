"""
Vector Store — FAISS-backed semantic similarity search over tweet corpus.
Persisted to disk, incremental updates.
"""
import numpy as np
import faiss
import sqlite3
import pickle
from pathlib import Path
from typing import Optional

from config import KG, DB_PATH

INDEX_PATH = KG / "faiss.index"
ID_MAP_PATH = KG / "faiss_id_map.pkl"  # faiss_idx → tweet_id
EMBEDDING_DIM = 384


def _get_model():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("all-MiniLM-L6-v2")


def build_index(force: bool = False) -> faiss.Index:
    """Build FAISS index from all embedded tweets in DB."""
    if INDEX_PATH.exists() and not force:
        return load_index()

    print("[vector_store] Building FAISS index...")
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("""
        SELECT id, embedding FROM feed_tweets
        WHERE embedding IS NOT NULL
    """).fetchall()
    conn.close()

    if not rows:
        print("[vector_store] No embeddings found. Run embed first.")
        index = faiss.IndexFlatIP(EMBEDDING_DIM)
        return index

    ids = []
    vecs = []
    for tweet_id, blob in rows:
        emb = np.frombuffer(blob, dtype=np.float32)
        if len(emb) == EMBEDDING_DIM:
            ids.append(tweet_id)
            vecs.append(emb)

    matrix = np.stack(vecs).astype(np.float32)
    faiss.normalize_L2(matrix)

    index = faiss.IndexFlatIP(EMBEDDING_DIM)
    index.add(matrix)

    faiss.write_index(index, str(INDEX_PATH))
    with open(ID_MAP_PATH, "wb") as f:
        pickle.dump(ids, f)

    print(f"[vector_store] Index built: {len(ids):,} vectors")
    return index


def load_index():
    if not INDEX_PATH.exists():
        return build_index()
    index = faiss.read_index(str(INDEX_PATH))
    return index


def load_id_map() -> list[str]:
    if not ID_MAP_PATH.exists():
        return []
    with open(ID_MAP_PATH, "rb") as f:
        return pickle.load(f)


def search(query: str, top_k: int = 10, min_likes: int = 50) -> list[dict]:
    """Semantic search over tweet corpus."""
    model = _get_model()
    q_vec = model.encode([query], normalize_embeddings=True)[0].astype(np.float32)

    index = load_index()
    id_map = load_id_map()

    if index.ntotal == 0:
        return []

    scores, indices = index.search(q_vec.reshape(1, -1), min(top_k * 3, index.ntotal))

    # Fetch tweet details
    tweet_ids = [id_map[i] for i in indices[0] if i < len(id_map)]
    if not tweet_ids:
        return []

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    placeholders = ",".join(["?" for _ in tweet_ids])
    rows = conn.execute(f"""
        SELECT id, text, author_handle, likes, retweets, bookmarks,
               views, engagement_rate, topic, hook_type, tweet_url
        FROM feed_tweets
        WHERE id IN ({placeholders}) AND likes >= ?
    """, tweet_ids + [min_likes]).fetchall()
    conn.close()

    results = []
    for i, idx in enumerate(indices[0]):
        if idx >= len(id_map):
            continue
        tid = id_map[idx]
        for row in rows:
            if row["id"] == tid:
                results.append({**dict(row), "similarity": float(scores[0][i])})
                break

    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results[:top_k]


def embed_text(text: str) -> np.ndarray:
    model = _get_model()
    return model.encode([text], normalize_embeddings=True)[0].astype(np.float32)
