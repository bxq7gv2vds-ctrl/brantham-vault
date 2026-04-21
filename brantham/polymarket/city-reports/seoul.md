---
name: Seoul — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: INSUFFICIENT_DATA
tags: [polymarket, city, seoul, insufficient_data]
---

# Seoul — deep dive

**Verdict: INSUFFICIENT_DATA** — N=15 trop petit pour verdict

## Identité

- ICAO : `RKSI`
- Coords : 37.4602, 126.4407
- Country / TZ : KR / Asia/Seoul
- UTC offset : 9.0h
- Elevation : 7.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 15
- **Notes** : kelly from N=15 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 15
- **Outcomes réconciliés** : 15
- **P&L total** : +$102.94
- **Avg / trade** : +$6.86
- **WR** : 100.0%
- **Exposure cumulée** : +$333.25
- **Sharpe (ann.)** : 220.76
- **Daily P&L** : ['+$48.85', '+$54.09']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 13 | +$54.09 | +$4.16 | 100.0% |
| MODEL_VS_MARKET | NO | mid | 2 | +$48.85 | +$24.43 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| high (15-30%) | 13 | +$54.09 | +$4.16 | 100.0% |
| extreme (>30%) | 2 | +$48.85 | +$24.43 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 13 | +$54.09 | +$4.16 | 100.0% |
| 24-48h | 2 | +$48.85 | +$24.43 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.28°C**
- Predicted YES rate : 99.9%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:40:07 | MODEL_VS_MARKET | NO | 0.570 | 1.000 | 43.0% | $50.0 | +$37.72 |
| 2026-04-17 14:44:59 | MODEL_VS_MARKET | NO | 0.570 | 1.000 | 43.0% | $14.8 | +$11.13 |
| 2026-04-19 17:29:47 | MODEL_VS_MARKET | NO | 0.830 | 0.999 | 16.9% | $22.4 | +$4.58 |
| 2026-04-19 17:49:57 | MODEL_VS_MARKET | NO | 0.835 | 0.999 | 16.4% | $22.4 | +$4.42 |
| 2026-04-19 15:46:09 | MODEL_VS_MARKET | NO | 0.830 | 0.999 | 16.9% | $21.3 | +$4.37 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 17:39:52 | MODEL_VS_MARKET | NO | 0.835 | 0.999 | 16.4% | $18.9 | +$3.73 |
| 2026-04-19 17:34:49 | MODEL_VS_MARKET | NO | 0.840 | 0.999 | 15.9% | $19.6 | +$3.74 |
| 2026-04-19 17:09:32 | MODEL_VS_MARKET | NO | 0.830 | 0.999 | 16.9% | $18.9 | +$3.87 |
| 2026-04-19 15:48:13 | MODEL_VS_MARKET | NO | 0.830 | 0.999 | 16.9% | $19.6 | +$4.02 |
| 2026-04-19 17:44:55 | MODEL_VS_MARKET | NO | 0.835 | 0.999 | 16.4% | $20.4 | +$4.03 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]