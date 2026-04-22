---
title: Shanghai — Quant Deep Dive
city: Shanghai
slug: shanghai
generated: 2026-04-22
n_markets: 280
n_trades: 362233
volume_usdc: 2278289
volume_per_market: 8137
yes_win_rate: 0.0896
xgb_auc: 0.783
kyle_lambda_median: 0.000321
hhi_makers: 0.006754
best_strategy: buy_no_uncertain
sharpe_no_uncertain: 0.903
ev_no_uncertain_pct: 53.6
ev_longshot_yes_pct: 44.3
calibrated: true
serie_too_short: true
tags: [polymarket, weather, shanghai, quant, microstructure, calibrated, short-series]
---

# Shanghai — Quant Deep Dive

## Résumé Exécutif

Shanghai est le marché le **plus jeune** (26 jours) mais avec le **volume par marché le plus élevé** ($8 137/marché). Bien calibré (p=0.345). Seul marché où `is_bracket` est la feature XGBoost #1 (30.9 %). Marché le plus profond : Kyle lambda = 0.000321 (le plus bas des 5), HHI = 0.00675 (le plus compétitif). Anomalie : `buy_yes_longshot` EV **+44.3 %** (unique dans le corpus). Régime Quiet NO (n=185, WR=0 % absolu).

## Chiffres Clés

| Métrique | Valeur |
|---|---|
| Durée historique | **26 jours** (série courte) |
| Volume par marché | **$8 137** (record des 5) |
| YES win rate | **8.96 %** (le plus bas des 5) |
| XGBoost AUC | 0.783 ± 0.138 |
| Brier score | **0.074** (meilleure calibration probabiliste) |
| Kyle lambda médiane | **0.000321** (marché le plus profond) |
| HHI makers | **0.006754** (le plus compétitif) |
| Spread proxy | **57 bps** (le plus étroit) |
| IAT médiane | 28 secondes |
| Whales > $100 | **56.0 %** du volume (record) |
| EV buy_no_uncertain | +53.6 %, Sharpe 0.903 (N=8) |
| EV buy_yes_longshot | **+44.3 %** (unique positif) |
| Régime Quiet WR_YES | **0.0 %** absolu (n=185) |

## Findings Principaux

1. **`is_bracket` feature #1** (30.9 %) — unique parmi les 5 villes
2. **EV longshot +44.3 %** — seul cas positif du corpus (Sharpe=0.049, vol=897 %)
3. **Régime Quiet Bear WR=0 %** sur 185 marchés — signal quasi-certain pour buy_NO
4. **Whale unique** `0xfca3c1` : 1 trade = $68 418 (potentiel insider météo)
5. **Buy ratio 63.5 %** (le plus bas) — marché sell-side plus actif qu'ailleurs
6. **Série trop courte** : Hurst, Half-life, ADF, KPSS non conclusifs — attendre 60 jours

## Edge Opérationnel

- **NO uncertain** : vol_pp < 0.020 → acheter NO (WR=0 % YES sur 185 marchés)
- **NO quiet** : trigger régime vol faible → sizing $20–$50 (marché profond)
- **Timing** : 07h–08h UTC (peak USDC, 15h–16h CST)
- **Oracle whale** : si `0xfca3c1` trade YES → suivre immédiatement
- **Thresholds** : 11–12°C les plus actifs ($738–740K)

## Visualisations

- `viz_shanghai/surface_ev.html`
- `viz_shanghai/scatter_regimes.html`
- `viz_shanghai/density_volume.html`

## Related

- [[_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/shanghai|baseline Shanghai]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[quant-deep-dive/tel-aviv|Tel Aviv QDD]]
- [[quant-deep-dive/miami|Miami QDD]]
