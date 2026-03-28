#!/usr/bin/env python3
"""
Twitter Agent — CLI Orchestrator
Usage:
  python main.py scrape              — scrape feed + keywords + accounts
  python main.py draft               — generate today's drafts via Claude
  python main.py draft --date DATE   — generate drafts for specific date
  python main.py review              — show pending drafts (read-only)
  python main.py post                — post approved drafts that are due now
  python main.py post --dry          — dry run (no actual posting)
  python main.py track               — sync metrics from profile
  python main.py track --add         — manually add a tweet + metrics
  python main.py analyze             — update patterns from DB
  python main.py run                 — full pipeline: scrape + draft + post
  python main.py status              — show today's status summary
"""
import sys
from datetime import datetime
from pathlib import Path

# Add system dir to path
sys.path.insert(0, str(Path(__file__).parent))

from config import DRAFTS, METRICS, TWITTER_HANDLE
from db import init_db, get_all_drafts, get_recent_posted_stats


def cmd_scrape():
    from scraper import run
    run()


def cmd_draft(date: str = None):
    from drafter import run
    run(date)


def cmd_post(date: str = None, dry: bool = False):
    from poster import run, run_scheduled
    run(date, dry_run=dry)
    run_scheduled(date)


def cmd_track(add_manual: bool = False):
    from tracker import run, add_tweet_manually
    if add_manual:
        add_tweet_manually()
    else:
        run()


def cmd_analyze():
    from analyst import run
    run()


def cmd_review(date: str = None):
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    path = DRAFTS / f"{date}.md"
    if not path.exists():
        print(f"No drafts found for {date}. Run: python main.py draft")
        return
    print(path.read_text(encoding="utf-8"))


def cmd_status():
    date = datetime.now().strftime("%Y-%m-%d")
    print(f"\n=== Twitter Agent Status — {date} ===\n")

    # Drafts status
    drafts = get_all_drafts(date)
    if drafts:
        status_counts = {}
        for d in drafts:
            s = d["status"]
            status_counts[s] = status_counts.get(s, 0) + 1

        print(f"Drafts today: {len(drafts)} total")
        for s, n in status_counts.items():
            print(f"  [{s}] {n}")

        print("\nDraft schedule:")
        for i, d in enumerate(drafts, 1):
            status_icon = {
                "pending": "⏳",
                "approved_scheduled": "✅",
                "posted": "🐦",
                "rejected": "❌",
                "dry_run": "🧪",
            }.get(d["status"], "?")
            content_preview = (d.get("content") or "")[:60]
            print(f"  {status_icon} {d.get('recommended_time','?')} — Draft {i}: {content_preview}...")
    else:
        print("No drafts for today. Run: python main.py draft")

    # Recent stats
    stats = get_recent_posted_stats()
    if stats.get("total", 0) > 0:
        print(f"\nLast 30 days:")
        print(f"  Tweets posted: {stats['total']}")
        print(f"  Avg likes: {stats['avg_likes']:.1f}")
        print(f"  Avg eng rate: {stats['avg_eng_rate']:.2f}%")
        print(f"  Best tweet: {stats['max_likes']} likes")

    # Files
    digest_path = Path("/Users/paul/vault/twitter/digests") / f"{date}.md"
    print(f"\nFiles:")
    print(f"  Digest: {'✓' if digest_path.exists() else '✗'} {digest_path}")
    draft_path = DRAFTS / f"{date}.md"
    print(f"  Drafts: {'✓' if draft_path.exists() else '✗'} {draft_path}")

    print(f"\nTwitter handle: {TWITTER_HANDLE or '(not set in .env)'}")
    print()


def cmd_run(dry: bool = False):
    """Full pipeline: scrape → draft → post."""
    print("=== Running full pipeline ===\n")
    print("1/3 Scraping...")
    cmd_scrape()
    print("\n2/3 Generating drafts...")
    cmd_draft()
    print("\n3/3 Posting approved tweets...")
    cmd_post(dry=dry)
    print("\n=== Done ===")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return

    command = args[0]
    date = None
    for i, a in enumerate(args):
        if a == "--date" and i + 1 < len(args):
            date = args[i + 1]

    init_db()

    if command == "scrape":
        cmd_scrape()
    elif command == "draft":
        cmd_draft(date)
    elif command == "post":
        cmd_post(date, dry="--dry" in args)
    elif command == "track":
        cmd_track(add_manual="--add" in args)
    elif command == "analyze":
        cmd_analyze()
    elif command == "review":
        cmd_review(date)
    elif command == "status":
        cmd_status()
    elif command == "run":
        cmd_run(dry="--dry" in args)
    else:
        print(f"Unknown command: {command}")
        print(__doc__)


if __name__ == "__main__":
    main()
