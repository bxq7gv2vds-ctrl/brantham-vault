"""
Mass Collector — scrapes tens of thousands of tweets using time-windowed search.
Strategy: for each account, query `from:handle since:X until:Y` across 24+ monthly windows.
Also scrapes Paul's full following list if handle is provided.

Usage:
  python mass_collector.py                    — scrape all known accounts (windowed)
  python mass_collector.py --handle paulhandle — also fetch full following list first
  python mass_collector.py --account levelsio  — single account
"""
import subprocess
import json
import time
import sys
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from pathlib import Path

from config import CLIX, KG, LEARNING_DIR
from db import init_db, upsert_feed_tweet, get_conn
from scraper import classify_tweet, run_clix

PROGRESS_FILE = KG / "mass_collection_progress.json"

# All known niche accounts
SEED_ACCOUNTS = [
    # Tier 1 — builders + AI power users
    "levelsio", "swyx", "steipete", "karpathy", "alexalbert__",
    "buccocapital", "RoundtableSpace", "bindureddy",
    # Tier 2 — daily feed
    "_akhaliq", "therundownai", "gregisenberg",
    "noahzweben", "lydiahallie", "poetengineer__",
    "WatcherGuru", "DeItaone",
    # Tier 2-FR
    "Frenchiee", "melvynx", "0xmaxou", "BrivaelFr", "thismacapital",
    # Tier 3
    "arafatkatze", "zostaff", "sawyerhood", "plbiojout",
    # Extra high-value found in feed
    "vivoplt", "CantEverDie", "Hesamation", "HighyieldHarry",
    "bcherny", "emollick", "sama", "paulg", "naval",
    "cdixon", "benedictevans", "stratechery",
    # From 0xMikeTheIntern's following — AI/ML/builders
    "NousResearch", "ylecun", "OpenAI", "TheRundownAI", "SemiAnalysis_",
    "ericliujt", "shafu0x", "SpencerHakimian",
]

KEYWORDS = [
    "AI agents", "Claude Code", "LLM", "agentic AI",
    "automation pipeline", "building in public",
    "indie hacker", "Cursor IDE", "Claude vs GPT",
    "AI tools 2026", "solo founder AI", "ship fast",
    "autonomous agent", "multi-agent", "context window",
    "Anthropic claude", "openai gpt", "llm workflow",
    "AI startup", "build with AI",
    # Extended AI niche keywords
    "vibe coding", "MCP server", "Claude agent", "AI workflow",
    "open source LLM", "fine-tuning", "RAG pipeline",
    "AI product", "10x developer AI", "coding agent",
]


def generate_monthly_windows(months_back: int = 30) -> list[tuple[str, str]]:
    """Generate monthly time windows going back N months."""
    windows = []
    today = date.today()
    for i in range(months_back):
        end = today - relativedelta(months=i)
        start = end - relativedelta(months=1)
        windows.append((start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")))
    return windows


def search_windowed(query: str, since: str, until: str, delay: float = 3.5) -> list[dict]:
    """Search with time window, return tweets."""
    full_query = f"{query} since:{since} until:{until}"
    tweets = run_clix(["search", full_query, "--json", "-n", "50"])
    time.sleep(delay)
    return tweets


def get_following_list(handle: str) -> list[str]:
    """Get the full list of accounts Paul follows."""
    print(f"[mass] Fetching following list for @{handle}...")
    result = run_clix(["user", handle, "following", handle, "--json", "-n", "200"])
    if not result:
        return []
    # Following list is users, not tweets — extract handles
    handles = []
    for item in result:
        h = item.get("handle") or item.get("author_handle") or item.get("screen_name")
        if h:
            handles.append(h)
    print(f"[mass] Found {len(handles)} followed accounts")
    return handles


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {
        "account_windows_done": {},  # {handle: [window1, window2, ...]}
        "keywords_done": [],
        "total_stored": 0,
        "started_at": datetime.now().isoformat(),
    }


def save_progress(p: dict):
    p["last_updated"] = datetime.now().isoformat()
    PROGRESS_FILE.write_text(json.dumps(p, indent=2))


def scrape_account_windowed(handle: str, months_back: int = 30, progress: dict = None) -> int:
    """Scrape all tweets from an account using monthly windows."""
    windows = generate_monthly_windows(months_back)
    done_windows = (progress or {}).get("account_windows_done", {}).get(handle, [])

    stored = 0
    for since, until in windows:
        window_key = f"{since}_{until}"
        if window_key in done_windows:
            continue

        tweets = search_windowed(f"from:{handle}", since, until, delay=3.0)
        for t in tweets:
            if not t.get("is_retweet"):
                t = classify_tweet(t)
                upsert_feed_tweet(t)
                stored += 1

        if progress is not None:
            if handle not in progress["account_windows_done"]:
                progress["account_windows_done"][handle] = []
            progress["account_windows_done"][handle].append(window_key)

    return stored


def scrape_keywords_windowed(months_back: int = 12, progress: dict = None) -> int:
    """Scrape all keywords across time windows."""
    windows = generate_monthly_windows(months_back)
    stored = 0

    for keyword in KEYWORDS:
        for since, until in windows:
            key = f"{keyword}_{since}_{until}"
            if key in (progress or {}).get("keywords_done", []):
                continue

            tweets = search_windowed(keyword, since, until, delay=2.5)
            for t in tweets:
                if not t.get("is_retweet"):
                    t = classify_tweet(t)
                    upsert_feed_tweet(t)
                    stored += 1

            if progress is not None:
                progress["keywords_done"].append(key)
                progress["total_stored"] += len(tweets)

    return stored


def print_stats():
    conn = get_conn()
    total = conn.execute("SELECT COUNT(*) FROM feed_tweets").fetchone()[0]
    top = conn.execute("""
        SELECT author_handle, COUNT(*) as n
        FROM feed_tweets
        GROUP BY author_handle
        ORDER BY n DESC LIMIT 15
    """).fetchall()
    conn.close()
    print(f"\n=== Mass Collection Stats ===")
    print(f"Total tweets in DB: {total:,}")
    print("Top accounts:")
    for row in top:
        print(f"  @{row[0]}: {row[1]} tweets")


def write_progress_md(progress: dict):
    """Update the Obsidian progress file."""
    total = progress.get("total_stored", 0)
    accounts_done = len(progress.get("account_windows_done", {}))
    lines = [
        f"---",
        f"type: collection-progress",
        f"updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"---",
        f"",
        f"# Mass Collection Progress",
        f"",
        f"- **Total tweets collectés** : {total:,}",
        f"- **Comptes traités** : {accounts_done}/{len(SEED_ACCOUNTS)}",
        f"- **Dernière mise à jour** : {datetime.now().strftime('%H:%M')}",
        f"",
        f"## Comptes terminés",
        f"",
    ]
    for handle, windows in progress.get("account_windows_done", {}).items():
        lines.append(f"- @{handle} : {len(windows)} fenêtres temporelles")
    path = LEARNING_DIR / "mass-collection-progress.md"
    path.write_text("\n".join(lines), encoding="utf-8")


def run(paul_handle: str = None, single_account: str = None):
    init_db()
    progress = load_progress()

    # Optionally fetch Paul's following list first
    accounts_to_scrape = list(SEED_ACCOUNTS)
    if paul_handle:
        following = get_following_list(paul_handle)
        # Add new accounts not already in seed list
        new_accounts = [h for h in following if h not in accounts_to_scrape]
        accounts_to_scrape = accounts_to_scrape + new_accounts
        print(f"[mass] Total accounts to scrape: {len(accounts_to_scrape)} ({len(new_accounts)} from following list)")

    if single_account:
        accounts_to_scrape = [single_account]

    total_new = 0
    total_accounts = len(accounts_to_scrape)

    print(f"[mass] Starting mass collection: {total_accounts} accounts × ~30 monthly windows")
    print(f"[mass] Estimated: {total_accounts * 30 * 15:,} tweets (15 avg per window)")
    print(f"[mass] Progress saved — safe to interrupt and resume\n")

    for i, handle in enumerate(accounts_to_scrape, 1):
        done_windows = progress["account_windows_done"].get(handle, [])
        if len(done_windows) >= 30:
            print(f"  [{i}/{total_accounts}] @{handle} — already complete ({len(done_windows)} windows)")
            continue

        print(f"  [{i}/{total_accounts}] @{handle} — scraping 30 monthly windows...")
        n = scrape_account_windowed(handle, months_back=30, progress=progress)
        total_new += n
        progress["total_stored"] += n
        save_progress(progress)
        write_progress_md(progress)
        print(f"  → {n} tweets stored (total: {progress['total_stored']:,})")
        time.sleep(0.5)

    # Keywords
    print(f"\n[mass] Phase 2 — Keywords ({len(KEYWORDS)} × 12 months)...")
    n_kw = scrape_keywords_windowed(months_back=12, progress=progress)
    total_new += n_kw
    progress["total_stored"] += n_kw
    save_progress(progress)

    print(f"\n[mass] Done. {total_new:,} new tweets collected.")
    print_stats()
    write_progress_md(progress)


if __name__ == "__main__":
    handle = None
    account = None
    for i, a in enumerate(sys.argv[1:], 1):
        if a == "--handle" and i < len(sys.argv) - 1:
            handle = sys.argv[i + 1]
        if a == "--account" and i < len(sys.argv) - 1:
            account = sys.argv[i + 1]
    run(paul_handle=handle, single_account=account)
