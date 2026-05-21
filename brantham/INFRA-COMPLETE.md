---
type: reference
project: brantham
updated: 2026-05-12
---

# Brantham Partners — Infra Complète (extraction du vault)

Vue d'ensemble exhaustive de toute l'infra : vault, repos code, pipelines, agents, skills, MCP, crons. Source de vérité : `/Users/paul/vault/`.

## 1. Le Vault (`/Users/paul/vault/`)

1151 fichiers markdown, repo git, Obsidian. Single source of truth. Index racine : `_system/MOC-master.md`.

### Arborescence haut niveau
| Dossier | Contenu |
|---|---|
| `_system/` | MOC indexes (master, decisions, assumptions, patterns, bugs), templates, ADR, agents config, scripts (vault-linker.py, vault-health.py) |
| `brantham/` | **Tout le projet Brantham** (voir §2) |
| `website/` | SEO Machine / zura-inspired (audits, autopilot, bugs, patterns, research, sessions, strategies) |
| `founder/` | decisions, assumptions, customers, daily plans, data, investors, journal, sessions, strategy |
| `twitter/` | agent (voice card, hooks, blacklist, tier list), digests, drafts, threads, replies, knowledge-graph, persona, strategy |
| `linkedin/` | feed capturé (LinkedIn Machine), drafts, comments, reports, _raw |
| `patterns/` | patterns techniques transverses |
| `knowledge/` | m-and-a, seo, tech (général) |
| `issues/` | issue tracker local-markdown (skills mattpocock, pas de GitHub) |
| `remember/` | session remembers |
| `reports/` | rapports santé vault |
| `alliance-coiffure/`, `lat-arb-bot/`, `soren-mendy/` | sous-projets |

### Vault writing séparé : `/Users/paul/writing-vault/`
Vault Obsidian indépendant (1347 docs). Pipeline raw → concepts → drafts → published. Skills `/write` + `/tweet-gen`.

## 2. Brantham dans le vault (`vault/brantham/` — ~360 fichiers)

| Dossier | Rôle |
|---|---|
| `_MOC.md` | Map of Content — point d'entrée |
| `architecture.md` | Stack technique (voir §3) |
| `context/` | `business-profile/_PROFILE.md` (living profile, MAJ à chaque vocal), `realite-business.md`, `process-end-to-end.md` (10 phases), `sow.md`, `roles-et-responsabilites.md` |
| `protocols/` | `work-in-vault-only.md`, `voice-notes-continues.md` |
| `playbooks/` | `call-introduction-repreneur.md`, `call-script-verbatim.md`, `call-trame-visuelle-deal.md` |
| `deals/` | `active/` (magic-form-levallois, itfi-groupe, ingebime, open-bee-france, sas-fitness-levallois, mld, alphosa), `aj-feed/` (feed quotidien des annonces AJ), `closed/`, templates |
| `knowledge/` | base de connaissance distressed M&A : `procedures/`, `legal/`, `finance/`, `process/`, `acteurs/`, `sectors/`, `skills/`, `case-studies/`, `market/`, `glossary/`, `raw/`, `concepts/` (49+ sujets) |
| `mastery/` | programme formation 30j : `curriculum.md`, `fiches/` (22 fiches), `finance/` (6 modules), `cas-pratiques/`, `quiz/`, `drill-quotidien.md`, `log-mastery.md` |
| `agents/` | les 6 agents LLM : `_shared/` (BRAIN, PIPELINE, OPPORTUNITIES, SOUL, HEARTBEAT, AGENTS, ERRORS, VEILLE_REPORT), un dossier par agent (director/scout/analyst/writer/hunter/enricher avec IDENTITY.md) |
| `data-pipeline/` | `_MOC.md`, `schema.md`, `scoring.md` |
| `dashboard/` | `_MOC.md`, `api-endpoints.md` |
| `cockpit/` | `roadmap-2026-05-05.md` (cockpit web Next.js) |
| `pipeline/` | `BOARD.md` (kanban), `QUEUE.md` |
| `pappers/` | cartographie entreprises FR : `_MOC.md`, `entreprises/`, `dirigeants/`, scripts |
| `patterns/` | ~30 patterns techniques (teaser, scoring, db-abstraction, hunters-api-gouv, cockpit-tui, dldo-extraction, etc.) |
| `bugs/` | bugs résolus datés |
| `sessions/` | logs de session, `auto-enrichment-*`, `auto-health-*` (auto-générés) |
| `analyses/` | analyses M&A IA |
| `teasers/` | teasers générés |
| `linkedin/` + `linkedin-factory/` | fabrique LinkedIn (posts, design system, formats internationaux) |
| `strategy/` | `mirofish-*` (vision/roadmap/todo), `webapp-roadmap.md`, `roadmap-platform-2026.md` |
| `cowork-prompts/` | prompts agents Cowork (sourcing, pipeline-check, deal-analysis, buyer-hunt, morning-brief, outreach-draft) |
| `templates/` | `lettre-de-mission.md`, `note-cadrage-deal.md`, `courrier-extension-nda-aj.md` |
| `corp/` | `brantham-corp-identite.md` |
| `mastery/`, `knowledge/training/` | curriculum |

## 3. Stack technique Brantham (`architecture.md`)

| Layer | Tech |
|---|---|
| Backend API | Python 3.12+, FastAPI — `/Users/paul/Desktop/brantham-partners/api/` (~3900 lignes) |
| Data pipeline | Python, PostgreSQL 16 (Docker `brantham-data-postgres-1`), Redis 7, Prefect — `/Users/paul/Desktop/brantham-partners/` |
| Agent pipeline | server.js + 6 agents LLM — `/Users/paul/Downloads/brantham-pipeline/` |
| Frontend dashboard | React 19 + TS 5.9 + Vite 7 + Zustand 5 + React Router 7 — `/Users/paul/internal-tool/` |
| Cockpit web | Next.js 15 — `/Users/paul/cockpit-web/` (459 opps, 200 actives) |
| MiroFish | Python 3.12, MLX, FastAPI, Vue/Vite — `/Users/paul/MiroFish/` (R&D, simulateur monde M&A) |
| Deals archive | 600+ deals markdown — `/Users/paul/brantham-vault/` |
| LLM | Anthropic (opus-4 / sonnet-4 / haiku-4), fallback OpenRouter |
| Deploy | Hetzner VPS 95.216.198.143 (backend), Vercel (frontends) |

### Base de données (PostgreSQL 16)
43+ tables. 1.8M BODACC · 184K procédures collectives · 194K bilans financiers.
Tables clés : `procedure_collective`, `entreprise`, `score_qualification` (9 composantes), `transaction_cession`, `stats_mandataire`, `stats_tribunal`, `cox_predictions` (Cox PH), `dossier_complet` (84K+), `bilan_ratios`, `buyer_match_score` (841K+).
Materialized views : `mv_top_opportunites`, `mv_distressed_ma`.

### Pipeline quotidien (Prefect, 07h00 via launchd `com.brantham.daily.plist`)
10 étapes : setup_schema → bodacc_collectors → ingest/dedup → sirene_enrichment → geocoding → scoring → bilan_ratios → dossier_complet → refresh_views → stats_and_predictions (Cox + backtest + early warning + buyer match + IBSE).
Weekly (dimanche) : matrices corrélation sectorielles, full refresh views, saisonnalité, analyses annuelles, buyer match re-run.
Monthly (1er) : IBSE sectoriel, sector stress index.

### Les 6 agents LLM (orchestrés par Director — `brantham-pipeline/server.js`)
| Agent | Rôle | LLM | QC |
|---|---|---|---|
| Director | orchestrateur, QC, go/no-go (seuil 60+) | opus-4 | — |
| Scout | veille BODACC, détection opportunités | haiku-4 | — |
| Analyst | analyse M&A, due diligence light | sonnet-4 | 7/10 |
| Writer | teaser PPTX anonymisé | sonnet-4 | 7/10 |
| Hunter | mapping acheteurs (A/B/C) | sonnet-4 | 7/10 |
| Enricher | validation contacts | haiku-4 | 6/10 |

Flow : Scout → Director(score) → Analyst → Writer+Hunter(//) → Enricher → Director(QC final).
Limites : max 2 analyses simultanées, max 3 deals actifs, priorité LJ, escalade si deadline < 7j.
Mémoire partagée : `BRAIN.md`, `PIPELINE.md`, `OPPORTUNITIES.md`, `SOUL.md`, `HEARTBEAT.md` + workspaces par deal.

### Dashboard (`internal-tool/`)
Routes : `/dashboard`, `/agents`, `/pipeline`, `/veille`, `/analyse`, `/chat`, `/office`, `/memory`, `/dossier/:slug`.
Stores Zustand : opportunities, ui, agents, chat. Polling OPPORTUNITIES.json (8s) + activity.json (6s) + SSE `/api/stream`. 26+ endpoints API.
Design tokens : white #FAFAF8, off #F4F3F0, ink #0F0F0E, red #C8251A, indigo #5E54F0 (pas de violet). Fonts : DM Sans, DM Mono, Instrument Serif.

### Cockpit (TUI Python + Supabase) — `brantham-pipeline/cockpit/`
Triage AJ, scraper Mayday v5, DLDO extraction regex FR, hunters concurrents via api.gouv (SIRENE gratuit), todos manager. Abstraction DB SQLite/Postgres HybridRow.

## 4. Connexion au vault — comment ça marche

- **QMD MCP** (`qmd mcp`, user-scope) : recherche sémantique hybride (BM25 + vecteurs + reranking) sur 2 collections : `vault` (1123 docs) et `writing-vault` (1347 docs). Modèles locaux : embeddinggemma, query-expansion, reranker Qwen3-0.6B, GPU Apple M5 Metal. Re-index : `qmd embed`. Outils : `query`, `get`, `multi_get`, `status`.
- **qmd-vault MCP** : second serveur QMD identique.
- **CLAUDE.md** (`/Users/paul/CLAUDE.md`) : directives globales — début de session lit `_system/MOC-master.md` + `_MOC.md` projet + decisions/assumptions en attente + `/daily-plan`. Auto-capture pendant la session : décisions → `founder/decisions/`, assumptions → `founder/assumptions/`, customers → `founder/customers/`, bugs → `<projet>/bugs/`, patterns → `patterns/`. Fin de session → `<projet>/sessions/YYYY-MM-DD.md`.
- **Wikilinks Obsidian obligatoires** : section `## Related` + backlink MOC parent + projet MOC dans chaque fichier. Audit `vault/_system/vault-linker.py`, fix auto `vault-linker.py fix`.
- **Health check** : `vault/_system/vault-health.py` (sources non compilées, stats périmées, liens cassés, whitespots).
- **Memory auto** : `/Users/paul/.claude/projects/-Users-paul/memory/` (MEMORY.md index + fichiers par fait).

## 5. Skills installés (`~/.claude/skills/`)

### Skill `brantham` (knowledge graph — point d'entrée deals)
Sous-nœuds : `deal-scoring` (5 critères, seuil ≥60/100, secteurs A/B/C/D, précédents), `teaser-patterns` (structure + exemples), `acheteur-mapping` (base acheteurs sectoriels, stratégiques vs financiers), `director-workflow` (priorisation, limites), `ma-context` (procédures LJ/RJ/SV, acteurs, délais), `agent-network` (architecture 6 agents).

### Skills Brantham / M&A
- `distressed-expert` — agent expert droit des entreprises en difficulté. `learn`/`teach`/`quiz`/`deep-dive`/`map`/`sources`. KB : `vault/brantham/knowledge/`.
- `prospect` — recherche repreneur (Pappers MCP + Gmail MCP) → fiche intel + brouillon outreach.
- `pageindex` — RAG vectorless sur PDFs lourds (data rooms, comptes annuels, jugements). CLI `brantham-pageindex <slug> <pdf>`, backend `claude -p`.
- `compile-concepts` — compile `knowledge/raw/` → `knowledge/concepts/` (articles encyclopédiques) + health check.
- `internal-tool` — control center terminal Brantham (KPIs, pipeline, todos).
- `autopilot-status` — statut autopilot Brantham.

### Skills vault / knowledge
- `qmd` — recherche QMD. `obsidian-vault` — CRUD notes Obsidian + wikilinks. `brain-ingest` — YouTube/audio/texte → notes structurées. `founder-vault` — knowledge graph fondateur (decisions/assumptions/customers/journal). `save-state` / `remember` — dump état session. `daily-plan` / `daily-report` — brief matin / rapport.

### Skills dev / orchestration
- `swarm-superpowers`, `swarm-iosm`, `auto-dev-loop` — orchestration parallèle d'agents + TDD + review.
- `tdd`, `diagnose`, `prototype`, `improve-codebase-architecture`, `simplify`, `grill-me`, `grill-with-docs`, `to-issues`, `to-prd`, `triage`, `zoom-out` — skills mattpocock (issues local-markdown dans `vault/issues/`, ADR dans `vault/_system/adr/`, jamais gh/glab).
- `launch-dev`, `deploy-vps`, `setup-pre-commit`, `git-all`, `git-guardrails-claude-code`, `setup-matt-pocock-skills`, `write-a-skill`, `scaffold-exercises`, `migrate-to-shoehorn`, `tmux-ide`.

### Skills writing / content
- `write` (seed/draft/review/publish/health/ingest), `tweet-gen` (batch/thread/article/react/calendar), `twitter` (digest Twitter + OSINT Crucix), `edit-article`, `clean-separators`, `caveman`, `agent-reach`.

### Skills divers
- `todo` (`vault/founder/todo.md`), `loop`, `schedule`, `update-config`, `pulse`, `keybindings-help`, `claude-api`, `fewer-permission-prompts`, `init`, `review`, `security-review`.

## 6. MCP servers actifs
- **qmd** + **qmd-vault** — recherche sémantique vault.
- **pappers** — cartographie entreprises FR (100 tokens/mois gratuit) : informations-entreprise, comptes, dirigeants, bénéficiaires, procédures collectives, cartographie groupes, recherche acteurs politiques, articles de loi, décisions de justice.
- **claude_ai_Gmail** — drafts, labels, threads, recherche.
- **claude_ai_Google_Calendar** / **Google_Drive** — auth.
- **computer-use** — contrôle desktop (screenshots, clics, clavier).
- **claude-peers** — réseau d'instances Claude Code sur la machine.
- **figma-developer-mcp** — données Figma.
- Plugins : context7, playwright, firecrawl, vercel, supabase, github, commit-commands, frontend-design.

## 7. Crons / automatisations (launchd)
- `com.brantham.daily.plist` — pipeline data 07h00.
- Cron daily relances outreach (cockpit web).

## 8. Autres projets connectés (hors Brantham)
- **LinkedIn Machine** (`/Users/paul/linkedin-machine/`) — capture feed → FastAPI :7331 → `vault/linkedin/`. CLI `lkm`.
- **Karaté Pipeline** (`/Users/paul/karate-pipeline/`) — analyse vidéo kumité, vault dédié `/Users/paul/karate-vault/`.
- **Website / SEO Machine** (`/Users/paul/zura-inspired/`) — vault `website/`.
- **Crucix** (`/Users/paul/Crucix/`) — 27 sources OSINT. **clix** — Twitter CLI.
- Polytech Strategist (terminé), MiroFish (R&D).

## Related
- [[brantham/_MOC]]
- [[brantham/architecture]]
- [[_system/MOC-master]]
- [[brantham/data-pipeline/_MOC]]
- [[brantham/agents/_MOC]]
- [[brantham/dashboard/_MOC]]
