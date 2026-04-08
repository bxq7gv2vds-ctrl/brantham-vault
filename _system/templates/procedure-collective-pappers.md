---
type: procedure_collective
siren:
denomination:
type_procedure: # sauvegarde | redressement_judiciaire | liquidation_judiciaire | mandat_ad_hoc | conciliation | sauvegarde_financiere_acceleree
tribunal:
date_ouverture:
date_jugement:
date_fin_periode_observation:
date_plan:
date_cloture:
administrateur_judiciaire:
mandataire_judiciaire:
juge_commissaire:
statut: en_cours # en_cours | plan_arrete | cloture | converti
est_deal_potentiel: false
score_deal: # 0-100
code_naf:
secteur_brantham:
ca_dernier:
effectif:
localisation:
tags: []
date_fetch_pappers:
---

# {{type_procedure}} — {{denomination}} ({{siren}})

> Procedure collective suivie via Pappers/BODACC. Derniere maj: {{date_fetch_pappers}}.

## Entreprise

[[brantham/pappers/entreprises/{{siren}}-{{slug}}]]

| Champ | Valeur |
|-------|--------|
| Denomination | {{denomination}} |
| SIREN | {{siren}} |
| Secteur | {{code_naf}} — {{libelle_naf}} |
| CA dernier | {{ca_dernier}} EUR |
| Effectif | {{effectif}} |
| Localisation | {{localisation}} |

## Procedure

| Champ | Valeur |
|-------|--------|
| Type | {{type_procedure}} |
| Tribunal | {{tribunal}} |
| Date ouverture | {{date_ouverture}} |
| Date fin observation | {{date_fin_periode_observation}} |
| Statut | {{statut}} |

## Intervenants

| Role | Nom | Etude/Cabinet | Lien |
|------|-----|---------------|------|
| Administrateur judiciaire | {{administrateur_judiciaire}} | | [[brantham/pappers/dirigeants/]] |
| Mandataire judiciaire | {{mandataire_judiciaire}} | | [[brantham/pappers/dirigeants/]] |
| Juge-commissaire | {{juge_commissaire}} | | |

## Timeline BODACC

<!-- Toutes les publications liees a cette procedure -->

| Date | Type publication | Resume |
|------|-----------------|--------|
| | Jugement ouverture | |

## Evaluation Deal Brantham

| Critere | Score | Notes |
|---------|-------|-------|
| Taille cible (CA > 500K) | /20 | |
| Secteur porteur | /20 | |
| Actifs tangibles | /20 | |
| Timeline exploitable | /20 | |
| Complexite limitee | /20 | |
| **TOTAL** | **/100** | |

### Decision

- [ ] Qualifier comme deal
- [ ] Lancer analyse approfondie
- [ ] Rejeter (motif: )

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/pappers/entreprises/{{siren}}-{{slug}}]]
- [[brantham/pappers/secteurs/{{code_naf}}-{{secteur_slug}}]]
- [[brantham/knowledge/procedures/]]
