---
name: Facture Autodesk AEC Collection 3 255 € (nov. 2025, impayée probable)
description: Facture directe Autodesk Ireland pour renouvellement AEC Collection 1 an — échéance 25/12/2025, probablement composante de la dette 401AUT (4 275 € au 31/12/2025)
type: reference
doc_source: 86/6-ACTIF/FACTURE AUTODESK 3 255 €.PDF
pages: 2
date_doc: facture 10/11/2025 — échéance 25/12/2025
---

# Doc 50 — Facture Autodesk AEC Collection 3 255 € (novembre 2025)

## Nature
**Facture directe Autodesk Ireland** (N° 9034047923) pour un abonnement **AEC Collection 1 an**. Envoyée le 10/11/2025 avec échéance 25/12/2025.

## Détail

| Champ | Valeur |
|---|---|
| Numéro de facture | **9034047923** |
| Date facture | **10/11/2025** |
| Date d'échéance | **25/12/2025** |
| Conditions | À 45 jours nets |
| Client facturé | Ingebime, 1 rue du 1er Mai, 92000 Nanterre |
| Numéro payeur (CSN) | **5151745145** |
| Numéro TVA | **FR44843349374** |
| Numéro souscription | **76279067229855** |
| Produit | **AEC Collection — Durée 1 an** |
| Montant HT | **3 255,00 €** |
| TVA | 0 € (autoliquidation — reverse charge) |
| **Net à payer** | **3 255,00 €** |

## Interprétation — lien avec le Doc 49 et la dette 401AUT

### Relation entre les deux souscriptions AEC Collection
- **Doc 50** (cette facture) : souscription ID **76279067229855** — facturée 10/11/2025, **échéance 25/12/2025**
- **Doc 49** (devis) : souscription ID **70834318219666** — période 19/02/2026 → 18/02/2027, facturée en janvier 2026

**Les deux IDs de souscription sont différents.** Hypothèses :
- **H1 — Rotation** : l'abonnement 76279067229855 couvrait l'année 2024-2025, et le 70834318219666 le prend en relais pour 2026-2027. Les deux coexistent brièvement au moment du passage de relais.
- **H2 — Deux AEC Collections actives** : Ingebime détenait **deux licences AEC Collection** en parallèle (pour deux utilisateurs différents). Improbable au vu du faible effectif technique (10 salariés).
- **H3 — Renouvellement raté + reprise** : l'ancienne souscription n'a pas été renouvelée à temps (facture 10/11/2025 impayée → suspension → nouvelle souscription ouverte en janvier 2026 avec un nouvel ID pour débloquer la situation).

**Hypothèse H3 la plus probable** : 
- Novembre 2025 : Autodesk facture le renouvellement annuel
- 25/12/2025 : échéance → **non payée** (Ingebime est en RJ, cash serré)
- Fin décembre 2025 / janvier 2026 : **suspension de licence**
- Janvier 2026 : l'équipe technique **perd l'accès à Revit/AEC Collection** — blocage opérationnel critique
- 26/01/2026 : Atlancad intervient et met en place un **nouveau devis** (Doc 49) avec nouvelle souscription ID 70834318219666 pour **réactiver l'accès** à partir du 19/02/2026

**Conséquence** : il y a eu une **période d'interruption de l'AEC Collection** entre décembre 2025 et février 2026 (~2 mois) pendant laquelle le Directeur de Pôle Fluides ou le BIM lead n'avait **probablement plus accès à Revit**. Impact opérationnel sérieux sur la production MOE.

### Cohérence avec la dette 401AUT (4 275 €)
Le Doc 36 (balance fournisseurs 2025) indique **401AUT "AUTODESK" 4 275 €** au 31/12/2025. La facture présente (3 255 €) représente la **ligne principale** de cette dette. Le solde (~1 020 €) correspond probablement à d'autres lignes antérieures ou à d'autres services complémentaires.

→ **Cette facture n'a probablement PAS été payée** à son échéance du 25/12/2025. Elle est **déclarée au passif de la procédure RJ** dans le compte 401AUT.

## Données bancaires Autodesk Ireland
Pour info (utile pour un éventuel règlement de régularisation post-reprise) :

| Champ | Valeur |
|---|---|
| Banque | Citibank Europe PLC |
| Adresse | 1 North Wall Quay, Dublin D01 T8Y1, Ireland |
| N° compte | 24056007 |
| SWIFT | CITIIE2X |
| IBAN | IE47CITI99005124056007 |
| Nom compte | Autodesk Ireland Operations UC |

## Implications pour l'offre de reprise

### 1. La licence BIM Revit est un point dur
**Si Ingebime a perdu l'accès à Revit** pendant 2 mois, le **directeur de pôle Fluides / lead BIM** a dû chercher des alternatives (version d'évaluation, BIM chez un partenaire, etc.). **Le travail BIM continue sans doute mais avec friction**.

**Priorité post-reprise** : réactiver immédiatement la licence AEC Collection (via le devis Doc 49) pour éliminer toute rupture de production.

### 2. Budget apurement partiel dette Autodesk
- Dette 401AUT : 4 275 € → **apurement partiel** de 2 000-3 000 € proposé à Autodesk peut débloquer une **reprise de bonne foi** de la relation commerciale
- Alternative : l'AJ a peut-être déjà procédé à ce règlement (via l'admin judiciaire validant une dépense de maintien d'activité). **À demander à l'AJ.**

### 3. Autoliquidation TVA (reverse charge)
Les factures Autodesk Ireland sont en **TVA 0 % autoliquidée** (Reverse Charge). Le repreneur doit veiller à bien **déclarer la TVA en autoliquidation** dans ses futures déclarations (CA3 — ligne 08 "Achats intracommunautaires de services"). Simple formalité mais à ne pas oublier.

### 4. CSN 5151745145
Le **Customer Service Number** d'Autodesk pour Ingebime est 5151745145. **À conserver précieusement** — c'est l'identifiant unique qui permettra au repreneur de continuer à gérer les licences existantes et l'historique sous un même compte (vs. ouvrir un compte vierge et perdre l'historique).

## Points à demander à l'AJ

- [ ] **La facture 9034047923 a-t-elle été payée** ? (intégralement, partiellement, ou totalement en attente au passif ?)
- [ ] **Dates de suspension et réactivation** éventuelles des licences Autodesk
- [ ] **Impact opérationnel** de la coupure BIM (retard projets ?)
- [ ] **Liste des factures Autodesk 2023-2025** — toutes payées, certaines impayées ?
- [ ] **Transférabilité du CSN 5151745145** au repreneur (procédure Autodesk)

## Related
- [[brantham/deals/active/ingebime/docs/49-autodesk-5343-78]] (devis de renouvellement 2026)
- [[brantham/deals/active/ingebime/docs/36-balance-provisoire-fournisseur-2025]] (401AUT 4 275 €, 401ATLANCAD 6 310 €)
- [[brantham/deals/active/ingebime/docs/34-balance-generale-provisoire-2025-1]] (compte 20500000 logiciels)
- [[brantham/deals/active/ingebime/docs/25-contrat-emaging-grenke]]
- [[brantham/_MOC]]
