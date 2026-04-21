---
name: Polymarket Hedge Fund — Architecture Map
description: Vision ultra-claire du stack après cleanup 2026-04-21. Modules, scripts, launchd, DBs, vault docs avec responsabilité de chacun. Point d'entrée pour toute nouvelle session.
type: architecture
project: brantham/polymarket
created: 2026-04-17
updated: 2026-04-21
tags: [polymarket, architecture, infra, cleanup]
priority: critical
---

# Polymarket Hedge Fund — Architecture Map

**Entrée rapide** : toute nouvelle session lit ce doc + [[MODEL-STATE-COMPLETE]] + [[CONTINUATION-PROMPT]].

## 1. FLUX DE DONNÉES (signal → trade)

```
┌─────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│  12 NWP sources │   │   METAR + ERA5   │   │  Polymarket API  │
│  (Open-Meteo +  │   │   observations   │   │  (Gamma / CLOB)  │
│   Pangu local)  │   │                  │   │                  │
└────────┬────────┘   └────────┬─────────┘   └────────┬─────────┘
         │                     │                      │
         ▼                     ▼                      ▼
   ┌──────────────────────────────────────────────────────────┐
   │             alpha_data_hub.db  (source of truth)         │
   │  nwp_forecasts · obs_temperature · stations · calibrators│
   └──────────────────────────┬───────────────────────────────┘
                              │
         ┌────────────────────┴────────────────────┐
         ▼                                         ▼
   ┌──────────────┐                        ┌──────────────┐
   │ Training jobs│                        │ Live scanner │
   │  (launchd)   │                        │   300s loop  │
   └──────┬───────┘                        └──────┬───────┘
          │                                       │
          ▼                                       ▼
   EMOS · BMA · XGB · HMM · Calibrators     signal_generator
                                                  │
                                                  ▼
                          ┌─────────────────────────────┐
                          │  Filters (séquentiels):     │
                          │  1. city_config (DISABLED?) │
                          │  2. alpha_states (kill?)    │
                          │  3. ttr_filter (denylist?)  │
                          │  4. session_filter          │
                          │  5. tail_filter             │
                          │  6. volatility_filter       │
                          │  7. calibration per-city    │
                          │  8. risk_manager (Kelly)    │
                          └─────────────┬───────────────┘
                                        │
                                        ▼
                                  persist_signal
                                        │
                                ┌───────┴───────┐
                                ▼               ▼
                          signal_log       execute_signal
                                                │
                                                ▼
                          bucket_router (S/A/C tier assignment)
                                                │
                                                ▼
                                           trade_log
                                                │
                                     (reconcile cron 09:20)
                                                │
                                                ▼
                                        signal_outcomes
                                                │
                                                ▼
                                    trade CLOSED + pnl_usdc
```

## 2. MODULES CORE (`src/pmhedge/alpha/` — 68 fichiers)

### Pipeline principal (ordre d'exécution)
| Module | Rôle |
|--------|------|
| `data_hub.py` | DB schema + connexions + alpha_states kill-switch |
| `nwp_sources.py` | 12 sources NWP (GFS/GEFS/ICON/ECMWF/AIFS/HRRR/JMA/UKMO/CMA/GRAPHCAST/AROME) |
| `pangu_runner.py` | **[NEW]** Pangu-Weather local inference (M5 CoreML) |
| `era5_ingest.py` | **[NEW]** ERA5 via CDS API pour Pangu input |
| `ecmwf_client.py` | Stub ECMWF payant (optionnel, inutile car OpenData gratuit dispo) |
| `mesonet_client.py` | Stub Mesonet Synoptic (free tier dispo) |
| `forecast_cache.py` | Cache 6h pour éviter re-fetch |
| `feature_engineering.py` | 37 features (climato, lag, UHI, cross-station) |
| `diurnal_features.py` | t_prev_{06,12,15,18}z + slopes |
| `synoptic_features.py` | ONI / NAO / AO / PNA |
| `soil_moisture.py` | sm_0_7cm + aridity_z |
| `emos.py` | Gneiting 2005 per-station × month |
| `bma.py` | Bayesian model averaging (12 sources → weights) |
| `xgboost_post.py` | Residual correction regional + per-station |
| `regime_hmm.py` | 3-state HMM (CALM/TRANSITION/STORMY) |
| `regime_selector_v2.py` | XGB continuous regime inference |
| `gmm_forecast.py` | Mixture model fallback |
| `calibration.py` | Isotonic K-fold global + per-city |
| `tail_filter.py` | Reject YES tail > climo+2σ |
| `volatility_filter.py` | σ threshold per (alpha, zone/city) |
| `ttr_filter.py` | **[NEW]** Deny-list per (city, TTR-bucket) |
| `session_filter.py` | Block h06-09 UTC loss hours |
| `bucket_router.py` | **[NEW]** Tier S/A/C/KILL + Kelly multiplier |
| `risk_manager.py` | Kelly sizing + portfolio factor + circuit breaker |
| `city_config.py` | Per-city DISABLED/ENABLED + Kelly override |
| `signal_generator.py` | **Orchestre tout ci-dessus + persist_signal** |
| `live_executor.py` | **[NEW]** Bridge signal → trade_log (paper fill avec slippage EMA) |

### Alpha types
| Module | Alpha type |
|--------|------------|
| `signal_generator.py` | MODEL_VS_MARKET (principal, Tier S/A) |
| `confirmed_oracle.py` | CONFIRMED_NO (oracle, CONFIRMED_YES KILLED) |
| `pair_arb.py` | PAIR_ARB (rare) |
| `sum_arb.py` | SUM_ARB (rare) |
| `convex_arb.py` | CONVEX_ARB (dormant) |
| `orderbook_imbalance.py` | OB_IMBALANCE (dormant) |
| `market_making.py` | Market maker (dormant) |

### Risk / Capital
| Module | Rôle |
|--------|------|
| `compound_engine.py` | Dynamic bankroll $1k → $100k |
| `concurrent_positions.py` | Cap 50 positions simultanées |
| `vol_targeting.py` | Vol targeting opt-in |
| `conformal.py` | Conformal prediction intervals |
| `var_cvar.py` | Value-at-Risk + CVaR-Kelly |

### Meta-learning / observabilité
| Module | Rôle |
|--------|------|
| `bandit_allocator.py` | Thompson sampling entre alphas |
| `champion_challenger.py` | A/B test modèles |
| `model_registry.py` | Versioning modèles |
| `mlflow_logger.py` | MLflow tracking |
| `freshness.py` | Data staleness detection |

### Dormant / scaffolds
| Module | Status |
|--------|--------|
| `kalshi_client.py` | Cross-venue arb (dormant) |
| `goes_satellite.py` | GOES-18 nowcast (dormant) |
| `llm_features.py` | Claude API features (opt-in) |
| `monsoon_features.py` | Monsoon-aware (opt-in) |
| `altitude_features.py` | Topographie (opt-in) |

## 3. MODULES EXECUTION (`src/pmhedge/execution/` — 9 fichiers)

| Module | Rôle |
|--------|------|
| `order_manager.py` | CLOB order lifecycle (stub py-clob-client, prêt live) |
| `optimal_execution.py` | TWAP / VWAP |
| `slippage.py` | Slippage EMA per market/size |
| `latency.py` | Latency tracking |
| `market_maker.py` | **[NEW scaffold]** Maker rebate mode |
| `mev_protection.py` | MEV protection Polygon |
| `rpc_supervisor.py` | RPC health |
| `dashboard.py` | FastAPI dashboard backend (legacy, port 8080) |
| `metrics.py` | Prometheus metrics |

## 4. SCRIPTS (`scripts/` — 150 actifs + legacy/)

### Scripts essentiels (entrypoints canoniques)
| Script | Rôle |
|--------|------|
| `run_alpha_live.py` | **Scanner live loop 300s** (launchd PID persistant) |
| `run_pangu_cycle.py` | **[NEW]** Pangu forecast cycle (ingest ERA5 + inference) |
| `setup_pangu.py` | **[NEW]** Setup Pangu stack (download + verify) |
| `alpha_tui.py` | **[NEW] TUI Rich — canonical dashboard** |
| `alpha_dashboard.py` | Web dashboard (port 8090, launchd KeepAlive) |
| `trade_status.py` | CLI snapshot rapide |
| `city_optimizer.py` | **[NEW]** Tuning per-city auto |
| `city_deep_dive.py` | **[NEW]** Rapport markdown par ville |
| `reconcile_from_obs.py` | Réconciliation signaux ↔ observations + close trades |

### Scripts training (tous dans launchd)
`train_bma.py`, `train_emos_per_station.py`, `train_calibrators.py`, `train_city_calibrators.py`, `train_drn.py`, `train_ensemble_weights.py`, `train_model.py`, `train_quantile_regressors.py`, `train_regime_hmm.py`, `train_pangu_city.py` (scaffold)

### Legacy archivé (`scripts/legacy/`)
`analyze_coldmath.py`, `run_bracket_scalper.py`, `dashboard.py`, `dashboard_tui.py`, `dashboard_quant.py`

## 5. LAUNCHD JOBS (54 actifs après cleanup)

### Par catégorie

**Live (1)** : `live-runner` (loop 300s)

**Data ingest (5)** : `nwp-ingest`, `metar-archive`, `soil-ingest`, `synoptic-fetch`, `event-alerts`

**Training (11)** : `bma-train`, `emos-train`, `ensemble-train`, `hmm-train`, `regime-v2-train`, `station-xgb`, `xgb-retrain`, `calibration`, `calibrators-train`, `city-calibrators`, `quantile-train`, `conformal`

**Tuning quotidien (6)** : `city-optimizer` (09:30), `ttr-denylist` (09:45), `city-kelly`, `bandit-allocator`, `vol-filter`, `city-audit`

**Reconcile / Settle (7)** : `reconcile` (generic), `reconcile-obs` (09:20 + close trades), `auto-settle`, `daily-pnl`, `daily-summary`, `perf-digest` (08:15), `perf-metrics`

**Monitoring (9)** : `circuit-breaker`, `drift-monitor`, `decay-monitor`, `health-check`, `mc-var`, `attribution`, `gate-scorecard` (08:00), `validator`, `pair-corr`

**Oracle scans (4)** : `oracle-scan-0300/0907/1032/1617`

**Dashboards + bot (3)** : `alpha-dashboard` (port 8090), `telegram-bot`, `prom-exporter`

**Utilities (8)** : `audit-prune`, `db-snapshot`, `caffeinate`, `paper-session`, `precompute`, `scan-freq`, `scan-night`

## 6. DATABASES (15 SQLite)

### DBs actives (source de vérité)
| DB | Rôle |
|----|------|
| **`alpha_data_hub.db`** | **PRINCIPAL** : signals, trades, outcomes, forecasts, calibrators, config |
| `city_models.db` | XGB models per-station + climatology cache |
| `all_markets.db` | Polymarket markets historique (slugs, metadata) |

### DBs legacy (encore lues par des scripts archivés)
| DB | Last modif | Status |
|----|-----------|--------|
| `bracket_scalper_trades.db` | 2026-04-21 | Ancien scalper — 21 refs |
| `pmhedge.db` | 2026-04-20 | Old bracket system |
| `oracle_data.db` | 2026-04-09 | Oracle backtest session 6 |
| `mega_dataset.db` | 2026-04-16 | Training mega-dataset |
| `wu_tmax_dataset.db` | 2026-04-16 | Weather Underground hist |
| `metar_wu_validation.db` | 2026-04-16 | METAR vs WU validation |
| `coldmath_trades.db` | 2026-04-05 | COLDMATH désactivé session 7 |
| `emos_alpha.db` | 2026-04-20 | EMOS cache alternatif |
| `sum_arb_trades.db` | 2026-04-07 | SUM_ARB rare |
| `backtest_data.db` | 2026-03-30 | Ancien backtest |
| `emos_cache.db` | 2026-04-21 | EMOS cache actif |

**Cleanup futur** : archiver 8 DBs dans `backups/legacy-dbs/` après audit complet dépendances.

## 7. VAULT (`/Users/paul/vault/brantham/polymarket/`)

### Core docs (à lire en priorité)
- **`ARCHITECTURE.md`** (ce doc) — vision structurelle
- `MODEL-STATE-COMPLETE.md` — snapshot zéro-omission models
- `CONTINUATION-PROMPT.md` — prompt à copier dans nouvelle session
- `STATE-HANDOFF.md` — état global actualisé

### Strategy & findings
- `weather-domination-strategy.md` — décision weather only
- `economic-thesis.md` — DRAFT (bloquant G1 user review)
- `city-optimization.md` — kill/boost list per city
- `deep-learning-roadmap.md`
- `findings.md`

### Per-city (31 rapports)
- `city-reports/_SUMMARY-2026-04-21.md` — vue d'ensemble
- `city-reports/<slug>.md` — rapport détaillé par ville (27 + 4 sessions)

### Sessions (chronologique)
- `sessions/2026-04-20-polymarket-exec-wire.md`
- `sessions/2026-04-20-g1-g2-kit-build.md`
- Plus anciennes

### Quality / gates
- `g1-g2-qualification-kit.md`
- `g1-g2-todo-tracker.md`
- `gate-scorecard-spec.md`
- `audit-hedge-fund-grade.md`

## 8. DATA FLOW RÉEL (après cleanup)

### Signal émis toutes les 5 minutes
1. Scanner fetch 348 markets Polymarket actifs
2. Pour chaque (icao, target_date), enrich features
3. Apply ensemble (BMA + XGB + HMM)
4. Calibration per-city
5. 8 filtres séquentiels (voir Flow Diagram)
6. `persist_signal` → signal_log
7. `execute_signal` → trade_log FILLED (slippage-adjusted)

### Settlement toutes les 24h (09:20 UTC)
1. `reconcile_from_obs.py` fetch observations (METAR + ARCHIVE)
2. Match (icao, target_date) → compute outcome_yes
3. INSERT INTO signal_outcomes
4. `close_resolved_trades` → trade_log CLOSED + pnl_usdc

### Monitoring quotidien
- 08:00 `gate-scorecard` → G1 status
- 08:15 `perf-digest` → Telegram
- 09:00 `daily-pnl` → track_record.csv
- 09:20 `reconcile-obs` → outcomes + close trades
- 09:30 `city-optimizer` → DISABLED/BOOST per ville
- 09:45 `ttr-denylist` → refit per (city, bucket)

## 9. COMMANDES PRATIQUES

```bash
cd /Users/paul/polymarket-hedge

# Status rapide
uv run python scripts/trade_status.py

# TUI live
uv run python scripts/alpha_tui.py

# Web dashboard
open http://127.0.0.1:8090

# Deep dive une ville
uv run python scripts/city_deep_dive.py --city austin

# Tuner per-city manuel
uv run python scripts/city_optimizer.py --apply

# Setup Pangu (après download complet)
uv run python scripts/setup_pangu.py --verify

# Run Pangu cycle (après ~/.cdsapirc setup)
uv run python scripts/run_pangu_cycle.py --steps 3

# Force scan manuel
uv run python scripts/run_alpha_live.py --once
```

## 10. CLEANUP DONE (2026-04-21)

- ✅ Delete `pangu_forecaster.py` (scaffold orphelin)
- ✅ Disable launchd `polymarket-dashboard` (ancien web_dashboard port 8765 en conflit)
- ✅ Move legacy scripts vers `scripts/legacy/` (5 fichiers)
- ✅ 54 launchd jobs actifs (était 55)
- ✅ Documentation architecture ce doc

## 11. CLEANUP RESTANT (à faire quand Paul valide)

- [ ] Archive DBs legacy (8 DBs) dans `backups/legacy-dbs/` après audit dépendances
- [ ] Re-check 100+ scripts non-listés (probablement 30-40% legacy)
- [ ] Tests unitaires pour `bucket_router.py`, `ttr_filter.py`, `live_executor.py`
- [ ] Consolider 2 systèmes coexistants : migrer complètement `pmhedge.db` → `alpha_data_hub.db`

## Related

- [[MODEL-STATE-COMPLETE]]
- [[CONTINUATION-PROMPT]]
- [[STATE-HANDOFF]]
- [[city-optimization]]
- [[_MOC]]
