---
name: P&L Inflation 20× — Duplicate Market Positions Bug
description: Bug critique découvert 2026-04-22. Le scanner re-signalait le même market_id toutes les 5 min → 35× positions dupliquées sur le même pari. P&L paper gonflé 20× la réalité. Fix market_side_dup dans live_executor.py.
type: bug
project: brantham/polymarket
created: 2026-04-22
tags: [polymarket, bug, critical, pnl, dedup, hedge-fund]
priority: critical
---

# Bug : P&L inflation 20× par duplicate market positions

## Découverte

2026-04-22 pendant analyse Tier S hedge-fund-grade : les 37 trades "gagnants"
Austin étaient en fait **35+ copies du même pari** sur le même market_id
(`0x185bede1d321549470944c2881e300a7bfbd17199609c8fd91daaaa6b03bc8c8`),
scanné toutes les 5 minutes entre 22:42 et 00:59 le 17-18 avril 2026.

Le scanner live loop 300s re-détecte le même market à chaque passage, émet
un nouveau signal (signal_id différent car hash sur emit_ts), passe le
risk_manager et persiste un nouveau trade. Guard existant = uniquement
au niveau `signal_id`, pas `market_id + side`.

## Impact empirique

| Metric | Value |
|--------|------:|
| P&L "inflaté" (toutes positions) | **+$19,925** |
| P&L réel (dedup market_id + side) | **+$979** |
| Inflation factor | **20.3×** |
| Trades 'closed' total | 1693 |
| Trades uniques (after dedup) | 136 |

## Breakdown tier post-dedup

| Tier | n unique | P&L | Avg |
|------|--------:|----:|----:|
| **S** | 21 | +$628 | +$29.9 |
| **A** | 80 | +$353 | +$4.4 |
| **C** | 6 | +$8 | +$1.3 |
| **B** | 29 | -$9 | -$0.3 |

Total : **+$980 sur 136 unique trades** — pas le "+$19.6k hedge fund" montré
précédemment. La performance reste positive mais à une échelle 20× plus
modeste : **~5% ROI paper sur $10k en 2 semaines**, avant slippage/fees réels.

## Fix

`src/pmhedge/alpha/live_executor.py::execute_signal` — ajout guard avant insert :

```sql
SELECT t.trade_id FROM trade_log t
JOIN signal_log s ON s.signal_id = t.signal_id
WHERE s.market_id = ? AND s.side = ?
  AND t.status IN ('OPEN', 'FILLED')
LIMIT 1
```

Si hit → audit_log `trade.skip` reason=`market_side_dup` + return None.

## Conséquences sur les analyses passées

**Tous les rapports P&L précédents étaient gonflés ~20×** :
- Le "+$19,599 realised" annoncé dans STATE-HANDOFF / memory
- Le "Tier S = 80% du P&L, $15,607" dans les rapports
- Le backtest v2 Tier S "+$18,748 Austin" — en réalité **~$605 un seul hit**

Le vrai signal de performance paper :
- **$980 / 14 jours / $10k bankroll = 0.5% ROI/jour moyen** (avant slippage live)
- Tier S avg +$29.9/trade (pas +$68) — toujours rentable mais moins dramatic
- Tier A avg +$4.4/trade sur 80 trades — **workhorse steady, c'est l'âme du système**

## Implications hedge-fund-grade

1. **Le paper résultats passés sont INVALIDES** — tout rapport doit être recalculé avec dedup
2. **Le vrai edge est dans le Tier A** (NO workhorse), pas Tier S (YES deep_OTM)
3. **En live, slippage réel tuera encore une fraction** — peut-être 30-50% du P&L
4. **G1/G2 gates** : attendre n ≥ 100 unique trades avec nouveau dedup avant promotion

## Actions suivantes

1. Re-run `audit_tier_s_whitelist.py` avec logique dedup (à patcher)
2. Re-run `reconcile_from_obs.py` avec collapse dupes
3. Flag existing trades as `IS_DUP` in trade_log pour ne pas les compter en P&L futur
4. Mesurer vraie capacity : $979 paper sur $10k = ROI mesuré = 0.5% par jour. Si on hedge-fund-grade, scale à $100k = $9,790/mois. Modeste mais pas ridicule pour un petit fonds.

## Related

- [[_MOC]]
- [[tier-s-v2-hedge-fund-gates]] (à revoir avec dedup)
- [[research-findings-2026-04-21]]
- [[TODO-pending]]
- [[_system/MOC-bugs]]
