---
title: "Quant Deep Dive — Mexico City"
date: 2026-04-22
slug: mexico-city
type: quant-deep-dive
status: low-predictability
tags:
  - polymarket
  - weather-markets
  - quant
  - mexico-city
  - sun-belt
xgb_auc: 0.5529
skill_score_pct: 10.6
yes_win_rate: 0.0909
n_markets: 99
n_trades: 30882
volume_usdc: 79831
best_edge: buy_no_brackets
ev_per_bet_pct: 3.1199
garch_persistence: N/A
---

# Quant Deep Dive — Mexico City

> Analyse quantitative hedge-fund-grade des marchés météo Polymarket. 99 marchés, 30,882 trades, $79,831 USDC.

## Résumé exécutif

- **XGB AUC**: 0.5529 (skill 10.6% au-dessus du hasard)
- **YES WR réel**: 9.1% — structure NO-dominant confirmée
- **Best edge**: `buy_no_brackets` — EV=3.12%/bet
- **GARCH persistence**: N/A
- **Climat**: Highland tropical (2240m a.s.l.) — Altitude = no extreme heat; strong wet/dry seasonal binary; unique regime
- **Prédictibilité vs diversité climatique**: AUC modérée/faible → haute variabilité climatique réduit l'edge ex-ante

## Métriques propriétaires (microstructure custom)

| VWPDI | RTF | BNER | HLCI | LSCG |
|---|---|---|---|---|
| -1.206 | 0.283 | 0.082 | 0.05156 | 0.015 |

## Recommandation principale

Stratégie `buy_no_brackets` avec seuils :
- `price_open` ≥ 0.82, TTR ≥ 0.75
- Position max $50 (Kyle λ contrôlé)
- Filtre régime : vol médiane ≤ 0.0463

## Fichiers

- Rapport complet : `research/outputs/12_quant_deep_dive/mexico-city_report.md`
- Viz 3D : `research/outputs/12_quant_deep_dive/viz_mexico-city/`
  - `surface_vol_ttr_price.html`
  - `scatter3d_drift_vol_hurst.html`
  - `density_hour_price_volume.html`

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectoires v2 findings]]
- [[../per-city-deep-dive/mexico-city|Baseline per-city deep dive]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 gates]]
- [[../dedup-bug-p-and-l-inflation|Dédup bug P&L inflation]]
