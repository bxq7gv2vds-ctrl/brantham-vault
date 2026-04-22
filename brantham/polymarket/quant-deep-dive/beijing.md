---
title: "Quant Deep Dive — Beijing"
slug: beijing
city: Beijing
country: China
timezone: UTC+8
n_markets: 209
n_trades: 111000
volume_usdc: 545641
yes_win_rate: 0.0922
xgb_auc: 0.8514
kyle_lambda_median: 0.000180
garch_persistence: 0.5017
best_edge: buy_no_uncertain
best_ev_pct: 38.31
asian_volume_pct: 47.8
peak_hour_utc: 7
vol_regime_ratio: 7.37
tags: [polymarket, weather, quant, asian-markets, beijing]
generated: 2026-04-22
---

# Quant Deep Dive — Beijing

> Analyse quantitative profonde des marchés météo Polymarket pour Beijing (China, UTC+8).
> 209 marchés | 111,000 trades | $545,641 USDC | WR YES = 9.2%

## Synthèse exécutive

Beijing présente le profil typique des marchés asiatiques Polymarket : concentration du volume sur la fenêtre UTC 00-07h (47.8% des trades), pic absolu à UTC 07:00 (10,566 trades), et une formation de prix dominée par les participants locaux (CST).

L'edge principal est **`buy_no_uncertain`** avec EV/bet = **+38.31%**. Le modèle XGBoost atteint AUC = **0.8514**, signal fort. Kyle lambda médian = 0.000180 (impact élevé — sizing max ~$50).

## Métriques clés (≥30 chiffres)

| Indicateur | Valeur |
|---|---|
| N marchés | 209 |
| N trades | 111,000 |
| Volume USDC | $545,641 |
| YES win rate | 0.0922 |
| NO win rate | 0.9078 |
| Trades / marché | 531.1 |
| Kyle lambda médian | 0.000180 |
| Kyle lambda moyen | 0.001402 |
| GARCH persistence | 0.5017 |
| GARCH omega | 352.2101 |
| GARCH alpha1 | 0.0000 |
| GARCH beta1 | 0.5017 |
| XGB AUC | 0.8514 (±0.0720) |
| XGB Brier | 0.06999 |
| XGB log-loss | 0.2376 |
| Feature top | price_open (0.595) |
| Calibration p | 0.1059 (PASS) |
| Régimes k | 2 (silhouette=0.3971) |
| Régime 0 vol | 0.021361 |
| Régime 1 vol | 0.157421 |
| Ratio vol1/vol0 | 7.37x |
| Régime 0 Hurst | 0.1413 |
| Régime 1 Hurst | 0.32438480097204125 |
| Régime 0 WR YES | 0.0000 |
| Régime 1 WR YES | 0.31666666666666665 |
| Skewness drifts | 1.9802 |
| Kurtosis excess | 4.3163 |
| JB stat | 287.15 |
| Shapiro stat | 0.6986 |
| Bracket NO WR | 0.8869 |
| Bracket NO EV | +2.44% |
| Bracket NO Sharpe | 0.0589 |
| Longshot WR | 0.0085 |
| Longshot EV | -87.89% |
| Asian vol % | 47.82% |
| Asian/Western ratio | 1.98x |
| Peak heure UTC | 07:00 (10,566 trades) |

## Pattern temporel asiatique

Volume UTC 00-07h (fenêtre locale CST 08-15h) : **47.8%** — Ce ratio est la caractéristique la plus distinctive du cluster asiatique vs villes américaines (ratio inverse occidental > 2x). La liquidité est concentrée au début de session locale, avec un pic qui correspond à l'ouverture des marchés de capitaux asiatiques (Tokyo 09:00 JST = UTC 00:00, Shanghai 09:30 CST = UTC 01:30).

## Edges et recommandations

- **`buy_no_uncertain`** (meilleur) : EV = +38.31%, WR = 0.714, Sharpe = 0.4361
- **`buy_yes_longshot`** (à éviter) : EV = -87.89%

**Seuil d'entrée bracket NO :** vol 3 premiers trades <= 0.0427, prix >= 0.867
**Fenêtre optimale :** UTC 06:00-08:00

## Visualisations

- `viz_beijing/surface_volume.html` — Surface 3D volume par heure UTC x DOW
- `viz_beijing/scatter_calibration_regimes.html` — Scatter 3D calibration x régimes
- `viz_beijing/density_volume.html` — Density 3D trades avec fenêtre asiatique

## Related

- [[../_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/beijing|Baseline Beijing]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[../capacity-reality-check]]
