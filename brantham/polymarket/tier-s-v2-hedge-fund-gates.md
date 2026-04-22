---
name: Tier S Hedge-Fund-Grade Gates v2
description: Upgrade bucket_router avec gates stricts sur Tier S (MODEL YES deep_OTM) basé sur empirical backtest 228 trades closed. Austin whitelisted, above_N/narrow/short_TTR/low_edge killed. +$3,151 P&L gain validé.
type: pattern
project: brantham/polymarket
created: 2026-04-22
tags: [polymarket, tier-s, pattern, edge, hedge-fund]
priority: critical
---

# Tier S v2 — Hedge-Fund-Grade Gates

## Contexte

Le Tier S v1 (MODEL_VS_MARKET YES + entry < 0.15 → Kelly ×1.5) produisait
+$15,597 P&L paper sur 228 trades, WR 17.6%. Analyse 2026-04-22 a révélé
que le P&L était **entièrement concentré sur Austin** :

| Pattern | n | WR | P&L | Verdict |
|---------|--:|---:|----:|---------|
| Austin below_N + TTR≥30h | 37 | 100% | +$18,748 | ★ star |
| Tokyo/Wellington above_N long TTR | 97 | 0% | -$2,389 | pure loss |
| Short TTR (<30h) deep_OTM | 22 | 9% | -$118 | near-zero edge |
| Narrow bin deep_OTM | 32 | 0% | -$638 | payout < variance |
| Other below_N low edge | 6 | 0% | -$69 | under the floor |

**Insight** : les brackets **above_N** (open-ended "T ≥ N") à deep_OTM sont
une pure loterie loser. Les brackets **below_N** à long TTR avec ville où
le modèle a un edge directionnel = WR 100% sur Austin.

## Nouveaux gates (v2)

Implémentés dans `src/pmhedge/alpha/bucket_router.py::route()` :

1. **Price ≥ 0.15** → KILL (existed)
2. **bracket_type == above_N** → KILL (new, -$2,326 saved)
3. **bracket_type == narrow_bin** → KILL (new, -$638 saved)
4. **TTR < 30h** → KILL (new, -$118 saved)
5. **intrinsic_edge < 0.15** → KILL (new, -$69 saved)
6. **City whitelist** :
   - `TIER_S_STAR_CITIES` = {austin} → Kelly ×1.5
   - `TIER_S_GRAYLIST` = {} → Kelly ×1.0 (empty, populate as evidence arrives)
   - Other cities passing gates → Kelly ×0.75 (exploration tier)

## Backward compat

`route()` accepts optional kwargs (bracket_lo_c, bracket_hi_c, ttr_hours,
city_slug, intrinsic_edge). When NONE are provided, the legacy v1 path
applies (backward-compat for `backfill_from_existing_signals`). Live
pipeline always passes full context via `live_executor.execute_signal`.

## Backtest

```sql
-- Tier S v2 applied retroactively on 228 closed trades
PASS:star (Austin)    37 trades    100% WR    +$18,748
KILL:above_N         131 trades      1% WR    -$2,326
KILL:narrow           32 trades      0% WR     -$638
KILL:short_TTR        22 trades      9% WR     -$118
KILL:low_edge          6 trades      0% WR      -$69
```

**Net gain v2 vs v1 : +$3,151 (+20%)** sans perte de signal gagnant.

## Evolution

Ajouter à `TIER_S_GRAYLIST` une ville lorsque :
- n_outcomes Tier S ≥ 15 dans la ville
- WR ≥ 50%
- PnL net > 0

Ajouter à `TIER_S_STAR_CITIES` lorsque :
- n_outcomes Tier S ≥ 30 dans la ville
- WR ≥ 60%
- PnL net supérieur à la moyenne top-2

## Script d'audit automatique

TODO (P1) : `scripts/audit_tier_s_whitelist.py` qui tourne daily et update
`TIER_S_STAR_CITIES` + `TIER_S_GRAYLIST` en fonction des outcomes fraîchement
settled. Pour l'instant whitelist statique — review manuelle hebdomadaire.

## Capacity + scale considerations

Tier S v2 est beaucoup plus sélectif — volume de signaux émis baisse de ~85%.
Conséquence : capacity réduite mais edge-per-trade plus pur. Pour scale :
1. Accumulate evidence on more cities → graduate to graylist / star
2. Ensemble avec Pangu fine-tuning once CDS setup → corrige bias Austin-style
3. Expand à below_N brackets avec bias documenté (Austin = µ surestimé,
   cherche autres villes avec bias > +1°C en pôle stats 05)

## Related

- [[_MOC]]
- [[TODO-pending]]
- [[research-findings-2026-04-21]]
- [[CONTINUATION-PROMPT]]
- [[ARCHITECTURE]]
- [[_system/MOC-patterns]]
