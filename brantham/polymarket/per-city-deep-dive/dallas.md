# Dallas — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **1,027** markets analysés
- **412,414** trades on-chain
- **$2.76M** volume total USDC
- Période : 2025-12-04 → 2026-04-08

## Outcomes

- YES wins : **121** (11.9%)
- NO wins : **892**
- Ambiguous : 14

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0110 | 0.0400 | 0.1900 | 0.3500 | 0.1308 | 0.1816 |
| `price_mid_avg` | 0.0010 | 0.0032 | 0.0168 | 0.1510 | 0.4487 | 0.1359 | 0.2368 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0020 | 0.9990 | 0.1239 | 0.3261 |
| `drift_pp` | -0.2604 | -0.1100 | -0.0190 | -0.0090 | 0.3650 | -0.0069 | 0.2956 |
| `volatility_pp` | 0.0034 | 0.0083 | 0.0306 | 0.1067 | 0.2325 | 0.0755 | 0.0961 |
| `max_drawdown` | -0.6933 | -0.4290 | -0.1744 | -0.0455 | -0.0190 | -0.2671 | 0.2624 |
| `hurst` | 0.0258 | 0.0863 | 0.1490 | 0.2357 | 0.3223 | 0.1607 | 0.1266 |
| `half_life_minutes` | 0.0000 | 0.2351 | 1.007 | 4.007 | 11.731 | 5.569 | 20.363 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 615 | 3.6% | -0.0190 |
| [0.1, 0.2) | 151 | 12.6% | -0.1290 |
| [0.2, 0.3) | 122 | 25.4% | -0.2090 |
| [0.3, 0.4) | 37 | 21.6% | -0.3290 |
| [0.4, 0.5) | 30 | 33.3% | -0.4008 |
| [0.5, 0.6) | 26 | 38.5% | -0.4990 |
| [0.6, 0.7) | 8 | 25.0% | -0.6272 |
| [0.7, 0.8) | 3 | 66.7% | 0.2690 |
| [0.8, 0.9) | 7 | 71.4% | 0.1690 |
| [0.9, 1.0) | 14 | 85.7% | 0.0390 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 11 | 9.1% | 0.1500 | -0.0970 |
| cold | 72 | 11.1% | 0.0550 | -0.0190 |
| mild | 385 | 9.3% | 0.0400 | -0.0200 |
| warm | 237 | 13.7% | 0.1300 | -0.0590 |
| hot | 72 | 6.9% | 0.0550 | -0.0390 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **22** trades, WR=3.6%
- **Favorite losses** (open>0.90 + NO win) : **2** trades, WR=16.7%

- Long-shot payoff moyen : +0.964 pp

## Patterns temporels

- **Heures peak (UTC)** : [21, 22, 20] (89,827 trades)
- **Heures calmes (UTC)** : [2, 3, 1] (26,546 trades)
- **Jours peak** : ['Thu', 'Mon']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0433 | 0.0218 | 48.258 |
| [0.25-0.50] | 0.0372 | 0.0150 | 56.542 |
| [0.50-0.75] | 0.0238 | 0.0112 | 100.352 |
| [0.75-1.00] | 0.0106 | 0.0088 | 208.942 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 98 | 0.7890 | 0.3045 | 0.2776 | -0.4800 | 99.0% |
| 1 | 665 | -0.0190 | 0.0138 | 0.1245 | -0.0760 | 3.0% |
| 2 | 250 | -0.1990 | 0.1238 | 0.2112 | -0.5545 | 2.5% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $76
- Total volume USDC : $2.76M
- Trades total : 412,414

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/dallas.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
