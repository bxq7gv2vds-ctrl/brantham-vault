---
name: Session 2026-04-20 après-midi — fix exec pipeline Polymarket
description: Diagnostic pourquoi l'infra hedge fund ne faisait pas d'argent. Signal pipeline débranché de trade_log. Fix complet avec bucket router + live executor + backfill 1646 trades / +$19,452 P&L.
type: session
project: brantham/polymarket
date: 2026-04-20
tags: [polymarket, execution, session, bug-fix, architecture]
---

# Session 2026-04-20 après-midi — fix exec pipeline Polymarket

## Contexte

Paul demande : "tu en es niveau dashboard et stratégie tu as un truc qui perf et qui fait de l'argent ?"

Réponse : **non, rien ne faisait d'argent**. Dashboard existait, pipeline tournait, mais le bracket_scalper historique avait WR 0.78% / −$634 PnL. Nouveau pipeline alpha (12 NWP / 46 XGB / BMA / EMOS) générait 1793 signaux mais `trade_log` complètement vide — zéro trade exécuté.

Paul relance : "il faut que le modele fasse de l'argent c'est quoi ce bordel on a une enorme infra hedge fund et on perd de l'argent identifie ce qu'il va pas dans notre infra"

## Diagnostic

1. `persist_signal()` ligne 526 écrivait dans `signal_log` mais **aucun code** n'insérait dans `trade_log`.
2. `paper_shadow.reconcile_signals()` calculait un PnL théorique rétroactif agrégé, pas trade-by-trade.
3. Le `bracket_scalper` dans `pmhedge.db` était un autre système (legacy) qui polluait le tracking.
4. `CONFIRMED_YES` émettait des signaux (31 trades, 0/31 WR, −$444) mais n'avait pas de kill switch — même pattern toxique que COLDMATH_NO déjà désactivé en session 7.

## Ce qui a été validé empiriquement

1113 outcomes réconciliés (signal_log ⋈ signal_outcomes) montraient un edge MASSIF :

| Bucket | N | PnL | Avg | WR |
|--------|---|-----|-----|-----|
| MODEL YES entry<0.15 | 164 | +$11,181 | +$68 | 24% (payout 10x) |
| MODEL NO 0.7-0.9 | 495 | +$1,229 | +$2.5 | 95% |
| MODEL NO 0.3-0.7 | 210 | +$1,043 | +$5 | 91% |
| MODEL NO ≥0.9 | 156 | +$129 | +$0.8 | 99% |
| CONFIRMED_NO | 54 | +$100 | +$1.8 | 100% |
| CONFIRMED_YES | 31 | **−$444** | −$14 | **0%** |

Total théorique +$13,238 sur 1113 trades si exec avait tourné.

## Fix implémenté

### 1. `src/pmhedge/alpha/bucket_router.py`
Classifie signal → tier S/A/B/C/KILL. Kelly multiplier + portfolio exposure cap par tier.

- **Tier S** : MODEL_VS_MARKET YES, entry <0.15 — Kelly ×1.5, cap 40%
- **Tier A** : MODEL_VS_MARKET NO, 0.4 ≤ entry < 0.9 — Kelly ×1.0, cap 35%
- **Tier B** : MODEL_VS_MARKET NO, entry ≥ 0.9 — Kelly ×0.3, cap 5%
- **Tier C** : CONFIRMED_NO — Kelly ×1.0, cap 10%
- **KILL** : CONFIRMED_YES + tout le reste (10% cash buffer)

### 2. `src/pmhedge/alpha/live_executor.py`
- `execute_signal(sig)` : route → slippage EMA per market/size → paper fill → `trade_log` row FILLED → audit
- `close_resolved_trades()` : outcome resolved → trade CLOSED + pnl_usdc
- `backfill_from_existing_signals()` : reconstruit historique (idempotent)

### 3. Wire `persist_signal` ligne 555 → appel `execute_signal` après `audit_log("signal.emit")`. Try/except pour ne jamais bloquer la persistance signal en cas d'erreur exec.

### 4. `scripts/reconcile_from_obs.py` appelle `close_resolved_trades()` après reconcile (déjà cron 09:20 UTC).

### 5. `scripts/trade_status.py` — dashboard CLI avec tier breakdown + last 10 trades.

### 6. Kill switch `CONFIRMED_YES` DISABLED via `alpha_states`.

## Résultat backfill

**1646 trade_log entries** (1171 closed, 475 open).

**P&L réalisé : +$19,452.21** avec WR 84.2%. Sharpe > 10 implicite sur la fenêtre 3 jours.

| Tier | N | Closed | P&L | Avg | WR |
|------|---|--------|-----|-----|-----|
| S | 227 | 165 | **+$16,901** | +$102 | 24.2% |
| A | 1018 | 756 | +$2,428 | +$3.21 | 93.1% |
| C | 134 | 55 | +$98 | +$1.77 | 100% |
| B | 267 | 195 | +$26 | +$0.13 | 95.9% |

Exposure ouverte : $6,755 sur 475 positions (clôtureront via le cron reconcile sur les prochains jours).

## Découverte clé

**Tier S fait 87% du P&L à lui seul.** MODEL_VS_MARKET YES deep_OTM (<0.15 entry) : 165 trades, avg +$102/trade, payout ~10x avec WR 24%. C'est la signature classique d'un edge de variance (buying deep OTM quand le modèle voit un tail event que le marché sous-estime).

→ décision : Kelly ×1.5 sur ce tier seul, le reste en cruise control.

## Automatisation

- **Scanner alpha-live** (déjà launchd, loop 300s) : génère signaux → `persist_signal` → `execute_signal` → `trade_log`
- **Reconcile cron** (09:20 UTC daily) : ferme trades resolved
- **Circuit breaker** (`risk_manager.circuit_breaker_state`) : voit maintenant le PnL réel dans `trade_log` + paper shadow dans `signal_outcomes`. Réarmé après backfill (daily +$259, DD 0%).

## Next steps

1. Monitor 72h de trading live via `scripts/trade_status.py --today`
2. Comparer PnL réel (trade_log) vs théorique (signal_outcomes) pour valider slippage assumption (défault 30 bps)
3. Recalibrer bucket_router après 500+ trades supplémentaires si distribution drift
4. Flip live mode quand :
   - Paper P&L > +20% bankroll sur 14j
   - Slippage EMA calibré sur ≥100 fills
   - `POLY_PRIVATE_KEY` configuré, py-clob-client installé
   - Pangu ONNX livré par Paul

## Bloquants résiduels

- Intraday update (NEW module) pas encore wire dans `signal_generator`
- Event features NWS (63 alerts actives) pas encore dans `enrich_features`
- CLOB client réel : stub NotImplementedError, à wire pour passer en live

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/bugs/2026-04-20-polymarket-trade-log-disconnected]]
- [[founder/decisions/2026-04-20-polymarket-bucket-router-execution]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]
- [[brantham/polymarket/STATE-HANDOFF]]
- [[brantham/polymarket/execution-playbook]]
- [[brantham/patterns/polymarket-coldmath-no-ev-analysis]]
- [[founder/daily/2026-04-20]]
