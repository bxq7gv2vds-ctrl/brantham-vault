---
type: entreprise
siren:
siret_siege:
denomination:
nom_commercial:
forme_juridique:
categorie_juridique:
capital_social:
devise_capital: EUR
date_creation:
date_immatriculation_rcs:
date_radiation:
est_active: true
code_naf:
libelle_naf:
secteur_brantham:
convention_collective:
tranche_effectif:
effectif_exact:
ca_dernier: # EUR
resultat_net_dernier: # EUR
annee_derniers_comptes:
adresse_siege:
code_postal:
ville:
departement:
region:
pays: France
rcs:
greffe:
numero_tva:
est_entreprise_employeur:
score_brantham: # 0-100 scoring interne
tags: []
procedure_en_cours: # none | sauvegarde | rj | lj | mandat_ad_hoc | conciliation
date_fetch_pappers:
---

# {{denomination}} ({{siren}})

> Fiche entreprise enrichie via Pappers. Derniere maj: {{date_fetch_pappers}}.

## Identite

| Champ | Valeur |
|-------|--------|
| SIREN | {{siren}} |
| SIRET siege | {{siret_siege}} |
| Denomination | {{denomination}} |
| Nom commercial | {{nom_commercial}} |
| Forme juridique | {{forme_juridique}} |
| Capital social | {{capital_social}} EUR |
| Date creation | {{date_creation}} |
| Code NAF | {{code_naf}} — {{libelle_naf}} |
| Convention collective | {{convention_collective}} |
| TVA intra | {{numero_tva}} |

## Siege Social

{{adresse_siege}}, {{code_postal}} {{ville}}
Departement: {{departement}} | Region: {{region}}

## Dirigeants

<!-- Wikilinks vers vault/brantham/pappers/dirigeants/ -->

| Nom | Qualite | Date nomination | Lien |
|-----|---------|-----------------|------|
| | | | [[brantham/pappers/dirigeants/]] |

## Beneficiaires Effectifs

<!-- Wikilinks vers vault/brantham/pappers/beneficiaires/ -->

| Nom | Nationalite | % Detention | Modalite controle | Lien |
|-----|-------------|-------------|-------------------|------|
| | | | | [[brantham/pappers/beneficiaires/]] |

## Etablissements

| SIRET | Enseigne | Adresse | Effectif | Siege? |
|-------|----------|---------|----------|--------|
| {{siret_siege}} | | {{adresse_siege}} | | Oui |

## Donnees Financieres

<!-- Wikilinks vers vault/brantham/pappers/financials/ -->

| Annee | CA | Resultat Net | Effectif | Lien |
|-------|-----|-------------|----------|------|
| | | | | [[brantham/pappers/financials/]] |

### Trajectoire

<!-- Evolution CA/RN/effectif sur 3-5 ans. Signaux d'alerte. -->

## Procedures Collectives

<!-- Wikilinks vers vault/brantham/pappers/procedures-collectives/ -->

| Date | Type | Tribunal | Statut | Lien |
|------|------|----------|--------|------|
| | | | | [[brantham/pappers/procedures-collectives/]] |

## Publications BODACC

<!-- Immatriculations, modifications, radiations, ventes -->

| Date | Type | Resume |
|------|------|--------|
| | | |

## Actes Deposes

<!-- Statuts, PV AG, rapports -->

| Date depot | Type | Periode | Tokens |
|------------|------|---------|--------|
| | | | |

## Cartographie Groupe

<!-- Wikilinks vers vault/brantham/pappers/cartographie/ -->

- Groupe: [[brantham/pappers/cartographie/]]
- Filiales:
- Societe mere:
- Dirigeants communs:

## Secteur

[[brantham/pappers/secteurs/{{code_naf}}-{{secteur_slug}}]]

## Scoring Brantham

<!-- Evaluation interne pour M&A distressed -->

| Critere | Score | Notes |
|---------|-------|-------|
| Taille (CA/effectif) | /25 | |
| Secteur attractif | /25 | |
| Procedure exploitable | /25 | |
| Qualite actifs | /25 | |
| **TOTAL** | **/100** | |

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/pappers/secteurs/{{code_naf}}-{{secteur_slug}}]]
