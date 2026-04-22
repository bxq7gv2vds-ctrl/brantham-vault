# Istanbul — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **110** markets analysés
- **45,721** trades on-chain
- **$226k** volume total USDC
- Période : 2026-03-30 → 2026-04-08

## Outcomes

- YES wins : **10** (9.1%)
- NO wins : **100**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0125 | 0.0600 | 0.1500 | 0.2919 | 0.1122 | 0.1318 |
| `price_mid_avg` | 0.0022 | 0.0050 | 0.0300 | 0.1662 | 0.3306 | 0.1163 | 0.1740 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0047 | 0.0920 | 0.2882 |
| `drift_pp` | -0.2711 | -0.1365 | -0.0340 | -0.0090 | -0.0071 | -0.0202 | 0.2996 |
| `volatility_pp` | 0.0042 | 0.0141 | 0.0350 | 0.1083 | 0.2408 | 0.0834 | 0.1066 |
| `max_drawdown` | -0.6130 | -0.4490 | -0.2246 | -0.0800 | -0.0288 | -0.2871 | 0.2471 |
| `hurst` | 0.0663 | 0.1047 | 0.1828 | 0.2572 | 0.3509 | 0.1904 | 0.1113 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.1318 | 0.8468 | 0.6668 | 3.152 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 64 | 4.7% | -0.0190 |
| [0.1, 0.2) | 25 | 8.0% | -0.1290 |
| [0.2, 0.3) | 11 | 36.4% | -0.2090 |
| [0.3, 0.4) | 3 | 33.3% | -0.3190 |
| [0.4, 0.5) | 2 | 0.0% | -0.4460 |
| [0.5, 0.6) | 5 | 0.0% | -0.5080 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 90 | 10.0% | 0.0750 | -0.0590 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **3** trades, WR=4.7%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.972 pp

## Patterns temporels

- **Heures peak (UTC)** : [13, 12, 11] (11,043 trades)
- **Heures calmes (UTC)** : [4, 22, 5] (2,295 trades)
- **Jours peak** : ['Tue', 'Mon']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0651 | 0.0236 | 17.206 |
| [0.25-0.50] | 0.0429 | 0.0180 | 39.861 |
| [0.50-0.75] | 0.0393 | 0.0194 | 90.953 |
| [0.75-1.00] | 0.0191 | 0.0203 | 274.569 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 32 | -0.1540 | 0.1128 | 0.2614 | -0.4990 | 0.0% |
| 1 | 68 | -0.0210 | 0.0168 | 0.1318 | -0.1023 | 0.0% |
| 2 | 10 | 0.8120 | 0.3831 | 0.3445 | -0.5050 | 100.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $50
- Total volume USDC : $226k
- Trades total : 45,721

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/istanbul.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
