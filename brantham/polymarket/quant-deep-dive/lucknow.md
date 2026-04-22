---
name: Quant Deep Dive — Lucknow
description: Analyse quant rigoureuse Lucknow sur 6 mois on-chain. AUC XGBoost ex-ante=0.894, Hurst RS=0.941, χ² calibration=12.8, best strategy=buy_yes_uncertain.
type: analysis
project: brantham/polymarket
created: 2026-04-22
tags: [polymarket, quant, deep-dive, lucknow, weather]
priority: high
---

# Lucknow — Quant Deep Dive (6 mois on-chain)

## TL;DR

Lucknow est la ville **indienne unique** du dataset — 352 marchés, $1.13M de volume on-chain, YES win rate à **9.7%** confirmant un biais climatique extrême (chaleur sèche du Gangetic Plain). La liquidité est **biphasique** : 82.7% des marchés font moins de $1 000 de volume mais 10% des marchés concentrent 91.6% du volume total (top traders géants). Le XGBoost ex-ante sort un AUC de **0.894** — le meilleur des 5 villes — ce qui révèle une prédictabilité structurelle exploitable. L'illiquidité crée des **spreads Roll à 0.63 cent médian** et un Kyle λ de 0.074% par $1 tradé, rendant l'entrée possible avec des positions ≤$15 sans signal de marché visible. Edge principal : `buy_no_brackets` (+3.45% EV, Sharpe 0.12) avec confirmation Hurst H=0.94 (trending fort).

---

## Rapport complet

Voir : `research/outputs/12_quant_deep_dive/lucknow_report.md`

## Visualisations 3D interactives

`research/outputs/12_quant_deep_dive/viz_lucknow/` (3 HTML Plotly)

## Stats canoniques

- N markets : **352**
- AUC XGBoost (ex-ante) : **0.894**
- Hurst RS : **0.941**
- Calibration χ² : **12.8**
- Best strategy : **buy_yes_uncertain**

## Related

- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../per-city-deep-dive/lucknow|Deep dive baseline]]
- [[../STATE-HANDOFF|State Handoff]]
