---
title: "Milan — Quant Deep Dive"
date: 2026-04-22
city: Milan
slug: milan
cluster: europe-south
n_markets: 253
volume_usdc: 1967626
yes_wr: 0.0909
xgb_auc: 0.8102
garch_persistence: 0.961
kyle_lambda_median: 0.000345
calibrated: true
chi2_pvalue: 0.1063
best_strategy: buy_no_uncertain
tags: [polymarket, weather, europe, milan, quant]
---

# Milan — Quant Deep Dive

## Résumé

253 marchés, $1.97M volume. **XGBoost AUC = 0.810 — le plus élevé des 6 villes.** Hurst le plus bas (0.173 — anti-persistance maximale). Kyle lambda le plus faible (0.000345 — marché le plus liquide). Brackets sur-pricés de **+4.60 pp** en moyenne. Tail (p<0.05) a WR réel 0 % sur 128 marchés.

## Chiffres clés

- XGBoost AUC : 0.810 ± 0.059 (meilleur et le plus stable)
- GARCH persistence : 0.961
- Kyle lambda médian : 0.000345 (le plus faible = le plus liquide)
- Hurst médian : 0.171 (anti-persistance maximale)
- Tail trades (p<0.05) : 60.3 % count (le plus élevé des 6)
- Durée marché : 73.9h (la plus courte)
- `price_open` feature importance : 51.7 % (signal le plus dominant toutes villes)

## Régimes

| Régime | N | WR YES | Vol médiane |
|---|---|---|---|
| 0 Faible vol | 178 | 0.56 % | 0.015 |
| 1 Résolution | 75 | 29.3 % | 0.144 |

## Edges documentés

| Stratégie | EV/trade | Bps ann. |
|---|---|---|
| BUY NO uncertain | +48.6 % | ~6 300 |
| BUY NO brackets all | +29.7 % | +460 |
| BUY NO high-drift | +26.4 % | +2 643 |
| BUY NO tail (p<0.05) | +2.2 % | +215 |

## Tail européen

- Bin [0.5–0.6] : WR réel = 0 % sur 6 marchés → vendre YES 0.50–0.65 agressivement
- Brackets mispricing : +4.60 pp (le plus élevé des 6)
- Règle price_open : si price_open < 0.10, BUY NO automatique (AUC 0.81 → 87 % précision)

## Recommandations

1. BUY NO bracket [0.5–0.6] (certainement NO, WR réel = 0 %)
2. BUY NO bracket standard + filtre monotonicity < 0.1
3. AUC-based scoring : price_open < 0.10 → BUY NO automatique

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectories v2 findings]]
- [[../per-city-deep-dive/milan|Milan baseline deep-dive]]
- [[../../../_system/MOC-patterns|MOC Patterns]]
- [[./madrid|Madrid deep-dive]]
- [[./warsaw|Warsaw deep-dive]]
