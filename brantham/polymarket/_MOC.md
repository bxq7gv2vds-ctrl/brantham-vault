---
tags: [polymarket, hedge-fund, moc]
created: 2026-04-17
status: active
---

# Polymarket Hedge Fund — Map of Content

Knowledge hub pour la construction d'un système trading hedge-fund grade sur Polymarket (weather markets puis expansion).

**Projet code** : `/Users/paul/polymarket-hedge/`
**DB locale** : `bracket_scalper_trades.db`, `all_markets.db`, `pmhedge.db`, `alpha_data_hub.db` (new)
**Module principal** : `src/pmhedge/alpha/` (architecture unifiée)

## Objectif

Construire un système de trading **100% data-driven** sur Polymarket avec :
- Data multi-source best-in-class par région (HRRR US, AROME FR, ICON-EU, etc.)
- Modèle ML calibré SOTA (EMOS + BMA + XGBoost + DRN)
- Exécution CLOB direct avec rebate capture
- Risk management hedge-fund grade (Kelly correlation-adjusted, kill switch)
- Backtest walk-forward rigoureux avec Monte Carlo + attribution

**Target P&L** : $200-400k/an avec capital scaling $1k → $50k

## ⚡ Point d'entrée nouvelle session

1. **[[STATE-HANDOFF|🎯 STATE-HANDOFF]]** — état complet système (LIRE EN PREMIER)
2. **[[g1-g2-qualification-kit|G1→G2 Qualification Kit]]** — framework actuel de qualification (initiative en cours)
3. **[[g1-g2-todo-tracker|G1→G2 Todo Tracker]]** — état d'exécution des 16 livrables
4. **[[audit-hedge-fund-grade|📊 Audit hedge fund grade]]** — gap analysis 10 dimensions, score 56/100
5. **[[TODO-pending|📋 TODO Pending]]** — tâches restantes priorisées
6. **[[quick-start|Quick-start]]** — commandes opérationnelles

## Qualification Kit G1→G2 (initiative courante)

- [[g1-g2-qualification-kit|Framework master — 16 livrables, 5 packages]]
- [[g1-g2-todo-tracker|Execution tracker]]
- [[gate-scorecard-spec|Gate scorecard — spec critères quantitatifs]]
- [[economic-thesis|Economic thesis — DRAFT needs user review]]
- [[failure-modes|Failure modes catalog]]
- [[strategy-lifecycle|Strategy lifecycle — sunset criteria]]
- [[feature-rejection-log|Feature rejection log — validation empirique 2026-04-20]]

## Execution & Performance Kit (2026-04-20)

- [[sessions/2026-04-20-execution-performance-kit|Session log complet]]
- Scripts : attribution / rolling / MC / CVaR-Kelly / drawdown / hourly / exec quality / markout / fill prob / digest
- Session filter : `src/pmhedge/alpha/session_filter.py` — bloque h06-h09 UTC empiriquement unprofitable
- Launchd : `com.paul.polymarket-alpha-perf-digest` daily 08:15 avec Telegram

## Hedge Fund Rigor Upgrade (2026-04-20)

- [[hedge-fund-rigor-upgrade|Methodology upgrade complet]]
- Scripts : tc_aware_attribution / diebold_mariano_test / var_es_kupiec / correlation_kelly / stationarity_tests / bonferroni_fdr_calibrators
- TC-aware sunset : CONFIRMED_YES, Miami, edge_tier_8_15 (CI95 post-TC < 0)
- Portfolio Kelly : -35% vs naive (cross-correlation adjusted)
- Stationarity : autocorrelation detected → HAC correction requise

## Contenu

### Architecture & Design
- [[architecture|Architecture hedge fund grade (4 couches)]]
- [[data-sources|Data sources inventory — best-in-class par région]]
- [[deep-learning-roadmap|Deep Learning Roadmap — 7 couches SOTA]]
- [[execution-playbook|Execution Playbook — 16 dimensions d'optimisation]]

### Roadmap & Decisions
- [[roadmap|Roadmap phased 4 semaines]]
- [[decisions|Log des décisions architecturales]]
- [[questions|Questions critiques + réponses]]

### Findings & Backtests
- [[findings|Diagnostics & edges détectés]]
- [[backtest-results/2026-04-17-baseline|Baseline backtest 2026-04-17]]

### Sessions
- [[sessions/2026-04-17-diagnostic-and-alpha-engine|Session 2026-04-17 #1: diagnostic + alpha engine v0]]
- [[sessions/2026-04-17-phase1-data-foundation|Session 2026-04-17 #2: Phase 1 data foundation + model hub]]
- [[sessions/2026-04-17-phase1-live-runner|Session 2026-04-17 #3: live runner end-to-end (19 signaux émis)]]
- [[sessions/2026-04-17-phase1-risk-orderbook|Session 2026-04-17 #4: CLOB orderbook + risk manager + ERA5]]
- [[sessions/2026-04-17-phase2-completion|Session 2026-04-17 #5: Phase 2 completion — CONFIRMED + paper shadow + XGBoost (25/25 tasks)]]
- [[sessions/2026-04-17-city-focused-analysis|Session 2026-04-17 #6: City-focused analysis — $728k/an paper, Mexico City Kelly 0.82]]
- [[sessions/2026-04-17-deep-learning-foundation|Session 2026-04-17 #7: Deep Learning foundation — DRN + Transformer + PPO + LLM + AIFS]]
- [[sessions/2026-04-18-overnight-model-upgrades|Session 2026-04-18 overnight: BMA + XGBoost training réel, backfill 100k obs, reconcile autonome, fix CONFIRMED_YES]]

## Métriques actuelles (2026-04-17)

| Métrique | Valeur |
|---|---|
| Settled trades (paper) | 6,740 |
| Signal types | 10 (CONVEX_YES, COLDMATH_NO, EXACT_BIN_YES, PROB_NO, PROB_YES, etc.) |
| Cities couvertes | 43 |
| Filter v1 PnL (bankroll $1k) | +$1,049 (+269% vs baseline) |
| Walk-forward Sharpe pooled | 16.4 |
| Data pipeline freshness | **12 jours stale** (à fix) |

## État actuel & prochaines étapes

✅ **25/25 tasks complétées en 5 sessions (2026-04-17, ~6h)** :
- Diagnostic complet + EdgeFilter v1 (session 1)
- Data Hub + Model Hub (EMOS + BMA) + Signal Generator (session 2)
- Live Runner end-to-end (session 3)
- CLOB orderbook + Risk Manager + ERA5 (session 4)
- CONFIRMED oracle + Paper Shadow + XGBoost (session 5)

**Architecture 4 couches opérationnelle** :
1. Data Hub (NWP multi-source + METAR + orderbook + ERA5)
2. Model Hub (EMOS + BMA + XGBoost)
3. Alpha Layers (CONFIRMED + MODEL_VS_MARKET + Sum-arb + EdgeFilter)
4. Risk + Execution (correlation Kelly + kill switch + paper shadow)

⏳ **Bloquants utilisateur pour go-live** :
1. Copernicus CDS account + ~/.cdsapirc
2. Run `backfill_era5.py --years 5` (1-3h)
3. Run `train_xgboost_post.py` (après ERA5)
4. Setup cron launchd (health/NWP/METAR/live runner/reconcile)
5. Polymarket wallet funded + private key
6. 30 jours paper shadow avant real money

## Related

- [[../_MOC|Brantham MOC]]
- [[../../_system/MOC-master|Master MOC]]
- Project code: `/Users/paul/polymarket-hedge/`
