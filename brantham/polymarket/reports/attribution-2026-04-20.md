---
name: P&L Attribution
description: Breakdown by alpha x city x hour x dow on settled paper outcomes
generated: 2026-04-20T07:59:40.985620+00:00
type: report
---

# Attribution Breakdown

**Overall:** N=1113 WR=81.8% P&L=$+13324.69

## Top by (alpha × city) — by P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | austin | 100 | 77.0% [67.8, 84.2] | $+12381.96 |
| MODEL_VS_MARKET | atlanta | 88 | 100.0% [95.8, 100.0] | $+670.55 |
| MODEL_VS_MARKET | beijing | 52 | 98.1% [89.9, 99.7] | $+396.99 |
| MODEL_VS_MARKET | houston | 74 | 98.6% [92.7, 99.8] | $+273.75 |
| MODEL_VS_MARKET | san francisco | 62 | 100.0% [94.2, 100.0] | $+267.25 |
| MODEL_VS_MARKET | los angeles | 79 | 94.9% [87.7, 98.0] | $+192.28 |
| MODEL_VS_MARKET | shenzhen | 56 | 96.4% [87.9, 99.0] | $+163.64 |
| MODEL_VS_MARKET | denver | 70 | 100.0% [94.8, 100.0] | $+152.76 |
| MODEL_VS_MARKET | dallas | 77 | 76.6% [66.0, 84.7] | $+143.28 |
| MODEL_VS_MARKET | kuala lumpur | 33 | 100.0% [89.6, 100.0] | $+88.66 |
| CONFIRMED_NO | denver | 30 | 100.0% [88.6, 100.0] | $+59.98 |
| MODEL_VS_MARKET | new york city | 17 | 88.2% [65.7, 96.7] | $+54.07 |
| MODEL_VS_MARKET | lucknow | 48 | 100.0% [92.6, 100.0] | $+53.53 |
| MODEL_VS_MARKET | paris | 19 | 100.0% [83.2, 100.0] | $+31.73 |
| MODEL_VS_MARKET | miami | 40 | 97.5% [87.1, 99.6] | $+25.24 |

## Bottom by (alpha × city) — P&L (N ≥ 10)

| Alpha | City | N | WR (95 % CI) | P&L |
|-------|------|---|--------------|-----|
| MODEL_VS_MARKET | kuala lumpur | 33 | 100.0% [89.6, 100.0] | $+88.66 |
| CONFIRMED_NO | denver | 30 | 100.0% [88.6, 100.0] | $+59.98 |
| MODEL_VS_MARKET | new york city | 17 | 88.2% [65.7, 96.7] | $+54.07 |
| MODEL_VS_MARKET | lucknow | 48 | 100.0% [92.6, 100.0] | $+53.53 |
| MODEL_VS_MARKET | paris | 19 | 100.0% [83.2, 100.0] | $+31.73 |
| MODEL_VS_MARKET | miami | 40 | 97.5% [87.1, 99.6] | $+25.24 |
| MODEL_VS_MARKET | mexico city | 17 | 88.2% [65.7, 96.7] | $+24.74 |
| CONFIRMED_NO | atlanta | 11 | 100.0% [74.1, 100.0] | $+24.48 |
| MODEL_VS_MARKET | hong kong | 22 | 100.0% [85.1, 100.0] | $+22.72 |
| MODEL_VS_MARKET | tel aviv | 19 | 100.0% [83.2, 100.0] | $+15.84 |
| CONFIRMED_NO | miami | 10 | 100.0% [72.2, 100.0] | $+10.30 |
| CONFIRMED_YES | new york city | 13 | 0.0% [0.0, 22.8] | $-204.96 |
| CONFIRMED_YES | miami | 18 | 0.0% [0.0, 17.6] | $-238.92 |
| MODEL_VS_MARKET | chicago | 44 | 31.8% [20.0, 46.6] | $-335.58 |
| MODEL_VS_MARKET | tokyo | 85 | 0.0% [0.0, 4.3] | $-1013.16 |

## Insufficient data (N < 10) — suppressed from ranking

- 8 (alpha × city) buckets with fewer than 10 outcomes; do not draw conclusions yet.

## Candidates to retire (N≥30, WR<50%)

- `MODEL_VS_MARKET` × **chicago** : N=44, WR=31.8%, P&L=$-335.58
- `MODEL_VS_MARKET` × **tokyo** : N=85, WR=0.0%, P&L=$-1013.16

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
| MODEL_VS_MARKET | 01h | 34 | 94.1% | $+111.57 |
| MODEL_VS_MARKET | 02h | 29 | 86.2% | $+93.95 |
| MODEL_VS_MARKET | 13h | 76 | 82.9% | $+42.49 |
| MODEL_VS_MARKET | 12h | 26 | 80.8% | $+35.91 |
| MODEL_VS_MARKET | 04h | 8 | 87.5% | $+29.71 |
| CONFIRMED_NO | 09h | 14 | 100.0% | $+25.78 |
| CONFIRMED_NO | 08h | 10 | 100.0% | $+19.40 |

## Related
- [[_MOC|Polymarket Hub]]
- [[STATE-HANDOFF|State handoff]]
- [[audit-hedge-fund-grade|Audit hedge fund grade]]
