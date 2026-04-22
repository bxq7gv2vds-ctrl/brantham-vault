---
name: "Atlanta — Quant Deep Dive"
description: "Analyse quantitative complète de Atlanta sur les weather markets Polymarket. Tests stat, ML, microstructure, régimes, edges."
type: quant-deep-dive
city: Atlanta
slug: atlanta
generated: 2026-04-22
tags:
  - polymarket
  - weather
  - quant
  - atlanta
  - deep-dive
---

# Atlanta — Quant Deep Dive

## Résumé exécutif

- **Marchés analysés** : 1,020
- **Période** : 2025-09-30 → 2026-04-11
- **Meilleure stratégie** : `buy_no_favorites` — EV=+2129%, Sharpe=0.573
- **XGBoost AUC** : 0.8242
- **Hurst H** : 0.7175 (trending)
- **Calibration** : NON calibré — biais exploitable

## Findings clés

1. La calibration χ²=54.9 (p=1.27e-08) révèle un biais systématique dans le pricing des marchés Atlanta.
2. XGBoost AUC=0.8242 — le signal est fort ex-ante.
3. Kyle's lambda=0.000504 → high_impact — caps recommandés $50-200/trade.
4. Edge `buy_no_favorites` : 18 bets historiques, WR=33.3%.

## Liens vers les outputs

- Rapport complet : `research/outputs/12_quant_deep_dive/atlanta_report.md`
- Viz 1 (surface) : `research/outputs/12_quant_deep_dive/viz_atlanta/viz1_surface_price_ttr_drift.html`
- Viz 2 (clusters) : `research/outputs/12_quant_deep_dive/viz_atlanta/viz2_scatter_regimes.html`
- Viz 3 (densité) : `research/outputs/12_quant_deep_dive/viz_atlanta/viz3_density_hour_price.html`

## Related

- [[../_MOC|MOC Polymarket]]
- [[../odds-trajectories-v2-findings|Odds Trajectories v2 Findings]]
- [[../per-city-deep-dive/atlanta|Deep Dive Baseline Atlanta]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 Gates]]
- [[../capacity-reality-check|Capacity Reality Check]]
