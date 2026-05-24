---
name: Hyperflow Adaptive Maker Hedged Architecture
type: decision
date: 2026-05-24
status: approved
tags: [founder, quant-research, hyperliquid, market-making]
---

# Build Hyperflow As An Adaptive Maker-First Hedged Platform

**Date**: 2026-05-24
**Status**: Approved
**Decision Maker**: Paul
**Impacted by**: [[founder/assumptions/hype-order-flow-scalping-alpha]]

## Context

Initial HYPE order-flow research detects occasional gross effects but taker
fees and time-regime instability eliminate a deployable edge. Two reviewed
grid papers support dynamic grid spacing and risk controls, but do not model
Hyperliquid queue position, passive fills, adverse selection or executable
hedges.

## Decision

**Chosen**: Build the next research layer as an adaptive maker-first platform
on HYPE, with optional executable beta hedges in BTC, ETH or SOL.

The platform must separate:

- residual alpha prediction;
- maker fill and queue estimation;
- post-fill adverse-selection prediction;
- volatility/regime classification;
- inventory and hedge optimization;
- independent hard risk controls.

The quote engine may use only positive expected net value after maker fees,
hedge cost, adverse selection, inventory risk and operational buffers. Static
loss-averaging grids and optimistic touch-fill backtests are rejected.

## Rationale

The current learned taker baseline is approximately flat after fees while its
gross counterpart remains materially positive. A maker-first hypothesis is
therefore economically testable, but only with conservative fill replay and
future unseen validation. Complexity is justified only where it improves
measurement of executable net PnL and controlled risk.

## Action Items

- [x] Capture HYPE, spot @107, BTC, ETH and SOL contemporaneously.
- [x] Specify the platform architecture and validation gates in
  `hyperflow/docs/ADAPTIVE_MARKET_MAKING_ARCHITECTURE.md`.
- [ ] Implement deterministic maker replay with conservative queue fills.
- [ ] Implement inventory-aware dynamic grid and symmetric-grid baseline.
- [ ] Implement HYPE residual hedge evaluation with two-leg cost accounting.
- [ ] Add private paper fill/order telemetry before any live quote submission.
- [ ] Consider local non-validating node infrastructure after maker-paper
  evidence justifies it.

## Related

- [[_system/MOC-decisions]]
- [[_system/MOC-assumptions]]
- [[founder/decisions/2026-05-23-hyperflow-rust-research-engine]]
- [[founder/assumptions/hype-order-flow-scalping-alpha]]
