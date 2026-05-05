---
date: 2026-05-05
type: remember
session: pageindex-setup
---

# Remember 2026-05-05 — PageIndex setup

## Done
- PageIndex (Vectify AI) cloné dans `~/tools/pageindex/`
- venv uv Python 3.13, deps installées (`python-dotenv==1.0.1` requis pour litellm 1.83.7)
- Backend custom `claude_cli_backend.py` shell-out vers `claude -p` (auth Claude Code OAuth, no API key)
- Wrapper CLI : `brantham-pageindex <deal-slug> <pdf-path>` dans `~/.local/bin/`
- Skill `/pageindex` créé
- Test E2E validé : Disney Q1 FY25 (22 pages) → tree JSON 56 KB, TOC accuracy 100 %

## Files créés
- `~/tools/pageindex/pageindex/claude_cli_backend.py` (backend custom)
- `~/tools/pageindex/bin/brantham-pageindex` (wrapper CLI)
- `~/.claude/skills/pageindex/SKILL.md` (skill)
- `vault/founder/decisions/2026-05-05-pageindex-data-rooms.md`
- `vault/brantham/patterns/data-room-pageindex.md`
- `vault/brantham/sessions/2026-05-05-pageindex-setup.md`
- `~/.claude/projects/-Users-paul/memory/pageindex_setup.md`

## Files modifiés
- `~/tools/pageindex/pageindex/utils.py` (switch backend via `PAGEINDEX_BACKEND` env)
- `~/tools/pageindex/pageindex/config.yaml` (model = claude-sonnet-4-5)
- `vault/brantham/deals/active/itfi-groupe/_MOC.md` (section Data room PageIndex)
- `vault/_system/MOC-decisions.md`, `MOC-patterns.md`
- `~/.claude/projects/-Users-paul/memory/MEMORY.md`

## Usage immédiat
```bash
brantham-pageindex <deal-slug> <pdf-path>
```
Plug & play tant que `claude` CLI est loggé. Aucune clé API.

## Related
- [[brantham/sessions/2026-05-05-pageindex-setup]]
- [[founder/decisions/2026-05-05-pageindex-data-rooms]]
- [[brantham/patterns/data-room-pageindex]]
