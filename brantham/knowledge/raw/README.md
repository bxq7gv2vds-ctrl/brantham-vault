---
type: readme
project: brantham
updated: 2026-04-03
---

# Raw Sources — Brantham Knowledge

Ce répertoire contient les **sources primaires brutes** : articles, papers, jurisprudence, rapports, extraits BODACC, notes terrain. Les fichiers ici ne sont pas des notes finales — ce sont des matériaux à compiler.

## Convention de nommage

```
YYYY-MM-DD-[source]-[slug].md
```

Exemples :
- `2026-04-03-legifrance-liquidation-judiciaire-art-L640.md`
- `2026-03-28-lemonde-distressed-pme-2025.md`
- `2026-04-01-mandataire-entretien-jean-dupont.md`

## Frontmatter obligatoire

```yaml
---
type: raw-source
source_type: article | paper | jurisprudence | rapport | entretien | BODACC | autre
url: <url si applicable>
title: <titre original>
author: <auteur ou publication>
date_published: YYYY-MM-DD
date_ingested: YYYY-MM-DD
compiled_into: []  # Liste des concepts qui ont ingéré ce fichier
project: brantham
---
```

## Règle de compilation

Un fichier `raw/` doit être compilé dans au moins un fichier `concepts/`. Une fois compilé, ajouter le path du concept dans `compiled_into:`. Cela permet de savoir quelles sources restent non compilées (= whitespot potentiel).

## Related

- [[brantham/knowledge/_knowledge-map]]
- [[brantham/_MOC]]
