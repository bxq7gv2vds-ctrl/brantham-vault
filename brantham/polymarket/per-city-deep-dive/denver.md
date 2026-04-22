# Denver — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **175** markets analysés
- **64,788** trades on-chain
- **$271k** volume total USDC
- Période : 2025-12-04 → 2026-04-08

## Outcomes

- YES wins : **12** (7.4%)
- NO wins : **151**
- Ambiguous : 12

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1800 | 0.3187 | 0.1097 | 0.1193 |
| `price_mid_avg` | 0.0020 | 0.0049 | 0.0230 | 0.1344 | 0.3243 | 0.1165 | 0.2096 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0020 | 0.0700 | 0.0992 | 0.2961 |
| `drift_pp` | -0.2942 | -0.1480 | -0.0290 | -0.0090 | 0.0600 | -0.0105 | 0.2912 |
| `volatility_pp` | 0.0043 | 0.0122 | 0.0396 | 0.0955 | 0.1892 | 0.0753 | 0.0966 |
| `max_drawdown` | -0.5969 | -0.4090 | -0.2090 | -0.0595 | -0.0200 | -0.2601 | 0.2284 |
| `hurst` | 0.0419 | 0.0846 | 0.1696 | 0.2365 | 0.3336 | 0.1765 | 0.1119 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.1423 | 0.6732 | 2.685 | 1.679 | 6.276 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 106 | 3.8% | -0.0190 |
| [0.1, 0.2) | 20 | 10.0% | -0.1190 |
| [0.2, 0.3) | 19 | 21.1% | -0.2190 |
| [0.3, 0.4) | 15 | 0.0% | -0.3290 |
| [0.4, 0.5) | 1 | 100.0% | 0.5029 |
| [0.5, 0.6) | 2 | 50.0% | 0.0000 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| cold | 24 | 4.5% | 0.0150 | -0.0090 |
| mild | 57 | 11.3% | 0.0800 | -0.0567 |
| warm | 51 | 4.3% | 0.0800 | -0.0490 |
| hot | 11 | 9.1% | 0.0500 | -0.0380 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **4** trades, WR=3.8%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.956 pp

## Patterns temporels

- **Heures peak (UTC)** : [23, 22, 0] (14,978 trades)
- **Heures calmes (UTC)** : [3, 5, 2] (3,957 trades)
- **Jours peak** : ['Fri', 'Mon']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0700 | 0.0324 | 27.576 |
| [0.25-0.50] | 0.0405 | 0.0160 | 38.306 |
| [0.50-0.75] | 0.0303 | 0.0136 | 94.988 |
| [0.75-1.00] | 0.0122 | 0.0115 | 219.430 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 15 | 0.8090 | 0.3045 | 0.3387 | -0.4650 | 90.9% |
| 1 | 107 | -0.0290 | 0.0142 | 0.1152 | -0.0950 | 0.9% |
| 2 | 48 | -0.1690 | 0.1005 | 0.2132 | -0.4540 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $47
- Total volume USDC : $271k
- Trades total : 64,788

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/denver.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
