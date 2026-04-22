# Los Angeles — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **179** markets analysés
- **89,055** trades on-chain
- **$294k** volume total USDC
- Période : 2025-12-04 → 2026-04-08

## Outcomes

- YES wins : **16** (9.1%)
- NO wins : **160**
- Ambiguous : 3

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0600 | 0.1750 | 0.2960 | 0.1165 | 0.1460 |
| `price_mid_avg` | 0.0020 | 0.0065 | 0.0280 | 0.1329 | 0.3328 | 0.1204 | 0.2110 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0157 | 0.0965 | 0.2932 |
| `drift_pp` | -0.2496 | -0.1419 | -0.0420 | -0.0090 | -0.0040 | -0.0200 | 0.2946 |
| `volatility_pp` | 0.0068 | 0.0198 | 0.0409 | 0.0921 | 0.2096 | 0.0764 | 0.0893 |
| `max_drawdown` | -0.5572 | -0.3740 | -0.2490 | -0.1190 | -0.0398 | -0.2775 | 0.2043 |
| `hurst` | 0.0364 | 0.0923 | 0.1648 | 0.2413 | 0.3405 | 0.1752 | 0.1199 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.2633 | 1.147 | 3.938 | 1.647 | 4.350 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 103 | 4.9% | -0.0190 |
| [0.1, 0.2) | 35 | 11.4% | -0.1090 |
| [0.2, 0.3) | 22 | 9.1% | -0.2090 |
| [0.3, 0.4) | 11 | 36.4% | -0.3190 |
| [0.4, 0.5) | 1 | 0.0% | -0.3990 |
| [0.5, 0.6) | 2 | 0.0% | -0.5040 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 1 | 100.0% | 0.1890 |
| [0.9, 1.0) | 1 | 0.0% | -0.9390 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| mild | 66 | 11.1% | 0.0500 | -0.0390 |
| warm | 76 | 5.3% | 0.1000 | -0.0690 |
| hot | 3 | 0.0% | 0.0200 | -0.0170 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **5** trades, WR=4.9%
- **Favorite losses** (open>0.90 + NO win) : **1** trades, WR=100.0%

- Long-shot payoff moyen : +0.959 pp

## Patterns temporels

- **Heures peak (UTC)** : [21, 20, 19] (20,126 trades)
- **Heures calmes (UTC)** : [6, 3, 4] (5,517 trades)
- **Jours peak** : ['Thu', 'Wed']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0741 | 0.0360 | 45.094 |
| [0.25-0.50] | 0.0675 | 0.0239 | 58.682 |
| [0.50-0.75] | 0.0365 | 0.0190 | 121.500 |
| [0.75-1.00] | 0.0151 | 0.0153 | 285.284 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 48 | -0.1802 | 0.0980 | 0.2601 | -0.4790 | 0.0% |
| 1 | 108 | -0.0290 | 0.0236 | 0.1239 | -0.1490 | 0.9% |
| 2 | 15 | 0.8390 | 0.3139 | 0.3291 | -0.4266 | 100.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $43
- Total volume USDC : $294k
- Trades total : 89,055

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/los-angeles.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
