# Pattern: Swarm Intelligence M&A (OASIS)

## Concept
Agents LLM locaux (qwen2.5:7b via llama-cpp-python) evaluent des deals M&A par consensus emergent. Chaque agent a un profil investisseur (type, fund size, sectors, thesis) et decide BID/WATCH/PASS/DD par round.

## Architecture
- **Engine**: `api/oasis_ma/` — module Python standalone
- **LLM**: llama-cpp-python + GGUF qwen2.5:7b (Metal sans bf16, ~8 tok/s)
- **Trace**: SQLite in-memory pour actions
- **API**: `/api/swarm/*` dans main.py (5 endpoints)
- **Frontend**: `/swarm` page dans internal-tool

## Key Decisions
- Ollama 0.18.0 crash sur M5/macOS Tahoe (Metal bfloat error) → llama-cpp-python comme workaround
- camel-oasis incompatible Python 3.14 → implementation custom du marketplace + runner
- Sequential agent execution (pas de parallelisme LLM) car llama.cpp single-threaded
- SQLite `check_same_thread=False` pour compatibilite asyncio + thread executor

## Files
```
api/oasis_ma/
├── __init__.py     # Exports
├── actions.py      # ActionType enum + AgentAction dataclass
├── agents.py       # 27 archetypes + real buyer profile generation
├── platform.py     # DealMarketplacePlatform (bids/watches/passes/dd)
├── prompts.py      # System + round prompts for agents
└── runner.py       # SwarmRunner orchestration (rounds x agents)
```

## Performance
- 3 agents x 2 rounds x 3 deals: ~60s (model load ~2s, inference ~8s/agent/round)
- 25 agents x 12 rounds x 50 deals: estimé ~40 min (sequential)

## GGUF Model Path
`/Users/paul/.ollama/models/blobs/sha256-2bada8a7450677000f678be90653b85d364de7db25eb5ea54136ada5f3933730`

## Related
- [[brantham/_MOC]]
