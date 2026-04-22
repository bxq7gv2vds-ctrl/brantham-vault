# Madrid — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **253** markets analysés
- **150,361** trades on-chain
- **$538k** volume total USDC
- Période : 2026-03-16 → 2026-04-08

## Outcomes

- YES wins : **23** (9.1%)
- NO wins : **230**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0100 | 0.0400 | 0.1600 | 0.3160 | 0.1046 | 0.1387 |
| `price_mid_avg` | 0.0016 | 0.0028 | 0.0152 | 0.0820 | 0.3282 | 0.0928 | 0.1723 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0100 | 0.0922 | 0.2873 |
| `drift_pp` | -0.2690 | -0.1190 | -0.0290 | -0.0090 | -0.0050 | -0.0124 | 0.2832 |
| `volatility_pp` | 0.0037 | 0.0070 | 0.0224 | 0.0780 | 0.2057 | 0.0633 | 0.0890 |
| `max_drawdown` | -0.6298 | -0.3600 | -0.1480 | -0.0400 | -0.0190 | -0.2282 | 0.2330 |
| `hurst` | 0.0604 | 0.0972 | 0.1806 | 0.2701 | 0.3790 | 0.1915 | 0.1266 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.3877 | 1.417 | 0.9722 | 3.843 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 169 | 5.3% | -0.0190 |
| [0.1, 0.2) | 32 | 15.6% | -0.1390 |
| [0.2, 0.3) | 26 | 15.4% | -0.2190 |
| [0.3, 0.4) | 17 | 11.8% | -0.3390 |
| [0.4, 0.5) | 2 | 0.0% | -0.4000 |
| [0.5, 0.6) | 5 | 20.0% | -0.4990 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 1 | 100.0% | 0.2390 |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 1 | 100.0% | 0.0090 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 207 | 10.1% | 0.0500 | -0.0390 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **9** trades, WR=5.3%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.946 pp

## Patterns temporels

- **Heures peak (UTC)** : [15, 13, 14] (36,148 trades)
- **Heures calmes (UTC)** : [2, 3, 4] (8,088 trades)
- **Jours peak** : ['Thu', 'Fri']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0476 | 0.0193 | 48.631 |
| [0.25-0.50] | 0.0315 | 0.0133 | 83.847 |
| [0.50-0.75] | 0.0174 | 0.0078 | 145.675 |
| [0.75-1.00] | 0.0076 | 0.0059 | 318.245 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 179 | -0.0190 | 0.0119 | 0.1400 | -0.0790 | 0.6% |
| 1 | 48 | -0.2340 | 0.1279 | 0.2898 | -0.5645 | 2.1% |
| 2 | 20 | 0.8590 | 0.2903 | 0.3980 | -0.4400 | 100.0% |

## Volume profile

- Trade size : médian $0, p90 $4, p99 $47
- Total volume USDC : $538k
- Trades total : 150,361

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/madrid.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
