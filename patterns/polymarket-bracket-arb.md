---
title: Polymarket Bracket Arb — Temperature Markets
type: pattern
project: polymarket-hedge
date: 2026-03-30
---

# Pattern: Polymarket Temperature Bracket Arbitrage

## Signal Logic

Temperature markets on Polymarket come in sets of ~9 brackets per city+date:
- "≤5°C" / "6°C" / "7°C" / ... / "≥12°C"
- These form a complete partition — sum of YES prices should = 1.0

**Arb trigger**: `|sum - 1.0| > 0.02`
- sum > 1.02 → SELL the most overpriced bracket (price furthest above fair = price/sum)
- sum < 0.98 → BUY the most underpriced bracket

**P&L**: Acts as directional bet + arb. When the overpriced bracket resolves NO (price → 0), captures the full 0.9→0 swing. ~63-84% win rate in backtests.

## Implementation Notes

```python
# From backtester.py _scan_bracket_arb:
total = sum(prices.values())   # sum of YES prices for all brackets in city+date
violation = total - 1.0

if violation > 0.02:
    # SELL the most overpriced token
    candidate = max(group, key=lambda m: prices[m.token_id_yes])
    fair = p_mkt / total
    edge = p_mkt - fair
    target = max(p_mkt - edge * 0.8, 0.01)
    stop   = min(p_mkt + edge * 0.5, 0.99)
```

## Scan Frequency

- Every 50 price events (not just during NWP_JUMP)
- Also triggered on each NWP_JUMP event for the same city+date group

## Backtest Results (March 2026)

- 265 trades, 63.4% win rate, +6792 USDC (on 10k bankroll)
- Best params: `min_edge=0.03`, `bracket_arb_ttl_min=152`, `kelly=0.40`

## Caveats

1. **Short-only dominant**: Sum > 1 more common than < 1. All top wins are SELL positions.
2. **Near-resolution amplification**: Overpriced brackets near resolution swing from 0.9→0 = big P&L
3. **Depends on data freshness**: Requires live price cache with multiple brackets per group

## Related

- [[vault/patterns/polymarket-intraday-architecture]]
- [[vault/founder/sessions/2026-03-30-polymarket-backtest]]
- [[vault/_system/MOC-patterns]]
