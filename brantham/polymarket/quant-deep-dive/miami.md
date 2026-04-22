---
title: Miami — Quant Deep Dive
city: Miami
slug: miami
generated: 2026-04-22
n_markets: 697
n_trades: 423994
volume_usdc: 2219127
yes_win_rate: 0.1098
xgb_auc: 0.871
kyle_lambda_median: 0.00055
hhi_makers: 0.02263
best_strategy: buy_no_favorites
sharpe_no_uncertain: 0.489
ev_no_uncertain_pct: 39.4
tags: [polymarket, weather, miami, quant, microstructure]
---

# Miami — Quant Deep Dive

## Résumé Exécutif

Miami est le marché le **plus liquide et le plus ancien** du corpus (697 marchés, 423 994 trades, $2.22M on-chain). Le YES ne gagne que **11.0 %** du temps. XGBoost AUC **0.871** — meilleur prédicteur des 5 villes. Marché mis-calibré (p=5.5e-5), surtout dans les bins 0.30–0.60.

## Chiffres Clés

| Métrique | Valeur |
|---|---|
| YES win rate | 10.98 % |
| XGBoost AUC | 0.871 ± 0.052 |
| Kyle lambda médiane | 0.00055 |
| HHI makers | 0.02263 (compétitif) |
| IAT médiane | 68 secondes |
| Whales > $100 | 52.7 % du volume |
| Buy ratio | 72.4 % |
| EV buy_no_uncertain | +39.4 % |
| Sharpe buy_no_uncertain | 0.489 |
| Régime Bull (WR=100 %) | 71 marchés |

## Findings Principaux

1. **Calibration** : bin [0.5–0.6] WR=0 % sur 6 marchés — achat NO quasi-certain
2. **Hurst H=2.139** : artefact de série courte mais confirme tendance forte vers NO
3. **Régime vol cluster 0** (n=71, drift=+0.79, WR=100 %) — identifiable par vol > 0.20
4. **Feature importance** : price_open domine à 38.6 %, is_bracket 23.9 %
5. **Pic activité** : 17h UTC (13h EST) — session après-midi US

## Edge Opérationnel

- **Seuil NO uncertain** : prix YES ∈ [0.45, 0.60] → EV +39.4 %, Sharpe 0.489
- **Seuil NO bracket** : is_bracket=1, prix YES ≤ 0.15 → EV +8.8 %, WR=87.5 %
- **Trigger Bull** : drift > +0.50 AND vol > 0.20 → acheter YES (WR=100 %, n=71)

## Visualisations

- `viz_miami/surface_ev.html` — Surface EV 3D par prix et stratégie
- `viz_miami/scatter_regimes.html` — Scatter 3D des régimes de marché
- `viz_miami/density_volume.html` — Volume density 3D par heure UTC

## Related

- [[_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/miami|baseline Miami]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[quant-deep-dive/paris|Paris QDD]]
- [[quant-deep-dive/shanghai|Shanghai QDD]]
