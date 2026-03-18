---
type: pattern
project: brantham/mirofish
created: 2026-03-18
tags: [performance, numpy, python, anti-pattern]
---

# Pattern: Numpy Aggregation Over Object Creation

## Probleme

Python for-loop creant N objets (N > 100K) est le bottleneck #1 dans les simulations vectorisees. Meme si le calcul numpy est rapide, la materialisation en objets Python domine le runtime.

## Anti-pattern

```python
# 900K iterations, 900K Bid objects → 140s/round
for i in range(n_agents):
    if actions[i] == BID:
        deal.bids.append(Bid(agent_id=ids[i], amount=amounts[i], ...))
```

## Solution

Agreger en numpy, materialiser le minimum:

```python
# Aggregate per deal
bid_mask = (actions == BID)
deal_indices = deal_assignments[bid_mask]
amounts_bid = amounts[bid_mask]

# Best bid per deal
for di in np.unique(deal_indices):
    mask = deal_indices == di
    best_idx = np.argmax(amounts_bid[mask])
    deal.bids.append(Bid(...))  # 1 seul objet
    if mask.sum() > 1:
        deal.bids.append(Bid(agent_id="bulk", ...))  # placeholder
```

De 900K objets a ~600 (2 par deal actif).

## Gain mesure

| Approche | Objets/round | Temps/round (1M agents) |
|----------|-------------|------------------------|
| Per-agent loop | 937K | 144s |
| Per-deal aggregation | ~600 | 0.83s |

## Regle

Si N > 10K: ne jamais creer N objets Python. Agreger en numpy, materialiser seulement les O(deals) resultats.
