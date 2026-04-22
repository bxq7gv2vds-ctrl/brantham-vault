# Beijing — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **209** markets analysés
- **111,000** trades on-chain
- **$546k** volume total USDC
- Période : 2026-03-20 → 2026-04-08

## Outcomes

- YES wins : **19** (9.2%)
- NO wins : **187**
- Ambiguous : 3

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1600 | 0.3200 | 0.1125 | 0.1299 |
| `price_mid_avg` | 0.0020 | 0.0040 | 0.0200 | 0.1161 | 0.3544 | 0.1047 | 0.1825 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0318 | 0.0956 | 0.2903 |
| `drift_pp` | -0.2730 | -0.1190 | -0.0290 | -0.0090 | 0.0006 | -0.0168 | 0.2655 |
| `volatility_pp` | 0.0052 | 0.0136 | 0.0378 | 0.0912 | 0.1949 | 0.0746 | 0.0921 |
| `max_drawdown` | -0.5190 | -0.3690 | -0.1890 | -0.0890 | -0.0308 | -0.2493 | 0.2057 |
| `hurst` | 0.0544 | 0.1056 | 0.1914 | 0.2889 | 0.3780 | 0.1997 | 0.1341 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.3231 | 2.218 | 2.265 | 9.882 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 118 | 0.8% | -0.0190 |
| [0.1, 0.2) | 50 | 10.0% | -0.1270 |
| [0.2, 0.3) | 11 | 36.4% | -0.2590 |
| [0.3, 0.4) | 19 | 31.6% | -0.3091 |
| [0.4, 0.5) | 4 | 25.0% | -0.4531 |
| [0.5, 0.6) | 3 | 33.3% | -0.4990 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 1 | 100.0% | 0.1990 |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 171 | 11.3% | 0.1000 | -0.0390 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **1** trades, WR=0.8%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.929 pp

## Patterns temporels

- **Heures peak (UTC)** : [7, 6, 5] (28,378 trades)
- **Heures calmes (UTC)** : [20, 15, 21] (6,565 trades)
- **Jours peak** : ['Tue', 'Wed']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0706 | 0.0273 | 34.522 |
| [0.25-0.50] | 0.0561 | 0.0199 | 58.365 |
| [0.50-0.75] | 0.0290 | 0.0131 | 132.976 |
| [0.75-1.00] | 0.0095 | 0.0082 | 309.861 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 138 | -0.0290 | 0.0189 | 0.1358 | -0.1185 | 0.0% |
| 1 | 18 | 0.7490 | 0.3148 | 0.3836 | -0.3300 | 100.0% |
| 2 | 53 | -0.1690 | 0.1048 | 0.3050 | -0.4680 | 1.9% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $50
- Total volume USDC : $546k
- Trades total : 111,000

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/beijing.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
