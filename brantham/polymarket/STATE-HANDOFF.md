---
name: State Handoff — Polymarket Hedge Fund
description: Document de transmission complet — tout ce qu'il faut savoir pour reprendre la prochaine session sans perte de contexte
type: handoff
updated: 2026-04-20
priority: critical
tags: [polymarket, handoff, state, continuity]
---

# 📋 State Handoff — Polymarket Hedge Fund

**À LIRE EN PRIORITÉ dans toute nouvelle session.** Ce doc est à jour au 2026-04-20 après 3 sessions de refonte massive.

## TL;DR

**Status** : Pipeline alpha hedge-fund-grade avec 35 launchd jobs autonomes, 12 sources NWP (dont GraphCast/AIFS/NBM/UKMO/CMA), 37 features engineered, 46 per-station XGB, 11 per-city calibrators, 4 regime HMM, tail filter critique.

**Dernière session** : feature engineering massif (diurnal / synoptic / soil moisture) + MLflow + MC VaR + Pangu scaffold en attente du fichier ONNX.

**Initiative courante** : [[g1-g2-qualification-kit|G1→G2 Qualification Kit]] — 16 livrables structurés en 5 packages pour passer le signal de "research" à "paper shadow ready" avec validation statistique hedge-fund-grade. Voir [[g1-g2-todo-tracker|todo tracker]] pour l'état d'avancement.

**Score audit** : **~82/100** vs "hedge fund grade" générique, **~30/100** vs "énorme hedge fund" (Jane Street weather). Gap principal = **data privée + real money + équipe**, pas l'architecture.

**Bloquants user** :
1. ⏳ **Pangu-Weather ONNX** — user s'est engagé à fournir le fichier → drop à `models/pangu_24h.onnx`
2. ⏳ **Review [[economic-thesis]]** — thesis doc DRAFT, ajouter sentinel `THESIS VALIDATED` pour débloquer G1 exit
3. 🔴 **ERA5 via Copernicus** (account + `~/.cdsapirc`)
4. 🔴 **Polymarket wallet** + `POLY_PRIVATE_KEY` + `uv add py-clob-client`
5. 🟡 **Avocat crypto FR** avant $10k real

## Architecture en place

### Pipeline de décision d'un signal (ordre d'application)
```
1. TTR + volume + freshness gates
2. NWP forecast(icao, target_date) via forecast_cache 6h
3. EMOS per-station (506 buckets, CRPS médian 0.35°C)
4. BMA per-station (12 sources weighted, 152k samples training)
5. XGBoost station (46 models) OU region (10 models)
6. DRN ensemble (weight 0 tant que pas ERA5 — polluait)
7. Regime selector V1 (12 buckets) OU V2 (XGB continuous)
8. Ensemble mixture moment-matched → (μ, σ)
9. Tail filter (rejette YES "Above N" si > climo+2σ) ← 95/95 historic losses blocked
10. Isotonic calibration per-city (11 villes) → fallback global
11. Volatility filter city > zone > hard cap
12. Regime HMM Kelly multiplier (CALM ×1.0, TRANSITION ×0.8, STORMY ×0.4)
13. City config DISABLED/SHADOW/ENABLED + per-city Kelly fraction
```

### Modules alpha livrés (`src/pmhedge/alpha/`)
| Module | Rôle |
|---|---|
| `data_hub.py` | schema + connect + alpha_states kill-switch |
| `nwp_sources.py` | 12 sources (GraphCast/AIFS/NBM/UKMO/CMA/GEFS/ICON/ECMWF/JMA/HRRR/AROME/ICON_EU) |
| `emos.py` | Gneiting 2005 per-station × month |
| `bma.py` | Bayesian model averaging per station |
| `xgboost_post.py` | résiduel regional + per-station + feature extended flag |
| `feature_engineering.py` | 37 features (climato + lag + UHI + cross-station + **diurnal** + **synoptic** + **soil**) |
| `diurnal_features.py` | t_prev_{06,12,15,18}z + slopes + range + t_so_far |
| `synoptic_features.py` | ONI/NAO/AO/PNA teleconnections |
| `soil_moisture.py` | sm_0_7cm + sm_7_28cm + aridity_z |
| `calibration.py` | isotonic K-fold OOS global + per-city |
| `volatility_filter.py` | sigma threshold per (alpha, zone OR city) |
| `tail_filter.py` | reject YES tail bets > climo+2σ |
| `regime_hmm.py` | Gaussian HMM 3 states (CALM/TRANSITION/STORMY) |
| `regime_selector.py` + `regime_selector_v2.py` | ensemble weights par régime |
| `quantile_model.py` | LightGBM-style XGBoost quantile regression (DISABLED par défaut, hurt Brier) |
| `conformal.py` | split conformal shifts (marche avec quantile seulement) |
| `champion_challenger.py` | registry promote if better |
| `pair_arb.py` | cross-station stat-arb (5 signals so far) |
| `convex_arb.py` | same-station bracket non-monotonicities (opt-in) |
| `orderbook_imbalance.py` | microstructure (opt-in, books thin) |
| `kalshi_client.py` | cross-venue framework (bloqué user auth) |
| `risk_manager.py` | Kelly + circuit breaker hysteresis + cooldown |
| `city_config.py` | per-city status/kelly/size_cap |
| `audit.py` | audit_log + tax_lots FIFO |
| `model_registry.py` | model_runs table + mirror MLflow |
| `mlflow_logger.py` | wrapper graceful fallback |
| `gmm_forecast.py` | 2-component Gaussian mixture (dormant) |
| `pangu_forecaster.py` | **scaffold en attente du fichier ONNX user** |

### Launchd jobs (35 actifs)
```
live-runner (KeepAlive 300s) · nwp-ingest (4x/jour) · metar-archive (2h) · 
health-check (15min) · circuit-breaker (15min) · prom-exporter (KeepAlive) ·
db-snapshot (03:00) · audit-prune (02:30) · synoptic-fetch (02:00) ·
soil-ingest (03:30) · calibrators-train (04:15) · city-calibrators (04:20) ·
vol-filter (04:30) · emos-train (Mon 04:45) · regime-train (Tue 04:45) ·
regime-v2-train (Wed 04:45) · pair-corr (Wed 05:00) · quantile-train (Thu 05:00) ·
conformal (Thu 05:30) · station-xgb (Fri 05:15) · hmm-train (Fri 05:30) ·
ensemble-train (Mon 04:30) · bma-train (daily 03:30) · xgb-retrain (weekly) ·
precompute (every 6h) · reconcile-obs (09:10) · reconcile (09:15) ·
calibration-report (09:30) · perf-metrics (09:30) · drift-monitor (10:00) ·
city-audit (10:00) · city-kelly (10:10) · mc-var (09:50) · attribution (09:45) ·
validator (10:30)
```

## État des données

| Table | Count |
|---|---|
| `nwp_forecasts` | ~310 000 rows (12 sources × 46 stations × 1 an) |
| `nwp_ensemble_blend` | ~17k rows |
| `obs_temperature` | 510 000 rows (365j ARCHIVE + METAR + WU) |
| `signal_log` | 1 584 |
| `signal_outcomes` | **992 resolved** |
| `synoptic_indices` | 915 mois × 4 = 3 660 |
| `soil_moisture` | 60 rows (growing) |
| `emos_params` | 506 buckets |
| `bma_weights` | 47 stations × 12 sources |
| `city_config` | 26 (3 DISABLED, 2 SHADOW, 21 ENABLED) |
| `calibrators` (global) | 1 |
| `calibrators_city` | 11 |
| `volatility_thresholds` + `_city` | 2 + 2 |
| `ensemble_weights_regime` | 12 × 3 |
| `pair_correlations` (filtered meanΔ≤5°C) | 28 |
| `alpha_states` | toutes ENABLED sauf __CIRCUIT_BREAKER__ clean |
| `audit_log` | active avec retention 90j |
| `model_runs` | Optuna + training runs |

## Villes critiques

| Status | Villes | Raison |
|---|---|---|
| **DISABLED** | Tokyo (83, 0% WR), Chicago (41, 34%), NYC (22, CI<30%) | losers confirmés |
| **SHADOW** (×0.2 size) | Dallas (77, 77%), Miami (61, mixed) | marginaux |
| **Kelly 0.50** | atlanta, austin, beijing, denver, houston, KL, lucknow, LA, paris, SF, shenzhen, tel aviv, HK, mexico city | validated winners |
| **Kelly 0.25** (N<10) | ankara, helsinki, chongqing, taipei, seoul, madrid, moscow | exploration |

## Dernières findings critiques

### 1. Ablation révèle que quantile + conformal HURT
- Gaussian + calibration per-city: Brier **0.0815** (best)
- Full stack quantile+conformal: Brier 0.1010 (worse 24%)
- **Défaut actuel** : `use_calibration=True`, `use_quantile=False`, `use_volatility_filter=True`

### 2. Tail filter bloque Tokyo/NYC pattern
- 80 signaux Tokyo "Above 26°C" avril (climato 16°C) : 0 wins — YES tails over-estimate
- `pmhedge.alpha.tail_filter.is_tail_bet()` rejette `YES` avec `bracket_lo > climo + 2·std`
- Empirical 95/95 losses preempted

### 3. DRN pollue l'ensemble tant que pas ERA5
- Val CRPS DRN 1.22 vs BMA 0.48, XGB 0.40
- `DRN_DISABLED_UNTIL_ERA5 = True` dans `train_ensemble_weights.py` et `train_regime_selector.py`
- Weight = 0 dans `ensemble_weights` et `ensemble_weights_regime`

### 4. Chicago drop 100% → 34% sur N=11 → N=41
- Overfit small-sample classique
- Per-city calibrator absorbed: Brier 0.51 → 0.05 après fit

## Commandes essentielles

### Sanity checks reprise session
```bash
cd /Users/paul/polymarket-hedge

# 1. Launchd OK ? (35 jobs attendus)
launchctl list | grep polymarket-alpha | wc -l

# 2. Validator 8/8 ?
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/validate_strategy.py --skip-pytest

# 3. Data freshness
sqlite3 alpha_data_hub.db "SELECT source, status, datetime(last_success,'unixepoch','localtime') FROM data_freshness;"

# 4. Circuit breaker
sqlite3 alpha_data_hub.db "SELECT alpha_type, status, reason FROM alpha_states;"

# 5. Outcomes recent count
sqlite3 alpha_data_hub.db "SELECT date(emit_ts,'unixepoch') AS d, COUNT(*) FROM signal_log GROUP BY d ORDER BY d DESC LIMIT 5;"

# 6. Logs live runner
tail -30 /Users/paul/polymarket-hedge/logs/alpha-live.log

# 7. Test live scan
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/run_alpha_live.py --once --no-telegram --min-edge 0.05 --bankroll 1000
```

### Entraînement complet (après changement de features)
```bash
# Dans l'ordre :
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_emos_per_station.py
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_bma.py --days 365
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_xgb_per_station.py
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_xgboost_post.py --obs-source ARCHIVE
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_calibrators.py
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_city_calibrators.py
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_regime_hmm.py
uv run scripts/audit_per_city.py --apply --quiet
uv run scripts/compute_city_kelly.py
```

### Ablation study
```bash
# Global (N=400 outcomes sampled)
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/ablation_study.py --max-rows 400
# Per-city
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/ablation_study.py --per-city --window 30
```

## Ce qui attend

### 🎯 Priorité immédiate prochaine session
1. **Drop Pangu ONNX** à `models/pangu_24h.onnx` → 5 min wire via scaffold en place
2. Re-run ablation post-Pangu pour voir +15% CRPS attendu
3. Backfill Pangu sur 1 an pour enrichir BMA weights

### Non attaqués (faisables solo)
- **Transformer temporel MPS** (5-10h training sur 1 an)
- **Aurora Microsoft ONNX** (1 jour integration)
- **Walk-forward strict** (déjà covered par signal_outcomes par construction)
- **CI/CD GitHub Actions** (3h)
- **Postgres migration** (SQLite ~30 MB OK pour l'instant)
- **Docker compose full** (4h)

### Bloqués attente temps réel
- **Sharpe live crédible** : besoin de 20+ jours distincts de P&L (actuellement 2 jours)
- **VaR Monte Carlo** : idem, dormant jusqu'à N≥5 days distincts
- **Champion/Challenger shadow 10%** : attendre que challenger soit enregistré

### Bloqués user
- ERA5 Copernicus → débloque DRN SOTA + vraie ground truth
- Wallet Polymarket + `py-clob-client` → real money 
- Avocat crypto FR → compliance > $10k
- Pangu ONNX file (user a promis)

### Hors scope solo
- Mesonet US dense ($500/mo Synoptic)
- GOES-18 / Himawari / Meteosat direct (500 GB+)
- MRMS radar NEXRAD
- Colocation AWS us-east-1 ($200/mo)
- GPU Hetzner GEX44 (€200/mo)
- Private feeds Vaisala ($50k/an)
- Équipe 5-20 quants PhD

## Sessions associées

- [[sessions/2026-04-19-hedge-fund-grade-upgrades|Session 1 — architecture hedge fund]]
- [[sessions/2026-04-19-critical-review-and-fixes|Session 2 — critical review 52/100 → 65/100]]
- [[sessions/2026-04-19-per-city-optimization|Session 3 — diagnostic Tokyo/Chicago per-ville]]
- [[sessions/2026-04-19-backfill-scale-up|Session 4 — backfill 1 an + 46 per-station XGB]]
- [[sessions/2026-04-19-ml-sota-integration|Session 5 — GraphCast/AIFS/NBM/UKMO/CMA via Open-Meteo]]
- [[sessions/2026-04-19-overnight-model-upgrades|Session overnight]]

## Related

- [[_MOC|Polymarket Hub MOC]]
- [[audit-hedge-fund-grade|Audit détaillé gaps]]
- [[architecture|Architecture classique 4 couches]]
- [[deep-learning-roadmap|Deep Learning roadmap]]
- [[TODO-pending|TODO priorisé]]
- [[decisions|Décisions archi]]
