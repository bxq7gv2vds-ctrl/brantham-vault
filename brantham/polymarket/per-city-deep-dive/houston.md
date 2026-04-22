# Houston — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **165** markets analysés
- **63,118** trades on-chain
- **$212k** volume total USDC
- Période : 2026-03-24 → 2026-04-08

## Outcomes

- YES wins : **14** (8.5%)
- NO wins : **150**
- Ambiguous : 1

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0400 | 0.1700 | 0.3020 | 0.0990 | 0.1160 |
| `price_mid_avg` | 0.0020 | 0.0040 | 0.0124 | 0.0942 | 0.3360 | 0.0946 | 0.1608 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0096 | 0.0920 | 0.2877 |
| `drift_pp` | -0.2686 | -0.0890 | -0.0290 | -0.0090 | -0.0090 | -0.0070 | 0.2769 |
| `volatility_pp` | 0.0041 | 0.0096 | 0.0286 | 0.0904 | 0.1904 | 0.0689 | 0.0895 |
| `max_drawdown` | -0.5796 | -0.3772 | -0.1680 | -0.0590 | -0.0246 | -0.2472 | 0.2276 |
| `hurst` | 0.0368 | 0.0912 | 0.1683 | 0.2507 | 0.3377 | 0.1809 | 0.1204 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.1151 | 1.056 | 4.988 | 3.538 | 18.445 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 111 | 1.8% | -0.0190 |
| [0.1, 0.2) | 20 | 30.0% | -0.1260 |
| [0.2, 0.3) | 16 | 12.5% | -0.2240 |
| [0.3, 0.4) | 14 | 21.4% | -0.3190 |
| [0.4, 0.5) | 2 | 50.0% | 0.0100 |
| [0.5, 0.6) | 1 | 0.0% | -0.4990 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| mild | 19 | 5.3% | 0.0300 | -0.0190 |
| warm | 87 | 15.1% | 0.0700 | -0.0390 |
| hot | 29 | 0.0% | 0.0300 | -0.0290 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **2** trades, WR=1.8%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.924 pp

## Patterns temporels

- **Heures peak (UTC)** : [21, 18, 22] (13,477 trades)
- **Heures calmes (UTC)** : [3, 6, 4] (4,220 trades)
- **Jours peak** : ['Sat', 'Tue']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0480 | 0.0256 | 25.352 |
| [0.25-0.50] | 0.0398 | 0.0169 | 32.821 |
| [0.50-0.75] | 0.0194 | 0.0109 | 84.000 |
| [0.75-1.00] | 0.0103 | 0.0110 | 243.018 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 113 | -0.0190 | 0.0151 | 0.1203 | -0.0890 | 0.0% |
| 1 | 37 | -0.1890 | 0.1156 | 0.2549 | -0.4625 | 0.0% |
| 2 | 15 | 0.8190 | 0.2938 | 0.2835 | -0.4700 | 100.0% |

## Volume profile

- Trade size : médian $0, p90 $4, p99 $40
- Total volume USDC : $212k
- Trades total : 63,118

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/houston.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
