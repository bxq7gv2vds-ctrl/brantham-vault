---
name: Quant Deep Dive — Busan
description: Analyse quant rigoureuse Busan sur 6 mois on-chain. AUC XGBoost ex-ante=0.539, Hurst RS=0.000, χ² calibration=1.4, best strategy=buy_yes_uncertain.
type: analysis
project: brantham/polymarket
created: 2026-04-22
tags: [polymarket, quant, deep-dive, busan, weather]
priority: high
---

# Busan — Quant Deep Dive (6 mois on-chain)

## TL;DR

Busan est la ville la **plus illiquide** du dataset sur les 5 villes analysées — 66 marchés, $57 735 volume total, **$875/marché**, active seulement depuis 6 jours. En tant que port maritime coréen, son climat printanier est relativement stable : YES win rate = 9.2%. L'illiquidité est critique : **Roll spread médian = 192 bps**, Kyle λ = 235 bps — le plus élevé des 5 villes. Le XGBoost ex-ante ressort un AUC de **0.539**, à peine au-dessus du hasard, confirmant que le N est insuffisant pour calibrer un signal. L'unique edge identifié — `buy_no_brackets` (+3.27% EV) — est mathématiquement positif mais avec un Sharpe de 0.08 et N = 53, reste **pré-significatif**. Recommandation principale : **SHADOW ONLY** jusqu'à N ≥ 300 marchés, puis réévaluation Q3 2026.

---

## Rapport complet

Voir : `research/outputs/12_quant_deep_dive/busan_report.md`

## Visualisations 3D interactives

`research/outputs/12_quant_deep_dive/viz_busan/` (3 HTML Plotly)

## Stats canoniques

- N markets : **66**
- AUC XGBoost (ex-ante) : **0.539**
- Hurst RS : **0.000**
- Calibration χ² : **1.4**
- Best strategy : **buy_yes_uncertain**

## Related

- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../per-city-deep-dive/busan|Deep dive baseline]]
- [[../STATE-HANDOFF|State Handoff]]
