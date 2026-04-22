---
name: "Seoul — Quant Deep Dive"
description: "Analyse quantitative complète de Seoul sur les weather markets Polymarket. Tests stat, ML, microstructure, régimes, edges."
type: quant-deep-dive
city: Seoul
slug: seoul
generated: 2026-04-22
tags:
  - polymarket
  - weather
  - quant
  - seoul
  - deep-dive
---

# Seoul — Quant Deep Dive

## Résumé exécutif

- **Marchés analysés** : 1,013
- **Période** : 2025-09-30 → 2026-04-11
- **Meilleure stratégie** : `buy_no_favorites` — EV=+309%, Sharpe=0.372
- **XGBoost AUC** : 0.7944
- **Hurst H** : 0.6202 (trending)
- **Calibration** : NON calibré — biais exploitable

## Findings clés

1. La calibration χ²=23.2 (p=1.56e-03) révèle un biais systématique dans le pricing des marchés Seoul.
2. XGBoost AUC=0.7944 — le signal est modéré ex-ante.
3. Kyle's lambda=0.000267 → high_impact — caps recommandés $50-200/trade.
4. Edge `buy_no_favorites` : 8 bets historiques, WR=25.0%.

## Liens vers les outputs

- Rapport complet : `research/outputs/12_quant_deep_dive/seoul_report.md`
- Viz 1 (surface) : `research/outputs/12_quant_deep_dive/viz_seoul/viz1_surface_price_ttr_drift.html`
- Viz 2 (clusters) : `research/outputs/12_quant_deep_dive/viz_seoul/viz2_scatter_regimes.html`
- Viz 3 (densité) : `research/outputs/12_quant_deep_dive/viz_seoul/viz3_density_hour_price.html`

## Related

- [[../_MOC|MOC Polymarket]]
- [[../odds-trajectories-v2-findings|Odds Trajectories v2 Findings]]
- [[../per-city-deep-dive/seoul|Deep Dive Baseline Seoul]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 Gates]]
- [[../capacity-reality-check|Capacity Reality Check]]
