---
title: Crypto Polymarket × Deribit Arbitrage — MOC
created: 2026-04-23
status: design-validated → build phase 1
parent: [[brantham/polymarket/_MOC]]
tags: [polymarket, deribit, hedge, statistical-arb, crypto]
---

# Crypto Polymarket × Deribit Arbitrage

Sous-projet : arbitrage statistique entre brackets crypto Polymarket (BTC/ETH) et options Deribit + perp Hyperliquid.

## Approche centrale validée 2026-04-23

**Portfolio of edges (statistical arbitrage)** — pas course à la latency single-trade.

- N positions micro avec edges individuels 2-5pp
- Hedge agrégé delta-neutral via Deribit options (long premium) + Hyperliquid perp
- Rebalancing continu 60s soft / 5min hard
- Sharpe portfolio ≈ √N × Sharpe_individual

## Capital initial

$1000 — split :
- Polymarket positions : $400
- Deribit options hedge (long premium) : $150
- Hyperliquid perp collateral : $100 (× 5x leverage = $500 hedge notional)
- Reserve : $350

## Capacity réelle

Hard cap : **$250k-500k AUM** (pas plus, marché Polymarket est binaire avec depth limitée).

Au plafond avec Sharpe 1-2 : $75k-300k/an récurrent.

## Documents

- [[architecture]] — design technique complet
- [[math-pricing-hedge]] — Breeden-Litzenberger, SVI, Greeks, Kelly multi-asset
- [[risks-mitigation]] — 10 pièges identifiés + mitigations
- [[roadmap]] — plan build Phases 1-5
- [[../decisions]] — decisions log parent

## Phases

| Phase | Durée | Output | Go/No-Go criterion |
|---|---|---|---|
| Phase 1 — Data + validation empirique | 1-2 jours | Snapshot 24h, mesure edge réel | ≥10 brackets simultanés avec edge >2pp |
| Phase 2 — Pricing engine complet | 2-3 jours | SVI fitter, fair_prob, edge net | Pricing < 100ms par cycle |
| Phase 3 — Portfolio + hedge | 2-3 jours | Greeks aggregator, cvxpy optimizer | Hedge cost < 30% edge gross |
| Phase 4 — Paper trading 7j | 7 jours | Live paper full pipeline | Sharpe paper > 1.5 |
| Phase 5 — Live $200 | 14 jours | Real capital small | Live ratio > 0.6 vs paper |

## Stack technique

- Python 3.13 + uv (existant polymarket-hedge)
- numpy + numba JIT (pricing hot path)
- scipy.optimize (SVI calibration)
- cvxpy (hedge optimizer)
- DuckDB + Parquet (storage)
- websockets + aiohttp (async I/O)
- loguru (logging)

## Module location

`/Users/paul/polymarket-hedge/src/pmhedge/crypto_arb/`
- `clients/` — Deribit, Polymarket crypto, Hyperliquid
- `pricing/` — SVI, density, fair_prob, edge
- `hedge/` — Greeks, optimizer, executor
- `portfolio/` — sizing, rebalancer, risk
- `scripts/` — runners, snapshots, backtests
- `tests/` — unit + integration

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/architecture]] — strat météo existante
- [[_system/MOC-decisions]]
- [[_system/MOC-patterns]]
