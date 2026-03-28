"""
Deep style analysis — goes beyond DNA basics.
For each account extracts:
  - Hook patterns (first line of top tweets)
  - Format breakdown (thread, one-liner, list, story, hot-take)
  - Emotional register (humor, authority, vulnerability, aggression)
  - Top 10 performing tweets verbatim
  - Posting rhythm (time of day)
  - Viral formula (what structure their 10K+ tweets share)

Output: /Users/paul/twitter-agent/knowledge-graph/reply_dna/{handle}_deep.md
        (readable in Obsidian + injectable in prompts)
"""
import json
import re
import sqlite3
from collections import Counter
from datetime import datetime
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))
from db import get_conn
from config import KG

OUT_DIR = KG / "reply_dna"
OUT_DIR.mkdir(parents=True, exist_ok=True)

TARGETS = {
    "Hesamation":    {"niche": "ai_builder",         "lang": "en"},
    "poetengineer__":{"niche": "ai_engineer",        "lang": "en"},
    "gregisenberg":  {"niche": "community_builder",  "lang": "en"},
    "levelsio":      {"niche": "indie_builder",      "lang": "en"},
    "buccocapital":  {"niche": "finance_builder",    "lang": "en"},
    "BrivaelFr":     {"niche": "fr_builder",         "lang": "fr"},
    "Frenchie_":     {"niche": "fr_crypto_builder",  "lang": "fr"},
}


def get_tweets(handle: str) -> list[dict]:
    conn = get_conn()
    rows = conn.execute("""
        SELECT text, likes, retweets, bookmarks, views, engagement_rate,
               tweet_url, created_at
        FROM feed_tweets
        WHERE LOWER(author_handle) = LOWER(?)
          AND is_retweet = 0
          AND LENGTH(text) > 20
        ORDER BY likes DESC
    """, (handle,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def classify_format(text: str) -> str:
    t = text.strip()
    lines = [l for l in t.splitlines() if l.strip()]

    if len(lines) >= 3 and any(re.match(r'^\d+[\.\)—\-]', l.strip()) for l in lines[1:]):
        return "list"
    if "\n" in t and len(t) > 200 and lines[0].endswith(":"):
        return "thread_opener"
    if len(t) < 100 and "\n" not in t:
        return "one_liner"
    if any(w in t.lower()[:60] for w in ["i built", "i shipped", "i made", "j'ai", "we launched", "just shipped"]):
        return "builder_story"
    if any(w in t.lower()[:80] for w in ["hot take", "unpopular", "wrong", "actually", "nobody", "stop saying"]):
        return "hot_take"
    if t.upper()[:40] == t[:40] and len(t) > 30:
        return "breaking_news"
    if "?" in t[:80]:
        return "question"
    if len(lines) >= 4:
        return "thread_opener"
    return "statement"


def extract_hook(text: str) -> str:
    """First meaningful line, stripped of @mentions."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    if not lines:
        return ""
    first = re.sub(r'^@\w+\s*', '', lines[0]).strip()
    return first[:120]


def classify_register(text: str) -> str:
    t = text.lower()
    if any(w in t for w in ["lol", "😂", "lmao", "bruh", "bro", "mdr", "wtf", "💀"]):
        return "humor"
    if any(w in t for w in ["i built", "j'ai", "we shipped", "i made", "my product", "my app"]):
        return "builder_flex"
    if any(w in t for w in ["wrong", "stop", "actually", "hot take", "unpopular", "nobody"]):
        return "authority_challenge"
    if any(w in t for w in ["scary", "wild", "insane", "crazy", "wait wait", "holy"]):
        return "shock_value"
    if any(w in t for w in ["i was wrong", "i failed", "mistake", "lesson", "learned"]):
        return "vulnerability"
    if any(w in t for w in ["here's how", "step 1", "guide", "tutorial", "learn"]):
        return "educational"
    return "observation"


def analyze(handle: str, meta: dict) -> dict:
    tweets = get_tweets(handle)
    if len(tweets) < 5:
        return {"handle": handle, "error": f"only {len(tweets)} tweets"}

    n = len(tweets)
    top = tweets[:max(10, n // 5)]    # top 20%
    viral = [t for t in tweets if t.get("likes", 0) >= 1000]

    # Format distribution
    all_formats = Counter(classify_format(t["text"]) for t in tweets)
    top_formats = Counter(classify_format(t["text"]) for t in top)

    # Emotional register distribution (top tweets)
    top_register = Counter(classify_register(t["text"]) for t in top)

    # Hook patterns from viral/top tweets
    hooks = [extract_hook(t["text"]) for t in top if extract_hook(t["text"])]

    # Lengths
    lengths = [len(t["text"]) for t in tweets]
    avg_len = round(sum(lengths) / len(lengths))
    top_lengths = [len(t["text"]) for t in top]
    avg_top_len = round(sum(top_lengths) / len(top_lengths)) if top_lengths else 0

    # Vocabulary (content words from top tweets)
    stopwords = {
        "the","a","an","is","it","in","on","at","to","for","of","and","or",
        "but","not","this","that","with","you","i","we","he","she","they",
        "my","your","our","its","be","are","was","were","have","has","had",
        "do","does","did","will","would","can","could","should","may","might",
        "just","so","as","by","from","up","about","than","more","also","yes",
        "no","le","la","les","de","du","un","une","des","et","en","je","tu",
        "il","nous","vous","ils","est","sont","pas","plus","très","bien","ça",
        "ce","qui","que","https","http","t.co","rt","via","re","on","au","par",
        "if","then","all","when","what","how","why","too","out","get","got",
        "now","here","there","been","into","over","after","before","because",
    }
    words = []
    for t in top:
        clean = re.sub(r'https?://\S+', '', t["text"])
        clean = re.sub(r'@\w+', '', clean)
        for w in re.findall(r"\b[a-zA-Zàâçéèêëîïôùûü']{3,}\b", clean.lower()):
            if w not in stopwords and not w.startswith("http"):
                words.append(w)
    vocab = [w for w, _ in Counter(words).most_common(20)]

    # Best tweets verbatim (top 10)
    best = []
    for t in tweets[:10]:
        best.append({
            "text": t["text"][:400],
            "likes": t.get("likes", 0),
            "format": classify_format(t["text"]),
            "register": classify_register(t["text"]),
            "hook": extract_hook(t["text"])[:100],
        })

    # Viral formula (what top tweets have in common)
    viral_formats = Counter(classify_format(t["text"]) for t in viral) if viral else {}
    viral_registers = Counter(classify_register(t["text"]) for t in viral) if viral else {}

    return {
        "handle": handle,
        "niche": meta["niche"],
        "lang": meta["lang"],
        "total_tweets": n,
        "viral_count": len(viral),  # tweets > 1K likes
        "avg_likes": round(sum(t.get("likes",0) for t in tweets) / n),
        "max_likes": max(t.get("likes",0) for t in tweets),
        "avg_length_all": avg_len,
        "avg_length_top": avg_top_len,
        "format_distribution": dict(all_formats.most_common()),
        "top_formats": dict(top_formats.most_common(4)),
        "top_registers": dict(top_register.most_common(4)),
        "viral_formats": dict(viral_formats.most_common(3)),
        "viral_registers": dict(viral_registers.most_common(3)),
        "vocabulary": vocab,
        "top_hooks": hooks[:8],
        "best_tweets": best,
    }


def write_md(handle: str, d: dict):
    """Write a human-readable Obsidian note + machine-usable JSON."""
    if d.get("error"):
        print(f"  [skip] {d['error']}")
        return

    # JSON for machine use
    json_path = OUT_DIR / f"{handle.lower()}_deep.json"
    json_path.write_text(json.dumps(d, indent=2, ensure_ascii=False))

    # Markdown for Obsidian reading
    lines = [
        f"---",
        f"handle: {handle}",
        f"niche: {d['niche']}",
        f"lang: {d['lang']}",
        f"avg_likes: {d['avg_likes']}",
        f"max_likes: {d['max_likes']}",
        f"---",
        f"",
        f"# Style DNA — @{handle}",
        f"",
        f"**Niche:** {d['niche']} | **Lang:** {d['lang']} | **Tweets analysés:** {d['total_tweets']}",
        f"**Avg likes:** {d['avg_likes']:,} | **Max:** {d['max_likes']:,} | **Viral (>1K):** {d['viral_count']}",
        f"",
        f"## Longueur",
        f"- Tous tweets: **{d['avg_length_all']} chars** avg",
        f"- Top tweets (20%): **{d['avg_length_top']} chars** avg",
        f"",
        f"## Formats (tous tweets)",
    ]
    for fmt, n in sorted(d["format_distribution"].items(), key=lambda x: -x[1]):
        pct = round(n / d["total_tweets"] * 100)
        lines.append(f"- {fmt}: {n} ({pct}%)")

    lines += ["", "## Formats des top tweets (20% les plus likés)"]
    for fmt, n in d["top_formats"].items():
        lines.append(f"- **{fmt}**: {n}")

    lines += ["", "## Registre émotionnel (top tweets)"]
    for reg, n in d["top_registers"].items():
        lines.append(f"- {reg}: {n}")

    if d.get("viral_formats"):
        lines += ["", "## Formule virale (tweets >1K likes)"]
        lines.append(f"- Formats: {', '.join(d['viral_formats'].keys())}")
        lines.append(f"- Registres: {', '.join(d.get('viral_registers', {}).keys())}")

    lines += ["", "## Vocabulaire signature"]
    lines.append(", ".join(d["vocabulary"][:15]))

    if d.get("top_hooks"):
        lines += ["", "## Hooks (première ligne des top tweets)"]
        for h in d["top_hooks"][:6]:
            if h:
                lines.append(f'- "{h}"')

    lines += ["", "## Top 10 tweets verbatim", ""]
    for i, t in enumerate(d["best_tweets"], 1):
        lines += [
            f"### {i}. [{t['likes']:,}L | {t['format']} | {t['register']}]",
            f"```",
            t["text"],
            f"```",
            f"",
        ]

    md_path = OUT_DIR / f"{handle.lower()}_deep.md"
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  → {md_path.name}")


def run():
    print(f"\n=== Deep Analysis — {len(TARGETS)} accounts ===\n")
    for handle, meta in TARGETS.items():
        tweets = get_tweets(handle)
        print(f"@{handle}: {len(tweets)} tweets...", end=" ", flush=True)
        if len(tweets) < 5:
            print(f"SKIP (not enough data — scraping in background)")
            continue
        d = analyze(handle, meta)
        print(f"ok ({d.get('avg_likes',0):,} avg likes, {d.get('viral_count',0)} viral)")
        write_md(handle, d)

    print(f"\nFiles → {OUT_DIR}")


if __name__ == "__main__":
    run()
