---
name: Roadmap Polymarket Hedge Fund
description: Roadmap phased 4 semaines pour construire le système hedge fund grade
type: roadmap
created: 2026-04-17
tags: [polymarket, roadmap, planning]
---

# Roadmap — Polymarket Hedge Fund

**Principe** : phasing priorisé par EV/effort. Chaque phase livre valeur trackable. Pas de big bang.

## Phase 0 — FAIT (2026-04-17)

✅ Diagnostic complet 6,740 trades settled
✅ Identification edges rentables (PROB_NO, COLDMATH_NO, EXACT_BIN_YES)
✅ Identification poches toxiques (PROB_YES low-price, SPEEDA_EARLY, etc.)
✅ EdgeFilter v1 : pocket registry data-driven + Kelly sizing
✅ Backtest engine unifié : walk-forward + MC + attribution
✅ Metrics lib complète : Sharpe/Sortino/Calmar/VaR/attribution
✅ Markdown report generator
✅ Module `alpha/` scaffold (data_hub.py, nwp_sources.py)
✅ Architecture hedge fund 4-couches définie
✅ Questions critiques framework (93 questions)

**Livré** : Filter + Kelly transforme baseline -$620 en +$1,049 (Sharpe 12.3) sur bankroll $1k

## Phase 1 — Data Foundation (J1-J3)

**Objectif** : pipeline data fiable, fresh, multi-source. Sans ça rien d'autre ne marche.

### Tasks
- [ ] 1.1 — Finaliser `alpha/nwp_sources.py` : HRRR + ICON-EU + AROME + GFS + ECMWF fetchers
- [ ] 1.2 — `scripts/ingest_nwp_daily.py` : cron script quotidien (02:00 UTC après GFS 00Z)
- [ ] 1.3 — METAR 30-day rolling archive (écriture continue via scalper)
- [ ] 1.4 — ERA5 backfill script (5 ans × 40 stations, via `cdsapi`) — one-off download
- [ ] 1.5 — Polymarket CLOB WebSocket client : orderbook L2 depth snapshots
- [ ] 1.6 — Data freshness monitor + Telegram alerts si source DOWN
- [ ] 1.7 — Populate `market_resolutions` depuis settled trades + METAR history
- [ ] 1.8 — Seed `stations` table (40+ stations Polymarket)

**Livrable** : DB `alpha_data_hub.db` peuplée avec :
- 40 stations registered
- NWP forecasts des 7 derniers jours (4 sources × 40 stations)
- METAR 30-day history × 40 stations
- ERA5 training data 5 ans × 40 stations
- Orderbook snapshots en temps réel
- Freshness status OK sur toutes sources

## Phase 2 — Model Hub (J4-J10)

**Objectif** : modèle ML qui produit P(T_max) calibré mieux que marché.

### Tasks
- [ ] 2.1 — `alpha/emos.py` : EMOS calibration par (station × mois) sur ERA5
- [ ] 2.2 — `alpha/bma.py` : Bayesian Model Averaging online weights
- [ ] 2.3 — `alpha/xgboost_post.py` : XGBoost post-proc avec features riches
- [ ] 2.4 — Feature engineering pipeline : NWP ensemble stats + obs lags + radar + climato
- [ ] 2.5 — Training pipeline + eval harness (RMSE, CRPS, reliability diagram, Brier)
- [ ] 2.6 — Model evaluation dashboard
- [ ] 2.7 — Monthly retrain cron
- [ ] 2.8 — Model versioning (git tags + DB `model_performance` table)

**Livrable** : model v1 beats baseline NWP de 10-20% sur RMSE, 15-25% sur CRPS

## Phase 3 — Alpha + Execution (J11-J17)

**Objectif** : signaux alpha + execution propre + risk management.

### Tasks
- [ ] 3.1 — `alpha/signal_generator.py` : unified signal emission (model vs market)
- [ ] 3.2 — `alpha/sum_arb_live.py` : sum-to-1 arb scanner temps réel avec orderbook
- [ ] 3.3 — `alpha/confirmed_oracle.py` : debug + fix CONFIRMED (jamais triggered)
- [ ] 3.4 — `alpha/orderbook_imbalance.py` : microstructure alpha
- [ ] 3.5 — Order manager : limit-first + cancel-replace + rebate capture
- [ ] 3.6 — Slippage auto-calibration online (EMA sur fills historiques)
- [ ] 3.7 — Risk manager : Kelly correlation-adjusted + caps + kill switch
- [ ] 3.8 — `scripts/run_alpha_live.py` : main orchestrator live mode

**Livrable** : bot live mode avec 3+ alphas actifs, paper shadow pendant 7 jours

## Phase 4 — Scale + Advanced (J18-J28)

**Objectif** : extend alphas + neural models + monitoring hedge-fund grade.

### Tasks
- [ ] 4.1 — `alpha/drn.py` : Distributional Regression Network (PyTorch)
- [ ] 4.2 — `alpha/nowcast.py` : radar + HRRR blend pour 0-6h
- [ ] 4.3 — `alpha/cross_market.py` : pairs trading inter-villes
- [ ] 4.4 — `alpha/analog.py` : k-NN sur patterns synoptiques pour events rares
- [ ] 4.5 — Grafana dashboard + Prometheus metrics
- [ ] 4.6 — Monitoring stack (VPS primary AWS + backup Hetzner)
- [ ] 4.7 — Health checks + failover automatique
- [ ] 4.8 — Documentation complète

**Livrable** : système prod-ready, paper-validated 30 jours, ready for small capital deploy

## Phase 5 — Live Deploy (J29+)

**Objectif** : deploy real money small, scale si validé.

### Tasks
- [ ] 5.1 — Fund wallet Polymarket ($500-$1000)
- [ ] 5.2 — Deploy on VPS avec monitoring full
- [ ] 5.3 — Start LIVE avec filter strict + caps conservatives
- [ ] 5.4 — Daily reconciliation backtest vs live
- [ ] 5.5 — Scale decision : si +$20-50/jour sur 14j, double bankroll
- [ ] 5.6 — Continue scaling jusqu'à $10-25k si perfs tenables
- [ ] 5.7 — Expansion universe (sport, crypto) si weather saturé

## Dépendances + risques

**Bloquants** :
- Capital réel non précisé
- Private key Polymarket à confirmer
- VPS à provisionner (ou utiliser existant ?)

**Risques tech** :
- Open-Meteo rate limit 10k/jour — si dépassé, fallback direct NOMADS
- ERA5 download lent (plusieurs heures)
- Polymarket CLOB API changes
- Model overfitting (mitigé par walk-forward + paper shadow)

**Risques business** :
- Concurrence bots autres traders weather
- Liquidité thin limitant scale
- Oracle disputes rares mais ruineuses
- Regulatory changes Polymarket

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture]]
- [[data-sources|Data sources]]
- [[questions|Questions critiques]]
- [[sessions/2026-04-17-diagnostic-and-alpha-engine|Session kickoff]]
