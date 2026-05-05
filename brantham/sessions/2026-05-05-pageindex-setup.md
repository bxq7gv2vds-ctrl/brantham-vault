---
date: 2026-05-05
type: session
project: brantham
tags: [tooling, rag, data-room, pageindex]
---

# Session 2026-05-05 — Setup PageIndex pour data rooms M&A

## Objectif

Évaluer puis intégrer [PageIndex](https://github.com/VectifyAI/PageIndex) (Vectify AI) — RAG arborescent vectorless — dans le process Brantham, de manière naturellement utilisable.

## Décisions

- Adoption confirmée pour PDFs > 100 pages des data rooms M&A actives → [[founder/decisions/2026-05-05-pageindex-data-rooms]]
- Pattern Brantham documenté → [[brantham/patterns/data-room-pageindex]]
- Hors scope : vault interne (QMD couvre), Pappers structuré (API JSON), PDFs courts (Claude direct)

## Ce qui a été fait

1. **Clone + venv** : `~/tools/pageindex/` (uv Python 3.13, deps installées avec fix `python-dotenv==1.0.1` pour compat litellm)
2. **Wrapper CLI** : `~/tools/pageindex/bin/brantham-pageindex` symlinké dans `~/.local/bin/`
   - Usage : `brantham-pageindex <deal-slug> <pdf-path>`
   - Output : `vault/brantham/deals/active/<slug>/_dataroom/<pdf>.tree.json`
   - Auto-wikilink ajouté dans `_MOC.md` du deal
3. **Backend Claude CLI** (au lieu de LiteLLM) : `~/tools/pageindex/pageindex/claude_cli_backend.py`
   - `llm_completion` / `llm_acompletion` shell-out vers `claude -p --model claude-sonnet-4-5`
   - Auth Claude Code OAuth — **aucune clé API requise**
   - Switch via env var : `PAGEINDEX_BACKEND=litellm` pour repasser sur clé API
4. **Skill Claude Code** : `/pageindex` (`~/.claude/skills/pageindex/SKILL.md`)
5. **Test end-to-end validé** : Disney Q1 FY25 earnings (22 pages) → tree JSON 56 KB, **TOC accuracy 100 %**, hiérarchie 4 niveaux propre, citations page-level.

## Pour reprendre

Workflow type sur un nouveau deal avec data room :

```bash
brantham-pageindex itfi-groupe ~/Downloads/itfi-comptes-2024.pdf
```

Le tree JSON apparaît dans Obsidian sous le deal, linké automatiquement. Q&A reasoning-based via le skill `/pageindex` ou en chargeant le JSON directement.

## Notes techniques

- `--bare` casse l'auth Claude Code (force ANTHROPIC_API_KEY) → utiliser `--no-session-persistence` à la place
- `python-dotenv 1.2.2` (requirements.txt) incompatible avec `litellm 1.83.7` qui pin `1.0.1` → install manuelle des deps
- Le backend custom monkey-patch `pageindex/utils.py` proprement avec un switch `PAGEINDEX_BACKEND`

## Validation production

À tester sur la première vraie data room reçue (ITFI extension ou Magic Form). Si l'écart de précision vs Claude direct justifie le tooling → industrialiser sur tous les deals. Sinon → restreindre aux pactes + liasses fiscales lourdes.

## Related

- [[brantham/_MOC]]
- [[founder/decisions/2026-05-05-pageindex-data-rooms]]
- [[brantham/patterns/data-room-pageindex]]
- [[brantham/deals/active/itfi-groupe/_MOC]]
- [[brantham/deals/active/magic-form-levallois/_MOC]]
