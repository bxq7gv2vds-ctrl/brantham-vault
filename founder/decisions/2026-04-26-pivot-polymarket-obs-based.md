---
name: Pivot stratégique Polymarket vers obs-based
description: Décision 2026-04-26 de pivoter de la stratégie NWP/Tier A ITM vers METAR observation front-running TTR<2h prix 0.05-0.50, suite reverse engineering top winners et dedup bug.
type: decision
project: brantham/polymarket
created: 2026-04-26
status: active
tags: [polymarket, decision, pivot, strategy]
---

# Pivot stratégique Polymarket — vers obs-based

## Décision

Pivoter la stratégie Polymarket de **NWP forecasting + Tier A ITM 0.95+**
vers **METAR observation front-running TTR<2h sur prix 0.05–0.50**.

## Contexte

Deux findings empiriques majeurs :

1. **Dedup bug (2026-04-22)** : P&L paper passé inflaté 20×. Vrai
   ROI = 0.5%/jour sur $10k paper, pas 10%/jour fantasmé.

2. **Reverse engineering top winners (2026-04-25/26)** : top 3 traders
   weather (+$69k, +$28k, +$27k P&L réel) ne font PAS de NWP. Pattern
   unifié = METAR obs front-running TTR<2h sur prix 0.05–0.50.

## Alternatives considérées

| Option | Verdict |
|---|---|
| Continuer NWP/Pangu/EMOS + Tier A ITM | Edge prouvé faible (1-2% ROI), on perd vs MM, pas l'edge réel |
| Pivoter obs-based pur (heuristique simple) | **Choix** — match empirique winners, capacity validée, build léger |
| Hybrider NWP + obs | Complexité élevée pour gain marginal, NWP infra déjà bloquée (CDS) |
| Killer le projet | Capacity $10-20k = micro-strat rentable, vaut la peine pour preuve méthodologie |

## Implications

- Couper Tier A ITM 0.95+ (ou size ÷ 3 pour benchmark)
- Build `bracket_pricer_obs.py` (heuristique sans ML)
- Étendre data layer aux NO tokens (70% volume invisible aujourd'hui)
- Park Pangu, EMOS Tmin extension, precipitation NWP
- Plafond AUM accepté : $10-20k weather seul, ~$44k/an max

## Critères de succès

- W2 paper 7j : ROI dedup-clean > 0.3%/jour
- 30j paper post-W2 stable
- Sinon : retour planche à dessin sur ce projet

## Related

- [[brantham/polymarket/strategy-2026-04-26]] — strategy doc canonique
- [[brantham/polymarket/dedup-bug-p-and-l-inflation]]
- [[brantham/polymarket/reverse-engineer-true-winners]]
- [[brantham/polymarket/capacity-reality-check]]
- [[_system/MOC-decisions]]
- [[brantham/_MOC]]
