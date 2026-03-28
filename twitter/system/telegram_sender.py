"""
Telegram Sender — Push draft tweets to a Telegram channel for review.

Original drafts: text block to copy + posting time
Reply drafts: text + inline button to open target tweet

Setup:
  1. Create bot via @BotFather → get TELEGRAM_BOT_TOKEN
  2. Add bot to your channel/group → get TELEGRAM_CHAT_ID
  3. Set both in system/.env

Usage:
  python telegram_sender.py              — send today's pending drafts
  python telegram_sender.py --replies    — send only reply drafts
  python telegram_sender.py --originals  — send only original drafts
  python telegram_sender.py --date DATE  — send drafts for specific date
"""
import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Load .env manually (no dependency)
_ENV_PATH = Path(__file__).parent / ".env"
if _ENV_PATH.exists():
    for _line in _ENV_PATH.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _, _v = _line.partition("=")
            if _k not in os.environ:
                os.environ[_k] = _v.strip()

from config import DB_PATH
from db import get_conn, init_db


def _get_config() -> tuple[str, str]:
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not token or not chat_id:
        print("[telegram] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set in .env")
        print("  → Create a bot via @BotFather, then add:")
        print("    TELEGRAM_BOT_TOKEN=your_token")
        print("    TELEGRAM_CHAT_ID=your_chat_id  (use @userinfobot to get your ID)")
    return token, chat_id


def _api_call(token: str, method: str, payload: dict) -> dict:
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data,
                                  headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"[telegram] HTTP {e.code}: {body[:300]}")
        return {"ok": False}
    except Exception as e:
        print(f"[telegram] error: {e}")
        return {"ok": False}


def send_message(token: str, chat_id: str, text: str,
                 reply_markup: dict = None) -> bool:
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    result = _api_call(token, "sendMessage", payload)
    return result.get("ok", False)


def _escape(text: str) -> str:
    """Escape HTML special chars outside of <code> blocks."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ─── Original drafts ──────────────────────────────────────────────────────────

def get_pending_originals(date: str) -> list[dict]:
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM drafts WHERE date=? AND status='pending' ORDER BY id",
        (date,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def send_original_draft(token: str, chat_id: str, draft: dict, index: int) -> bool:
    time_slot = draft.get("recommended_time", "?")
    topic = draft.get("topic", "")
    hook = draft.get("hook_type", "")
    context = _escape(draft.get("context", ""))
    content = draft.get("content", "")

    text = (
        f"<b>Draft {index} — {time_slot}</b>  [{topic}/{hook}]\n"
        f"<i>{context}</i>\n\n"
        f"<code>{_escape(content)}</code>"
    )
    return send_message(token, chat_id, text)


def send_originals(token: str, chat_id: str, date: str) -> int:
    drafts = get_pending_originals(date)
    if not drafts:
        print(f"[telegram] No pending original drafts for {date}")
        return 0

    # Header
    send_message(token, chat_id,
                 f"<b>Drafts originaux — {date}</b>\n{len(drafts)} tweets a poster")

    sent = 0
    for i, draft in enumerate(drafts, 1):
        ok = send_original_draft(token, chat_id, draft, i)
        if ok:
            sent += 1
            print(f"  [ok] Draft {i} ({draft.get('recommended_time','?')})")
        else:
            print(f"  [fail] Draft {i}")

    return sent


# ─── Reply drafts ─────────────────────────────────────────────────────────────

def get_pending_replies(date: str) -> list[dict]:
    conn = get_conn()
    try:
        rows = conn.execute(
            """SELECT * FROM reply_performance
               WHERE date=? AND status='draft'
               ORDER BY opportunity_score DESC""",
            (date,)
        ).fetchall()
    except Exception:
        rows = []
    conn.close()
    return [dict(r) for r in rows]


def send_reply_draft(token: str, chat_id: str, reply: dict, index: int) -> bool:
    handle = reply.get("target_handle", "?")
    score = reply.get("opportunity_score", 0)
    strategy = reply.get("strategy", "")
    target_url = reply.get("target_url", "")
    target_likes = reply.get("target_likes_at_reply", 0)
    reply_text = reply.get("reply_text", "")

    text = (
        f"<b>Reply {index} — @{handle}</b>  "
        f"[{strategy}  score {score:.2f}  {target_likes}L]\n\n"
        f"<code>{_escape(reply_text)}</code>"
    )

    markup = None
    if target_url:
        markup = {
            "inline_keyboard": [[
                {"text": "Open tweet", "url": target_url}
            ]]
        }

    return send_message(token, chat_id, text, reply_markup=markup)


def send_replies(token: str, chat_id: str, date: str) -> int:
    replies = get_pending_replies(date)
    if not replies:
        print(f"[telegram] No pending reply drafts for {date}")
        return 0

    send_message(token, chat_id,
                 f"<b>Reply opportunities — {date}</b>\n{len(replies)} replies a envoyer")

    sent = 0
    for i, reply in enumerate(replies, 1):
        ok = send_reply_draft(token, chat_id, reply, i)
        if ok:
            sent += 1
            print(f"  [ok] Reply {i} @{reply.get('target_handle','?')} ({reply.get('opportunity_score',0):.2f})")
        else:
            print(f"  [fail] Reply {i}")

    return sent


# ─── Main ─────────────────────────────────────────────────────────────────────

def run(date: str = None, only_replies: bool = False, only_originals: bool = False):
    init_db()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    token, chat_id = _get_config()
    if not token or not chat_id:
        return

    total = 0
    if not only_replies:
        n = send_originals(token, chat_id, date)
        print(f"[telegram] {n} original drafts sent")
        total += n

    if not only_originals:
        n = send_replies(token, chat_id, date)
        print(f"[telegram] {n} reply drafts sent")
        total += n

    print(f"[telegram] Done — {total} messages sent to Telegram")


if __name__ == "__main__":
    args = sys.argv[1:]
    date = None
    for i, a in enumerate(args):
        if a == "--date" and i + 1 < len(args):
            date = args[i + 1]

    run(
        date=date,
        only_replies="--replies" in args,
        only_originals="--originals" in args,
    )
