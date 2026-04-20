---
name: Session 2026-04-20 — Execution & Performance Kit
description: 10 livrables execution/performance hedge-fund-grade. Attribution, rolling metrics, Monte Carlo, CVaR-Kelly, drawdown manager, hour-of-day edge, markout, fill probability, execution quality, daily digest. Plus session_filter actionable.
type: session
created: 2026-04-20
tags: [polymarket, execution, performance, attribution, risk]
---

# Session 2026-04-20 — Execution & Performance Kit

Post G1-G2 Kit build + validation empirique, attaque de l'**axe execution & performance** (noté 3/10 + 9/10 dans l'audit initial). 10 livrables. Plus un actionable finding critique sur hour-of-day.

## Livrables (10/10 done)

| ID | Script / module | Rôle |
|---|---|---|
| PA1 | `scripts/performance_attribution.py` | Décompose P&L par alpha × city × TTR × edge_tier × hour × side |
| PA2 | `scripts/rolling_metrics.py` | Sharpe/Sortino/Calmar/Omega/profit_factor rolling 7d/30d/90d |
| PA3 | `scripts/monte_carlo_pnl.py` | Bootstrap 10k annual scenarios + CVaR95/99 |
| PA4 | `scripts/execution_quality.py` | Latency P50/P95/P99 par step + slippage distribution |
| PA5 | `scripts/fill_probability.py` | Logistic P(fill in 60s \| depth, spread, hour) — skeleton post-G3 |
| PA6 | `scripts/cvar_kelly.py` | Kelly ajusté pour contrainte CVaR95 worst-case |
| PA7 | `scripts/drawdown_manager.py` | Rolling DD + auto-scale Kelly bands (normal/caution/reduced/breaker) |
| PA8 | `scripts/hour_of_day_edge.py` | WR/edge/Sharpe par heure UTC — overweight/sunset detection |
| PA9 | `scripts/markout_analysis.py` | Post-fill price drift 5s/30s/5min/30min — skeleton post-G3 |
| PA10 | `scripts/performance_digest.py` | Aggregator quotidien → markdown report vault + Telegram |

## Finding critique actionable — hour-of-day

**Analyse empirique (N=1113 outcomes sur 2026-04-17/18)** :

| Heure UTC | N | WR | ROI | Sharpe/trade | Verdict |
|---|---|---|---|---|---|
| **h06** | 19 | 52.6% | -47.2% | -0.60 | **SUNSET** |
| **h07** | 7 | 57.1% | -37.5% | -0.51 | SUNSET |
| **h08** | 22 | 59.1% | -36.7% | -0.50 | SUNSET |
| **h09** | 26 | 61.5% | -37.4% | -0.48 | SUNSET |
| h14 | 34 | 79.4% | +40.5% | +0.30 | **OVERWEIGHT** |
| h19 | 91 | 80.2% | +145.3% | +0.28 | peak |
| h20 | 158 | 80.4% | +178.7% | +0.28 | peak |
| h21 | 145 | 82.8% | +152.0% | +0.27 | peak |
| h22 | 145 | 89.7% | +74.0% | +0.21 | peak |
| h23 | 169 | 91.7% | +57.6% | +0.19 | peak |

**Action immédiate appliquée** : `session_filter.py` créé + wire dans `persist_signal()`. Les signaux émis entre **h06-h09 UTC sont automatiquement bloqués** et logués dans audit_log avec `reason=session_filter`.

Gain attendu : évite -$348 cumulés observés sur ces 92 trades, préserve les +$12k des h19-h23.

## Attribution findings (context)

### Sunset candidates (n≥30, ROI<-5%)
- **CONFIRMED_YES** alpha : N=31, ROI **-100%** (totalement cassé, à investiguer)
- **Tokyo** : N=85, ROI -100% (déjà DISABLED city_config — cohérent)
- **Chicago** : N=44, ROI -43%
- **Miami** : N=68, ROI -33% (à downgrade de SHADOW→DISABLED)
- **NYC** : N=30, ROI -33% (déjà DISABLED)
- **edge_tier 8-15%** : N=300, ROI -13% (edges "moyens" perdent)

### Winners
- **austin** : N=100, ROI +680% (+$12,387) — leader
- **atlanta** : N=88, ROI +42% (+$695)
- **MODEL_VS_MARKET** alpha : ROI +89% global
- **YES side** : N=196, WR 20% mais ROI +387% (convex tails paient)

## Execution quality findings

Pipeline latency (~2.6s total mean, P99 ~13s) :
- **fetch_markets** : P95 3.9s, **P99 10.5s** → bottleneck Polymarket API
- model_vs_market_batch : P99 2.2s
- confirmed_scan : P99 136ms (fast)

**Pour G3 live** : target pipeline < 1s. Optimisations à considérer :
- Cache markets 60s (au lieu de fetch à chaque scan)
- HTTP connection pooling
- Parallelize market queries

## CVaR-Kelly findings

```
Pool 1113 trades, mean return/trade +0.695, std 3.45
Cluster (30 concurrent) CVaR95 return: -0.061
Pure Kelly fraction    : 0.058 (5.8%)
CVaR-Kelly fraction    : 1.000 (non-binding at 10% cap)
Recommended fraction   : 0.058
```

Interprétation : Kelly est déjà conservatif (variance élevée), CVaR n'est pas binding. OK à utiliser pure Kelly avec cap 10% worst-case.

## Infrastructure ajoutée

- **`com.paul.polymarket-alpha-perf-digest.plist`** — daily 08:15 UTC avec Telegram digest
- **`src/pmhedge/alpha/session_filter.py`** — integré dans persist_signal
- **`vault/brantham/polymarket/reports/`** — dossier reports auto-générés

## Caveats méthodologiques

1. **T=2 distinct days** pour rolling metrics — les Sharpe sont inflated. Attendre 30+ jours pour métriques crédibles.
2. **MC P&L v1 naïf** : utilise per-trade size fixe = 1% bankroll × trades/day. Real sizing dynamique via Kelly + risk_manager. À raffiner.
3. **Markout + fill probability** = skeletons, data-dependent (post-G3 real fills).
4. **Latency `fetch_markets` 10.5s P99** = Polymarket API, pas notre code. Pas optimisable côté nous sans cache.
5. **Equity curve $14,324** = paper inflated par convex YES tails. Real money TC gas eat 40-60% de ce edge.

## Tasks résolues cette session

Sprint Execution & Performance : 10/10 livrables (tasks #24-#33).

## État launchd actif

36 + 1 nouveau = **37 jobs polymarket-alpha** (perf-digest ajouté).

## Prochaine session possible

**Attente data** (passif) :
- T≥30 distinct days → rolling Sharpe crédible
- 50+ real fills → TC calibration, markout, fill_probability live

**Actions hors scope Claude** (toi) :
- Review economic-thesis.md
- Drop Pangu ONNX
- Polymarket wallet + py-clob-client

**Actions possibles Claude** si tu veux plus :
- Hourly edge tracker launchd weekly → auto-update blocked_hours set
- Champion/challenger shadow mode
- Alpha-book registry si multi-strat
- Regime transition forecast model

## Related

- [[_MOC|Polymarket Hub]]
- [[g1-g2-qualification-kit|G1→G2 Framework]]
- [[gate-scorecard-spec|Scorecard spec]]
- [[feature-rejection-log|Feature rejection log]]
- [[STATE-HANDOFF]]
- [[sessions/2026-04-20-g1-g2-kit-build|Session kit build]]
- [[sessions/2026-04-20-feature-engineering-burst|Session feature burst]]
- [[reports/daily-2026-04-20|Daily digest 2026-04-20]]
