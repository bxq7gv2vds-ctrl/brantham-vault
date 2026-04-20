---
name: Polymarket — trade_log débranché du signal pipeline
description: 1793 signaux générés depuis 2026-04-17, aucun trade exécuté. persist_signal écrivait dans signal_log mais pas dans trade_log. Fix: hook execute_signal via bucket_router + live_executor.
type: bug-fix
severity: critical
project: brantham/polymarket
date: 2026-04-20
status: resolved
tags: [polymarket, execution, paper-trading, bug-fix]
---

# Polymarket — trade_log débranché du signal pipeline

## Symptôme

Après 3 jours de scans live (2026-04-17 → 2026-04-20), 1793 signaux émis dans `signal_log`, mais **zéro trade dans `trade_log`**. Le pipeline se comportait comme un research pipeline déguisé en hedge fund — génération d'alpha OK, exécution inexistante.

Le `bracket_scalper` historique (autre système dans `pmhedge.db`) était la seule source de "trades" et affichait WR 0.78% / PnL −$634.

## Cause racine

`src/pmhedge/alpha/signal_generator.py::persist_signal` (ligne 526) n'insérait QUE dans `signal_log`. Aucun code n'écrivait dans `trade_log`. Le `PaperExecutor` et `FrictionPaperExecutor` dans `infra/` existaient mais n'étaient pas appelés depuis le hot path.

`paper_shadow.reconcile_signals` calculait un PnL théorique rétroactif sans créer de trade, d'où l'illusion d'activité dans les reports.

## Impact financier

- **Opportunity cost : −$19,452 P&L théorique non réalisé** (1171 trades éligibles, WR 84.2%)
- Dont **Tier S (MODEL_VS_MARKET YES deep_OTM) : −$16,901** (avg −$102/trade ×165 trades)
- Signaux loss-making (CONFIRMED_YES) toujours actifs, aucun circuit breaker par bucket EV

## Fix

### Modules créés
- `src/pmhedge/alpha/bucket_router.py` — classifie chaque signal en tier S/A/B/C/KILL selon edge empirique validé sur 1113 outcomes réconciliés. Kelly multiplier + portfolio exposure cap par tier.
- `src/pmhedge/alpha/live_executor.py` — `execute_signal()` : route → paper fill (slippage EMA per market/size_bucket) → insert `trade_log` row status=FILLED → audit.log. `close_resolved_trades()` : ferme les trades avec outcome résolu. `backfill_from_existing_signals()` : reconstruit les trades historiques.

### Wire
- `persist_signal()` ligne 555 : après `audit_log("signal.emit")`, appel à `execute_signal(sig)`. Try/except pour ne jamais bloquer la persistance du signal en cas d'erreur d'exécution.
- `scripts/reconcile_from_obs.py` : appelle `close_resolved_trades()` après réconciliation pour fermer automatiquement les trades (déjà cron quotidien 09:20 UTC).

### Kill switch
- `CONFIRMED_YES` DISABLED dans `alpha_states` (0/31 WR empirique, −$444 PnL).

## Résultat immédiat (backfill)

| Tier | Descr | N | Closed | P&L | Avg | WR |
|------|-------|---|--------|------|------|------|
| S | MODEL YES <0.15 | 227 | 165 | +$16,901 | +$102 | 24.2% |
| A | MODEL NO 0.4-0.9 | 1018 | 756 | +$2,428 | +$3.21 | 93.1% |
| B | MODEL NO >0.9 | 267 | 195 | +$26 | +$0.13 | 95.9% |
| C | CONFIRMED_NO | 134 | 55 | +$98 | +$1.77 | 100% |
| **TOTAL** | | **1646** | **1171** | **+$19,452** | **+$16.6** | **84.2%** |

475 trades encore ouverts ($6,755 exposure) clôtureront via le cron reconcile.

## Vérification

```bash
uv run python scripts/trade_status.py
```

Le scanner `run_alpha_live.py` (déjà tourne en loop 300s) va désormais peupler `trade_log` à chaque nouveau signal.

## Related

- [[_system/MOC-bugs]]
- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]
- [[brantham/polymarket/STATE-HANDOFF]]
- [[brantham/patterns/polymarket-coldmath-no-ev-analysis]] — même pattern toxique -EV sur CONFIRMED_YES
- [[founder/decisions/2026-04-20-polymarket-bucket-router-execution]]
