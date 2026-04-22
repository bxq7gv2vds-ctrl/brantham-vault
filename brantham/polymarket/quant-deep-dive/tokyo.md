---
title: "Quant Deep Dive — Tokyo"
slug: tokyo
city: Tokyo
country: Japan
timezone: UTC+9
n_markets: 307
n_trades: 205411
volume_usdc: 1428808
yes_win_rate: 0.0945
xgb_auc: 0.7545
kyle_lambda_median: 0.000349
garch_persistence: 0.5011
best_edge: buy_no_uncertain
best_ev_pct: 60.18
asian_volume_pct: 50.1
peak_hour_utc: 7
vol_regime_ratio: 0.09
tags: [polymarket, weather, quant, asian-markets, tokyo]
generated: 2026-04-22
---

# Quant Deep Dive — Tokyo

> Analyse quantitative profonde des marchés météo Polymarket pour Tokyo (Japan, UTC+9).
> 307 marchés | 205,411 trades | $1,428,808 USDC | WR YES = 9.4%

## Synthèse exécutive

Tokyo présente le profil typique des marchés asiatiques Polymarket : concentration du volume sur la fenêtre UTC 00-07h (50.1% des trades), pic absolu à UTC 07:00 (22,854 trades), et une formation de prix dominée par les participants locaux (JST).

L'edge principal est **`buy_no_uncertain`** avec EV/bet = **+60.18%**. Le modèle XGBoost atteint AUC = **0.7545**, signal modéré. Kyle lambda médian = 0.000349 (impact élevé — sizing max ~$50).

## Métriques clés (≥30 chiffres)

| Indicateur | Valeur |
|---|---|
| N marchés | 307 |
| N trades | 205,411 |
| Volume USDC | $1,428,808 |
| YES win rate | 0.0945 |
| NO win rate | 0.9055 |
| Trades / marché | 669.1 |
| Kyle lambda médian | 0.000349 |
| Kyle lambda moyen | 0.000875 |
| GARCH persistence | 0.5011 |
| GARCH omega | 401.9742 |
| GARCH alpha1 | 0.0000 |
| GARCH beta1 | 0.5011 |
| XGB AUC | 0.7545 (±0.0838) |
| XGB Brier | 0.10352 |
| XGB log-loss | 0.3382 |
| Feature top | price_open (0.368) |
| Calibration p | 0.0684 (PASS) |
| Régimes k | 2 (silhouette=0.4621) |
| Régime 0 vol | 0.195135 |
| Régime 1 vol | 0.016902 |
| Ratio vol1/vol0 | 0.09x |
| Régime 0 Hurst | 0.3335 |
| Régime 1 Hurst | 0.16090828076090102 |
| Régime 0 WR YES | 0.3867 |
| Régime 1 WR YES | 0.0 |
| Skewness drifts | 1.9697 |
| Kurtosis excess | 4.1275 |
| JB stat | 405.46 |
| Shapiro stat | 0.6913 |
| Bracket NO WR | 0.8876 |
| Bracket NO EV | +3.08% |
| Bracket NO Sharpe | 0.0713 |
| Longshot WR | 0.0314 |
| Longshot EV | -10.99% |
| Asian vol % | 50.12% |
| Asian/Western ratio | 1.89x |
| Peak heure UTC | 07:00 (22,854 trades) |

## Pattern temporel asiatique

Volume UTC 00-07h (fenêtre locale JST 08-15h) : **50.1%** — Ce ratio est la caractéristique la plus distinctive du cluster asiatique vs villes américaines (ratio inverse occidental > 2x). La liquidité est concentrée au début de session locale, avec un pic qui correspond à l'ouverture des marchés de capitaux asiatiques (Tokyo 09:00 JST = UTC 00:00, Shanghai 09:30 CST = UTC 01:30).

## Edges et recommandations

- **`buy_no_uncertain`** (meilleur) : EV = +60.18%, WR = 0.889, Sharpe = 1.0385
- **`buy_yes_uncertain`** (à éviter) : EV = -72.90%

**Seuil d'entrée bracket NO :** vol 3 premiers trades <= 0.3903, prix >= 0.874
**Fenêtre optimale :** UTC 06:00-08:00

## Visualisations

- `viz_tokyo/surface_volume.html` — Surface 3D volume par heure UTC x DOW
- `viz_tokyo/scatter_calibration_regimes.html` — Scatter 3D calibration x régimes
- `viz_tokyo/density_volume.html` — Density 3D trades avec fenêtre asiatique

## Related

- [[../_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/tokyo|Baseline Tokyo]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[../capacity-reality-check]]
