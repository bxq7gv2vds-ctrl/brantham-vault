---
title: "Quant Deep Dive — Shenzhen"
slug: shenzhen
city: Shenzhen
country: China
timezone: UTC+8
n_markets: 209
n_trades: 111021
volume_usdc: 906960
yes_win_rate: 0.0909
xgb_auc: 0.7924
kyle_lambda_median: 0.000355
garch_persistence: 0.5018
best_edge: buy_yes_longshot
best_ev_pct: 64.44
asian_volume_pct: 48.3
peak_hour_utc: 7
vol_regime_ratio: 10.69
tags: [polymarket, weather, quant, asian-markets, shenzhen]
generated: 2026-04-22
---

# Quant Deep Dive — Shenzhen

> Analyse quantitative profonde des marchés météo Polymarket pour Shenzhen (China, UTC+8).
> 209 marchés | 111,021 trades | $906,960 USDC | WR YES = 9.1%

## Synthèse exécutive

Shenzhen présente le profil typique des marchés asiatiques Polymarket : concentration du volume sur la fenêtre UTC 00-07h (48.3% des trades), pic absolu à UTC 07:00 (10,079 trades), et une formation de prix dominée par les participants locaux (CST).

L'edge principal est **`buy_yes_longshot`** avec EV/bet = **+64.44%**. Le modèle XGBoost atteint AUC = **0.7924**, signal modéré. Kyle lambda médian = 0.000355 (impact élevé — sizing max ~$50).

## Métriques clés (≥30 chiffres)

| Indicateur | Valeur |
|---|---|
| N marchés | 209 |
| N trades | 111,021 |
| Volume USDC | $906,960 |
| YES win rate | 0.0909 |
| NO win rate | 0.9091 |
| Trades / marché | 531.2 |
| Kyle lambda médian | 0.000355 |
| Kyle lambda moyen | 0.000877 |
| GARCH persistence | 0.5018 |
| GARCH omega | 400.7433 |
| GARCH alpha1 | 0.0000 |
| GARCH beta1 | 0.5018 |
| XGB AUC | 0.7924 (±0.0940) |
| XGB Brier | 0.08289 |
| XGB log-loss | 0.2837 |
| Feature top | threshold (0.583) |
| Calibration p | 0.2755 (PASS) |
| Régimes k | 2 (silhouette=0.4470) |
| Régime 0 vol | 0.018159 |
| Régime 1 vol | 0.194173 |
| Ratio vol1/vol0 | 10.69x |
| Régime 0 Hurst | 0.1504 |
| Régime 1 Hurst | 0.3135690137324286 |
| Régime 0 WR YES | 0.0000 |
| Régime 1 WR YES | 0.38 |
| Skewness drifts | 2.1877 |
| Kurtosis excess | 4.9710 |
| JB stat | 367.00 |
| Shapiro stat | 0.6633 |
| Bracket NO WR | 0.8947 |
| Bracket NO EV | +1.77% |
| Bracket NO Sharpe | 0.0451 |
| Longshot WR | 0.0584 |
| Longshot EV | +64.44% |
| Asian vol % | 48.26% |
| Asian/Western ratio | 1.99x |
| Peak heure UTC | 07:00 (10,079 trades) |

## Pattern temporel asiatique

Volume UTC 00-07h (fenêtre locale CST 08-15h) : **48.3%** — Ce ratio est la caractéristique la plus distinctive du cluster asiatique vs villes américaines (ratio inverse occidental > 2x). La liquidité est concentrée au début de session locale, avec un pic qui correspond à l'ouverture des marchés de capitaux asiatiques (Tokyo 09:00 JST = UTC 00:00, Shanghai 09:30 CST = UTC 01:30).

## Edges et recommandations

- **`buy_yes_longshot`** (meilleur) : EV = +64.44%, WR = 0.058, Sharpe = 0.0688
- **`buy_yes_uncertain`** (à éviter) : EV = -20.00%

**Seuil d'entrée bracket NO :** vol 3 premiers trades <= 0.0363, prix >= 0.887
**Fenêtre optimale :** UTC 06:00-08:00

## Visualisations

- `viz_shenzhen/surface_volume.html` — Surface 3D volume par heure UTC x DOW
- `viz_shenzhen/scatter_calibration_regimes.html` — Scatter 3D calibration x régimes
- `viz_shenzhen/density_volume.html` — Density 3D trades avec fenêtre asiatique

## Related

- [[../_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/shenzhen|Baseline Shenzhen]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[../capacity-reality-check]]
