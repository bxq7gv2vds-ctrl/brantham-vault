# Wuhan — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **209** markets analysés
- **71,971** trades on-chain
- **$294k** volume total USDC
- Période : 2026-03-20 → 2026-04-08

## Outcomes

- YES wins : **19** (9.1%)
- NO wins : **190**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1600 | 0.3275 | 0.1126 | 0.1295 |
| `price_mid_avg` | 0.0020 | 0.0032 | 0.0228 | 0.1580 | 0.3420 | 0.1187 | 0.1950 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0082 | 0.0919 | 0.2875 |
| `drift_pp` | -0.2710 | -0.1190 | -0.0390 | -0.0100 | -0.0090 | -0.0207 | 0.2806 |
| `volatility_pp` | 0.0051 | 0.0097 | 0.0444 | 0.1006 | 0.2619 | 0.0820 | 0.1026 |
| `max_drawdown` | -0.5792 | -0.3890 | -0.1943 | -0.0590 | -0.0233 | -0.2582 | 0.2345 |
| `hurst` | 0.0567 | 0.1111 | 0.1775 | 0.3171 | 0.4043 | 0.2120 | 0.1351 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.1733 | 0.9618 | 4.241 | 4.187 | 25.239 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 133 | 2.3% | -0.0290 |
| [0.1, 0.2) | 34 | 17.6% | -0.1290 |
| [0.2, 0.3) | 18 | 16.7% | -0.2540 |
| [0.3, 0.4) | 13 | 38.5% | -0.3259 |
| [0.4, 0.5) | 7 | 28.6% | -0.4490 |
| [0.5, 0.6) | 4 | 0.0% | -0.4990 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 171 | 9.9% | 0.0600 | -0.0490 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **3** trades, WR=2.3%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.939 pp

## Patterns temporels

- **Heures peak (UTC)** : [8, 7, 6] (19,970 trades)
- **Heures calmes (UTC)** : [22, 18, 11] (4,318 trades)
- **Jours peak** : ['Mon', 'Fri']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0737 | 0.0242 | 25.189 |
| [0.25-0.50] | 0.0690 | 0.0135 | 38.273 |
| [0.50-0.75] | 0.0347 | 0.0118 | 77.869 |
| [0.75-1.00] | 0.0129 | 0.0096 | 212.552 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 145 | -0.0390 | 0.0173 | 0.1446 | -0.0990 | 0.0% |
| 1 | 19 | 0.7890 | 0.3357 | 0.4073 | -0.3600 | 100.0% |
| 2 | 45 | -0.1790 | 0.1218 | 0.3326 | -0.4950 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $50
- Total volume USDC : $294k
- Trades total : 71,971

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/wuhan.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
