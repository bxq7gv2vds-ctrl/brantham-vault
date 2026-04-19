---
name: Paper vs Live-net P&L
description: Realistic slippage haircut on settled paper outcomes
generated: 2026-04-19T17:47:37.535210+00:00
type: report
---

# Paper vs Live-net — 2026-04-19

Slippage params: spread_cts=2.0, fill_ratio=0.8, pct_rejected=0.05, resolution_cost=0.01

**Paper P&L**  : $+915.14  (WR 83.9%)
**Live  P&L**  : $+544.73  (WR 79.3%)
**Haircut**    : $+370.41

## By alpha

| Alpha | N | Paper | Live | Haircut % |
|-------|---|-------|------|-----------|
| CONFIRMED_NO | 14 | $+28.16 | $+18.44 | +34.5% |
| CONFIRMED_YES | 14 | $-186.78 | $-128.34 | -31.3% |
| MODEL_VS_MARKET | 189 | $+1073.76 | $+654.63 | +39.0% |
