---
name: Shenzhen — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: KEEP
tags: [polymarket, city, shenzhen, keep]
---

# Shenzhen — deep dive

**Verdict: KEEP** — Steady: $165 on 57 trades

## Identité

- ICAO : `ZGSZ`
- Coords : 22.6393, 113.8108
- Country / TZ : CN / Asia/Shanghai
- UTC offset : 8.0h
- Elevation : 4.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 57
- **Notes** : kelly from N=57 WR=96.5% (emp 0.818 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 57
- ECE before : 0.0890 → after : 0.0100
- Brier before : 0.0084 → after : 0.0001
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 57
- **Outcomes réconciliés** : 57
- **P&L total** : +$164.82
- **Avg / trade** : +$2.89
- **WR** : 96.5%
- **Exposure cumulée** : +$924.58
- **Sharpe (ann.)** : 8.22
- **Daily P&L** : ['-$13.59', '+$177.23', '+$1.19']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 54 | +$177.23 | +$3.28 | 100.0% |
| MODEL_VS_MARKET | YES | deep_OTM | 2 | -$13.59 | -$6.79 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 45 | +$144.04 | +$3.20 | 100.0% |
| mid (8-15%) | 12 | +$20.78 | +$1.73 | 83.3% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 2 | -$13.59 | -$6.79 | 0.0% |
| 24-48h | 55 | +$178.41 | +$3.24 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **0.89°C**
- Predicted YES rate : 88.2%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 22:59:10 | MODEL_VS_MARKET | NO | 0.815 | 0.905 | 9.0% | $18.9 | +$4.29 |
| 2026-04-17 23:04:13 | MODEL_VS_MARKET | NO | 0.815 | 0.905 | 9.0% | $18.9 | +$4.29 |
| 2026-04-17 21:48:30 | MODEL_VS_MARKET | NO | 0.835 | 0.905 | 7.0% | $21.3 | +$4.21 |
| 2026-04-17 21:53:33 | MODEL_VS_MARKET | NO | 0.835 | 0.905 | 7.0% | $21.3 | +$4.21 |
| 2026-04-17 22:54:08 | MODEL_VS_MARKET | NO | 0.820 | 0.905 | 8.5% | $18.3 | +$4.01 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 20:32:18 | MODEL_VS_MARKET | YES | 0.006 | 0.089 | 8.3% | $7.4 | -$7.40 |
| 2026-04-17 20:37:22 | MODEL_VS_MARKET | YES | 0.006 | 0.089 | 8.3% | $6.2 | -$6.19 |
| 2026-04-18 12:57:20 | MODEL_VS_MARKET | NO | 0.943 | 0.998 | 5.5% | $19.6 | +$1.19 |
| 2026-04-18 01:29:42 | MODEL_VS_MARKET | NO | 0.840 | 0.905 | 6.5% | $12.1 | +$2.30 |
| 2026-04-18 01:23:55 | MODEL_VS_MARKET | NO | 0.835 | 0.905 | 7.0% | $11.7 | +$2.31 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]