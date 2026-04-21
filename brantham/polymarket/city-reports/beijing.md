---
name: Beijing — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: KEEP
tags: [polymarket, city, beijing, keep]
---

# Beijing — deep dive

**Verdict: KEEP** — Steady: $352 on 59 trades

## Identité

- ICAO : `ZBAA`
- Coords : 40.0799, 116.6031
- Country / TZ : CN / Asia/Shanghai
- UTC offset : 8.0h
- Elevation : 35.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.40725624907917185
- **N outcomes** : 59
- **Notes** : kelly from N=59 WR=88.1% (emp 0.487 → blended 0.407)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 52
- ECE before : 0.0801 → after : 0.0190
- Brier before : 0.0434 → after : 0.0238
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 82
- **Outcomes réconciliés** : 59
- **P&L total** : +$351.60
- **Avg / trade** : +$5.96
- **WR** : 88.1%
- **Exposure cumulée** : +$1,306.84
- **Sharpe (ann.)** : 11.40
- **Daily P&L** : ['+$280.96', '+$116.02', '-$45.39']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | YES | deep_OTM | 8 | +$252.53 | +$31.57 | 25.0% |
| MODEL_VS_MARKET | NO | ITM | 43 | +$84.73 | +$1.97 | 97.7% |
| MODEL_VS_MARKET | NO | deep_ITM | 8 | +$14.33 | +$1.79 | 100.0% |
| CONFIRMED_YES | YES | OTM | 17 | +$0.00 | +$0.00 | 0.0% |
| CONFIRMED_YES | YES | deep_OTM | 6 | +$0.00 | +$0.00 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 26 | +$280.05 | +$10.77 | 76.9% |
| mid (8-15%) | 33 | +$71.54 | +$2.17 | 97.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 4 | +$281.69 | +$70.42 | 75.0% |
| 24-48h | 55 | +$69.91 | +$1.27 | 89.1% |

## σ bias — model vs empirical

- σ_c predicted avg : **2.05°C**
- Predicted YES rate : 84.9%
- Actual YES rate : 5.1%
- **Calibration bias ratio** : 0.06 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:40:07 | MODEL_VS_MARKET | YES | 0.074 | 0.143 | 6.9% | $18.6 | +$230.57 |
| 2026-04-17 14:44:59 | MODEL_VS_MARKET | YES | 0.074 | 0.143 | 6.9% | $5.5 | +$68.08 |
| 2026-04-17 21:43:28 | MODEL_VS_MARKET | NO | 0.881 | 0.971 | 9.0% | $21.3 | +$2.88 |
| 2026-04-17 21:48:30 | MODEL_VS_MARKET | NO | 0.881 | 0.971 | 9.0% | $21.3 | +$2.88 |
| 2026-04-17 21:53:33 | MODEL_VS_MARKET | NO | 0.881 | 0.971 | 9.0% | $21.3 | +$2.88 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 19:51:54 | MODEL_VS_MARKET | NO | 0.816 | 0.857 | 4.1% | $17.7 | -$17.68 |
| 2026-04-19 16:03:50 | MODEL_VS_MARKET | YES | 0.012 | 0.092 | 8.0% | $8.0 | -$7.95 |
| 2026-04-19 15:58:47 | MODEL_VS_MARKET | YES | 0.013 | 0.092 | 7.9% | $7.9 | -$7.86 |
| 2026-04-19 16:08:52 | MODEL_VS_MARKET | YES | 0.014 | 0.092 | 7.8% | $7.8 | -$7.77 |
| 2026-04-19 15:53:44 | MODEL_VS_MARKET | YES | 0.013 | 0.092 | 7.9% | $7.6 | -$7.57 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]