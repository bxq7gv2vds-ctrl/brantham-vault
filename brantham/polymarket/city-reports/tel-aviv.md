---
name: Tel Aviv — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: INSUFFICIENT_DATA
tags: [polymarket, city, tel-aviv, insufficient_data]
---

# Tel Aviv — deep dive

**Verdict: INSUFFICIENT_DATA** — N=19 trop petit pour verdict

## Identité

- ICAO : `LLBG`
- Coords : 32.0004, 34.8867
- Country / TZ : IL / Asia/Jerusalem
- UTC offset : 3.0h
- Elevation : 41.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 19
- **Notes** : kelly from N=19 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 22
- **Outcomes réconciliés** : 19
- **P&L total** : +$15.84
- **Avg / trade** : +$0.83
- **WR** : 100.0%
- **Exposure cumulée** : +$347.88
- **Sharpe (ann.)** : 134.16
- **Daily P&L** : ['+$8.58', '+$7.26']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | deep_ITM | 19 | +$15.84 | +$0.83 | 100.0% |
| CONFIRMED_NO | NO | deep_ITM | 2 | +$0.00 | +$0.00 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 19 | +$15.84 | +$0.83 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 10 | +$8.58 | +$0.86 | 100.0% |
| 24-48h | 9 | +$7.26 | +$0.81 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **0.90°C**
- Predicted YES rate : 100.0%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:45:00 | MODEL_VS_MARKET | NO | 0.940 | 1.000 | 6.0% | $14.8 | +$0.94 |
| 2026-04-17 22:23:51 | MODEL_VS_MARKET | NO | 0.953 | 1.000 | 4.7% | $18.9 | +$0.93 |
| 2026-04-17 22:33:56 | MODEL_VS_MARKET | NO | 0.953 | 1.000 | 4.7% | $18.9 | +$0.93 |
| 2026-04-17 22:59:10 | MODEL_VS_MARKET | NO | 0.953 | 1.000 | 4.7% | $18.9 | +$0.93 |
| 2026-04-17 22:13:45 | MODEL_VS_MARKET | NO | 0.954 | 1.000 | 4.6% | $18.9 | +$0.91 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 23:54:41 | MODEL_VS_MARKET | NO | 0.953 | 1.000 | 4.7% | $14.5 | +$0.72 |
| 2026-04-17 23:44:35 | MODEL_VS_MARKET | NO | 0.956 | 1.000 | 4.4% | $15.8 | +$0.73 |
| 2026-04-17 23:39:32 | MODEL_VS_MARKET | NO | 0.954 | 1.000 | 4.6% | $15.6 | +$0.75 |
| 2026-04-17 19:46:51 | MODEL_VS_MARKET | NO | 0.958 | 1.000 | 4.2% | $17.1 | +$0.75 |
| 2026-04-17 19:51:54 | MODEL_VS_MARKET | NO | 0.958 | 1.000 | 4.2% | $17.7 | +$0.78 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]