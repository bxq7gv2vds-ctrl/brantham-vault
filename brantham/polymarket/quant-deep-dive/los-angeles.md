---
title: "Quant Deep Dive — Los Angeles"
date: 2026-04-22
slug: los-angeles
type: quant-deep-dive
status: moderate-predictability
tags:
  - polymarket
  - weather-markets
  - quant
  - los-angeles
  - sun-belt
xgb_auc: 0.6795
skill_score_pct: 35.9
yes_win_rate: 0.0909
n_markets: 179
n_trades: 89055
volume_usdc: 294285
best_edge: buy_yes_longshot
ev_per_bet_pct: 14.9743
garch_persistence: 0.9615
---

# Quant Deep Dive — Los Angeles

> Analyse quantitative hedge-fund-grade des marchés météo Polymarket. 179 marchés, 89,055 trades, $294,285 USDC.

## Résumé exécutif

- **XGB AUC**: 0.6795 (skill 35.9% au-dessus du hasard)
- **YES WR réel**: 9.1% — structure NO-dominant confirmée
- **Best edge**: `buy_yes_longshot` — EV=14.97%/bet
- **GARCH persistence**: 0.9615
- **Climat**: Mediterranean / Pacific coast — Extremely low variance: 18-27°C year-round, minimal rain events
- **Prédictibilité vs diversité climatique**: AUC modérée/faible → haute variabilité climatique réduit l'edge ex-ante

## Métriques propriétaires (microstructure custom)

| VWPDI | RTF | BNER | HLCI | LSCG |
|---|---|---|---|---|
| -1.148 | 0.257 | 0.111 | 0.04968 | 0.002 |

## Recommandation principale

Stratégie `buy_no_brackets` avec seuils :
- `price_open` ≥ 0.82, TTR ≥ 0.75
- Position max $50 (Kyle λ contrôlé)
- Filtre régime : vol médiane ≤ 0.0614

## Fichiers

- Rapport complet : `research/outputs/12_quant_deep_dive/los-angeles_report.md`
- Viz 3D : `research/outputs/12_quant_deep_dive/viz_los-angeles/`
  - `surface_vol_ttr_price.html`
  - `scatter3d_drift_vol_hurst.html`
  - `density_hour_price_volume.html`

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectoires v2 findings]]
- [[../per-city-deep-dive/los-angeles|Baseline per-city deep dive]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 gates]]
- [[../dedup-bug-p-and-l-inflation|Dédup bug P&L inflation]]
