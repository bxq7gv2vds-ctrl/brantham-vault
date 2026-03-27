---
type: pattern
project: cross-project
date: 2026-03-05
category: data
tags: [asyncpg, database, async, python]
---

# asyncpg Connection Pool Pattern

## Problem
Concurrent async database operations fail with "another operation in progress" when sharing a single connection.

## Solution
Always use connection pools:
```python
pool = await asyncpg.create_pool(
    dsn=DATABASE_URL,
    min_size=2,
    max_size=8
)
async with pool.acquire() as conn:
    result = await conn.fetch(query)
```

## When to Use
Any async Python code accessing PostgreSQL concurrently (asyncio.gather, multiple coroutines).

## Gotchas
- Don't forget to close the pool on shutdown
- Set max_size based on expected concurrent connections
- Each acquired connection must be released (use async with)

## Origin
Discovered fixing [[brantham/bugs/2026-03-05-asyncpg-another-operation]].

## Related
- [[_system/MOC-patterns]]
- [[brantham/bugs/2026-03-05-asyncpg-another-operation]]
