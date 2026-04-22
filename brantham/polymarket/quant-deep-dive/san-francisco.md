---
title: "Quant Deep Dive — San Francisco"
date: 2026-04-22
slug: san-francisco
type: quant-deep-dive
status: high-predictability
tags:
  - polymarket
  - weather-markets
  - quant
  - san-francisco
  - sun-belt
xgb_auc: 0.7994
skill_score_pct: 59.9
yes_win_rate: 0.0802
n_markets: 165
n_trades: 71830
volume_usdc: 300263
best_edge: buy_no_brackets
ev_per_bet_pct: 3.4275
garch_persistence: 0.5037
---

# Quant Deep Dive — San Francisco

> Analyse quantitative hedge-fund-grade des marchés météo Polymarket. 165 marchés, 71,830 trades, $300,263 USDC.

## Résumé exécutif

- **XGB AUC**: 0.7994 (skill 59.9% au-dessus du hasard)
- **YES WR réel**: 8.0% — structure NO-dominant confirmée
- **Best edge**: `buy_no_brackets` — EV=3.43%/bet
- **GARCH persistence**: 0.5037
- **Climat**: Cool maritime Mediterranean — Persistent marine layer, narrow range, strong micro-climate patchwork
- **Prédictibilité vs diversité climatique**: AUC élevée cohérente avec faible variance climatique

## Métriques propriétaires (microstructure custom)

| VWPDI | RTF | BNER | HLCI | LSCG |
|---|---|---|---|---|
| -1.317 | 0.145 | 0.111 | 0.04569 | 0.031 |

## Recommandation principale

Stratégie `buy_no_brackets` avec seuils :
- `price_open` ≥ 0.82, TTR ≥ 0.75
- Position max $50 (Kyle λ contrôlé)
- Filtre régime : vol médiane ≤ 0.0432

## Fichiers

- Rapport complet : `research/outputs/12_quant_deep_dive/san-francisco_report.md`
- Viz 3D : `research/outputs/12_quant_deep_dive/viz_san-francisco/`
  - `surface_vol_ttr_price.html`
  - `scatter3d_drift_vol_hurst.html`
  - `density_hour_price_volume.html`

## Related

- [[../_MOC|Polymarket MOC]]
- [[../odds-trajectories-v2-findings|Trajectoires v2 findings]]
- [[../per-city-deep-dive/san-francisco|Baseline per-city deep dive]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 gates]]
- [[../dedup-bug-p-and-l-inflation|Dédup bug P&L inflation]]
