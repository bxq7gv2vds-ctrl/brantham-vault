---
title: "Quant Deep Dive — Houston"
date: 2026-04-22
slug: houston
type: quant-deep-dive
status: moderate-predictability
tags:
  - polymarket
  - weather-markets
  - quant
  - houston
  - sun-belt
xgb_auc: 0.7243
skill_score_pct: 44.9
yes_win_rate: 0.0854
n_markets: 165
n_trades: 63118
volume_usdc: 211976
best_edge: buy_no_brackets
ev_per_bet_pct: 1.1790
garch_persistence: 0.5009
---

# Quant Deep Dive — Houston

> Analyse quantitative hedge-fund-grade des marchés météo Polymarket. 165 marchés, 63,118 trades, $211,976 USDC.

## Résumé exécutif

- **XGB AUC**: 0.7243 (skill 44.9% au-dessus du hasard)
- **YES WR réel**: 8.5% — structure NO-dominant confirmée
- **Best edge**: `buy_no_brackets` — EV=1.18%/bet
- **GARCH persistence**: 0.5009
- **Climat**: Humid subtropical / Gulf Coast — Tropical storms, high humidity, narrow temperature window
- **Prédictibilité vs diversité climatique**: AUC modérée/faible → haute variabilité climatique réduit l'edge ex-ante

## Métriques propriétaires (microstructure custom)

| VWPDI | RTF | BNER | HLCI | LSCG |
|---|---|---|---|---|
| -1.201 | 0.236 | 0.031 | 0.04798 | 0.032 |

## Recommandation principale

Stratégie `buy_no_brackets` avec seuils :
- `price_open` ≥ 0.82, TTR ≥ 0.75
- Position max $50 (Kyle λ contrôlé)
- Filtre régime : vol médiane ≤ 0.0429

## Fichiers

- Rapport complet : `research/outputs/12_quant_deep_dive/houston_report.md`
- Viz 3D : `research/outputs/12_quant_deep_dive/viz_houston/`
  - `surface_vol_ttr_price.html`
  - `scatter3d_drift_vol_hurst.html`
  - `density_hour_price_volume.html`

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectoires v2 findings]]
- [[../per-city-deep-dive/houston|Baseline per-city deep dive]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 gates]]
- [[../dedup-bug-p-and-l-inflation|Dédup bug P&L inflation]]
