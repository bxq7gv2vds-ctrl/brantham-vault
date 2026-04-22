# Chengdu — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **198** markets analysés
- **68,085** trades on-chain
- **$295k** volume total USDC
- Période : 2026-03-20 → 2026-04-08

## Outcomes

- YES wins : **17** (8.6%)
- NO wins : **180**
- Ambiguous : 1

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0400 | 0.1400 | 0.2660 | 0.0975 | 0.1220 |
| `price_mid_avg` | 0.0020 | 0.0046 | 0.0153 | 0.0919 | 0.3160 | 0.1053 | 0.1956 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0043 | 0.0919 | 0.2876 |
| `drift_pp` | -0.1990 | -0.0990 | -0.0290 | -0.0090 | -0.0080 | -0.0056 | 0.2783 |
| `volatility_pp` | 0.0044 | 0.0088 | 0.0297 | 0.0863 | 0.2015 | 0.0687 | 0.0934 |
| `max_drawdown` | -0.6179 | -0.3245 | -0.1590 | -0.0490 | -0.0190 | -0.2297 | 0.2298 |
| `hurst` | 0.0288 | 0.0813 | 0.1696 | 0.2577 | 0.3513 | 0.1774 | 0.1268 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.5850 | 3.208 | 1.187 | 3.426 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 131 | 4.6% | -0.0190 |
| [0.1, 0.2) | 33 | 6.1% | -0.1390 |
| [0.2, 0.3) | 15 | 20.0% | -0.1990 |
| [0.3, 0.4) | 9 | 33.3% | -0.3190 |
| [0.4, 0.5) | 5 | 20.0% | -0.4390 |
| [0.5, 0.6) | 3 | 66.7% | 0.4990 |
| [0.6, 0.7) | 1 | 0.0% | -0.6143 |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 162 | 7.5% | 0.0500 | -0.0390 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **6** trades, WR=4.6%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.971 pp

## Patterns temporels

- **Heures peak (UTC)** : [7, 5, 6] (16,594 trades)
- **Heures calmes (UTC)** : [19, 21, 11] (3,546 trades)
- **Jours peak** : ['Mon', 'Fri']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0565 | 0.0206 | 31.595 |
| [0.25-0.50] | 0.0400 | 0.0115 | 42.194 |
| [0.50-0.75] | 0.0222 | 0.0075 | 70.047 |
| [0.75-1.00] | 0.0086 | 0.0055 | 208.333 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 147 | -0.0290 | 0.0177 | 0.1252 | -0.0990 | 1.4% |
| 1 | 16 | 0.8540 | 0.3271 | 0.3098 | -0.5599 | 100.0% |
| 2 | 34 | -0.1990 | 0.1315 | 0.3086 | -0.4840 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $53
- Total volume USDC : $295k
- Trades total : 68,085

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/chengdu.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
