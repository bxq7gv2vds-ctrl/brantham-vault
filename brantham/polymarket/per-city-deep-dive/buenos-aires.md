# Buenos Aires — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **1,013** markets analysés
- **353,565** trades on-chain
- **$1.90M** volume total USDC
- Période : 2025-12-06 → 2026-04-08

## Outcomes

- YES wins : **122** (12.2%)
- NO wins : **880**
- Ambiguous : 11

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1800 | 0.4000 | 0.1433 | 0.2068 |
| `price_mid_avg` | 0.0014 | 0.0050 | 0.0284 | 0.1616 | 0.4180 | 0.1356 | 0.2268 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0020 | 0.9990 | 0.1260 | 0.3286 |
| `drift_pp` | -0.2788 | -0.1190 | -0.0290 | -0.0090 | 0.2990 | -0.0173 | 0.3104 |
| `volatility_pp` | 0.0040 | 0.0099 | 0.0347 | 0.1026 | 0.2455 | 0.0787 | 0.1011 |
| `max_drawdown` | -0.6900 | -0.4380 | -0.1890 | -0.0490 | -0.0190 | -0.2779 | 0.2702 |
| `hurst` | 0.0258 | 0.0823 | 0.1540 | 0.2325 | 0.3332 | 0.1638 | 0.1180 |
| `half_life_minutes` | 0.0000 | 0.1371 | 0.9825 | 4.133 | 12.479 | 5.164 | 13.415 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 612 | 3.8% | -0.0190 |
| [0.1, 0.2) | 158 | 14.6% | -0.1290 |
| [0.2, 0.3) | 96 | 25.0% | -0.1990 |
| [0.3, 0.4) | 33 | 21.2% | -0.3390 |
| [0.4, 0.5) | 24 | 33.3% | -0.3990 |
| [0.5, 0.6) | 26 | 34.6% | -0.5085 |
| [0.6, 0.7) | 13 | 30.8% | -0.6300 |
| [0.7, 0.8) | 6 | 66.7% | 0.2240 |
| [0.8, 0.9) | 14 | 57.1% | 0.1190 |
| [0.9, 1.0) | 20 | 60.0% | 0.0190 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 373 | 11.2% | 0.1000 | -0.0590 |
| cold | 394 | 8.7% | 0.0400 | -0.0275 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **23** trades, WR=3.8%
- **Favorite losses** (open>0.90 + NO win) : **8** trades, WR=42.1%

- Long-shot payoff moyen : +0.957 pp

## Patterns temporels

- **Heures peak (UTC)** : [18, 17, 16] (70,537 trades)
- **Heures calmes (UTC)** : [4, 23, 2] (23,526 trades)
- **Jours peak** : ['Mon', 'Sun']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0538 | 0.0220 | 40.147 |
| [0.25-0.50] | 0.0416 | 0.0159 | 56.444 |
| [0.50-0.75] | 0.0289 | 0.0135 | 90.685 |
| [0.75-1.00] | 0.0160 | 0.0129 | 173.385 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 684 | -0.0190 | 0.0160 | 0.1392 | -0.0890 | 2.5% |
| 1 | 226 | -0.1990 | 0.1213 | 0.1736 | -0.6040 | 6.4% |
| 2 | 94 | 0.8040 | 0.3202 | 0.3140 | -0.4658 | 98.9% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $70
- Total volume USDC : $1.90M
- Trades total : 353,565

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/buenos-aires.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
