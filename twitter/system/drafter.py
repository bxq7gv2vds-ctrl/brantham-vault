"""
Drafter Agent — generates 7 tweet drafts per day via Claude API.
Drafts are spread across the day with recommended posting times.
"""
import json
from datetime import datetime
from pathlib import Path

import anthropic

from config import (
    ANTHROPIC_API_KEY, CLAUDE_MODEL,
    VOICE_CARD, BLACKLIST, HOOKS_PATTERNS, TOPICS_RANKING,
    DRAFTS, DRAFTS_PER_DAY
)
from db import init_db, save_draft, get_top_feed_tweets, get_all_drafts


# Posting schedule throughout the day
POSTING_SCHEDULE = [
    ("08:30", "matin — audience pro FR se reveille"),
    ("10:30", "matin — peak attention travail"),
    ("12:30", "midi — pause dejeuner scroll"),
    ("15:00", "apres-midi — creux productif"),
    ("18:30", "fin de journee — debrief"),
    ("20:30", "soiree — prime time global"),
    ("22:30", "late night — builder community"),
]

DRAFT_TYPES = [
    ("hot_take", "Hot take / opinion tranchee — pas de hedge, affirme direct"),
    ("breaking_react", "Reaction a une news du feed — etre le premier, angle inattendu"),
    ("builder_log", "Builder log avec chiffres concrets — ce que tu build"),
    ("reply_thread", "Reply strategique sous un tweet viral du feed — ajouter une info, pas juste 'good take'"),
    ("hot_take", "Second hot take — sujet different du premier"),
    ("builder_log", "Observation technique — un truc que tu as realise en buildant"),
    ("humor", "Humor sec sur la vie de dev/builder — relatable, pas force"),
]


def read_file(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def build_system_prompt() -> str:
    voice = read_file(VOICE_CARD)
    blacklist = read_file(BLACKLIST)
    hooks = read_file(HOOKS_PATTERNS)
    topics = read_file(TOPICS_RANKING)

    return f"""Tu es l'agent Twitter de Paul Roulleau. Tu dois generer des tweets qui sonnent EXACTEMENT comme lui.

## QUI EST PAUL
{voice}

## PATTERNS DE HOOKS QUI MARCHENT
{hooks}

## TOPICS ET LEUR ENGAGEMENT
{topics}

## BLACKLIST ABSOLUE — JAMAIS UTILISER CES MOTS
{blacklist}

## REGLES DE GENERATION
1. Chaque tweet doit passer le test : "Est-ce qu'un pote de Paul dirait 'ouais c'est du Paul ca' ?"
2. Phrases courtes. Fragments autorises. Pas de ponctuation systematique.
3. Franglais naturel — pas force, juste quand ca vient naturellement.
4. Zero emoji sauf usage ironique RARE.
5. Varier la longueur des phrases (burstiness anti-AI).
6. Pas de transition lisse entre idees — sauter directement au point.
7. Les chiffres doivent etre SPECIFIQUES et VRAIS (issus du feed ou du contexte de Paul).
8. Pour les replies : ajouter une INFO ou un CONTREPOINT, jamais "good take" ou "exactly".

## FORMAT DE SORTIE
Tu generes exactement un JSON valide avec ce schema :
{{
  "drafts": [
    {{
      "content": "texte du tweet",
      "format": "single|reply|thread_opener",
      "topic": "llm_models|ai_agents|builders|automation|hot_take|humor|breaking_news",
      "hook_type": "prediction|builder_flex|breaking_news|hot_take|humor|question|statement",
      "recommended_time": "HH:MM",
      "context": "en 1 ligne : pourquoi ce tweet maintenant, quelle inspiration du feed"
    }}
  ]
}}

Genere exactement {DRAFTS_PER_DAY} drafts. Pas plus, pas moins. JSON pur, sans markdown."""


def build_user_prompt(feed_highlights: list[dict], date: str) -> str:
    # Format top tweets from feed as context
    feed_text = ""
    for i, t in enumerate(feed_highlights[:15], 1):
        eng = t.get("engagement", {}) if isinstance(t.get("engagement"), dict) else {
            "likes": t.get("likes", 0),
            "retweets": t.get("retweets", 0),
            "bookmarks": t.get("bookmarks", 0),
            "views": t.get("views", 0),
        }
        feed_text += (
            f"{i}. @{t.get('author_handle')} [{t.get('topic','?')}/{t.get('hook_type','?')}]\n"
            f"   \"{t.get('text','')[:200]}\"\n"
            f"   {eng.get('likes',0)}L · {eng.get('retweets',0)}RT · {eng.get('bookmarks',0)}BM · {eng.get('views',0):,}v\n\n"
        )

    schedule_text = "\n".join([f"- {time}: {desc}" for time, desc in POSTING_SCHEDULE])
    types_text = "\n".join([f"- Draft {i+1} ({t[0]}): {t[1]}" for i, t in enumerate(DRAFT_TYPES)])

    return f"""Date : {date}

## FEED DU JOUR — Top tweets niche (inspiration pour les reactions et le contexte)
{feed_text}

## PROGRAMME DE PUBLICATION
{schedule_text}

## TYPES DE DRAFTS A GENERER (dans cet ordre)
{types_text}

Genere les {DRAFTS_PER_DAY} drafts. Utilise le feed pour :
- Les reactions / breaking news : cite ou reagis a un tweet specifique du feed
- Le contexte du marche AI today
- Les chiffres et faits recents

Pour les builder logs : utilise les chiffres REELS de Paul (3900 procedures/jour, 6 agents, 184K procedures scrapees, Cox C-index 0.84, Claude Code 10h/jour).
"""


def write_draft_queue(drafts: list[dict], date: str):
    """Write human-readable approval queue to vault."""
    lines = [
        f"---",
        f"type: drafts",
        f"date: {date}",
        f"status: pending-review",
        f"---",
        f"",
        f"# Drafts {date} — En attente de review",
        f"",
        f"> **Instructions** : Change `[PENDING]` en `[A]` (approve), `[R]` (reject), ou edite le contenu.",
        f"> Ensuite lance : `python main.py post --date {date}`",
        f"",
    ]

    for i, d in enumerate(drafts, 1):
        lines += [
            f"---",
            f"",
            f"## Draft {i} — {d.get('recommended_time', '?')} — {d.get('topic','?')} / {d.get('hook_type','?')}",
            f"",
            f"**Status:** [PENDING]",
            f"**Context:** {d.get('context','')}",
            f"",
            f"```",
            d.get("content", ""),
            f"```",
            f"",
        ]

    path = DRAFTS / f"{date}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[drafter] Draft queue written → {path}")


def run(date: str = None):
    init_db()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    # Check if drafts already exist for today
    existing = get_all_drafts(date)
    if existing:
        print(f"[drafter] {len(existing)} drafts already exist for {date}, skipping generation")
        return existing

    # Get feed highlights from DB
    feed_highlights = get_top_feed_tweets(limit=20, min_likes=30)
    print(f"[drafter] Using {len(feed_highlights)} feed highlights as context")

    # Build prompts
    system = build_system_prompt()
    user = build_user_prompt(feed_highlights, date)

    # Call Claude API
    print(f"[drafter] Calling Claude {CLAUDE_MODEL}...")
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": user}],
    )

    response_text = message.content[0].text.strip()

    # Parse JSON response
    try:
        data = json.loads(response_text)
        raw_drafts = data.get("drafts", [])
    except json.JSONDecodeError as e:
        print(f"[drafter] JSON parse error: {e}")
        print(f"[drafter] Raw response (first 500 chars): {response_text[:500]}")
        return []

    print(f"[drafter] {len(raw_drafts)} drafts generated")

    # Save to DB
    saved = []
    for d in raw_drafts:
        draft_id = save_draft(
            date=date,
            content=d.get("content", ""),
            format=d.get("format", "single"),
            topic=d.get("topic", "other"),
            hook_type=d.get("hook_type", "statement"),
            recommended_time=d.get("recommended_time", "12:00"),
            context=d.get("context", ""),
        )
        d["id"] = draft_id
        saved.append(d)

    # Write human-readable queue to vault
    write_draft_queue(saved, date)

    print(f"[drafter] Done. Review at: vault/twitter/agent/drafts/{date}.md")
    return saved


if __name__ == "__main__":
    run()
