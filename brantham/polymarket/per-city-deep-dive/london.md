# London — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **1,475** markets analysés
- **1,049,441** trades on-chain
- **$8.66M** volume total USDC
- Période : 2025-10-01 → 2026-04-08

## Outcomes

- YES wins : **187** (12.7%)
- NO wins : **1,280**
- Ambiguous : 8

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0600 | 0.2300 | 0.4100 | 0.1506 | 0.1812 |
| `price_mid_avg` | 0.0010 | 0.0030 | 0.0170 | 0.1736 | 0.5512 | 0.1444 | 0.2387 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.9990 | 0.1294 | 0.3335 |
| `drift_pp` | -0.3390 | -0.1490 | -0.0390 | -0.0090 | 0.5090 | -0.0212 | 0.3180 |
| `volatility_pp` | 0.0042 | 0.0097 | 0.0329 | 0.1246 | 0.2422 | 0.0808 | 0.0975 |
| `max_drawdown` | -0.6990 | -0.4690 | -0.1990 | -0.0669 | -0.0280 | -0.2958 | 0.2713 |
| `hurst` | 0.0442 | 0.0912 | 0.1658 | 0.2559 | 0.3493 | 0.1812 | 0.1177 |
| `half_life_minutes` | 0.0000 | 0.2525 | 1.602 | 5.575 | 14.852 | 6.884 | 34.901 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 806 | 3.6% | -0.0190 |
| [0.1, 0.2) | 236 | 13.6% | -0.1090 |
| [0.2, 0.3) | 160 | 18.8% | -0.2190 |
| [0.3, 0.4) | 93 | 30.1% | -0.3290 |
| [0.4, 0.5) | 79 | 44.3% | -0.3990 |
| [0.5, 0.6) | 61 | 41.0% | -0.4990 |
| [0.6, 0.7) | 16 | 12.5% | -0.6890 |
| [0.7, 0.8) | 3 | 66.7% | 0.2090 |
| [0.8, 0.9) | 3 | 33.3% | -0.8390 |
| [0.9, 1.0) | 10 | 30.0% | -0.9790 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 742 | 13.7% | 0.1000 | -0.0490 |
| cold | 80 | 16.2% | 0.1100 | -0.0590 |
| mild | 275 | 20.7% | 0.1600 | -0.0590 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **29** trades, WR=3.6%
- **Favorite losses** (open>0.90 + NO win) : **7** trades, WR=70.0%

- Long-shot payoff moyen : +0.952 pp

## Patterns temporels

- **Heures peak (UTC)** : [12, 13, 11] (240,194 trades)
- **Heures calmes (UTC)** : [2, 3, 4] (68,634 trades)
- **Jours peak** : ['Mon', 'Thu']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0662 | 0.0269 | 63.983 |
| [0.25-0.50] | 0.0427 | 0.0190 | 90.326 |
| [0.50-0.75] | 0.0259 | 0.0147 | 197.057 |
| [0.75-1.00] | 0.0104 | 0.0094 | 368.179 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 357 | -0.2790 | 0.1260 | 0.2564 | -0.6090 | 0.6% |
| 1 | 926 | -0.0290 | 0.0136 | 0.1176 | -0.0944 | 0.3% |
| 2 | 184 | 0.6940 | 0.2626 | 0.2913 | -0.4700 | 100.0% |

## Volume profile

- Trade size : médian $1, p90 $10, p99 $107
- Total volume USDC : $8.66M
- Trades total : 1,049,441

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/london.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
