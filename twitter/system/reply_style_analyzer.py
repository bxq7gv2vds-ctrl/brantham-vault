"""
Reply Style Analyzer — extracts the reply DNA from accounts who blew up.

Analyzes HOW they reply (not what they tweet originally):
- Opening patterns
- Length distribution
- Tone / vocabulary
- Structure (question, statement, proof, one-liner)
- Their best performing replies as exemplars

Generates a reply_dna.json per account, used by reply_guy.py as style reference.

Usage:
  python reply_style_analyzer.py                    — analyze all reference accounts
  python reply_style_analyzer.py --account levelsio — single account
  python reply_style_analyzer.py --scrape           — scrape replies first, then analyze
  python reply_style_analyzer.py --show             — print DNA cards
"""
import json
import re
import subprocess
import time
from collections import Counter
from pathlib import Path
from datetime import datetime

import sys
sys.path.insert(0, str(Path(__file__).parent))
from config import CLIX, KG
from db import init_db, get_conn
from scraper import classify_tweet, run_clix

DNA_DIR = KG / "reply_dna"
DNA_DIR.mkdir(parents=True, exist_ok=True)

# Reference accounts — people who blew up in AI/builder/crypto
REFERENCE_ACCOUNTS = {
    "levelsio": {
        "niche": "indie_builder",
        "lang": "en",
        "why": "The OG solo builder. Direct, no hedge, provocateur. Built Nomad List, RemoteOK.",
    },
    "swyx": {
        "niche": "ai_dev",
        "lang": "en",
        "why": "AI educator. Adds real depth, always a specific example or counter. Thoughtful.",
    },
    "Frenchiee": {
        "niche": "crypto_builder_fr",
        "lang": "fr",
        "why": "French crypto/builder. Grew fast. Writes short and punchy in French.",
    },
    "melvynx": {
        "niche": "ai_builder_fr",
        "lang": "fr",
        "why": "French AI builder. Exploded 2024-2025. Very close profile to Paul.",
    },
    "gregisenberg": {
        "niche": "community_builder",
        "lang": "en",
        "why": "Community + startups. Sharp replies, adds a framework or number every time.",
    },
}


# ─── Scraping replies ─────────────────────────────────────────────────────────

def scrape_account_replies(handle: str, n_windows: int = 6) -> int:
    """Scrape reply tweets for an account using time-windowed search."""
    from datetime import date
    from dateutil.relativedelta import relativedelta

    stored = 0
    today = date.today()

    for i in range(n_windows):
        end = today - relativedelta(months=i)
        start = end - relativedelta(months=1)
        since = start.strftime("%Y-%m-%d")
        until = end.strftime("%Y-%m-%d")

        query = f"from:{handle} filter:replies since:{since} until:{until}"
        tweets = run_clix(["search", query, "--json", "-n", "50"])

        for t in tweets:
            if t.get("text", "").startswith("@") or "in_reply_to" in t:
                t = classify_tweet(t)
                conn = get_conn()
                try:
                    eng = t.get("engagement", {})
                    views = eng.get("views", 1) or 1
                    total_eng = (eng.get("likes", 0) + eng.get("retweets", 0)
                                 + eng.get("replies", 0) + eng.get("bookmarks", 0))
                    eng_rate = round(total_eng / views * 100, 4)
                    conn.execute("""
                        INSERT OR REPLACE INTO feed_tweets
                        (id, text, author_handle, created_at, likes, retweets,
                         replies, bookmarks, views, engagement_rate, is_retweet,
                         tweet_url, topic, hook_type)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """, (
                        t["id"], t.get("text", ""), handle, t.get("created_at", ""),
                        eng.get("likes", 0), eng.get("retweets", 0),
                        eng.get("replies", 0), eng.get("bookmarks", 0),
                        eng.get("views", 0), eng_rate, 0,
                        t.get("tweet_url", ""), t.get("topic", ""), t.get("hook_type", ""),
                    ))
                    conn.commit()
                    stored += 1
                except Exception:
                    pass
                finally:
                    conn.close()

        print(f"  [{handle}] {since}→{until}: {len(tweets)} tweets")
        time.sleep(2.5)

    return stored


# ─── Analysis ─────────────────────────────────────────────────────────────────

def _is_reply(text: str) -> bool:
    """Heuristic: is this tweet a reply?"""
    return (
        text.startswith("@")
        or bool(re.match(r'^[A-Z][a-z]', text) and "@" in text[:40])
        or ".@" in text[:10]
    )


def get_all_tweets(handle: str, min_likes: int = 0) -> list[dict]:
    """Get all non-RT tweets from DB for an account."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT text, likes, retweets, bookmarks, views, engagement_rate,
               tweet_url, created_at, topic, hook_type
        FROM feed_tweets
        WHERE LOWER(author_handle) = LOWER(?)
          AND is_retweet = 0
          AND likes >= ?
        ORDER BY likes DESC
    """, (handle, min_likes)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_reply_tweets(handle: str, min_likes: int = 0) -> list[dict]:
    """Get reply tweets from DB for an account (falls back to all if not enough)."""
    all_tweets = get_all_tweets(handle, min_likes)
    replies = [t for t in all_tweets if _is_reply(t.get("text", ""))]
    # If < 10 replies detected, use all tweets for style analysis
    return replies if len(replies) >= 10 else all_tweets


def _extract_opening(text: str) -> str:
    """First 3 words of reply (after the @mention)."""
    # Remove leading @mention
    text = re.sub(r'^@\w+\s*', '', text).strip()
    words = text.split()[:3]
    return " ".join(words).lower()


def _classify_structure(text: str) -> str:
    """Classify reply structure."""
    # Remove leading @mention
    clean = re.sub(r'^@\w+\s*', '', text).strip()

    if clean.endswith("?"):
        return "question"
    if re.match(r'^\d+[\.\)]\s', clean) or re.search(r'\n\d+[\.\)]\s', clean):
        return "list"
    if len(clean) < 80:
        return "one_liner"
    if any(w in clean.lower() for w in ["i built", "i made", "j'ai", "i shipped", "je"]):
        return "personal_proof"
    if any(w in clean.lower() for w in ["actually", "actually,", "but wait", "wrong", "non,"]):
        return "counter"
    if ":" in clean[:60] and "\n" in clean:
        return "structured_take"
    return "statement"


def _extract_vocabulary(texts: list[str], top_n: int = 30) -> list[str]:
    """Most distinctive words in their replies."""
    stopwords = {
        "the", "a", "an", "is", "it", "in", "on", "at", "to", "for", "of",
        "and", "or", "but", "not", "this", "that", "with", "you", "i", "we",
        "he", "she", "they", "my", "your", "our", "its", "be", "are", "was",
        "were", "have", "has", "had", "do", "does", "did", "will", "would",
        "can", "could", "should", "may", "might", "must", "if", "so", "as",
        "by", "from", "up", "about", "than", "more", "just", "also", "yes",
        "no", "le", "la", "les", "de", "du", "un", "une", "des", "et", "en",
        "je", "tu", "il", "nous", "vous", "ils", "est", "sont", "c'est",
        "pas", "plus", "très", "bien", "ça", "ce", "qui", "que", "https",
        "http", "t.co", "rt", "via", "re:", "on", "au", "aux", "par",
    }
    words = []
    for text in texts:
        clean = re.sub(r'^@\w+\s*', '', text).strip()
        clean = re.sub(r'https?://\S+', '', clean)
        for w in re.findall(r'\b[a-zA-Zàâçéèêëîïôùûü]{3,}\b', clean.lower()):
            if w not in stopwords:
                words.append(w)
    return [w for w, _ in Counter(words).most_common(top_n)]


def analyze_account(handle: str, meta: dict) -> dict:
    """Build the reply DNA for an account."""
    tweets = get_reply_tweets(handle)

    if len(tweets) < 5:
        return {"handle": handle, "error": f"only {len(tweets)} reply tweets found"}

    # Split into high-performing and average
    sorted_tweets = sorted(tweets, key=lambda x: x.get("likes", 0), reverse=True)
    top_replies = sorted_tweets[:min(30, len(sorted_tweets) // 3 + 5)]
    all_texts = [t["text"] for t in tweets]
    top_texts = [t["text"] for t in top_replies]

    # Length analysis
    lengths = [len(re.sub(r'^@\w+\s*', '', t.get("text", "")).strip()) for t in tweets]
    avg_len = sum(lengths) / len(lengths)
    med_len = sorted(lengths)[len(lengths) // 2]

    # Opening patterns (from top replies)
    openings = Counter(_extract_opening(t["text"]) for t in top_replies)
    top_openings = [o for o, _ in openings.most_common(8) if o]

    # Structure distribution (all replies)
    structures = Counter(_classify_structure(t["text"]) for t in tweets)
    structure_pct = {k: round(v / len(tweets) * 100) for k, v in structures.most_common()}

    # Top structure in HIGH-performing replies
    top_structures = Counter(_classify_structure(t["text"]) for t in top_replies)

    # Vocabulary signature
    vocab_all = _extract_vocabulary(all_texts, top_n=40)
    vocab_top = _extract_vocabulary(top_texts, top_n=25)
    # Distinctive words = appear in top but maybe less in all
    distinctive = [w for w in vocab_top if w in vocab_all[:60]][:15]

    # Best exemplar replies (for direct injection into prompts)
    exemplars = []
    for t in top_replies[:10]:
        clean = re.sub(r'^@\w+\s*', '', t["text"]).strip()
        if len(clean) > 20:
            exemplars.append({
                "text": clean,
                "likes": t.get("likes", 0),
                "structure": _classify_structure(t["text"]),
                "length": len(clean),
            })

    # Tone markers from top replies
    tone_words = []
    for t in top_texts:
        clean = re.sub(r'^@\w+\s*', '', t).lower()
        if any(w in clean for w in ["actually", "non,", "mais", "wait"]):
            tone_words.append("direct_counter")
        if any(w in clean for w in ["i built", "j'ai", "we shipped", "i shipped"]):
            tone_words.append("proof")
        if "?" in clean[-20:]:
            tone_words.append("ends_with_question")
        if len(clean) < 100:
            tone_words.append("short")

    tone_dist = dict(Counter(tone_words))

    # Build DNA card
    dna = {
        "handle": handle,
        "niche": meta.get("niche", ""),
        "lang": meta.get("lang", "en"),
        "why_reference": meta.get("why", ""),
        "sample_size": len(tweets),
        "top_n_analyzed": len(top_replies),
        "avg_reply_length": round(avg_len),
        "median_reply_length": med_len,
        "length_guidance": (
            "very short (<80 chars)" if med_len < 80
            else "short (80-150 chars)" if med_len < 150
            else "medium (150-250 chars)"
        ),
        "structure_distribution": structure_pct,
        "winning_structures": [s for s, _ in top_structures.most_common(3)],
        "opening_patterns": top_openings,
        "vocabulary_signature": distinctive,
        "tone_markers": tone_dist,
        "exemplars": exemplars[:8],
        "analyzed_at": datetime.now().isoformat(),
    }

    return dna


def build_style_prompt_block(dna: dict) -> str:
    """Convert DNA into a prompt-injectable style block."""
    if dna.get("error"):
        return f"[{dna['handle']} DNA not available: {dna['error']}]"

    lines = [
        f"### Style @{dna['handle']} ({dna['niche']}, {dna['lang']})",
        f"Pourquoi référence: {dna['why_reference']}",
        f"Longueur typique: {dna['length_guidance']} (moy={dna['avg_reply_length']}c)",
        f"Structures gagnantes: {', '.join(dna['winning_structures'][:3])}",
    ]

    if dna.get("vocabulary_signature"):
        lines.append(f"Vocabulaire signature: {', '.join(dna['vocabulary_signature'][:10])}")

    if dna.get("opening_patterns"):
        examples = [f'"{o}"' for o in dna["opening_patterns"][:4] if o]
        lines.append(f"Comment il commence: {', '.join(examples)}")

    if dna.get("exemplars"):
        lines.append("Meilleures replies:")
        for ex in dna["exemplars"][:4]:
            lines.append(f'  [{ex["likes"]}L | {ex["structure"]}] "{ex["text"][:150]}"')

    return "\n".join(lines)


# ─── Main ─────────────────────────────────────────────────────────────────────

def run(accounts: list[str] = None, scrape_first: bool = False) -> dict:
    init_db()
    accounts = accounts or list(REFERENCE_ACCOUNTS.keys())
    all_dna = {}

    for handle in accounts:
        meta = REFERENCE_ACCOUNTS.get(handle, {})
        print(f"\n[analyzer] @{handle} — {meta.get('niche', '')}...")

        if scrape_first:
            print(f"  Scraping replies...")
            n = scrape_account_replies(handle, n_windows=6)
            print(f"  → {n} replies scraped")

        tweets = get_reply_tweets(handle)
        print(f"  {len(tweets)} reply tweets in DB")

        if len(tweets) < 5:
            print(f"  [skip] Not enough data. Run with --scrape first.")
            all_dna[handle] = {"handle": handle, "error": "insufficient_data"}
            continue

        dna = analyze_account(handle, meta)
        all_dna[handle] = dna

        # Save individual DNA file
        path = DNA_DIR / f"{handle.lower()}.json"
        path.write_text(json.dumps(dna, indent=2, ensure_ascii=False))
        print(f"  → DNA saved: {path}")
        print(f"  Structures: {dna.get('structure_distribution', {})}")
        print(f"  Winning: {dna.get('winning_structures', [])}")
        print(f"  Avg length: {dna.get('avg_reply_length', '?')} chars")
        print(f"  Vocab: {', '.join(dna.get('vocabulary_signature', [])[:8])}")

    # Save combined
    combined_path = DNA_DIR / "combined.json"
    combined_path.write_text(json.dumps(all_dna, indent=2, ensure_ascii=False))
    print(f"\n[analyzer] Combined DNA → {combined_path}")

    return all_dna


def load_dna(handles: list[str] = None) -> dict:
    """Load DNA cards from disk."""
    dna = {}
    handles = handles or list(REFERENCE_ACCOUNTS.keys())
    for h in handles:
        path = DNA_DIR / f"{h.lower()}.json"
        if path.exists():
            try:
                dna[h] = json.loads(path.read_text())
            except Exception:
                pass
    return dna


def build_combined_style_prompt(handles: list[str] = None) -> str:
    """Build the full style reference block for injection into reply prompts."""
    dna = load_dna(handles)
    if not dna:
        return ""

    lines = ["## STYLE DNA — Comptes de référence qui ont explosé\n"]
    lines.append("Inspire-toi de COMMENT ils écrivent, pas de ce qu'ils disent.\n")

    for handle, d in dna.items():
        if not d.get("error"):
            lines.append(build_style_prompt_block(d))
            lines.append("")

    return "\n".join(lines)


def show(handles: list[str] = None):
    dna = load_dna(handles)
    if not dna:
        print("No DNA files found. Run: python reply_style_analyzer.py")
        return
    for handle, d in dna.items():
        if d.get("error"):
            print(f"\n@{handle}: {d['error']}")
        else:
            print(f"\n{'='*60}")
            print(build_style_prompt_block(d))


if __name__ == "__main__":
    accounts = None
    scrape = False
    show_mode = False

    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--account" and i + 1 < len(args):
            accounts = [args[i + 1]]
        if a == "--scrape":
            scrape = True
        if a == "--show":
            show_mode = True

    if show_mode:
        show(accounts)
    else:
        run(accounts=accounts, scrape_first=scrape)
