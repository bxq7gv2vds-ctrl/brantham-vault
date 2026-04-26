---
date: 2026-04-26
project: brantham
tags: [bug, postgres, sql, fixed]
severity: medium
---

# Bug : `HAVING n` avec alias marche en SQLite, pas en Postgres

## Symptôme
Crash sur `cockpit.suggestions.generate_suggestions()` en mode Postgres :
```
psycopg.errors.UndefinedColumn: column "n" does not exist
LINE 1: ... GROUP BY source_aj HAVING n >= 5
                                                                 ^
```

## Cause racine
SQL :
```sql
SELECT source_aj, MAX(last_seen_at) as last, COUNT(*) as n
FROM opportunities
GROUP BY source_aj
HAVING n >= 5
```

- **SQLite** : autorise les alias dans `HAVING` (extension non standard)
- **Postgres** : standard SQL strict — `HAVING` doit utiliser l'**expression** complète, pas l'alias

## Fix
```sql
HAVING COUNT(*) >= 5
```

Au lieu de `HAVING n >= 5`.

## Leçon générale
Différences SQLite vs Postgres à connaître :
- ❌ Alias dans HAVING (Postgres refuse)
- ❌ Alias dans WHERE (les deux refusent — pareil)
- ✅ Alias dans ORDER BY (les deux acceptent)
- ❌ `date('now')` (SQLite-only) → utiliser param Python
- ❌ `AUTOINCREMENT` (SQLite) → `BIGSERIAL` (Postgres)
- ⚠ `IF NOT EXISTS` sur `CREATE INDEX` : OK partout
- ⚠ Boolean `0/1` : Postgres veut `false/true`

## Where
- Fichier : `/Users/paul/Downloads/brantham-pipeline/cockpit/suggestions.py`
- Ligne ~236 (catégorie veille — silent breakage)

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/patterns/db-abstraction-sqlite-postgres-hybridrow]]
- [[brantham/bugs/2026-04-26-hybridrow-iter-postgres]]
- [[brantham/_MOC]]
- [[_system/MOC-bugs]]
