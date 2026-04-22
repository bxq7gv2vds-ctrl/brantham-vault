---
name: P&L Attribution
description: Breakdown by alpha x city x hour x dow on settled paper outcomes
generated: 2026-04-22T07:45:05.559558+00:00
type: report
---

# Attribution Breakdown

**Overall:** N=1768 WR=82.2% P&L=$+18893.52

## Top by (alpha × city) — by P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | austin | 112 | 79.5% [71.1, 85.9] | $+16790.10 |
| MODEL_VS_MARKET | atlanta | 138 | 96.4% [91.8, 98.4] | $+1122.75 |
| MODEL_VS_MARKET | dallas | 131 | 86.3% [79.3, 91.1] | $+694.10 |
| MODEL_VS_MARKET | houston | 117 | 91.5% [85.0, 95.3] | $+547.04 |
| MODEL_VS_MARKET | los angeles | 121 | 96.7% [91.8, 98.7] | $+471.13 |
| MODEL_VS_MARKET | beijing | 59 | 88.1% [77.5, 94.1] | $+351.60 |
| MODEL_VS_MARKET | san francisco | 119 | 89.1% [82.2, 93.5] | $+278.82 |
| MODEL_VS_MARKET | shenzhen | 57 | 96.5% [88.1, 99.0] | $+164.82 |
| MODEL_VS_MARKET | denver | 70 | 100.0% [94.8, 100.0] | $+152.76 |
| MODEL_VS_MARKET | chongqing | 31 | 100.0% [89.0, 100.0] | $+112.60 |
| MODEL_VS_MARKET | new york city | 66 | 95.5% [87.5, 98.4] | $+103.03 |
| MODEL_VS_MARKET | seoul | 15 | 100.0% [79.6, 100.0] | $+102.94 |
| MODEL_VS_MARKET | buenos aires | 30 | 100.0% [88.6, 100.0] | $+95.84 |
| MODEL_VS_MARKET | kuala lumpur | 34 | 100.0% [89.8, 100.0] | $+92.68 |
| MODEL_VS_MARKET | warsaw | 16 | 100.0% [80.6, 100.0] | $+85.79 |

## Bottom by (alpha × city) — P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | lucknow | 49 | 100.0% [92.7, 100.0] | $+54.67 |
| MODEL_VS_MARKET | mexico city | 58 | 79.3% [67.2, 87.7] | $+47.31 |
| CONFIRMED_NO | atlanta | 19 | 100.0% [83.2, 100.0] | $+38.24 |
| CONFIRMED_NO | miami | 37 | 100.0% [90.6, 100.0] | $+35.67 |
| MODEL_VS_MARKET | hong kong | 35 | 100.0% [90.1, 100.0] | $+34.52 |
| MODEL_VS_MARKET | paris | 19 | 100.0% [83.2, 100.0] | $+31.73 |
| MODEL_VS_MARKET | wuhan | 10 | 100.0% [72.2, 100.0] | $+28.83 |
| CONFIRMED_NO | houston | 27 | 100.0% [87.5, 100.0] | $+23.66 |
| MODEL_VS_MARKET | helsinki | 19 | 100.0% [83.2, 100.0] | $+18.80 |
| MODEL_VS_MARKET | tel aviv | 19 | 100.0% [83.2, 100.0] | $+15.84 |
| CONFIRMED_YES | new york city | 13 | 0.0% [0.0, 22.8] | $-204.96 |
| CONFIRMED_YES | miami | 18 | 0.0% [0.0, 17.6] | $-238.92 |
| MODEL_VS_MARKET | wellington | 28 | 0.0% [0.0, 12.1] | $-519.24 |
| MODEL_VS_MARKET | chicago | 69 | 21.7% [13.6, 32.8] | $-641.82 |
| MODEL_VS_MARKET | tokyo | 94 | 1.1% [0.2, 5.8] | $-1071.81 |

## Insufficient data (N < 10) — suppressed from ranking

- 13 (alpha × city) buckets with fewer than 10 outcomes; do not draw conclusions yet.

## Candidates to retire (N≥30, WR<50%)

- `MODEL_VS_MARKET` × **chicago** : N=69, WR=21.7%, P&L=$-641.82
- `MODEL_VS_MARKET` × **tokyo** : N=94, WR=1.1%, P&L=$-1071.81

## By (alpha × hour UTC)

| Alpha | Hour | N | WR | P&L |
|-------|------|---|-----|-----|
| MODEL_VS_MARKET | 20h | 158 | 80.4% | $+3946.78 |
| MODEL_VS_MARKET | 21h | 145 | 82.8% | $+3320.43 |
| MODEL_VS_MARKET | 17h | 146 | 80.8% | $+2794.52 |
| MODEL_VS_MARKET | 19h | 93 | 80.6% | $+2271.63 |
| MODEL_VS_MARKET | 22h | 145 | 89.7% | $+1682.81 |
| MODEL_VS_MARKET | 16h | 206 | 78.6% | $+1588.08 |
| MODEL_VS_MARKET | 23h | 169 | 91.7% | $+1381.52 |
| MODEL_VS_MARKET | 15h | 54 | 83.3% | $+613.34 |
| MODEL_VS_MARKET | 14h | 43 | 83.7% | $+472.19 |
| MODEL_VS_MARKET | 00h | 54 | 83.3% | $+375.84 |
| MODEL_VS_MARKET | 03h | 9 | 88.9% | $+262.19 |
| MODEL_VS_MARKET | 13h | 135 | 85.9% | $+236.59 |
| MODEL_VS_MARKET | 01h | 34 | 94.1% | $+111.57 |
| MODEL_VS_MARKET | 18h | 41 | 82.9% | $+104.90 |
| MODEL_VS_MARKET | 02h | 29 | 86.2% | $+93.95 |

## Related
- [[_MOC|Polymarket Hub]]
- [[STATE-HANDOFF|State handoff]]
- [[audit-hedge-fund-grade|Audit hedge fund grade]]
