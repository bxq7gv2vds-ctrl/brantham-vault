---
type: pattern
project: brantham
date: 2026-03-12
category: agent
tags: [agents, orchestration, multi-agent]
---

# Agent Orchestration Pattern

## Problem
Multiple specialized agents need to collaborate on complex workflows without stepping on each other.

## Solution
Director pattern:
1. Director reads shared state (BRAIN.md)
2. Director assigns tasks to specialized agents
3. Each agent has isolated workspace but reads shared memory
4. QC gate after each agent (score threshold 6-7/10)
5. If below threshold -> re-assign with specific feedback
6. Parallelization: Writer + Hunter run concurrently, Enricher waits for Hunter

Rules:
- Max 2 analyses simultaneous
- Max 3 active deals
- LJ priority over RJ/SV
- Heartbeat protocol: agent reads WORKING.md -> checks PIPELINE.md -> acts or reports HEARTBEAT_OK

## When to Use
Multi-step pipelines where quality gates matter.

## Gotchas
- Agents cannot access each other's workspaces directly
- Shared memory (BRAIN.md) must be atomic writes
- sendCommand must be awaited (async)
- Auth: copy auth-profiles.json, use anthropic-beta header

## Related
- [[_system/MOC-patterns]]
- [[patterns/gemweb-rss-parsing]]
- [[patterns/teaser-pptx-generation]]
- [[patterns/prefect-pipeline]]
- [[patterns/scraping-robust]]
- [[brantham/patterns/scoring-patterns]]
- [[brantham/patterns/teaser-patterns]]
- [[brantham/patterns/acheteur-mapping]]
- [[founder/journal/2026-03-12]]
- [[founder/decisions/2026-03-12-unified-vault]]
- [[brantham/bugs/2026-03-02-analyse-regionale-unique-constraint]]
- [[brantham/bugs/2026-02-19-pipeline-cron-delivery]]
- [[brantham/bugs/2026-03-06-agent-auth-401]]
- [[brantham/bugs/2026-03-06-sendcommand-not-awaited]]
