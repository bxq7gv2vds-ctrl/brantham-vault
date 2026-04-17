---
tags: [polymarket, hedge-fund, moc]
created: 2026-04-17
status: active
---

# Polymarket Hedge Fund — Map of Content

Knowledge hub pour la construction d'un système trading hedge-fund grade sur Polymarket (weather markets puis expansion).

**Projet code** : `/Users/paul/polymarket-hedge/`
**DB locale** : `bracket_scalper_trades.db`, `all_markets.db`, `pmhedge.db`, `alpha_data_hub.db` (new)
**Module principal** : `src/pmhedge/alpha/` (architecture unifiée)

## Objectif

Construire un système de trading **100% data-driven** sur Polymarket avec :
- Data multi-source best-in-class par région (HRRR US, AROME FR, ICON-EU, etc.)
- Modèle ML calibré SOTA (EMOS + BMA + XGBoost + DRN)
- Exécution CLOB direct avec rebate capture
- Risk management hedge-fund grade (Kelly correlation-adjusted, kill switch)
- Backtest walk-forward rigoureux avec Monte Carlo + attribution

**Target P&L** : $200-400k/an avec capital scaling $1k → $50k

## Contenu

### Architecture & Design
- [[architecture|Architecture hedge fund grade (4 couches)]]
- [[data-sources|Data sources inventory — best-in-class par région]]
- [[model-design|Design modèle ML (EMOS + BMA + ML post-proc)]]
- [[execution-design|Infrastructure execution (CLOB WebSocket + order manager)]]
- [[risk-management|Risk & portfolio management]]

### Roadmap & Decisions
- [[roadmap|Roadmap phased 4 semaines]]
- [[decisions|Log des décisions architecturales]]
- [[questions|Questions critiques + réponses]]

### Findings & Backtests
- [[findings|Diagnostics & edges détectés]]
- [[backtest-results/2026-04-17-baseline|Baseline backtest 2026-04-17]]

### Sessions
- [[sessions/2026-04-17-diagnostic-and-alpha-engine|Session 2026-04-17 #1: diagnostic + alpha engine v0]]
- [[sessions/2026-04-17-phase1-data-foundation|Session 2026-04-17 #2: Phase 1 data foundation + model hub]]
- [[sessions/2026-04-17-phase1-live-runner|Session 2026-04-17 #3: live runner end-to-end (19 signaux émis)]]
- [[sessions/2026-04-17-phase1-risk-orderbook|Session 2026-04-17 #4: CLOB orderbook + risk manager + ERA5]]
- [[sessions/2026-04-17-phase2-completion|Session 2026-04-17 #5: Phase 2 completion — CONFIRMED + paper shadow + XGBoost (25/25 tasks)]]

## Métriques actuelles (2026-04-17)

| Métrique | Valeur |
|---|---|
| Settled trades (paper) | 6,740 |
| Signal types | 10 (CONVEX_YES, COLDMATH_NO, EXACT_BIN_YES, PROB_NO, PROB_YES, etc.) |
| Cities couvertes | 43 |
| Filter v1 PnL (bankroll $1k) | +$1,049 (+269% vs baseline) |
| Walk-forward Sharpe pooled | 16.4 |
| Data pipeline freshness | **12 jours stale** (à fix) |

## État actuel & prochaines étapes

✅ **Fait aujourd'hui (session 2026-04-17)** :
- Diagnostic complet des edges (PROB_NO/COLDMATH_NO/EXACT_BIN_YES rentables, PROB_YES/SPEEDA_EARLY toxiques)
- EdgeFilter v1 : pocket registry + Kelly sizing
- Backtest engine unifié : walk-forward + MC + attribution
- Architecture hedge fund grade définie
- Module `alpha/` créé avec data_hub + nwp_sources

⏳ **À faire (priorisé par impact)** :
1. Finir `nwp_sources.py` (HRRR + ICON-EU direct intégration)
2. Construire EMOS + BMA modules
3. Orderbook WebSocket CLOB live
4. Backfill ERA5 5 ans pour training ML
5. XGBoost post-processing
6. Unified signal generator (model vs market)
7. Risk manager correlation-adjusted
8. Paper shadow mode 30-jour validation

## Related

- [[../_MOC|Brantham MOC]]
- [[../../_system/MOC-master|Master MOC]]
- Project code: `/Users/paul/polymarket-hedge/`
