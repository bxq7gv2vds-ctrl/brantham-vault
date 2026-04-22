---
title: "Munich — Quant Deep Dive"
date: 2026-04-22
city: Munich
slug: munich
cluster: europe-central
n_markets: 352
volume_usdc: 2085095
yes_wr: 0.0969
xgb_auc: 0.7749
garch_persistence: 0.501
kyle_lambda_median: 0.000970
calibrated: false
chi2_pvalue: 0.0029
best_strategy: buy_no_uncertain
tags: [polymarket, weather, europe, munich, quant]
---

# Munich — Quant Deep Dive

## Résumé

352 marchés (le plus grand univers EU), $2.09M volume. **Seule ville non-calibrée** (chi² p=0.003) avec sur-pricing double : les extrêmes (0–0.10) et la zone 0.3–0.5 sont tous deux sur-pricés. GARCH persistence = 0.501 = la plus basse des 6 — chocs de vol s'amortissent vite. Le cluster hibernation (253 marchés) a YES WR = **0 %**.

## Chiffres clés

- XGBoost AUC : 0.775 ± 0.055 (le plus stable)
- GARCH persistence : 0.501 (mean-reverting rapide)
- Kyle lambda médian : 0.000970
- OFI : +0.639 (pression acheteuse la plus forte des 6)
- Maker HHI : 0.0791, top maker 26.0 %
- `is_bracket` feature importance : 6.7 % (seule ville avec contribution significative)
- WR YES régime hibernation : 0.00 % (253 marchés)

## Régimes

| Régime | N | WR YES | Vol médiane |
|---|---|---|---|
| 0 Hibernation | 253 | 0.00 % | 0.012 |
| 1 Résolution | 99 | 34.7 % | 0.144 |

## Edges documentés

| Stratégie | EV/trade | Bps ann. |
|---|---|---|
| BUY NO uncertain | +47.9 % | ~6 200 |
| BUY NO non-bracket | +43.1 % | ~5 600 |
| BUY NO tail (p<0.05) | +2.4 % | +237 |
| BUY NO high-drift | +19.4 % | +1 939 |
| BUY YES longshot | -74.1 % | ÉVITER |

## Tail européen

Non-brackets sous-pricés de **+4.31 pp** (WR réel 1.47 % vs prix 5.78 %). Les bookies surestiment la probabilité des événements directionnels Munich.

## Recommandations

1. BUY NO non-brackets Munich (edge structurel le plus fort)
2. BUY NO tail avec confirmation NWP 48h > 8 °C au-dessus du seuil
3. Signal monotonicity ≤ 0.1 → BUY NO automatique

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectories v2 findings]]
- [[../per-city-deep-dive/munich|Munich baseline deep-dive]]
- [[../../../_system/MOC-patterns|MOC Patterns]]
- [[./madrid|Madrid deep-dive]]
- [[./warsaw|Warsaw deep-dive]]
