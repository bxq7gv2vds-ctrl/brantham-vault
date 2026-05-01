---
name: P&L Attribution
description: Breakdown by alpha x city x hour x dow on settled paper outcomes
generated: 2026-05-01T07:46:02.502348+00:00
type: report
---

# Attribution Breakdown

**Overall:** N=2672 WR=81.4% P&L=$+17799.47

## Top by (alpha × city) — by P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | austin | 112 | 79.5% [71.1, 85.9] | $+16790.10 |
| MODEL_VS_MARKET | atlanta | 138 | 96.4% [91.8, 98.4] | $+1122.75 |
| MODEL_VS_MARKET | san francisco | 172 | 92.4% [87.5, 95.5] | $+1069.87 |
| MODEL_VS_MARKET | dallas | 148 | 87.8% [81.6, 92.2] | $+734.12 |
| MODEL_VS_MARKET | houston | 129 | 91.5% [85.4, 95.2] | $+564.28 |
| MODEL_VS_MARKET | beijing | 59 | 88.1% [77.5, 94.1] | $+351.60 |
| CONFIRMED_NO | atlanta | 103 | 100.0% [96.4, 100.0] | $+216.92 |
| CONFIRMED_NO | miami | 110 | 100.0% [96.6, 100.0] | $+188.94 |
| CONFIRMED_NO | new york city | 71 | 100.0% [94.9, 100.0] | $+173.66 |
| MODEL_VS_MARKET | shenzhen | 57 | 96.5% [88.1, 99.0] | $+164.82 |
| MODEL_VS_MARKET | denver | 70 | 100.0% [94.8, 100.0] | $+152.76 |
| MODEL_VS_MARKET | miami | 67 | 98.5% [92.0, 99.7] | $+139.32 |
| MODEL_VS_MARKET | seoul | 33 | 100.0% [89.6, 100.0] | $+138.06 |
| MODEL_VS_MARKET | warsaw | 35 | 100.0% [90.1, 100.0] | $+126.21 |
| MODEL_VS_MARKET | chongqing | 31 | 100.0% [89.0, 100.0] | $+112.60 |

## Bottom by (alpha × city) — P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | helsinki | 19 | 100.0% [83.2, 100.0] | $+18.80 |
| CONFIRMED_NO | wuhan | 11 | 100.0% [74.1, 100.0] | $+17.71 |
| MODEL_VS_MARKET | tel aviv | 19 | 100.0% [83.2, 100.0] | $+15.84 |
| CONFIRMED_NO | chengdu | 13 | 100.0% [77.2, 100.0] | $+7.43 |
| MODEL_VS_MARKET | ankara | 20 | 90.0% [69.9, 97.2] | $-4.02 |
| MODEL_VS_MARKET | moscow | 16 | 68.8% [44.4, 85.8] | $-14.71 |
| CONFIRMED_YES | new york city | 13 | 0.0% [0.0, 22.8] | $-204.96 |
| CONFIRMED_YES | miami | 18 | 0.0% [0.0, 17.6] | $-238.92 |
| MODEL_VS_MARKET | seattle | 49 | 59.2% [45.2, 71.8] | $-240.71 |
| CONFIRMED_NO | buenos aires | 25 | 0.0% [0.0, 13.3] | $-349.63 |
| MODEL_VS_MARKET | wellington | 28 | 0.0% [0.0, 12.1] | $-519.24 |
| MODEL_VS_MARKET | chicago | 69 | 21.7% [13.6, 32.8] | $-641.82 |
| CONFIRMED_NO | mexico city | 89 | 5.6% [2.4, 12.5] | $-672.86 |
| MODEL_VS_MARKET | tokyo | 94 | 1.1% [0.2, 5.8] | $-1071.81 |
| MODEL_VS_MARKET | los angeles | 172 | 69.2% [61.9, 75.6] | $-1339.13 |

## Insufficient data (N < 10) — suppressed from ranking

- 10 (alpha × city) buckets with fewer than 10 outcomes; do not draw conclusions yet.

## Candidates to retire (N≥30, WR<50%)

- `MODEL_VS_MARKET` × **chicago** : N=69, WR=21.7%, P&L=$-641.82
- `MODEL_VS_MARKET` × **tokyo** : N=94, WR=1.1%, P&L=$-1071.81
- `CONFIRMED_NO` × **mexico city** : N=89, WR=5.6%, P&L=$-672.86

## By (alpha × hour UTC)

| Alpha | Hour | N | WR | P&L |
|-------|------|---|-----|-----|
| MODEL_VS_MARKET | 20h | 183 | 82.5% | $+4039.75 |
| MODEL_VS_MARKET | 21h | 160 | 84.4% | $+3404.09 |
| MODEL_VS_MARKET | 17h | 146 | 80.8% | $+2794.52 |
| MODEL_VS_MARKET | 19h | 126 | 84.9% | $+2365.87 |
| MODEL_VS_MARKET | 22h | 145 | 89.7% | $+1682.81 |
| MODEL_VS_MARKET | 16h | 207 | 78.3% | $+1538.08 |
| MODEL_VS_MARKET | 23h | 170 | 91.2% | $+1353.87 |
| MODEL_VS_MARKET | 15h | 59 | 83.1% | $+581.59 |
| MODEL_VS_MARKET | 00h | 54 | 83.3% | $+375.84 |
| MODEL_VS_MARKET | 03h | 9 | 88.9% | $+262.19 |
| MODEL_VS_MARKET | 01h | 35 | 94.3% | $+114.48 |
| MODEL_VS_MARKET | 18h | 44 | 84.1% | $+110.79 |
| CONFIRMED_NO | 06h | 102 | 88.2% | $+96.72 |
| MODEL_VS_MARKET | 02h | 29 | 86.2% | $+93.95 |
| CONFIRMED_NO | 05h | 77 | 84.4% | $+68.00 |

## Related
- [[_MOC|Polymarket Hub]]
- [[STATE-HANDOFF|State handoff]]
- [[audit-hedge-fund-grade|Audit hedge fund grade]]
