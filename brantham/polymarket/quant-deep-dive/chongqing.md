---
name: Quant Deep Dive — Chongqing
description: Analyse quant rigoureuse Chongqing sur 6 mois on-chain. AUC XGBoost ex-ante=0.689, Hurst RS=0.000, χ² calibration=10.1, best strategy=buy_no_uncertain.
type: analysis
project: brantham/polymarket
created: 2026-04-22
tags: [polymarket, quant, deep-dive, chongqing, weather]
priority: high
---

# Chongqing — Quant Deep Dive (6 mois on-chain)

## TL;DR

Chongqing est la "montagne de feu" de Chine — une des villes les plus chaudes en été (four furnaces), avec un relief accidenté et un microclimat distinct du Sichuan voisin. Sur 209 marchés et $312 961 de volume, YES win rate = **9.1%**. L'anomalie statistique majeure : en zone incertaine (40-60¢), la stratégie `buy_no_uncertain` génère un **Sharpe de 8.22** et **EV +94.7%** sur N=7 — le Sharpe le plus élevé des 5 villes, mais aussi le plus fragile (N=7). La calibration est rejetée (Chi-2 p=0.039) avec un biais net : les marchés à 50-60¢ ont un YES WR de **0%** (vs attendu 55%). XGBoost AUC = **0.689**. Structure GARCH identique à Chengdu (persistence = 0.501). Chongqing est la ville avec le plus grand potentiel si l'anomalie uncertain zone se confirme.

---

## Rapport complet

Voir : `research/outputs/12_quant_deep_dive/chongqing_report.md`

## Visualisations 3D interactives

`research/outputs/12_quant_deep_dive/viz_chongqing/` (3 HTML Plotly)

## Stats canoniques

- N markets : **209**
- AUC XGBoost (ex-ante) : **0.689**
- Hurst RS : **0.000**
- Calibration χ² : **10.1**
- Best strategy : **buy_no_uncertain**

## Related

- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../per-city-deep-dive/chongqing|Deep dive baseline]]
- [[../STATE-HANDOFF|State Handoff]]
