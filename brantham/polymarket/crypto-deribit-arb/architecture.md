---
title: Architecture — Crypto Polymarket × Deribit Arbitrage
created: 2026-04-23
parent: [[_MOC]]
tags: [architecture, design]
---

# Architecture technique

## Principe : Portfolio of edges + continuous rebalancing

Au lieu de chasser un trade parfait latency-critical, on construit un portefeuille de N positions micro hedgées en continu. La diversification réduit la variance par √N (positions indépendantes), permettant un Sharpe portfolio élevé même avec edges individuels modestes.

## Pipeline complet

```
┌────────────────────────────────────────────────────────────┐
│  Universe Scanner (every 60s)                              │
│  - Polymarket Gamma API: tous brackets crypto actifs       │
│  - Filter: TTR > 6h, depth > $200, settlement = Chainlink  │
│  Output: ~100-300 candidate markets                        │
└──────────────────┬─────────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────────┐
│  Pricing Engine (every 60s)                                │
│  - Pull Deribit option chain BTC + ETH (REST/WS)           │
│  - Fit SVI per asset per expiry (5 params, scipy)          │
│  - Build risk-neutral density f(K) per asset               │
│  - For each bracket: fair_prob = ∫_{K1}^{K2} f(K) dK       │
│  - Compute edge_net = poly_price - fair_prob - fees(p)     │
│  Output: edge table ranked                                 │
└──────────────────┬─────────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────────┐
│  Position Manager                                          │
│  - For each market with |edge_net| > threshold (2-3pp):    │
│    - Compute Greeks (Δ, Γ, Vega) of bracket                │
│    - Compute Kelly size (fractional, shrinkage)            │
│    - State: pending/open/closing                           │
│  - Maintain target portfolio                               │
└──────────────────┬─────────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────────┐
│  Portfolio Greeks Aggregator                               │
│  - Sum Δ, Γ, Vega across all positions                     │
│  - Net exposure by asset (BTC, ETH)                        │
│  - Factor exposures (level, slope, curvature smile)        │
└──────────────────┬─────────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────────┐
│  Hedge Optimizer (cvxpy)                                   │
│  Minimize: Σ |w_i| × cost_i                                │
│  Subject to:                                               │
│    Δ_portfolio + Σ w_i × Δ_hedge_i = 0                     │
│    |Vega_portfolio + Σ w_i × Vega_hedge_i| < cap           │
│    |Γ_portfolio + Σ w_i × Γ_hedge_i| < cap                 │
│  Hedge instruments: Hyperliquid perp + Deribit options     │
└──────────────────┬─────────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────────┐
│  Continuous Rebalancer (60s soft / 5min hard)              │
│  - Recompute pricing, edges                                │
│  - Close if edge inverted or eroded                        │
│  - Adjust hedge if Δ drift > threshold                     │
│  - Log everything to DuckDB                                │
└────────────────────────────────────────────────────────────┘
```

## Module structure

```
src/pmhedge/crypto_arb/
├── __init__.py
├── config.py                   # constants, thresholds, fees
├── clients/
│   ├── deribit.py              # REST + WS client option chain
│   ├── polymarket_crypto.py    # extends polymarket_client.py for crypto
│   └── hyperliquid.py          # perp execution + funding
├── pricing/
│   ├── svi.py                  # SVI parametric smile fitter
│   ├── density.py              # Breeden-Litzenberger extraction
│   ├── bracket_pricer.py       # fair_prob + Greeks for digital double
│   ├── fees.py                 # exact Polymarket fee formula
│   └── edge.py                 # edge_brut, edge_net, signal generation
├── hedge/
│   ├── greeks.py               # bracket + portfolio Greeks
│   ├── optimizer.py            # cvxpy hedge optimization
│   ├── executor.py             # multi-venue order routing
│   └── instruments.py          # hedge instrument catalog
├── portfolio/
│   ├── sizing.py               # Kelly multi-asset + Ledoit-Wolf shrinkage
│   ├── rebalancer.py           # continuous rebalance loop
│   ├── risk.py                 # DD, position limits, kill-switch
│   └── state.py                # portfolio state, persistence
├── scripts/
│   ├── snapshot.py             # ingest universe + smile, store DB
│   ├── validate_edge.py        # Phase 1: 24h snapshot validation
│   ├── backtest.py             # historical replay
│   ├── paper_trade.py          # Phase 4: paper trading runner
│   └── live_runner.py          # Phase 5: live trading
└── tests/
    ├── test_svi.py
    ├── test_density.py
    ├── test_bracket_pricer.py
    ├── test_fees.py
    ├── test_optimizer.py
    └── test_sizing.py
```

## Storage : DuckDB

Tables :

```sql
CREATE TABLE deribit_smile_snapshots (
    snapshot_ts TIMESTAMP,
    asset VARCHAR,            -- BTC or ETH
    expiry TIMESTAMP,
    spot DOUBLE,
    svi_a DOUBLE,
    svi_b DOUBLE,
    svi_rho DOUBLE,
    svi_m DOUBLE,
    svi_sigma DOUBLE,
    raw_chain JSONB           -- raw option chain for replay
);

CREATE TABLE polymarket_crypto_brackets (
    snapshot_ts TIMESTAMP,
    market_id VARCHAR,
    token_id VARCHAR,
    asset VARCHAR,
    strike_lo DOUBLE,
    strike_hi DOUBLE,
    expiry TIMESTAMP,
    yes_price DOUBLE,
    no_price DOUBLE,
    bid_depth_usd DOUBLE,
    ask_depth_usd DOUBLE,
    volume_24h DOUBLE
);

CREATE TABLE edge_history (
    snapshot_ts TIMESTAMP,
    market_id VARCHAR,
    poly_price DOUBLE,
    fair_prob DOUBLE,
    edge_brut DOUBLE,
    fee_pct DOUBLE,
    edge_net DOUBLE,
    delta DOUBLE,
    gamma DOUBLE,
    vega DOUBLE
);

CREATE TABLE positions (
    position_id VARCHAR PRIMARY KEY,
    open_ts TIMESTAMP,
    close_ts TIMESTAMP,
    market_id VARCHAR,
    side VARCHAR,             -- yes/no
    size_shares DOUBLE,
    entry_price DOUBLE,
    exit_price DOUBLE,
    fee_paid DOUBLE,
    realized_pnl DOUBLE,
    status VARCHAR            -- open/closed/settled
);

CREATE TABLE hedges (
    hedge_id VARCHAR PRIMARY KEY,
    open_ts TIMESTAMP,
    close_ts TIMESTAMP,
    venue VARCHAR,            -- deribit/hyperliquid
    instrument VARCHAR,
    side VARCHAR,
    size DOUBLE,
    entry_price DOUBLE,
    exit_price DOUBLE,
    fee_paid DOUBLE,
    realized_pnl DOUBLE,
    linked_position_ids VARCHAR[]
);

CREATE TABLE portfolio_snapshots (
    ts TIMESTAMP,
    total_capital DOUBLE,
    poly_capital DOUBLE,
    deribit_capital DOUBLE,
    hyperliquid_capital DOUBLE,
    n_positions INT,
    portfolio_delta DOUBLE,
    portfolio_gamma DOUBLE,
    portfolio_vega DOUBLE,
    realized_pnl_today DOUBLE,
    unrealized_pnl DOUBLE,
    drawdown DOUBLE
);
```

## Latency budget

Pas critique pour cette stratégie (rebalance 60s). Mais pour info :

- Deribit option chain pull : 200-500ms
- SVI fit (per asset+expiry) : 5-20ms
- Density + bracket pricing : 1-5ms par bracket × 100 = 100-500ms
- Cvxpy hedge optim : 50-200ms
- **Total cycle : 1-2s** — largement sous 60s budget

## Risk controls

- Max DD : 30% capital → halt 24h
- Per-position cap : 5% capital
- Total exposure cap : 80% capital
- Pin risk filter : skip si |S - K_proche| < 0.5σ√T
- Vol-of-vol filter : reduce size 50% J-2 avant FOMC/CPI
- Hard kill : move >2σ en 60s → close all

## Related

- [[_MOC]]
- [[math-pricing-hedge]]
- [[risks-mitigation]]
- [[roadmap]]
- [[../architecture]] — strat météo existante (référence)
