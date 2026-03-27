---
type: decision
project: cross-project
date: 2026-03-12
status: active
tags: [infrastructure, memory, vault]
alternatives_considered: [hermes-agent, qdrant-vector-db, keep-fragmented]
linked_assumptions: []
review_at: 2026-04-12
---

# Unified Obsidian Vault over Hermes Agent or Vector DB

## Context
Had 11 fragmented MEMORY.md files, empty founder vault, scattered project files. Considered Hermes Agent (NousResearch) and Qdrant vector DB as alternatives.

## Alternatives
1. **Hermes Agent** -- Standalone CLI agent with memory. Rejected: separate system from Claude Code, memory wouldn't transfer, duplicate infrastructure.
2. **Qdrant on VPS** -- Vector DB for semantic search. Deferred: over-engineering at current scale, can add later on top of markdown vault.
3. **Unified Obsidian Vault** -- Single ~/vault/ with structured markdown, read/written natively by Claude Code. Chosen.

## Decision
Build a unified Obsidian vault at ~/vault/ with structured directories, templates, MOCs, and automation via Claude Code directives. All projects write to one vault. Cross-project search via grep/links.

## Consequences
- Single source of truth for all knowledge
- No new infrastructure to maintain
- Claude Code reads/writes natively
- Obsidian graph view shows connections
- Can add vector DB later as overlay

## Related
- [[_system/MOC-decisions]]
- [[_system/MOC-master]]
- [[patterns/agent-orchestration]]
- [[patterns/gemweb-rss-parsing]]
- [[patterns/teaser-pptx-generation]]
- [[patterns/prefect-pipeline]]
- [[patterns/scraping-robust]]
- [[brantham/patterns/scoring-patterns]]
- [[brantham/patterns/teaser-patterns]]
- [[brantham/patterns/acheteur-mapping]]
- [[founder/journal/2026-03-12]]
- [[founder/strategy/current-strategy]]
