---
type: financial_snapshot
siren:
denomination:
annee_exercice:
date_cloture:
duree_exercice_mois: 12
chiffre_affaires:
resultat_exploitation:
resultat_net:
ebitda:
capitaux_propres:
total_bilan:
endettement_net:
tresorerie:
effectif:
date_fetch_pappers:
tags: []
---

# Comptes {{annee_exercice}} — {{denomination}} ({{siren}})

> Donnees financieres extraites via Pappers. Cloture: {{date_cloture}}.

## Entreprise

[[brantham/pappers/entreprises/{{siren}}-{{slug}}]]

## Compte de Resultat

| Poste | Montant (EUR) | N-1 | Variation |
|-------|---------------|-----|-----------|
| Chiffre d'affaires | {{chiffre_affaires}} | | |
| Production | | | |
| Achats & charges externes | | | |
| Charges de personnel | | | |
| **Resultat d'exploitation** | {{resultat_exploitation}} | | |
| Resultat financier | | | |
| Resultat exceptionnel | | | |
| Impots | | | |
| **Resultat net** | {{resultat_net}} | | |

## Bilan Actif

| Poste | Montant (EUR) |
|-------|---------------|
| Immobilisations incorporelles | |
| Immobilisations corporelles | |
| Immobilisations financieres | |
| Stocks | |
| Creances clients | |
| Tresorerie | {{tresorerie}} |
| **Total Actif** | {{total_bilan}} |

## Bilan Passif

| Poste | Montant (EUR) |
|-------|---------------|
| Capital social | |
| Reserves | |
| Resultat exercice | {{resultat_net}} |
| **Capitaux propres** | {{capitaux_propres}} |
| Dettes financieres | |
| Dettes fournisseurs | |
| Dettes fiscales & sociales | |
| **Total Passif** | {{total_bilan}} |

## Ratios Cles

| Ratio | Valeur | Benchmark secteur |
|-------|--------|-------------------|
| Marge nette | | |
| ROE | | |
| Gearing (dette/CP) | | |
| BFR (jours CA) | | |
| Ratio liquidite | | |
| Endettement net / EBITDA | | |

## Signaux d'Alerte

<!-- Detecter les signaux de difficulte -->

- [ ] Capitaux propres negatifs
- [ ] Resultat net negatif 2 annees consecutives
- [ ] CA en baisse > 20%
- [ ] Endettement > 5x EBITDA
- [ ] Tresorerie negative

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/pappers/entreprises/{{siren}}-{{slug}}]]
- [[brantham/_MOC]]
