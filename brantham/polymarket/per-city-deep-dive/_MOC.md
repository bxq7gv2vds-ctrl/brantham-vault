# Per-City Deep Dive — Summary

_Généré : 2026-04-22 14:58 UTC_

Source : 6 mois on-chain trades (subgraph Goldsky), 9,084,703 trades sur 17,597 markets, 38 villes.

## Top 10 par volume

| Ville | N markets | N trades | Volume | WR YES | open | vol | hurst |
|-------|----------:|---------:|-------:|-------:|-----:|----:|------:|
| **London** | 1,475 | 1,049,441 | $8.66M | 12.7% | 0.0600 | 0.0329 | 0.1658 |
| **New York** | 1,486 | 931,578 | $7.43M | 12.0% | 0.0700 | 0.0368 | 0.1642 |
| **Seoul** | 1,013 | 696,480 | $5.92M | 12.1% | 0.0600 | 0.0464 | 0.1649 |
| **Dallas** | 1,027 | 412,414 | $2.76M | 11.9% | 0.0400 | 0.0306 | 0.1490 |
| **Atlanta** | 1,020 | 434,179 | $2.47M | 11.9% | 0.0500 | 0.0296 | 0.1534 |
| **Wellington** | 684 | 312,315 | $2.46M | 11.1% | 0.0600 | 0.0338 | 0.1689 |
| **Shanghai** | 280 | 362,233 | $2.28M | 9.0% | 0.0500 | 0.0330 | 0.1971 |
| **Miami** | 697 | 423,994 | $2.22M | 11.0% | 0.0600 | 0.0301 | 0.1621 |
| **Tel Aviv** | 307 | 113,903 | $2.21M | 9.4% | 0.0500 | 0.0263 | 0.1528 |
| **Chicago** | 698 | 398,810 | $2.12M | 10.6% | 0.0700 | 0.0387 | 0.1765 |

## Top 10 YES win rate (NO bookies trop conservateurs ?)

| Ville | WR YES | open med | vol | hurst | N |
|-------|-------:|---------:|----:|------:|--:|
| London | **12.7%** | 0.0600 | 0.0329 | 0.1658 | 1,475 |
| Buenos Aires | **12.2%** | 0.0500 | 0.0347 | 0.1540 | 1,013 |
| Seoul | **12.1%** | 0.0600 | 0.0464 | 0.1649 | 1,013 |
| New York | **12.0%** | 0.0700 | 0.0368 | 0.1642 | 1,486 |
| Dallas | **11.9%** | 0.0400 | 0.0306 | 0.1490 | 1,027 |
| Atlanta | **11.9%** | 0.0500 | 0.0296 | 0.1534 | 1,020 |
| Wellington | **11.1%** | 0.0600 | 0.0338 | 0.1689 | 684 |
| Miami | **11.0%** | 0.0600 | 0.0301 | 0.1621 | 697 |
| Chicago | **10.6%** | 0.0700 | 0.0387 | 0.1765 | 698 |
| Toronto | **10.5%** | 0.0600 | 0.0393 | 0.1608 | 1,024 |

## Top 10 mean reversion (Hurst le plus bas)

_Hurst < 0.5 = mean reverting → CONVEX_YES strategy edge_

| Ville | hurst | drift | vol | WR YES | N |
|-------|------:|------:|----:|-------:|--:|
| Busan | **0.1366** | -0.0330 | 0.0297 | 9.2% | 66 |
| Seattle | **0.1489** | -0.0290 | 0.0320 | 8.9% | 1,011 |
| Dallas | **0.1490** | -0.0190 | 0.0306 | 11.9% | 1,027 |
| Mexico City | **0.1498** | -0.0390 | 0.0309 | 9.1% | 99 |
| Tel Aviv | **0.1528** | -0.0290 | 0.0263 | 9.4% | 307 |
| Atlanta | **0.1534** | -0.0290 | 0.0296 | 11.9% | 1,020 |
| Buenos Aires | **0.1540** | -0.0290 | 0.0347 | 12.2% | 1,013 |
| Toronto | **0.1608** | -0.0295 | 0.0393 | 10.5% | 1,024 |
| Miami | **0.1621** | -0.0290 | 0.0301 | 11.0% | 697 |
| Singapore | **0.1624** | -0.0190 | 0.0217 | 9.0% | 280 |

## Top 10 volatilité (timing entry critique)

| Ville | vol med | drift | hurst | WR YES | N |
|-------|--------:|------:|------:|-------:|--:|
| Taipei | **0.0540** | -0.0290 | 0.1641 | 9.2% | 253 |
| Seoul | **0.0464** | -0.0290 | 0.1649 | 12.1% | 1,013 |
| Wuhan | **0.0444** | -0.0390 | 0.1775 | 9.1% | 209 |
| Los Angeles | **0.0409** | -0.0420 | 0.1648 | 9.1% | 179 |
| Denver | **0.0396** | -0.0290 | 0.1696 | 7.4% | 175 |
| Toronto | **0.0393** | -0.0295 | 0.1608 | 10.5% | 1,024 |
| Chicago | **0.0387** | -0.0490 | 0.1765 | 10.6% | 698 |
| Beijing | **0.0378** | -0.0290 | 0.1914 | 9.2% | 209 |
| Chongqing | **0.0372** | -0.0290 | 0.1920 | 9.1% | 209 |
| New York | **0.0368** | -0.0390 | 0.1642 | 12.0% | 1,486 |

## Top 10 long-shot wins (edge upside potential)

_Markets où prix open <0.10 et YES gagne : NO était favori, bookies wrong._

| Ville | long-shot WR | favorite loss WR | N markets |
|-------|-------------:|-----------------:|----------:|
| Taipei | 6.5% | 100.0% | 253 |
| Shenzhen | 5.8% | 0.0% | 209 |
| Madrid | 5.3% | 0.0% | 253 |
| Los Angeles | 4.9% | 100.0% | 179 |
| Istanbul | 4.7% | 0.0% | 110 |
| Shanghai | 4.6% | 100.0% | 280 |
| Chengdu | 4.6% | 0.0% | 198 |
| Moscow | 4.2% | 0.0% | 99 |
| Chicago | 4.2% | 0.0% | 698 |
| Seoul | 4.0% | 20.0% | 1,013 |

## Liens vers fiches détaillées

- [[atlanta|Atlanta]]
- [[austin|Austin]]
- [[beijing|Beijing]]
- [[buenos-aires|Buenos Aires]]
- [[busan|Busan]]
- [[chengdu|Chengdu]]
- [[chicago|Chicago]]
- [[chongqing|Chongqing]]
- [[dallas|Dallas]]
- [[denver|Denver]]
- [[hong-kong|Hong Kong]]
- [[houston|Houston]]
- [[istanbul|Istanbul]]
- [[london|London]]
- [[los-angeles|Los Angeles]]
- [[lucknow|Lucknow]]
- [[madrid|Madrid]]
- [[mexico-city|Mexico City]]
- [[miami|Miami]]
- [[milan|Milan]]
- [[moscow|Moscow]]
- [[munich|Munich]]
- [[new-york|New York]]
- [[paris|Paris]]
- [[san-francisco|San Francisco]]
- [[sao-paulo|Sao Paulo]]
- [[seattle|Seattle]]
- [[seoul|Seoul]]
- [[shanghai|Shanghai]]
- [[shenzhen|Shenzhen]]
- [[singapore|Singapore]]
- [[taipei|Taipei]]
- [[tel-aviv|Tel Aviv]]
- [[tokyo|Tokyo]]
- [[toronto|Toronto]]
- [[warsaw|Warsaw]]
- [[wellington|Wellington]]
- [[wuhan|Wuhan]]

## Visualisations

- `research/outputs/11_per_city_deep_dive/_OVERVIEW.html` — overview cross-city interactif
- `research/outputs/11_per_city_deep_dive/<city>.html` — 38 dashboards interactifs par ville (8 panels chacun)

## Related

- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 gates]]