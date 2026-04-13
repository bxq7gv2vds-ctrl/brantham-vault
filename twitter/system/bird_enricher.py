"""
Bird Enricher — targeted Twitter searches using bird CLI.
Complements clix mass_collector with real-time high-quality searches.

Uses AUTH_TOKEN + CT0 from clix auth.json automatically.
"""
import subprocess
import json
import re
import sqlite3
import time
from datetime import datetime
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))
from config import DB_PATH
from db import init_db, upsert_feed_tweet
from scraper import classify_tweet

# Auth from clix config
_AUTH_CACHE = {}

BIRD_QUERIES = [
    # AI builders — highest engagement potential
    "Claude Code shipped built solo",
    "AI agents autonomous workflow",
    "LLM vibe coding shipped",
    "solo builder AI shipped",
    "Claude agent built",
    # Hot takes / opinions
    "AI hot take unpopular opinion developers",
    "LLM wrong actually builders",
    # Specific tools
    "MCP server built autonomous",
    "cursor claude copilot comparison",
    # French niche
    "IA agents construit francais",
    "claude code builder francais",
]


def _get_auth() -> tuple[str, str]:
    """Load auth tokens from clix auth.json."""
    global _AUTH_CACHE
    if _AUTH_CACHE:
        return _AUTH_CACHE.get("auth_token", ""), _AUTH_CACHE.get("ct0", "")
    try:
        auth_path = Path.home() / ".config" / "clix" / "auth.json"
        data = json.loads(auth_path.read_text())
        acct = data.get("accounts", {}).get("default", data.get("default", {}))
        auth_token = acct.get("auth_token", "")
        ct0 = acct.get("ct0", "")
        _AUTH_CACHE = {"auth_token": auth_token, "ct0": ct0}
        return auth_token, ct0
    except Exception:
        return "", ""


def bird_search(query: str, n: int = 20) -> list[dict]:
    """Run bird search and return parsed tweets."""
    auth_token, ct0 = _get_auth()
    if not auth_token:
        print("[bird_enricher] No auth token found")
        return []

    env = {"AUTH_TOKEN": auth_token, "CT0": ct0, "PATH": "/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin"}
    result = subprocess.run(
        ["bird", "search", query, "-n", str(n)],
        capture_output=True, text=True, timeout=30, env=env,
    )
    if result.returncode != 0 or not result.stdout:
        return []

    return _parse_bird_output(result.stdout)


def bird_user_tweets(handle: str, n: int = 20) -> list[dict]:
    """Fetch recent tweets from a user via bird."""
    auth_token, ct0 = _get_auth()
    if not auth_token:
        return []

    env = {"AUTH_TOKEN": auth_token, "CT0": ct0, "PATH": "/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin"}
    handle_clean = handle.lstrip("@")
    result = subprocess.run(
        ["bird", "user-tweets", f"@{handle_clean}", "-n", str(n)],
        capture_output=True, text=True, timeout=30, env=env,
    )
    if result.returncode != 0 or not result.stdout:
        return []

    return _parse_bird_output(result.stdout)


def _parse_bird_output(text: str) -> list[dict]:
    """Parse bird's text output into tweet dicts."""
    tweets = []
    current = {}

    for line in text.splitlines():
        line = line.strip()

        # Author line: @handle (Display Name):
        m = re.match(r'^@(\S+)\s*\(([^)]+)\):', line)
        if m:
            if current.get("text"):
                tweets.append(current)
            current = {
                "author_handle": m.group(1),
                "author_name": m.group(2),
                "text": "",
                "likes": 0,
                "retweets": 0,
                "bookmarks": 0,
                "views": 0,
            }

        # Date line
        elif line.startswith("📅 "):
            date_str = line[2:].strip()
            try:
                dt = datetime.strptime(date_str, "%a %b %d %H:%M:%S +0000 %Y")
                current["created_at"] = dt.isoformat() + "Z"
            except ValueError:
                current["created_at"] = ""

        # URL line
        elif line.startswith("🔗 "):
            url = line[2:].strip()
            current["tweet_url"] = url
            # Extract tweet ID
            m_id = re.search(r'/status/(\d+)', url)
            if m_id:
                current["id"] = m_id.group(1)

        # Engagement lines (bird shows 🔁 RT, ❤️ likes etc.)
        elif re.match(r'^[🔁❤️👁📊]', line):
            nums = re.findall(r'\d+', line.replace(',', ''))
            if '🔁' in line and nums:
                current["retweets"] = int(nums[0])
            elif '❤️' in line and nums:
                current["likes"] = int(nums[0])
            elif '👁' in line and nums:
                current["views"] = int(nums[0])

        # Separator
        elif line.startswith("──"):
            if current.get("text"):
                tweets.append(current)
            current = {}

        # Text content (everything else that's not metadata)
        elif current and not line.startswith(("┌─", "│", "└─", "ℹ️", "⚠️", "🖼️", "🎬")):
            if line and "text" in current:
                if current["text"]:
                    current["text"] += "\n" + line
                else:
                    current["text"] = line

    if current.get("text"):
        tweets.append(current)

    return tweets


def _store_tweet(tweet: dict) -> bool:
    """Store a bird-parsed tweet in the DB."""
    if not tweet.get("text") or not tweet.get("author_handle"):
        return False
    if not tweet.get("id"):
        # Generate synthetic ID from handle + text hash
        tweet["id"] = f"bird_{abs(hash(tweet['author_handle'] + tweet.get('text','')[:50]))}"

    # Mark as not retweet (we skip RTs)
    if tweet.get("text", "").startswith("RT @"):
        return False

    tweet["is_retweet"] = 0
    tweet = classify_tweet(tweet)
    upsert_feed_tweet(tweet)
    return True


def enrich(queries: list[str] = None, top_accounts: list[str] = None) -> int:
    """
    Run targeted bird searches and store results.
    Returns number of tweets stored.
    """
    init_db()
    queries = queries or BIRD_QUERIES
    top_accounts = top_accounts or []

    stored = 0

    # Search queries
    print(f"[bird_enricher] Searching {len(queries)} queries...")
    for q in queries:
        tweets = bird_search(q, n=20)
        for t in tweets:
            if _store_tweet(t):
                stored += 1
        time.sleep(2.0)

    # Top accounts
    if top_accounts:
        print(f"[bird_enricher] Fetching {len(top_accounts)} accounts...")
        for handle in top_accounts:
            tweets = bird_user_tweets(handle, n=30)
            for t in tweets:
                if _store_tweet(t):
                    stored += 1
            time.sleep(2.0)

    print(f"[bird_enricher] Done — {stored} tweets stored")
    return stored


def get_latest_on_topic(topic: str, n: int = 10) -> list[dict]:
    """
    Quick search for the latest high-engagement tweets on a topic.
    Used by drafter for real-time context.
    """
    tweets = bird_search(topic, n=n * 2)
    # Sort by likes descending
    return sorted(tweets, key=lambda x: x.get("likes", 0), reverse=True)[:n]


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        q = " ".join(sys.argv[1:])
        tweets = bird_search(q, n=10)
        for t in tweets:
            print(f"[{t.get('likes',0)}L @{t.get('author_handle','')}] {t.get('text','')[:100]}")
    else:
        n = enrich()
        print(f"Stored: {n}")
