"""
Data Collector — Week 1 mass data collection.
Scrapes ALL tweets from every niche account (200+ per account).
Goal: build a corpus of 10K+ tweets to train the engagement model.

Usage:
  python data_collector.py            — full deep scrape (all accounts, all keywords)
  python data_collector.py --quick    — only feed + bookmarks (faster)
  python data_collector.py --account levelsio  — single account
"""
import subprocess
import json
import time
import sys
from datetime import datetime
from pathlib import Path

from config import CLIX, BASE
from db import init_db, upsert_feed_tweet, get_conn
from scraper import classify_tweet, run_clix

# All accounts to scrape in Week 1
ALL_ACCOUNTS = {
    "tier1": [
        "levelsio", "swyx", "steipete", "karpathy", "alexalbert__",
        "buccocapital", "RoundtableSpace", "bindureddy",
    ],
    "tier2": [
        "_akhaliq", "therundownai", "gregisenberg",
        "noahzweben", "lydiahallie", "poetengineer__",
        "WatcherGuru", "DeItaone",
    ],
    "tier2_fr": [
        "Frenchiee", "melvynx", "0xmaxou", "BrivaelFr", "thismacapital",
    ],
    "tier3": [
        "arafatkatze", "zostaff", "sawyerhood", "plbiojout",
    ],
}

ALL_KEYWORDS = [
    "AI agents", "Claude Code", "LLM", "agentic AI",
    "automation pipeline", "building in public",
    "indie hacker", "Cursor IDE", "OpenAI", "Anthropic",
    "self-improvement builder", "Claude vs GPT",
    "AI tools 2026", "ship fast", "solo founder AI",
]

PROGRESS_FILE = BASE / "knowledge-graph" / "collection_progress.json"


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {"accounts_done": [], "keywords_done": [], "total_collected": 0, "started_at": datetime.now().isoformat()}


def save_progress(p: dict):
    p["last_updated"] = datetime.now().isoformat()
    PROGRESS_FILE.write_text(json.dumps(p, indent=2))


def scrape_account_deep(handle: str, n: int = 200) -> int:
    """Scrape up to n tweets from a single account. Returns count stored."""
    print(f"  [collect] @{handle} — scraping {n} tweets...")
    tweets = run_clix(["user", handle, "tweets", handle, "--json", "-n", str(n)])
    if not tweets:
        print(f"  [collect] @{handle} — no results")
        return 0

    stored = 0
    for t in tweets:
        t = classify_tweet(t)
        upsert_feed_tweet(t)
        stored += 1

    print(f"  [collect] @{handle} — {stored} tweets stored")
    return stored


def scrape_keyword_deep(keyword: str, n: int = 100) -> int:
    print(f"  [collect] keyword '{keyword}' — scraping {n} tweets...")
    tweets = run_clix(["search", keyword, "--json", "-n", str(n)])
    if not tweets:
        return 0

    stored = 0
    for t in tweets:
        if not t.get("is_retweet"):
            t = classify_tweet(t)
            upsert_feed_tweet(t)
            stored += 1

    print(f"  [collect] '{keyword}' — {stored} tweets stored")
    return stored


def print_stats():
    conn = get_conn()
    total = conn.execute("SELECT COUNT(*) FROM feed_tweets").fetchone()[0]
    by_tier = conn.execute("""
        SELECT author_handle, COUNT(*) as n, AVG(likes) as avg_likes
        FROM feed_tweets
        GROUP BY author_handle
        ORDER BY n DESC
        LIMIT 20
    """).fetchall()
    conn.close()

    print(f"\n=== Collection Stats ===")
    print(f"Total tweets in DB: {total:,}")
    print(f"\nTop accounts by tweet count:")
    for row in by_tier:
        print(f"  @{row['author_handle']}: {row['n']} tweets, avg {row['avg_likes']:.0f} likes")


def run(quick: bool = False, single_account: str = None):
    init_db()
    progress = load_progress()
    total_new = 0

    if single_account:
        n = scrape_account_deep(single_account, n=200)
        print(f"\nCollected {n} tweets from @{single_account}")
        return

    if quick:
        print("[collector] Quick mode — feed + bookmarks only")
        from scraper import scrape_feed, scrape_bookmarks
        for t in scrape_feed(200):
            t = classify_tweet(t)
            upsert_feed_tweet(t)
            total_new += 1
        for t in scrape_bookmarks(50):
            t = classify_tweet(t)
            upsert_feed_tweet(t)
            total_new += 1
        print(f"\n[collector] Quick done. {total_new} tweets collected.")
        print_stats()
        return

    # Full deep collection
    print(f"[collector] DEEP COLLECTION — Week 1 data harvest")
    print(f"[collector] Already done: {len(progress['accounts_done'])} accounts, {len(progress['keywords_done'])} keywords")

    # Accounts
    all_handles = []
    for tier, handles in ALL_ACCOUNTS.items():
        for h in handles:
            all_handles.append((tier, h))

    print(f"\n[collector] Phase 1 — Accounts ({len(all_handles)} total)")
    for tier, handle in all_handles:
        if handle in progress["accounts_done"]:
            print(f"  [skip] @{handle} (already done)")
            continue

        n = scrape_account_deep(handle, n=200)
        total_new += n
        progress["accounts_done"].append(handle)
        progress["total_collected"] += n
        save_progress(progress)
        time.sleep(1.5)  # Rate limit courtesy

    # Keywords
    print(f"\n[collector] Phase 2 — Keywords ({len(ALL_KEYWORDS)} total)")
    for keyword in ALL_KEYWORDS:
        if keyword in progress["keywords_done"]:
            print(f"  [skip] '{keyword}' (already done)")
            continue

        n = scrape_keyword_deep(keyword, n=100)
        total_new += n
        progress["keywords_done"].append(keyword)
        progress["total_collected"] += n
        save_progress(progress)
        time.sleep(1.0)

    print(f"\n[collector] Done. {total_new} new tweets collected this run.")
    print_stats()


if __name__ == "__main__":
    quick = "--quick" in sys.argv
    account = None
    for i, a in enumerate(sys.argv):
        if a == "--account" and i + 1 < len(sys.argv):
            account = sys.argv[i + 1]
    run(quick=quick, single_account=account)
