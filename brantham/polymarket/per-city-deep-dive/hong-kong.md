# Hong Kong — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **260** markets analysés
- **140,256** trades on-chain
- **$1.09M** volume total USDC
- Période : 2026-03-13 → 2026-04-08

## Outcomes

- YES wins : **24** (9.3%)
- NO wins : **233**
- Ambiguous : 3

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0100 | 0.0300 | 0.1925 | 0.3200 | 0.1177 | 0.1425 |
| `price_mid_avg` | 0.0010 | 0.0014 | 0.0060 | 0.0798 | 0.4272 | 0.1057 | 0.2201 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0337 | 0.0944 | 0.2891 |
| `drift_pp` | -0.3100 | -0.1531 | -0.0190 | -0.0090 | -0.0059 | -0.0233 | 0.2812 |
| `volatility_pp` | 0.0030 | 0.0055 | 0.0267 | 0.1189 | 0.2256 | 0.0759 | 0.1012 |
| `max_drawdown` | -0.6890 | -0.4417 | -0.2090 | -0.0305 | -0.0190 | -0.2817 | 0.2685 |
| `hurst` | 0.0395 | 0.0911 | 0.1666 | 0.2563 | 0.3504 | 0.1785 | 0.1209 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.3398 | 1.526 | 1.006 | 4.670 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 157 | 2.5% | -0.0190 |
| [0.1, 0.2) | 37 | 21.6% | -0.1400 |
| [0.2, 0.3) | 28 | 14.3% | -0.2240 |
| [0.3, 0.4) | 22 | 18.2% | -0.3190 |
| [0.4, 0.5) | 5 | 0.0% | -0.4090 |
| [0.5, 0.6) | 6 | 50.0% | -0.0171 |
| [0.6, 0.7) | 1 | 0.0% | -0.6890 |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 1 | 100.0% | 0.1490 |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 212 | 8.6% | 0.0450 | -0.0190 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **4** trades, WR=2.5%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.970 pp

## Patterns temporels

- **Heures peak (UTC)** : [6, 5, 7] (34,624 trades)
- **Heures calmes (UTC)** : [20, 19, 21] (6,597 trades)
- **Jours peak** : ['Thu', 'Wed']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0478 | 0.0354 | 47.494 |
| [0.25-0.50] | 0.0184 | 0.0131 | 156.580 |
| [0.50-0.75] | 0.0051 | 0.0040 | 270.458 |
| [0.75-1.00] | 0.0017 | 0.0011 | 122.955 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 165 | -0.0190 | 0.0087 | 0.1254 | -0.0690 | 0.0% |
| 1 | 23 | 0.8090 | 0.3105 | 0.3337 | -0.5320 | 100.0% |
| 2 | 70 | -0.1940 | 0.1299 | 0.2537 | -0.5190 | 1.5% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $100
- Total volume USDC : $1.09M
- Trades total : 140,256

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/hong-kong.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
