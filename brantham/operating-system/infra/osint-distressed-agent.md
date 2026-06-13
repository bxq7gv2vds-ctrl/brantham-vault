---
type: infra
system: brantham-osint-agent
status: v0-working-offline
updated: 2026-06-03
---

# OSINT Distressed Agent

## Objectif

Transformer une annonce brute de procédure collective en dossier Brantham exploitable:

```text
annonce -> cible -> SIREN -> procédure -> corporate -> finances -> actifs
-> diagnostic -> thèses de reprise -> repreneurs -> scoring -> outreach -> QC -> rapport
```

## Repo local

```text
/Users/paul/Desktop/brantham-agent
```

## Commandes validées

```bash
cd /Users/paul/Desktop/brantham-agent
.venv/bin/python -m compileall agent tests
.venv/bin/python -m pytest -q
.venv/bin/python -m agent.main run --offline --text "Plan de cession - ..."
```

Dernière vérification: `47 passed`.

## Workflow LangGraph

1. `extract_announcement`
2. `resolve_entity`
3. `fetch_procedure`
4. `corporate_research`
5. `extract_financials`
6. `reconstruct_business`
7. `analyze_assets`
8. `diagnose_distress`
9. `generate_theses`
10. `map_acquirers`
11. `score_acquirers`
12. `generate_outreach`
13. `red_team_qc`
14. `generate_report`

## Emplacements Vault

| Usage | Emplacement |
|---|---|
| Deals actifs | `deals/active/<deal>/` |
| Infra / protocoles / continuité | `operating-system/` |
| Patterns réutilisables | `patterns/` |
| Knowledge evergreen | `knowledge/` |
| Sessions datées | `sessions/` |

## Limites actuelles

- PostgreSQL `brantham` n’était pas joignable sur `localhost:5432` lors du run Gesler.
- Le mode complet DB + Ollama doit être testé sur une opportunité réelle.
- Le mapping repreneurs doit intégrer officiellement les listes DGAL abattage/découpe.
- Il manque un export CSV natif pour les cibles LinkedIn.

## Prochaines corrections prioritaires

1. Réparer l’accès Postgres local ou documenter le DSN réel.
2. Ajouter une table `leader_contact_targets`.
3. Ajouter un score sectoriel viande:
   - espèce,
   - agrément sanitaire,
   - distance routière,
   - filière éleveurs,
   - capacité froid,
   - réseau distribution.
4. Ajouter export CSV deal -> repreneurs -> dirigeants -> requêtes LinkedIn.
## Related
## Related
## Related
## Related
## Related
