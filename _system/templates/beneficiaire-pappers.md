---
type: beneficiaire_effectif
nom:
prenom:
date_naissance:
nationalite:
nb_participations:
est_ppe: false
sanctions: false
tags: []
date_fetch_pappers:
---

# {{prenom}} {{nom}} (Beneficiaire Effectif)

> Profil beneficiaire effectif enrichi via Pappers. Derniere maj: {{date_fetch_pappers}}.

## Identite

| Champ | Valeur |
|-------|--------|
| Nom | {{nom}} |
| Prenom | {{prenom}} |
| Date naissance | {{date_naissance}} |
| Nationalite | {{nationalite}} |

## Participations

<!-- Wikilinks vers les fiches entreprise -->

| Entreprise | SIREN | % Detention | Modalite controle | Lien |
|-----------|-------|-------------|-------------------|------|
| | | | | [[brantham/pappers/entreprises/]] |

## Conformite

| Check | Resultat | Date |
|-------|----------|------|
| PPE | {{est_ppe}} | {{date_fetch_pappers}} |
| Sanctions | {{sanctions}} | {{date_fetch_pappers}} |

## Reseau

<!-- Autres beneficiaires/dirigeants des memes entreprises -->

| Personne | Entreprises communes | Role | Lien |
|----------|---------------------|------|------|
| | | | [[brantham/pappers/dirigeants/]] |

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
