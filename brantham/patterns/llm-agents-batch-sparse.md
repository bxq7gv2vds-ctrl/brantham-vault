# Pattern: LLM Agents Batch + Sparse Rounds

## Contexte
MiroFish world simulator — 6884 agents M&A. Activer des agents LLM (MLX qwen2.5:7b-4bit) sans exploser le temps de simulation.

## Probleme
Sans optimisation: 5 LLM agents x 100 rounds x 20s/call = 10,000s = impossible.

## Solution
Deux optimisations combinees:

### 1. Sparse Rounds (`llm_call_interval`)
Les agents LLM ne consultent le LLM que tous les N rounds (defaut: 5). Entre deux, ils rejouent la derniere decision si le deal est encore actif. Si le deal a disparu, fallback rule-based.

### 2. Batch Calls (`llm_batch_size`)
Au lieu d'un appel MLX par agent, on batch N agents dans un seul prompt. Le system prompt decrit les N personas, le user prompt liste leurs deals respectifs (pre-filtres top 3 par score rule-based). La reponse est un JSON array.

### 3. Truncation-Tolerant JSON Parsing
La reponse LLM peut etre tronquee (token limit). Au lieu de `json.loads()` sur le JSON array entier, on utilise `re.finditer(r'\{[^{}]+\}', content)` pour extraire les objets JSON individuels. Resultat: 0% failure rate meme avec troncation.

### 4. Agent Name/ID Mapping
Le LLM retourne `agent_id` correspondant a `agent.name` (avec prefixe `LLM-`), mais le code interne utilise `agent.id` (sans prefixe). Un mapping `agent_name_to_id` resout ca dans `_parse_batch_response`.

### 5. Round Number Cloning
Les decisions cachees (replay entre les LLM rounds) doivent etre clonees avec le `round_num` actuel, pas celui du round original. Sinon toutes les replays montrent le meme round.

### Resultat
4 calls x ~12s = ~50s pour 5 LLM agents sur 20 rounds.
Extrapolation: 20 calls x ~12s = ~240s pour 250 rounds = acceptable.

## Fichiers
- `backend/ma/agents/llm_agent.py` — `batch_llm_decide()`, `_parse_batch_response()`, stats globales
- `backend/ma/engine/simulation.py` — `_llm_agent_round()`, `_batch_llm_round()`, `_replay_cached_decisions()`
- `backend/ma/models/config.py` — `llm_call_interval`, `llm_batch_size`, `llm_max_tokens`
- `backend/ma/api/router.py` — `agent_filter` param sur timeline endpoint
- `frontend/src/components/PaneView.vue` — filtre LLM toggle, cyan styling

## Config par defaut
```python
llm_call_interval: int = 5    # LLM decide tous les 5 rounds
llm_batch_size: int = 5       # batch 5 agents par appel MLX
llm_max_tokens: int = 250     # assez pour batch JSON (150 tronquait)
```

## Pieges connus
1. `max_tokens` trop bas = JSON tronque. Minimum 250 pour batch de 5 agents.
2. Le LLM peut retourner `agent.name` au lieu de `agent.id` — toujours mapper les deux.
3. Toujours cloner les AgentAction pour le replay, ne pas reutiliser la reference.

## Tags
#mirofish #llm #optimisation #batch #mlx #json-parsing
