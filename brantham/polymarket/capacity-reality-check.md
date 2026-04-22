---
name: Polymarket Weather Capacity Reality Check
description: Analyse capacity 2026-04-22. Micro-marché volume median $749 Tier S. Plafond AUM $10-20k avant market impact. Système pas scalable comme vrai hedge fund sans multi-venue.
type: analysis
project: brantham/polymarket
created: 2026-04-22
tags: [polymarket, capacity, hedge-fund, realistic]
priority: critical
---

# Polymarket Weather — Capacity Reality Check

## TL;DR

**Plafond AUM ≈ $10-20k** avant que le market impact (5% volume threshold)
tue l'alpha. Ce n'est PAS un vrai hedge fund scalable. C'est un micro-strat
rentable à petit AUM uniquement.

## Mesures

Script : `research/pole_analysis/06_capacity_analysis.py`
Data : 85 signaux avec volume_usdc backfilled (sur 438 markets actifs fetched)

### Volume par tier

| Tier | n | vol median | vol P75 | our size | safe max (5%) | daily cap |
|------|--:|-----------:|--------:|--------:|--------------:|----------:|
| S (YES deep_OTM) | 23 | $749 | $749 | $32 | $37 | $29/day |
| A (NO workhorse) | 2 | $2,080 | $2,678 | $35 | $104 | $7/day |
| B (NO ITM) | 15 | $876 | $876 | $7 | $44 | $36/day |
| OTHER | 45 | $1,063 | $5,376 | $32 | $53 | $182/day |

### Scaling simulation

| Bankroll | Signals restant dans capacity |
|----------|-------------------------------|
| $10,000 | ~20% Tier B seulement |
| $100,000 | **0%** partout |
| $500,000+ | **0%** partout |

## Pourquoi

Un market "Austin T_max < 25°C on April 20" a typiquement $500-1000 de volume
cumulé. Prendre 5% = $25-50 position. Au-delà, on move le prix → l'edge
disparaît (on fill à un pire prix, puis la résolution n'est plus 100%
gagnante après slippage).

## Impact réel sur le P&L attendu

Hypothèses :
- Bankroll $10k
- ROI brut 2%/jour post-slippage
- 220 jours trading/an

**Rendement max réaliste** :
- **$200/jour**
- **$44,000/an**
- **440% ROI annuel en %** (impressionnant) → **$44k absolu** (petit)

À $100k bankroll ? **Le capacity limit transforme le 2%/jour en 0.2%/jour** car
on ne peut déployer que la moitié des signaux. **ROI attendu ~$20-40k/an**,
pas $880k (linéaire).

## Options pour vraiment scaler

1. **Multi-venue** (priorité) :
   - Kalshi weather — $100M+/mois, plus liquide, regulated (US)
   - Manifold — plus thin mais complementary
   - Polymarket non-weather si edge transférable

2. **Expand au-delà weather** :
   - Sports prediction (high volume mais edge différent)
   - Politics (macro opportunities)
   - Crypto predictions

3. **Accept micro-cap strategy** :
   - $10-20k AUM cap
   - $30-60k profit/an
   - Ne compte pas pour une vraie structure M&A Brantham

## Verdict pour Brantham Partners

**Ne pas compter sur Polymarket pour financer l'activité principale**.
Le système peut :
- Compléter un revenu personnel (~$3-5k/mois à petit AUM)
- Servir de R&D / laboratoire pour la méthodologie hedge-fund-grade
- Être un proof-of-concept pour attirer une mission capital markets

**Pas un print-cash generator.**

## Related

- [[_MOC]]
- [[dedup-bug-p-and-l-inflation]]
- [[odds-trajectories-findings]]
- [[research-findings-2026-04-21]]
- [[tier-s-v2-hedge-fund-gates]]
