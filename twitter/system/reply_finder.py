"""
Reply Finder — finds high-value reply opportunities in the feed.
Generates contextual replies using Claude + semantic similarity for inspiration.

Strategy:
  - Find tweets < 2h old with high engagement (viral window)
  - Find semantically similar successful tweets for inspiration
  - Generate reply with Paul's voice using Claude CLI
  - Add to draft queue with REPLY tag
"""
import json
import subprocess
import sqlite3
from datetime import datetime, timedelta, timezone

from config import CLIX, DRAFTS
from db import init_db, get_conn, save_draft
from scraper import classify_tweet, run_clix


# Accounts whose tweets are worth replying to (high follower count = free distribution)
HIGH_VALUE_ACCOUNTS = [
    "levelsio", "karpathy", "swyx", "steipete", "alexalbert__",
    "buccocapital", "RoundtableSpace", "_akhaliq", "therundownai",
    "gregisenberg", "noahzweben", "poetengineer__",
    "Frenchiee", "melvynx", "0xmaxou", "thismacapital",
    "vivoplt", "CantEverDie", "Hesamation",
]

# Topics worth replying on
REPLY_TOPICS = {"llm_models", "ai_agents", "builders", "automation", "breaking_news"}


def get_recent_viral_tweets(max_age_hours: int = 3, min_likes: int = 100) -> list[dict]:
    """Get tweets from the feed that are recent AND getting traction."""
    conn = get_conn()
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=max_age_hours)).isoformat()

    rows = conn.execute("""
        SELECT id, text, author_handle, likes, retweets, replies,
               bookmarks, views, engagement_rate, topic, hook_type,
               tweet_url, created_at
        FROM feed_tweets
        WHERE created_at >= ?
          AND likes >= ?
          AND is_retweet = 0
          AND topic IN ('llm_models', 'ai_agents', 'builders', 'automation', 'breaking_news')
        ORDER BY engagement_rate DESC, likes DESC
        LIMIT 20
    """, (cutoff, min_likes)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_high_value_recent_tweets() -> list[dict]:
    """Tweets from high-value accounts regardless of age."""
    conn = get_conn()
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=6)).isoformat()

    handles_placeholder = ",".join(["?" for _ in HIGH_VALUE_ACCOUNTS])
    rows = conn.execute(f"""
        SELECT id, text, author_handle, likes, retweets, replies,
               bookmarks, views, engagement_rate, topic, hook_type,
               tweet_url, created_at
        FROM feed_tweets
        WHERE created_at >= ?
          AND author_handle IN ({handles_placeholder})
          AND is_retweet = 0
          AND likes >= 50
        ORDER BY likes DESC
        LIMIT 15
    """, [cutoff] + HIGH_VALUE_ACCOUNTS).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_inspiration_tweets(topic: str, hook_type: str, top_k: int = 5) -> list[dict]:
    """Get high-performing tweets with similar topic/hook for reply inspiration."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT text, author_handle, likes, bookmarks, tweet_url
        FROM feed_tweets
        WHERE (topic = ? OR hook_type = ?)
          AND likes >= 200
          AND is_retweet = 0
        ORDER BY engagement_rate DESC
        LIMIT ?
    """, (topic, hook_type, top_k)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def call_claude_reply(tweet_to_reply: dict, inspiration_tweets: list[dict]) -> str:
    """Generate a reply using Claude CLI."""
    from config import VOICE_CARD, BLACKLIST
    voice = VOICE_CARD.read_text(encoding="utf-8") if VOICE_CARD.exists() else ""
    blacklist = BLACKLIST.read_text(encoding="utf-8") if BLACKLIST.exists() else ""

    inspiration_text = ""
    if inspiration_tweets:
        inspiration_text = "\n## REPLIES/TWEETS SIMILAIRES QUI ONT BIEN PERFORMÉ\nInspire-toi du TON, pas du contenu exact:\n"
        for t in inspiration_tweets[:3]:
            inspiration_text += f"- @{t.get('author_handle')} [{t.get('likes',0)}L]: \"{t.get('text','')[:200]}\"\n"

    prompt = f"""Génère une reply Twitter pour Paul Roulleau. Réponds avec UNIQUEMENT le texte de la reply, rien d'autre.

## VOIX DE PAUL
{voice}

## BLACKLIST (ne jamais utiliser)
{blacklist}

{inspiration_text}

## TWEET À RÉPONDRE
@{tweet_to_reply.get('author_handle')}: "{tweet_to_reply.get('text','')}"
Engagement: {tweet_to_reply.get('likes',0)} likes, {tweet_to_reply.get('retweets',0)} RT
URL: {tweet_to_reply.get('tweet_url','')}

## RÈGLES POUR LA REPLY
1. Ajoute une INFORMATION ou un CONTREPOINT réel — jamais "good take" ou "exactly"
2. Court: 1-3 phrases max
3. Montre que tu build vraiment (pas que tu observes)
4. Si t'as rien d'intéressant à dire, réponds avec juste : [SKIP]
5. Aucun emoji, aucun hashtag

Génère la reply maintenant (texte brut uniquement):"""

    result = subprocess.run(
        ["claude", "-p", "--output-format", "text", "--model", "haiku"],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def find_and_generate_replies(date: str = None, max_replies: int = 5) -> list[dict]:
    """Main function: find opportunities + generate replies."""
    init_db()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    # Get candidate tweets
    viral = get_recent_viral_tweets(max_age_hours=3, min_likes=100)
    high_value = get_high_value_recent_tweets()

    # Merge + deduplicate
    seen_ids = set()
    candidates = []
    for t in viral + high_value:
        if t["id"] not in seen_ids:
            seen_ids.add(t["id"])
            candidates.append(t)

    if not candidates:
        print("[reply_finder] No reply candidates found")
        return []

    print(f"[reply_finder] {len(candidates)} candidates — generating replies...")

    generated = []
    for tweet in candidates[:max_replies]:
        inspiration = get_inspiration_tweets(
            tweet.get("topic", "ai_agents"),
            tweet.get("hook_type", "statement")
        )

        reply_text = call_claude_reply(tweet, inspiration)

        if not reply_text or reply_text == "[SKIP]" or len(reply_text) < 10:
            print(f"  [skip] @{tweet['author_handle']}: no good reply")
            continue

        # Save to DB
        draft_id = save_draft(
            date=date,
            content=reply_text,
            format="reply",
            topic=tweet.get("topic", "other"),
            hook_type="statement",
            recommended_time=_pick_reply_time(),
            context=f"Reply to @{tweet['author_handle']} ({tweet.get('likes',0)}L): {tweet.get('tweet_url','')}",
        )

        generated.append({
            "id": draft_id,
            "content": reply_text,
            "reply_to": tweet.get("tweet_url"),
            "reply_to_handle": tweet.get("author_handle"),
            "reply_to_likes": tweet.get("likes", 0),
        })

        print(f"  [reply] @{tweet['author_handle']} → \"{reply_text[:80]}...\"")

    # Append to today's draft queue
    if generated:
        _append_replies_to_draft_queue(generated, date)

    return generated


def _pick_reply_time() -> str:
    """Pick next available reply posting time."""
    now = datetime.now()
    # Replies should go out ASAP (within 30 min for viral window)
    minutes = (now.minute // 30 + 1) * 30
    if minutes >= 60:
        hour = (now.hour + 1) % 24
        minutes = 0
    else:
        hour = now.hour
    return f"{hour:02d}:{minutes:02d}"


def _append_replies_to_draft_queue(replies: list[dict], date: str):
    """Append reply drafts to the existing draft queue file."""
    path = DRAFTS / f"{date}.md"

    lines = ["\n---\n", f"## REPLIES GÉNÉRÉES — {datetime.now().strftime('%H:%M')}\n"]
    for i, r in enumerate(replies, 1):
        lines += [
            f"---",
            f"",
            f"## Reply {i} — {r.get('recommended_time', '?')} — REPLY @{r.get('reply_to_handle','')} ({r.get('reply_to_likes',0)}L)",
            f"",
            f"**Status:** [PENDING]",
            f"**Reply to:** {r.get('reply_to','')}",
            f"",
            f"```",
            r.get("content", ""),
            f"```",
            f"",
        ]

    with open(path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[reply_finder] {len(replies)} replies appended to {path}")


if __name__ == "__main__":
    import sys
    date = None
    for i, a in enumerate(sys.argv):
        if a == "--date" and i + 1 < len(sys.argv):
            date = sys.argv[i + 1]
    replies = find_and_generate_replies(date=date)
    print(f"\nGenerated {len(replies)} reply drafts")
