"""
Reply Guy — Smart reply system for Twitter growth.
Finds live viral opportunities, generates high-value contextual replies,
tracks performance, and learns what works.

Strategy: Be the most insightful person in the thread.
- add_fact: concrete data/example the author missed
- counter_nuance: agree but add important nuance
- builder_proof: "I built X and found..."
- predict_extend: extend their prediction logically
- smart_question: question that shows deep understanding

Usage:
  python reply_guy.py                  — generate 10 reply drafts
  python reply_guy.py --n 15           — generate N reply drafts
  python reply_guy.py --live-only      — bird only, skip DB
  python reply_guy.py --patterns       — show what's working
  python reply_guy.py --track          — sync reply metrics
"""
import json
import re
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))
from config import DRAFTS, DB_PATH, VOICE_CARD, BLACKLIST
from db import init_db, get_conn, save_draft


# ─── Tier config ─────────────────────────────────────────────────────────────

TIER_1 = {
    # Mega accounts in our niche — reply here = free distribution
    "karpathy", "levelsio", "swyx", "sama", "paulg", "naval",
    "alexalbert__", "steipete", "gregisenberg", "emollick",
    "ylecun", "benedictevans", "cdixon",
}

TIER_2 = {
    # Engaged niche communities
    "buccocapital", "roundtablespace", "_akhaliq", "therundownai",
    "noahzweben", "poetengineer__", "vivoplt", "canteverdie",
    "hesamation", "highyieldharry", "bcherny", "ericliujt",
    "frenchiee", "melvynx", "0xmaxou", "thismacapital", "brivaelfr",
    "shafu0x", "spencerhakimian", "lydiahallie",
}

TIER_3 = {
    # Reply if the tweet is fire
    "nousresearch", "openai", "therundownai", "semianalysis_",
    "arafatkatze", "zostaff", "sawyerhood", "stratechery",
}

# Bird search queries for hunting reply opportunities
REPLY_HUNT_QUERIES = [
    "Claude Code shipped builder 2026",
    "AI agents autonomous workflow actually",
    "LLM hot take developers wrong",
    "solo founder AI built product",
    "MCP server Claude agent workflow",
    "vibe coding reality experience",
    "cursor claude copilot comparison developer",
    "AI automation replaced developer job",
]

STRATEGY_INSTRUCTIONS = {
    "add_fact": (
        "Ajoute un fait concret, une donnée précise ou un exemple réel que l'auteur n'a pas mentionné. "
        "Sois spécifique — pas de généralités."
    ),
    "counter_nuance": (
        "Reconnais le point principal mais ajoute une nuance critique ou un cas limite important "
        "que l'auteur a omis. Ne sois pas agressif."
    ),
    "builder_proof": (
        "Réponds avec une preuve personnelle de Paul: 'j'ai build X et j'ai constaté Y'. "
        "Doit être crédible (Paul build des agents AI en Python/Claude)."
    ),
    "predict_extend": (
        "Étends logiquement leur prédiction ou observation avec une conséquence qu'ils n'ont pas vue. "
        "'Et la suite logique c'est...'"
    ),
    "smart_question": (
        "Pose une question courte et précise qui montre que tu comprends le sujet en profondeur "
        "et qui force une réflexion. Pas de question rhétorique."
    ),
}


# ─── DB schema ───────────────────────────────────────────────────────────────

def init_reply_table():
    conn = get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS reply_performance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            target_tweet_id TEXT,
            target_handle TEXT,
            target_likes_at_reply INTEGER DEFAULT 0,
            target_url TEXT NOT NULL,
            reply_text TEXT NOT NULL,
            reply_tweet_id TEXT,
            reply_url TEXT,
            reply_likes INTEGER DEFAULT 0,
            reply_retweets INTEGER DEFAULT 0,
            reply_views INTEGER DEFAULT 0,
            opportunity_score REAL DEFAULT 0,
            strategy TEXT,
            topic TEXT,
            status TEXT DEFAULT 'draft',
            created_at TEXT DEFAULT (datetime('now')),
            posted_at TEXT,
            tracked_at TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_reply_date ON reply_performance(date);
        CREATE INDEX IF NOT EXISTS idx_reply_status ON reply_performance(status);
        CREATE INDEX IF NOT EXISTS idx_reply_handle ON reply_performance(target_handle);
    """)
    conn.commit()
    conn.close()


def save_reply_draft_db(date: str, target: dict, reply_text: str,
                        score: float, strategy: str) -> int:
    conn = get_conn()
    cur = conn.execute("""
        INSERT INTO reply_performance
        (date, target_tweet_id, target_handle, target_likes_at_reply,
         target_url, reply_text, opportunity_score, strategy, topic, status)
        VALUES (?,?,?,?,?,?,?,?,?,?)
    """, (
        date,
        target.get("id", ""),
        target.get("author_handle", ""),
        target.get("likes", 0),
        target.get("tweet_url", ""),
        reply_text,
        score,
        strategy,
        target.get("topic", "other"),
        "draft",
    ))
    reply_id = cur.lastrowid
    conn.commit()
    conn.close()
    return reply_id


def get_replied_handles_today(date: str) -> set:
    """Avoid replying twice to same account in one day."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT DISTINCT LOWER(target_handle) FROM reply_performance
        WHERE date = ? AND status IN ('draft', 'approved', 'posted')
    """, (date,)).fetchall()
    conn.close()
    return {r[0] for r in rows if r[0]}


def get_reply_patterns() -> dict:
    """Analyze which strategies/topics work best from tracked replies."""
    conn = get_conn()

    by_strategy = conn.execute("""
        SELECT strategy, COUNT(*) as n,
               AVG(reply_likes) as avg_likes,
               AVG(reply_views) as avg_views
        FROM reply_performance
        WHERE status = 'tracked' AND reply_likes IS NOT NULL
        GROUP BY strategy ORDER BY avg_likes DESC
    """).fetchall()

    by_topic = conn.execute("""
        SELECT topic, COUNT(*) as n, AVG(reply_likes) as avg_likes
        FROM reply_performance WHERE status = 'tracked'
        GROUP BY topic ORDER BY avg_likes DESC
    """).fetchall()

    best_replies = conn.execute("""
        SELECT reply_text, strategy, topic, reply_likes, target_handle
        FROM reply_performance
        WHERE status = 'tracked' AND reply_likes >= 3
        ORDER BY reply_likes DESC LIMIT 15
    """).fetchall()

    conn.close()
    return {
        "by_strategy": [dict(r) for r in by_strategy],
        "by_topic": [dict(r) for r in by_topic],
        "best_replies": [dict(r) for r in best_replies],
    }


# ─── Bird helpers ─────────────────────────────────────────────────────────────

def _get_auth() -> tuple[str, str]:
    try:
        auth_path = Path.home() / ".config" / "clix" / "auth.json"
        data = json.loads(auth_path.read_text())
        acct = data.get("accounts", {}).get("default", data.get("default", {}))
        return acct.get("auth_token", ""), acct.get("ct0", "")
    except Exception:
        return "", ""


def _bird_env() -> dict:
    token, ct0 = _get_auth()
    return {
        "AUTH_TOKEN": token, "CT0": ct0,
        "PATH": "/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin",
    }


def bird_search(query: str, n: int = 20) -> list[dict]:
    env = _bird_env()
    if not env["AUTH_TOKEN"]:
        return []
    result = subprocess.run(
        ["bird", "search", query, "-n", str(n)],
        capture_output=True, text=True, timeout=30, env=env,
    )
    return _parse_bird(result.stdout) if result.returncode == 0 and result.stdout else []


def bird_read_thread(url_or_id: str) -> str:
    """Read a full thread for context before replying."""
    env = _bird_env()
    if not env["AUTH_TOKEN"]:
        return ""
    result = subprocess.run(
        ["bird", "thread", url_or_id],
        capture_output=True, text=True, timeout=30, env=env,
    )
    return result.stdout[:3000] if result.returncode == 0 else ""


def _parse_bird(text: str) -> list[dict]:
    tweets = []
    current = {}
    for line in text.splitlines():
        line = line.strip()
        m = re.match(r'^@(\S+)\s*\(([^)]+)\):', line)
        if m:
            if current.get("text"):
                tweets.append(current)
            current = {
                "author_handle": m.group(1), "author_name": m.group(2),
                "text": "", "likes": 0, "retweets": 0, "views": 0,
            }
        elif line.startswith("📅 "):
            try:
                dt = datetime.strptime(line[2:].strip(), "%a %b %d %H:%M:%S +0000 %Y")
                current["created_at"] = dt.replace(tzinfo=timezone.utc).isoformat()
            except ValueError:
                current["created_at"] = datetime.now(timezone.utc).isoformat()
        elif line.startswith("🔗 "):
            url = line[2:].strip()
            current["tweet_url"] = url
            m_id = re.search(r'/status/(\d+)', url)
            if m_id:
                current["id"] = m_id.group(1)
        elif re.match(r'^[🔁❤️👁📊]', line):
            nums = re.findall(r'\d+', line.replace(',', ''))
            if '🔁' in line and nums:
                current["retweets"] = int(nums[0])
            elif '❤️' in line and nums:
                current["likes"] = int(nums[0])
            elif '👁' in line and nums:
                current["views"] = int(nums[0])
        elif line.startswith("──"):
            if current.get("text"):
                tweets.append(current)
            current = {}
        elif current and not line.startswith(("┌─", "│", "└─", "ℹ️", "⚠️", "🖼️", "🎬")):
            if line and "text" in current:
                current["text"] = (current["text"] + "\n" + line).strip() if current["text"] else line
    if current.get("text"):
        tweets.append(current)
    return tweets


# ─── Opportunity finding ─────────────────────────────────────────────────────

def _classify_topic(text: str) -> str:
    t = text.lower()
    if any(w in t for w in ["claude", "gpt", "llm", "gemini", "anthropic", "openai"]):
        return "llm_models"
    if any(w in t for w in ["agent", "autonomous", "pipeline", "workflow", "mcp"]):
        return "ai_agents"
    if any(w in t for w in ["built", "build", "shipped", "launched", "indie", "founder", "saas"]):
        return "builders"
    if any(w in t for w in ["automation", "scraping", "deploy", "cursor", "copilot"]):
        return "automation"
    return "other"


def find_live_opportunities(n_queries: int = 4) -> list[dict]:
    """Bird real-time search for fresh viral tweets."""
    all_tweets = []
    seen = set()
    for query in REPLY_HUNT_QUERIES[:n_queries]:
        tweets = bird_search(query, n=15)
        for t in tweets:
            tid = t.get("id") or t.get("tweet_url", "")
            if tid and tid not in seen:
                seen.add(tid)
                if not t.get("topic"):
                    t["topic"] = _classify_topic(t.get("text", ""))
                all_tweets.append(t)
        time.sleep(1.5)
    return all_tweets


def find_from_db(max_age_hours: int = 4, min_likes: int = 50) -> list[dict]:
    """Recent high-value tweets from local DB."""
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
          AND topic IN ('llm_models','ai_agents','builders','automation','breaking_news')
        ORDER BY engagement_rate DESC, likes DESC
        LIMIT 30
    """, (cutoff, min_likes)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ─── Scoring ─────────────────────────────────────────────────────────────────

def _tier_score(handle: str) -> float:
    h = handle.lower()
    if h in TIER_1:
        return 1.0
    if h in TIER_2:
        return 0.65
    if h in TIER_3:
        return 0.40
    return 0.20


def _freshness_score(created_at: str) -> float:
    if not created_at:
        return 0.3
    try:
        ts = created_at.rstrip("Z") + ("+00:00" if created_at.endswith("Z") else "")
        dt = datetime.fromisoformat(ts).replace(tzinfo=timezone.utc) if "+" not in ts else datetime.fromisoformat(ts)
        age = (datetime.now(timezone.utc) - dt).total_seconds() / 60
        if age < 20:   return 1.0
        if age < 60:   return 0.85
        if age < 120:  return 0.65
        if age < 240:  return 0.45
        if age < 480:  return 0.25
        return 0.10
    except Exception:
        return 0.3


def _velocity_score(likes: int, created_at: str) -> float:
    """Likes per hour — proxy for viral momentum."""
    if not created_at:
        return min(likes / 500, 1.0)
    try:
        ts = created_at.rstrip("Z") + ("+00:00" if created_at.endswith("Z") else "")
        dt = datetime.fromisoformat(ts)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        hours = max((datetime.now(timezone.utc) - dt).total_seconds() / 3600, 0.1)
        rate = likes / hours
        return min(rate / 200, 1.0)  # 200 likes/h = 1.0
    except Exception:
        return min(likes / 500, 1.0)


def _replyable_score(text: str) -> float:
    t = text.lower()
    score = 0.45

    if "?" in text[:120]:
        score += 0.30  # Question = easy to reply
    if any(w in t for w in ["wrong", "actually", "hot take", "unpopular", "nobody", "stop"]):
        score += 0.20  # Claim/opinion = easy counter
    if any(w in t for w in ["claude", "gpt", "llm", "cursor", "mcp", "agent", "build"]):
        score += 0.15  # Our domain = add real info
    if any(w in t for w in ["built", "shipped", "launched", "i made"]):
        score += 0.10  # Builder post = share experience

    if len(text) < 80:
        score -= 0.20  # Too short = hard to add value
    if text.startswith("RT @"):
        return 0.05

    return min(max(score, 0.0), 1.0)


def _topic_score(topic: str) -> float:
    return {
        "llm_models": 1.0, "ai_agents": 0.95, "builders": 0.85,
        "automation": 0.70, "breaking_news": 0.60,
    }.get(topic, 0.25)


def score_opportunity(tweet: dict) -> float:
    tier  = _tier_score(tweet.get("author_handle", ""))
    fresh = _freshness_score(tweet.get("created_at", ""))
    vel   = _velocity_score(tweet.get("likes", 0), tweet.get("created_at", ""))
    rep   = _replyable_score(tweet.get("text", ""))
    topic = _topic_score(tweet.get("topic", "other"))

    return round(
        vel   * 0.30 +
        tier  * 0.28 +
        rep   * 0.20 +
        topic * 0.12 +
        fresh * 0.10,
        4
    )


# ─── Reply generation ─────────────────────────────────────────────────────────

def _pick_strategy(tweet: dict, patterns: dict) -> str:
    """Pick strategy based on tweet content + past performance."""
    # If we have performance data, bias toward what works
    if patterns.get("by_strategy") and len(patterns["by_strategy"]) >= 3:
        best_strategy = patterns["by_strategy"][0].get("strategy", "add_fact")
        # But only if it's contextually appropriate
        text = tweet.get("text", "").lower()
        if best_strategy == "builder_proof" and not any(
            w in text for w in ["build", "ship", "made", "created", "code"]
        ):
            pass  # Fall through to heuristic
        else:
            return best_strategy

    # Heuristic fallback
    text = tweet.get("text", "").lower()
    if "?" in tweet.get("text", "")[:120]:
        return "smart_question" if tweet.get("topic") in {"llm_models", "ai_agents"} else "add_fact"
    if any(w in text for w in ["built", "shipped", "launched", "made"]):
        return "builder_proof"
    if any(w in text for w in ["wrong", "unpopular", "hot take", "actually", "nobody"]):
        return "counter_nuance"
    if any(w in text for w in ["will", "future", "next year", "6 months", "prediction"]):
        return "predict_extend"
    return "add_fact"


def _get_exemplars(topic: str, strategy: str, patterns: dict) -> list[dict]:
    best = patterns.get("best_replies", [])
    scored = []
    for r in best:
        s = 0
        if r.get("topic") == topic:    s += 2
        if r.get("strategy") == strategy: s += 1
        if s > 0:
            scored.append((s, r))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [r for _, r in scored[:3]] or best[:2]


def _load_style_dna() -> str:
    """Load compact reply style DNA — key stats + 2 exemplars per account."""
    try:
        import json
        from pathlib import Path
        dna_dir = Path("/Users/paul/twitter-agent/knowledge-graph/reply_dna")
        if not dna_dir.exists():
            return ""

        lines = ["## STYLE DNA (comptes qui ont explosé — inspire le HOW, pas le WHAT)\n"]
        for handle in ["levelsio", "swyx", "Frenchiee", "melvynx"]:
            path = dna_dir / f"{handle.lower()}.json"
            if not path.exists():
                continue
            d = json.loads(path.read_text())
            if d.get("error"):
                continue
            lines.append(f"@{handle} ({d['niche']}): {d['length_guidance']}, "
                         f"structures={'/'.join(d['winning_structures'][:2])}")
            for ex in d.get("exemplars", [])[:2]:
                text = ex["text"][:120].replace("\n", " ")
                lines.append(f'  [{ex["likes"]}L] "{text}"')
        return "\n".join(lines)
    except Exception:
        return ""


def generate_reply(tweet: dict, strategy: str, thread_ctx: str,
                   patterns: dict) -> str:
    """Generate reply via Claude CLI (haiku = fast)."""
    voice = VOICE_CARD.read_text(encoding="utf-8") if VOICE_CARD.exists() else ""
    blacklist = BLACKLIST.read_text(encoding="utf-8") if BLACKLIST.exists() else ""

    strategy_text = STRATEGY_INSTRUCTIONS.get(strategy, STRATEGY_INSTRUCTIONS["add_fact"])
    style_dna = _load_style_dna()

    exemplars = _get_exemplars(tweet.get("topic", ""), strategy, patterns)
    exemplar_block = ""
    if exemplars:
        exemplar_block = "\n## MEILLEURES REPLIES DE PAUL QUI ONT MARCHÉ\n"
        for ex in exemplars:
            exemplar_block += f"- [{ex.get('reply_likes',0)}L | {ex.get('strategy','')}]: \"{ex.get('reply_text','')[:160]}\"\n"

    thread_block = ""
    if thread_ctx and len(thread_ctx.strip()) > 80:
        thread_block = f"\n## CONTEXTE DU THREAD\n{thread_ctx[:1800]}\n"

    prompt = f"""Génère une reply Twitter pour Paul Roulleau (@0xMikeTheIntern). Réponds avec UNIQUEMENT le texte de la reply.

## VOIX DE PAUL
{voice}

## BLACKLIST ABSOLUE
{blacklist}

{style_dna}

## TWEET CIBLE
@{tweet.get('author_handle')}: "{tweet.get('text','')}"
Stats: {tweet.get('likes',0)} likes | {tweet.get('retweets',0)} RT | {tweet.get('views',0):,} vues
URL: {tweet.get('tweet_url','')}
{thread_block}{exemplar_block}
## STRATÉGIE: {strategy.upper()}
{strategy_text}

## RÈGLES STRICTES
1. Maximum 240 caractères — court et dense
2. Minimum 30 caractères — si rien à dire → [SKIP]
3. ZERO emoji, ZERO hashtag
4. Ne commence jamais par "Great", "Exactly", "100%", "Agreed", "This"
5. Inspire-toi du style DNA ci-dessus (longueur, structure, ton) — mais avec le contenu/perspective de Paul
6. Pour builder_proof: "J'ai" ou "I built/shipped" avec quelque chose de crédible et concret
7. Si vraiment rien d'intéressant → réponds UNIQUEMENT: [SKIP]

Reply (texte brut uniquement):"""

    result = subprocess.run(
        ["claude", "-p", "--output-format", "text", "--model", "haiku"],
        input=prompt, capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


# ─── Performance tracking ─────────────────────────────────────────────────────

def track_reply_metrics():
    """Update metrics for posted replies by checking their performance."""
    conn = get_conn()
    to_track = conn.execute("""
        SELECT id, reply_url, reply_tweet_id, target_handle
        FROM reply_performance
        WHERE status = 'posted' AND reply_url IS NOT NULL
          AND (tracked_at IS NULL OR tracked_at < datetime('now', '-6 hours'))
        LIMIT 20
    """).fetchall()
    conn.close()

    if not to_track:
        print("[reply_guy] No posted replies to track")
        return

    env = _bird_env()
    updated = 0
    for row in to_track:
        row = dict(row)
        url = row.get("reply_url") or row.get("reply_tweet_id")
        if not url:
            continue

        result = subprocess.run(
            ["bird", "read", url],
            capture_output=True, text=True, timeout=20, env=env,
        )
        if result.returncode != 0 or not result.stdout:
            continue

        # Parse metrics from bird read output
        likes = retweets = views = 0
        for line in result.stdout.splitlines():
            line = line.strip()
            nums = re.findall(r'\d+', line.replace(',', ''))
            if '❤️' in line and nums:
                likes = int(nums[0])
            elif '🔁' in line and nums:
                retweets = int(nums[0])
            elif '👁' in line and nums:
                views = int(nums[0])

        conn = get_conn()
        conn.execute("""
            UPDATE reply_performance
            SET reply_likes=?, reply_retweets=?, reply_views=?,
                status='tracked', tracked_at=datetime('now')
            WHERE id=?
        """, (likes, retweets, views, row["id"]))
        conn.commit()
        conn.close()

        print(f"  [track] @{row['target_handle']}: {likes}L {retweets}RT {views}v")
        updated += 1
        time.sleep(1.0)

    print(f"[reply_guy] Tracked {updated} replies")


# ─── Main pipeline ─────────────────────────────────────────────────────────────

def run(n: int = 10, live_only: bool = False, date: str = None) -> list[dict]:
    init_db()
    init_reply_table()

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    # Load performance patterns for adaptive strategy selection
    patterns = get_reply_patterns()
    if patterns["best_replies"]:
        print(f"[reply_guy] Loaded {len(patterns['best_replies'])} exemplar replies for learning")

    already_replied = get_replied_handles_today(date)
    if already_replied:
        print(f"[reply_guy] Already targeted today: {', '.join(list(already_replied)[:5])}")

    # Find candidates
    candidates = []

    print("[reply_guy] Hunting live opportunities via bird...")
    live = find_live_opportunities(n_queries=min(4, len(REPLY_HUNT_QUERIES)))
    candidates.extend(live)
    print(f"  → {len(live)} live tweets found")

    if not live_only:
        print("[reply_guy] Checking DB (last 4h)...")
        db_tweets = find_from_db(max_age_hours=4, min_likes=50)
        candidates.extend(db_tweets)
        print(f"  → {len(db_tweets)} from DB")

    # Dedup by tweet ID / URL
    seen, unique = set(), []
    for t in candidates:
        tid = t.get("id") or t.get("tweet_url", "")
        if tid and tid not in seen:
            seen.add(tid)
            unique.append(t)

    # Filter
    filtered = [
        t for t in unique
        if t.get("author_handle", "").lower() not in already_replied
        and not t.get("text", "").startswith("RT @")
        and t.get("author_handle", "").lower() not in {"0xmiketheintern"}
        and len(t.get("text", "")) > 50
        and t.get("topic", "other") != "other"
    ]

    print(f"[reply_guy] {len(filtered)} candidates after filter (from {len(unique)} unique)")

    if not filtered:
        print("[reply_guy] No reply opportunities found")
        return []

    # Score all
    for t in filtered:
        t["_score"] = score_opportunity(t)
    filtered.sort(key=lambda x: x["_score"], reverse=True)

    # Display top opportunities
    print("\nTop reply opportunities:")
    for t in filtered[:8]:
        age = ""
        if t.get("created_at"):
            try:
                ts = t["created_at"].rstrip("Z") + "+00:00"
                dt = datetime.fromisoformat(ts)
                mins = (datetime.now(timezone.utc) - dt).total_seconds() / 60
                age = f"{mins:.0f}m ago"
            except Exception:
                pass
        print(f"  [{t['_score']:.2f}] @{t.get('author_handle','')} "
              f"({t.get('likes',0)}L {age}) — {t.get('text','')[:70]}...")

    # Generate replies for top N
    generated = []
    for tweet in filtered[:n]:
        handle = tweet.get("author_handle", "")
        score = tweet["_score"]

        # Read thread for high-value targets
        thread_ctx = ""
        if score >= 0.55 and tweet.get("tweet_url"):
            print(f"  [ctx] @{handle} thread...")
            thread_ctx = bird_read_thread(tweet["tweet_url"])
            time.sleep(1.0)

        strategy = _pick_strategy(tweet, patterns)
        print(f"  [gen] @{handle} (score={score:.2f} strat={strategy})...", end=" ", flush=True)

        reply_text = generate_reply(tweet, strategy, thread_ctx, patterns)

        # Filter hallucinations and meta-commentary
        BAD_PATTERNS = [
            "je n'ai pas le tweet", "partage le tweet", "copie le lien",
            "je génère la reply", "tu veux que paul", "fournit le tweet",
            "tweet cible", "provide the tweet", "share the tweet",
        ]
        is_bad = any(p in reply_text.lower() for p in BAD_PATTERNS)
        if not reply_text or reply_text.strip() == "[SKIP]" or len(reply_text) < 20 or is_bad:
            print("SKIP")
            continue

        print(f"ok")

        # Save to reply_performance table
        reply_id = save_reply_draft_db(date, tweet, reply_text, score, strategy)

        # Save to drafts queue (for poster.py to handle)
        recommended_time = _reply_time(score)
        draft_id = save_draft(
            date=date,
            content=reply_text,
            format="reply",
            topic=tweet.get("topic", "other"),
            hook_type="statement",
            recommended_time=recommended_time,
            context=f"REPLY [{score:.2f}] @{handle} ({tweet.get('likes',0)}L) {tweet.get('tweet_url','')}",
        )

        generated.append({
            "reply_id": reply_id,
            "draft_id": draft_id,
            "content": reply_text,
            "strategy": strategy,
            "score": score,
            "target_handle": handle,
            "target_url": tweet.get("tweet_url", ""),
            "target_likes": tweet.get("likes", 0),
            "recommended_time": recommended_time,
        })

        print(f"    → \"{reply_text[:100]}\"")
        time.sleep(0.5)

    if generated:
        _write_reply_queue(generated, date)

    print(f"\n[reply_guy] Done — {len(generated)} reply drafts generated")
    return generated


def _reply_time(score: float) -> str:
    """Higher score = reply sooner."""
    now = datetime.now()
    bucket = 15 if score >= 0.65 else 30
    minutes = ((now.minute // bucket) + 1) * bucket
    extra_h = minutes // 60
    minutes %= 60
    hour = (now.hour + extra_h) % 24
    return f"{hour:02d}:{minutes:02d}"


def _write_reply_queue(replies: list[dict], date: str):
    path = DRAFTS / f"{date}.md"
    lines = [f"\n\n---\n## REPLY GUY — {datetime.now().strftime('%H:%M')} "
             f"— {len(replies)} opportunités\n"]

    for r in replies:
        lines += [
            f"\n---\n",
            f"## Reply [{r['score']:.2f}] — {r['recommended_time']} — "
            f"@{r['target_handle']} ({r['target_likes']}L) — {r['strategy']}\n",
            f"**Status:** [PENDING]",
            f"**Reply to:** {r['target_url']}",
            f"**Score:** {r['score']:.2f} | **Strategy:** {r['strategy']}\n",
            f"```",
            r["content"],
            f"```\n",
        ]

    mode = "a" if path.exists() else "w"
    with open(path, mode, encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[reply_guy] → {path}")


def show_patterns():
    init_reply_table()
    p = get_reply_patterns()
    print("\n=== Reply Performance Patterns ===\n")
    if p["by_strategy"]:
        print("By strategy (tracked replies):")
        for s in p["by_strategy"]:
            print(f"  {s['strategy']:20s} n={s['n']:3d} | avg_likes={s.get('avg_likes',0):.1f}")
    else:
        print("No tracked replies yet — post some and run --track")

    if p["by_topic"]:
        print("\nBy topic:")
        for t in p["by_topic"]:
            print(f"  {t['topic']:20s} n={t['n']:3d} | avg_likes={t.get('avg_likes',0):.1f}")

    if p["best_replies"]:
        print("\nBest performing replies:")
        for r in p["best_replies"][:5]:
            print(f"  [{r['reply_likes']}L @{r['target_handle']} | {r['strategy']}] "
                  f"\"{r['reply_text'][:90]}\"")


if __name__ == "__main__":
    n = 10
    live_only = False
    do_track = False
    do_patterns = False

    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--n" and i + 1 < len(args):
            n = int(args[i + 1])
        if a == "--live-only":
            live_only = True
        if a == "--track":
            do_track = True
        if a == "--patterns":
            do_patterns = True

    if do_patterns:
        show_patterns()
    elif do_track:
        init_db()
        init_reply_table()
        track_reply_metrics()
    else:
        replies = run(n=n, live_only=live_only)
        print(f"\nTotal: {len(replies)} reply drafts ready")
