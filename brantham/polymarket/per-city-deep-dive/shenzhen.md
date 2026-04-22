# Shenzhen — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **209** markets analysés
- **111,021** trades on-chain
- **$907k** volume total USDC
- Période : 2026-03-20 → 2026-04-08

## Outcomes

- YES wins : **19** (9.1%)
- NO wins : **190**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0400 | 0.1600 | 0.3000 | 0.1011 | 0.1195 |
| `price_mid_avg` | 0.0020 | 0.0040 | 0.0210 | 0.1150 | 0.3788 | 0.1177 | 0.2077 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0048 | 0.0918 | 0.2876 |
| `drift_pp` | -0.2510 | -0.1190 | -0.0290 | -0.0090 | -0.0090 | -0.0093 | 0.2836 |
| `volatility_pp` | 0.0043 | 0.0098 | 0.0284 | 0.1076 | 0.2377 | 0.0762 | 0.0974 |
| `max_drawdown` | -0.6896 | -0.4090 | -0.1990 | -0.0490 | -0.0190 | -0.2693 | 0.2554 |
| `hurst` | 0.0373 | 0.0974 | 0.1874 | 0.2805 | 0.3669 | 0.1938 | 0.1260 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.5197 | 1.693 | 0.8194 | 2.561 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 137 | 5.8% | -0.0190 |
| [0.1, 0.2) | 28 | 10.7% | -0.1295 |
| [0.2, 0.3) | 27 | 14.8% | -0.2190 |
| [0.3, 0.4) | 12 | 16.7% | -0.3390 |
| [0.4, 0.5) | 1 | 0.0% | -0.4890 |
| [0.5, 0.6) | 4 | 50.0% | 0.0000 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 170 | 10.6% | 0.0500 | -0.0390 |
| cold | 1 | 0.0% | 0.0200 | -0.0190 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **8** trades, WR=5.8%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.945 pp

## Patterns temporels

- **Heures peak (UTC)** : [7, 6, 5] (28,320 trades)
- **Heures calmes (UTC)** : [19, 13, 21] (6,953 trades)
- **Jours peak** : ['Fri', 'Wed']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0583 | 0.0180 | 26.645 |
| [0.25-0.50] | 0.0469 | 0.0179 | 52.141 |
| [0.50-0.75] | 0.0280 | 0.0119 | 106.966 |
| [0.75-1.00] | 0.0135 | 0.0124 | 360.441 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 139 | -0.0190 | 0.0142 | 0.1385 | -0.0790 | 0.0% |
| 1 | 19 | 0.8590 | 0.3278 | 0.3013 | -0.5910 | 100.0% |
| 2 | 51 | -0.1790 | 0.1269 | 0.2669 | -0.5090 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $7, p99 $97
- Total volume USDC : $907k
- Trades total : 111,021

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/shenzhen.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
