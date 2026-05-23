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

A subsequent event-based liquidity-pattern scan on the same closed dataset
found two gross candidates after bid/ask but before fees:
`microprice_momentum` at `+2.606 bps` test and `liquidity_vacuum` at
`+1.608 bps` test. Both are far below the approximately `9 bps` base
taker/taker fee hurdle, and the test trade counts remain too small for
inference. They justify maker-fill research, not capital deployment.

With a less permissive minimum of `30` training trades, the selected
event-pattern candidate is `ofi`; it records `-9.603 bps` on test after fees
and `-0.602 bps` even with fees removed. Continuous collection now rolls closed
segments every fifteen minutes and reruns the screen automatically.

Reverse-engineering additions now screen extreme-event continuation versus
reversal, asymmetric tails, spot-to-perp lead-lag and outcome-conditioned
precursors. On an exploratory immutable snapshot of `2,603` HYPE observations,
large executable upward moves (`>9 bps`) were preceded by strongly positive
liquidity-vacuum readings, suggesting thin asks as a candidate trigger.
However, the corresponding asymmetric `positive liquidity_vacuum -> long`
rule lost `-0.975 bps` on test even before fees and `-9.974 bps` after fees.
This signature remains a monitored hypothesis only.

Crossed-feature screening is now implemented. In exploratory snapshots, no
two-factor strategy is positive and sufficiently frequent on train after
taker fees. Before fees, interactions such as `OFI` with
`microprice_momentum` can be mildly positive in train (`+1.554 bps`) but
remain negative on test (`-0.830 bps`). The working implication is unchanged:
crossed signals may only justify maker-model research if the gross effect
persists on closed multi-day data.

The first automatically closed fifteen-minute segment increased the
reproducible feature sample to `1,905` observations. Across `540` crossed
feature strategies, none were positive and sufficiently frequent on training
data after taker fees. Without fees, the selected
`microprice_momentum`/`trade_momentum` interaction returned `+2.092 bps` on
train but `-0.304 bps` on test. This weakens the case for further taker-rule
combinatorics and elevates maker-fill/adverse-selection modeling as the next
required experiment.

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
