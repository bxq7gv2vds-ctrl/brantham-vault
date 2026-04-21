---
name: Lucknow — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: WATCH
tags: [polymarket, city, lucknow, watch]
---

# Lucknow — deep dive

**Verdict: WATCH** — Marginal: $55, waiting for more data

## Identité

- ICAO : `VILK`
- Coords : 26.7606, 80.8893
- Country / TZ : IN / Asia/Kolkata
- UTC offset : 5.5h
- Elevation : 125.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 49
- **Notes** : kelly from N=49 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 49
- **Outcomes réconciliés** : 49
- **P&L total** : +$54.67
- **Avg / trade** : +$1.12
- **WR** : 100.0%
- **Exposure cumulée** : +$807.98
- **Sharpe (ann.)** : 11.06
- **Daily P&L** : ['+$5.21', '+$48.32', '+$1.14']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | deep_ITM | 48 | +$52.56 | +$1.09 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 48 | +$52.56 | +$1.09 | 100.0% |
| mid (8-15%) | 1 | +$2.11 | +$2.11 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 4 | +$5.21 | +$1.30 | 100.0% |
| 24-48h | 44 | +$48.32 | +$1.10 | 100.0% |
| >48h | 1 | +$1.14 | +$1.14 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.54°C**
- Predicted YES rate : 99.1%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 21:33:22 | MODEL_VS_MARKET | NO | 0.884 | 0.995 | 11.0% | $16.2 | +$2.11 |
| 2026-04-17 19:34:51 | MODEL_VS_MARKET | NO | 0.925 | 0.991 | 6.6% | $18.3 | +$1.48 |
| 2026-04-17 19:35:23 | MODEL_VS_MARKET | NO | 0.925 | 0.991 | 6.6% | $18.3 | +$1.48 |
| 2026-04-17 22:08:42 | MODEL_VS_MARKET | NO | 0.936 | 0.991 | 5.4% | $19.6 | +$1.33 |
| 2026-04-17 22:33:56 | MODEL_VS_MARKET | NO | 0.935 | 0.991 | 5.5% | $18.9 | +$1.30 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 02:08:11 | MODEL_VS_MARKET | NO | 0.951 | 0.991 | 4.0% | $12.5 | +$0.65 |
| 2026-04-18 01:23:55 | MODEL_VS_MARKET | NO | 0.946 | 0.991 | 4.5% | $11.7 | +$0.67 |
| 2026-04-18 01:29:42 | MODEL_VS_MARKET | NO | 0.946 | 0.991 | 4.5% | $12.1 | +$0.69 |
| 2026-04-18 01:06:19 | MODEL_VS_MARKET | NO | 0.945 | 0.991 | 4.6% | $12.1 | +$0.70 |
| 2026-04-18 01:18:01 | MODEL_VS_MARKET | NO | 0.945 | 0.991 | 4.6% | $12.9 | +$0.75 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]