---
name: "Dallas — Quant Deep Dive"
description: "Analyse quantitative complète de Dallas sur les weather markets Polymarket. Tests stat, ML, microstructure, régimes, edges."
type: quant-deep-dive
city: Dallas
slug: dallas
generated: 2026-04-22
tags:
  - polymarket
  - weather
  - quant
  - dallas
  - deep-dive
---

# Dallas — Quant Deep Dive

## Résumé exécutif

- **Marchés analysés** : 1,027
- **Période** : 2025-09-30 → 2026-04-11
- **Meilleure stratégie** : `buy_yes_longshot` — EV=+67%, Sharpe=0.063
- **XGBoost AUC** : 0.8406
- **Hurst H** : 0.7072 (trending)
- **Calibration** : NON calibré — biais exploitable

## Findings clés

1. La calibration χ²=19.9 (p=1.06e-02) révèle un biais systématique dans le pricing des marchés Dallas.
2. XGBoost AUC=0.8406 — le signal est fort ex-ante.
3. Kyle's lambda=0.000601 → high_impact — caps recommandés $50-200/trade.
4. Edge `buy_yes_longshot` : 615 bets historiques, WR=3.6%.

## Liens vers les outputs

- Rapport complet : `research/outputs/12_quant_deep_dive/dallas_report.md`
- Viz 1 (surface) : `research/outputs/12_quant_deep_dive/viz_dallas/viz1_surface_price_ttr_drift.html`
- Viz 2 (clusters) : `research/outputs/12_quant_deep_dive/viz_dallas/viz2_scatter_regimes.html`
- Viz 3 (densité) : `research/outputs/12_quant_deep_dive/viz_dallas/viz3_density_hour_price.html`

## Related

- [[../_MOC|MOC Polymarket]]
- [[../odds-trajectories-v2-findings|Odds Trajectories v2 Findings]]
- [[../per-city-deep-dive/dallas|Deep Dive Baseline Dallas]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 Gates]]
- [[../capacity-reality-check|Capacity Reality Check]]
