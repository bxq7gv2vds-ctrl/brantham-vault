# Moscow — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **99** markets analysés
- **40,203** trades on-chain
- **$138k** volume total USDC
- Période : 2026-03-30 → 2026-04-08

## Outcomes

- YES wins : **9** (9.1%)
- NO wins : **90**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0400 | 0.1050 | 0.3100 | 0.0952 | 0.1291 |
| `price_mid_avg` | 0.0020 | 0.0031 | 0.0106 | 0.0541 | 0.3410 | 0.1093 | 0.2288 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0020 | 0.0918 | 0.2884 |
| `drift_pp` | -0.1767 | -0.0885 | -0.0290 | -0.0090 | -0.0090 | -0.0035 | 0.2512 |
| `volatility_pp` | 0.0054 | 0.0096 | 0.0223 | 0.0622 | 0.1709 | 0.0569 | 0.0824 |
| `max_drawdown` | -0.5130 | -0.2940 | -0.1470 | -0.0545 | -0.0270 | -0.2060 | 0.2103 |
| `hurst` | 0.0563 | 0.0940 | 0.1707 | 0.2670 | 0.3535 | 0.1875 | 0.1133 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.1893 | 0.1977 | 0.8909 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 71 | 4.2% | -0.0190 |
| [0.1, 0.2) | 14 | 7.1% | -0.1490 |
| [0.2, 0.3) | 3 | 0.0% | -0.1990 |
| [0.3, 0.4) | 5 | 20.0% | -0.3090 |
| [0.4, 0.5) | 0 | — | — |
| [0.5, 0.6) | 6 | 66.7% | 0.4990 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 81 | 6.2% | 0.0400 | -0.0290 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **3** trades, WR=4.2%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.939 pp

## Patterns temporels

- **Heures peak (UTC)** : [15, 8, 12] (9,581 trades)
- **Heures calmes (UTC)** : [2, 1, 0] (1,778 trades)
- **Jours peak** : ['Mon', 'Wed']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0469 | 0.0208 | 21.163 |
| [0.25-0.50] | 0.0346 | 0.0153 | 57.494 |
| [0.50-0.75] | 0.0219 | 0.0100 | 127.422 |
| [0.75-1.00] | 0.0041 | 0.0044 | 227.884 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 19 | -0.1490 | 0.1067 | 0.2847 | -0.4490 | 0.0% |
| 1 | 7 | 0.8390 | 0.3280 | 0.3252 | -0.3817 | 100.0% |
| 2 | 65 | -0.0190 | 0.0156 | 0.1403 | -0.0990 | 3.1% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $46
- Total volume USDC : $138k
- Trades total : 40,203

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/moscow.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
