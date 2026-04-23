---
title: Décision — Polymarket × Deribit Crypto Arb via Portfolio of Edges
date: 2026-04-23
status: validated → build phase 1
type: decision
tags: [polymarket, deribit, hedge, statistical-arb, crypto]
---

# Décision : Construire un système d'arbitrage statistique Polymarket × Deribit en mode "portfolio of edges"

## Contexte

Paul demande de construire une stratégie de trading rentable entre Polymarket (brackets crypto BTC/ETH) et Deribit (options) avec hedging. Capital initial $1000. Objectif optionnalité de scaler à $50-200k AUM si validé.

## Décisions clés

### 1. Approche : Portfolio of edges (statistical arbitrage)

**Pas** chasser un trade parfait latency-critical (HFT pur).
**Mais** construire portefeuille de N positions micro hedgées en continu, diversification √N réduit variance.

**Pourquoi** :
- Marche avec micro-capital ($1000)
- Pas latency-critical (rebalance 60s, Hetzner suffit)
- Robuste aux disparitions individuelles d'edge
- Math hedge-fund-grade rigoureuse
- Scalable jusqu'à plafond capacity ~$250-500k AUM

### 2. Marchés ciblés

**Primary** : Polymarket weekly + monthly brackets BTC/ETH (settlement Chainlink Data Streams).
**Secondary** : possiblement daily brackets si edge confirmé.
**Skip** : 5min UP/DOWN markets — pas hedgeable via Deribit options (pas d'expiry matching).

### 3. Hedge instruments

- **Hyperliquid perp BTC/ETH** : delta hedge primaire (frais 0.025%)
- **Deribit USDC linear options BTC/ETH** : long premium pour Greeks-matching (vega, gamma)
- **Pas** de short naked options Deribit pour $1000 (margin trop limitante)

Min order Deribit linear : 0.01 BTC ($500 notional) — accessible avec long premium ($2-15 par contract OTM).

### 4. Math centrale

- **Pricing** : SVI smile fit + Breeden-Litzenberger density extraction
- **Fair value bracket** : ∫_{K1}^{K2} f(K) dK
- **Sizing** : Kelly fractional (α=0.25) avec Ledoit-Wolf shrinkage
- **Hedge optimization** : cvxpy minimize cost s.t. Δ=0, |Vega|<cap, |Γ|<cap
- **Rebalancing** : 60s soft, 5min hard

### 5. Capital allocation $1000

- Polymarket positions : $400
- Deribit options hedge (long premium) : $150
- Hyperliquid perp collateral : $100 (× 5x leverage)
- Reserve : $350

### 6. Stack technique

Réutilise polymarket-hedge existant (70% reusable selon audit).

Nouveau module : `src/pmhedge/crypto_arb/`
Stack : Python 3.13 + uv + numpy + numba + scipy + cvxpy + DuckDB + websockets + loguru.

### 7. Phases de build

| Phase | Durée | Go/No-Go criterion |
|---|---|---|
| 1 — Data + validation empirique | 1-2j | ≥10 brackets simultanés avec edge >2pp |
| 2 — Pricing engine production | 2-3j | Cycle complet <2s |
| 3 — Portfolio + hedge | 2-3j | Hedge cost <30% edge gross |
| 4 — Paper trading 7j | 7j | Sharpe paper >1.5 |
| 5 — Live $200 → $1000 | 14j | Live ratio >0.6 vs paper |

## Alternatives considérées et rejetées

### Alt 1 : HFT pur sur 5min UP/DOWN markets
**Rejetée** car : latency-critical (besoin AWS Tokyo $80/mo), pas d'options Deribit 5min pour hedge, edge purement directionnel = grosse variance, ne marche pas avec $1000.

### Alt 2 : Single-trade arb avec hedge perfect
**Rejetée** car : fragile aux disparitions edge, latency wars, pas scalable, pas robuste.

### Alt 3 : Pure Polymarket directional sans hedge
**Rejetée** car : variance explosive, pas hedge fund grade, $1000 disparaît en quelques mauvaises séries.

### Alt 4 : Greek-matching exact via butterflies Deribit étroits
**Partiellement adopté** : utilisé pour weekly+ brackets quand min order Deribit permet (> $250 notional bracket position).

## Engagements honnêtes

- Pas de promesse de gains — math validée mais edge réel doit être mesuré sur live
- Phase 1 obligatoire avant tout capital réel
- Kill-switches respectés
- Si live ratio <0.3 du paper → STOP, pas de wishful thinking
- Capacity hard cap ~$250-500k AUM, pas plus

## Why (motivation)

Paul veut :
1. Construire un asset trading scalable (à long terme)
2. Apprendre la mécanique des prediction markets + options hedging
3. Optionnalité de revenus récurrents trading
4. Storytelling Twitter (build in public)

Cette stratégie offre :
- Math rigoureuse hedge-fund-grade
- Downside limité ($500-700 max loss réaliste)
- Upside scalable (jusqu'à $50-200k/an récurrent à plafond)
- Skill transferable

## How to apply

1. Build Phase 1 immédiatement (jour 1-2)
2. Strict respect des Go/No-Go criteria à chaque phase
3. Pas de scaling au-dessus du plafond capacity
4. Reporting quotidien dans vault sessions
5. Si Phase 4 (paper) Sharpe <1 → STOP avant live capital

## Related

- [[brantham/polymarket/crypto-deribit-arb/_MOC]]
- [[brantham/polymarket/crypto-deribit-arb/architecture]]
- [[brantham/polymarket/crypto-deribit-arb/math-pricing-hedge]]
- [[brantham/polymarket/crypto-deribit-arb/risks-mitigation]]
- [[brantham/polymarket/crypto-deribit-arb/roadmap]]
- [[brantham/polymarket/_MOC]]
- [[_system/MOC-decisions]]
