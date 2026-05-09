# Issue tracker: Obsidian Vault (Local Markdown)

Issues, PRDs, et tickets vivent comme fichiers markdown dans le vault Obsidian unifié.

**Pas de GitHub Issues. Pas de Linear. Pas de Jira.** Tout reste local dans `/Users/paul/vault/`.

## Location

- Racine issues : `/Users/paul/vault/issues/`
- Une feature par dossier : `vault/issues/<feature-slug>/`
- PRD : `vault/issues/<feature-slug>/PRD.md`
- Issues d'implémentation : `vault/issues/<feature-slug>/<NN>-<slug>.md` (numérotées depuis `01`)
- Comments / conversation : append à la fin du fichier sous `## Comments`

## Frontmatter requis

Chaque fichier issue/PRD doit contenir :

```yaml
---
title: <titre court>
status: <needs-triage | needs-info | ready-for-agent | ready-for-human | wontfix | done>
project: <brantham | website | polymarket | writing | founder | other>
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Le statut remplace les labels GitHub. Voir `triage-labels.md` pour le vocabulaire.

## Wikilinks Obsidian (obligatoires)

Chaque issue/PRD doit contenir une section `## Related` en bas avec :

- Backlink vers le PRD parent : `[[issues/<feature-slug>/PRD]]`
- Backlink vers le projet MOC : `[[brantham/_MOC]]` ou `[[website/_MOC]]` etc.
- Cross-links vers décisions/bugs/patterns du vault liés
- Cross-links vers d'autres issues du même feature-slug

## Quand un skill dit "publish to the issue tracker"

Créer un nouveau fichier sous `vault/issues/<feature-slug>/`, en créant le dossier si besoin. Remplir le frontmatter complet. Ajouter `## Related` avec wikilinks.

Mettre à jour l'index `vault/issues/_MOC.md` (créé à la première issue) avec une ligne par feature.

## Quand un skill dit "fetch the relevant ticket"

Lire le fichier au chemin référencé. L'utilisateur passera normalement le chemin ou le slug directement.

Recherche transverse : `qmd query "<sujet>" --collection vault` cible aussi les issues.

## Pas de gh / pas de glab

Les skills ne doivent **jamais** appeler `gh issue create`, `gh issue list`, `glab`, ou autre CLI distant. Tout est local-markdown dans le vault.

## Related

- [[_system/agents/triage-labels]]
- [[_system/agents/domain]]
- [[_system/MOC-master]]
