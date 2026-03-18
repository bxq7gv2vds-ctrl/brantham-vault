---
type: strategy
created: 2026-03-17
updated: 2026-03-17
project: mirofish-world-sim
status: active
priority: critical
---

# MiroFish World Simulator — TODO Executif

> Objectif: Construire le premier simulateur de monde M&A distressed au monde.
> Ref: vision dans [[mirofish-vision]], repo `/Users/paul/MiroFish/`

---

## Etat d'avancement (17 mars 2026)

```
Phase 0 (Infra)          ████████████████ DONE
Phase 1 (World Models)   ████████████████ DONE
Phase 2 (Agent Pop.)     ████████████████ DONE
Phase 3 (Sim Engine)     ████████████████ DONE
Phase 4 (World Config)   ████████████████ DONE
Phase 5 (Analytics)      ████████████████ DONE
Phase 6 (API)            ████████████████ DONE — 19 endpoints
Phase 7 (Frontend)       ████████████████ DONE — Vue3/Vite, 9 tabs (+ AGENTS)
Phase 7b (LLM Agents)    ████████████████ DONE — batch+sparse, 0 failures
Phase 8 (Real Data)      ████████████░░░░ 80% — 8.1-8.5 done, 8.6 TODO
Phase 9 (Calibration)    ░░░░░░░░░░░░░░░░ TODO
```

### v0.2 Roadmap Progress
```
Batch inference (LLM)    ████████████████ DONE — batch_llm_decide(), 5 agents/call
Agent memory             ████████████████ DONE — last 5 actions in LLM prompt
Inter-agent visibility   ████████████████ DONE — phase-dependent competition context
SSE streaming            ████████████████ DONE — background thread + EventSource + progress bar
Resume simulation        ████████████████ DONE — snapshot serialize/restore + /resume endpoint
Persistence (SQLite)     ████████████████ DONE — auto-save completed sims, survive restart
Agent inspector          ████████████████ DONE — /agents list + /agents/{name} drill-down + UI tab
```

---

## Architecture reelle (implementee)

```
/Users/paul/MiroFish/
├── backend/ma/
│   ├── models/          4 fichiers — ontologie M&A complete
│   │   ├── entities.py    Entreprise, Procedure, Deal, Bid, DealPhase (8 phases)
│   │   ├── actions.py     MAActionType (16 types), AgentAction
│   │   ├── config.py      WorldConfig (25+ params), 6 SCENARIOS presets
│   │   └── conclusions.py Conclusion dataclass + serialization
│   │
│   ├── agents/          4 fichiers — population 10 types
│   │   ├── types.py       AgentType enum (10 types)
│   │   ├── rule_based.py  RuleBasedAgent — scoring multi-criteres, decision trees
│   │   ├── llm_agent.py   LLMAgent — MLX qwen2.5:7b, JSON parsing, fallback
│   │   └── population.py  generate_population() — real+synthetic, calibrated NAF/regions
│   │
│   ├── data/            3 fichiers — Brantham PostgreSQL integration
│   │   ├── __init__.py
│   │   ├── connector.py   get_connection(), fetch_all(), fetch_one()
│   │   └── loader.py      5 loaders: procedures, buyers, mandataires, tribunaux, calibration
│   │
│   ├── engine/          6 fichiers — coeur de la simulation
│   │   ├── environment.py   MAEnvironment — Poisson injection, state machine, phases
│   │   ├── simulation.py    WorldSimulation — orchestration, vectorized batch
│   │   ├── vectorized.py    AgentIndex + batch_decide() — numpy, 107K actions/s
│   │   ├── monte_carlo.py   run_monte_carlo() — N runs, CI95, aggregation
│   │   ├── deal_injection.py inject_deal() — real deal prediction
│   │   └── sweep.py         sweep() — parameter sensitivity, tipping points
│   │
│   ├── analytics/       1 fichier — extraction conclusions
│   │   └── engine.py      AnalyticsEngine — 7 modules, 60+ conclusions
│   │
│   └── api/             3 fichiers — FastAPI :8888
│       ├── app.py         FastAPI app + CORS
│       ├── schemas.py     Pydantic models (10 schemas)
│       └── router.py      12 endpoints RESTful
│
├── run_api.py           uvicorn launcher
├── run_simulation.py    CLI script
├── .env                 LLM_BACKEND=mlx
└── .venv/               Python 3.12, uv
```

24 fichiers Python, ~2500 lignes de code.

---

## Phase 0 — INFRASTRUCTURE -- DONE

| # | Tache | Status |
|---|-------|--------|
| 0.1 | Python 3.12 venv (`uv`) | DONE |
| 0.2 | Deps: numpy, mlx-lm, fastapi, uvicorn | DONE |
| 0.3 | LLM: MLX `Qwen2.5-7B-Instruct-4bit` (Ollama casse macOS 25.3) | DONE |
| 0.4 | Structure `backend/ma/{models,agents,engine,analytics,api}` | DONE |

---

## Phase 1 — WORLD MODELS -- DONE

Ontologie complete implementee dans `backend/ma/models/`:

| Composant | Fichier | Detail |
|-----------|---------|--------|
| Entites | `entities.py` | Entreprise, Procedure (RJ/LJ/SV), Deal (8 phases), Bid |
| Actions | `actions.py` | 16 MAActionType (discover, DD, IOI, LOI, binding, negotiate, withdraw...) |
| Config | `config.py` | WorldConfig 25+ params, 6 presets scenarios |
| Conclusions | `conclusions.py` | Conclusion structuree avec CI, tags, metrics |

**10 types d'agents**: RepreneurIndustriel, FondsPE, FamilyOffice, SerialAcquirer, Mandataire, Tribunal, Banque, CSE, Conseiller, Concurrent

**8 phases deal**: PUBLICATION -> DISCOVERY -> DUE_DILIGENCE -> BID_SUBMISSION -> NEGOTIATION -> TRIBUNAL_REVIEW -> CLOSED/FAILED

---

## Phase 2 — AGENT POPULATION -- DONE

| Composant | Fichier | Detail |
|-----------|---------|--------|
| Types | `agents/types.py` | 10 AgentType enum |
| Rule-based | `agents/rule_based.py` | Multi-criteria scoring (secteur 30%, ticket 25%, geo 15%, competition 15%, timing 15%) |
| LLM agents | `agents/llm_agent.py` | MLX qwen2.5:7b, pre-filter top 3, JSON parsing, fallback to rule-based |
| Population | `agents/population.py` | NAF sector weights (15 secteurs), region weights (14 regions), log-normal budgets |

**Population par defaut**: 6884 agents (5000 repreneurs, 500 PE, 300 FO, 50 serial, 300 mandataires, 134 tribunaux, 200 banques, 400 conseillers)

**LLM agents**: ratio configurable (`llm_ratio`), default 1%. Chaque LLM call = ~6s (MLX M5).

---

## Phase 3 — SIMULATION ENGINE -- DONE

| Composant | Fichier | Detail |
|-----------|---------|--------|
| Environnement | `engine/environment.py` | Poisson injection, phase transitions, deadlines, macro events |
| Simulation | `engine/simulation.py` | WorldSimulation orchestration, agent partitioning, vectorized batch |
| Vectorisation | `engine/vectorized.py` | AgentIndex (numpy), batch_decide(), 107K actions/s |

**Performance**: 6884 agents x 100 rounds = 6s. Speedup numpy: 9x vs pure Python.

---

## Phase 4 — WORLD CONFIGURATOR -- DONE

25+ parametres configurables dans `WorldConfig`:
- Macro: procedures/year, interest_rate, pme_confidence, default_rates
- Agents: count par type, capital_total
- Rules: tribunal_strictness, info_asymmetry, dd_cost, market_friction, legal_deadlines
- Simulation: n_rounds, seed, llm_agent_ratio

**6 scenarios presets**:
| Scenario | Key params |
|----------|-----------|
| baseline_2025 | 70K proc/an, taux 3.5%, 50Md capital |
| crise_2008 | 120K proc, taux 6%, capital 25Md, confiance 30% |
| boom_2021 | 45K proc, taux 1%, capital 100Md |
| hausse_taux | taux 6%, capital 30Md |
| reforme_judiciaire | deadlines acceleres, tribunal strict 0.8 |
| desert_repreneurs | 1000 repreneurs, 100 PE |

---

## Phase 5 — ANALYTICS ENGINE -- DONE

`analytics/engine.py` — 7 modules d'analyse:

| Module | Conclusions |
|--------|------------|
| market_dynamics | taux cession global, volume, tendances |
| sector_analysis | hot/cold sectors, ratio bids/deals par NAF |
| geographic_analysis | coverage regionale, deserts de repreneurs |
| agent_performance | success rate par type, budget utilise |
| deal_lifecycle | duree moyenne par phase, dropout rate |
| competition_analysis | concentration bids, herding behavior |
| pricing_analysis | prix moyen, ecart bid/valeur, elasticite |

**Output**: 60+ conclusions structurees par simulation.

**Extensions avancees** (implementees dans `engine/`):

| Extension | Fichier | Detail |
|-----------|---------|--------|
| Monte Carlo | `monte_carlo.py` | N runs, CI95, aggregation cross-run |
| Deal Injection | `deal_injection.py` | Inject real deal, predict p_cession, price, bidders |
| Parameter Sweep | `sweep.py` | Vary 1 param, elasticity, tipping points, 6 presets |

---

## Phase 6 — API FastAPI -- DONE

19 endpoints sur `:8888`, prefix `/api/mirofish`:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Status check |
| `/scenarios` | GET | Liste des 6 presets avec params cles |
| `/simulate` | POST | Lance simulation async, retourne immediatement |
| `/stream/{id}` | GET | SSE streaming progression en temps reel |
| `/simulations` | GET | Historique des simulations (SQLite) |
| `/simulations/{id}` | GET | Status d'une simulation |
| `/simulations/{id}/full` | GET | Resultats complets post-completion |
| `/simulations/{id}/conclusions` | GET | Conclusions filtrees (category, tags, confidence) |
| `/simulations/{id}/timeline` | GET | Action log pagine |
| `/simulations/{id}/snapshot` | GET | Snapshot serialise pour resume |
| `/simulations/{id}/agents` | GET | Liste agents avec stats |
| `/simulations/{id}/agents/{name}` | GET | Detail agent: timeline, bids, deals |
| `/resume/{id}` | POST | Reprendre une simulation a round N |
| `/compare` | POST | Compare 2+ scenarios cote a cote |
| `/monte-carlo` | POST | N simulations, intervalles de confiance CI95 |
| `/inject-deal` | POST | Injecter un deal reel, predictions |
| `/sweep` | POST | Sweep un parametre, analyse sensibilite |
| `/sweep/presets` | GET | 6 presets de sweep disponibles |

Schemas Pydantic: SimulationRequest, SimulationResponse, SimulationStatus, MonteCarloRequest, DealInjectionRequest, SweepRequest, CompareRequest, ConclusionFilter, ScenarioInfo.

---

## Phase 7 — FRONTEND -- DONE

Implementee dans `/Users/paul/MiroFish/frontend/` (Vue 3 + Vite), pas Next.js.

| Tab | Composant | Status |
|-----|-----------|--------|
| DASH | PaneView.vue | DONE — KPIs, deals par phase, LLM stats panel |
| CONCL | PaneView.vue | DONE — conclusions filtrees par categorie |
| TIME | PaneView.vue | DONE — pagination + filtre LLM server-side |
| CMP | PaneView.vue | DONE — compare scenarios cote a cote |
| MC | PaneView.vue + MCChart | DONE — Monte Carlo dashboard, CI95, distributions |
| SWP | PaneView.vue + SweepChart | DONE — parameter sweep + sensibilite |
| INJ | PaneView.vue | DONE — inject deal, predictions |
| GRAPH | AgentGraph.vue | DONE — D3 force graph, noeuds LLM cyan |
| Sidebar | Terminal.vue | DONE — config, LLM toggle/slider, compare |

**v0.2 ajouts**: Progress bar SSE, tab AGENTS (list + drill-down individuel)

---

## Phase 8 — REAL DATA -- 80% DONE

| # | Tache | Status | Detail |
|---|-------|--------|--------|
| 8.1 | Connecteur PostgreSQL | DONE | `backend/ma/data/` — connector.py + loader.py (5 fonctions) |
| 8.2 | Import vrais acheteurs | DONE | 143 buyers reels, classes par nom/historique (130 RI, 10 PE, 3 SA) |
| 8.3 | Import mandataires | DONE | 504 mandataires reels, reputation calibree sur taux_cession |
| 8.4 | Import tribunaux | DONE | 505 tribunaux reels, geo-localises par departement |
| 8.5 | Calibration distributions | DONE | 30 NAF codes + 18 regions calibres depuis 84K+ procedures |
| 8.6 | Deal data enrichment | TODO | Bilans, scores existants, P(cession) quant |

**Scenario `real_france_2025`**: 7459 agents (1152 reels), 184K actions en 1.6s (30 rounds).
**Endpoints**: `/calibration` + `/real-data/stats` + data_mode override sur `/simulate`.
**3 modes injection**: synthetic (Poisson), real (queue from DB), hybrid (70% real + 30% synthetic).

---

## Phase 9 — CALIBRATION (TODO) -- PRIORITE MEDIUM

| # | Tache | Detail |
|---|-------|--------|
| 9.1 | Backtest 600+ deals | Simuler sur deals archives a outcome connu |
| 9.2 | Brier score | (prediction - outcome)^2 par deal |
| 9.3 | Weight learning | Ajuster poids scoring sur performance reelle |
| 9.4 | Sector calibration | Calibrer params par secteur |
| 9.5 | Ensemble integration | Signal world-sim dans scoring Brantham existant |
| 9.6 | Report generation | Rapport PDF structure (exec summary, market, what-if) |

---

## Problemes connus

| Issue | Detail | Fix |
|-------|--------|-----|
| Ollama 0.18.0 casse | Metal shader bug bfloat/half sur macOS 25.3 | Utiliser MLX |
| Cession rate = 0 sur <50 rounds | Deal lifecycle trop long pour runs courts | Augmenter n_rounds ou reduire phases |
| LLM bottleneck | 6s/decision, 100 calls = 10min | Limiter LLM a 1%, 1 call/5 rounds |
| Price range enorme | Deal injection montre min/max tres ecartes | Normaliser par population, ajouter outlier filtering |
| ~~Raisons opaques~~ | ~~`vec_bid_0.713` sans explications~~ | FIXED — breakdown `sec= tic= geo= cmp= tim=` |
| ~~Herding massif~~ | ~~argmax pur, tous sur le meme deal~~ | FIXED — top-3 weighted selection |
| ~~Agents stateless~~ | ~~rule-based re-bid infini sur meme deal~~ | FIXED — memory masking (11.5% re-bids) |
| ~~Conseillers spam~~ | ~~share_info aveugle sur 1er deal~~ | FIXED — filtre watchers<10 |

---

## Benchmarks

| Config | Agents | Rounds | Temps | Actions/s |
|--------|--------|--------|-------|-----------|
| baseline x50 | 6884 | 50 | 3.2s | 89K |
| baseline x100 | 6884 | 100 | 7.4s | 83K |
| small + 2 LLM | 280 | 50 | 34min | ~6 (LLM) |
| Monte Carlo x3 | 6884 | 30 | 5.0s | — |
| Sweep x9 | 6884 | 30 | 15.5s | — |
| Deal injection x10 | 6884 | 50 | ~20s | — |
| real_france_2025 x30 | 7459 (1152 real) | 30 | 1.6s | 115K |
| real_france_2025 x80 | 7459 (1152 real) | 80 | 5.3s | 103K |

---

## Notes techniques

- **MLX model**: `mlx-community/Qwen2.5-7B-Instruct-4bit` — natif Apple Silicon M5, zero cout
- **Vectorisation**: numpy AgentIndex pre-built, batch_decide() en matrix ops, top-K anti-herding, memory masking
- **Explainability**: raisons enrichies `sec= tic= geo= cmp= tim=` pour chaque action vectorisee
- **Agent memory**: rule-based agents penalisent les deals deja bid (0.2x) ou withdraw (0.1x)
- **API**: FastAPI async, background threads pour simulations longues, SSE streaming
- **Persistence**: SQLite auto-save (`data/simulations.db`), survit aux restarts
- **Resume**: Snapshot complet (env, agents, RNG state) → reprendre a n'importe quel round
- **Agent inspector**: Tab AGENTS avec list + drill-down individuel (timeline, bids, deals)
- **Simulation deterministe**: seed control pour reproducibilite exacte
- **Architecture modulaire**: models/agents/engine/analytics/api — chaque couche independante

---

*Derniere mise a jour: 17 mars 2026*
