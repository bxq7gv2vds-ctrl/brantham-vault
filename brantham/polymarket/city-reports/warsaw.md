---
name: Warsaw — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: INSUFFICIENT_DATA
tags: [polymarket, city, warsaw, insufficient_data]
---

# Warsaw — deep dive

**Verdict: INSUFFICIENT_DATA** — N=16 trop petit pour verdict

## Identité

- ICAO : `EPWA`
- Coords : 52.1657, 20.9671
- Country / TZ : PL / Europe/Warsaw
- UTC offset : 2.0h
- Elevation : 110.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 16
- **Notes** : kelly from N=16 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 16
- **Outcomes réconciliés** : 16
- **P&L total** : +$85.79
- **Avg / trade** : +$5.36
- **WR** : 100.0%
- **Exposure cumulée** : +$308.56
- **Sharpe (ann.)** : 25.68
- **Daily P&L** : ['+$24.15', '+$61.64']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 16 | +$85.79 | +$5.36 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| mid (8-15%) | 2 | +$6.79 | +$3.40 | 100.0% |
| high (15-30%) | 14 | +$79.00 | +$5.64 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 9 | +$61.64 | +$6.85 | 100.0% |
| 24-48h | 2 | +$6.79 | +$3.40 | 100.0% |
| >48h | 5 | +$17.35 | +$3.47 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.37°C**
- Predicted YES rate : 99.3%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:03:50 | MODEL_VS_MARKET | NO | 0.710 | 0.993 | 28.3% | $19.6 | +$8.01 |
| 2026-04-19 15:53:44 | MODEL_VS_MARKET | NO | 0.705 | 0.993 | 28.8% | $18.9 | +$7.91 |
| 2026-04-19 16:08:52 | MODEL_VS_MARKET | NO | 0.715 | 0.993 | 27.8% | $19.6 | +$7.82 |
| 2026-04-19 16:11:54 | MODEL_VS_MARKET | NO | 0.715 | 0.990 | 27.5% | $19.6 | +$7.82 |
| 2026-04-19 16:13:58 | MODEL_VS_MARKET | NO | 0.715 | 0.990 | 27.5% | $19.6 | +$7.82 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 16:23:05 | MODEL_VS_MARKET | NO | 0.855 | 0.989 | 13.4% | $19.6 | +$3.33 |
| 2026-04-18 09:16:56 | MODEL_VS_MARKET | NO | 0.825 | 0.997 | 17.2% | $15.8 | +$3.35 |
| 2026-04-18 09:47:35 | MODEL_VS_MARKET | NO | 0.830 | 0.997 | 16.7% | $16.7 | +$3.41 |
| 2026-04-18 16:48:50 | MODEL_VS_MARKET | NO | 0.845 | 0.989 | 14.4% | $18.9 | +$3.47 |
| 2026-04-18 09:10:44 | MODEL_VS_MARKET | NO | 0.830 | 0.997 | 16.7% | $17.1 | +$3.51 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]