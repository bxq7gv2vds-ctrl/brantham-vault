---
title: "Quant Deep Dive — Denver"
date: 2026-04-22
slug: denver
type: quant-deep-dive
status: low-predictability
tags:
  - polymarket
  - weather-markets
  - quant
  - denver
  - sun-belt
xgb_auc: 0.5420
skill_score_pct: 8.4
yes_win_rate: 0.0736
n_markets: 175
n_trades: 64788
volume_usdc: 270895
best_edge: buy_yes_longshot
ev_per_bet_pct: 4.7697
garch_persistence: 0.9804
---

# Quant Deep Dive — Denver

> Analyse quantitative hedge-fund-grade des marchés météo Polymarket. 175 marchés, 64,788 trades, $270,895 USDC.

## Résumé exécutif

- **XGB AUC**: 0.5420 (skill 8.4% au-dessus du hasard)
- **YES WR réel**: 7.4% — structure NO-dominant confirmée
- **Best edge**: `buy_yes_longshot` — EV=4.77%/bet
- **GARCH persistence**: 0.9804
- **Climat**: High-altitude semi-arid continental — Wide swings: Chinook winds, blizzards, 300 sunny days/yr — HIGH variance
- **Prédictibilité vs diversité climatique**: AUC modérée/faible → haute variabilité climatique réduit l'edge ex-ante

## Métriques propriétaires (microstructure custom)

| VWPDI | RTF | BNER | HLCI | LSCG |
|---|---|---|---|---|
| -1.338 | 0.294 | 0.141 | 0.04961 | 0.012 |

## Recommandation principale

Stratégie `buy_no_brackets` avec seuils :
- `price_open` ≥ 0.82, TTR ≥ 0.75
- Position max $50 (Kyle λ contrôlé)
- Filtre régime : vol médiane ≤ 0.0593

## Fichiers

- Rapport complet : `research/outputs/12_quant_deep_dive/denver_report.md`
- Viz 3D : `research/outputs/12_quant_deep_dive/viz_denver/`
  - `surface_vol_ttr_price.html`
  - `scatter3d_drift_vol_hurst.html`
  - `density_hour_price_volume.html`

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectoires v2 findings]]
- [[../per-city-deep-dive/denver|Baseline per-city deep dive]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 gates]]
- [[../dedup-bug-p-and-l-inflation|Dédup bug P&L inflation]]
