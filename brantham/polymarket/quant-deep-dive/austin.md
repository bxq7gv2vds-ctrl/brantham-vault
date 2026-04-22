---
title: "Quant Deep Dive — Austin"
date: 2026-04-22
slug: austin
type: quant-deep-dive
status: high-predictability
tags:
  - polymarket
  - weather-markets
  - quant
  - austin
  - sun-belt
xgb_auc: 0.7837
skill_score_pct: 56.7
yes_win_rate: 0.0909
n_markets: 165
n_trades: 73024
volume_usdc: 232415
best_edge: buy_no_brackets
ev_per_bet_pct: 1.0419
garch_persistence: 0.5020
---

# Quant Deep Dive — Austin

> Analyse quantitative hedge-fund-grade des marchés météo Polymarket. 165 marchés, 73,024 trades, $232,415 USDC.

## Résumé exécutif

- **XGB AUC**: 0.7837 (skill 56.7% au-dessus du hasard)
- **YES WR réel**: 9.1% — structure NO-dominant confirmée
- **Best edge**: `buy_no_brackets` — EV=1.04%/bet
- **GARCH persistence**: 0.5020
- **Climat**: Sun Belt semi-arid/subtropical — Hot summers, mild winters, rare frost, low precip variability
- **Prédictibilité vs diversité climatique**: AUC élevée cohérente avec faible variance climatique

## Métriques propriétaires (microstructure custom)

| VWPDI | RTF | BNER | HLCI | LSCG |
|---|---|---|---|---|
| -1.540 | 0.188 | 0.026 | 0.04611 | 0.022 |

## Recommandation principale

Stratégie `buy_no_brackets` avec seuils :
- `price_open` ≥ 0.82, TTR ≥ 0.75
- Position max $50 (Kyle λ contrôlé)
- Filtre régime : vol médiane ≤ 0.0472

## Fichiers

- Rapport complet : `research/outputs/12_quant_deep_dive/austin_report.md`
- Viz 3D : `research/outputs/12_quant_deep_dive/viz_austin/`
  - `surface_vol_ttr_price.html`
  - `scatter3d_drift_vol_hurst.html`
  - `density_hour_price_volume.html`

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectoires v2 findings]]
- [[../per-city-deep-dive/austin|Baseline per-city deep dive]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 gates]]
- [[../dedup-bug-p-and-l-inflation|Dédup bug P&L inflation]]
