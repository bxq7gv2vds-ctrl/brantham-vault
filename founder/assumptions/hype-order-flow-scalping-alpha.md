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
with spot/perpetual lead-lag, contain an intraminute-to-multiminute trading
signal that remains positive after executable bid/ask pricing, latency, fees,
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

The research horizon was then shifted from seconds to holds of `30s`, `1m`,
`2m`, `3m` and `5m`, while retaining fast liquidity states as entry triggers.
At a `1m` markout, `960` observations moved beyond the `9 bps` taker/taker
hurdle, compared with only `73` at `5s`, so minute holds are the appropriate
next testing regime. The diagnostic scan with a relaxed `10`-trade train gate
selected `trade_momentum` reversal at `1m`: it returned `+7.474 bps` on only
four test trades before fees, but `-1.528 bps` after taker fees. Under the
proper `30`-trade gate, the next completed segment increased the reproducible
sample to `3,165` observations and made minute-scale rules eligible. The
selected `depth_momentum` rule at a `30s` hold lost `-11.403 bps` on test
after taker fees and `-2.403 bps` even with fees removed. The zero-fee crossed
rule also lost `-4.559 bps` on test. This is a lead for accumulation and
maker-fill modeling, not deployment evidence.

A dedicated long-only pre-pump scanner now tests rolling order-flow context
windows of `5s`, `15s` and `30s` before executable upside moves across the
minute hold grid. It requires positive training PnL, lift above the
unconditional pump rate and the trade-count gate. Across `2,160` candidate
signatures on the `3,165`-observation closed sample, no rule passes those
requirements after taker fees. With fees removed, the selected
`microprice_momentum` negative-tail pattern over `5s` returned `+1.529 bps`
and `1.090` lift on training, then `-0.793 bps` and `0.300` lift on test.
There is no reproducible pre-pump trigger yet.

After accumulation to `30,889` closed HYPE observations, a causal learned
baseline was introduced. It forecasts net executable long and short returns
from rolling order-flow features, selecting hold, ridge regularization and
entry threshold on validation only before one final test. The selected
taker/taker model uses a `5m` hold and is only marginally positive on its final
test: `+0.110 bps` over `32` trades after modeled fees, versus `+9.115 bps`
for the corresponding gross/no-fee evaluation. Alternate chronological
boundaries fail (`-26.268 bps` on one test split; no eligible validation model
on two others). This is evidence of a gross microstructure effect consumed by
fees and regime instability, not an investable model.

The collector now records `BTC`, `ETH` and `SOL` perps alongside `HYPE` and
spot `@107`. This enables the next falsifiable hedge experiment: whether a
HYPE order-flow signal remains net positive after neutralizing common crypto
market movement with an executable second leg and fees on both legs.

## Next Tests

- Accumulate at least seven days of continuous HYPE perp and `@107` spot data.
- Test spot-to-perp lead-lag, absorption reversal and liquidity-vacuum signals.
- Model maker fills and adverse selection independently of taker strategies.
- Evaluate HYPE residual-return models against simultaneous `BTC`/`ETH`/`SOL`
  hedge legs once a sufficient multi-asset closed sample exists.
- Require positive unseen-sample performance under realistic latency stress
  before paper execution.

## Related

- [[_system/MOC-assumptions]]
- [[_system/MOC-decisions]]
- [[founder/decisions/2026-05-23-hyperflow-rust-research-engine]]
- [[founder/strategy/current-strategy]]
