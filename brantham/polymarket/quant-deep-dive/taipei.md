---
title: "Quant Deep Dive — Taipei"
slug: taipei
city: Taipei
country: Taiwan
timezone: UTC+8
n_markets: 253
n_trades: 104476
volume_usdc: 643221
yes_win_rate: 0.0916
xgb_auc: 0.5654
kyle_lambda_median: 0.000916
garch_persistence: 0.0951
best_edge: buy_yes_longshot
best_ev_pct: 155.45
asian_volume_pct: 46.7
peak_hour_utc: 4
vol_regime_ratio: 7.97
tags: [polymarket, weather, quant, asian-markets, taipei]
generated: 2026-04-22
---

# Quant Deep Dive — Taipei

> Analyse quantitative profonde des marchés météo Polymarket pour Taipei (Taiwan, UTC+8).
> 253 marchés | 104,476 trades | $643,221 USDC | WR YES = 9.2%

## Synthèse exécutive

Taipei présente le profil typique des marchés asiatiques Polymarket : concentration du volume sur la fenêtre UTC 00-07h (46.7% des trades), pic absolu à UTC 04:00 (7,926 trades), et une formation de prix dominée par les participants locaux (CST).

L'edge principal est **`buy_yes_longshot`** avec EV/bet = **+155.45%**. Le modèle XGBoost atteint AUC = **0.5654**, signal faible. Kyle lambda médian = 0.000916 (impact élevé — sizing max ~$50).

## Métriques clés (≥30 chiffres)

| Indicateur | Valeur |
|---|---|
| N marchés | 253 |
| N trades | 104,476 |
| Volume USDC | $643,221 |
| YES win rate | 0.0916 |
| NO win rate | 0.9084 |
| Trades / marché | 412.9 |
| Kyle lambda médian | 0.000916 |
| Kyle lambda moyen | 0.001452 |
| GARCH persistence | 0.0951 |
| GARCH omega | 954.7984 |
| GARCH alpha1 | 0.0951 |
| GARCH beta1 | 0.0000 |
| XGB AUC | 0.5654 (±0.1491) |
| XGB Brier | 0.09339 |
| XGB log-loss | 0.3491 |
| Feature top | is_bracket (0.369) |
| Calibration p | 0.0000 (FAIL) |
| Régimes k | 4 (silhouette=0.3349) |
| Régime 0 vol | 0.012708 |
| Régime 1 vol | 0.101225 |
| Ratio vol1/vol0 | 7.97x |
| Régime 0 Hurst | 0.1210 |
| Régime 1 Hurst | 0.25628466131805366 |
| Régime 0 WR YES | 0.0000 |
| Régime 1 WR YES | 0.0 |
| Skewness drifts | 1.3077 |
| Kurtosis excess | 3.7962 |
| JB stat | 215.41 |
| Shapiro stat | 0.7343 |
| Bracket NO WR | 0.9175 |
| Bracket NO EV | +33.46% |
| Bracket NO Sharpe | 0.1398 |
| Longshot WR | 0.0645 |
| Longshot EV | +155.45% |
| Asian vol % | 46.72% |
| Asian/Western ratio | 1.70x |
| Peak heure UTC | 04:00 (7,926 trades) |

## Pattern temporel asiatique

Volume UTC 00-07h (fenêtre locale CST 08-15h) : **46.7%** — Ce ratio est la caractéristique la plus distinctive du cluster asiatique vs villes américaines (ratio inverse occidental > 2x). La liquidité est concentrée au début de session locale, avec un pic qui correspond à l'ouverture des marchés de capitaux asiatiques (Tokyo 09:00 JST = UTC 00:00, Shanghai 09:30 CST = UTC 01:30).

## Edges et recommandations

- **`buy_yes_longshot`** (meilleur) : EV = +155.45%, WR = 0.065, Sharpe = 0.1339
- **`buy_yes_uncertain`** (à éviter) : EV = -73.05%

**Seuil d'entrée bracket NO :** vol 3 premiers trades <= 0.0254, prix >= 0.862
**Fenêtre optimale :** UTC 03:00-05:00

## Visualisations

- `viz_taipei/surface_volume.html` — Surface 3D volume par heure UTC x DOW
- `viz_taipei/scatter_calibration_regimes.html` — Scatter 3D calibration x régimes
- `viz_taipei/density_volume.html` — Density 3D trades avec fenêtre asiatique

## Related

- [[../_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/taipei|Baseline Taipei]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[../capacity-reality-check]]
