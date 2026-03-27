---
type: bug-fix
project: brantham
date: 2026-03-06
component: agents
severity: high
tags: [agents, async, server]
---

# sendCommand not awaited in agent server

## Symptom
Agent commands silently failing, no response from agents.

## Root Cause
sendCommand() was async but call was not awaited.

## Fix
Add `await` to sendCommand() calls.

## Related
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[brantham/bugs/2026-03-06-agent-auth-401]]
- [[brantham/bugs/2026-03-06-handoff-raw-wrapper]]
- [[patterns/agent-orchestration]]
