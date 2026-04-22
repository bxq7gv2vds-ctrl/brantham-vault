---
title: "Quant Deep Dive — Singapore"
slug: singapore
city: Singapore
country: Singapore
timezone: UTC+8
n_markets: 280
n_trades: 153985
volume_usdc: 822743
yes_win_rate: 0.0896
xgb_auc: 0.8785
kyle_lambda_median: 0.000331
garch_persistence: 0.5016
best_edge: buy_yes_uncertain
best_ev_pct: 13.88
asian_volume_pct: 46.2
peak_hour_utc: 6
vol_regime_ratio: 11.87
tags: [polymarket, weather, quant, asian-markets, singapore]
generated: 2026-04-22
---

# Quant Deep Dive — Singapore

> Analyse quantitative profonde des marchés météo Polymarket pour Singapore (Singapore, UTC+8).
> 280 marchés | 153,985 trades | $822,743 USDC | WR YES = 9.0%

## Synthèse exécutive

Singapore présente le profil typique des marchés asiatiques Polymarket : concentration du volume sur la fenêtre UTC 00-07h (46.2% des trades), pic absolu à UTC 06:00 (12,665 trades), et une formation de prix dominée par les participants locaux (SGT).

L'edge principal est **`buy_yes_uncertain`** avec EV/bet = **+13.88%**. Le modèle XGBoost atteint AUC = **0.8785**, signal fort. Kyle lambda médian = 0.000331 (impact élevé — sizing max ~$50).

## Métriques clés (≥30 chiffres)

| Indicateur | Valeur |
|---|---|
| N marchés | 280 |
| N trades | 153,985 |
| Volume USDC | $822,743 |
| YES win rate | 0.0896 |
| NO win rate | 0.9104 |
| Trades / marché | 549.9 |
| Kyle lambda médian | 0.000331 |
| Kyle lambda moyen | 0.000864 |
| GARCH persistence | 0.5016 |
| GARCH omega | 370.9883 |
| GARCH alpha1 | 0.0000 |
| GARCH beta1 | 0.5016 |
| XGB AUC | 0.8785 (±0.0771) |
| XGB Brier | 0.07006 |
| XGB log-loss | 0.2395 |
| Feature top | threshold (0.609) |
| Calibration p | 0.1803 (PASS) |
| Régimes k | 2 (silhouette=0.4569) |
| Régime 0 vol | 0.012660 |
| Régime 1 vol | 0.150236 |
| Ratio vol1/vol0 | 11.87x |
| Régime 0 Hurst | 0.1278 |
| Régime 1 Hurst | 0.2822016694209189 |
| Régime 0 WR YES | 0.0000 |
| Régime 1 WR YES | 0.33783783783783783 |
| Skewness drifts | 1.9408 |
| Kurtosis excess | 4.2580 |
| JB stat | 375.89 |
| Shapiro stat | 0.6924 |
| Bracket NO WR | 0.8899 |
| Bracket NO EV | +2.46% |
| Bracket NO Sharpe | 0.0578 |
| Longshot WR | 0.0167 |
| Longshot EV | -5.56% |
| Asian vol % | 46.20% |
| Asian/Western ratio | 1.70x |
| Peak heure UTC | 06:00 (12,665 trades) |

## Pattern temporel asiatique

Volume UTC 00-07h (fenêtre locale SGT 08-15h) : **46.2%** — Ce ratio est la caractéristique la plus distinctive du cluster asiatique vs villes américaines (ratio inverse occidental > 2x). La liquidité est concentrée au début de session locale, avec un pic qui correspond à l'ouverture des marchés de capitaux asiatiques (Tokyo 09:00 JST = UTC 00:00, Shanghai 09:30 CST = UTC 01:30).

## Edges et recommandations

- **`buy_yes_uncertain`** (meilleur) : EV = +13.88%, WR = 0.500, Sharpe = 0.1216
- **`buy_no_uncertain`** (à éviter) : EV = -5.74%

**Seuil d'entrée bracket NO :** vol 3 premiers trades <= 0.0253, prix >= 0.877
**Fenêtre optimale :** UTC 05:00-07:00

## Visualisations

- `viz_singapore/surface_volume.html` — Surface 3D volume par heure UTC x DOW
- `viz_singapore/scatter_calibration_regimes.html` — Scatter 3D calibration x régimes
- `viz_singapore/density_volume.html` — Density 3D trades avec fenêtre asiatique

## Related

- [[../_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/singapore|Baseline Singapore]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[../capacity-reality-check]]
