"""
Analyst Agent — extracts patterns from DB, updates patterns.json.
Run weekly (or after N new tweets are tracked).
"""
import json
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

from config import PATTERNS_JSON, TOPICS_JSON, METRICS
from db import init_db, get_conn, get_recent_posted_stats


def compute_pattern_stats() -> dict:
    """Compute engagement stats grouped by topic, hook_type, format, posting hour."""
    conn = get_conn()

    patterns = {}

    # By topic
    rows = conn.execute("""
        SELECT topic, COUNT(*) as n, AVG(likes) as avg_likes,
               AVG(engagement_rate) as avg_eng, MAX(likes) as max_likes
        FROM posted_tweets
        WHERE topic IS NOT NULL AND time_posted >= datetime('now', '-60 days')
        GROUP BY topic
        HAVING n >= 2
        ORDER BY avg_eng DESC
    """).fetchall()
    patterns["by_topic"] = [dict(r) for r in rows]

    # By hook type
    rows = conn.execute("""
        SELECT hook_type, COUNT(*) as n, AVG(likes) as avg_likes,
               AVG(engagement_rate) as avg_eng
        FROM posted_tweets
        WHERE hook_type IS NOT NULL AND time_posted >= datetime('now', '-60 days')
        GROUP BY hook_type
        HAVING n >= 2
        ORDER BY avg_eng DESC
    """).fetchall()
    patterns["by_hook"] = [dict(r) for r in rows]

    # By format
    rows = conn.execute("""
        SELECT format, COUNT(*) as n, AVG(likes) as avg_likes,
               AVG(engagement_rate) as avg_eng
        FROM posted_tweets
        WHERE format IS NOT NULL AND time_posted >= datetime('now', '-60 days')
        GROUP BY format
        HAVING n >= 2
        ORDER BY avg_eng DESC
    """).fetchall()
    patterns["by_format"] = [dict(r) for r in rows]

    # By hour of posting
    rows = conn.execute("""
        SELECT strftime('%H', time_posted) as hour,
               COUNT(*) as n, AVG(likes) as avg_likes, AVG(engagement_rate) as avg_eng
        FROM posted_tweets
        WHERE time_posted >= datetime('now', '-60 days')
        GROUP BY hour
        HAVING n >= 2
        ORDER BY avg_eng DESC
    """).fetchall()
    patterns["by_hour"] = [dict(r) for r in rows]

    # Top performers
    rows = conn.execute("""
        SELECT content, likes, retweets, bookmarks, engagement_rate, topic, hook_type
        FROM posted_tweets
        ORDER BY engagement_rate DESC
        LIMIT 10
    """).fetchall()
    patterns["top_tweets"] = [dict(r) for r in rows]

    conn.close()
    return patterns


def update_patterns_json(patterns: dict):
    data = {
        "updated": datetime.now().isoformat(),
        "patterns": patterns,
        "summary": {
            "best_topic": patterns["by_topic"][0]["topic"] if patterns["by_topic"] else None,
            "best_hook": patterns["by_hook"][0]["hook_type"] if patterns["by_hook"] else None,
            "best_format": patterns["by_format"][0]["format"] if patterns["by_format"] else None,
            "best_hour": patterns["by_hour"][0]["hour"] if patterns["by_hour"] else None,
        }
    }
    PATTERNS_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"[analyst] patterns.json updated → {PATTERNS_JSON}")
    return data


def generate_weekly_report(date: str = None) -> str:
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    patterns = compute_patterns_json_data = compute_pattern_stats()
    stats = get_recent_posted_stats()
    summary = update_patterns_json(patterns)["summary"]

    report_lines = [
        f"---",
        f"type: weekly-report",
        f"date: {date}",
        f"---",
        f"",
        f"# Rapport hebdomadaire — {date}",
        f"",
        f"## Statistiques globales (30 derniers jours)",
        f"",
        f"- **Tweets postés :** {stats.get('total', 0)}",
        f"- **Avg likes :** {stats.get('avg_likes', 0):.1f}",
        f"- **Avg RT :** {stats.get('avg_rt', 0):.1f}",
        f"- **Avg engagement rate :** {stats.get('avg_eng_rate', 0):.2f}%",
        f"- **Max likes (1 tweet) :** {stats.get('max_likes', 0)}",
        f"",
        f"## Patterns gagnants",
        f"",
        f"- **Meilleur topic :** `{summary.get('best_topic', '?')}`",
        f"- **Meilleur hook :** `{summary.get('best_hook', '?')}`",
        f"- **Meilleur format :** `{summary.get('best_format', '?')}`",
        f"- **Meilleure heure :** `{summary.get('best_hour', '?')}h`",
        f"",
        f"## Top 5 tweets",
        f"",
    ]

    for i, t in enumerate(patterns.get("top_tweets", [])[:5], 1):
        report_lines += [
            f"### {i}. {t.get('likes',0)}L · {t.get('retweets',0)}RT · {t.get('bookmarks',0)}BM",
            f"*{t.get('topic','?')} / {t.get('hook_type','?')}*",
            f"```",
            t.get("content", ""),
            f"```",
            f"",
        ]

    report_lines += [
        f"## Topic breakdown",
        f"",
        f"| Topic | Count | Avg Likes | Avg Eng% |",
        f"|-------|-------|-----------|----------|",
    ]
    for row in patterns.get("by_topic", []):
        report_lines.append(
            f"| {row['topic']} | {row['n']} | {row['avg_likes']:.1f} | {row['avg_eng']:.2f}% |"
        )

    report_lines += [
        f"",
        f"## Hook breakdown",
        f"",
        f"| Hook | Count | Avg Likes | Avg Eng% |",
        f"|------|-------|-----------|----------|",
    ]
    for row in patterns.get("by_hook", []):
        report_lines.append(
            f"| {row['hook_type']} | {row['n']} | {row['avg_likes']:.1f} | {row['avg_eng']:.2f}% |"
        )

    report_content = "\n".join(report_lines)

    # Save to vault
    report_path = METRICS / f"weekly-{date}.md"
    report_path.write_text(report_content, encoding="utf-8")
    print(f"[analyst] Weekly report → {report_path}")
    return report_content


def run():
    init_db()
    patterns = compute_pattern_stats()

    if not any(patterns.values()):
        print("[analyst] No posted tweets yet. Patterns will be available after first posts.")
        return

    update_patterns_json(patterns)
    generate_weekly_report()


if __name__ == "__main__":
    run()
