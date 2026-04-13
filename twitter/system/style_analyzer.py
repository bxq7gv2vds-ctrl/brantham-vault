"""
Style Analyzer — analyzes top-performing tweets from the feed to extract
winning patterns and styles. Updates patterns.json with actionable insights.
Run after each scrape session.
"""
import json
import subprocess
from datetime import datetime
from pathlib import Path

from config import PATTERNS_JSON, PATTERNS_DIR
from db import init_db, get_conn


def get_top_performers(limit: int = 60) -> list[dict]:
    """Get highest-engagement tweets from the scraped feed."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT text, author_handle, author_verified,
               likes, retweets, replies, bookmarks, views,
               engagement_rate, topic, hook_type,
               created_at, tweet_url
        FROM feed_tweets
        WHERE is_retweet = 0
          AND likes >= 100
        ORDER BY engagement_rate DESC, likes DESC
        LIMIT ?
    """, (limit,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_style_diversity(limit: int = 40) -> list[dict]:
    """Get diverse sample including lower-engagement but interesting tweets."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT text, author_handle, likes, retweets, bookmarks, views,
               engagement_rate, topic, hook_type, tweet_url
        FROM feed_tweets
        WHERE is_retweet = 0
          AND likes >= 20
          AND length(text) > 30
        ORDER BY RANDOM()
        LIMIT ?
    """, (limit,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def call_claude(prompt: str) -> str:
    """Call claude CLI in non-interactive mode."""
    result = subprocess.run(
        ["claude", "-p", "--output-format", "text"],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=300,
    )
    if result.returncode != 0:
        print(f"[style_analyzer] claude error: {result.stderr[:300]}")
        return ""
    return result.stdout.strip()


def format_tweets_for_analysis(tweets: list[dict]) -> str:
    lines = []
    for i, t in enumerate(tweets, 1):
        # Compact format to reduce token count
        text = (t.get("text") or "")[:200].replace("\n", " ")
        lines.append(
            f"{i}. @{t.get('author_handle')} [{t.get('likes',0)}L/{t.get('bookmarks',0)}BM/{t.get('views',0):,}v] "
            f"[{t.get('topic','?')}/{t.get('hook_type','?')}]: \"{text}\""
        )
    return "\n".join(lines)


def analyze_style() -> dict:
    """Main analysis: ask Claude to identify winning patterns."""
    top = get_top_performers(30)
    diverse = get_style_diversity(20)

    if not top:
        print("[style_analyzer] Not enough data yet. Run scraper first.")
        return {}

    top_text = format_tweets_for_analysis(top)
    diverse_text = format_tweets_for_analysis(diverse[:15])

    prompt = f"""Tu es un expert en croissance Twitter/X. Analyse ces tweets du feed d'un builder AI/tech français.

## OBJECTIF
Identifier les patterns de style qui font qu'un tweet performe exceptionnellement bien dans cette niche.
Je veux construire un compte personnel (builder AI, 24 ans, Paris) et atteindre 10K followers en 6 mois.

## TOP TWEETS (les plus viraux du feed)
{top_text}

## SAMPLE DIVERS (tweets avec engagement modeste mais potentiel)
{diverse_text}

## ANALYSE DEMANDEE
Reponds en JSON valide UNIQUEMENT, sans markdown, avec cette structure exacte:

{{
  "winning_styles": [
    {{
      "name": "nom du style",
      "description": "description courte de ce style",
      "why_it_works": "pourquoi ca engage dans cette niche",
      "example_account": "@handle",
      "template": "structure/template reutilisable",
      "example_tweet": "exemple de tweet avec ce style adapte a Paul (builder AI francais)",
      "estimated_engagement": "low|medium|high|viral"
    }}
  ],
  "top_hooks": [
    {{
      "hook": "formulation du hook",
      "pattern": "pattern abstrait",
      "example": "tweet reel qui utilise ce hook",
      "engagement": "likes observes"
    }}
  ],
  "content_pillars": [
    {{
      "pillar": "nom du pilier",
      "description": "quel contenu",
      "frequency": "% du contenu recommande",
      "why": "pourquoi ce pilier fonctionne pour cette audience"
    }}
  ],
  "anti_patterns": [
    "pattern a eviter 1",
    "pattern a eviter 2"
  ],
  "growth_tactics": [
    {{
      "tactic": "nom de la tactique",
      "how": "comment la mettre en oeuvre",
      "impact": "low|medium|high"
    }}
  ],
  "ideal_voice": {{
    "tone": "description du ton ideal pour percer dans cette niche",
    "length": "longueur optimale des tweets",
    "language_mix": "mix FR/EN recommande",
    "formality": "niveau de formalite",
    "what_makes_follow_worthy": "en 2-3 phrases : pourquoi un user voudrait follow ce compte"
  }},
  "analysis_date": "{datetime.now().strftime('%Y-%m-%d')}",
  "tweets_analyzed": {len(top) + len(diverse)}
}}

Analyse profonde, pas de generalites. Basee uniquement sur les tweets fournis."""

    print(f"[style_analyzer] Analyzing {len(top)} top + {len(diverse)} diverse tweets...")
    response = call_claude(prompt)

    if not response:
        return {}

    # Parse JSON
    try:
        # Try direct parse first
        data = json.loads(response)
    except json.JSONDecodeError:
        # Try to extract JSON from response
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                data = json.loads(response[start:end])
            except json.JSONDecodeError:
                print(f"[style_analyzer] Could not parse JSON response")
                print(f"[style_analyzer] Raw: {response[:500]}")
                return {}
        else:
            return {}

    return data


def save_analysis(data: dict):
    """Save analysis to vault."""
    # Save as JSON
    PATTERNS_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"[style_analyzer] Analysis saved → {PATTERNS_JSON}")

    # Also save as readable markdown
    date = data.get("analysis_date", datetime.now().strftime("%Y-%m-%d"))
    md_path = PATTERNS_DIR / f"style-analysis-{date}.md"

    lines = [
        f"---",
        f"type: style-analysis",
        f"date: {date}",
        f"tweets_analyzed: {data.get('tweets_analyzed', 0)}",
        f"---",
        f"",
        f"# Style Analysis — {date}",
        f"",
    ]

    # Ideal voice
    if voice := data.get("ideal_voice"):
        lines += [
            f"## Voix Idéale",
            f"",
            f"- **Ton :** {voice.get('tone', '')}",
            f"- **Longueur :** {voice.get('length', '')}",
            f"- **Mix FR/EN :** {voice.get('language_mix', '')}",
            f"- **Formalité :** {voice.get('formality', '')}",
            f"",
            f"**Pourquoi on voudrait follow :**",
            f"> {voice.get('what_makes_follow_worthy', '')}",
            f"",
        ]

    # Winning styles
    if styles := data.get("winning_styles"):
        lines += [f"## Styles Gagnants", f""]
        for s in styles:
            lines += [
                f"### {s.get('name')} — `{s.get('estimated_engagement','?')}`",
                f"{s.get('description','')}",
                f"",
                f"**Pourquoi ça marche :** {s.get('why_it_works','')}",
                f"**Template :** `{s.get('template','')}`",
                f"**Exemple pour Paul :** {s.get('example_tweet','')}",
                f"",
            ]

    # Top hooks
    if hooks := data.get("top_hooks"):
        lines += [f"## Top Hooks", f"", f"| Hook | Pattern | Engagement |", f"|------|---------|------------|"]
        for h in hooks[:10]:
            lines.append(f"| {h.get('hook','')} | `{h.get('pattern','')}` | {h.get('engagement','?')} |")
        lines.append("")

    # Content pillars
    if pillars := data.get("content_pillars"):
        lines += [f"## Content Pillars", f""]
        for p in pillars:
            lines += [
                f"### {p.get('pillar','')} — {p.get('frequency','')}",
                f"{p.get('description','')}",
                f"*{p.get('why','')}*",
                f"",
            ]

    # Anti-patterns
    if anti := data.get("anti_patterns"):
        lines += [f"## À Éviter", f""]
        for a in anti:
            lines.append(f"- {a}")
        lines.append("")

    # Growth tactics
    if tactics := data.get("growth_tactics"):
        lines += [f"## Tactiques de Croissance", f"", f"| Tactique | Comment | Impact |", f"|---------|---------|--------|"]
        for t in tactics:
            lines.append(f"| {t.get('tactic','')} | {t.get('how','')} | `{t.get('impact','?')}` |")
        lines.append("")

    lines += [
        f"## Related",
        f"- [[twitter/_MOC]]",
        f"- [[twitter/agent/patterns/hooks-that-work]]",
        f"- [[_system/MOC-patterns]]",
    ]

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[style_analyzer] Markdown report → {md_path}")


def run():
    init_db()
    data = analyze_style()
    if data:
        save_analysis(data)
        print(f"[style_analyzer] Done. Analyzed {data.get('tweets_analyzed', 0)} tweets.")
        print(f"[style_analyzer] Winning styles found: {len(data.get('winning_styles', []))}")
    else:
        print("[style_analyzer] Analysis failed or no data.")


if __name__ == "__main__":
    run()
