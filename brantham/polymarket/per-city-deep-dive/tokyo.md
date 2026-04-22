# Tokyo — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **307** markets analysés
- **205,411** trades on-chain
- **$1.43M** volume total USDC
- Période : 2026-03-10 → 2026-04-08

## Outcomes

- YES wins : **29** (9.4%)
- NO wins : **278**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1855 | 0.3100 | 0.1080 | 0.1227 |
| `price_mid_avg` | 0.0020 | 0.0031 | 0.0144 | 0.1403 | 0.3908 | 0.1177 | 0.2112 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0024 | 0.0953 | 0.2923 |
| `drift_pp` | -0.2690 | -0.1340 | -0.0290 | -0.0090 | -0.0064 | -0.0126 | 0.2837 |
| `volatility_pp` | 0.0037 | 0.0091 | 0.0255 | 0.0891 | 0.2563 | 0.0730 | 0.0993 |
| `max_drawdown` | -0.6732 | -0.4015 | -0.1767 | -0.0497 | -0.0200 | -0.2583 | 0.2407 |
| `hurst` | 0.0652 | 0.1197 | 0.1964 | 0.2773 | 0.3580 | 0.2034 | 0.1120 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.6885 | 3.831 | 1.568 | 6.109 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 191 | 3.1% | -0.0190 |
| [0.1, 0.2) | 41 | 7.3% | -0.1480 |
| [0.2, 0.3) | 43 | 32.6% | -0.2090 |
| [0.3, 0.4) | 22 | 22.7% | -0.3190 |
| [0.4, 0.5) | 7 | 14.3% | -0.4090 |
| [0.5, 0.6) | 2 | 0.0% | -0.4990 |
| [0.6, 0.7) | 1 | 0.0% | -0.6990 |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 249 | 11.2% | 0.0600 | -0.0390 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **6** trades, WR=3.1%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.959 pp

## Patterns temporels

- **Heures peak (UTC)** : [7, 6, 5] (54,864 trades)
- **Heures calmes (UTC)** : [21, 18, 20] (13,793 trades)
- **Jours peak** : ['Thu', 'Fri']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0602 | 0.0244 | 39.727 |
| [0.25-0.50] | 0.0427 | 0.0166 | 65.762 |
| [0.50-0.75] | 0.0235 | 0.0114 | 135.055 |
| [0.75-1.00] | 0.0128 | 0.0118 | 435.439 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 216 | -0.0286 | 0.0153 | 0.1537 | -0.0935 | 0.0% |
| 1 | 62 | -0.2190 | 0.1254 | 0.2949 | -0.5687 | 0.0% |
| 2 | 29 | 0.7690 | 0.3127 | 0.3382 | -0.4610 | 100.0% |

## Volume profile

- Trade size : médian $0, p90 $6, p99 $91
- Total volume USDC : $1.43M
- Trades total : 205,411

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/tokyo.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
