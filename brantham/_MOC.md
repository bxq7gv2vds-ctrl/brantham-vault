---
type: moc
project: brantham
updated: 2026-03-26
---

# Brantham Partners -- Map of Content

## Mission

Cabinet M&A specialise dans les entreprises en difficulte (PME France). Cible les procedures collectives (redressement judiciaire, liquidation judiciaire, sauvegarde) pour identifier les opportunites de cession et les connecter a des repreneurs qualifies.

## Revenue Model

Success fees sur cessions realisees. Commission sur mise en relation vendeur/repreneur. Pre-revenue actuellement.

## Statut

- API FastAPI: operationnelle (3900+ lignes)
- Pipeline Prefect: operationnel (daily + weekly + monthly)
- Agents: 6 agents operationnels, orchestration Director
- 1 deal actif: MLD (Multi Loisirs Distribution)
- 600+ deals archives
- Revenue: **0 EUR** (pre-revenue)

---

## Project Locations

| Composant | Chemin | Stack |
|---|---|---|
| Backend API | `/Users/paul/Desktop/brantham-partners/api/` | FastAPI, 3900 lines |
| Frontend dashboard | `/Users/paul/internal-tool/` | React 19 + Vite + Zustand |
| Data pipeline | `/Users/paul/Desktop/brantham-partners/` | Python, PostgreSQL 16, Redis 7, Docker |
| Agent pipeline | `/Users/paul/Downloads/brantham-pipeline/` | server.js + 6 agents |
| Memory vault (ops) | **MERGED into vault/brantham/** | Markdown |
| Deals archive | `/Users/paul/brantham-vault/` | 600+ deals |
| MiroFish Engine | `/Users/paul/MiroFish/` | Python 3.12, MLX, FastAPI, Vue/Vite |
| Design/Next.js | `/Users/paul/Desktop/brantham-next/` | Next.js |
| SEO | see [[website/_MOC]] | |

---

## Key Links

- [[brantham/architecture]]
- [[brantham/data-pipeline/_MOC]]
- [[brantham/agents/_MOC]]
- [[brantham/dashboard/_MOC]]
- [[brantham/patterns/teaser-patterns]]
- [[brantham/patterns/teaser-onepager-html-pdf]] — One-pager HTML/PDF aligne sur DA site web
- [[brantham/patterns/scoring-patterns]]

## Knowledge Base — Procedures

- [[brantham/knowledge/procedures/mandat-ad-hoc-conciliation]] — Mandat ad hoc, conciliation, pre-pack cession, privilege new money
- [[brantham/knowledge/procedures/sauvegarde]] — Procedure de sauvegarde
- [[brantham/knowledge/procedures/redressement-judiciaire]] — Redressement judiciaire
- [[brantham/knowledge/procedures/liquidation-judiciaire]] — Liquidation judiciaire

## Knowledge Base — Legal

- [[brantham/knowledge/legal/plans-de-cession]] — Plans de cession judiciaire (L642-1+) : offre, criteres, procedure, effets, execution
- [[brantham/knowledge/legal/nullites-periode-suspecte]] — Nullites periode suspecte (L632-1/L632-2), responsabilite dirigeants (L651-2, L653-1+, L654-1+), checklist due diligence repreneur
- [[brantham/patterns/acheteur-mapping]]

## Knowledge Base — Process

- [[brantham/knowledge/process/due-diligence-distressed]] — Due diligence distressed exhaustif: checklist financiere/juridique/sociale/fiscale/operationnelle, red flags, timing LJ vs RJ, quick scan 48h, scoring DD

## Knowledge Base — Finance

- [[brantham/knowledge/finance/valorisation-distressed]] — Valorisation distressed exhaustif: 4 methodes, EBITDA normalise, 13-week CF, BP retournement, multiples sectoriels, scoring deals

## Knowledge Base — Market Intelligence

- [[brantham/knowledge/market/stats-defaillances-2025]] — Statistiques defaillances France 2024-2025: 70K defaillances/an, 267K emplois, secteurs, PGE, previsions 2026, comparaison internationale, application Brantham

## Pipeline Operations

- [[brantham/pipeline/BOARD]] — Kanban pipeline (statuts des deals)
- [[brantham/pipeline/QUEUE]] — File d'attente opportunites
- [[brantham/analyses/INDEX]] — Toutes les analyses IA
- [[brantham/teasers/INDEX]] — Tous les teasers generes

## Strategy

- [[brantham/strategy/2026-03-15-linkedin-personal-brand]]
- [[brantham/strategy/mirofish-vision]] — Vision MiroFish: simulateur de monde M&A distressed (agents autonomes, echelle massive)
- [[brantham/strategy/mirofish-roadmap]] — Roadmap technique MiroFish (v0.1 → v2.0)
- [[brantham/strategy/mirofish-todo]] — TODO executif: World Simulator M&A (7 phases)

### MiroFish v0.3 Status (2026-03-18)
- **995K agents x 100 rounds = 83.4s** (0.83s/round sur M5)
- Modele distille: MLP 4293 params, 83.9% accuracy, 17.2KB
- MLX GPU inference: 0.117s pour 1M agents
- 7 scenarios pre-configures (baseline, crise_2008, boom_2021, hausse_taux, reforme, desert, million_agents)
- API FastAPI + Frontend Vue/Vite operationnels
- Patterns: [[brantham/patterns/distilled-model-scaling]], [[brantham/patterns/numpy-aggregation-over-objects]]
- [[brantham/strategy/webapp-roadmap]] — Roadmap Web App internal-tool (6 phases)

---

## Current Pipeline Status

| Deal | Statut | Deadline | Next Step |
|---|---|---|---|
| MLD (Multi Loisirs Distribution) | teaser_redige | 17/03/2026 | Pret pour Hunter |

- 600+ deals archives dans `/Users/paul/brantham-vault/`
- Dernier scan AJ: [[brantham/sessions/auto-enrichment-2026-03-25]] -- 456 opportunites (24/31 sites), 75 avec CA>=1M, top pick: Papier & electricite (204M), Commerce sport (deadline 07/04)

---

## Revenue

**0 EUR** -- pre-revenue. Premier deal actif en cours (MLD). Fee structure a definir sur premiere cession reussie.
