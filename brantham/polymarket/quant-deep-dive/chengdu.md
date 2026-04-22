---
name: Quant Deep Dive — Chengdu
description: Analyse quant rigoureuse Chengdu sur 6 mois on-chain. AUC XGBoost ex-ante=0.701, Hurst RS=0.000, χ² calibration=3.6, best strategy=buy_yes_longshot.
type: analysis
project: brantham/polymarket
created: 2026-04-22
tags: [polymarket, quant, deep-dive, chengdu, weather]
priority: high
---

# Chengdu — Quant Deep Dive (6 mois on-chain)

## TL;DR

Chengdu est une ville sub-tropicale du Sichuan, enclavée dans un bassin avec une couverture nuageuse chronique et des précipitations fréquentes. Sur 198 marchés et $294 767 de volume, le YES win rate est de **8.6%** — le plus bas des 5 villes. L'anomalie majeure est dans l'edge `buy_yes_longshot` : **EV = +182.4%** sur 131 bets, le meilleur EV brut du dataset. Ce chiffre paradoxal s'explique par un **désalignement de calibration** : les marchés ouvrant à 1-4¢ à Chengdu gagnent à 4.58% alors que le prix implique 1-4%. La sous-évaluation est réelle mais le N est insuffisant (131 trades, 6 gains). XGBoost AUC = **0.701** (bon signal, variance élevée). Les 3 villes chinoises partagent une structure identique — 81.8% de marchés bracket, GARCH persistence ~0.50 (vs 0.997 à Lucknow).

---

## Rapport complet

Voir : `research/outputs/12_quant_deep_dive/chengdu_report.md`

## Visualisations 3D interactives

`research/outputs/12_quant_deep_dive/viz_chengdu/` (3 HTML Plotly)

## Stats canoniques

- N markets : **198**
- AUC XGBoost (ex-ante) : **0.701**
- Hurst RS : **0.000**
- Calibration χ² : **3.6**
- Best strategy : **buy_yes_longshot**

## Related

- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../per-city-deep-dive/chengdu|Deep dive baseline]]
- [[../STATE-HANDOFF|State Handoff]]
