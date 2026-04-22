---
title: "Moscow — Quant Deep Dive"
date: 2026-04-22
city: Moscow
slug: moscow
cluster: europe-east
n_markets: 99
volume_usdc: 385138
yes_wr: 0.0909
xgb_auc: 0.5114
garch_persistence: 0.0
kyle_lambda_median: 0.000717
calibrated: true
chi2_pvalue: 0.6612
best_strategy: buy_yes_uncertain
tags: [polymarket, weather, europe, moscow, quant]
---

# Moscow — Quant Deep Dive

## Résumé

99 marchés seulement (10 jours de données), $385K volume. **XGBoost AUC = 0.511 ≈ aléatoire** — Moscou est la ville la moins prévisible à l'ouverture. **Meilleure calibration des 6** (chi² p=0.661). Anomalie : non-brackets "above" sous-pricés de **-4.12 pp** (dérèglement climatique printanier non intégré). Maker HHI = 0.0286 (le plus fragmenté — pas de maker dominant). Régime résolution YES WR = 46.7 % (le plus élevé des 6).

## Chiffres clés

- XGBoost AUC : 0.511 ± 0.025 (le plus faible — non prédictif)
- Calibration chi² p=0.661 (la meilleure)
- Kyle lambda : 0.000717 (impact élevé → micro-positions requises)
- Maker HHI : 0.0286 (le plus fragmenté)
- OFI : +0.419 (la plus faible pression retail)
- Skewness : 2.302 / kurtosis : 6.489 (les plus élevés des 6)
- WR YES régime résolution : 46.7 % (le plus élevé des 6)

## Régimes

| Régime | N | WR YES | Vol médiane |
|---|---|---|---|
| 0 Hibernation | 76 | 2.63 % | 0.018 |
| 1 Résolution | 15 | 46.7 % | 0.188 |

## Edges documentés

| Stratégie | EV/trade | Bps ann. |
|---|---|---|
| BUY YES uncertain | +33.3 % | ~4 300 |
| BUY YES non-bracket above | +4.12 pp | +412 |
| BUY NO high-drift | +16.4 % | +1 638 |
| BUY NO brackets | +2.1 % | +145 |

## Tail européen

- Non-brackets "above" : WR réel 22.2 % vs prix 18.1 % → **sous-pricing -4.12 pp**
- Interprétation : printemps moscovites plus chauds avec le dérèglement climatique — non intégré dans le pricing
- Tail (YES p<0.05) : quasi-neutre (+0.25 pp)
- **Règle critique : NWP avant toute entrée** (AUC 0.511 → price_open non informatif)

## Recommandations

1. NWP obligatoire avant toute entrée (AUC 0.511 = pas d'edge à l'ouverture)
2. BUY YES non-bracket "above" (dérèglement climatique sous-pricé)
3. BUY NO bracket si NWP confirme pas de gel dans les 48h

## Contrainte

Données insuffisantes (10 jours). Tous les edges à confirmer sur 3 mois minimum.

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectories v2 findings]]
- [[../per-city-deep-dive/moscow|Moscow baseline deep-dive]]
- [[../../../_system/MOC-patterns|MOC Patterns]]
- [[./warsaw|Warsaw deep-dive]]
- [[./istanbul|Istanbul deep-dive]]
