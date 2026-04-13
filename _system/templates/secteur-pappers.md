---
type: secteur
code_naf:
libelle_naf:
secteur_brantham: # retail | btp | restaurant | manufacturing | tech | real_estate | agri_food | services | transport | sante | autre
nb_entreprises_actives:
nb_procedures_en_cours:
ca_median:
effectif_median:
taux_defaillance: # %
date_fetch_pappers:
tags: []
---

# Secteur: {{libelle_naf}} ({{code_naf}})

> Cartographie sectorielle enrichie via Pappers. Derniere maj: {{date_fetch_pappers}}.

## Vue d'Ensemble

| Metrique | Valeur | Date |
|----------|--------|------|
| Code NAF | {{code_naf}} |  |
| Entreprises actives | {{nb_entreprises_actives}} | {{date_fetch_pappers}} |
| Procedures en cours | {{nb_procedures_en_cours}} | {{date_fetch_pappers}} |
| CA median | {{ca_median}} EUR | |
| Effectif median | {{effectif_median}} | |
| Taux defaillance | {{taux_defaillance}}% | |

## Top Entreprises du Secteur

<!-- Les plus grosses par CA. Wikilinks vers fiches entreprise. -->

| Rang | Entreprise | SIREN | CA | Effectif | Lien |
|------|-----------|-------|-----|----------|------|
| 1 | | | | | [[brantham/pappers/entreprises/]] |

## Entreprises en Procedure

<!-- Toutes les entreprises du secteur en RJ/LJ/sauvegarde -->

| Entreprise | SIREN | Procedure | Date | CA | Lien |
|-----------|-------|-----------|------|-----|------|
| | | | | | [[brantham/pappers/entreprises/]] |

## Repreneurs Potentiels

<!-- Entreprises saines du secteur = cibles pour acheteurs strategiques -->

| Entreprise | SIREN | CA | Effectif | Historique M&A | Lien |
|-----------|-------|-----|----------|----------------|------|
| | | | | | [[brantham/pappers/entreprises/]] |

## Dynamique Sectorielle

### Tendances
-

### Signaux Faibles
-

### Risques Specifiques
-

## Playbook Brantham

<!-- Lien vers le playbook sectoriel existant si applicable -->

[[brantham/knowledge/sectors/{{secteur_brantham}}-playbook]]

## Benchmark Valorisation

| Metrique | Multiple median | Fourchette | Source |
|----------|----------------|-----------|--------|
| EV/CA | | | |
| EV/EBITDA | | | |
| EV/Effectif | | | |

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/knowledge/sectors/{{secteur_brantham}}-playbook]]
- [[_system/MOC-patterns]]
