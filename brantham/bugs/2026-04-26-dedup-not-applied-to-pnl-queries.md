---
name: Dedup flag not applied to risk_manager P&L queries
description: Bug 2026-04-26. La colonne is_dup existait sur trade_log (1580/1723 trades flagués) mais aucune query P&L dans risk_manager / live_executor / metrics ne filtrait dessus. Résultat: circuit breaker tripé en permanence avec 7d DD=159.55% (artefact dedup bug). signal_log n'avait pas du tout de colonne is_dup. Fix: ajout colonne signal_log.is_dup, flag dupes, JOIN dans queries paper.
type: bug
project: brantham/polymarket
created: 2026-04-26
status: fixed
priority: critical
tags: [polymarket, bug, dedup, circuit-breaker, fix]
---

# Bug — Dedup flag posé sur DB mais code ne filtrait pas

## Découverte

2026-04-26 — investigation du kill switch en cours depuis ~7 jours
(`7d DD = 159.55% breached 10% cap`). Diagnostic :

- `trade_log.is_dup` existait, 1580/1723 trades flagués (suite fix dedup-bug 2026-04-22)
- **Aucun fichier de `src/pmhedge/alpha/`** ne référençait `is_dup` (grep)
- `signal_log` (paper shadow source) **n'avait pas de colonne is_dup du tout**
- 2576/2764 signals étaient des dupes non flagués
- → P&L paper agrégé = $16,884 sur 7 jours = artefact 20× inflated

Symptôme : kill switch tripé en permanence sur DD historique faux, le
système ne tradait plus.

## Impact mesuré

| Metric | Avant fix | Après fix |
|---|---:|---:|
| 7d DD% | 159.55% | **7.59%** |
| Today P&L | $0 inflated | $0 réel |
| Paper P&L 7d | $16,884 | **+$610** |
| Trade P&L 7d (real) | $? inflated | **+$467** |
| Circuit breaker | TRIPPED | cooling down |

## Fix appliqué

### 1. SQL — ajout colonne signal_log.is_dup
```sql
ALTER TABLE signal_log ADD COLUMN is_dup INTEGER NOT NULL DEFAULT 0;

WITH ranked AS (
  SELECT signal_id,
         ROW_NUMBER() OVER (PARTITION BY market_id, side ORDER BY emit_ts ASC) AS rn
  FROM signal_log
)
UPDATE signal_log SET is_dup = 1
WHERE signal_id IN (SELECT signal_id FROM ranked WHERE rn > 1);
```

### 2. Code — filter is_dup=0 dans queries P&L
- `src/pmhedge/alpha/risk_manager.py::today_realized_pnl()` — trade_log + signal_outcomes JOIN signal_log
- `src/pmhedge/alpha/risk_manager.py::rolling_drawdown_pct()` — idem
- `src/pmhedge/alpha/live_executor.py::_tier_exposure_usdc()` — trade_log
- `src/pmhedge/execution/metrics.py::_collect_trades()` — trade_log

## Cause racine

Le fix dedup 2026-04-22 a posé le flag `is_dup` côté écriture
(`live_executor.execute_signal` skip insert si dup détecté) mais la
**lecture** des P&L existants n'a jamais été migrée. Tout le code lisant
`trade_log` continuait à voir les dupes pré-fix. Et `signal_log` a été
oublié complètement (pas de colonne is_dup).

## Pattern à retenir

**Un dedup côté écriture seul ne suffit pas.** Les rapports P&L, les
risk metrics, les exposures, les dashboards — toutes les queries doivent
filtrer la même colonne. Dédiquer un test smoke après chaque migration
schéma : `SELECT P&L_clean vs P&L_all` doit montrer écart cohérent avec
le ratio dupes.

## Validation

```python
from pmhedge.alpha.risk_manager import today_realized_pnl, rolling_drawdown_pct
print(rolling_drawdown_pct(7, bankroll=1000.0))  # 0.0759 (was 1.5955)
```

Circuit breaker log : `[TRIPPED] today P&L=$+0.00  7d DD=7.59%  — cooling down`

## Related

- [[brantham/polymarket/dedup-bug-p-and-l-inflation]] — bug parent (fix côté écriture)
- [[brantham/polymarket/strategy-2026-04-26]] — strategy doc (W1.1 step)
- [[founder/decisions/2026-04-26-pivot-polymarket-obs-based]]
- [[brantham/_MOC]]
- [[_system/MOC-bugs]]
