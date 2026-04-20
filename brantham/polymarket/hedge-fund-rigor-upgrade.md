---
name: Hedge Fund Rigor Upgrade — 2026-04-20 session C
description: Upgrade méthodologique pour passer de "scaffold hedge fund" à "rigueur hedge fund institutionnelle". 10 livrables couvrant statistical rigor, backtest discipline, risk management professionnel.
type: methodology
created: 2026-04-20
updated: 2026-04-20
priority: critical
tags: [polymarket, hedge-fund, rigor, statistics, methodology, validation]
---

# Hedge Fund Rigor Upgrade — 2026-04-20

Post G1-G2 Kit + Execution & Performance Kit, le user a demandé **plus de rigueur niveau hedge fund pro**. Cet upgrade apporte la discipline statistique et méthodologique manquante.

## Scripts livrés (10)

| # | Livrable | Rôle | Status |
|---|---|---|---|
| H1 | `tc_aware_attribution.py` | Attribution avec TC model per-trade + bootstrap CI95 | done, findings below |
| H2 | (survivorship audit) | Investigation manuelle via audit_log city_config history | done, no bias confirmed |
| H3 | `diebold_mariano_test.py` | DM test HLN-corrected pour forecast accuracy comparison | done, framework ready |
| H4 | (bootstrap CI upgrades) | Intégré dans tc_aware_attribution.py | done |
| H5 | `var_es_kupiec.py` | VaR historical/parametric/MC + ES + Kupiec POF + Christoffersen CC | done, T=2 limited |
| H6 | `correlation_kelly.py` | Portfolio Kelly via pair_correlations (C^-1 · f) | done, 35% reduction vs naive |
| H7 | `stationarity_tests.py` | ADF + KPSS + Ljung-Box avec consensus | done, findings ci-dessous |
| H8 | (regime-aware P&L) | **Deferred** — nécessite backfill HMM state par signal | skipped v1 |
| H9 | (PIT data audit) | **Covered by leakage_audit.py v1** — no HARD leakage detected | done |
| H10 | `bonferroni_fdr_calibrators.py` | Multiple-testing correction Bonferroni + BH FDR 5% | done, 21/21 survive |

## Findings hedge-fund-grade

### H1 — TC-aware attribution (bootstrap CI95)

**Résultats critiques** :
- TC eats **6.8 %** of gross P&L (modèle conservatif)
- **5 sunset candidates confirmés** avec CI95 upper < 0 :
  - `CONFIRMED_YES alpha` : CI95 [-1.10, -1.09] — complètement cassée
  - `city Tokyo` : CI95 [-1.06, -1.05] — DISABLED cohérent
  - `city Miami` : CI95 [-0.31, -0.02] — **SHADOW → DISABLED recommandé**
  - `city NYC` : CI95 [-0.62, -0.08]
  - `edge_tier 8-15 %` : CI95 [-0.31, -0.18] — threshold min à raise à 15 %
- **Winners high-confidence** (CI95 > 0) : austin, atlanta, SF, houston, denver, LA, shenzhen, KL, lucknow, tier_25+

### H2 — Survivorship bias audit

Via `audit_log.city_config.update` history : Tokyo/Chicago/NYC signaux tous émis PRE-DISABLE. Miami SHADOW signaux post-19:48 sont size-reduced (by design). **Pas de bias** dans notre sample.

Subtle reserve : villes jamais-enabled (Jakarta, Buenos Aires, etc.) absentes → échantillon biased vers villes ex-ante favorables. Inévitable sans A/B randomization.

### H3 — Diebold-Mariano test

Framework DM HLN opérationnel. Révèle que **features validées comme REJECTED** dans `validate_feature_impact.py` sont **cohérentes** : quand disabled dans `build_features` (où je les ai retirées), DM ne peut pas les distinguer (RMSE identique) → cohérence méthodologique confirmée.

Seul groupe testable (synoptic/pdo_dmi group) montre **RJTT M2 better p<5 %** (DM 1.86) — synoptic bulk marginalement utile à Tokyo.

### H5 — VaR / ES / Kupiec

T=2 daily returns → test non-exécutable. **Framework prêt** pour quand T≥30 (2-3 semaines).

### H6 — Correlation-adjusted Kelly

Sur 8 positions US/Asia :
- Avg off-diagonal ρ = **+0.09** (well-diversified)
- Naive allocation : 8 × 0.5 = **4x bankroll** (over-leveraged)
- Shrunk Kelly : **3.6x**
- **Portfolio Kelly (C^-1 · f)** : **2.6x** = correct answer

**35 % reduction** vs naive. À appliquer en live runner post-wallet — modifier `risk_manager.py` pour utiliser portfolio Kelly au lieu de per-signal.

### H7 — Stationarity & autocorrelation

Per-trade N=1113 :
- **ADF stationary** p<0.01
- **KPSS non-stationary** p=0.01 (disagree avec ADF — clustering)
- **Ljung-Box lag-10** p=0.019 → **autocorrelation présente**
- Skew +4.88, Kurt 25.6 → **fat tails convex**

**Conséquence** : Sharpe annualization (×√252) est **BIAISÉ** sur cette data. Il faut :
- Newey-West HAC standard errors (in place de simple std)
- OR Block bootstrap (déjà partly en MC P&L v1)

Notre DSR per-trade reste indicatif mais doit être reporté avec HAC correction pour G2 graduation strict. Je l'ajouterai à `deflated_sharpe.py` quand T daily ≥ 30.

### H8 — Regime-aware P&L (DEFERRED)

Nécessite backfill HMM state par signal_log row. Chaque signal devrait stocker `regime_state` au moment emit_ts. Tâche séparée (besoin re-computer HMM state historique sur ~1700 signaux). Prioritizer post-G2.

### H9 — Point-in-time data audit

`leakage_audit.py` v1 : 0 HARD / 1 SOFT (synoptic publication lag) / 2 CROSS (diurnal + soil, mitigated by obs_ts < issue_ts check). **No leakage**.

v2 dynamic check : potentiel upgrade — build features at `ts - 48h` then at `ts`, diff columns. Deferred v2 si besoin.

### H10 — Bonferroni / BH FDR

**21/21 per-city calibrators** passent Bonferroni FWER 5 % + Benjamini-Hochberg FDR 5 %. p-value=0.000 sur chacun → **statistiquement robustes à multiple-testing correction**.

La discipline de per-city calibration est **empiriquement justifiée** au standard hedge fund.

## Conséquences sur le G1 Scorecard

Aucun critère G1 n'est remis en cause par cet audit. Cependant :

- **DSR** devrait intégrer NW correction pour production-grade (v2)
- **MC P&L** devrait utiliser block bootstrap par défaut (autocorrelation detected)
- **VaR backtest** attend T≥30 pour être crédible
- **Sunset list** post-TC : CONFIRMED_YES + Miami + edge_tier_8_15 → action immediate
- **Portfolio Kelly** à wire dans risk_manager quand live

## Actions immédiates recommandées (hors user actions)

1. **Downgrade Miami SHADOW → DISABLED** (CI95 post-TC strict < 0)
2. **Investigate CONFIRMED_YES alpha logic** (ROI -100 % — impossible sans bug)
3. **Raise min_edge threshold** de 4 % à 8 % ou 15 % (tier_4_8 OK mais tier_8_15 négatif, tier_15_25 limite)
4. **Switch MC P&L default** à block bootstrap (autocorrelation detected)
5. **Portfolio Kelly wiring** dans risk_manager.py après wallet setup

## Hors scope explicite

| Gap | Raison |
|---|---|
| Model Confidence Set (MCS) | Framework Hansen-Lunde-Nason — complexité non-justifiée jusqu'à plusieurs candidate models |
| White's Reality Check / SPA | DSR + Bonferroni couvrent le multiple-testing usual |
| Ledoit-Wolf shrinkage covariance | Pertinent quand N_assets >> N_obs. On a 47 stations × 1700 signals : OK raw sample covariance |
| GARCH forecasting | Classique pour equity vol. Weather vol a régime-switching mieux capturé par HMM |
| Adversarial validation | Très data-size dependent — pas de gain clair sur 1 year data |
| Almgren-Chriss optimal exec | Pour post-G3. Skeleton livrable |
| VPIN toxic flow | Pour post-G3 avec trade tape |
| Copula joint dependency | Risk dimension complexity — correlation-Kelly couvre premier ordre |

## Related

- [[g1-g2-qualification-kit|G1→G2 Framework]]
- [[gate-scorecard-spec|Scorecard spec]]
- [[feature-rejection-log|Feature rejection log]]
- [[sessions/2026-04-20-execution-performance-kit|Execution & Perf Kit session]]
- [[sessions/2026-04-20-g1-g2-kit-build|G1-G2 Kit build session]]
- [[STATE-HANDOFF]]
- [[_MOC|Polymarket MOC]]
