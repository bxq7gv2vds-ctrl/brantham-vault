---
title: "Quant Deep Dive — Hong Kong"
slug: hong-kong
city: Hong Kong
country: China SAR
timezone: UTC+8
n_markets: 260
n_trades: 140256
volume_usdc: 1090039
yes_win_rate: 0.0934
xgb_auc: 0.7415
kyle_lambda_median: 0.000537
garch_persistence: 0.8551
best_edge: buy_yes_longshot
best_ev_pct: 56.05
asian_volume_pct: 49.2
peak_hour_utc: 6
vol_regime_ratio: 16.20
tags: [polymarket, weather, quant, asian-markets, hong-kong]
generated: 2026-04-22
---

# Quant Deep Dive — Hong Kong

> Analyse quantitative profonde des marchés météo Polymarket pour Hong Kong (China SAR, UTC+8).
> 260 marchés | 140,256 trades | $1,090,039 USDC | WR YES = 9.3%

## Synthèse exécutive

Hong Kong présente le profil typique des marchés asiatiques Polymarket : concentration du volume sur la fenêtre UTC 00-07h (49.2% des trades), pic absolu à UTC 06:00 (12,663 trades), et une formation de prix dominée par les participants locaux (HKT).

L'edge principal est **`buy_yes_longshot`** avec EV/bet = **+56.05%**. Le modèle XGBoost atteint AUC = **0.7415**, signal marginal. Kyle lambda médian = 0.000537 (impact élevé — sizing max ~$50).

## Métriques clés (≥30 chiffres)

| Indicateur | Valeur |
|---|---|
| N marchés | 260 |
| N trades | 140,256 |
| Volume USDC | $1,090,039 |
| YES win rate | 0.0934 |
| NO win rate | 0.9066 |
| Trades / marché | 539.4 |
| Kyle lambda médian | 0.000537 |
| Kyle lambda moyen | 0.001868 |
| GARCH persistence | 0.8551 |
| GARCH omega | 110.3414 |
| GARCH alpha1 | 0.0000 |
| GARCH beta1 | 0.8551 |
| XGB AUC | 0.7415 (±0.0974) |
| XGB Brier | 0.08557 |
| XGB log-loss | 0.2929 |
| Feature top | price_open (0.359) |
| Calibration p | 0.0367 (FAIL) |
| Régimes k | 2 (silhouette=0.4449) |
| Régime 0 vol | 0.010357 |
| Régime 1 vol | 0.167815 |
| Ratio vol1/vol0 | 16.20x |
| Régime 0 Hurst | 0.1303 |
| Régime 1 Hurst | 0.2754669973094765 |
| Régime 0 WR YES | 0.0000 |
| Régime 1 WR YES | 0.3037974683544304 |
| Skewness drifts | 1.9435 |
| Kurtosis excess | 4.4511 |
| JB stat | 366.13 |
| Shapiro stat | 0.7108 |
| Bracket NO WR | 0.9139 |
| Bracket NO EV | +5.31% |
| Bracket NO Sharpe | 0.1339 |
| Longshot WR | 0.0255 |
| Longshot EV | +56.05% |
| Asian vol % | 49.23% |
| Asian/Western ratio | 1.94x |
| Peak heure UTC | 06:00 (12,663 trades) |

## Pattern temporel asiatique

Volume UTC 00-07h (fenêtre locale HKT 08-15h) : **49.2%** — Ce ratio est la caractéristique la plus distinctive du cluster asiatique vs villes américaines (ratio inverse occidental > 2x). La liquidité est concentrée au début de session locale, avec un pic qui correspond à l'ouverture des marchés de capitaux asiatiques (Tokyo 09:00 JST = UTC 00:00, Shanghai 09:30 CST = UTC 01:30).

## Edges et recommandations

- **`buy_yes_longshot`** (meilleur) : EV = +56.05%, WR = 0.025, Sharpe = 0.0489
- **`buy_yes_uncertain`** (à éviter) : EV = -46.62%

**Seuil d'entrée bracket NO :** vol 3 premiers trades <= 0.0207, prix >= 0.883
**Fenêtre optimale :** UTC 05:00-07:00

## Visualisations

- `viz_hong-kong/surface_volume.html` — Surface 3D volume par heure UTC x DOW
- `viz_hong-kong/scatter_calibration_regimes.html` — Scatter 3D calibration x régimes
- `viz_hong-kong/density_volume.html` — Density 3D trades avec fenêtre asiatique

## Related

- [[../_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/hong-kong|Baseline Hong Kong]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[../capacity-reality-check]]
