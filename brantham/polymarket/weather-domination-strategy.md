---
name: Weather Domination Strategy — 100% Polymarket weather focus
description: Décision stratégique 2026-04-20 — pas de diversification vers crypto/sports. Devenir la référence absolue weather Polymarket, accepter la capacity cap naturelle, scaler via leverage sur le même edge.
type: strategy
created: 2026-04-20
updated: 2026-04-20
priority: critical
tags: [polymarket, strategy, weather, domination, focus]
---

# Weather Domination — la décision

**Choix** : on reste **100% weather Polymarket**. Pas de crypto brackets. Pas de sports. Pas de politics.

## Pourquoi ce focus

### Notre edge réel est weather

Validé empiriquement :
- 12 sources NWP agrégées via BMA per-station (47 × 12 = 564 params)
- 46 per-station XGB residual (RMSE val 0.2-1.8°C)
- 15 per-city isotonic calibrators (Bonferroni-robust 21/21)
- Tail filter + vol filter + session filter empiriques
- WR 82-88%, DSR prob_real = 1.0
- 19 hypothèses testées, 12 closed, N_trials correct

### Sur tout autre vertical on n'a rien

- **Crypto** : GBM + realized vol = baseline que TOUS les options desks + HFT market makers utilisent. Zero edge vs pros.
- **Sports** : bookmakers ont 20+ ans historique + Elo internal data. Zero edge vs eux.
- **Politics** : polling firms + prediction market HFT déjà saturated.

Ajouter ces verticals diluerait le capital **sans alpha**. Perte garantie.

## La bonne question : comment dominer la niche weather

### Capacity naturelle Polymarket weather

- Volume daily ~$1-50k par market × ~370 markets actifs = **$100k-$5M total weather**
- Notre capacity max (edge retention ≥ 50%) ≈ **$50-100k bankroll**
- Au-delà : market impact + liquidity constraints

### Leviers pour scaler SANS diluer

| Levier | Principe | Capacity unlock |
|---|---|---|
| **1. Market-making thin weather markets** | Notre forecast skew les quotes bilatérales sur Seoul/Moscow/Lucknow/Taipei/Chongqing/Helsinki (no MM competition) | $50k → $500k capacity sur weather |
| **2. Kalshi cross-venue weather** | Arbitrage pur entre Polymarket et Kalshi weather markets (même edge forecast) | $50-100k additionnel |
| **3. LP hedge fund weather-focused** | Notre track record weather → 3-10 LP HNWI crypto-native | AUM $500k-5M |
| **4. Weather API SaaS** | Wrap notre pipeline forecast en API → $99-999/mo × clients | $50-500k/an MRR décorélé |
| **5. Academic paper + consulting** | "Multi-source NWP ensemble calibration on prediction markets" | Credibility + $50-200k/an consulting |

**Tout utilise le même weather edge**. Aucune dilution.

### Ce qu'on NE fait pas (explicit)

- ❌ Crypto brackets Polymarket
- ❌ Sports brackets
- ❌ Elections / politics
- ❌ Pure arbitrage sans model edge
- ❌ HFT latency race (colocation race perdue d'avance)

### Ce qu'on explore éventuellement (weather-adjacent seulement)

- 🟡 **ERCOT day-ahead electricity** — notre weather forecast est INPUT CRITIQUE pour peak demand. Extension naturelle du même edge vers autre venue. Capacity $1-10M institutional.
- 🟡 **CME Weather futures (HDD/CDD)** — même logique.
- 🟡 **Parametric cat bonds** — weather extrêmes triggers. Institutional only.

Ces items utilisent **notre output weather** comme alpha, pas un nouveau model.

## Plan d'exécution weather-only

### Phase 1 — Max out Polymarket weather capacity (Mois 0-3)
- Wallet wire → $1k real trading
- Compound $1k → $50k via weather MODEL_VS_MARKET + CONFIRMED_NO
- Bandit allocator + decay monitor + DD bands (tous fait)
- Kelly 0.40 + portfolio Kelly opt-in validation

### Phase 2 — Market-making weather thin markets (Mois 2-5)
- Activate MM sur Seoul, Moscow, Lucknow, Taipei, Chongqing, Helsinki
- Inventory management + cancel-replace loop
- Capacity 10× sur ces markets spécifiques

### Phase 3 — Cross-venue Kalshi weather (Mois 3-6)
- KYC Kalshi, API credentials
- Arbitrage detector live (skeleton exists)
- Capacity +$50-100k weather

### Phase 4 — Weather API SaaS launch (Mois 5-9)
- FastAPI wrapper forecast service
- Target crypto mining farms, insurance, energy traders
- $5-50k MRR

### Phase 5 — LP weather-focused (Mois 9-15)
- Track record 12 mois validé
- Academic paper published
- 3-10 LP HNWI crypto-native → $500k-5M AUM
- 2% + 20% fees

### Phase 6 — ERCOT / CME si justifiable (Mois 15-24)
- Seulement si weather edge prouvé multi-year
- Institutional infrastructure required
- Carrier potential $1-50M capacity

## Success metrics

**Pas "comment atteindre $1M"**. Plutôt :

- **Devenir #1 weather hedge fund Polymarket** (position compétitive)
- **Extraire le maximum du volume weather disponible** sans dilution
- **Track record propre** → credibility pour scale via LP ou SaaS
- **Ne jamais perdre d'argent sur un vertical où on n'a pas d'edge**

## Révision trimestrielle

Chaque 3 mois, re-évaluer :
1. Est-ce qu'on a atteint capacity naturelle ? (si oui, activer next levier)
2. Est-ce que l'edge tient ? (bandit + decay monitor surveillent)
3. Est-ce que la compétition arrive ? (monitor orderbook patterns)
4. Est-ce qu'un nouveau vertical **weather-adjacent** émerge ? (ERCOT expansion, cat bonds, etc.)

Jamais de pivot émotionnel vers crypto/sports. Discipline stratégique = notre moat.

## Related

- [[g1-g2-qualification-kit|G1→G2 Framework]]
- [[hedge-fund-rigor-upgrade|Rigor upgrade]]
- [[sessions/2026-04-20-meta-optimization|Meta-optimization session]]
- [[STATE-HANDOFF]]
- [[_MOC|Polymarket MOC]]
