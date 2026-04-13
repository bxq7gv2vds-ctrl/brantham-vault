---
type: bug-fix
project: brantham
date: 2026-03-05
component: data-pipeline
severity: critical
tags: [asyncpg, database, async]
---

# asyncpg "another operation in progress" with asyncio.gather

## Symptom
asyncpg.connect() + asyncio.gather() throwing "another operation in progress" error.

## Root Cause
Single connection shared across concurrent coroutines. asyncpg connections are not thread-safe for concurrent operations.

## Fix
Use `asyncpg.create_pool(min_size=2, max_size=8)` instead of single connection.

## Prevention
Always use connection pool for async database access. Never share a single connection across gather().

See [[patterns/asyncpg-connection-pool]] for the reusable pattern.

## Related
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[patterns/asyncpg-connection-pool]]
- [[patterns/prefect-pipeline]]
- [[brantham/patterns/teaser-onepager-html-pdf]]
