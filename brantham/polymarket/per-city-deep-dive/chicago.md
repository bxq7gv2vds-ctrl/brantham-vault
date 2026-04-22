# Chicago — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **698** markets analysés
- **398,810** trades on-chain
- **$2.12M** volume total USDC
- Période : 2025-12-04 → 2026-04-08

## Outcomes

- YES wins : **72** (10.6%)
- NO wins : **608**
- Ambiguous : 18

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0700 | 0.2000 | 0.3800 | 0.1392 | 0.1660 |
| `price_mid_avg` | 0.0020 | 0.0074 | 0.0339 | 0.1515 | 0.3506 | 0.1220 | 0.1954 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.9990 | 0.1150 | 0.3161 |
| `drift_pp` | -0.2822 | -0.1490 | -0.0490 | -0.0090 | 0.2990 | -0.0242 | 0.2949 |
| `volatility_pp` | 0.0052 | 0.0146 | 0.0387 | 0.0968 | 0.2349 | 0.0760 | 0.0916 |
| `max_drawdown` | -0.6498 | -0.4318 | -0.2190 | -0.0905 | -0.0353 | -0.2872 | 0.2380 |
| `hurst` | 0.0581 | 0.1007 | 0.1765 | 0.2540 | 0.3332 | 0.1847 | 0.1082 |
| `half_life_minutes` | 0.0000 | 0.1838 | 0.9070 | 3.371 | 10.392 | 4.732 | 13.593 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 379 | 4.2% | -0.0190 |
| [0.1, 0.2) | 127 | 7.9% | -0.1390 |
| [0.2, 0.3) | 83 | 15.7% | -0.2090 |
| [0.3, 0.4) | 29 | 27.6% | -0.3390 |
| [0.4, 0.5) | 31 | 22.6% | -0.4090 |
| [0.5, 0.6) | 15 | 46.7% | -0.4990 |
| [0.6, 0.7) | 8 | 50.0% | -0.1750 |
| [0.7, 0.8) | 2 | 100.0% | 0.2390 |
| [0.8, 0.9) | 2 | 50.0% | -0.3325 |
| [0.9, 1.0) | 4 | 100.0% | 0.0340 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 122 | 14.0% | 0.0750 | -0.0440 |
| cold | 270 | 9.1% | 0.0800 | -0.0490 |
| mild | 129 | 7.9% | 0.1000 | -0.0790 |
| warm | 21 | 9.5% | 0.0500 | -0.0370 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **16** trades, WR=4.2%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.963 pp

## Patterns temporels

- **Heures peak (UTC)** : [19, 21, 16] (65,776 trades)
- **Heures calmes (UTC)** : [4, 1, 2] (34,562 trades)
- **Jours peak** : ['Wed', 'Thu']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0664 | 0.0266 | 67.771 |
| [0.25-0.50] | 0.0548 | 0.0180 | 80.730 |
| [0.50-0.75] | 0.0372 | 0.0174 | 149.058 |
| [0.75-1.00] | 0.0185 | 0.0158 | 278.763 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 420 | -0.0290 | 0.0193 | 0.1293 | -0.1090 | 1.4% |
| 1 | 67 | 0.7590 | 0.3071 | 0.3413 | -0.4700 | 100.0% |
| 2 | 207 | -0.1990 | 0.0995 | 0.2398 | -0.4890 | 2.5% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $57
- Total volume USDC : $2.12M
- Trades total : 398,810

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/chicago.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
