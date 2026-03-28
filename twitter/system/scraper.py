"""
Scraper Agent — fetches Twitter feed via clix, stores in SQLite + vault digest.
Run 3x/day: 08:00, 13:00, 19:00
"""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from config import CLIX, DIGESTS
from db import init_db, upsert_feed_tweet, get_top_feed_tweets


SEARCH_KEYWORDS = [
    "AI agents",
    "Claude Code",
    "LLM",
    "agentic AI",
    "automation pipeline",
    "building in public",
    "indie hacker",
]

NICHE_ACCOUNTS = [
    "levelsio", "swyx", "steipete", "karpathy", "alexalbert__",
    "buccocapital", "RoundtableSpace", "_akhaliq", "therundownai",
    "noahzweben", "poetengineer__", "Frenchiee", "melvynx",
    "0xmaxou", "thismacapital",
]


def run_clix(args: list[str]) -> list[dict]:
    cmd = [CLIX] + args
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"[clix error] {result.stderr[:200]}")
        return []
    try:
        data = json.loads(result.stdout)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def scrape_feed(n: int = 80) -> list[dict]:
    print(f"[scraper] Fetching feed ({n} tweets)...")
    return run_clix(["feed", "--json", "-n", str(n)])


def scrape_search(keyword: str, n: int = 20) -> list[dict]:
    print(f"[scraper] Searching: {keyword}")
    return run_clix(["search", keyword, "--json", "-n", str(n)])


def scrape_account(handle: str, n: int = 5) -> list[dict]:
    print(f"[scraper] Account: @{handle}")
    # syntax: clix user <handle> tweets <handle> --json -n N
    return run_clix(["user", handle, "tweets", handle, "--json", "-n", str(n)])


def classify_tweet(tweet: dict) -> dict:
    text = (tweet.get("text") or "").lower()
    eng = tweet.get("engagement", {})

    # Topic detection
    topic = "other"
    if any(w in text for w in ["claude", "anthropic", "llm", "gpt", "gemini", "openai"]):
        topic = "llm_models"
    elif any(w in text for w in ["agent", "agentic", "autonomous", "pipeline", "workflow"]):
        topic = "ai_agents"
    elif any(w in text for w in ["build", "built", "shipped", "launched", "code"]):
        topic = "builders"
    elif any(w in text for w in ["automation", "scraping", "scraper", "deploy"]):
        topic = "automation"
    elif any(w in text for w in ["crypto", "bitcoin", "btc", "eth", "defi", "solana"]):
        topic = "crypto"
    elif any(w in text for w in ["breaking", "just announced", "new:", "just dropped"]):
        topic = "breaking_news"

    # Hook type detection
    hook = "statement"
    if text.startswith(("calling it", "mark my words", "in 6 months", "prediction")):
        hook = "prediction"
    elif any(w in text for w in ["i built", "i shipped", "i made", "j'ai build", "j'ai cree"]):
        hook = "builder_flex"
    elif text[:50].upper() == text[:50] and len(text) > 20:
        hook = "breaking_news"
    elif "?" in text[:80]:
        hook = "question"
    elif any(w in text for w in ["unpopular", "hot take", "contrarian", "wrong", "nobody"]):
        hook = "hot_take"
    elif any(w in text for w in ["lol", "mdr", "😂", "😭", "bro", "mes freres"]):
        hook = "humor"

    tweet["topic"] = topic
    tweet["hook_type"] = hook
    return tweet


def is_niche_relevant(tweet: dict) -> bool:
    text = (tweet.get("text") or "").lower()
    handle = (tweet.get("author_handle") or "").lower()

    if handle in [h.lower() for h in NICHE_ACCOUNTS]:
        return True

    niche_words = [
        "claude", "gpt", "llm", "agent", "ai ", "artificial", "anthropic",
        "openai", "cursor", "copilot", "automation", "pipeline", "builder",
        "indie", "saas", "ship", "crypto", "startup", "founder"
    ]
    return any(w in text for w in niche_words)


def write_digest(tweets: list[dict], date: str):
    top = sorted(
        [t for t in tweets if not t.get("is_retweet")],
        key=lambda x: x.get("engagement", {}).get("likes", 0),
        reverse=True
    )[:30]

    lines = [
        f"---",
        f"type: digest",
        f"date: {date}",
        f"tweet_count: {len(top)}",
        f"---",
        f"",
        f"# Digest {date}",
        f"",
        f"## Top Tweets (by likes)",
        f"",
    ]

    for i, t in enumerate(top, 1):
        eng = t.get("engagement", {})
        lines += [
            f"### {i}. @{t.get('author_handle')} — {t.get('topic','?')} / {t.get('hook_type','?')}",
            f"```",
            t.get("text", ""),
            f"```",
            f"**Engagement:** {eng.get('likes',0)}L · {eng.get('retweets',0)}RT · "
            f"{eng.get('replies',0)}R · {eng.get('bookmarks',0)}BM · {eng.get('views',0):,} views",
            f"**URL:** {t.get('tweet_url','')}",
            f"",
        ]

    path = DIGESTS / f"{date}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[scraper] Digest written → {path}")


def run():
    init_db()
    date = datetime.now().strftime("%Y-%m-%d")
    all_tweets = []

    # 1. Main feed
    feed = scrape_feed(80)
    all_tweets.extend(feed)

    # 2. Search keywords (sample 3 random to avoid rate limits)
    for kw in SEARCH_KEYWORDS[:3]:
        results = scrape_search(kw, 15)
        all_tweets.extend(results)

    # 3. Trending accounts (sample 5)
    for handle in NICHE_ACCOUNTS[:5]:
        acct = scrape_account(handle, 3)
        all_tweets.extend(acct)

    # Deduplicate by id
    seen = set()
    unique = []
    for t in all_tweets:
        if t.get("id") not in seen:
            seen.add(t["id"])
            unique.append(t)

    print(f"[scraper] {len(unique)} unique tweets collected")

    # Classify + store niche-relevant ones
    relevant = []
    for t in unique:
        t = classify_tweet(t)
        if is_niche_relevant(t):
            upsert_feed_tweet(t)
            relevant.append(t)

    print(f"[scraper] {len(relevant)} niche-relevant tweets stored")

    # Write digest
    write_digest(relevant, date)

    return relevant


if __name__ == "__main__":
    run()
