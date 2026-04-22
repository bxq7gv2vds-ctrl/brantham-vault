---
name: Quant Deep Dive — Wuhan
description: Analyse quant rigoureuse Wuhan sur 6 mois on-chain. AUC XGBoost ex-ante=0.754, Hurst RS=0.000, χ² calibration=3.8, best strategy=buy_no_uncertain.
type: analysis
project: brantham/polymarket
created: 2026-04-22
tags: [polymarket, quant, deep-dive, wuhan, weather]
priority: high
---

# Wuhan — Quant Deep Dive (6 mois on-chain)

## TL;DR

Wuhan, au confluent du Yangtsé et de la Han, est connue pour ses étés extrêmement chauds et humides (four furnaces également) et ses printemps pluvieux. Sur 209 marchés et $294 108 de volume, YES win rate = **9.1%**. La stratégie `buy_no_uncertain` ressort avec **Sharpe = 0.77 et EV = +58%** sur N=11 — bien plus robuste que Chongqing (N=7) sur la même fenêtre. La calibration est **non rejetée** (p = 0.435) : le marché est bien calibré globalement mais la zone 40-60¢ est sous-évaluée pour NO. XGBoost AUC = **0.754** — le deuxième meilleur après Lucknow. Le GARCH (persistence = 0.502) confirme la structure partagée des villes chinoises. La microstructure est la plus favorable des villes chinoises : Roll spread 158 bps, makers les plus dispersés (HHI = 0.0085).

---

## Rapport complet

Voir : `research/outputs/12_quant_deep_dive/wuhan_report.md`

## Visualisations 3D interactives

`research/outputs/12_quant_deep_dive/viz_wuhan/` (3 HTML Plotly)

## Stats canoniques

- N markets : **209**
- AUC XGBoost (ex-ante) : **0.754**
- Hurst RS : **0.000**
- Calibration χ² : **3.8**
- Best strategy : **buy_no_uncertain**

## Related

- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../per-city-deep-dive/wuhan|Deep dive baseline]]
- [[../STATE-HANDOFF|State Handoff]]
