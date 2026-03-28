"""
Tracker — records performance of posted tweets.
Manual entry via CLI, or semi-auto via clix profile scraping.
Run daily at 22:00.
"""
import subprocess
import json
import sqlite3
from datetime import datetime

from config import CLIX, TWITTER_HANDLE, METRICS
from db import init_db, get_conn, get_all_drafts


def get_profile_tweets(handle: str, n: int = 20) -> list[dict]:
    """Fetch recent tweets from Paul's profile via clix."""
    if not handle:
        print("[tracker] TWITTER_HANDLE not set in .env")
        return []

    # syntax: clix user <handle> tweets <handle> --json -n N
    cmd = [CLIX, "user", handle, "tweets", handle, "--json", "-n", str(n)]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"[tracker] clix error: {result.stderr[:200]}")
        return []
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return []


def update_tweet_metrics(tweet_id: str, likes: int, retweets: int,
                          replies: int, bookmarks: int, impressions: int):
    conn = get_conn()
    views = impressions or 1
    total_eng = likes + retweets + replies + bookmarks
    eng_rate = round(total_eng / views * 100, 4)

    conn.execute("""
        UPDATE posted_tweets
        SET likes=?, retweets=?, replies=?, bookmarks=?, impressions=?,
            engagement_rate=?
        WHERE id=?
    """, (likes, retweets, replies, bookmarks, impressions, eng_rate, tweet_id))
    conn.commit()
    conn.close()


def record_posted_tweet(tweet_id: str, content: str, format: str, topic: str,
                         hook_type: str, time_posted: str = None,
                         original_draft: str = None, paul_edit_delta: float = 0):
    """Record a new posted tweet in the DB."""
    conn = get_conn()
    conn.execute("""
        INSERT OR IGNORE INTO posted_tweets
        (id, content, format, topic, hook_type, time_posted, original_draft, paul_edit_delta)
        VALUES (?,?,?,?,?,?,?,?)
    """, (
        tweet_id, content, format, topic, hook_type,
        time_posted or datetime.now().isoformat(),
        original_draft, paul_edit_delta
    ))
    conn.commit()
    conn.close()


def sync_from_profile(date: str = None):
    """Pull metrics from Paul's profile and update DB."""
    if not TWITTER_HANDLE:
        print("[tracker] Set TWITTER_HANDLE in .env to enable auto-sync")
        return

    print(f"[tracker] Syncing metrics for @{TWITTER_HANDLE}...")
    tweets = get_profile_tweets(TWITTER_HANDLE, n=20)

    conn = get_conn()
    updated = 0
    for t in tweets:
        tweet_id = t.get("id")
        if not tweet_id:
            continue

        eng = t.get("engagement", {})
        likes = eng.get("likes", 0)
        retweets = eng.get("retweets", 0)
        replies_count = eng.get("replies", 0)
        bookmarks = eng.get("bookmarks", 0)
        views = eng.get("views", 0)

        # Check if this tweet is in our DB
        row = conn.execute(
            "SELECT id FROM posted_tweets WHERE id=?", (tweet_id,)
        ).fetchone()

        if row:
            views_safe = views or 1
            total_eng = likes + retweets + replies_count + bookmarks
            eng_rate = round(total_eng / views_safe * 100, 4)
            conn.execute("""
                UPDATE posted_tweets
                SET likes=?, retweets=?, replies=?, bookmarks=?, impressions=?,
                    engagement_rate=?
                WHERE id=?
            """, (likes, retweets, replies_count, bookmarks, views, eng_rate, tweet_id))
            updated += 1

    conn.commit()
    conn.close()
    print(f"[tracker] Updated metrics for {updated} tweets")


def write_daily_metrics(date: str = None):
    """Generate daily metrics report."""
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    conn = get_conn()
    rows = conn.execute("""
        SELECT content, likes, retweets, replies, bookmarks, impressions,
               engagement_rate, topic, hook_type, time_posted
        FROM posted_tweets
        WHERE DATE(time_posted) = ?
        ORDER BY engagement_rate DESC
    """, (date,)).fetchall()
    conn.close()

    if not rows:
        print(f"[tracker] No posted tweets found for {date}")
        return

    lines = [
        f"---",
        f"type: daily-metrics",
        f"date: {date}",
        f"---",
        f"",
        f"# Métriques {date}",
        f"",
        f"| Tweet | Likes | RT | R | BM | Views | Eng% | Topic | Hook |",
        f"|-------|-------|----|---|----|-------|------|-------|------|",
    ]

    for r in rows:
        snippet = (r["content"] or "")[:40].replace("|", "/")
        lines.append(
            f"| {snippet}... | {r['likes']} | {r['retweets']} | {r['replies']} | "
            f"{r['bookmarks']} | {r['impressions']:,} | {r['engagement_rate']:.2f}% | "
            f"{r['topic']} | {r['hook_type']} |"
        )

    path = METRICS / f"{date}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[tracker] Daily metrics → {path}")


def add_tweet_manually():
    """Interactive CLI to add a posted tweet and its metrics."""
    print("\n[tracker] Add posted tweet manually")
    tweet_id = input("Tweet ID or URL: ").strip()
    if "status/" in tweet_id:
        tweet_id = tweet_id.split("status/")[-1].strip()

    content = input("Tweet content: ").strip()
    topic = input("Topic (ai_agents/llm_models/builders/hot_take/humor): ").strip() or "other"
    hook_type = input("Hook type (prediction/builder_flex/hot_take/humor/statement): ").strip() or "statement"
    format_ = input("Format (single/reply/thread_opener): ").strip() or "single"

    record_posted_tweet(tweet_id, content, format_, topic, hook_type)

    print("Metrics (press Enter to skip):")
    likes = int(input("Likes: ") or 0)
    retweets = int(input("Retweets: ") or 0)
    replies = int(input("Replies: ") or 0)
    bookmarks = int(input("Bookmarks: ") or 0)
    impressions = int(input("Views/Impressions: ") or 0)

    if any([likes, retweets, replies, bookmarks, impressions]):
        update_tweet_metrics(tweet_id, likes, retweets, replies, bookmarks, impressions)

    print(f"[tracker] Tweet {tweet_id} recorded.")


def run():
    init_db()
    date = datetime.now().strftime("%Y-%m-%d")
    sync_from_profile(date)
    write_daily_metrics(date)


if __name__ == "__main__":
    import sys
    if "--add" in sys.argv:
        add_tweet_manually()
    else:
        run()
