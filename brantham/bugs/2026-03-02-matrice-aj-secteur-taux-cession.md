---
type: bug-fix
project: brantham
date: 2026-03-02
component: data-pipeline
severity: high
tags: [analytics, scoring, data]
---

# matrice_aj_secteur taux_cession contained raw count instead of rate

## Symptom
taux_cession column in matrice_aj_secteur had nb_cessions raw count instead of rate.

## Root Cause
Missing division in the SQL calculation.

## Fix
`ROUND(nb_cessions::numeric / NULLIF(nb_total, 0), 4)` -- proper rate calculation.

## Prevention
Always validate analytical columns with sanity checks (rates should be 0-1, counts should be integers).

## Related
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[brantham/bugs/2026-03-02-analyse-regionale-unique-constraint]]
