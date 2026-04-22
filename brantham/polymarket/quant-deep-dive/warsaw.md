---
title: "Warsaw — Quant Deep Dive"
date: 2026-04-22
city: Warsaw
slug: warsaw
cluster: europe-east
n_markets: 253
volume_usdc: 1457707
yes_wr: 0.0909
xgb_auc: 0.7551
garch_persistence: 0.985
kyle_lambda_median: 0.000268
calibrated: true
chi2_pvalue: 0.1043
best_strategy: buy_yes_uncertain
tags: [polymarket, weather, europe, warsaw, quant]
---

# Warsaw — Quant Deep Dive

## Résumé

253 marchés, $1.46M volume. **GARCH persistence = 0.985 — la plus élevée des 6.** Seule ville où `is_bracket` est le feature XGBoost dominant (32 %). **Seule ville où BUY YES uncertain est la meilleure stratégie** (WR 71.4 %). Les non-brackets sont sous-pricés de **-5.78 pp** — anomalie inverse par rapport aux autres villes. Kurtosis = 5.749 (le plus élevé = queues les plus épaisses).

## Chiffres clés

- XGBoost AUC : 0.755 ± 0.105
- GARCH persistence : 0.985 (quasi marche aléatoire)
- Kyle lambda médian : 0.000268 (le plus bas mais volume aussi le plus faible)
- `is_bracket` feature importance : 32.0 % (unique parmi les 6 villes)
- Tail trades (p<0.05) : 67.2 % count (le 2ème plus élevé)
- Large trade dominance : 90.9 % du volume (le plus concentré)
- Kurtosis drifts : 5.749

## Régimes

| Régime | N | WR YES | Vol médiane |
|---|---|---|---|
| 0 Hibernation | 191 | 1.05 % | 0.014 |
| 1 Résolution | 58 | 36.2 % | 0.151 |

## Edges documentés

| Stratégie | EV/trade | Bps ann. |
|---|---|---|
| BUY YES uncertain | +45.3 % | ~5 900 |
| BUY YES non-bracket | +5.78 pp | +578 |
| BUY NO high-drift | +19.4 % | +1 940 |
| BUY NO brackets | +5.4 % | +311 |

## Tail européen — Anomalie inverse

- Non-brackets sous-pricés : WR réel 13 % vs prix 7.3 % → -5.78 pp
- Bin [0.5–0.6] : WR réel 66.7 % vs exp 55 % → sous-pricé -11.7 pp
- Bracket [0.30–0.40] : WR réel 0 % vs exp 35 % → sur-pricé +35 pp

## Recommandations

1. BUY YES uncertain Warsaw (contre-intuitif mais documenté, WR 71.4 %)
2. BUY YES non-bracket (sous-pricing chaleur printanière)
3. BUY NO bracket [0.30–0.40] (sur-pricing massif)

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectories v2 findings]]
- [[../per-city-deep-dive/warsaw|Warsaw baseline deep-dive]]
- [[../../../_system/MOC-patterns|MOC Patterns]]
- [[./moscow|Moscow deep-dive]]
- [[./istanbul|Istanbul deep-dive]]
