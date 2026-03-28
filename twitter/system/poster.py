"""
Poster — reads approved drafts and posts them via clix at the right time.
Run every 30 minutes via cron.
Posts tweets whose recommended_time has passed and are approved.
"""
import subprocess
import json
from datetime import datetime

from config import CLIX, DRAFTS
from db import init_db, get_pending_drafts, get_all_drafts, update_draft_status


def parse_draft_queue(date: str) -> dict[int, str]:
    """Parse the markdown approval queue. Returns {db_id: 'approved'|'rejected'|edited_content}."""
    path = DRAFTS / f"{date}.md"
    if not path.exists():
        return {}

    content = path.read_text(encoding="utf-8")
    results = {}

    # Parse each draft section
    sections = content.split("## Draft ")
    for section in sections[1:]:  # Skip header
        lines = section.strip().split("\n")
        if not lines:
            continue

        # Extract draft number from header: "1 — 08:30 — ..."
        try:
            draft_num = int(lines[0].split(" ")[0])
        except (ValueError, IndexError):
            continue

        # Look for status line
        status_raw = None
        for line in lines:
            if line.startswith("**Status:**"):
                status_raw = line.replace("**Status:**", "").strip()
                break

        if not status_raw:
            continue

        if "[A]" in status_raw or "[APPROVED]" in status_raw:
            # Check if content was edited (between ``` markers)
            code_blocks = []
            in_block = False
            for line in lines:
                if line.strip() == "```":
                    if in_block:
                        in_block = False
                    else:
                        in_block = True
                        code_blocks.append([])
                elif in_block:
                    code_blocks[-1].append(line)

            if code_blocks:
                edited = "\n".join(code_blocks[0]).strip()
                results[draft_num] = edited if edited else "approved"
            else:
                results[draft_num] = "approved"

        elif "[R]" in status_raw or "[REJECTED]" in status_raw:
            results[draft_num] = "rejected"

    return results


def should_post_now(recommended_time: str, tolerance_min: int = 45) -> bool:
    """Returns True if current time is within tolerance_min of recommended_time."""
    now = datetime.now()
    try:
        h, m = map(int, recommended_time.split(":"))
        target = now.replace(hour=h, minute=m, second=0, microsecond=0)
        diff = abs((now - target).total_seconds() / 60)
        return diff <= tolerance_min
    except (ValueError, AttributeError):
        return False


def post_tweet(content: str) -> str | None:
    """Post a tweet via clix. Returns tweet ID or None."""
    cmd = [CLIX, "post", content]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

    if result.returncode != 0:
        print(f"[poster] clix error: {result.stderr[:200]}")
        return None

    # Try to extract tweet ID from output
    output = result.stdout.strip()
    print(f"[poster] clix output: {output[:200]}")

    # clix typically returns the tweet URL or ID
    if "status/" in output:
        tweet_id = output.split("status/")[-1].strip().split("?")[0]
        return tweet_id

    return output or "posted"


def run(date: str = None, dry_run: bool = False):
    init_db()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    now_str = datetime.now().strftime("%H:%M")
    print(f"[poster] Checking drafts for {date} at {now_str}...")

    # Parse approval queue from markdown file
    approvals = parse_draft_queue(date)
    if not approvals:
        print("[poster] No approval updates found in draft queue")
        return

    # Get all drafts from DB
    all_drafts = get_all_drafts(date)

    posted_count = 0
    for i, draft in enumerate(all_drafts, 1):
        if draft["status"] != "pending":
            continue

        approval = approvals.get(i)
        if not approval:
            continue

        draft_id = draft["id"]
        rec_time = draft.get("recommended_time", "12:00")

        # Handle rejection
        if approval == "rejected":
            update_draft_status(draft_id, "rejected")
            print(f"[poster] Draft {i} rejected")
            continue

        # Determine final content (edited or original)
        content = approval if approval != "approved" else draft["content"]

        # Check if it's the right time to post
        if not should_post_now(rec_time):
            print(f"[poster] Draft {i} approved but not yet time (scheduled {rec_time}, now {now_str})")
            # Mark as approved-pending-time
            update_draft_status(draft_id, "approved_scheduled", content if approval != "approved" else None)
            continue

        # Post it
        print(f"[poster] Posting draft {i}: {content[:80]}...")
        if dry_run:
            print(f"[poster] DRY RUN — would post: {content}")
            update_draft_status(draft_id, "dry_run")
        else:
            tweet_id = post_tweet(content)
            if tweet_id:
                update_draft_status(draft_id, "posted")
                print(f"[poster] Posted! ID: {tweet_id}")
                posted_count += 1
            else:
                print(f"[poster] Post failed for draft {i}")

    print(f"[poster] Done. {posted_count} tweets posted.")


def run_scheduled(date: str = None):
    """Post all approved+scheduled tweets whose time has come."""
    init_db()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    now_str = datetime.now().strftime("%H:%M")
    all_drafts = get_all_drafts(date)

    posted_count = 0
    for draft in all_drafts:
        if draft["status"] != "approved_scheduled":
            continue

        rec_time = draft.get("recommended_time", "12:00")
        if not should_post_now(rec_time):
            continue

        content = draft.get("paul_edited_content") or draft["content"]
        print(f"[poster] Time! Posting scheduled tweet: {content[:80]}...")
        tweet_id = post_tweet(content)
        if tweet_id:
            update_draft_status(draft["id"], "posted")
            print(f"[poster] Posted! ID: {tweet_id}")
            posted_count += 1

    if posted_count > 0:
        print(f"[poster] {posted_count} scheduled tweets posted.")


if __name__ == "__main__":
    import sys
    dry = "--dry" in sys.argv
    run(dry_run=dry)
