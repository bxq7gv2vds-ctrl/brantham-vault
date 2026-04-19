---
name: Session 2026-04-19 — Backfill + Scale-up per-station
description: NWP+obs backfill 1 an → EMOS 106→506 buckets, XGB 6→46 stations, Optuna 10 régions
type: session
created: 2026-04-19
tags: [polymarket, backfill, per-station, scale-up, xgboost, optuna]
---

# Session 2026-04-19 — Backfill & scale-up par station

Débloque les Western stations bloquées à 91 jours pour fit per-station XGB partout.

## Backfill 1 an

### NWP historical forecasts
Open-Meteo `historical-forecast-api` — fetch 5 modèles (GEFS/ICON/ICON_EU/ECMWF/JMA) pour 46 stations × 365 jours.

- **Before** : 46 stations, 6 à 368 jours NWP
- **After** : 46 stations, **370 jours chacune**
- Inserted : **72 102 nwp_forecasts + 16 836 blends** en 6.7 s

### Obs historical
Open-Meteo `archive-api` — ERA5-derived hourly T pour 1 an.
- **Inserted** : **404 064 obs rows** en 1.9 s
- 46 stations × ~365 jours × ~24 heures

## Retrain massif

### EMOS per-station
- **Before** : 106 buckets (stations asiatiques + quelques US)
- **After** : **506 buckets** (toutes les stations × mois qui ont ≥30 obs)
- CRPS médian : **0.43 → 0.35 °C** (−18%)
- 46 stations skippées (obs insuffisantes pour certains mois spécifiques)

### BMA weights
- **Before** : 47 stations, 6 212 samples training
- **After** : 47 stations, **72 301 samples** (+11× data)
- Top predictor : JMA (share 8.1%, MAE 1.47°C)

### Per-station XGBoost
- **Before** : 6 stations (toutes asiatiques, N≥200)
- **After** : **46 stations** (100% coverage)

**RMSE par station** (sample) :
| Station | RMSE °C | Notes |
|---|---|---|
| KPHX Phoenix | 0.36 | Meilleur — désertique, prévisible |
| EPWA Warsaw | 0.47 | Bon — plaines européennes |
| LTAC Ankara | 0.49 | |
| EGLC London | 0.52 | |
| VHHH Hong Kong | 0.52 | |
| KMIA Miami | 0.55 | |
| WMKK KL | 0.59 | Équatorial stable |
| KATL Atlanta | 0.65 | |
| LFPG Paris | 0.68 | |
| KORD Chicago | 0.86 | Variable continental |
| KDEN Denver | 0.85 | Altitude |
| KLGA NYC | 1.08 | Urban |
| KLAX LA | 1.17 | Coastal marine layer |
| KSFO San Francisco | 1.82 | Brouillard microclimat |
| RKSI Seoul | 2.56 | Pire — montagneux bordure mer |

## Optuna search per région

10 régions XGBoost post-proc, 25 trials TPE chacune, CV 4-fold time-series.
- All regions persisted dans `model_runs`
- Best params variables (max_depth 3-8, eta 0.02-0.15, n_rounds 100-600)
- À wire dans le prochain `train_xgboost_post.py --use-optuna` (TODO)

## Re-run ablation N=400

Avec la nouvelle architecture :

| Config | Brier | Verdict |
|---|---|---|
| **no_quantile** (Gauss + Cal) | **0.0905** | **BEST** |
| no_conformal | 0.1119 | |
| gaussian_baseline | 0.1115 | |
| full_stack | 0.1165 | |
| no_calibration | 0.1237 | worst |

**Conclusions stables** :
- Calibration per-city reste NET POSITIVE (+22 % vs Gaussian)
- Quantile reste TOXIQUE (+7% Brier)
- Ensemble XGB post-proc neutre (identical with/without)

## Live scan après scale-up

Après tous les changements, les signaux convergent vers quelques trades à très haut signal :
- **1 signal par scan** (MODEL_VS_MARKET + PAIR_ARB combinés)
- Edges 0.09-0.30
- Tail filter bloque 95/95 historiques perdants
- 3 villes DISABLED (Tokyo, Chicago, NYC)
- 46/46 stations ont leur model XGB per-station

## Ce qui reste à faire

### Skippé cette session (lourd)
- **Pangu-Weather ONNX** (1.1 GB download, onnxruntime integration 2-3h)
- **Diurnal curve features** (nécessite METAR intraday refactor)
- **Transformer temporel** (5-10h MPS training)

### Bloqué utilisateur
- ERA5 via Copernicus (DRN propre)
- Polymarket wallet ($500 test)
- `py-clob-client` (real orders)
- Avocat crypto FR avant $10k real

## État final de l'infra

| Métrique | Valeur |
|---|---|
| Outcomes résolus | 992 |
| NWP forecasts | 165k (2× avant backfill) |
| Obs rows | 510k (5× avant) |
| EMOS buckets | 506 |
| Per-station XGB | 46 |
| Per-city calibrators | 11 |
| Launchd jobs | 30 |
| City config: ENABLED / SHADOW / DISABLED | 21 / 2 / 3 |

## Score audit réactualisé

**72 → 78/100**. Gains :
- Backfill coverage 100 % (+3)
- Per-station XGB 46 vs 6 (+2)
- EMOS 5× plus de buckets (+1)
- Optuna search fait (+1)

Ce qui bloque encore :
- Ablation sur N=400 reste dans régime "noisy" (pas 5 000+)
- Pas de Pangu / foundation model (−5 vs énorme hedge fund)
- Pas de real money (−10 vs real fund)
- 1 dev, 1 Mac (−10 vs équipe+cluster)

## Related

- [[_MOC|Polymarket Hub]]
- [[sessions/2026-04-19-per-city-optimization|Session précédente — diagnostic Tokyo/Chicago]]
- [[reports/ablation-2026-04-19|Ablation study]]
- [[STATE-HANDOFF|State handoff]]
