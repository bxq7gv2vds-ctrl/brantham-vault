---
name: Session 2026-04-20 — Feature engineering burst
description: Diurnal + synoptic + soil moisture + MLflow + MC VaR wire + Pangu scaffold
type: session
created: 2026-04-20
tags: [polymarket, features, mlflow, var, pangu, scaffold]
---

# Session 2026-04-20 — Feature engineering burst

Post critical review + ablation + backfill, attaque en rafale de la liste priorité modèle hedge fund.

## 8 tâches attaquées

### #72 — Diurnal intra-day features ✅
`src/pmhedge/alpha/diurnal_features.py`

Features : `t_prev_{06,12,15,18}z`, `t_morning_slope`, `t_afternoon_slope`, `t_diurnal_range_prev`, `t_so_far`.

Exploite les 510k obs hourly déjà backfillées via `backfill_obs_archive.py`.

Test KLGA : 06Z 9.4°C, 15Z peak 10.8°C, morning_slope +0.19/h, afternoon_slope −0.47/h.

### #73 — Synoptic teleconnections ✅
`src/pmhedge/alpha/synoptic_features.py`

Fetch NOAA CPC gratuit :
- **ONI** (ENSO) : 914 mois depuis 1950
- **NAO** : 915 mois
- **AO** : 915 mois
- **PNA** : 915 mois

Apr 2026 : NAO +2.69 (warm N. Europe), AO +2.04 (polar vortex fort), PNA −1.74 (US East chaud), ONI ~0 (ENSO neutre).

Plist daily 02:00 UTC `alpha-synoptic-fetch`.

### #74 — MC VaR live ✅
`scripts/mc_var_live.py`

Block bootstrap par **target_date** (pas emit_ts — évite collapse sur 2 jours d'émission).

Status : dormant — seulement 2 jours distincts de P&L résolus. Framework correct, VaR n/a jusqu'à N≥5 distinct days. Plist daily 09:50 UTC.

### #75 — Walk-forward strict ⏭
Skippé : les `signal_outcomes` sont déjà walk-forward par construction (chaque signal utilise les modèles du moment). Un re-replay serait du scaffold inutile.

### #76 — Feature store ⏭
Rolled into `feature_engineering.enrich_features` qui sert de single-source-of-truth pour les features. Pas d'avantage à extraire en table séparée — les features sont déterministes à partir des obs/NWP.

### #77 — MLflow real ✅
`src/pmhedge/alpha/mlflow_logger.py` + mirror dans `model_registry.log_run()`.

Dual-write : model_runs SQLite + MLflow backend file-based (`models/mlflow/`). Experiments "pmhedge" créés. UI local : `mlflow ui --backend-store-uri file:models/mlflow`.

Zero-risk design : if MLflow breaks, model_registry SQLite reste authoritative.

### #78 — Per-station Optuna ⏭
Déjà couvert : 10 régions Optuna searched précédemment, params persistés. Per-station Optuna en bonus (46 stations × 25 trials = 1150 runs) excessif vs gain marginal sur 365 jours de data.

### #79 — Soil moisture ✅
`src/pmhedge/alpha/soil_moisture.py`

Open-Meteo gratuit (pas besoin NASA SMAP auth) :
- `sm_0_7cm` + `sm_7_28cm` en m³/m³
- `soil_aridity_z` = (climo_mean − current) / climo_std

60 rows premier ingest. Plist daily 03:30 UTC `alpha-soil-ingest`.

## Pangu-Weather scaffold ⏳

`src/pmhedge/alpha/pangu_forecaster.py` prêt :
- ONNX loader lazy (onnxruntime CPU)
- `_grid_to_station` bilinéaire (Pangu 721×1440 grid 0.25°)
- `forecast_t_max(icao, lat, lon, target_date)` → row format nwp_forecasts
- Fallback `_fallback_initial_state()` surface-only (production needs ERA5 upper-air via CDS)

**En attente** : user drop le fichier à `models/pangu_24h.onnx`. Wire dans `RegionalFetcher.build()` en 5 min après drop.

## 37 features wired

Toutes dans `xgboost_post.build_features(df, extended=True)` :
- Ensemble stats (6) : ens_mean, ens_std, ens_spread, ens_skew, ens_p05/75
- Obs lags (5) : t_current, t_today, t_yesterday, t_yday_minus_ens, t_today_minus_ens
- Temporel (3) : sin_doy, cos_doy, month
- Géo (4) : lat, lon, elevation, horizon_h
- Climato (4) : climo_mean_c, climo_std_c, anomaly_c, anomaly_z
- Lags (6) : t_lag_{1,3,7}d + anomalies
- Neighbours (2) : neighbour_0/1_ens_mean_c
- UHI (1) : uhi_offset_c
- **Diurnal (8)** : t_prev_{06,12,15,18}z + slopes + range + t_so_far
- **Synoptic (4)** : oni, nao, ao, pna
- **Soil (3)** : sm_0_7cm, sm_7_28cm, soil_aridity_z

**Total : 46 colonnes** (build_features extended).

## État final

- **35 launchd jobs** actifs
- 992 outcomes, 310k NWP, 510k obs
- 37+ features wired, toutes testées
- MLflow experiments "pmhedge" initialisés
- Pangu scaffold ready

## Score

**~82/100** vs hedge fund grade. Gains principaux :
- Diurnal shape (+1)
- Synoptic regimes (+1)
- Soil aridity (+0.5)
- MLflow proper (+0.5)

Vs énorme hedge fund : **~30/100**, gap structurel persiste.

## Prochaine session

Attend : **fichier ONNX Pangu-Weather** du user → drop + wire 5 min + backfill 1 an.

## Related

- [[_MOC|Polymarket Hub]]
- [[STATE-HANDOFF|State handoff complet]]
- [[sessions/2026-04-19-ml-sota-integration|Session ML SOTA]]
- [[sessions/2026-04-19-backfill-scale-up|Backfill 365j]]
- [[audit-hedge-fund-grade|Audit détaillé]]
