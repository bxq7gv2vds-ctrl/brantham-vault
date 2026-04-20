---
name: MODEL STATE COMPLETE — 2026-04-20 snapshot
description: Zero-omission snapshot of every model, feature, filter, data source, calibration, risk band, meta-layer currently in the Polymarket weather hedge fund stack. For context-clear recovery focused on models specifically.
type: snapshot
priority: critical
created: 2026-04-20
tags: [polymarket, models, snapshot, handoff, zero-omission]
---

# MODEL STATE COMPLETE — snapshot zéro-omission 2026-04-20

Ce doc est la **source de vérité** pour tout ce qui concerne les modèles. Un Claude qui reprend après context clear doit pouvoir reconstruire 100% du stack modèle depuis ce doc.

## 1. DATA SOURCES (inputs)

### NWP forecasts (12 sources)
Tables : `nwp_forecasts` (~310k rows), `nwp_ensemble_blend` (~17k rows)
Ingest : `nwp-ingest` cron 4×/jour (00/06/12/18 UTC)
Sources : **GFS, GEFS, ICON, ICON_EU, ECMWF, AIFS, HRRR, JMA, UKMO, CMA, GRAPHCAST, AROME**
Endpoint : Open-Meteo unified (sauf GRAPHCAST via dedicated endpoint)

### Observations (510k rows)
Table : `obs_temperature`
Sources :
- **METAR** (rolling 30j via `metar_archive.py`)
- **ARCHIVE** (Open-Meteo ERA5-derivé 90j backfilled)
- **WU_HISTORICAL** (Weather Underground legacy dataset)

### Synoptic indices (monthly)
Table : `synoptic_indices` (8560 rows)
Sources NOAA CPC :
- **ONI** (914 mois depuis 1950) — El Niño/La Niña
- **NAO** (915 mois) — North Atlantic Oscillation
- **AO** (915 mois) — Arctic Oscillation
- **PNA** (915 mois) — Pacific North American
- **PDO** (2067 mois) — Pacific Decadal Oscillation
- **DMI/IOD** (1864 mois) — Dipole Mode Index (Indian Ocean)
Refresh : cron monthly (synoptic-fetch daily placeholder)

### Soil moisture
Table : `soil_moisture` (60 rows, en croissance)
Source : Open-Meteo soil API
Cron : `alpha-soil-ingest` daily 03:30

### Climatology
Built from `obs_temperature` via `feature_engineering._load_climatology`
Cache : `city_models.db` (46 stations × 12 mois × 338 samples)
Columns : mean_c, std_c, p05-p95 per (icao, month)

### NWS weather alerts (NEW 2026-04-20)
Table : `event_alerts`
Source : api.weather.gov/alerts/active (NWS JSON API)
Cron : `com.paul.polymarket-alpha-event-alerts` toutes 30 min
Events filtered : heat/cold/freeze/hurricane/winter storm/red flag/dense fog/dust/ice
Current count : 63 active alerts

### Polymarket markets
Endpoint : Polymarket Gamma API `/public-search`
Cache : 60s TTL via `polymarket_client.fetch_active_bracket_markets`
Typical : 370 active weather bracket markets
Latency : P95 1.03s (was 3.9s before optimization)

### Station geolocation
Table : `stations` (46 rows)
Columns : icao, city_slug, lat, lon, **elevation_m** (backfilled 2026-04-20), country, timezone, utc_offset_h

### Data pending activation (user unlocks)
- **ERA5 Copernicus CDS** (user account) — débloque DRN + multi-year validation
- **Pangu-Weather ONNX** (user file drop) — +5-10% CRPS SOTA
- **Mesonet Synoptic** (user API token free 5k calls/day) — dense US stations
- **GOES-18 satellite** (free NOAA S3, boto3 install) — nowcast H0-H6
- **LLM features Claude API** (user `ANTHROPIC_API_KEY`) — +3-5% event edge

## 2. FORECAST MODELS (ordre d'application)

### 2.1 Climatology (baseline)
Module : `feature_engineering._load_climatology`
Buckets : 46 stations × 12 mois = 552
Use : prior distribution per (station, month)

### 2.2 EMOS per-station × month
Module : `src/pmhedge/alpha/emos.py`
Params : 506 buckets × 4 params (a, b, c, d)
Model : Gneiting 2005 non-homogeneous Gaussian regression
Training : `scripts/train_emos_per_station.py`, 338 samples per station-month
CRPS : moyenne 0.36°C ; meilleur HECA 0.22 ; pire RKSI 0.64 (Seoul — finding documented)

### 2.3 BMA (Bayesian Model Averaging)
Module : `src/pmhedge/alpha/bma.py`
Weights : per-station × source = **47 × 12 = 564 params** (+1 GLOBAL fallback)
Combiner : mixture Gaussian moment-matched (mu_BMA, sigma²_BMA)
Training : `scripts/train_bma.py` — EWMA update (alpha=0.1, half-life ~7 obs)
Cron : `alpha-bma-train` daily 03:30

### 2.4 XGBoost post-proc regional (10 régions)
Module : `src/pmhedge/alpha/xgboost_post.py`
Files : `models/xgb_postproc_{US_EAST,US_WEST,EU_WEST,EU_CENTRAL,EU_EAST,JP_KR,CN,TW_SEA,IN_ME,LATAM,OCEANIA,CA}.json`
Target : residual = T_obs - BMA_mu
Features : 36 variables (ensemble stats + obs lags + temporal + geo + climato + diurnal + synoptic + soil)
Train : `scripts/train_xgboost_post.py`, RMSE val 0.6-1.4°C
Cron : weekly + on-demand

### 2.5 XGBoost per-station (46 models)
Module : `src/pmhedge/alpha/xgboost_post.py::train_region_model`
Files : `models/xgb_station_{ICAO}.json` + `.meta.json`
Last retrain : 2026-04-20 avec feature rejections appliquées
Best RMSE : WMKK 0.216°C ; pire RKSI 1.658°C
Cron : `alpha-station-xgb` weekly Fri 05:15

### 2.6 DRN (Distributional Regression Network)
Module : `src/pmhedge/alpha/drn.py` + `models/drn.pt`
**Status : DISABLED** (`DRN_DISABLED_UNTIL_ERA5=True`)
Raison : val CRPS 1.22 vs BMA 0.48. Pollue l'ensemble sans ERA5 training data propre.
Weight = 0 dans `ensemble_weights` et `ensemble_weights_regime`

### 2.7 Regime HMM (Gaussian 3-state × 4 climate zones)
Module : `src/pmhedge/alpha/regime_hmm.py`
Files : `models/regime_hmm_{TROPICAL,SUBTROPICAL,TEMPERATE,POLAR}.pkl` + `.meta.json`
States : CALM / TRANSITION / STORMY
Kelly multipliers : 1.0 / 0.8 / 0.4
Cron : `alpha-hmm-train` weekly Fri 05:30

### 2.8 Regime selector V1 + V2
Files : `regime_selector.py` (12 buckets), `regime_selector_v2.py` (XGB continuous)
Use : pick ensemble weights per régime
Train : weekly crons

### 2.9 Pangu-Weather (SCAFFOLD — awaiting user ONNX file)
Module : `src/pmhedge/alpha/pangu_forecaster.py`
ONNX path expected : `models/pangu_24h.onnx`
Wire ready : `RegionalFetcher.build()` in 5 min post-drop

### 2.10 Quantile XGBoost + Conformal
Files : `models/xgb_quantile_*.json` (q005-q099 per region)
**Status : DISABLED default** (ablation showed Brier 0.1010 vs 0.0815 Gaussian — hurts)
Flag : `use_quantile=False`

### 2.11 GMM forecast mixture (dormant)
Module : `src/pmhedge/alpha/gmm_forecast.py`
Status : 2-component Gaussian mixture, ready but not wired

### 2.12 Gaussian integration (final step)
Module : `src/pmhedge/alpha/model_prob.py`
Compute : `P(bracket_lo ≤ T ≤ bracket_hi | N(mu, sigma²))`

## 3. POST-PROCESSING LAYERS

### 3.1 Isotonic calibration — GLOBAL
Table : `calibrators` (1 row, refit daily)
Module : `src/pmhedge/alpha/calibration.py`
Data : K-fold on all MODEL_VS_MARKET outcomes
Cron : `alpha-calibrators-train` daily 04:15

### 3.2 Isotonic calibration — PER CITY (15/21 ENABLED)
Table : `calibrators_city` (15 rows × alpha_type)
Cities fitted : atlanta, austin, beijing, chicago, dallas, denver, houston, KL, LA, miami, NYC, san francisco, shenzhen, tokyo, mexico city, HK (+CONFIRMED_YES miami, CONFIRMED_NO denver)
Cron : `alpha-city-calibrators` daily 04:20
**Bonferroni + BH FDR verified : 21/21 p<0.001** (all statistically robust)

### 3.3 Volatility filter (thresholds per zone + city)
Table : `volatility_thresholds` (2 rows : SUBTROPICAL σ 2.13, TROPICAL σ 1.49)
Table : `volatility_thresholds_city` (2 rows : beijing σ 1.91, miami σ 1.72)
Other cities : no significant gap detected statistically
Module : `volatility_filter.py`
Cron : `alpha-vol-filter` daily 04:30

### 3.4 Tail filter (YES tail bets)
Module : `src/pmhedge/alpha/tail_filter.py`
Rule : reject YES signal where `bracket_lo_c > climo_mean + 2 × climo_std`
Empirical : 95/95 Tokyo/NYC YES tail losses preempted
Config : `SignalGenConfig.use_tail_filter=True`, `tail_sigma_mult=2.0`

### 3.5 Edge band blocker (NEW 2026-04-20)
Module : `signal_generator.py`
Config : `SignalGenConfig.edge_band_blocked = (0.08, 0.15)`
Justification : tc_aware_attribution CI95 [-0.31, -0.18] sur tier_8_15 = statistiquement sunset
Effet : rejette signaux où |edge| ∈ [8%, 15%)

### 3.6 Session filter h06-h09 UTC (NEW 2026-04-20)
Module : `src/pmhedge/alpha/session_filter.py`
Blocked hours UTC : {6, 7, 8, 9}
Override : env `PMHEDGE_BLOCKED_HOURS=csv`
Empirical : ROI -47% à -36% sur N=92 sessions Asian morning

### 3.7 NWP disagreement features
Module : `feature_engineering.add_nwp_disagreement_features`
Cols : nwp_disagreement_c, nwp_disagreement_ratio, nwp_disagreement_pct
**Status : disabled by default** (validation empirique INCONCLUSIVE, H0016 PARTIAL)

### 3.8 Monsoon features v1 rule-based
Module : `src/pmhedge/alpha/monsoon_features.py`
**Status : disabled by default** (H0013 REJECTED — mean Δ -0.002°C)

### 3.9 Altitude features
Module : `src/pmhedge/alpha/altitude_features.py`
**Status : disabled by default** (H0014 REJECTED — mean Δ -0.0006°C)

### 3.10 City feature profiles (masks)
Module : `src/pmhedge/alpha/city_feature_profiles.py`
Masks : Singapore (soil_aridity_z), Moscow (NAO, PNA), Chongqing (NAO, PNA), etc.

### 3.11 Intraday Bayesian update (NEW 2026-04-20)
Module : `src/pmhedge/alpha/intraday_update.py`
Function : `refine_intraday(icao, target_date, mu_fcst, sigma_fcst, now_ts)` → posterior mu/sigma
Uses : DIURNAL_FRACTION climato × obs_so_far_today → Bayesian combine
Certainty levels : prior / partial / near_final / confirmed
**Status : ready to wire in signal_generator** (module tested, not yet wired)

## 4. SIGNALS / ALPHAS

### 4.1 MODEL_VS_MARKET (core alpha) — ENABLED
Module : `signal_generator.py::create_model_vs_market_signal`
Outcomes : 1027 settled
Gross ROI : +88%, net after TC : +83%
t-stat : +6.93 → KEEP (decay monitor)
Bandit weight : 72.22%

### 4.2 CONFIRMED_NO — ENABLED
Module : `confirmed_oracle.py`
Outcomes : 55 settled
ROI : +19% gross, +13% net
t-stat : +36.16 → KEEP (exceptional, convex NO tails)
Bandit weight : 27.78%

### 4.3 CONFIRMED_YES — RE-ENABLED 2026-04-20 (with guardrails)
**Previously** : DISABLED after 31 legacy signaux ROI -100% (prev_day bug)
**Now** : same-day logic strict (N≥4 obs AND obs_max≥bracket_hi OR h≥22 and obs_max<bracket_lo)
Module : `confirmed_oracle.py::_get_tmax_for_market` (refined 2026-04-20)
alpha_states : ENABLED with documented reason

### 4.4 PAIR_ARB — active
Module : `src/pmhedge/alpha/pair_arb.py`
Table : `pair_correlations` (28 filtered pairs, mean∆ ≤ 5°C)

### 4.5 CONVEX_ARB — opt-in (dormant)
Module : `src/pmhedge/alpha/convex_arb.py`
Flag : `enable_convex_arb=False`

### 4.6 OB_IMBALANCE — opt-in (dormant)
Module : `src/pmhedge/alpha/orderbook_imbalance.py`
Flag : `enable_ob_imbalance=False`

### 4.7 SUM_ARB — backtest mode
Module : `src/pmhedge/alpha/sum_arb.py`

### 4.8 XVENUE_ARB Kalshi — scaffold, Kalshi ticker obsolete
Module : `src/pmhedge/alpha/kalshi_client.py`
Script : `scripts/scan_xvenue_kalshi.py`
Fetch current : Polymarket 370 markets, Kalshi 0 (HIGHNY ticker obsolete)

## 5. RISK MANAGEMENT

### 5.1 Kelly sizing (correlation-adjusted scalar)
Module : `risk_manager.py::compute_portfolio_factor`
Formula : `factor = 1 / sqrt(1 + (n-1) × ρ_avg)`
Default active.

### 5.2 Portfolio Kelly full matrix (NEW, opt-in)
Module : `risk_manager.py::compute_portfolio_kelly_weights`
Formula : `f* = (C + λI)^{-1} · f_naive`
Flag : `RiskConfig.use_portfolio_kelly=False` (backward-compat default)
Empirical : -35% vs naive scalar (more conservative)

### 5.3 Drawdown bands (NEW 2026-04-20)
Module : `risk_manager.py::compute_dd_multiplier`
Bands : 0-3% NORMAL (×1.0) / 3-5% CAUTION (×0.8) / 5-8% REDUCED (×0.5) / 8-10% KILL (×0.0) / >10% BREAKER (×0.0 + manual rearm)
Source data : `compound_state` peak vs current
Config : `RiskConfig.dd_bands_enabled=True`

### 5.4 Kill switch daily loss cap (legacy)
Module : `risk_manager.py::evaluate_batch`
Cap : `cfg.daily_loss_cap_pct = 0.10`

### 5.5 Circuit breaker alpha drift
Module : `risk_manager.py::check_alpha_drift`
Table : `alpha_states`
Triggers : drift > 8pts OR ECE > 0.20 → auto-DISABLE

### 5.6 Per-city config auto-audit
Module : `scripts/audit_per_city.py`
**NEW criteria (2026-04-20)** :
- DISABLED si `net_roi_ci95_upper < 0` ET N≥30 (post-TC sunset)
- Override ENABLED si `net_roi_ci95_lower > 0` ET N≥30 (stat-profitable)
Current : 4 DISABLED (NYC, miami, chicago, tokyo), 2 SHADOW (dallas, mexico city), 20 ENABLED

### 5.7 CVaR-aware Kelly
Script : `scripts/cvar_kelly.py`
Output : fraction capped par CVaR95 worst-case cluster loss
Empirical : pure Kelly 0.058, CVaR-binding ratio 1.0 (non-binding)

### 5.8 VaR/ES/Kupiec/Christoffersen
Script : `scripts/var_es_kupiec.py`
Framework : Historical + Parametric + Monte Carlo + Kupiec POF + CC
**T=2 jours distincts** — framework ready, pas exécutable encore

### 5.9 Bandit allocator (Thompson sampling)
Module : `src/pmhedge/alpha/bandit_allocator.py`
Table : `alpha_allocator_weights`
Method : Normal-Inverse-Gamma conjugate prior, 200 samples per alpha
Bounds : [5%, 50%] per alpha
Cron : `alpha-bandit-allocator` daily 05:45
**Wired** dans `signal_generator._bandit_weight(alpha_type)` — cache 15min

### 5.10 Alpha decay monitor
Script : `scripts/alpha_decay_monitor.py`
Tables : `alpha_decay_log` + `alpha_states`
Logic : t-stat rolling 14d + 60d → DISABLE/SHADOW/KEEP
Cron : `alpha-decay-monitor` daily 06:00 `--apply`

### 5.11 Compound engine (NEW)
Module : `src/pmhedge/alpha/compound_engine.py`
Tables : `compound_state`, `compound_withdrawals`
Current : $1000 starting (paper session #1 started 2026-04-20)
Functions : `current_bankroll()`, `snapshot()`, `record_withdrawal()`, `project_to_target()`

### 5.12 Concurrent positions tracker
Module : `src/pmhedge/alpha/concurrent_positions.py`
Table : `concurrent_positions`
Status : module ready, NOT yet wired dans `persist_signal`

### 5.13 Vol targeting portfolio-level
Module : `src/pmhedge/alpha/vol_targeting.py`
Function : `vol_target_weights(signals, target_vol_annualized)`
Status : module ready, NOT yet wired in production

### 5.14 TC model (transaction cost)
Module : `src/pmhedge/alpha/tc_model.py`
Components : gas + half_spread + impact (Kyle sqrt) + adverse_selection
Defaults : gas $0.25, spread 150 bps, alpha_impact 0.10, adverse_fraction 0.10
Calibration : via `slippage_fills` (only 1 fill so far, static params)

### 5.15 MEV protection (skeleton)
Module : `src/pmhedge/execution/mev_protection.py`
Tiered : <$100 skip, $100-1k mev-blocker, >$1k Flashbots
Status : scaffolded, needs wallet

## 6. EXECUTION LAYER (most skeletons pre-wallet)

### 6.1 Almgren-Chriss optimal execution
Module : `src/pmhedge/execution/optimal_execution.py`
Functions : `optimal_trajectory`, `twap_schedule`, `pov_schedule`
Status : skeleton ready

### 6.2 VPIN toxic flow
Same module, `volume_bars + vpin()`
Threshold : VPIN > 0.3 → avoid posting

### 6.3 Microprice (Stoikov)
Same module, `microprice(best_bid, best_ask, bid_size, ask_size)`

### 6.4 Queue position + fill prob
Same module, `QueuePosition + prob_fill_by_horizon`

### 6.5 Market-making (weather thin markets only)
Module : `src/pmhedge/alpha/market_making.py`
Target markets : Seoul, Moscow, Lucknow, Taipei, Chongqing, Helsinki
Inventory mgmt + cancel-replace
Status : skeleton, needs py-clob-client

### 6.6 Fill probability logistic model
Script : `scripts/fill_probability.py`
Features : log_depth_over_size, log_spread_bps, hour_utc
Status : needs ≥50 real fills to train

### 6.7 Order manager + slippage EMA
Module : `src/pmhedge/execution/order_manager.py` (stub) + `alpha/slippage_model.py`

## 7. META LEARNING

### 7.1 Research log (append-only)
File : `research/hypotheses.jsonl`
Count : **19 hypothèses** loggées (12 closed : 4 CONFIRMED + 3 REJECTED + 1 PARTIAL + 4 ACTIVE ; 7 DEFERRED)
Wrapper : `scripts/log_hypothesis.py` (add/close/list/stats)

### 7.2 Model registry + MLflow
Table : `model_runs`
Module : `src/pmhedge/alpha/model_registry.py` + `mlflow_logger.py`
MLflow dir : `models/mlflow/`
Dual-write : model_runs SQLite + MLflow file-based

### 7.3 Champion/Challenger framework
Module : `src/pmhedge/alpha/champion_challenger.py`
Use : A/B test 2+ models, auto-promote winner

### 7.4 LLM feature extractor (Claude Haiku)
Module : `src/pmhedge/alpha/llm_features.py`
Model : `claude-haiku-4-5`
Output schema : extreme_event_flag, event_type, intensity_1to5, sentiment_hot, confidence_0to1, rationale
Cache : 1h TTL per (icao, target_date)
Status : **graceful fallback zero-vector without API key**. User action : `export ANTHROPIC_API_KEY=sk-ant-...`

### 7.5 Event ingest pipeline (NEW)
Module : `src/pmhedge/alpha/event_ingest.py`
Script : `scripts/ingest_event_alerts.py`
Function : `event_feature_for_market(icao, target_date)` → EventFeature
Status : **LIVE**, 63 active NWS alerts ingested
Cron : `event-alerts` toutes 30 min

## 8. GATE SCORECARD STATE

Last run : 10 PASS / 1 FAIL / 2 N/A

**10 PASS** : failure_modes (12), strategy_lifecycle, n_hypotheses (12), no_hard_leakage, shap_stability (tau=1), alpha_decay_edge_consistency (2/2 buckets), purged_kfold (1.17), dsr_prob_real (1.0), capacity_breakeven ($100k), factor_max_exposure (27%)

**1 FAIL** : economic_thesis_validated (user sentinel `THESIS VALIDATED` pending)

**2 N/A** : tc_model_calibrated (1 fill only), correlation_drift_ks_p (T=2 distinct days)

## 9. VALIDATED FEATURES (extended build_features list)

Default features in `xgboost_post.build_features(extended=True)` :
- Ensemble stats (6) : ens_mean, ens_std, ens_spread, ens_skew, ens_p05, ens_p75
- Obs lags (5) : t_current, t_today, t_yesterday, t_yday_minus_ens, t_today_minus_ens
- Temporal (3) : sin_doy, cos_doy, month
- Geo (4) : lat, lon, elevation, horizon_h
- Climato (4) : climo_mean_c, climo_std_c, anomaly_c, anomaly_z
- Lags (6) : t_lag_{1,3,7}d + anomalies
- Neighbours (2) : neighbour_0/1_ens_mean_c
- UHI (1) : uhi_offset_c
- Diurnal (8) : t_prev_{06,12,15,18}z + slopes + range + t_so_far
- Synoptic (4) : oni, nao, ao, pna
- Soil (3) : sm_0_7cm, sm_7_28cm, soil_aridity_z

**Total = 46 features actives**.

Features disabled by default (kept available via opt-in flags) :
- nwp_disagreement_c/ratio/pct (H0016 PARTIAL)
- is_monsoon_active, monsoon_doy_frac, monsoon_zone_id (H0013 REJECTED)
- elev_km, diurnal_amp_pred, altitude_class (H0014 REJECTED)
- pdo, dmi (H0015 PARTIAL)

## 10. HYPOTHESES LOG (19 entries)

| ID | Status | Hypothesis |
|---|---|---|
| H0001 | CONFIRMED | MODEL_VS_MARKET WR ≥ 88% on N=189 |
| H0002 | CONFIRMED | Per-city calibrator Brier -25% |
| H0003 | REJECTED | Quantile XGBoost improves Brier |
| H0004 | CONFIRMED | Tail filter preempts YES tail losses |
| H0005 | REJECTED | DRN improves ensemble CRPS |
| H0006 | ACTIVE | Regime HMM Kelly multipliers |
| H0007 | ACTIVE | Synoptic ONI/NAO/AO/PNA improve RMSE |
| H0008 | ACTIVE | Soil moisture improves summer forecasts |
| H0009 | ACTIVE | Diurnal intraday features |
| H0010 | PARTIAL | Per-city vol threshold — 2/26 fitted |
| H0011 | REJECTED | CONFIRMED_YES oracle (legacy bug) |
| H0012 | CONFIRMED | Chicago overestimation bias |
| H0013 | REJECTED | Monsoon rule-based features |
| H0014 | REJECTED | Altitude-coupled diurnal features |
| H0015 | PARTIAL | PDO + DMI teleconnections |
| H0016 | PARTIAL | NWP disagreement feature |
| H0017 | DEFERRED | Regime HMM 8 buckets (needs N≥500/bucket) |
| H0018 | DEFERRED | Per-station BMA × regime weights |
| H0019 | DEFERRED | Temporal Transformer (needs ERA5) |

## 11. KEY CONFIGS

### SignalGenConfig defaults (2026-04-20)
```python
min_edge            = 0.05
max_edge            = 0.40
edge_band_blocked   = (0.08, 0.15)   # NEW
kelly_fraction      = 0.40           # RAISED 0.25 → 0.40
size_cap_usdc       = 50.0
use_calibration     = True
use_volatility_filter = True
use_tail_filter     = True
use_regime_hmm      = True
# disabled by default
use_quantile        = False
use_drn             = False
include_nwp_disagreement = False
include_monsoon     = False
include_altitude    = False
```

### RiskConfig defaults (2026-04-20)
```python
max_pct_per_trade     = 0.05
max_pct_total         = 0.60
max_positions_per_city = 1
apply_correlation     = True
use_portfolio_kelly   = False        # opt-in
dd_bands_enabled      = True         # NEW
dd_band_caution_pct   = 0.03
dd_band_reduced_pct   = 0.05
dd_band_kill_pct      = 0.08
dd_band_breaker_pct   = 0.10
```

## 12. PAPER SESSION #1 EN COURS

```
session_id     : 1
status         : RUNNING
started_ts     : 2026-04-20 13:42 UTC
target_end_ts  : 2026-05-05 13:42 UTC
starting_br    : $1,000.00
current_br     : $1,000.00 (@ start)
```

Scripts :
- `scripts/paper_session_15d.py start|status|finalize`
- Cron daily 09:00 UTC : incremental report `vault/brantham/polymarket/paper-sessions/session-1-day-XX.md`
- Day 15 : `finalize` → comprehensive report `session-1-FINAL.md`

## 13. 41 LAUNCHD JOBS ACTIFS

```
live-runner (KeepAlive 300s)
nwp-ingest (4×/jour)                        calibrators-train (daily 04:15)
metar-archive (2h)                           city-calibrators (daily 04:20)
health-check (15min)                         vol-filter (daily 04:30)
circuit-breaker (15min)                      emos-train (Mon 04:45)
prom-exporter (KeepAlive)                    regime-train (Tue 04:45)
db-snapshot (03:00)                          regime-v2-train (Wed 04:45)
audit-prune (02:30)                          pair-corr (Wed 05:00)
synoptic-fetch (02:00)                       quantile-train (Thu 05:00)
soil-ingest (03:30)                          conformal (Thu 05:30)
bma-train (03:30)                            station-xgb (Fri 05:15)
xgb-retrain (weekly)                         hmm-train (Fri 05:30)
ensemble-train (Mon 04:30)                   bandit-allocator (05:45) NEW
reconcile-obs (09:10)                        decay-monitor (06:00 --apply) NEW
reconcile (09:15)                             city-audit (10:00)
calibration-report (09:30)                   city-kelly (10:10)
perf-metrics (09:30)                         drift-monitor (10:00)
mc-var (09:50)                                attribution (09:45)
validator (10:30)                             gate-scorecard (08:00)
perf-digest (08:15)                           paper-session (09:00) NEW
event-alerts (30min) NEW
precompute (every 6h)
```

## 14. VAULT DOCS INDEX

Master docs :
- `_MOC.md` — Map of Content
- `STATE-HANDOFF.md` — master state handoff
- `**MODEL-STATE-COMPLETE.md**` — CE DOC (zero-omission models)
- `CONTINUATION-PROMPT.md` — prompt next session
- `weather-domination-strategy.md` — philosophy 100% weather

G1→G2 Kit :
- `g1-g2-qualification-kit.md` + `g1-g2-todo-tracker.md`
- `gate-scorecard-spec.md`
- `economic-thesis.md` (DRAFT)
- `failure-modes.md` (12 modes)
- `strategy-lifecycle.md`

Research :
- `hedge-fund-rigor-upgrade.md`
- `feature-rejection-log.md`

Sessions (19) : `sessions/2026-04-19-*.md` + `sessions/2026-04-20-*.md`

## 15. CHECKS POUR REPRENDRE APRÈS CONTEXT CLEAR

```bash
cd /Users/paul/polymarket-hedge

# Compte launchd
launchctl list | grep polymarket-alpha | wc -l   # expected 41

# Validator
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/validate_strategy.py --skip-pytest

# Gate scorecard
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/gate_scorecard.py --gate G1

# Paper session status
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/paper_session_15d.py status

# Compound engine state
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/compound_status.py

# Bandit weights
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/bandit_allocator.py --lookback-days 30

# Decay monitor
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/alpha_decay_monitor.py

# Dashboard
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/dashboard_quant.py --once
```

## Related

- [[STATE-HANDOFF|State handoff complet]]
- [[CONTINUATION-PROMPT|Prompt next session]]
- [[weather-domination-strategy|Weather domination strategy]]
- [[g1-g2-qualification-kit|G1→G2 Kit]]
- [[_MOC|Polymarket Hub MOC]]
