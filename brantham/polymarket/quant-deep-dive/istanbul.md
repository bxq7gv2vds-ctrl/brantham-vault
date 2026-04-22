---
title: "Istanbul — Quant Deep Dive"
date: 2026-04-22
city: Istanbul
slug: istanbul
cluster: europe-east-med
n_markets: 110
volume_usdc: 670220
yes_wr: 0.0909
xgb_auc: 0.5717
garch_persistence: 0.504
kyle_lambda_median: 0.001416
calibrated: false
chi2_pvalue: 0.0494
best_strategy: buy_yes_longshot
tags: [polymarket, weather, europe, istanbul, quant]
---

# Istanbul — Quant Deep Dive

## Résumé

110 marchés, $670K volume. **Kyle lambda = 0.001416 — le plus élevé des 6** (impact de marché 4× Milan → micro-positions obligatoires). Mal calibrée (p=0.049). **Anomalie tail majeure : tail froids sous-pricés de -2.27 pp** (WR 4.0 % vs prix 1.73 %) — variabilité climatique méditerranéenne orientale non intégrée. `threshold` est le feature dominant XGBoost (37.9 % — unique). Régime hibernation : YES WR = 0 % (81 marchés). OFI = +0.597 (pression retail forte). BUY NO uncertain : Sharpe = 7.75 (résultat exceptionnel, n=7).

## Chiffres clés

- XGBoost AUC : 0.572 ± 0.197 (instable — données insuffisantes)
- GARCH persistence : 0.504 (mean-reverting modéré)
- Kyle lambda : 0.001416 (le plus élevé = marché le plus "impactable")
- Maker HHI : 0.0969 (le plus concentré des 6)
- `threshold` feature importance : 37.9 % (dominant, unique)
- Volatilité pp médiane : 0.035 (la plus élevée des 6)
- OFI : +0.597 (fort biais retail haussier)

## Régimes

| Régime | N | WR YES | Vol médiane |
|---|---|---|---|
| 0 Hibernation | 81 | 0.00 % | 0.021 |
| 1 Résolution | 29 | 34.5 % | 0.203 |

## Edges documentés

| Stratégie | N | WR | EV/trade | Bps ann. |
|---|---|---|---|---|
| BUY NO uncertain | 7 | 100 % | +96.7 % | ~12 500 |
| BUY YES longshot (<0.05) | 64 | 4.69 % | +238.5 % | ~2 400 |
| BUY NO high-drift | 50 | 100 % | +19.4 % | +1 938 |
| BUY NO brackets | 90 | 90.0 % | +5.7 % | +251 |
| BUY YES uncertain | 7 | 0.0 % | -100 % | ÉVITER |

## Tail européen — Anomalie méditerranéenne

Istanbul = seule ville avec sous-pricing des tail froids (-2.27 pp).

| Segment | WR réel | Prix | Mispricing |
|---|---|---|---|
| Tail (YES p<0.05) | 4.00 % | 1.73 % | **-2.27 pp sous-pricé** |
| Brackets all | 10.0 % | 12.5 % | +2.51 pp sur-pricé |
| Bin [0.5–0.6] | 0.0 % | 55 % exp | sur-pricing maximal |

Catalyseur : oscillation arctique (NAO négatif) → flow froid vers la Méditerranée orientale possible même en avril.

## Recommandations

1. BUY YES tail Istanbul (≤ 0.020, seuil ≤ 8 °C) avec vérification NAO/ECMWF ensemble
2. BUY NO uncertain (100 % WR, Sharpe 7.75 — à confirmer sur plus grand N)
3. Ne jamais BUY YES uncertain (EV = -100 %)
4. Positions max $10 sur tail (Kyle lambda élevé)

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectories v2 findings]]
- [[../per-city-deep-dive/istanbul|Istanbul baseline deep-dive]]
- [[../../../_system/MOC-patterns|MOC Patterns]]
- [[./moscow|Moscow deep-dive]]
- [[./warsaw|Warsaw deep-dive]]
