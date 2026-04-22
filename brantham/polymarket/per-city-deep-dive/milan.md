# Milan — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **253** markets analysés
- **112,482** trades on-chain
- **$379k** volume total USDC
- Période : 2026-03-16 → 2026-04-08

## Outcomes

- YES wins : **23** (9.1%)
- NO wins : **230**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0400 | 0.1900 | 0.3200 | 0.1306 | 0.1740 |
| `price_mid_avg` | 0.0020 | 0.0030 | 0.0160 | 0.1128 | 0.3662 | 0.1067 | 0.1826 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0100 | 0.0923 | 0.2873 |
| `drift_pp` | -0.2990 | -0.1590 | -0.0290 | -0.0090 | -0.0020 | -0.0383 | 0.3054 |
| `volatility_pp` | 0.0040 | 0.0093 | 0.0269 | 0.0862 | 0.2054 | 0.0657 | 0.0837 |
| `max_drawdown` | -0.6491 | -0.3490 | -0.1860 | -0.0580 | -0.0190 | -0.2514 | 0.2376 |
| `hurst` | 0.0425 | 0.0925 | 0.1706 | 0.2399 | 0.3381 | 0.1733 | 0.1127 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.3950 | 2.580 | 1.541 | 8.285 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 151 | 2.0% | -0.0190 |
| [0.1, 0.2) | 39 | 15.4% | -0.1390 |
| [0.2, 0.3) | 34 | 26.5% | -0.2240 |
| [0.3, 0.4) | 14 | 21.4% | -0.3240 |
| [0.4, 0.5) | 2 | 50.0% | 0.0550 |
| [0.5, 0.6) | 6 | 16.7% | -0.4990 |
| [0.6, 0.7) | 1 | 0.0% | -0.6590 |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 3 | 0.0% | -0.7989 |
| [0.9, 1.0) | 3 | 0.0% | -0.9490 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 207 | 9.7% | 0.0600 | -0.0390 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **3** trades, WR=2.0%
- **Favorite losses** (open>0.90 + NO win) : **3** trades, WR=100.0%

- Long-shot payoff moyen : +0.918 pp

## Patterns temporels

- **Heures peak (UTC)** : [15, 9, 14] (23,632 trades)
- **Heures calmes (UTC)** : [20, 2, 22] (7,038 trades)
- **Jours peak** : ['Thu', 'Mon']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0567 | 0.0264 | 42.647 |
| [0.25-0.50] | 0.0357 | 0.0141 | 51.218 |
| [0.50-0.75] | 0.0193 | 0.0083 | 117.532 |
| [0.75-1.00] | 0.0086 | 0.0047 | 237.585 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 48 | -0.2895 | 0.1285 | 0.2302 | -0.5840 | 0.0% |
| 1 | 183 | -0.0290 | 0.0162 | 0.1308 | -0.1090 | 0.5% |
| 2 | 22 | 0.7790 | 0.2820 | 0.2888 | -0.3850 | 100.0% |

## Volume profile

- Trade size : médian $0, p90 $4, p99 $42
- Total volume USDC : $379k
- Trades total : 112,482

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/milan.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
