# Issues — MOC

Index des features / issues / PRDs en local-markdown. Remplace GitHub Issues, Linear, Jira.

## Convention

- Une feature = un dossier `<feature-slug>/`
- Chaque dossier contient un `PRD.md` et des fichiers d'issue numérotés `01-<slug>.md`, `02-<slug>.md`, ...
- Statut dans le frontmatter : `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`, `done`

## Features actives

_(vide pour le moment — sera rempli au fur et à mesure)_

## Recherche

```bash
# Issues prêtes pour un agent
grep -lr "^status: ready-for-agent" /Users/paul/vault/issues/

# Issues d'un projet
grep -lr "^project: brantham" /Users/paul/vault/issues/
```

Ou : `qmd query "<sujet>" --collection vault`

## Related

- [[_system/agents/issue-tracker]]
- [[_system/agents/triage-labels]]
- [[_system/MOC-master]]
