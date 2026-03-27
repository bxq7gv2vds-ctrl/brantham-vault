---
type: pattern
project: brantham/mirofish
created: 2026-03-18
tags: [mlx, distillation, scaling, performance]
---

# Pattern: Knowledge Distillation for Agent Scaling

## Probleme

Simuler 1M+ agents avec des decisions de qualite LLM. LLM direct = impossible (1M calls/round). Rule-based = pas assez riche.

## Solution

1. **Teacher**: Qwen2.5-7B via MLX genere des decisions sur ~100K scenarios
2. **Student**: MLP 3-couches (31→64→32→4+1) entraine en distillation
   - Loss: 0.7 * KL_divergence(soft_targets) + 0.3 * CE(hard_labels) + 0.1 * MSE(amounts)
   - 4293 params, 17.2KB, accuracy 83.9%
3. **Inference**: MLX batch 1M en 0.117s (GPU Apple Silicon)

## Architecture MLP

```
Input (31 features) → Linear(64) → BatchNorm → ReLU
                     → Linear(32) → ReLU
                     → Classification head (4 actions: BID/WATCH/DD/PASS)
                     → Regression head (bid amount)
```

## Features (31 total)

- Agent (14): budget, risk_tolerance, reputation, threshold, ticket range, portfolio, type one-hot, has_geo
- Deal (13): ca, bids, watchers, passif, actifs, phase, sector affinity, geo match, competition, info tier, age, deadline proximity, already interacted
- Market (4): interest rate, friction, capital normalized, round normalized

## Resultats

| Scale | Time | Per round |
|-------|------|-----------|
| 7K agents (baseline) | 3.3s/50r | 66ms |
| 995K agents (distilled) | 83.4s/100r | 834ms |
| 1M MLX inference only | 0.117s | - |

## Quand utiliser

- Agent count > 50K
- Decisions doivent refleter la qualite LLM
- Temps reel ou near-real-time requis
- Hardware Apple Silicon disponible

## Limites

- Accuracy plafonne a ~84% (small model)
- Pas de raisonnement emergent (frozen decisions)
- Auto-retrain necessaire si les regles du monde changent

## Related
- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[brantham/bugs/2026-03-06-agent-auth-401]]
- [[brantham/sessions/2026-03-18]]
