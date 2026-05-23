---
name: Hyperflow Rust Research Engine
type: decision
date: 2026-05-23
status: approved
tags: [founder, quant-research, hyperliquid]
---

# Isolate Hyperflow As A Rust Research Engine

**Date**: 2026-05-23
**Status**: Approved
**Decision Maker**: Paul
**Impacted by**: [[_system/MOC-assumptions]]

## Context

A research tool is required to capture Hyperliquid HYPE spot and perpetual
microstructure data, calculate footprint/order-flow features and evaluate
ultra-short-horizon strategies after fees and latency. Existing local trading
projects are either oriented toward other markets or already carry substantial
uncommitted work.

## Options Considered

1. Extend `polymarket-hedge`: reuses some quantitative utilities, but mixes a
   distinct market-data problem into a dirty and unrelated working tree.
2. Extend `crypto-tracker`: small Python tracker, not structured for tick/L2
   event capture or latency-sensitive research.
3. Create `hyperflow`: isolated Rust live-data and research foundation with
   explicit raw-data preservation and backtest gates.

## Decision

**Chosen**: Create `hyperflow` as an isolated Rust project.

**Reasoning**: Rust provides an appropriate live-capture path, while an
isolated project avoids coupling this personal quant research to the existing
Polymarket and Brantham work. Trading execution is intentionally deferred until
data collection and out-of-sample testing demonstrate net alpha.

## Action Items

- [x] Implement public WebSocket capture for HYPE perp and spot.
- [x] Implement footprint features and a latency/fee-aware baseline backtest.
- [ ] Collect multi-day live data and assess signal stability.
- [ ] Consider local non-validating node infrastructure only after public-feed
  evidence justifies the operational cost.

## Related

- [[_system/MOC-decisions]]
- [[_system/MOC-master]]
- [[founder/strategy/current-strategy]]
- [[_system/MOC-assumptions|Related Assumptions]]
