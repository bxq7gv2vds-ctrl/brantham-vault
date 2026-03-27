---
type: reference
project: brantham
updated: 2026-03-12
---

# Architecture Brantham Partners

## Stack Principal

| Layer | Technology |
|---|---|
| Backend | Python 3.12+, FastAPI |
| Database | PostgreSQL 16 (Docker container: `brantham-data-postgres-1`) |
| Cache/Queue | Redis 7 |
| Orchestration | Prefect (daily/weekly/monthly flows) |
| Frontend | React 19, TypeScript 5.9, Vite 7, Zustand 5, React Router 7 |
| LLM | Anthropic (claude-opus-4, claude-sonnet-4, claude-haiku-4), fallback OpenRouter |
| Containerisation | Docker (postgres, redis, pgadmin) |

## Database Schema

- **43+ tables** dans PostgreSQL 16
- 1.8M enregistrements BODACC
- 184K procedures collectives
- 194K bilans financiers

### Tables Principales

| Table | Description |
|---|---|
| `procedure_collective` | Procedures actives et historiques (RJ, LJ, SV) |
| `entreprise` | Fiches entreprise enrichies (SIRENE, geocoding) |
| `score_qualification` | Scores de qualification (9 composantes) |
| `transaction_cession` | Historique des cessions realisees |
| `stats_mandataire` | Statistiques par mandataire judiciaire |
| `stats_tribunal` | Statistiques par tribunal de commerce |
| `cox_predictions` | Predictions de probabilite de cession (Cox PH model) |
| `dossier_complet` | Dossiers enrichis complets (84K+) |
| `bilan_ratios` | Ratios financiers calcules depuis bilans |
| `buyer_match_score` | Scores de matching acheteur/cible (841K+) |

### Materialized Views

- `mv_top_opportunites` -- Top opportunites qualifiees
- `mv_distressed_ma` -- Vue M&A distressed consolidee

## Docker Services

```
brantham-data-postgres-1  -- PostgreSQL 16
redis                      -- Redis 7
pgadmin                    -- PgAdmin web interface
```

## IMPORTANT -- PostgreSQL Local

> **brew postgres@16 auto-restarts via launchd.** Pour l'arreter proprement:
> ```bash
> pg_ctl stop -D /opt/homebrew/var/postgresql@16 -m fast
> ```
> Sinon conflit de ports avec le PostgreSQL Docker.

## Architecture Diagram (Simplified)

```
BODACC/SIRENE/INPI
       |
   [Prefect Pipeline]
       |
   PostgreSQL 16 --- Redis 7
       |
   [FastAPI Backend]  ---  [Agent Pipeline (server.js)]
       |                          |
   [React Dashboard]        [6 Agents LLM]
```

## Deployment

- Dev: local (macOS, Docker Desktop)
- Prod: Hetzner VPS (95.216.198.143) pour backend, Vercel pour frontend
- Cron pipeline: 07h00 via launchd (`com.brantham.daily.plist`)

## Related
- [[brantham/_MOC]]
