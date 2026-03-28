"""
Drafter Agent — generates 7 tweet drafts per day via claude CLI.
Uses local claude auth (subscription), no API key needed.
Drafts are spread across the day with recommended posting times.
"""
import json
import subprocess
from datetime import datetime
from pathlib import Path

from config import (
    VOICE_CARD, BLACKLIST, HOOKS_PATTERNS, TOPICS_RANKING,
    PATTERNS_JSON, DRAFTS, DRAFTS_PER_DAY
)
from db import init_db, save_draft, get_top_feed_tweets, get_all_drafts


POSTING_SCHEDULE = [
    ("07:00", "early — audience US west coast + builders qui dorment pas"),
    ("08:30", "matin — audience pro FR se réveille"),
    ("09:30", "matin — peak FR attention"),
    ("10:30", "matin — peak global attention"),
    ("11:30", "avant-midi — scroll de procrastination"),
    ("12:30", "midi — pause déjeuner"),
    ("13:30", "reprise post-déj"),
    ("14:30", "creux productif — bon pour les threads"),
    ("15:30", "après-midi — audience US east coast se réveille"),
    ("16:30", "fin d'après-midi"),
    ("17:30", "commute — mobile scroll peak"),
    ("18:30", "fin de journée — prime time FR"),
    ("19:30", "soirée — engagement maximal"),
    ("20:30", "prime time global"),
    ("22:30", "late night — builder community US"),
]

DRAFT_TYPES = [
    # poetengineer__ style — builder data avec chiffres
    ("builder_log",    "Builder log précis: quelque chose que Paul a build/observé avec des CHIFFRES exacts. '254 sessions, 3 agents, 40h de code'. Concret et vrai."),
    # Hesamation style — shock hook + observation AI
    ("shock_obs",      "Hook choc sur une observation AI que personne n'a encore verbalisée. Commence par WAIT / 'you wake up' / '> scenario'. Setup + reveal."),
    # Hot take direct
    ("hot_take",       "Opinion tranchée sur l'AI/dev — aucun hedge, affirme direct. Formule: '[sujet] is [jugement]. Here's why.' Max 2 phrases."),
    # Breaking react
    ("breaking_react", "Réaction à la news AI la plus virale du feed — angle inattendu, sous-entendu que les autres ratent"),
    # Builder log 2
    ("builder_log",    "Observation technique concrète: ce que Paul a appris en buildant. Pattern, bug, découverte. Avec code/chiffres si possible."),
    # Frenchie_ style — pour l'audience FR
    ("fr_content",     "Tweet EN FRANÇAIS uniquement. Opener: 'L'état de [sujet] en France :' ou 'Ce que personne dit sur [sujet] :' suivi d'un constat choc."),
    # Question engageante
    ("question",       "Question courte qui force une réponse binaire ou un avis dans la niche AI/builder. Doit créer du débat."),
    # Hot take 2
    ("hot_take",       "Second hot take — sujet différent du draft 3. Ton plus provocateur. Contre-pied d'une croyance commune dans la niche."),
    # poetengineer__ style 2
    ("builder_log",    "Micro-observation du quotidien builder: une chose précise remarquée aujourd'hui en buildant avec Claude. Court et factuel."),
    # Hesamation style 2
    ("shock_obs",      "Second tweet narratif Hesamation-style: setup en bullet points '>' ou '—' qui décrit un scenario builder/AI relatable. Punchline finale."),
    # Humor
    ("humor",          "Humour sec — vie de dev: localhost qui crash, context window plein, 3h du mat, token limit. Une situation absurde mais vraie."),
    # Prediction
    ("prediction",     "Prédiction concrète sur AI/dev avec timeline précise. 'In 6 months...' ou 'By end of 2026...'. Doit être audacieux mais défendable."),
    # Authority challenge
    ("hot_take",       "Démonte une croyance mainstream sur l'AI. 'Everyone says X. They're wrong.' Avec une vraie contre-argument."),
    # Thread opener
    ("thread_opener",  "Premier tweet d'un thread: hook qui force à cliquer 'show more'. Format: titre accrocheur + 'Thread:' ou numérotation."),
    # Late night builder
    ("builder_log",    "Tweet late-night authentique — ce que Paul est en train de builder maintenant, heure tardive. Crédible et spécifique."),
]


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def call_claude(prompt: str, model: str = "sonnet") -> str:
    """Call claude CLI in non-interactive mode — uses subscription auth."""
    result = subprocess.run(
        ["claude", "-p", "--output-format", "text", "--model", model],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=180,
    )
    if result.returncode != 0:
        print(f"[drafter] claude error: {result.stderr[:300]}")
        return ""
    return result.stdout.strip()


def load_style_patterns() -> str:
    """Load the latest style analysis if available."""
    if PATTERNS_JSON.exists():
        try:
            data = json.loads(PATTERNS_JSON.read_text(encoding="utf-8"))
            lines = ["## PATTERNS GAGNANTS (issus de l'analyse du feed)"]

            if voice := data.get("ideal_voice"):
                lines.append(f"Voix idéale: {voice.get('tone','')}. {voice.get('what_makes_follow_worthy','')}")

            if styles := data.get("winning_styles", [])[:4]:
                lines.append("\nStyles qui performent:")
                for s in styles:
                    lines.append(f"- [{s.get('estimated_engagement','?')}] {s.get('name','')}: {s.get('template','')}")

            if hooks := data.get("top_hooks", [])[:6]:
                lines.append("\nTop hooks:")
                for h in hooks:
                    lines.append(f"- \"{h.get('hook','')}\" ({h.get('engagement','?')} likes)")

            if anti := data.get("anti_patterns", []):
                lines.append(f"\nÀ éviter: {', '.join(anti[:4])}")

            return "\n".join(lines)
        except (json.JSONDecodeError, KeyError):
            pass
    return ""


def load_style_dna() -> str:
    """Load style DNA from reference accounts — injected into every draft prompt."""
    try:
        import json
        dna_dir = Path("/Users/paul/twitter-agent/knowledge-graph/reply_dna")
        lines = ["## STYLE DNA — Comptes de référence (inspire le HOW, pas le WHAT)\n"]

        refs = {
            "poetengineer__": "BASE quotidien — builder data avec chiffres, concret, authentique",
            "Hesamation":     "VIRAL — shock hook + narrative setup, observation AI tranchante",
            "steipete":       "REPLIES — one-liner direct, 56c avg, aucun fluff",
            "Frenchie_":      "FR CONTENT — opener 'L'état de X :' + constat choc",
        }
        for handle, role in refs.items():
            path = dna_dir / f"{handle.lower()}_deep.json"
            if not path.exists():
                path = dna_dir / f"{handle.lower()}.json"
            if not path.exists():
                continue
            d = json.loads(path.read_text())
            if d.get("error"):
                continue
            avg_l = d.get("avg_length_top") or d.get("avg_reply_length", "?")
            top_fmt = list((d.get("top_formats") or {}).keys())[:2] or d.get("winning_structures", [])[:2]
            lines.append(f"@{handle} [{role}]")
            lines.append(f"  Longueur: {avg_l}c | Formats: {'/'.join(top_fmt)}")
            # Best tweet examples
            best = d.get("best_tweets") or d.get("exemplars") or []
            for ex in best[:2]:
                text = (ex.get("text") or ex.get("text", ""))[:140].replace("\n", " ")
                likes = ex.get("likes", 0)
                lines.append(f'  [{likes}L] "{text}"')
            lines.append("")

        return "\n".join(lines)
    except Exception:
        return ""


def load_ml_context(date: str) -> str:
    """Load ML intelligence context from orchestrator (topic model, FAISS, fingerprints)."""
    try:
        from orchestrator import build_context_for_prompt
        return build_context_for_prompt(date)
    except Exception as e:
        return f"[ML context unavailable: {e}]"


def build_prompt(feed_highlights: list[dict], date: str) -> str:
    voice = read_file(VOICE_CARD)
    blacklist = read_file(BLACKLIST)
    style_patterns = load_style_patterns()
    ml_context = load_ml_context(date)
    style_dna = load_style_dna()

    # Format feed highlights
    feed_text = ""
    for i, t in enumerate(feed_highlights[:20], 1):
        views = t.get("views", 0)
        feed_text += (
            f"{i}. @{t.get('author_handle')} | "
            f"{t.get('likes',0)}L {t.get('retweets',0)}RT {t.get('bookmarks',0)}BM {views:,}v\n"
            f"   \"{t.get('text','')[:240]}\"\n"
            f"   tweet_url: {t.get('tweet_url','')}\n\n"
        )

    schedule_text = "\n".join([f"- {t}: {d}" for t, d in POSTING_SCHEDULE])
    types_text = "\n".join([f"Draft {i+1} ({tp}): {desc}" for i, (tp, desc) in enumerate(DRAFT_TYPES)])

    return f"""Tu génères des tweets pour Paul Roulleau. Réponds UNIQUEMENT en JSON valide (pas de markdown, pas d'explication).

## QUI EST PAUL
{voice}

## BLACKLIST ABSOLUE (ne jamais utiliser ces mots/patterns)
{blacklist}

{style_dna}

{style_patterns}

## INTELLIGENCE ML — Tendances, topics, tweets similaires haute-performance
{ml_context}

## FEED DU JOUR — Top tweets {date} (pour contexte et réactions)
{feed_text}

## PROGRAMME DE PUBLICATION
{schedule_text}

## TYPES DE DRAFTS À GÉNÉRER (dans l'ordre)
{types_text}

## CONTEXTE DE PAUL (pour l'authenticité, pas pour promouvoir quoi que ce soit)
- Utilise Claude Code 10h/jour, sessions marathon 5-11h
- Build des agents AI autonomes en solo
- Stack: Python, FastAPI, Next.js 15, Playwright, PostgreSQL
- EDHEC BBA, 24 ans, Paris
- Power user AI — il teste tout avant les autres
- Claude > GPT pour le code, conviction forte depuis 6 mois

## IMPORTANT — SUJETS INTERDITS DANS LES DRAFTS
- Toute référence à Brantham Partners
- M&A, redressement judiciaire, procédures collectives, BODACC
- Clients, deals, consulting
Ce compte est personnel. On parle d'AI, de tech, de builder culture. C'est tout.

## FORMAT DE SORTIE STRICT
JSON pur, pas de code block, pas de texte avant/après:
{{
  "drafts": [
    {{
      "content": "texte exact du tweet",
      "format": "single|reply|thread_opener",
      "topic": "llm_models|ai_agents|builders|automation|hot_take|humor|breaking_news",
      "hook_type": "prediction|builder_flex|breaking_news|hot_take|humor|question|statement",
      "recommended_time": "HH:MM",
      "context": "1 ligne: pourquoi ce tweet maintenant",
      "reply_to_url": "URL du tweet si c'est une reply, sinon null"
    }}
  ]
}}

Génère exactement {DRAFTS_PER_DAY} drafts. Test chaque draft: "Un pote de Paul lirait ça et dirait 'ouais c'est du Paul ca' ?" Si non, recommence."""


def write_draft_queue(drafts: list[dict], date: str):
    lines = [
        f"---",
        f"type: drafts",
        f"date: {date}",
        f"status: pending-review",
        f"---",
        f"",
        f"# Drafts {date} — En attente de review",
        f"",
        f"> Change `[PENDING]` → `[A]` (approve) ou `[R]` (reject).",
        f"> Édite le texte entre ``` si tu veux modifier.",
        f"> Ensuite: `python main.py post`",
        f"",
    ]

    for i, d in enumerate(drafts, 1):
        reply_note = f" | REPLY → {d.get('reply_to_url','')}" if d.get("reply_to_url") else ""
        lines += [
            f"---",
            f"",
            f"## Draft {i} — {d.get('recommended_time','?')} — {d.get('topic','?')}/{d.get('hook_type','?')}{reply_note}",
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
    print(f"[drafter] Draft queue → {path}")


def run(date: str = None):
    init_db()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    existing = get_all_drafts(date)
    if existing:
        print(f"[drafter] {len(existing)} drafts already exist for {date}")
        return existing

    feed_highlights = get_top_feed_tweets(limit=20, min_likes=50)
    print(f"[drafter] Feed context: {len(feed_highlights)} top tweets")

    prompt = build_prompt(feed_highlights, date)

    print(f"[drafter] Calling claude CLI...")
    response = call_claude(prompt)

    if not response:
        print("[drafter] No response from claude CLI")
        return []

    # Parse JSON
    raw_drafts = []
    try:
        data = json.loads(response)
        raw_drafts = data.get("drafts", [])
    except json.JSONDecodeError:
        # Try to extract JSON
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                data = json.loads(response[start:end])
                raw_drafts = data.get("drafts", [])
            except json.JSONDecodeError:
                print(f"[drafter] JSON parse error. Raw: {response[:400]}")
                return []

    print(f"[drafter] {len(raw_drafts)} drafts generated")

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

    write_draft_queue(saved, date)
    print(f"[drafter] Done. Review: vault/twitter/agent/drafts/{date}.md")
    return saved


if __name__ == "__main__":
    run()
