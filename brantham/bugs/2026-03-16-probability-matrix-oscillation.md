---
tags: [bug-fix, brantham-simulator, frontend, zustand]
date: 2026-03-16
project: brantham-simulator
severity: high
---

# Probability Matrix oscillait entre 500 et 0 deals

## Symptome
La Probability Matrix affichait 500 deals puis 0 deals en alternance toutes les ~2-3 secondes. Les donnees API etaient correctes (500 deals) mais le composant montrait "No data".

## Root Cause
`SimulationControl.jsx` poll `/simulation/quant-status` toutes les 5 secondes. L'endpoint retourne `deal_metrics: []` (tableau vide) quand aucune simulation n'est en cours. Le guard `if (status.deal_metrics)` est truthy pour un tableau vide en JavaScript (`[] == true`). Donc `setProbabilityMatrix([])` ecrasait les donnees reelles chargees par le ProbabilityMatrix component.

## Fix
Changer `if (status.deal_metrics)` en `if (status.deal_metrics?.length)` dans SimulationControl.jsx (3 occurrences). Meme fix pour `status.agents`.

## Pattern
Toujours utiliser `.length` pour verifier un tableau avant de l'utiliser comme guard en JS. `[]` est truthy.
