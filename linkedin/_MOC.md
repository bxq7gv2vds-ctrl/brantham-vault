---
type: moc
domain: linkedin
created: 2026-05-10
---

# LinkedIn — MOC

Capture du feed LinkedIn via userscript Tampermonkey, parsing voyager JSON, scoring reply ROI, et drafts auto.

## Pipeline

1. **Capture** : `userscript/linkedin-feed-capture.user.js` hook fetch/XHR, forward vers `localhost:7331/ingest`.
2. **Parse** : `api/parser.py` extrait posts/comments depuis voyager JSON.
3. **Enrichissement** : `api/enrich.py` tag niches (ai/finance/m&a), velocity, reply_score.
4. **Storage** : `api/storage.py` écrit MD dans `vault/linkedin/feed/YYYY-MM-DD/`.
5. **Analyse** : `analyzer/report.py` génère rapport quotidien.

## Dossiers

- `feed/` — un MD par post capturé
- `comments/` — un MD par commentaire capturé
- `reports/` — rapport quotidien (top reply targets, niche cartography)
- `drafts/` — drafts de réponses générées
- `_raw/` — payloads voyager bruts (debug, re-parse)
- `perf/` — analyse de **tes propres** posts (objectif 1M impressions/mois) : `daily.json` (série temporelle impressions/engagements/followers), `post_windows.json`, `followers.json`, `demographics.json`, `exports/`, `meta.yaml` (format/thème par post à remplir), `reports/*-content-perf.md`

## Analyse de ses propres posts — objectif 1M impressions/mois

Ingérer les exports XLSX d'analytics LinkedIn (page Analytics → Export, hebdo) :

```bash
uv run python -m analyzer.cli perf-ingest ~/Downloads/Content_<dates>_<nom>.xlsx
uv run python -m analyzer.cli perf          # vue console : run rate, leaderboard, cadence, recos
uv run python -m analyzer.cli perf-report   # -> perf/reports/YYYY-MM-DD-content-perf.md
```

Module : `analyzer/content_perf.py`. Remplir `perf/meta.yaml` ({urn: {title, format, theme, hook}}) pour corréler reach × format/thème.

## Commandes

```bash
cd /Users/paul/linkedin-machine
uv sync
./scripts/run_api.sh          # démarre receiver
uv run python -m analyzer.cli status
uv run python -m analyzer.cli top -n 20
uv run python -m analyzer.cli report
```

## Niches cibles

- ai — IA, agents, LLM, ML
- finance — fund, VC, valuation, trading
- m_and_a — M&A, distressed, RJ-LJ, plan de cession

Configurables : `linkedin-machine/config/niches.yaml`

## Related

- [[brantham/_MOC]]
- [[website/_MOC]]
- [[_system/MOC-master]]
- [[_system/MOC-patterns]]
