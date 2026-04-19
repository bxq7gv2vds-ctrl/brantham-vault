---
name: Session 2026-04-19 — Per-city Model Optimization
description: Diagnostic Tokyo/Chicago + refit complet avec N=992 + ablation per-city + tail filter
type: session
created: 2026-04-19
tags: [polymarket, per-city, model-tuning, ablation, root-cause]
---

# Session 2026-04-19 — Optimisation par ville

Après le critical review, attaque du modèle par ville : diagnostic des losers, refit avec le nouveau dataset, feature engineering UHI.

## Root causes trouvés

### Tokyo 0 % WR sur N=83 → −$979
Cause : **100 % des signaux étaient des YES "Above 26 °C"** pariés à 5 cts avec est_prob=0.18.
- Climatology Tokyo avril : mean 16.1 °C, σ 3.5 °C
- Climo + 2σ = 23.1 °C ; bracket_lo = 26 °C = **tail**
- Model Gaussian+BMA gonfle σ de variance → P(T≥26 °C) = 18 % vs réalité 0/80

**Fix** : `pmhedge.alpha.tail_filter` — rejette les YES où bracket_lo > climo_mean + 2σ + est_prob ≥ 0.10.
- Filtre aussi NYC (ancien 15/15 pertes tail) et toute future station avec pattern similaire.
- Déployé dans signal_generator, ON par défaut.

### Chicago 34 % WR sur N=41 → −$275
Pattern différent : 40 signaux NO à 0.73 prix, est_prob=0.91.
- Bracket_lo=11.7 °C, climo Chicago avril mean=11.5, σ=6.9
- Bracket proche de la moyenne, **pas tail**
- Model dit "91 % below 12 °C", réalité 33 % → modèle under-estime σ
- Pas de fix simple — le calibrator per-city Chicago persisté apprend à corriger ce biais (Brier 0.51 → 0.05).

### Chicago drop 100 % → 34 % avec plus de data
Ancien audit N=11 (100 %) était un **overfit small-sample** classique. N=41 révèle la vérité. Recommandation city_audit l'a auto-DISABLED.

## Refit complet avec N=992

Après backfill (217 → 992 outcomes) :

| Model | Before | After |
|---|---|---|
| EMOS per-station | 106 buckets | 106 buckets (stable) |
| BMA | 47 stations, MAE 1.24°C (GEFS best) | 47 stations retrained sur 6 212 obs |
| XGBoost per-station | 6 stations asiatiques | idem, RMSE 0.75-1.99 °C |
| **Calibrator global** | Brier 0.016→0.010 ECE 0.027→0.010 (N=189) | **Brier 0.057→0.038 ECE 0.087→0.007 (N=906)** |
| **Calibrator per-city** | 1 ville (KL) | **11 villes** — gains massifs ex. Tokyo 0.034→0.0001 |
| Volatility thresholds | 1 zone | 1 zone + 2 villes (Beijing, Miami) |
| Pair correlations | 53 pairs (18 useful) | 53 pairs (stable) |

## Ablation re-run avec N=300 outcomes

**Ordre de performance (Brier, lower=better)** :

| Config | Brier | Verdict |
|---|---|---|
| no_quantile (Gaussian + calibration) | **0.0815** | **BEST** |
| no_conformal (quantile sans shift) | 0.0935 | |
| full_stack | 0.1010 | |
| no_calibration | 0.1052 | |
| gaussian_baseline | 0.1056 | worst |

**Conclusions** :
1. **Calibration per-city est enfin NET POSITIVE** (+23 % vs Gaussian seul) — grâce aux 11 grids per-city sur data plus grande.
2. **Quantile regression reste NÉGATIVE** — overfit malgré le refit, à retirer jusqu'à 3 000+ outcomes.
3. **Conformal shifts** margin-négatifs — pareil.
4. Ensemble XGB post-proc neutre — le signal passe d'abord par EMOS+BMA qui capture déjà le gros.

**Action** : `use_calibration=True` par défaut, `use_quantile=False` opt-in.

## Per-city ablation (15 villes avec N≥20)

**Best config per city** :

| Best config | Cities | Note |
|---|---|---|
| Gaussian only | Austin, Chicago, HK, KL, Lucknow, Miami (6) | données propres, calibration overfit |
| Gaussian + Cal | Atlanta, Denver, Houston, LA, Tokyo (5) | **villes avec bias systémique corrigé** |
| Full stack | Dallas, SF, Shenzhen (3) | configurations mixtes |
| no_calib | Beijing (1) | calibration y fait perdre |

**Insight** : la moyenne (Gaussian + Cal) domine mais il y a de la variance inter-ville. Ouvre la voie pour **per-city layer config** (prochaine itération — nécessite plus de data).

## Nouvelle UHI feature

`feature_engineering.add_uhi_feature` : offset de chaque station vs moyenne des stations dans sa bande de latitude ±2 °.
- KDEN : −17.7 °C (altitude 1 500 m)
- Captures urban heat island, altitude, continental vs maritime.
- Ajoutée dans `build_features(extended=True)` — next XGB retrain capturera.

## État live

**Live scan après toutes les couches** :
- 5 signaux émis (vs 11 pré-diagnostic)
- Tokyo / NYC / Chicago **DISABLED** par city_config (audit auto)
- Brackets "Above N" type tail filtrés par tail_filter
- Edges plus honnêtes (0.09-0.29), sans boost calibration artificiel
- Tail filter bloque 95/95 signaux perdants historiques

## Ce qui reste bloqué pour aller plus loin

1. **NWP historical backfill Western** — Open-Meteo `previous-runs-api` existe mais nécessite rate-limited calls et storage ~50 MB. Débloquerait per-station XGB sur 30+ villes (actuellement 6).

2. **Diurnal curve features** — METAR hourly obs nécessaires. Le script `archive_metar.py` existe mais ne stocke pas intraday courbe continue. Refactor de 2-4h.

3. **ERA5 via Copernicus CDS** (bloqué user) — débloquerait vraie DRN + ground truth propre.

4. **Per-city layer config** — stocker le "best config" par ville dans city_config, lire à l'inférence. Nécessite 5 k+ outcomes pour être solid.

5. **Bracket-aware direct training** — fit XGBoost classification directement sur P(T ∈ bracket) vs recompute from μ/σ. Stalled par manque de variety de brackets historiques.

## Score audit actuel

**65 → 72/100** (tail filter +2, refit complet +3, UHI +1, per-city insight +1).

Ce qui bloque le score plus haut :
- N=992 toujours en dessous des 5 000 idéal
- Pas de real money test
- Western stations bloquées à 95 j NWP
- Toujours pas de foundation model (Pangu/GraphCast/Aurora)

## Related

- [[_MOC|Polymarket Hub]]
- [[sessions/2026-04-19-hedge-fund-grade-upgrades|Session matin — architecture]]
- [[sessions/2026-04-19-critical-review-and-fixes|Session soir — critical review]]
- [[reports/ablation-2026-04-19|Ablation full stack]]
- [[reports/ablation-per-city-2026-04-19|Ablation per-city]]
- [[STATE-HANDOFF|State handoff]]
