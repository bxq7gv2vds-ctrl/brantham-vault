---
type: pattern
created: 2026-03-17
project: mirofish-world-sim
tags: [agents, vectorization, anti-herding, memory, explainability]
---

# Pattern: Agent Decision Quality — Anti-Herding + Memory + Explainability

## Contexte

Simulateur multi-agents (6884 agents, vectorise numpy). Les agents rule-based prenaient des decisions differenciees (scoring multi-criteres) mais:
1. Raisons opaques (`vec_bid_0.713`)
2. Herding massif (argmax → tous sur le meme deal)
3. Stateless (re-bid infini sur le meme deal)
4. Conseillers = spam aveugle

## Solution implementee

### 1. Raisons enrichies
Stocker les scores composants dans `conditions` + `reason`:
```
reason: "sec=0.94 tic=0.05 geo=0.00 cmp=1.00 tim=0.90"
conditions: {score: 0.58, sector: 0.94, ticket: 0.05, geo: 0.0, competition: 1.0, timing: 0.9}
```

### 2. Anti-herding (top-K weighted)
Remplacer `np.argmax(total, axis=1)` par selection ponderee dans le top-3:
```python
top_k_idx = np.argpartition(-total, K, axis=1)[:, :K]
top_k_scores = np.take_along_axis(total, top_k_idx, axis=1)
exp_s = np.exp(np.clip(top_k_scores * 5.0, -50, 50))  # temperature=5
weights = exp_s / exp_s.sum(axis=1, keepdims=True)
cum_w = np.cumsum(weights, axis=1)
rand_vals = rng.random(n_agents)
chosen_k = np.argmax(cum_w >= rand_vals[:, np.newaxis], axis=1)
```
Resultat: 622 deals uniques/round au lieu d'une poignee.

### 3. Memory masking
Passer `agent_history` (dict[agent_id, list[last_5_actions]]) au batch_decide. Penaliser les deals deja vus:
- Deja bid → score * 0.2
- Withdraw → score * 0.1
- Watch/DD → score * 0.7
Resultat: 11.5% re-bids (vs 100% avant).

### 4. Conseillers conditionnels
`_decide_conseiller()` filtre `watchers < 10` avant de share_info.

## Performance

Aucun impact mesurable: 3.2s pour 50 rounds (vs 3.0s avant). La cle:
- Memory masking: O(n_agents * 5) avec lookup dict deal_id_to_idx
- Anti-herding: numpy vectorise (cumsum + argmax), zero Python loop
- Pre-filtrage institutional: conseillers recoivent seulement early-phase deals

## Fichiers

- `backend/ma/engine/vectorized.py` — anti-herding, memory masking, enriched reasons
- `backend/ma/agents/rule_based.py` — conseiller conditionnel
- `backend/ma/engine/simulation.py` — passage de agent_history a batch_decide
