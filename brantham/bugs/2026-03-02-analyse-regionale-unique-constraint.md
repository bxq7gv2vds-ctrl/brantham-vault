---
type: bug-fix
project: brantham
date: 2026-03-02
component: data-pipeline
severity: medium
tags: [database, schema]
---

# analyse_regionale UNIQUE constraint on wrong column

## Symptom
Duplicate entries in analyse_regionale.

## Root Cause
UNIQUE constraint was on departement alone, should be on (departement, region).

## Fix
Changed UNIQUE constraint to (departement, region).

## Related
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[brantham/bugs/2026-03-02-matrice-aj-secteur-taux-cession]]
