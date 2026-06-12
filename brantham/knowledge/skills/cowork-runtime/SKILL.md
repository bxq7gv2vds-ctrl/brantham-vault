---
type: skill
project: brantham
name: cowork-runtime
model_default: deepseek-v4-flash
---

# Skill: Cowork Runtime

## Quand l'utiliser

Utiliser cette skill pour orchestrer une mission interne multi-etapes avec delegation entre agents.

## Pattern standard

1. `router` comprend la demande.
2. `router` choisit skill + playbook.
3. `router` cree un plan court.
4. Sous-agents executent les blocs.
5. `qc` verifie si livrable important.
6. `router` assemble.
7. JSON cowork final est ecrit.

## Output JSON

Chemin :

```text
brantham/cowork-outputs/[agent]-[YYYY-MM-DD]-[HHMM].json
```

Schema :

```json
{
  "agent": "",
  "run_id": "",
  "timestamp": "",
  "status": "success | partial | error",
  "summary": "",
  "data": {},
  "actions_taken": [],
  "pending_for_human": [],
  "triggered_next": [],
  "errors": []
}
```

## Regles

- Un run sans output JSON est incomplet si la mission comporte plusieurs etapes.
- Les actions sensibles vont dans `pending_for_human`.
- Les erreurs de source, scraping ou fichier doivent etre explicites.
## Related
## Related
## Related
