---
type: knowledge
project: brantham
category: finance
topic: assurances en M&A distressed
level: avance
created: 2026-03-27
updated: 2026-03-27
tags: [assurance, D&O, RC-pro, W&I, garantie-passif, escrow, environnement, homme-cle, distressed]
status: active
related: [valorisation-distressed, due-diligence-distressed, structuration-offres-reprise]
---

# Assurances en M&A Distressed

Guide complet sur les produits d'assurance et mecanismes de couverture dans le contexte des reprises d'entreprises en difficulte en France. Couvre la D&O, la RC pro des mandataires, les alternatives a la garantie de passif, la W&I insurance, l'assurance homme-cle, et les couvertures environnementales.

---

## 1. Contexte General

### 1.1 Particularite du distressed

En M&A classique, la garantie de passif (garantie d'actif et de passif, GAP) est le mecanisme standard de protection de l'acquereur. Le vendeur garantit la sincerite des comptes et indemnise l'acquereur en cas de passif cache.

En M&A distressed, ce mecanisme est **inoperant** :
- En **cession judiciaire** ([[plans-de-cession|plan de cession]] L642-1 et suivants C.com) : le repreneur ne reprend pas le passif anterieur. Pas de vendeur solvable pour garantir quoi que ce soit
- En **cession de gre a gre en LJ** : le liquidateur cede "en l'etat", sans garantie
- En **pre-pack/conciliation** : le vendeur est en difficulte, sa capacite a honorer une garantie est douteuse
- Les actionnaires/dirigeants de la cible sont souvent insolvables

D'ou la necessite de recourir a des mecanismes alternatifs d'assurance et de couverture.

### 1.2 Cartographie des risques a couvrir

| Risque | Probabilite en distressed | Impact potentiel |
|---|---|---|
| Passif social cache (heures sup, contentieux prud'homaux) | Elevee | Moyen |
| Passif fiscal cache (redressement, TVA) | Moyenne | Eleve |
| Passif environnemental (depollution, ICPE) | Moyenne | Tres eleve |
| Vices caches sur actifs | Moyenne | Moyen |
| Contentieux en cours non reveles | Moyenne | Variable |
| Perte d'homme-cle post-reprise | Elevee | Eleve |
| Responsabilite des dirigeants anterieurs | Elevee | Moyen |

---

## 2. D&O (Directors & Officers Liability Insurance)

### 2.1 Definition et couverture

L'assurance D&O (Responsabilite Civile des Dirigeants) couvre les dirigeants de droit et de fait contre les consequences pecuniaires des reclamations de tiers liees a l'exercice de leurs fonctions.

### 2.2 Couverture standard

| Element couvert | Detail |
|---|---|
| **Fautes de gestion** | Erreurs, omissions, negligences dans la gestion |
| **Responsabilite civile** | Dommages causes aux tiers, salaries, associes |
| **Frais de defense** | Honoraires d'avocats, frais de procedure |
| **Sanctions financieres** | Amendes civiles et administratives (pas penales) |
| **Comblement de passif** | Action en responsabilite pour insuffisance d'actif (L651-2 C.com) |

### 2.3 Exclusions courantes

- Fraude et fautes intentionnelles (une fois etablies definitivement)
- Sanctions penales (amende, emprisonnement)
- Avantages personnels indument percus
- Actions entre co-assures (sauf insolvabilite)
- Dommages environnementaux (souvent exclus ou sous-limites)
- Dommages corporels (couverts par d'autres polices)

### 2.4 Specificites en distressed

**Run-off (extension de garantie posterieurement a la cessation du mandat)** :
- La police D&O couvre normalement les dirigeants en exercice
- Quand un dirigeant quitte ses fonctions (cession, LJ), il reste expose aux actions pendant plusieurs annees (prescription 3-5 ans)
- Le **run-off** etend la couverture pour 3, 5 ou 10 ans apres la fin du mandat
- **Cout** : 150-300% de la prime annuelle pour un run-off de 5 ans
- **Critique** : a souscrire AVANT l'ouverture de la procedure collective (apres, la compagnie refuse ou la prime explose)

**Points de vigilance** :
- Verifier que la police existante de la cible est toujours en vigueur (primes payees ?)
- En RJ : les primes d'assurance sont des creances posterieures privilegiees (L622-17)
- En LJ : si la police est resiliee, les anciens dirigeants perdent toute couverture
- Le repreneur doit souscrire sa propre police D&O des la prise de controle
- Les dirigeants de transition sont couverts par la police du cabinet de management de transition ou leur propre RC pro

### 2.5 Marche et cout

| Element | Fourchette |
|---|---|
| Prime annuelle PME (1-10M EUR de garantie) | 3 000 - 25 000 EUR |
| Prime annuelle ETI (10-50M EUR) | 20 000 - 100 000 EUR |
| Run-off 5 ans | 150-300% de la prime annuelle |
| Franchise | 5 000 - 50 000 EUR |

Principaux assureurs : AIG, Chubb, Allianz, AXA XL, Zurich, Hiscox.

---

## 3. RC Pro des Administrateurs et Mandataires Judiciaires

### 3.1 Obligation d'assurance

Les administrateurs judiciaires (AJ) et mandataires judiciaires (MJ) sont soumis a une **obligation legale d'assurance RC professionnelle** (L811-6 et L812-4 C.com).

### 3.2 Couverture

| Element | Detail |
|---|---|
| **Fautes professionnelles** | Erreurs dans la conduite de la procedure, mauvaise gestion pendant la periode d'observation |
| **Manquements a leurs obligations** | Defaut de diligence, retard dans les operations, omission de verification du passif |
| **Prejudice aux creanciers** | Repartition fautive, oubli de declaration, etc. |

### 3.3 Importance pour le repreneur

Si l'AJ ou le MJ commet une faute dans la conduite de la procedure de cession (ex: information incomplete en data room, vice cache non revele malgre connaissance), le repreneur peut engager la responsabilite du mandataire. La RC pro de celui-ci constitue alors la seule source d'indemnisation.

**Limites** :
- Plafonds de garantie souvent modestes (1-5M EUR)
- Franchises elevees
- Delais de reclamation longs (procedure judiciaire)
- Difficulte a prouver la faute du mandataire

---

## 4. Alternatives a la Garantie de Passif

### 4.1 Escrow (Sequestre)

**Principe** : une partie du prix d'acquisition est consignee chez un tiers (notaire, Caisse des Depots, banque) pendant une duree determinee. En cas de passif cache, le repreneur puise dans le sequestre.

| Element | Detail |
|---|---|
| **Montant typique** | 10-30% du prix d'acquisition |
| **Duree** | 12-24 mois (jusqu'a 36 mois pour les risques fiscaux) |
| **Liberation** | Automatique a l'echeance, sauf reclamation formelle |
| **Cout** | Faible (frais de gestion du sequestre : 0,1-0,5% du montant) |

**En distressed** :
- Fonctionne en cession amiable (conciliation, pre-pack)
- Difficile en cession judiciaire : le tribunal veut un prix certain et immediat
- Le vendeur en difficulte accepte mal de voir une partie du prix bloquee
- Alternative : sequestre finance par l'acquereur (deduction du prix offert)

### 4.2 Retention de prix

**Principe** : l'acquereur retient une partie du prix et ne la verse que si aucun passif cache ne se manifeste dans un delai convenu.

- Plus simple qu'un escrow (pas de tiers)
- Meme problematique en cession judiciaire (le tribunal peut refuser)
- Risque : le vendeur conteste la retenue

### 4.3 Earn-out

**Principe** : une partie du prix est conditionnee a l'atteinte de performances futures (CA, EBITDA, clients).

| Element | Detail |
|---|---|
| **Avantage** | Aligne les interets, reduit le risque de surpaiement |
| **Inconvenient** | Le tribunal de commerce prefere un prix certain et definitif |
| **Duree typique** | 1-3 ans |
| **Mecanisme** | Formule claire, audit contradictoire, arbitrage en cas de litige |

**En cession judiciaire** : l'earn-out pur est generalement refuse par le tribunal. Alternative : prix plancher garanti + complement conditionnel. Le tribunal retient le prix plancher pour l'analyse comparative des offres.

### 4.4 Clause de revision de prix

En cession amiable, une clause prevoyant la revision du prix en fonction d'un bilan de reference (closing accounts) peut jouer un role similaire a la garantie de passif.

**Avantage** : ajustement objectif base sur les comptes
**Limite** : ne couvre pas les passifs non refletes dans les comptes (contentieux latents, environnement)

---

## 5. W&I Insurance (Warranty & Indemnity)

### 5.1 Principe

L'assurance W&I (Warranty & Indemnity, ou garantie de passif assuree) est une police d'assurance qui couvre l'acquereur contre les pertes resultant d'une violation des declarations et garanties du vendeur.

En M&A classique, le marche W&I est mature : primes de 1-2% du montant de couverture, processus standardise, delais de 2-3 semaines.

### 5.2 Disponibilite en distressed

**Tres limitee.** Les assureurs W&I sont reticents en distressed pour les raisons suivantes :

| Frein | Explication |
|---|---|
| **Absence de representations** | En cession judiciaire, il n'y a pas de SPA classique avec declarations et garanties du vendeur. Pas de "warranty" a assurer. |
| **Qualite de la DD** | La DD est souvent incomplete (delai court, info limitee). L'assureur exige une DD complete pour souscrire. |
| **Risque moral** | Le vendeur insolvable n'a aucune incitation a reveler les passifs. |
| **Passifs connus eleves** | Beaucoup de passifs sont deja identifies ou probables (social, fiscal, environnement). L'assureur ne couvre pas les risques connus. |
| **Anti-selection** | Les dossiers distressed presentent un risque structurellement plus eleve. |

### 5.3 Cas ou la W&I peut fonctionner

- **Pre-pack / cession amiable** avec un SPA structure incluant des declarations et garanties
- **Cible en conciliation** (pas encore en procedure collective formelle) avec un vendeur cooperatif
- **Risques specifiques identifies** couverts par une police synthetique (ex: risque fiscal precis)
- **Staple W&I** : le vendeur souscrit la police et la cede a l'acquereur (rare en distressed)

### 5.4 Cout

| Element | Fourchette |
|---|---|
| **Prime** (si disponible) | 2-5% du montant de couverture (vs 1-2% en M&A classique) |
| **Franchise (retention)** | 1-3% de l'enterprise value (vs 0,5-1% en classique) |
| **Montant couverture typique** | 10-30% de l'enterprise value |
| **Duree** | 2-7 ans selon les risques |

### 5.5 Courtiers specialises

Le marche W&I est intermedie par des courtiers specialises :
- Marsh (JLT Specialty)
- Aon M&A Solutions
- WTW (Willis Towers Watson)
- Lockton
- Howden M&A

---

## 6. Assurance Homme-Cle

### 6.1 Principe

L'assurance homme-cle couvre l'entreprise contre les consequences financieres de l'indisponibilite (deces, invalidite, maladie longue) d'une personne essentielle a l'activite.

### 6.2 Pertinence en distressed

En reprise d'entreprise en difficulte, les hommes-cles sont souvent :
- Le dirigeant operationnel (si maintenu post-reprise)
- Le directeur commercial (relation client critique)
- Le directeur technique/R&D (savoir-faire unique)
- Le chef d'atelier / responsable production (process knowledge)

**Risque accru en distressed** : stress, surcharge, demotivation, tentatives de debauchage par les concurrents.

### 6.3 Couverture et cout

| Element | Detail |
|---|---|
| **Capital assure** | 1-5 annees de marge brute attribuable a la personne |
| **Evenements couverts** | Deces, PTIA, ITT (selon contrat) |
| **Prime** | 0,5-2% du capital assure par an |
| **Delai de souscription** | 2-4 semaines (questionnaire medical) |

**Attention** : l'assurance homme-cle ne couvre PAS la demission ou le debauchage. Pour ce risque, utiliser des clauses contractuelles (clause de non-concurrence, retention bonus, golden handcuffs).

---

## 7. Assurance Risque Environnemental (PLL)

### 7.1 Principe

La Pollution Legal Liability (PLL) couvre les frais de depollution et les responsabilites liees a une contamination environnementale du site. Particulierement critique pour les reprises de sites industriels (ICPE, Seveso).

### 7.2 Pertinence en distressed

| Situation | Risque |
|---|---|
| Site classe ICPE | Obligation de remise en etat a la cessation d'activite (L512-6-1 Code env.) |
| Pollution historique | Responsabilite du dernier exploitant (et potentiellement du proprietaire du terrain) |
| Seveso seuil haut/bas | Obligations renforcees de surveillance et depollution |
| Ancien site minier | Responsabilite de l'exploitant meme apres arret |

**En cession judiciaire** : le repreneur qui reprend l'exploitation du site **reprend aussi les obligations environnementales** (contrairement au passif financier qui reste a la procedure). C'est un risque majeur et souvent sous-estime.

### 7.3 Couverture PLL

| Element | Detail |
|---|---|
| **Frais de depollution** | Cout de decontamination du sol et des eaux souterraines |
| **Responsabilite civile pollution** | Dommages aux tiers (voisins, nappe phreatique) |
| **Frais de defense** | Procedures administratives et judiciaires |
| **Interruption d'activite** | Perte d'exploitation liee a la pollution |
| **Transport de polluants** | Contamination de sites voisins |

### 7.4 Processus de souscription

1. **Phase 1 ESA** (Environmental Site Assessment) : revue documentaire (historique du site, activites passees, bases de donnees BASOL/BASIAS/SIS)
2. **Phase 2 ESA** : investigations sur site (sondages, analyses sol/eau)
3. **Quantification du risque** : estimation des couts de depollution potentiels
4. **Souscription** : sur la base du rapport ESA, l'assureur propose une couverture

### 7.5 Cout

| Element | Fourchette |
|---|---|
| **Prime annuelle** | 5 000 - 100 000 EUR (selon risque et montant couvert) |
| **Montant couverture** | 1 - 50 M EUR |
| **Franchise** | 25 000 - 500 000 EUR |
| **Duree** | 5-10 ans |

**Disponibilite** : meilleure qu'en W&I car les assureurs environnementaux sont habitues aux risques historiques. Les principaux acteurs : AIG, AXA XL, Berkshire Hathaway, Zurich, Swiss Re.

### 7.6 Due diligence environnementale prealable

Obligatoire avant toute reprise de site industriel :
- Consultation BASOL (sites et sols pollues appeles a action), BASIAS (anciens sites industriels), SIS (secteurs d'information sur les sols)
- Analyse des arretes prefectoraux (ICPE)
- Verification des rapports de surveillance obligatoires
- Identification des substances dangereuses utilisees/stockees
- Evaluation des obligations de remise en etat

---

## 8. Application Brantham Partners

### 8.1 Checklist assurances dans le processus de deal

**Phase teaser/screening** :
- [ ] Identifier si la cible est sur un site ICPE (risque environnemental)
- [ ] Verifier l'existence d'une police D&O en cours sur la cible

**Phase DD** :
- [ ] Demander les polices d'assurance en vigueur (D&O, RC, multirisque, PLL)
- [ ] Identifier les hommes-cles et evaluer le risque de depart
- [ ] Commander un ESA Phase 1 si site industriel
- [ ] Estimer le cout des assurances post-reprise

**Phase offre** :
- [ ] Integrer le cout des assurances dans la valorisation
- [ ] Prevoir un mecanisme de couverture du passif cache (escrow, retention, W&I si applicable)
- [ ] Budgeter la D&O pour les nouveaux dirigeants

**Phase closing** :
- [ ] Souscrire D&O pour le repreneur et ses dirigeants
- [ ] Souscrire assurance homme-cle si applicable
- [ ] Souscrire PLL si site industriel
- [ ] Verifier le run-off D&O des anciens dirigeants

### 8.2 Cout total assurances pour une reprise type PME

| Poste | Budget annuel |
|---|---|
| D&O dirigeants | 5 000 - 15 000 EUR |
| RC exploitation | 3 000 - 20 000 EUR |
| Multirisque | Variable (existant souvent) |
| Homme-cle (1-2 personnes) | 3 000 - 10 000 EUR |
| PLL (si site industriel) | 10 000 - 50 000 EUR |
| **Total** | **20 000 - 100 000 EUR/an** |

A integrer dans le business plan de reprise.

---

## Ressources et References

- Code de commerce : L622-17 (creances posterieures), L651-2 (comblement de passif), L811-6 et L812-4 (assurance AJ/MJ)
- Code des assurances : L113-1 et suivants
- Code de l'environnement : L512-6-1 (ICPE, remise en etat), L556-1 et suivants (SIS)
- BASOL : https://basol.developpement-durable.gouv.fr/
- BASIAS/SIS : https://www.georisques.gouv.fr/
- CNAJMJ — Regime d'assurance des mandataires de justice
- AMRAE — Association pour le Management des Risques et des Assurances de l'Entreprise

---

## Voir aussi

- [[due-diligence-distressed]] — Checklist assurances dans la phase DD
- [[valorisation-distressed]] — Integration du cout des assurances dans la valorisation
- [[structuration-offres-reprise]] — Prevoir les mecanismes de couverture dans l'offre
- [[passif-environnemental]] — Risque environnemental et assurance PLL
- [[post-closing-execution]] — Souscription des polices post-cession
- [[sanctions-dirigeants]] — Responsabilite des dirigeants et D&O
- [[plans-de-cession]] — Purge du passif et alternatives a la GAP
- [[ecosysteme-restructuring]] — Courtiers W&I et assureurs specialises
