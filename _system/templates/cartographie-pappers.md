---
type: cartographie
nom_groupe:
siren_tete:
nb_entites:
ca_consolide:
effectif_consolide:
secteurs: []
regions: []
dirigeant_cle:
date_fetch_pappers:
tags: []
---

# Cartographie: {{nom_groupe}}

> Cartographie groupe enrichie via Pappers. Derniere maj: {{date_fetch_pappers}}.

## Tete de Groupe

[[brantham/pappers/entreprises/{{siren_tete}}-{{slug}}]]

| Champ | Valeur |
|-------|--------|
| Denomination | |
| SIREN | {{siren_tete}} |
| Forme | |
| Capital | |

## Organigramme

<!-- Arbre hierarchique des entites -->

```
{{nom_groupe}} ({{siren_tete}})
  |-- Filiale 1 (SIREN) — 100%
  |   |-- Sous-filiale A (SIREN) — 60%
  |-- Filiale 2 (SIREN) — 51%
  |-- Participation (SIREN) — 30%
```

## Entites du Groupe

| Denomination | SIREN | Relation | % Detention | CA | Statut | Lien |
|-------------|-------|----------|-------------|-----|--------|------|
| | | Filiale | | | Active | [[brantham/pappers/entreprises/]] |

## Dirigeants Communs

<!-- Personnes avec mandats dans plusieurs entites du groupe -->

| Dirigeant | Mandats | Entites | Lien |
|-----------|---------|---------|------|
| | | | [[brantham/pappers/dirigeants/]] |

## Secteurs du Groupe

| Code NAF | Libelle | Nb entites | CA cumule | Lien |
|----------|---------|-----------|-----------|------|
| | | | | [[brantham/pappers/secteurs/]] |

## Implantation Geographique

| Region | Departement | Nb etablissements | Effectif |
|--------|-------------|-------------------|----------|
| | | | |

## Consolidation Financiere

| Metrique | Valeur | Annee |
|----------|--------|-------|
| CA consolide estime | {{ca_consolide}} | |
| Effectif total | {{effectif_consolide}} | |
| Nb entites actives | | |
| Nb entites en procedure | | |

## Pertinence Brantham

<!-- Ce groupe est-il repreneur potentiel? Cible? Les deux? -->

- Type: repreneur | cible | ecosysteme
- Appetit M&A:
- Capacite financiere:
- Secteurs cibles:

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/pappers/entreprises/{{siren_tete}}-{{slug}}]]
