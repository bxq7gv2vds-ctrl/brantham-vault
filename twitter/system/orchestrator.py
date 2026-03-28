"""
Orchestrator — the brain of the Twitter agent.

Assembles the full intelligence context for draft generation:
- Trending topics from topic_model
- Best performing hooks from style_fingerprints
- Content gaps (underrepresented topics)
- Similar high-performing tweets via FAISS
- Engagement signal from engagement_net

Exposes `build_context()` used by drafter.py.
Also runs the unified training pipeline: embed → topic → fingerprint → neural net.
"""
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

import sys
sys.path.insert(0, str(Path(__file__).parent))
from config import KG, DB_PATH, PATTERNS_DIR


# ─── Context assembly ────────────────────────────────────────────────────────

def build_context(date: str = None, top_n_similar: int = 8) -> dict:
    """
    Build the full intelligence context for draft generation.
    Returns a structured dict consumed by drafter.py.
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    ctx = {
        "date": date,
        "trending_topics": [],
        "content_gaps": [],
        "best_accounts": [],
        "top_similar_tweets": [],
        "style_exemplars": {},
        "corpus_stats": {},
        "model_status": {},
    }

    # 1. Trending topics
    try:
        from models.topic_model import get_trending_topics, get_status as topic_status
        ctx["trending_topics"] = get_trending_topics(days=7, top_n=5)
        ctx["model_status"]["topics"] = topic_status()
    except Exception as e:
        ctx["trending_topics"] = []
        ctx["model_status"]["topics"] = f"error: {e}"

    # 2. Content gaps (vs last 14 days of posted content)
    try:
        recent_posted = _get_recent_posted_texts(days=14)
        from models.topic_model import get_content_gaps
        ctx["content_gaps"] = get_content_gaps(recent_posted, top_n=3)
    except Exception:
        ctx["content_gaps"] = []

    # 3. Best accounts by engagement
    try:
        from models.style_fingerprint import get_best_accounts, get_status as fp_status
        ctx["best_accounts"] = get_best_accounts(n=5)
        ctx["model_status"]["fingerprints"] = fp_status()
    except Exception as e:
        ctx["best_accounts"] = []
        ctx["model_status"]["fingerprints"] = f"error: {e}"

    # 4. Top similar tweets (semantic search on recent trending terms)
    try:
        from pipeline.vector_store import search
        trending_query = _build_trending_query(ctx["trending_topics"])
        ctx["top_similar_tweets"] = search(trending_query, top_k=top_n_similar, min_likes=100)
        ctx["model_status"]["vector_store"] = "ok"
    except Exception as e:
        ctx["top_similar_tweets"] = []
        ctx["model_status"]["vector_store"] = f"error: {e}"

    # 5. Style exemplars per style type
    try:
        from models.style_fingerprint import get_style_exemplars
        for style in ["list", "hot_take", "prediction", "observation", "builder"]:
            examples = get_style_exemplars(style, n=3)
            if examples:
                ctx["style_exemplars"][style] = examples
    except Exception:
        pass

    # 6. Corpus stats
    ctx["corpus_stats"] = _get_corpus_stats()

    # 7. Engagement model status
    try:
        from models.engagement_net import get_status as eng_status
        ctx["model_status"]["engagement_net"] = eng_status()
    except Exception as e:
        ctx["model_status"]["engagement_net"] = f"error: {e}"

    return ctx


def build_context_for_prompt(date: str = None) -> str:
    """
    Return a formatted string for injection into the Claude prompt.
    Compact, structured, actionable.
    """
    ctx = build_context(date)

    lines = []

    # Corpus
    cs = ctx.get("corpus_stats", {})
    lines.append(f"CORPUS: {cs.get('total', 0):,} tweets | {cs.get('authors', 0)} accounts | {cs.get('embedded', 0):,} embedded")
    lines.append("")

    # Trending topics
    trends = ctx.get("trending_topics", [])
    if trends:
        lines.append("TRENDING TOPICS (last 7 days):")
        for t in trends[:5]:
            kw = ", ".join(t.get("keywords", [])[:5])
            lines.append(f"  • [{t.get('count', 0)} tweets] {kw} — avg {t.get('avg_likes', 0)} likes")
        lines.append("")

    # Content gaps
    gaps = ctx.get("content_gaps", [])
    if gaps:
        lines.append("CONTENT GAPS (popular but you haven't covered):")
        for g in gaps[:3]:
            kw = ", ".join(g.get("keywords", [])[:4])
            lines.append(f"  • {kw}")
        lines.append("")

    # Best accounts
    best = ctx.get("best_accounts", [])
    if best:
        lines.append("TOP ACCOUNTS BY ENGAGEMENT:")
        for a in best[:5]:
            eng = a.get("engagement", {})
            pillars = ", ".join(a.get("content_pillars", [])[:4])
            lines.append(
                f"  @{a['handle']}: p90={eng.get('p90_likes', 0):.0f} likes | "
                f"topics: {pillars}"
            )
        lines.append("")

    # Top similar tweets
    similars = ctx.get("top_similar_tweets", [])
    if similars:
        lines.append("HIGH-PERFORMING SIMILAR TWEETS:")
        for s in similars[:5]:
            text_preview = s.get("text", "")[:100].replace("\n", " ")
            lines.append(
                f"  [{s.get('likes', 0)} likes @{s.get('author_handle', '')}] "
                f"{text_preview}..."
            )
        lines.append("")

    # Style exemplars
    exemplars = ctx.get("style_exemplars", {})
    if exemplars:
        lines.append("WINNING HOOKS BY STYLE:")
        for style, hooks in list(exemplars.items())[:4]:
            if hooks:
                lines.append(f"  [{style.upper()}] {hooks[0][:80]}")
        lines.append("")

    # Model status
    status = ctx.get("model_status", {})
    lines.append("MODEL STATUS: " + " | ".join(f"{k}={v}" for k, v in status.items()))

    return "\n".join(lines)


# ─── Training pipeline ───────────────────────────────────────────────────────

def train_all(force: bool = False) -> dict:
    """
    Full training pipeline:
    1. Embed any unembedded tweets
    2. Rebuild FAISS index
    3. Train topic model (BERTopic)
    4. Build style fingerprints
    5. Train engagement net (PyTorch)
    """
    results = {}
    start = datetime.now()

    print("\n=== Orchestrator: full training pipeline ===\n")

    # Step 1: Embed
    print("1/5 Embedding unembedded tweets...")
    try:
        from embedder import embed_all
        embed_all()
        results["embed"] = "ok"
    except Exception as e:
        results["embed"] = f"error: {e}"
        print(f"  [WARN] {e}")

    # Step 2: FAISS index
    print("2/5 Rebuilding FAISS index...")
    try:
        from pipeline.vector_store import build_index
        build_index(force=True)
        results["faiss"] = "ok"
    except Exception as e:
        results["faiss"] = f"error: {e}"
        print(f"  [WARN] {e}")

    # Step 3: Topic model
    print("3/5 Training topic model (BERTopic)...")
    try:
        from models.topic_model import train as train_topics
        topic_result = train_topics()
        results["topics"] = topic_result.get("n_topics", "ok")
    except Exception as e:
        results["topics"] = f"error: {e}"
        print(f"  [WARN] {e}")

    # Step 4: Style fingerprints
    print("4/5 Building style fingerprints...")
    try:
        from models.style_fingerprint import build_fingerprints
        fp_result = build_fingerprints()
        results["fingerprints"] = fp_result.get("n_accounts", "ok")
    except Exception as e:
        results["fingerprints"] = f"error: {e}"
        print(f"  [WARN] {e}")

    # Step 5: Neural net
    print("5/5 Training engagement neural net...")
    try:
        from models.engagement_net import train as train_net
        net_result = train_net(epochs=100)
        results["engagement_net"] = net_result.get("best_val_loss", "ok")
    except Exception as e:
        results["engagement_net"] = f"error: {e}"
        print(f"  [WARN] {e}")

    elapsed = (datetime.now() - start).total_seconds()
    results["elapsed_s"] = round(elapsed, 1)
    results["trained_at"] = datetime.now().isoformat()

    # Save training log
    log_path = PATTERNS_DIR / f"training-{datetime.now().strftime('%Y-%m-%d')}.json"
    log_path.write_text(json.dumps(results, indent=2))

    print(f"\n=== Training complete in {elapsed:.0f}s ===")
    print(json.dumps(results, indent=2))
    return results


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _get_recent_posted_texts(days: int = 14) -> list[str]:
    """Get texts of recently posted tweets."""
    since = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("""
        SELECT content FROM posted_tweets
        WHERE time_posted >= ?
        ORDER BY time_posted DESC LIMIT 50
    """, (since,)).fetchall()
    conn.close()
    return [r[0] for r in rows if r[0]]


def _build_trending_query(topics: list[dict]) -> str:
    """Build a search query from trending topic keywords."""
    if not topics:
        return "AI agents LLM builder"
    all_kw = []
    for t in topics[:3]:
        all_kw.extend(t.get("keywords", [])[:3])
    return " ".join(all_kw[:10]) if all_kw else "AI builder tool"


def _get_corpus_stats() -> dict:
    try:
        conn = sqlite3.connect(DB_PATH)
        total = conn.execute("SELECT COUNT(*) FROM feed_tweets").fetchone()[0]
        authors = conn.execute(
            "SELECT COUNT(DISTINCT author_handle) FROM feed_tweets"
        ).fetchone()[0]
        embedded = conn.execute(
            "SELECT COUNT(*) FROM feed_tweets WHERE embedding IS NOT NULL"
        ).fetchone()[0]
        conn.close()
        return {"total": total, "authors": authors, "embedded": embedded}
    except Exception:
        return {}


def get_full_status() -> str:
    """Print full system status."""
    lines = ["=== Twitter Agent — System Status ===", ""]

    # Corpus
    stats = _get_corpus_stats()
    lines.append(f"Corpus:     {stats.get('total', 0):,} tweets | {stats.get('authors', 0)} accounts | {stats.get('embedded', 0):,} embedded")

    # Model status
    try:
        from models.topic_model import get_status as ts
        lines.append(f"Topics:     {ts()}")
    except Exception:
        lines.append("Topics:     not available")

    try:
        from models.style_fingerprint import get_status as fs
        lines.append(f"Fingerprints: {fs()}")
    except Exception:
        lines.append("Fingerprints: not available")

    try:
        from models.engagement_net import get_status as es
        lines.append(f"Neural net: {es()}")
    except Exception:
        lines.append("Neural net: not available")

    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "train":
        train_all()
    elif len(sys.argv) > 1 and sys.argv[1] == "context":
        print(build_context_for_prompt())
    else:
        print(get_full_status())
