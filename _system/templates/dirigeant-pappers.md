---
type: dirigeant
nom:
prenom:
date_naissance:
nationalite:
slug:
siren_personnel: # si societe personnelle
mandats_actifs: 0
mandats_total: 0
est_ppe: false # personne politiquement exposee
sanctions: false
tags: []
date_fetch_pappers:
---

# {{prenom}} {{nom}}

> Profil dirigeant enrichi via Pappers. Derniere maj: {{date_fetch_pappers}}.

## Identite

| Champ | Valeur |
|-------|--------|
| Nom | {{nom}} |
| Prenom | {{prenom}} |
| Date naissance | {{date_naissance}} |
| Nationalite | {{nationalite}} |
| SIREN personnel | {{siren_personnel}} |

## Mandats Actifs

<!-- Wikilinks vers les fiches entreprise -->

| Entreprise | SIREN | Qualite | Depuis | Lien |
|-----------|-------|---------|--------|------|
| | | | | [[brantham/pappers/entreprises/]] |

## Mandats Historiques

| Entreprise | SIREN | Qualite | Periode | Lien |
|-----------|-------|---------|---------|------|
| | | | | |

## Reseau

<!-- Dirigeants partageant des mandats communs -->

| Dirigeant | Entreprises communes | Lien |
|-----------|---------------------|------|
| | | [[brantham/pappers/dirigeants/]] |

## Conformite

| Check | Resultat | Date |
|-------|----------|------|
| PPE (Pappers) | {{est_ppe}} | {{date_fetch_pappers}} |
| Sanctions internationales | {{sanctions}} | {{date_fetch_pappers}} |

## Pertinence Brantham

<!-- Ce dirigeant est-il repreneur potentiel? Mandataire judiciaire? Concurrent? -->

- Role dans l'ecosysteme:
- Historique M&A:
- Contact:

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
