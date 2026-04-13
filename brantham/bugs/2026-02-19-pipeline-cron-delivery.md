---
type: bug-fix
project: brantham
date: 2026-02-19
component: pipeline
severity: medium
tags: [pipeline, cron, agents]
---

# Cron Writer/Hunter delivery error

## Symptom
Writer and Hunter cron jobs failing with 'cron delivery' error.

## Root Cause
Cron mode was trying to deliver messages through messaging platform.

## Fix
Use mode 'silent' for cron executions.

## Prevention
Always use silent mode for agent cron tasks.

## Related
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[brantham/bugs/2026-02-19-scraper-abitbol-mailto]]
- [[brantham/bugs/2026-02-19-llm-glm47-content-null]]
- [[brantham/bugs/2026-02-19-scraper-gemweb-false-positives]]
- [[patterns/agent-orchestration]]
- [[patterns/prefect-pipeline]]
- [[brantham/patterns/scoring-patterns]]
