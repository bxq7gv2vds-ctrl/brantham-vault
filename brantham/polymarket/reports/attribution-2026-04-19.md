---
name: P&L Attribution
description: Breakdown by alpha x city x hour x dow on settled paper outcomes
generated: 2026-04-19T17:48:30.161855+00:00
type: report
---

# Attribution Breakdown

**Overall:** N=992 WR=82.1% P&L=$+13299.23

## Top by (alpha × city) — by P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | austin | 82 | 93.9% [86.5, 97.4] | $+12740.12 |
| MODEL_VS_MARKET | atlanta | 71 | 100.0% [94.9, 100.0] | $+530.47 |
| MODEL_VS_MARKET | beijing | 52 | 98.1% [89.9, 99.7] | $+396.99 |
| MODEL_VS_MARKET | houston | 61 | 98.4% [91.3, 99.7] | $+237.13 |
| MODEL_VS_MARKET | san francisco | 48 | 100.0% [92.6, 100.0] | $+181.69 |
| MODEL_VS_MARKET | shenzhen | 56 | 96.4% [87.9, 99.0] | $+163.64 |
| MODEL_VS_MARKET | dallas | 77 | 76.6% [66.0, 84.7] | $+143.28 |
| MODEL_VS_MARKET | denver | 57 | 100.0% [93.7, 100.0] | $+127.32 |

## Bottom by (alpha × city) — P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | hong kong | 22 | 100.0% [85.1, 100.0] | $+22.72 |
| MODEL_VS_MARKET | tel aviv | 19 | 100.0% [83.2, 100.0] | $+15.84 |
| CONFIRMED_NO | miami | 10 | 100.0% [72.2, 100.0] | $+10.30 |
| MODEL_VS_MARKET | miami | 33 | 97.0% [84.7, 99.5] | $-4.35 |
| CONFIRMED_YES | new york city | 13 | 0.0% [0.0, 22.8] | $-204.96 |
| CONFIRMED_YES | miami | 18 | 0.0% [0.0, 17.6] | $-238.92 |
| MODEL_VS_MARKET | chicago | 41 | 34.1% [21.6, 49.5] | $-275.15 |
| MODEL_VS_MARKET | tokyo | 83 | 0.0% [0.0, 4.4] | $-979.01 |

## Insufficient data (N < 10) — suppressed from ranking

- 9 (alpha × city) buckets with fewer than 10 outcomes; do not draw conclusions yet.

## Candidates to retire (N≥30, WR<50%)

- `MODEL_VS_MARKET` × **chicago** : N=41, WR=34.1%, P&L=$-275.15
- `MODEL_VS_MARKET` × **tokyo** : N=83, WR=0.0%, P&L=$-979.01

## By (alpha × hour UTC)

| Alpha | Hour | N | WR | P&L |
|-------|------|---|-----|-----|
| MODEL_VS_MARKET | 20h | 158 | 80.4% | $+3946.78 |
| MODEL_VS_MARKET | 21h | 145 | 82.8% | $+3320.43 |
| MODEL_VS_MARKET | 19h | 91 | 80.2% | $+2252.91 |
| MODEL_VS_MARKET | 22h | 145 | 89.7% | $+1682.81 |
| MODEL_VS_MARKET | 23h | 169 | 91.7% | $+1381.52 |
| MODEL_VS_MARKET | 14h | 34 | 79.4% | $+417.14 |
| MODEL_VS_MARKET | 00h | 54 | 83.3% | $+375.84 |
| MODEL_VS_MARKET | 03h | 9 | 88.9% | $+262.19 |

## Related
- [[_MOC|Polymarket Hub]]
- [[STATE-HANDOFF|State handoff]]
- [[audit-hedge-fund-grade|Audit hedge fund grade]]
