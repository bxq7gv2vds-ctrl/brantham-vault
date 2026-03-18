---
type: decision
project: brantham/mirofish
date: 2026-03-18
status: implemented
---

# Decision: MiroFish v0.3 Distilled Architecture

## Contexte

MiroFish devait scaler de 7K a 1M agents avec des decisions de qualite LLM. Plusieurs approches possibles.

## Alternatives considerees

1. **LLM direct sur 1M agents** — Impossible: 1M appels LLM/round
2. **Rule-based pure avec multiplier** — Rapide mais decisions pauvres
3. **Knowledge distillation MLP** — Choisi: entraine sur LLM, inference MLX batch

## Decisions architecturales

### 1. Buyer-only amplification
Les agents institutionnels (tribunal, banque, mandataire, conseiller) ne sont PAS clones lors du multiplier. Seuls les buyers (repreneur, PE, family office, serial acquirer) sont amplifies.
**Raison**: Les institutional ont des Python loops sur 10K+ deals chacun. 155K clones = 20s/round juste pour eux.

### 2. Direct env mutation (pas d'AgentAction)
En mode distille, `_distilled_agent_round()` mute directement `self.env` au lieu de retourner des `AgentAction` objects.
**Raison**: Creer 937K objets Python par round = 140s. Direct mutation = 0.

### 3. Deal-level aggregation
Les bids sont agreges par deal (numpy bincount/unique) plutot que crees par agent.
**Raison**: 900K Bid objects → ~600 (2 par deal actif).

### 4. Geo group pre-computation
Les preferences geo des agents sont groupees en clusters uniques. Score matrix calculee par groupe, pas par agent.
**Raison**: 1M agents mais seulement ~50 groupes geo uniques.

## Resultat

995K agents x 100 rounds = 83.4s (0.83s/round). Target etait < 180s. **2x mieux que le target.**
