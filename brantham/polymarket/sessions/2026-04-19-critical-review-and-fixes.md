---
name: Session 2026-04-19 — Critical Review & Fixes
description: Ablation-driven fixes après review critique quant — désactivation des couches nuisibles, backfill outcomes, realistic slippage
type: session
created: 2026-04-19
tags: [polymarket, ablation, critical-review, fixes, reality-check]
priority: high
---

# Session 2026-04-19 — Critical Review & Fixes

Audit quant-level de toute l'infra a révélé des problèmes structurels. Cette session attaque chaque point identifié.

## Résumé TL;DR

**10 fixes appliqués.** Le plus important :
- **Ablation study** prouve que `quantile + conformal + calibration` **dégradent** Brier 3-4× vs Gaussian baseline
- **Backfill outcomes** : N=217 → N=992 (+356 %) → toutes les stats device statistiquement utilisables
- **Tokyo, Chicago, NYC** désactivés par audit per-city (WR < 35 % sur N ≥ 22)
- **DRN zeroed** (weight 0) tant que pas ERA5 — il polluait l'ensemble
- **CRPS floor** 0.5 → 0.15 : les weights BMA/XGB sont enfin différentiables

## 10 fixes appliqués

### 🔧 #47 — Circuit breaker stuck DISABLED
Un test debug avait laissé `__CIRCUIT_BREAKER__` tripped à −100 $ simulé. **Cooldown 24 h → système OFF** pendant discussion.
- **Fix immédiat** : DELETE row → rearm immédiat
- **Fix structurel** : clean-state clemency — si `daily_pnl ≥ 0` et `dd = 0`, cooldown tombe à 1 h au lieu de 24 h. Protège contre les false positives de test sans compromettre les vrais trips.

### 🔧 #48 — DRN weight 0 tant que pas ERA5
DRN val CRPS = 1.22 vs BMA 0.48 / XGB 0.40 → DRN **dégrade** les prédictions. Weight 0.17 dans ensemble était net-négatif.
- `DRN_DISABLED_UNTIL_ERA5 = True` dans `train_ensemble_weights.py` et `train_regime_selector.py`
- Current state: BMA 0.5 / XGB 0.5 / DRN 0.0
- Flag pour ré-activer quand ERA5 ground truth disponible

### 🔧 #49 — CRPS floor regime V1
`CRPS_FLOOR = 0.5` était **plus grand que tous les CRPS empiriques** (0.4-0.47). Résultat : BMA = XGB identique dans chaque bucket.
- Baissé à 0.15
- Après retrain : weights spread 0.35-0.65 (discrimination retrouvée)
- Q2_AMJ POLAR : XGB 0.65 vs BMA 0.35 — XGB domine vraiment en spring polar

### 🔧 #50 — Audit log retention cron
`prune_older_than(90)` existait mais **jamais appelé** → table grossit sans fin.
- `scripts/audit_prune.py` + launchd daily 02:30
- Retention 90 jours

### 🔧 #51 — Latency samples schema
Fausse alerte — mon query SQL utilisait `stage` au lieu de `step` (colonne réelle). Code production OK.

### 🔥 #52 — Ablation study — L'INSIGHT MAJEUR

**Résultats sur 150 outcomes résolus** :

| Config | Brier | ΔBrier vs full_stack |
|--------|-------|----|
| full_stack (quantile+conformal+calibration) | 0.0565 | baseline |
| no_quantile | **0.0175** | **−70 % (BETTER)** |
| no_calibration | 0.0419 | −26 % (BETTER) |
| no_conformal | 0.0540 | −4 % (better) |
| no_ensemble / no_xgb_post | 0.0565 | ≈ |
| **gaussian_baseline** (raw BMA + XGB residual) | **0.0183** | **−68 % (BEST)** |

**Verdict brutal** : les 3 couches ML "avancées" ajoutées sur la semaine dégradent toutes les prédictions. Le modèle raw EMOS+BMA+XGB avec conversion Gaussienne bat tout le reste. Le quantile regression souffrait de la petite taille du training set (5870 rows spread sur 10 régions) — overfitting net. Le calibrator isotonic over-fitte sur 189 outcomes.

**Action** :
- `use_quantile`, `use_calibration` → **OFF par défaut** dans `run_alpha_live.py`
- Flags renommés en `--use-quantile` / `--use-calibration` (opt-in explicite)
- `use_volatility_filter` reste ON (il ablate positive)

### 🔧 #53 — Slippage realistic haircut
Module `slippage_model.py` : paper → live haircut avec spread 2 cts, fill ratio 80 %, rejection 5 %, oracle cost 1 %.
- Paper P&L $915 → **Live net $545** (haircut 40 %)
- MODEL_VS_MARKET paper $1 074 → net $655 (−39 %)
- Signal clair que **Sharpe live ≈ 0.6× Sharpe paper**

### 🔥 #54 — Backfill outcomes (CRITIQUE)
`reconcile_from_obs.py --lookback-hours 720` (30 jours) au lieu des 48 h par défaut.
- **775 nouveaux outcomes settled** via Open-Meteo archive
- N total: **217 → 992** (+356 %)
- WR overall: 83.9 % → 82.1 % (stable)
- Paper P&L $915 → **$13 299** (un mois de data)
- Live net P&L : **$13 182** (haircut seulement 0.9 % car dominant par les wins)

### 🔧 #55 — Retire dead alphas
CONVEX_ARB, OB_IMBALANCE : 0 signal live sur 2 jours. Code gardé mais derrière flags `enable_convex_arb` / `enable_ob_imbalance` (opt-in).
- Hot loop plus rapide
- Logs moins bruyants
- Les alphas core (MODEL_VS_MARKET, CONFIRMED_NO, PAIR_ARB) restent ON

### 🔧 #56 — Benchmark Gaussian vs Quantile
Résolu par l'ablation study #52 — Gaussian bat Quantile+Conformal par 3×. Pas besoin d'un test séparé.

## Nouveau état city_config (avec N=992)

Reconfiguré via `audit_per_city.py --apply` :

| Status | Cities | Raison |
|---|---|---|
| **DISABLED** (3) | Tokyo (83, 0%), Chicago (41, 34%), NYC (22, CI<30%) | **Tokyo = pire perdant du système** |
| **SHADOW** (2) | Dallas (77, 77%), Miami (61, mixed) | size × 0.20 |
| **ENABLED** avec Kelly 0.50 (14) | Atlanta, Austin, Beijing, Denver, Houston, KL, Lucknow, LA, Mexico City, Paris, SF, Shenzhen, Tel Aviv, Hong Kong | Kelly boost 2× |
| **ENABLED** Kelly 0.25 (7) | Ankara, Helsinki, Madrid, Moscow, Seoul, Taipei, Chongqing | N < 10 — exploration default |

**Chicago** a perdu son statut "top" en passant de N=11 (100%) à N=41 (34%) — **l'overfit small-sample est bien réel**.

**Tokyo** est maintenant le cas d'étude : N=83 WR 0 % sur MODEL_VS_MARKET. Investiguer pourquoi (probablement EMOS mal calibré RJTT, ou bias NWP sources).

## Ce qui reste honnête à dire

1. **Sharpe encore n/a** — 2 jours distincts de P&L seulement. Nécessite 20 j minimum. Les backfill settlent les outcomes mais sur les mêmes dates d'émission.

2. **N=992 est "bon" mais pas "excellent"** — un quant serious attend 5 000+ avant de mettre du real money.

3. **Le paper est toujours biaisé** — 80 % haircut slippage modélisé arbitrairement. Le vrai test reste avec real $500 en live.

4. **Les signaux émis actuels (2-3 par scan)** sont **cleaner** mais volume bas — l'infra est devenue trop restrictive ? À surveiller.

5. **Aucun model foundation** (Pangu / GraphCast / Aurora) → gap ML SOTA réel non comblé.

## Score audit réel

**52/100 → ~65/100**. J'avais flatté 82 avant l'audit.

Le gain vient de :
- Ablation honest (+5)
- Backfill 4× data (+5)
- DRN zeroed (+2)
- Dead alphas retirés (+1)

Ce qui reste bloque le gain :
- N=992 insuffisant pour Sharpe reliable
- Pas de live test avec real money
- ERA5 toujours bloqué

## Related

- [[_MOC|Polymarket Hub]]
- [[sessions/2026-04-19-hedge-fund-grade-upgrades|Session matin — upgrade hedge fund grade]]
- [[reports/ablation-2026-04-19|Ablation study complète]]
- [[reports/paper-vs-live-2026-04-19|Paper vs live net]]
- [[STATE-HANDOFF|State handoff]]
- [[audit-hedge-fund-grade|Audit détaillé]]
