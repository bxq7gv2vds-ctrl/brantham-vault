---
type: assumption
date: 2026-05-23
status: testing
confidence: low
tags: [quant-research, hyperliquid, scalping]
---

# HYPE Order Flow Contains Executable Scalping Alpha

## Hypothesis

Hyperliquid `HYPE` order-book and aggressor-flow data, potentially combined
with spot/perpetual lead-lag, contain an ultra-short-horizon trading signal
that remains positive after executable bid/ask pricing, latency, fees,
slippage and capacity limits.

## Current Evidence

The first `hyperflow` live capture produced 239 HYPE feature observations for a
chronological grid study. Across 60 exploratory taker/taker configurations,
zero were positive on training data and zero were positive on the test period.
The best training-ranked candidate produced `-9.203 bps` on train and
`-10.217 bps` on test after the base perp taker fee assumption.

This sample is far too short to reject the broader hypothesis, but it rejects
any immediate capital deployment based on the current taker continuation rule.

## Next Tests

- Accumulate at least seven days of continuous HYPE perp and `@107` spot data.
- Test spot-to-perp lead-lag, absorption reversal and liquidity-vacuum signals.
- Model maker fills and adverse selection independently of taker strategies.
- Require positive unseen-sample performance under realistic latency stress
  before paper execution.

## Related

- [[_system/MOC-assumptions]]
- [[_system/MOC-decisions]]
- [[founder/decisions/2026-05-23-hyperflow-rust-research-engine]]
- [[founder/strategy/current-strategy]]
