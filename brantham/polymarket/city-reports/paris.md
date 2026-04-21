---
name: Paris — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: INSUFFICIENT_DATA
tags: [polymarket, city, paris, insufficient_data]
---

# Paris — deep dive

**Verdict: INSUFFICIENT_DATA** — N=19 trop petit pour verdict

## Identité

- ICAO : `LFPG`
- Coords : 49.0097, 2.5479
- Country / TZ : FR / Europe/Paris
- UTC offset : 2.0h
- Elevation : 119.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 19
- **Notes** : kelly from N=19 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 24
- **Outcomes réconciliés** : 19
- **P&L total** : +$31.73
- **Avg / trade** : +$1.67
- **WR** : 100.0%
- **Exposure cumulée** : +$366.44
- **Daily P&L** : ['+$31.73']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 7 | +$17.71 | +$2.53 | 100.0% |
| MODEL_VS_MARKET | NO | deep_ITM | 12 | +$14.02 | +$1.17 | 100.0% |
| CONFIRMED_NO | NO | ITM | 2 | +$0.00 | +$0.00 | 0.0% |
| CONFIRMED_NO | NO | deep_ITM | 3 | +$0.00 | +$0.00 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 12 | +$14.02 | +$1.17 | 100.0% |
| mid (8-15%) | 7 | +$17.71 | +$2.53 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 19 | +$31.73 | +$1.67 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.49°C**
- Predicted YES rate : 99.8%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 22:28:53 | MODEL_VS_MARKET | NO | 0.880 | 1.000 | 11.9% | $19.6 | +$2.66 |
| 2026-04-17 21:58:36 | MODEL_VS_MARKET | NO | 0.878 | 1.000 | 12.1% | $18.9 | +$2.61 |
| 2026-04-17 22:13:45 | MODEL_VS_MARKET | NO | 0.879 | 1.000 | 12.0% | $18.9 | +$2.59 |
| 2026-04-17 22:18:48 | MODEL_VS_MARKET | NO | 0.879 | 1.000 | 12.0% | $18.9 | +$2.59 |
| 2026-04-17 22:23:50 | MODEL_VS_MARKET | NO | 0.879 | 1.000 | 12.0% | $18.9 | +$2.59 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 20:37:21 | MODEL_VS_MARKET | NO | 0.955 | 1.000 | 4.5% | $14.8 | +$0.70 |
| 2026-04-17 19:56:57 | MODEL_VS_MARKET | NO | 0.949 | 0.992 | 4.3% | $17.7 | +$0.95 |
| 2026-04-17 19:34:51 | MODEL_VS_MARKET | NO | 0.946 | 0.992 | 4.6% | $18.3 | +$1.04 |
| 2026-04-17 19:35:23 | MODEL_VS_MARKET | NO | 0.946 | 0.992 | 4.6% | $18.3 | +$1.04 |
| 2026-04-17 23:54:41 | MODEL_VS_MARKET | NO | 0.929 | 1.000 | 7.0% | $14.5 | +$1.10 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]