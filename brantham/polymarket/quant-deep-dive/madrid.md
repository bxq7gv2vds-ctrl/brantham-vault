---
title: "Madrid — Quant Deep Dive"
date: 2026-04-22
city: Madrid
slug: madrid
cluster: europe-south
n_markets: 253
volume_usdc: 2324341
yes_wr: 0.0909
xgb_auc: 0.7249
garch_persistence: 0.961
kyle_lambda_median: 0.000474
calibrated: true
chi2_pvalue: 0.0977
best_strategy: buy_no_uncertain
tags: [polymarket, weather, europe, madrid, quant]
---

# Madrid — Quant Deep Dive

## Résumé

253 marchés, $2.32M volume, YES WR = 9.09 %. Madrid est calibrée (chi² p=0.098) et présente un sur-pricing structurel des brackets en zone 0.3–0.4 de **-23 pp**. Anomalie unique : les tail froids (YES p<0.05) sont **sous-pricés** — WR réel 2.96 % vs prix 1.83 %.

## Chiffres clés

- XGBoost AUC : 0.725 ± 0.146
- GARCH persistence : 0.961 (quasi-unitaire)
- Kyle lambda médian : 0.000474 (impact modéré)
- OFI : +0.518 (pression acheteuse retail)
- Tail trades (p<0.05) : 47.3 % count, 1.9 % volume
- Maker HHI : 0.0433 (marché fragmenté)
- Hurst médian par marché : 0.181 (anti-persistant)

## Régimes

| Régime | N | WR YES | Vol médiane |
|---|---|---|---|
| 0 Hibernation | 196 | 0.51 % | 0.015 |
| 1 Résolution | 51 | 41.2 % | 0.203 |

## Edges documentés

| Stratégie | EV/trade | Bps ann. |
|---|---|---|
| BUY NO uncertain | +62.9 % | ~8 200 |
| BUY YES longshot | +51.2 % | ~500 |
| BUY NO high-drift | +21.5 % | ~2 152 |
| BUY NO brackets | +2.9 % | +165 |

## Recommandations

1. BUY YES tail froid ≤ 0.020 en mars-avril (sous-pricing +114 bps)
2. BUY NO bracket zone 0.30–0.40 (sur-pricing -23 pp)
3. Signal drift_pp < -0.05 → BUY NO immédiat

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectories v2 findings]]
- [[../per-city-deep-dive/madrid|Madrid baseline deep-dive]]
- [[../../../_system/MOC-patterns|MOC Patterns]]
- [[./munich|Munich deep-dive]]
- [[./milan|Milan deep-dive]]
