---
name: "London — Quant Deep Dive"
description: "Analyse quantitative complète de London sur les weather markets Polymarket. Tests stat, ML, microstructure, régimes, edges."
type: quant-deep-dive
city: London
slug: london
generated: 2026-04-22
tags:
  - polymarket
  - weather
  - quant
  - london
  - deep-dive
---

# London — Quant Deep Dive

## Résumé exécutif

- **Marchés analysés** : 1,475
- **Période** : 2025-09-30 → 2026-04-11
- **Meilleure stratégie** : `buy_no_favorites` — EV=+3939%, Sharpe=0.999
- **XGBoost AUC** : 0.8213
- **Hurst H** : 0.5564 (trending)
- **Calibration** : NON calibré — biais exploitable

## Findings clés

1. La calibration χ²=121.2 (p=0.00e+00) révèle un biais systématique dans le pricing des marchés London.
2. XGBoost AUC=0.8213 — le signal est fort ex-ante.
3. Kyle's lambda=0.000318 → high_impact — caps recommandés $50-200/trade.
4. Edge `buy_no_favorites` : 12 bets historiques, WR=66.7%.

## Liens vers les outputs

- Rapport complet : `research/outputs/12_quant_deep_dive/london_report.md`
- Viz 1 (surface) : `research/outputs/12_quant_deep_dive/viz_london/viz1_surface_price_ttr_drift.html`
- Viz 2 (clusters) : `research/outputs/12_quant_deep_dive/viz_london/viz2_scatter_regimes.html`
- Viz 3 (densité) : `research/outputs/12_quant_deep_dive/viz_london/viz3_density_hour_price.html`

## Related

- [[../_MOC|MOC Polymarket]]
- [[../odds-trajectories-v2-findings|Odds Trajectories v2 Findings]]
- [[../per-city-deep-dive/london|Deep Dive Baseline London]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 Gates]]
- [[../capacity-reality-check|Capacity Reality Check]]
