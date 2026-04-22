# San Francisco — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **165** markets analysés
- **71,830** trades on-chain
- **$300k** volume total USDC
- Période : 2026-03-24 → 2026-04-08

## Outcomes

- YES wins : **13** (8.0%)
- NO wins : **149**
- Ambiguous : 3

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1500 | 0.2460 | 0.0939 | 0.1030 |
| `price_mid_avg` | 0.0020 | 0.0036 | 0.0140 | 0.1000 | 0.3264 | 0.1007 | 0.1807 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0100 | 0.0921 | 0.2876 |
| `drift_pp` | -0.2118 | -0.0990 | -0.0390 | -0.0090 | -0.0084 | -0.0018 | 0.2693 |
| `volatility_pp` | 0.0042 | 0.0084 | 0.0288 | 0.0787 | 0.1906 | 0.0659 | 0.0881 |
| `max_drawdown` | -0.6396 | -0.3290 | -0.1790 | -0.0490 | -0.0246 | -0.2438 | 0.2298 |
| `hurst` | 0.0517 | 0.1071 | 0.1708 | 0.2591 | 0.3208 | 0.1855 | 0.1066 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0986 | 0.7707 | 2.458 | 1.661 | 8.510 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 106 | 1.9% | -0.0190 |
| [0.1, 0.2) | 30 | 16.7% | -0.1075 |
| [0.2, 0.3) | 17 | 17.6% | -0.2290 |
| [0.3, 0.4) | 7 | 28.6% | -0.3190 |
| [0.4, 0.5) | 2 | 50.0% | 0.0650 |
| [0.5, 0.6) | 0 | — | — |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| cold | 2 | 0.0% | 0.0100 | -0.0090 |
| mild | 112 | 6.3% | 0.0500 | -0.0390 |
| warm | 21 | 10.5% | 0.1300 | -0.0890 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **2** trades, WR=1.9%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.934 pp

## Patterns temporels

- **Heures peak (UTC)** : [23, 21, 22] (14,025 trades)
- **Heures calmes (UTC)** : [6, 5, 4] (4,766 trades)
- **Jours peak** : ['Wed', 'Fri']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0546 | 0.0256 | 37.850 |
| [0.25-0.50] | 0.0434 | 0.0157 | 46.077 |
| [0.50-0.75] | 0.0240 | 0.0126 | 88.840 |
| [0.75-1.00] | 0.0111 | 0.0115 | 267.764 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 40 | -0.1495 | 0.0909 | 0.2644 | -0.4540 | 0.0% |
| 1 | 15 | 0.7890 | 0.3122 | 0.3076 | -0.5000 | 92.9% |
| 2 | 110 | -0.0290 | 0.0143 | 0.1268 | -0.0890 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $49
- Total volume USDC : $300k
- Trades total : 71,830

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/san-francisco.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
