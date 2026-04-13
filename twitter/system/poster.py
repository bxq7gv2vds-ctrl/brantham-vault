"""
Poster — reads approved drafts and schedules/posts them via clix.
Uses clix schedule for timed posts (no need for cron every 30 min).

Usage:
  python poster.py              — process approval queue for today
  python poster.py --date DATE  — process for specific date
  python poster.py --dry        — dry run, no actual posting
"""
import subprocess
import json
from datetime import datetime, timedelta

from config import CLIX, DRAFTS
from db import init_db, get_all_drafts, update_draft_status


def parse_approval_queue(date: str) -> dict[int, str | None]:
    """
    Parse the markdown approval queue.
    Returns {draft_number: content_to_post | None_if_rejected}
    """
    path = DRAFTS / f"{date}.md"
    if not path.exists():
        return {}

    content = path.read_text(encoding="utf-8")
    results = {}

    sections = content.split("## Draft ")
    for section in sections[1:]:
        lines = section.strip().split("\n")
        if not lines:
            continue

        # Header: "1 — 08:30 — topic / hook"
        try:
            draft_num = int(lines[0].split(" ")[0])
        except (ValueError, IndexError):
            continue

        # Find status line
        status_raw = ""
        for line in lines:
            if line.startswith("**Status:**"):
                status_raw = line.replace("**Status:**", "").strip()
                break

        if not status_raw or "[PENDING]" in status_raw:
            continue  # Not reviewed yet

        if "[R]" in status_raw or "[REJECTED]" in status_raw:
            results[draft_num] = None  # rejected
            continue

        if "[A]" in status_raw or "[APPROVED]" in status_raw:
            # Extract content from ``` block
            code_lines = []
            in_block = False
            for line in lines:
                if line.strip() == "```":
                    if in_block:
                        break
                    else:
                        in_block = True
                elif in_block:
                    code_lines.append(line)

            tweet_content = "\n".join(code_lines).strip()
            results[draft_num] = tweet_content if tweet_content else "approved"

    return results


def schedule_tweet(content: str, at_time: str, date: str) -> str | None:
    """
    Schedule a tweet via clix schedule.
    at_time format: "HH:MM" → converted to "YYYY-MM-DD HH:MM"
    Returns tweet_id or None.
    """
    # Build full datetime string
    schedule_dt = f"{date} {at_time}"
    cmd = [CLIX, "schedule", content, "--at", schedule_dt]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        print(f"[poster] schedule error: {result.stderr[:300]}")
        return None

    output = result.stdout.strip()
    print(f"[poster] Scheduled: {output[:200]}")

    # Try to extract ID from output
    if "status/" in output:
        return output.split("status/")[-1].strip().split("?")[0]
    return output or "scheduled"


def post_tweet_now(content: str) -> str | None:
    """Post a tweet immediately via clix post."""
    cmd = [CLIX, "post", content]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        print(f"[poster] post error: {result.stderr[:300]}")
        return None

    output = result.stdout.strip()
    print(f"[poster] Posted: {output[:200]}")

    if "status/" in output:
        return output.split("status/")[-1].strip().split("?")[0]
    return output or "posted"


def is_in_past(time_str: str, date: str) -> bool:
    """Returns True if date+time_str is in the past."""
    try:
        dt = datetime.strptime(f"{date} {time_str}", "%Y-%m-%d %H:%M")
        return dt < datetime.now()
    except ValueError:
        return False


def run(date: str = None, dry_run: bool = False):
    init_db()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    print(f"[poster] Processing approval queue for {date}...")

    approvals = parse_approval_queue(date)
    if not approvals:
        print("[poster] No approvals found. Edit drafts file with [A] or [R] first.")
        return

    all_drafts = get_all_drafts(date)
    if not all_drafts:
        print(f"[poster] No drafts in DB for {date}")
        return

    scheduled_count = 0
    posted_count = 0
    rejected_count = 0

    for i, draft in enumerate(all_drafts, 1):
        # Skip already processed drafts
        if draft["status"] not in ("pending", "approved_scheduled"):
            continue

        approval = approvals.get(i)
        if approval is None and i not in approvals:
            continue  # Not in queue

        draft_id = draft["id"]
        rec_time = draft.get("recommended_time", "12:00")

        # Rejected
        if approval is None:
            update_draft_status(draft_id, "rejected")
            print(f"[poster] Draft {i} → rejected")
            rejected_count += 1
            continue

        # Get final content
        content = approval if approval != "approved" else draft["content"]
        if not content:
            content = draft["content"]

        if dry_run:
            print(f"[poster] DRY RUN Draft {i} ({rec_time}): {content[:80]}...")
            update_draft_status(draft_id, "dry_run")
            continue

        # Decide: schedule or post now
        if is_in_past(rec_time, date):
            # Time already passed — post now
            print(f"[poster] Draft {i}: time {rec_time} passed, posting now...")
            tweet_id = post_tweet_now(content)
            if tweet_id:
                update_draft_status(draft_id, "posted")
                posted_count += 1
            else:
                print(f"[poster] Draft {i} post failed")
        else:
            # Schedule for future time
            print(f"[poster] Draft {i}: scheduling for {rec_time}...")
            tweet_id = schedule_tweet(content, rec_time, date)
            if tweet_id:
                update_draft_status(draft_id, "scheduled")
                scheduled_count += 1
            else:
                print(f"[poster] Draft {i} scheduling failed")

    print(f"\n[poster] Done: {posted_count} posted now, {scheduled_count} scheduled, {rejected_count} rejected")


if __name__ == "__main__":
    import sys
    dry = "--dry" in sys.argv
    date = None
    for i, a in enumerate(sys.argv):
        if a == "--date" and i + 1 < len(sys.argv):
            date = sys.argv[i + 1]
    run(date, dry_run=dry)
