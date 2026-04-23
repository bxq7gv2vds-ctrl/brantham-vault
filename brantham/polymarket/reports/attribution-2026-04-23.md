---
name: P&L Attribution
description: Breakdown by alpha x city x hour x dow on settled paper outcomes
generated: 2026-04-23T08:00:41.191988+00:00
type: report
---

# Attribution Breakdown

**Overall:** N=2455 WR=82.0% P&L=$+18636.62

## Top by (alpha × city) — by P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | austin | 112 | 79.5% [71.1, 85.9] | $+16790.10 |
| MODEL_VS_MARKET | atlanta | 138 | 96.4% [91.8, 98.4] | $+1122.75 |
| MODEL_VS_MARKET | dallas | 131 | 86.3% [79.3, 91.1] | $+694.10 |
| MODEL_VS_MARKET | houston | 127 | 92.1% [86.1, 95.7] | $+590.24 |
| MODEL_VS_MARKET | los angeles | 123 | 95.9% [90.8, 98.3] | $+477.65 |
| MODEL_VS_MARKET | beijing | 59 | 88.1% [77.5, 94.1] | $+351.60 |
| MODEL_VS_MARKET | san francisco | 133 | 90.2% [84.0, 94.2] | $+332.76 |
| CONFIRMED_NO | atlanta | 103 | 100.0% [96.4, 100.0] | $+216.92 |
| CONFIRMED_NO | miami | 110 | 100.0% [96.6, 100.0] | $+188.94 |
| CONFIRMED_NO | new york city | 71 | 100.0% [94.9, 100.0] | $+173.66 |
| MODEL_VS_MARKET | shenzhen | 57 | 96.5% [88.1, 99.0] | $+164.82 |
| MODEL_VS_MARKET | denver | 70 | 100.0% [94.8, 100.0] | $+152.76 |
| MODEL_VS_MARKET | chongqing | 31 | 100.0% [89.0, 100.0] | $+112.60 |
| MODEL_VS_MARKET | new york city | 66 | 95.5% [87.5, 98.4] | $+103.03 |
| MODEL_VS_MARKET | seoul | 15 | 100.0% [79.6, 100.0] | $+102.94 |

## Bottom by (alpha × city) — P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | paris | 20 | 100.0% [83.9, 100.0] | $+33.17 |
| MODEL_VS_MARKET | wuhan | 10 | 100.0% [72.2, 100.0] | $+28.83 |
| CONFIRMED_NO | istanbul | 20 | 100.0% [83.9, 100.0] | $+22.27 |
| MODEL_VS_MARKET | helsinki | 19 | 100.0% [83.2, 100.0] | $+18.80 |
| CONFIRMED_NO | wuhan | 11 | 100.0% [74.1, 100.0] | $+17.71 |
| MODEL_VS_MARKET | tel aviv | 19 | 100.0% [83.2, 100.0] | $+15.84 |
| CONFIRMED_NO | chengdu | 13 | 100.0% [77.2, 100.0] | $+7.43 |
| CONFIRMED_YES | new york city | 13 | 0.0% [0.0, 22.8] | $-204.96 |
| CONFIRMED_YES | miami | 18 | 0.0% [0.0, 17.6] | $-238.92 |
| MODEL_VS_MARKET | seattle | 20 | 30.0% [14.5, 51.9] | $-255.03 |
| CONFIRMED_NO | buenos aires | 25 | 0.0% [0.0, 13.3] | $-349.63 |
| MODEL_VS_MARKET | wellington | 28 | 0.0% [0.0, 12.1] | $-519.24 |
| MODEL_VS_MARKET | chicago | 69 | 21.7% [13.6, 32.8] | $-641.82 |
| CONFIRMED_NO | mexico city | 89 | 5.6% [2.4, 12.5] | $-672.86 |
| MODEL_VS_MARKET | tokyo | 94 | 1.1% [0.2, 5.8] | $-1071.81 |

## Insufficient data (N < 10) — suppressed from ranking

- 13 (alpha × city) buckets with fewer than 10 outcomes; do not draw conclusions yet.

## Candidates to retire (N≥30, WR<50%)

- `MODEL_VS_MARKET` × **chicago** : N=69, WR=21.7%, P&L=$-641.82
- `MODEL_VS_MARKET` × **tokyo** : N=94, WR=1.1%, P&L=$-1071.81
- `CONFIRMED_NO` × **mexico city** : N=89, WR=5.6%, P&L=$-672.86

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
| MODEL_VS_MARKET | 15h | 55 | 83.6% | $+614.78 |
| MODEL_VS_MARKET | 14h | 43 | 83.7% | $+472.19 |
| MODEL_VS_MARKET | 00h | 54 | 83.3% | $+375.84 |
| MODEL_VS_MARKET | 03h | 9 | 88.9% | $+262.19 |
| MODEL_VS_MARKET | 13h | 135 | 85.9% | $+236.59 |
| MODEL_VS_MARKET | 01h | 34 | 94.1% | $+111.57 |
| MODEL_VS_MARKET | 18h | 41 | 82.9% | $+104.90 |
| CONFIRMED_NO | 06h | 102 | 88.2% | $+96.72 |

## Related
- [[_MOC|Polymarket Hub]]
- [[STATE-HANDOFF|State handoff]]
- [[audit-hedge-fund-grade|Audit hedge fund grade]]
