# Triage Labels

Les skills mattpocock parlent en termes de cinq rôles canoniques. Comme on est en local-markdown (pas GitHub), ces "labels" sont stockés dans le frontmatter `status:` de chaque fichier issue.

| Rôle canonique     | Valeur `status:` dans le frontmatter | Sens                                                 |
| ------------------ | ------------------------------------ | ---------------------------------------------------- |
| `needs-triage`     | `needs-triage`                       | Maintainer doit évaluer cette issue                  |
| `needs-info`       | `needs-info`                         | Attente d'info du reporter                           |
| `ready-for-agent`  | `ready-for-agent`                    | Spécifiée complètement, prête pour un agent AFK     |
| `ready-for-human`  | `ready-for-human`                    | Nécessite implémentation humaine                    |
| `wontfix`          | `wontfix`                            | Ne sera pas traitée                                 |

Statut additionnel custom : `done` (issue close, gardée pour archive).

## Comment changer le statut

Modifier la ligne `status:` dans le frontmatter du fichier issue. Mettre à jour `updated: YYYY-MM-DD`.

## Filtrage rapide

```bash
# Issues ready-for-agent dans le vault
grep -lr "^status: ready-for-agent" /Users/paul/vault/issues/

# Toutes issues d'un projet
grep -lr "^project: brantham" /Users/paul/vault/issues/
```

Ou via QMD : `qmd query "ready-for-agent" --collection vault`

## Related

- [[_system/agents/issue-tracker]]
- [[_system/agents/domain]]
