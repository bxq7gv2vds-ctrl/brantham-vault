---
name: Polymarket — bucket router EV + paper exec auto via persist_signal
description: Architecture execution hedge fund grade. Router tier S/A/B/C/KILL calibré sur 1113 outcomes. Kelly multiplier par tier. Paper broker branché au hot path signal → trade_log.
type: decision
project: brantham/polymarket
date: 2026-04-20
status: active
tags: [polymarket, execution, architecture, hedge-fund, kelly, paper-trading]
---

# Polymarket — bucket router EV + exec auto

## Décision

Adopter une architecture **router-based execution** avec kill-switch empirique sur chaque bucket (alpha × side × price). Brancher l'exécution paper directement dans `persist_signal` pour que TOUT signal émis se traduise en ligne `trade_log`.

## Alternatives rejetées

1. **Wire le CLOB client réel directement** — prématuré sans paper track record ≥ 14j. Les 1113 outcomes réconciliés sont du backtest rétroactif sans slippage, pas une validation live.
2. **Garder paper_shadow comme source de vérité PnL** — `paper_shadow.reconcile_signals` calcule du P&L théorique agrégé, pas exploitable pour observability (pas de trade-level tracking, pas de position management, pas de dashboard temps réel).
3. **Bucket router désactivé, exécution plate** — laisser passer CONFIRMED_YES (0/31 WR), bucket B marginal (avg +$0.13), et surtout ne pas booster Tier S qui fait 87% du P&L. Passer à côté de 16.9k d'edge.

## Tier definition (validé sur 1113 outcomes)

| Tier | Rule | N | PnL empirique | Kelly mult | Capital cap |
|------|------|---|---------------|------------|-------------|
| S | MODEL_VS_MARKET YES, entry <0.15 | 164 | +$11,181 | ×1.5 | 40% |
| A | MODEL_VS_MARKET NO, 0.4 ≤ entry < 0.9 | 705 | +$2,272 | ×1.0 | 35% |
| B | MODEL_VS_MARKET NO, entry ≥ 0.9 | 156 | +$129 | ×0.3 | 5% |
| C | CONFIRMED_NO | 54 | +$100 | ×1.0 | 10% |
| KILL | Everything else (inc. CONFIRMED_YES) | — | — | — | 0% |

10% cash buffer réservé (sum = 90%).

## Pourquoi

- **Tier S porte 87% du P&L** (+$16,901 / $19,452 total post-backfill). C'est la seule strat à large payout (~10x) avec edge réel. ×1.5 Kelly booster car confiance empirique élevée.
- **Tier A est le workhorse** : 1018 trades, 756 fermés, WR 93%, P&L stable. Risque faible, serves as smoother sur la courbe de capital.
- **Tier B downsize** car payout marginal : avg +$0.13/trade après slippage. Garder au cas où la distribution change mais avec 0.3x.
- **Tier C (CONFIRMED_NO)** : WR 100% mais volume faible (54 trades). Edge pur (certitude physique), à garder pour stabiliser le PnL.
- **KILL CONFIRMED_YES** : 0/31 WR, pattern identique à COLDMATH_NO déjà tué en session 7. Acheter deep OTM à 61%+ est mathématiquement −EV.

## Pourquoi pas scaler Tier S > 1.5x

- Variance : WR 24% avec payout 10x. Même avec 164 samples, kurtosis élevé. 1.5x Kelly est déjà agressif.
- Sizing intrinsèque : `signal_generator` applique déjà Kelly fractionnel + regime HMM + volatility filter. Multiplier par 1.5 au-dessus augmente déjà la variance. ×2.0 ou plus pousse vers Kelly full qui a un drawdown attendu trop élevé.

## Pourquoi pas wire live ($POLY_PRIVATE_KEY) tout de suite

- Session paper #1 lancée 2026-04-20, target 14j. Need track record complet avant real money.
- Slippage empirique (slippage_ema) calibré sur 1 seul point (mkt_test, 40 bps). Besoin de 100+ fills live ou simulés friction-full pour avoir un EMA fiable.
- Pangu-Weather ONNX pas encore livré (bloquant Paul). Le fichier améliore CRPS de 5-10% donc scaling live avant a un ROI inférieur.

## How to apply

- Tout nouveau signal passe **automatiquement** par le router via `persist_signal`. Pas d'appel manuel nécessaire.
- Backtest retroactif : `uv run python scripts/trade_status.py` pour voir le P&L actuel.
- Close trades resolved : cron `com.paul.polymarket-alpha-reconcile-obs` tourne 09:20 UTC, appelle `close_resolved_trades()` automatiquement.
- Kill switch per-tier : modifier `bucket_router.route()` + redémarrer scanner (les signaux en vol sont cancel-safe).
- Pour activer live mode (futur) : set `PMHEDGE_MODE=live` + `POLY_PRIVATE_KEY`. Implémenter l'appel CLOB dans `live_executor.execute_signal` (actuellement paper-only).

## Risques résiduels

1. **Slippage underestimate** — défault 30 bps sur markets peu liquides. Real fills peuvent être 50-100 bps. → monitoring via `friction_executor` en shadow (TODO).
2. **Market regime shift** — les empirical buckets sont calibrés sur signaux 2026-04-17→20 (3 jours, 1113 outcomes). Régime peut changer (ex: La Niña transition). → recalibrer le router chaque 7j via script auto.
3. **Over-fitting au bucket Tier S** — 164 trades sur 3 jours, sample size limité. 1.5x Kelly prudent jusqu'à ≥500 trades.
4. **Position concurrency** — `concurrent_positions.py` déjà cap à 50 positions simultanées, OK pour paper mais à vérifier live.

## Related

- [[_system/MOC-decisions]]
- [[brantham/polymarket/_MOC]]
- [[brantham/bugs/2026-04-20-polymarket-trade-log-disconnected]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]
- [[brantham/polymarket/execution-playbook]]
- [[brantham/patterns/polymarket-coldmath-no-ev-analysis]]
