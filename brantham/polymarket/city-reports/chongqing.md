---
name: Chongqing — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: KEEP
tags: [polymarket, city, chongqing, keep]
---

# Chongqing — deep dive

**Verdict: KEEP** — Steady: $113 on 31 trades

## Identité

- ICAO : `ZUCK`
- Coords : 29.7192, 106.6417
- Country / TZ : CN / Asia/Shanghai
- UTC offset : 8.0h
- Elevation : 416.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 31
- **Notes** : kelly from N=31 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 31
- **Outcomes réconciliés** : 31
- **P&L total** : +$112.60
- **Avg / trade** : +$3.63
- **WR** : 100.0%
- **Exposure cumulée** : +$603.45
- **Sharpe (ann.)** : 20.60
- **Daily P&L** : ['+$4.32', '+$57.12', '+$51.16']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 19 | +$89.22 | +$4.70 | 100.0% |
| MODEL_VS_MARKET | NO | deep_ITM | 11 | +$14.42 | +$1.31 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 11 | +$14.42 | +$1.31 | 100.0% |
| mid (8-15%) | 5 | +$17.45 | +$3.49 | 100.0% |
| high (15-30%) | 14 | +$71.77 | +$5.13 | 100.0% |
| extreme (>30%) | 1 | +$8.96 | +$8.96 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 19 | +$71.31 | +$3.75 | 100.0% |
| 24-48h | 9 | +$19.71 | +$2.19 | 100.0% |
| >48h | 3 | +$21.58 | +$7.19 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.86°C**
- Predicted YES rate : 99.6%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 12:52:18 | MODEL_VS_MARKET | NO | 0.695 | 0.999 | 30.4% | $20.4 | +$8.96 |
| 2026-04-18 11:56:42 | MODEL_VS_MARKET | NO | 0.715 | 0.999 | 28.4% | $19.6 | +$7.82 |
| 2026-04-18 09:47:35 | MODEL_VS_MARKET | NO | 0.705 | 0.995 | 29.0% | $16.7 | +$6.98 |
| 2026-04-18 07:54:48 | MODEL_VS_MARKET | NO | 0.705 | 0.995 | 29.0% | $16.2 | +$6.79 |
| 2026-04-18 13:52:46 | MODEL_VS_MARKET | NO | 0.779 | 0.984 | 20.4% | $21.3 | +$6.03 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:24:00 | MODEL_VS_MARKET | NO | 0.945 | 0.999 | 5.4% | $18.9 | +$1.10 |
| 2026-04-19 16:29:03 | MODEL_VS_MARKET | NO | 0.945 | 0.999 | 5.4% | $19.6 | +$1.14 |
| 2026-04-19 16:18:57 | MODEL_VS_MARKET | NO | 0.940 | 1.000 | 6.0% | $18.9 | +$1.21 |
| 2026-04-18 09:16:56 | MODEL_VS_MARKET | NO | 0.927 | 0.993 | 6.5% | $15.8 | +$1.24 |
| 2026-04-19 15:58:47 | MODEL_VS_MARKET | NO | 0.940 | 1.000 | 6.0% | $19.6 | +$1.25 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]