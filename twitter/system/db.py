import sqlite3
import json
from datetime import datetime
from pathlib import Path
from config import DB_PATH


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS feed_tweets (
            id TEXT PRIMARY KEY,
            text TEXT NOT NULL,
            author_handle TEXT,
            author_name TEXT,
            author_verified INTEGER DEFAULT 0,
            created_at TEXT,
            likes INTEGER DEFAULT 0,
            retweets INTEGER DEFAULT 0,
            replies INTEGER DEFAULT 0,
            quotes INTEGER DEFAULT 0,
            bookmarks INTEGER DEFAULT 0,
            views INTEGER DEFAULT 0,
            engagement_rate REAL DEFAULT 0,
            is_retweet INTEGER DEFAULT 0,
            language TEXT DEFAULT 'en',
            tweet_url TEXT,
            topic TEXT,
            hook_type TEXT,
            format TEXT DEFAULT 'single',
            why_it_works TEXT,
            collected_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS posted_tweets (
            id TEXT PRIMARY KEY,
            content TEXT NOT NULL,
            format TEXT,
            topic TEXT,
            hook_type TEXT,
            time_posted DATETIME DEFAULT (datetime('now')),
            likes INTEGER DEFAULT 0,
            retweets INTEGER DEFAULT 0,
            replies INTEGER DEFAULT 0,
            bookmarks INTEGER DEFAULT 0,
            impressions INTEGER DEFAULT 0,
            engagement_rate REAL DEFAULT 0,
            paul_approval TEXT DEFAULT 'approved',
            paul_edit_delta REAL DEFAULT 0,
            original_draft TEXT,
            notes TEXT
        );

        CREATE TABLE IF NOT EXISTS drafts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            content TEXT NOT NULL,
            format TEXT,
            topic TEXT,
            hook_type TEXT,
            recommended_time TEXT,
            context TEXT,
            status TEXT DEFAULT 'pending',
            paul_edited_content TEXT,
            posted_tweet_id TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS patterns (
            name TEXT PRIMARY KEY,
            type TEXT,
            description TEXT,
            examples TEXT,
            success_rate REAL DEFAULT 0.5,
            avg_engagement REAL DEFAULT 0,
            sample_size INTEGER DEFAULT 0,
            last_updated TEXT DEFAULT (datetime('now'))
        );

        CREATE INDEX IF NOT EXISTS idx_feed_collected ON feed_tweets(collected_at);
        CREATE INDEX IF NOT EXISTS idx_feed_engagement ON feed_tweets(likes DESC);
        CREATE INDEX IF NOT EXISTS idx_drafts_date ON drafts(date);
        CREATE INDEX IF NOT EXISTS idx_drafts_status ON drafts(status);
    """)
    conn.commit()
    conn.close()


def upsert_feed_tweet(tweet: dict):
    conn = get_conn()
    eng = tweet.get("engagement", {})
    views = eng.get("views", 1) or 1
    total_eng = eng.get("likes", 0) + eng.get("retweets", 0) + eng.get("replies", 0) + eng.get("bookmarks", 0)
    eng_rate = round(total_eng / views * 100, 4) if views > 0 else 0

    conn.execute("""
        INSERT OR REPLACE INTO feed_tweets
        (id, text, author_handle, author_name, author_verified, created_at,
         likes, retweets, replies, quotes, bookmarks, views, engagement_rate,
         is_retweet, language, tweet_url)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        tweet["id"],
        tweet.get("text", ""),
        tweet.get("author_handle", ""),
        tweet.get("author_name", ""),
        1 if tweet.get("author_verified") else 0,
        tweet.get("created_at", ""),
        eng.get("likes", 0),
        eng.get("retweets", 0),
        eng.get("replies", 0),
        eng.get("quotes", 0),
        eng.get("bookmarks", 0),
        eng.get("views", 0),
        eng_rate,
        1 if tweet.get("is_retweet") else 0,
        tweet.get("language", "en"),
        tweet.get("tweet_url", ""),
    ))
    conn.commit()
    conn.close()


def save_draft(date: str, content: str, format: str, topic: str, hook_type: str,
               recommended_time: str, context: str = "") -> int:
    conn = get_conn()
    cur = conn.execute("""
        INSERT INTO drafts (date, content, format, topic, hook_type, recommended_time, context)
        VALUES (?,?,?,?,?,?,?)
    """, (date, content, format, topic, hook_type, recommended_time, context))
    draft_id = cur.lastrowid
    conn.commit()
    conn.close()
    return draft_id


def get_pending_drafts(date: str) -> list[dict]:
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM drafts WHERE date=? AND status='pending' ORDER BY id",
        (date,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_all_drafts(date: str) -> list[dict]:
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM drafts WHERE date=? ORDER BY id",
        (date,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_draft_status(draft_id: int, status: str, edited_content: str = None):
    conn = get_conn()
    if edited_content:
        conn.execute(
            "UPDATE drafts SET status=?, paul_edited_content=? WHERE id=?",
            (status, edited_content, draft_id)
        )
    else:
        conn.execute("UPDATE drafts SET status=? WHERE id=?", (status, draft_id))
    conn.commit()
    conn.close()


def get_top_feed_tweets(limit: int = 20, min_likes: int = 50) -> list[dict]:
    conn = get_conn()
    rows = conn.execute("""
        SELECT * FROM feed_tweets
        WHERE is_retweet=0 AND likes >= ?
        ORDER BY engagement_rate DESC, likes DESC
        LIMIT ?
    """, (min_likes, limit)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_recent_posted_stats() -> dict:
    conn = get_conn()
    row = conn.execute("""
        SELECT
            COUNT(*) as total,
            AVG(likes) as avg_likes,
            AVG(retweets) as avg_rt,
            AVG(engagement_rate) as avg_eng_rate,
            MAX(likes) as max_likes
        FROM posted_tweets
        WHERE time_posted >= datetime('now', '-30 days')
    """).fetchone()
    conn.close()
    return dict(row) if row else {}
