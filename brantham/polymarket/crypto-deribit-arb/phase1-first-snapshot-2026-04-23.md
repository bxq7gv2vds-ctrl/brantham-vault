---
title: Phase 1 — Premier snapshot edge validation
date: 2026-04-23
status: positive-preliminary
parent: [[_MOC]]
tags: [phase1, validation, edge, bs-naive]
---

# Premier snapshot Phase 1 — résultats

**Timestamp** : 2026-04-23 11:44 UTC

## Setup

- **Pricing** : Black-Scholes naive avec ATM IV depuis Deribit (Phase 1 baseline, sans SVI smile)
- **Marchés** : Polymarket crypto BTC + ETH (above + between markets)
- **Filtres** : TTR > 6h, liquidity > $200, threshold edge_net 0.5%
- **Bid/Ask** : utilisés pour realistic fill prices (pas outcomePrices stale)

## Statistiques

| Métrique | Valeur |
|---|---|
| Marchés scannés | 195 (122 BTC + 73 ETH) |
| Signaux avec |edge| > 0.5% | **92** |
| Signaux avec |edge| > 2% | ~30 |
| Top edge | +13.2% |
| Médiane |edge| | 1.4% |
| BUY YES signals | 52 |
| BUY NO signals | 40 |

## Marchés crypto Polymarket disponibles

D'après scanning Gamma API :

| Pattern | Count | Math |
|---|---|---|
| "Will BTC be above $X on date" | 66 | Digital call : P(S(T) > K) |
| "Will ETH be above $X on date" | 33 | Idem |
| "Will BTC be between $X and $Y" | 18 | Digital double : P(K1 < S(T) < K2) |
| "Will ETH be between $X and $Y" | 18 | Idem |
| "Will BTC reach $X" / "dip to $X" | 50+ | Touch options — SKIPPED (math différente) |

## Top 5 signaux

| Asset | Type | TTR | Strike | Bid | Ask | Fair | Edge | Side |
|---|---|---|---|---|---|---|---|---|
| BTC | above | 12h | $78k | 0.21 | 0.22 | 0.36 | +13.2% | YES |
| BTC | between | 12h | $76-78k | 0.67 | 0.69 | 0.54 | +11.1% | NO |
| ETH | between | 12h | $2.2-2.3k | 0.18 | 0.22 | 0.30 | +6.3% | YES |
| ETH | between | 12h | $2.3-2.4k | 0.71 | 0.76 | 0.63 | +6.2% | NO |
| ETH | between | 36h | $2.4-2.5k | 0.09 | 0.10 | 0.16 | +5.8% | YES |

## Cohérence interne validée

Pour BTC ce soir (TTR 12h), les 3 markets adjacents :
- P(BTC > $76k) ≈ 0.95 (Polymarket)
- P(BTC between $76-78k) ≈ 0.68 (Polymarket)
- P(BTC > $78k) ≈ 0.21 (Polymarket)
- → P($76k < BTC < $78k) implicite = 0.95 - 0.21 = 0.74 (Polymarket)

Polymarket lui-même est 0.68 vs 0.74 implicite → **arb interne de 6pp possible** sans même Deribit !

## Caveats importants

1. **BS naive overestimates edges** : ATM IV ne capture pas le smile (skew + kurtosis). Le vrai fair_prob via SVI sera plus proche de Polymarket. Magnitude réelle des edges probablement 30-50% plus basse.

2. **Spreads larges intra-day** : bid-ask 1-5pp typique. Effective edge_net = edge théorique - 1/2 spread.

3. **Liquidité variable** : les top edges ont $15-30k liquidity, OK pour positions $50-200, slippage faible.

4. **Snapshot unique** : un seul instant. Faut loop 24h pour voir persistence vs noise transitoire.

## Décisions immédiates

1. **GO Phase 2** (validation préliminaire positive) — investir SVI smile pour pricing précis
2. **Setup snapshot loop 5min × 24h** pour mesurer persistence
3. **Build SVI smile fitter** prochaine étape

## Go/No-Go criterion vs Phase 1 plan

Plan : ≥10 brackets simultanés avec edge >2pp → GO.
**Réalité** : ~30 signaux avec edge >2pp. **GO confirmé.**

Mais avec caveat : magnitude probablement gonflée par BS naive. Re-mesurer après SVI Phase 2.

## Related

- [[_MOC]]
- [[architecture]]
- [[math-pricing-hedge]]
- [[roadmap]]
