---
name: Session 2026-04-19 — ML SOTA via Open-Meteo
description: Intégration GraphCast + NBM + UKMO + CMA + AROME en une heure via Open-Meteo API (au lieu de 6h+ d'ONNX download/integration)
type: session
created: 2026-04-19
tags: [polymarket, graphcast, aifs, nbm, ml-sota, nwp]
---

# Session 2026-04-19 — ML SOTA via Open-Meteo

## La trouvaille

J'étais parti pour passer 4-6h à télécharger Pangu-Weather ONNX (1.1 GB) + coder un wrapper CPU + gérer l'ERA5 initial state. Avant de plonger, test API Open-Meteo :

```
curl "https://api.open-meteo.com/v1/forecast?models=gfs_graphcast025..."
→ retourne des données !
```

**Open-Meteo expose les modèles ML SOTA en API gratuite :**
- `gfs_graphcast025` — **Google DeepMind GraphCast** (Nature 2023)
- `ecmwf_aifs025_single` — ECMWF AIFS (déjà intégré avant)
- `ncep_nbm_conus` — NCEP National Blend of Models (top US)
- `ukmo_seamless` — UK Met Office seamless
- `cma_grapes_global` — China GRAPES
- `meteofrance_seamless` — Meteo-France AROME

Aucun ONNX download, aucun compute local, aucun ERA5 initial state. API HTTP classique.

## Ce qui a été fait

### `nwp_sources.py` étendu
- Helper générique `_fetch_single_model(model_api_name, source_tag, …)` factorise l'accès.
- 4 fetchers ajoutés : `fetch_graphcast`, `fetch_nbm`, `fetch_ukmo`, `fetch_cma`, `fetch_meteofrance`.
- `RegionalFetcher.build()` route par zone :
  - **US** : + NBM
  - **Europe** : + UKMO + AROME
  - **Asia** : + CMA
  - **Toutes** : + AIFS + GraphCast

### Coverage par station vérifiée
| Station | Avant | Après |
|---|---|---|
| KLGA (NYC) | 5 sources | **8** (+ GRAPHCAST, NBM, AIFS) |
| RJTT (Tokyo) | 5 | **7** (+ GRAPHCAST, CMA) |
| LFPG (Paris) | 5 | **9** (+ GRAPHCAST, UKMO, AROME, AIFS) |

### Historical backfill 365 jours avec 11 modèles
- `scripts/backfill_nwp_history.py` étendu avec nouveaux models
- **146 299 nouveaux nwp_forecasts** backfillés en 14.5 s (4 errors marginaux)
- Nouvelles sources persistées :
  - GRAPHCAST : 15 530 rows sur 46 stations
  - UKMO : 15 410 rows sur 43
  - AROME : 15 410
  - CMA : 14 290 sur 43
  - AIFS : 16 319 (élargi de 947 à 16 319)
  - NBM : 4 742 sur 14 stations US

### Retrain BMA sur 152 421 samples (vs 72 301 avant)

**Global MAE rankings avec nouvelles sources** :

| Source | MAE (°C) | N | Share weight |
|---|---|---|---|
| **ECMWF** | **0.82** | 16 790 | 9.4% |
| **NBM** | **0.90** | 4 681 | 8.6% |
| HRRR | 0.97 | 28 | 8.0% |
| ICON | 1.02 | 16 790 | 7.6% |
| **UKMO** | **1.08** | 15 331 | 7.1% |
| GEFS | 1.10 | 16 790 | 7.0% |
| AIFS | 1.11 | 15 338 | 6.9% |
| AROME | 1.12 | 15 331 | 6.9% |
| **GRAPHCAST** | **1.26** | 15 334 | 6.2% |
| ICON_ENS | 1.27 | 138 | 6.1% |
| JMA | 1.47 | 16 790 | 5.3% |
| GEFS_ENS | 1.57 | 138 | 4.9% |
| CMA | 1.65 | 14 197 | 4.7% |

**Insights** :
- ECMWF reste king, NBM deuxième (excellent US blend)
- GRAPHCAST marginal sur MAE mais **diversité utile** (different architecture, different errors)
- AIFS + GRAPHCAST combinés = **2 sources ML**, weights cumulés 13.1 %
- CMA le plus faible (donnée limitée / coarse grid) mais utile Asie

### BMA per-station — NYC KLGA
ICON_ENS 0.17, ECMWF 0.15, GEFS_ENS 0.13, JMA 0.11, UKMO 0.11, NBM 0.11, GEFS 0.11, ICON 0.10, AROME 0.10, GRAPHCAST 0.09, CMA 0.07, AIFS 0.05

### Retrain downstream
- **EMOS** per-station : 506 buckets (stable, plus de NWP data)
- **XGB per-station** : 46 models refit (RMSE 0.41-2.56 range)
- **Calibrators per-city** : 11 persistés (Brier gains massifs)
- **Calibrator global** : Brier 0.057→0.038 OOS

## Verdict vs l'approche Pangu-Weather ONNX

| Métrique | Pangu ONNX route | Open-Meteo route (choisie) |
|---|---|---|
| Effort | 4-6 h + bloqué ERA5 | **30 min** |
| Download | 1.1 GB | 0 |
| Dependency | onnxruntime | stdlib HTTP |
| Modèles ML obtenus | 1 (Pangu) | **2 (GraphCast + AIFS)** |
| Bonus modèles classiques | 0 | **4 (NBM, UKMO, CMA, AROME)** |
| Coverage stations | Global mais requires init state | Free, instant, per-station |

**Meilleure décision de la session** : vérifier l'API avant de plonger sur la route dure.

## État final

- **30 launchd jobs** actifs
- **992 outcomes**, 311k+ NWP forecasts, 510k obs
- **12 NWP sources** dans BMA (vs 8 avant)
- **152k samples** training BMA (2× plus)
- **46 per-station XGB** + **506 EMOS buckets** + **11 per-city calibrators**
- 4 **regime HMM** (CALM/TRANSITION/STORMY)
- 10 **Optuna-tuned** régions
- 1 **tail filter** (bloque Tokyo/NYC tail over-estimates)
- 1 **regime Kelly multiplier** (×0.4 STORMY, ×0.8 TRANSITION)
- **SHAP** confirme features engineered (t_lag, neighbour, anomaly) portent
- **Strategy validator** 12/12 tests + 9 invariants daily
- **Audit prune** cron daily

## Score audit

**78 → 82/100** dans notre référentiel "hedge fund grade".

Vs. "énorme hedge fund directional + MM" : **~30/100**. On gagne 5 points grâce à GraphCast / AIFS intégrés (le ML SOTA sans compute), mais l'écart structurel persiste :
- Pas de real money live track record
- Pas d'équipe / SRE 24/7
- Pas de Mesonet / satellite / radar privé
- Pas de colocation / FPGA

## Ce qui reste (honnête)

### Faisable solo, non attaqué
- Diurnal intra-day features (refactor METAR archive)
- Wire Pangu-Weather ONNX direct (si un jour ERA5 disponible)
- Transformer temporel MPS (5-10h)

### Bloqué user
- ERA5 Copernicus
- Polymarket wallet + py-clob-client
- Avocat crypto FR
- Budget GPU €200/mo

### Hors scope solo
- Mesonet $500/mo
- Colocation AWS
- Équipe PhD quants

## Related

- [[_MOC|Polymarket Hub]]
- [[sessions/2026-04-19-backfill-scale-up|Session scale-up]]
- [[sessions/2026-04-19-per-city-optimization|Session per-city]]
- [[sessions/2026-04-19-critical-review-and-fixes|Critical review]]
- [[STATE-HANDOFF|State handoff]]
