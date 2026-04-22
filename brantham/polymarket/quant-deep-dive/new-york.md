---
name: "New York — Quant Deep Dive"
description: "Analyse quantitative complète de New York sur les weather markets Polymarket. Tests stat, ML, microstructure, régimes, edges."
type: quant-deep-dive
city: New York
slug: new-york
generated: 2026-04-22
tags:
  - polymarket
  - weather
  - quant
  - new-york
  - deep-dive
---

# New York — Quant Deep Dive

## Résumé exécutif

- **Marchés analysés** : 1,486
- **Période** : 2025-09-30 → 2026-04-11
- **Meilleure stratégie** : `buy_no_favorites` — EV=+2237%, Sharpe=0.788
- **XGBoost AUC** : 0.8196
- **Hurst H** : 0.4515 (random_walk)
- **Calibration** : NON calibré — biais exploitable

## Findings clés

1. La calibration χ²=102.5 (p=0.00e+00) révèle un biais systématique dans le pricing des marchés New York.
2. XGBoost AUC=0.8196 — le signal est modéré ex-ante.
3. Kyle's lambda=0.000454 → high_impact — caps recommandés $50-200/trade.
4. Edge `buy_no_favorites` : 12 bets historiques, WR=58.3%.

## Liens vers les outputs

- Rapport complet : `research/outputs/12_quant_deep_dive/new-york_report.md`
- Viz 1 (surface) : `research/outputs/12_quant_deep_dive/viz_new-york/viz1_surface_price_ttr_drift.html`
- Viz 2 (clusters) : `research/outputs/12_quant_deep_dive/viz_new-york/viz2_scatter_regimes.html`
- Viz 3 (densité) : `research/outputs/12_quant_deep_dive/viz_new-york/viz3_density_hour_price.html`

## Related

- [[../_MOC|MOC Polymarket]]
- [[../odds-trajectories-v2-findings|Odds Trajectories v2 Findings]]
- [[../per-city-deep-dive/new-york|Deep Dive Baseline New York]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 Gates]]
- [[../capacity-reality-check|Capacity Reality Check]]
