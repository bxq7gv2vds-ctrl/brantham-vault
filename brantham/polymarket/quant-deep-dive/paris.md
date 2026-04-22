---
title: Paris — Quant Deep Dive
city: Paris
slug: paris
generated: 2026-04-22
n_markets: 521
n_trades: 375840
volume_usdc: 1879834
yes_win_rate: 0.1021
xgb_auc: 0.852
kyle_lambda_median: 0.000622
hhi_makers: 0.00919
best_strategy: buy_no_uncertain
sharpe_no_uncertain: 0.531
ev_no_uncertain_pct: 39.0
half_life_days: 0.667
calibrated: true
tags: [polymarket, weather, paris, quant, microstructure, calibrated]
---

# Paris — Quant Deep Dive

## Résumé Exécutif

Paris est le seul marché **parfaitement calibré** des 5 villes (chi²=10.87, p=0.054). Stationnaire sur ADF et KPSS simultanément — unique dans le corpus. Half-life = **0.667 jours** — correction la plus rapide. HHI = 0.00919 — marché le plus compétitif. XGBoost AUC=0.852. Feature `threshold` plus importante ici (13 %) qu'ailleurs.

## Chiffres Clés

| Métrique | Valeur |
|---|---|
| YES win rate | 10.21 % |
| XGBoost AUC | 0.852 ± 0.060 |
| Half-life mean-reversion | **0.667 jours** (IC95 [0.489, 0.845]) |
| Kyle lambda médiane | 0.000622 |
| HHI makers | 0.00919 (le plus compétitif) |
| IAT médiane | 26 secondes (2e plus liquide) |
| Spread BUY/SELL proxy | 124 bps |
| EV buy_no_uncertain | +39.0 % |
| Sharpe buy_no_uncertain | 0.531 |
| EV buy_no_brackets | +28.5 % (N=413) |
| Calibration chi² p-value | 0.054 (CALIBRÉ) |

## Findings Principaux

1. **Seule ville stationnaire sur ADF+KPSS** — série de drifts bien comportée
2. **Half-life 0.667j** — prix aberrants corrigés en <16h (signal mean-reversion rapide)
3. **Calibration quasi-parfaite** bin [0.2–0.3] : WR=24.2 % vs attendu 25 % (−0.8 pp)
4. **Feature threshold 13 %** — variance saisonnière plus marquée en France
5. **Régime Bull** (n=50, drift=+0.774, WR=100 %) — vagues de chaleur parisiennes détectables
6. **Cluster Active** (n=148) génère 2.7× plus de trades/marché que Quiet (418.5 vs 1118)

## Edge Opérationnel

- **NO uncertain** : prix YES ∈ [0.42, 0.60] → EV +39 %, Sharpe 0.531
- **NO brackets** : threshold ∈ {12, 13, 14}°C, prix ≤ 0.12 → EV +28.5 %, WR=88.1 %
- **Timing** : 14h–17h UTC (peak volume Paris, meilleure exécution)
- **Signal canicule** : drift > +0.60 → acheter YES (WR=100 %, n=50 marchés)

## Visualisations

- `viz_paris/surface_ev.html` — Surface EV 3D
- `viz_paris/scatter_regimes.html` — Scatter 3D régimes
- `viz_paris/density_volume.html` — Volume density 3D

## Related

- [[_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/paris|baseline Paris]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[quant-deep-dive/miami|Miami QDD]]
- [[quant-deep-dive/sao-paulo|Sao Paulo QDD]]
