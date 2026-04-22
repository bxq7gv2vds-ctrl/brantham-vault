# Lucknow — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **352** markets analysés
- **150,878** trades on-chain
- **$1.13M** volume total USDC
- Période : 2026-03-05 → 2026-04-08

## Outcomes

- YES wins : **34** (9.7%)
- NO wins : **318**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0100 | 0.0200 | 0.1125 | 0.3090 | 0.1027 | 0.1733 |
| `price_mid_avg` | 0.0010 | 0.0020 | 0.0060 | 0.0476 | 0.4427 | 0.1081 | 0.2376 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0127 | 0.0978 | 0.2951 |
| `drift_pp` | -0.1988 | -0.0490 | -0.0190 | -0.0090 | -0.0020 | -0.0049 | 0.2177 |
| `volatility_pp` | 0.0023 | 0.0038 | 0.0141 | 0.0513 | 0.1373 | 0.0484 | 0.0788 |
| `max_drawdown` | -0.4990 | -0.2592 | -0.0850 | -0.0190 | -0.0131 | -0.1811 | 0.2268 |
| `hurst` | 0.0534 | 0.1007 | 0.1637 | 0.2322 | 0.3107 | 0.1732 | 0.0993 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.7874 | 2.213 | 1.116 | 4.026 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 254 | 0.8% | -0.0190 |
| [0.1, 0.2) | 33 | 12.1% | -0.1190 |
| [0.2, 0.3) | 29 | 20.7% | -0.2095 |
| [0.3, 0.4) | 14 | 35.7% | -0.3190 |
| [0.4, 0.5) | 4 | 25.0% | -0.4090 |
| [0.5, 0.6) | 6 | 83.3% | 0.4990 |
| [0.6, 0.7) | 3 | 66.7% | 0.3127 |
| [0.7, 0.8) | 2 | 100.0% | 0.2290 |
| [0.8, 0.9) | 5 | 100.0% | 0.1522 |
| [0.9, 1.0) | 2 | 100.0% | 0.0590 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 4 | 0.0% | 0.0600 | -0.0590 |
| cold | 280 | 5.0% | 0.0200 | -0.0190 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **2** trades, WR=0.8%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.934 pp

## Patterns temporels

- **Heures peak (UTC)** : [8, 9, 10] (40,465 trades)
- **Heures calmes (UTC)** : [20, 19, 23] (9,716 trades)
- **Jours peak** : ['Fri', 'Mon']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0233 | 0.0154 | 43.601 |
| [0.25-0.50] | 0.0144 | 0.0067 | 64.977 |
| [0.50-0.75] | 0.0052 | 0.0030 | 99.735 |
| [0.75-1.00] | 0.0031 | 0.0024 | 223.086 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 272 | -0.0190 | 0.0087 | 0.1473 | -0.0490 | 2.9% |
| 1 | 23 | 0.7090 | 0.2960 | 0.3119 | -0.4000 | 100.0% |
| 2 | 57 | -0.2095 | 0.1129 | 0.2600 | -0.4980 | 5.3% |

## Volume profile

- Trade size : médian $0, p90 $6, p99 $78
- Total volume USDC : $1.13M
- Trades total : 150,878

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/lucknow.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
