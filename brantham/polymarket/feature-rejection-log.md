---
name: Feature Rejection Log — empirical findings
description: Décisions d'activer / désactiver des features et de report des upgrades modèle, basées sur validation empirique walk-forward. Discipline hedge-fund-grade pour contrôler le data-mining bias et protéger le DSR.
type: findings
created: 2026-04-20
updated: 2026-04-20
priority: critical
tags: [polymarket, features, validation, hedge-fund, data-discipline]
---

# Feature Rejection Log — empirical findings 2026-04-20

Chaque feature ajoutée au modèle doit passer un test de validation
walk-forward strict **avant** d'être activée en default. Sans cela, on
inflationne le data-mining bias (augmente `N_trials` dans le DSR) et on
introduit du bruit qui dégrade la robustesse out-of-sample.

Ce log documente **ce qui n'a pas passé le test** et pourquoi on ne
l'active pas par défaut — discipline essentielle pour rester hedge-fund-grade.

## Méthodologie de validation (référence)

Utilisée par `scripts/validate_feature_impact.py` :

1. **Walk-forward 5-fold** : data time-sorted, chaque test fold est strictly future.
2. **Ablation** : baseline (feature OFF) vs complete (feature ON) sur même pipeline XGB.
3. **Paired bootstrap CI95** sur les diffs de RMSE OOS.
4. **Critère de retenue** : CI95 strictement > 0 (= mean_Δ significativement positif).
5. **Per-station + aggregate** pour détecter les effets hétérogènes.

## Features testées 2026-04-20

Toutes testées sur N=367 obs × 4-6 stations ciblées selon la feature.

| Feature | Stations | Mean Δ RMSE (°C) | CI95 | Status | Hypothesis ID |
|---|---|---|---|---|---|
| altitude (elev_km, diurnal_amp_pred, altitude_class) | MMMX, KDEN, LEMD, LTAC | -0.0006 | [-0.0016, +0.0005] | **REJECTED** | [[research/hypotheses-jsonl\|H0014]] |
| monsoon (is_active, doy_frac, zone_id) v1 rule-based | VHHH, WMKK, VILK, WIII, RJTT, RKSI | -0.0020 | [-0.0053, +0.0010] | **REJECTED** | H0013 |
| pdo + dmi teleconnections | KSFO, KLAX, KSEA, RJTT, VHHH, VILK | +0.0024 | [-0.0019, +0.0070] | **PARTIAL** | H0015 |
| nwp_disagreement (c, ratio, pct) | MMMX, KDEN, VHHH, KLAX, LFPG, RJTT | -0.0020 | [-0.0106, +0.0078] | **PARTIAL** | H0016 |

### Interprétation

**Toutes inconcluantes** sur cette data. Causes probables :

1. **Sample size limité** : 367 obs par station × 1 année calendaire.
   Pour capturer des régimes décennaux (PDO, IOD), il faut 10+ ans.
   Pour capturer 3+ cycles mousson, il faut 3+ ans.

2. **Information redondante** : XGBoost peut déjà capturer altitude via
   climatology + UHI implicitement ; ajouter `elev_km` explicite ne donne
   rien de nouveau. Pareil pour monsoon qui se reconstruit via
   `sin_doy` + `cos_doy` × `lat`.

3. **Régimes statiques** : synoptic indices (ONI, NAO) ne changent que
   lentement sur 1 an — une année entière peut-être en régime neutre
   ENSO, donc l'index n'a quasi aucune variance.

4. **Erreur moyenne vs queue** : la RMSE globale peut cacher un gain sur
   une petite fraction d'extreme events. Ces features pourraient être
   utiles en `risk_filter` (tail/vol gating) sans l'être comme
   `residual predictor`.

### Actions prises

- **Flags par défaut à False** dans `enrich_features` pour les 4 groupes.
- **Colonnes retirées de la liste extended** dans `xgboost_post.build_features`
  pour éviter mismatch train/inference.
- **Modules conservés** (`monsoon_features.py`, `altitude_features.py`)
  pour opt-in via training runs explicit + re-test avec plus de data.
- **Hypotheses loguées** REJECTED / PARTIAL dans `research/hypotheses.jsonl`
  → compte correctement dans `N_trials` du DSR.

## Upgrades modèle reportés 2026-04-20

Les upgrades suivants ont été **volontairement reportés** jusqu'à ce que
la data le permette.

### P6 — Regime HMM 8 climats (split TEMPERATE + TROPICAL)

**Pourquoi attendre** :
- 4-bucket HMM actuel a ~50-80 obs per bucket per station sur 1 an.
- 8-bucket diviserait par 2 → ~25-40 obs per bucket.
- BIC/AIC overfit penalty rend 8-bucket moins favorable que 4-bucket
  sur cette data.
- Attendre 2+ ans pour ré-évaluer.

**Activation conditionnelle** : re-run log-likelihood comparison quand
N > 500 per-bucket.

### P7 — Per-station BMA × regime weights (47 × 4 = 188 buckets)

**Pourquoi attendre** :
- BMA weights actuels : 47 stations × 12 sources = 564 paramètres libres
  sur ~17,000 observations blendées. Ratio param/obs = 3% — déjà limite.
- Extension regime : 47 × 4 × 12 = 2,256 paramètres → ratio 13%
  = **haut risque d'overfit**.
- Littérature NWP : ECMWF bat GFS en régime zonal, GFS meilleur en ridge,
  mais la différence est < 0.3°C et nécessite des années pour être
  validée statistiquement.

**Activation conditionnelle** : re-test après 2+ ans de data ou ERA5
hindcast multi-décennal disponible.

### N1 — Transformer temporel MPS (sequence 7-14j attention)

**Pourquoi attendre** :
- Transformer performance reposante fortement sur scale de data (10,000+
  sequences minimum pour éviter overfit sévère).
- Notre data : ~17,000 blend rows across 46 stations (367/station).
  Un transformer nécessiterait min. 3-5 stations × 3+ années pour
  atteindre un N effectif raisonnable.
- XGBoost actuel capture déjà >80% du signal extractable sur weather
  à 24-72h. Le marginal gain attendu d'un transformer : ~5-10% CRPS
  improvement (Pangu-Weather paper benchmark).
- Coût dev + training + maintenance : 10-15h + ~5h training MPS.
- **ROI défavorable** tant qu'on n'a pas ERA5 pour entraîner proprement.

**Activation conditionnelle** : post ERA5 5-ans (bloqué user CDS).
Alternative plus pragmatique : Pangu ONNX (bloqué user ONNX file).

### I3 — S3 snapshots, I2 — Grafana, I4 — Docker compose

**Pourquoi attendre** :
- Local Mac storage suffit tant que DB < 1 GB (actuellement 70 MB).
- Single-user local deployment → pas d'exigence multi-env / HA.
- Activation conditionnelle : post G3 real-money trading + > $10k capital.

## Discipline hedge-fund-grade — principes

Discussion 2026-04-20 : on évite les deux pièges classiques :

1. **Feature inflation** — ajouter des features non validées qui augmentent
   `N_trials` du DSR → le DSR prob_real baisse artificiellement.
2. **Complexité prématurée** — Transformer / per-city-regime BMA avant
   d'avoir la data qui permet de les valider → overfit garanti.

Ce que l'on fait à la place : stabiliser ce qui est **validé**
(EMOS + BMA + XGB + per-city calibrators + tail_filter), et ne pas
toucher avant que les données accumulent (G2 paper shadow 30+ jours,
ERA5, multi-années de weather).

**Règle** : pas de nouvelle feature activée en default sans CI95 > 0 sur
ablation walk-forward, N >= 100 per-test-fold, min 3 stations
diverses climatiquement.

## Related

- [[g1-g2-qualification-kit|G1→G2 Framework]]
- [[g1-g2-todo-tracker|Todo tracker]]
- [[economic-thesis|Economic thesis]]
- [[failure-modes|Failure modes]]
- [[strategy-lifecycle|Lifecycle]]
- [[STATE-HANDOFF]]
- [[_MOC|Polymarket MOC]]
