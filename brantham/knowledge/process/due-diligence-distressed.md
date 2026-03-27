---
type: knowledge
project: brantham
domain: process
topic: due-diligence-distressed
created: 2026-03-26
updated: 2026-03-26
tags: [due-diligence, distressed, M&A, procedure-collective, cession, reprise, checklist]
status: active
---

# Due Diligence Specifique aux Entreprises en Difficulte

Guide operationnel pour la due diligence dans le contexte des reprises d'entreprises en procedure collective ([[redressement-judiciaire]], [[liquidation-judiciaire]], [[sauvegarde]]) en France.

---

## 1. Specificites de la DD Distressed

### 1.1 Contraintes de temps

| Procedure | Delai typique DD | Contraintes |
|---|---|---|
| **Liquidation judiciaire (LJ)** | 2-4 semaines max | DLDO (date limite depot offres) tres courte. Tribunal fixe le delai. Pas de depot 8 jours avant audience. |
| **Redressement judiciaire (RJ)** | 4-8 semaines | 15 jours minimum entre depot offre et audience. Administrateur fixe la DLDO. Possibilite de surenchere 48h avant audience. |
| **Sauvegarde** | 2-3 mois | Plus de temps, mais information souvent aussi limitee. |
| **Conciliation (amiable)** | 1-3 mois | Procedure confidentielle. Meilleur acces a l'information. Pas de publicite. |

**Consequence directe** : impossible de mener une DD exhaustive classique (6-12 semaines). Il faut prioriser les sujets critiques et accepter un niveau d'incertitude residuel plus eleve.

### 1.2 Information limitee et peu fiable

- **Comptabilite souvent defaillante** : les entreprises en difficulte ont frequemment des lacunes comptables (retards de cloture, ecritures manquantes, provisions insuffisantes).
- **Pas de VDD (Vendor Due Diligence)** : contrairement au M&A classique, le cedant (AJ/liquidateur) n'a ni le budget ni le mandat de preparer une VDD.
- **Data room sommaire** : l'AJ/liquidateur met a disposition une base documentaire apres signature d'un engagement de confidentialite, mais elle est souvent incomplete.
- **Dirigeants peu cooperatifs** : le dirigeant sortant peut etre demotive, en conflit, ou simplement absent. L'acces aux informations passe par l'AJ.
- **Systemes IT defaillants** : ERP non a jour, fichiers clients incomplets, donnees dispersees.

### 1.3 Pas de garanties vendeur classiques

- **Aucune garantie d'actif et de passif (GAP)** dans une cession judiciaire. Le repreneur acquiert les actifs "en l'etat".
- **Pas de representations & warranties** du cedant.
- **Pas d'indemnisation** pour les vices caches.
- **Seul recours** : action contre les organes de la procedure si des charges non communiquees apparaissent apres jugement.
- **En conciliation/amiable** : negociation possible de garanties limitees (capacite, titre de propriete, pouvoir), mais toujours inferieures au M&A classique.

### 1.4 Focus different du M&A classique

| M&A classique | Distressed M&A |
|---|---|
| [[valorisation-distressed|Valorisation]] par multiples, DCF | Valeur de liquidation, actif net reel |
| EBITDA normalise | **Cash burn rate** et tresorerie [[financial-modeling-distressed|13 semaines]] |
| Synergies et croissance | **Survie operationnelle** et retournement |
| GAP + earn-out | Pas de garanties, prix ferme |
| DD 8-12 semaines | DD 2-4 semaines max |
| Exclusivite negociee | Offres concurrentes, tribunal decide |
| Conditions suspensives | **Aucune condition suspensive possible** |

---

## 2. Checklist par Domaine

### 2.1 Due Diligence Financiere

**Objectif** : evaluer la realite economique de l'entreprise au-dela des etats financiers (souvent non fiables en distressed).

#### Tresorerie et Cash Flow (PRIORITE N.1)

- [ ] **[[financial-modeling-distressed|13-Week Cash Flow (TWCF)]]** : construire un previsionnel de tresorerie semaine par semaine sur 13 semaines. C'est l'outil #1 en distressed.
  - Recettes : encaissements clients realistes (pas le CA facture)
  - Depenses : charges fixes incompressibles, fournisseurs critiques, salaires, charges sociales
  - Besoin de financement du retournement (le repreneur finance tout)
- [ ] Position de tresorerie actuelle (encaisse + decouverts + lignes de credit)
- [ ] Burn rate mensuel : combien l'entreprise perd par mois ?
- [ ] Cash runway : combien de semaines avant cessation de paiements (si pas deja en CDO) ?
- [ ] Existence de cash traps : tresorerie bloquee (nantissements, Dailly, reserves)
- [ ] Financements bancaires : lignes en place, covenants brises, risque de denonciation

#### Passif Declare vs. Reel

- [ ] Passif declare au passif de la procedure (verification au greffe)
- [ ] **Ecart passif declare / passif reel** : le red flag #1. Comparer les declarations de creances avec la comptabilite.
- [ ] Dettes fournisseurs : montant reel, anciennete, fournisseurs en contentieux
- [ ] Dettes fiscales et sociales : URSSAF, impots, TVA (verifier les mises en demeure)
- [ ] Dettes bancaires : detail par ligne, garanties associees, rang de privilege
- [ ] Dettes intra-groupe et comptes courants d'associes
- [ ] Engagements hors bilan : cautions, garanties, credit-bail, leasing
- [ ] Provisions : sont-elles suffisantes ? (litiges, garanties produits, restructuration)

#### Creances Clients

- [ ] Balance agee des creances : ventilation par anciennete
- [ ] Taux de recouvrement realiste : historique de recouvrement sur 12 mois
- [ ] Creances douteuses et provision pour depreciation
- [ ] Concentration client : un client > 20% du CA = risque majeur
- [ ] Cession de creances (Dailly, affacturage) : montants deja mobilises
- [ ] Litiges clients en cours

#### Stocks

- [ ] Inventaire physique (obligatoire, ne pas se fier au comptable)
- [ ] Valorisation realiste : FIFO vs. cout de remplacement vs. valeur de liquidation
- [ ] **Taux d'obsolescence** : age du stock, rotation, saisons
- [ ] Stocks consignes ou en depot chez des tiers
- [ ] Stocks nanties ou gagees
- [ ] Stocks en transit

#### Immobilisations

- [ ] Etat reel des immobilisations vs. valeur nette comptable
- [ ] Equipements loues vs. possedes (attention aux credit-bails)
- [ ] Immobilier : propriete ou location ? Etat du bien ?
- [ ] Suretetes grevant les immobilisations (hypotheques, nantissements, gages)
- [ ] Plan d'investissement necessaire pour le retournement (CAPEX)

#### Rentabilite Normalisee

- [ ] EBITDA ajuste : retraiter les elements exceptionnels, les salaires du dirigeant, les charges non recurrentes
- [ ] Marge brute par produit/service : identifier ce qui est rentable
- [ ] Point mort (break-even) : a quel CA l'entreprise est-elle a l'equilibre ?
- [ ] Saisonnalite : mois de forte/faible activite

---

### 2.2 Due Diligence Juridique

#### Procedure Collective

- [ ] Nature de la procedure : sauvegarde, RJ, LJ, conciliation
- [ ] Date de cessation des paiements fixee par le tribunal
- [ ] **[[nullites-periode-suspecte|Periode suspecte]]** : identifier tous les actes entre la date de CDO et le jugement d'ouverture
  - Actes nuls de plein droit (art. L632-1) : 12 categories dont actes a titre gratuit, paiements de dettes non echues, hypotheques, nantissements
  - Extension : actes a titre gratuit annulables jusqu'a 6 mois avant CDO
  - Nullites facultatives (art. L632-2) : paiements et actes si connaissance de la CDO
- [ ] Organes de la procedure : identite de l'AJ, du mandataire, du juge-commissaire
- [ ] Plan de sauvegarde/redressement en cours ? Possibilite de cession ?
- [ ] Jugements anterieurs : conversions, extensions de procedure

#### Contrats en Cours

- [ ] **Inventaire des contrats** : lesquels reprendre, lesquels abandonner
- [ ] Contrats essentiels a l'exploitation : liste avec conditions et echeances
- [ ] **Clauses de changement de controle** : certains contrats peuvent etre resilies en cas de cession
- [ ] Contrats onereux non resiliables : obligations disproportionnees
- [ ] Contrats intuitu personae : necessitent l'accord du cocontractant
- [ ] **Precision critique** : seuls les contrats explicitement cites dans l'offre sont repris. Les autres sont exclus de plein droit.

#### Baux Commerciaux

- [ ] Bail principal : duree restante, loyer, charges, depot de garantie
- [ ] Clause resolutoire : arrieres de loyer ?
- [ ] Droit au renouvellement : conditions
- [ ] Etat des locaux : travaux a prevoir
- [ ] Conformite : normes ERP (etablissement recevant du public), accessibilite, securite incendie
- [ ] Baux secondaires : entrepots, bureaux, points de vente

#### Litiges et Contentieux

- [ ] Litiges en cours (liste exhaustive avec montants et probabilites)
- [ ] Litiges potentiels non encore declares
- [ ] Contentieux avec l'administration (URSSAF, impots, DREAL)
- [ ] Actions en responsabilite contre le dirigeant
- [ ] Actions en nullite de la periode suspecte en cours

#### Propriete Intellectuelle

- [ ] Marques : deposees, en vigueur, titulaire correct
- [ ] Brevets : portefeuille, validite, maintenance
- [ ] Noms de domaine : propriete, renouvellement
- [ ] Licences logicielles : transferabilite
- [ ] Secret des affaires : protection effective

#### Conformite Reglementaire

- [ ] Autorisations d'exploiter (ICPE, licences sectorielles)
- [ ] Transferabilite des autorisations au repreneur
- [ ] Conformite RGPD : registre de traitement, DPO, consentements
- [ ] Conformite sectorielle : agroalimentaire, pharmaceutique, BTP, etc.

---

### 2.3 Due Diligence Sociale / RH

**Contexte** : en cession judiciaire, le repreneur choisit les salaries qu'il reprend (dans la limite de l'offre acceptee). C'est un avantage majeur vs. M&A classique. Les licenciements non repris sont a la charge de la procedure (AGS/CGEA).

#### Effectifs et Structure

- [ ] Effectif total : CDI, CDD, interimaires, stagiaires, alternants
- [ ] Organigramme fonctionnel
- [ ] Pyramide des ages et anciennete
- [ ] Masse salariale totale (salaires + charges + avantages)
- [ ] Salaries proteges : representants du personnel, delegues syndicaux (autorisation inspection du travail pour licenciement)
- [ ] Salaries en arret maladie, conge maternite/paternite, AT/MP

#### Conventions et Accords

- [ ] Convention collective applicable (attention : elle suit l'activite, pas l'entreprise)
- [ ] Accords d'entreprise : temps de travail, primes, avantages en nature
- [ ] Usages et engagements unilateraux (difficiles a remettre en cause)
- [ ] Participation, interessement, epargne salariale
- [ ] Prevoyance et mutuelle : contrats en cours, portabilite

#### Contentieux Prud'homaux

- [ ] Litiges prud'homaux en cours : nombre, montants, probabilite de condamnation
- [ ] Historique des contentieux (3-5 ans)
- [ ] Risques de requalification (CDD, interim, freelance)
- [ ] Harcelement, discrimination : plaintes en cours

#### Personnes Cles

- [ ] **Identification des personnes cles** : qui fait tourner l'entreprise au quotidien ?
- [ ] Risque de depart : quelles personnes cles risquent de partir apres la cession ?
- [ ] Competences critiques non documentees (know-how concentre sur 1-2 personnes)
- [ ] Conditions de retention : clauses de non-concurrence, bonus de retention

#### Obligations de Reclassement

- [ ] Salaries non repris : obligation de reclassement a la charge de la procedure
- [ ] PSE (Plan de Sauvegarde de l'Emploi) : obligatoire si >= 10 licenciements economiques sur 30 jours dans une entreprise de >= 50 salaries
- [ ] Cout des licenciements : indemnites legales/conventionnelles (supportees par la procedure via AGS)
- [ ] Consultation du CSE : obligatoire sur le projet de cession et les licenciements

---

### 2.4 Due Diligence Fiscale

#### Dettes Fiscales et Sociales

- [ ] Montant des dettes fiscales declarees au passif
- [ ] Dettes URSSAF : montant, anciennete, plan d'echeancement
- [ ] TVA : declarations a jour ? Credits de TVA ? Rappels en cours ?
- [ ] IS/IR : declarations a jour ? Redressements en cours ?
- [ ] CFE/CVAE : dettes, declarations
- [ ] Taxe fonciere : dettes (si proprietaire)

#### Controles et Risques

- [ ] Controles fiscaux en cours ou recents (3 ans)
- [ ] Controles URSSAF en cours ou recents
- [ ] Risques de redressement identifies mais non encore notifies
- [ ] Conventions intra-groupe : prix de transfert conformes ?
- [ ] Avantages fiscaux : CIR, CII, JEI, ZFU -- conditions toujours remplies ? (voir [[fiscalite-restructuration]])

#### Deficits Reportables

- [ ] **ATTENTION** : en cession judiciaire d'actifs (plan de cession), les deficits reportables ne sont PAS transferes au repreneur. Ils restent dans la personne morale en liquidation.
- [ ] En cession de titres (share deal), les deficits peuvent etre conserves mais risque de remise en cause si changement d'activite reelle (art. 209-I CGI : maintien de l'identite de l'entreprise).
- [ ] En fusion post-acquisition : transfert de deficits sur agrement (art. 209-II CGI), conditions strictes.
- [ ] Report en avant : illimite dans le temps mais plafonne a 1M EUR + 50% du benefice excedant 1M EUR par exercice.

#### Structure Fiscale de la Reprise

- [ ] Asset deal (plan de cession) vs. share deal : implications fiscales radicalement differentes
- [ ] Droits d'enregistrement : 3% (0-23K EUR), 5% (au-dela) pour fonds de commerce ; 0.1% pour titres de societes a l'IS
- [ ] TVA sur cession : exoneration si transfert d'universalite (art. 257 bis CGI)
- [ ] Plus-values : traitement fiscal pour le cedant (souvent sans objet en procedure)

---

### 2.5 Due Diligence Operationnelle

#### Equipements et Outils de Production

- [ ] Inventaire physique des equipements (avec etat et age)
- [ ] Plan de maintenance : a jour ? Retards ?
- [ ] Equipements critiques : si un seul equipement tombe, l'activite s'arrete ?
- [ ] Equipements loues/en credit-bail : conditions, transferabilite
- [ ] Investissements necessaires a court terme (CAPEX obligatoire)
- [ ] Conformite des equipements (normes CE, securite, controles periodiques)

#### Fournisseurs Critiques

- [ ] **Top 10 fournisseurs** : CA, anciennete, conditions de paiement
- [ ] Fournisseurs en exclusivite ou quasi-exclusivite
- [ ] Fournisseurs ayant coupe les livraisons (consequence frequente des procedures)
- [ ] Conditions de reprise des relations : paiement comptant exige ? Garanties ?
- [ ] Fournisseurs alternatifs identifies pour les approvisionnements critiques
- [ ] Dependance a un fournisseur unique (single source) = risque de rupture

#### Clients

- [ ] **Top 20 clients** : CA, anciennete, evolution
- [ ] Concentration client : un client > 20% du CA = risque majeur
- [ ] Solvabilite des principaux clients
- [ ] Contrats en cours : duree, conditions, resiliabilite
- [ ] Clients perdus depuis l'ouverture de la procedure
- [ ] Risque de perte de clients post-cession (effet de reputation)
- [ ] Carnet de commandes : pipeline reel vs. previsionnel

#### Systemes IT

- [ ] Infrastructure IT : age, etat, securite
- [ ] ERP/logiciels metier : licences, transferabilite, maintenance
- [ ] Donnees : sauvegarde, integrite, migration necessaire
- [ ] Cybersecurite : dernier audit, vulnerabilites connues
- [ ] Site web, e-commerce : propriete, hebergement, noms de domaine

#### Passif Environnemental

- [ ] **Phase I ESA** (Environmental Site Assessment) : historique du site, utilisation passee
- [ ] ICPE : l'entreprise est-elle classee Installation Classee pour la Protection de l'Environnement ?
- [ ] Autorisations ICPE : en cours de validite ? Transferables ?
- [ ] **Sols pollues** : consultation BASIAS/BASOL, historique industriel du site (voir [[passif-environnemental]])
- [ ] **Amiante** : DTA (Dossier Technique Amiante) a jour ?
- [ ] Dechets : gestion, borderaux de suivi, stockage
- [ ] Rejets : eaux usees, emissions atmospheriques, conformite
- [ ] **Responsabilite du repreneur** : en cas de cession judiciaire, le repreneur peut devenir le nouveau "dernier exploitant" au sens de l'art. L512-17 du Code de l'environnement, et donc responsable de la remise en etat du site.
- [ ] Cout estime de depollution/remise en etat
- [ ] Clauses de garantie environnementale (negociables en amiable, inexistantes en judiciaire)

---

## 3. Red Flags Specifiques au Distressed

### 3.1 Red Flags Financiers

| Red Flag | Explication | Gravite |
|---|---|---|
| Ecart passif declare / passif reel > 20% | Creanciers non declares, provisions insuffisantes | CRITIQUE |
| Cash burn > 100K EUR/mois sans visibilite | L'entreprise se vide avant la cession | CRITIQUE |
| Creances clients irrecouvrables > 30% | Surestimation de l'actif circulant | ELEVE |
| Stock obsolete > 40% de la valeur comptable | Actif surgonfle | ELEVE |
| Ecritures comptables manquantes sur 6+ mois | Impossible d'evaluer la realite economique | CRITIQUE |
| Revenue recognition agressive (CA facture mais non livrable) | Surestimation du CA | ELEVE |
| Changements frequents d'expert-comptable/CAC | Tentative de masquer des irregularites | MOYEN |

### 3.2 Red Flags Juridiques

| Red Flag | Explication | Gravite |
|---|---|---|
| Actes de la periode suspecte non identifies | Risque de nullite retroactive, perte d'actifs | CRITIQUE |
| Garanties donnees a des tiers (cautions, nantissements) | Actifs potentiellement indisponibles | ELEVE |
| Contrats onereux non resiliables | Charges fixes incompressibles | ELEVE |
| Baux avec clause resolutoire activee | Risque de perte du local commercial | CRITIQUE |
| Litiges majeurs non declares | Passif cache | CRITIQUE |
| Propriete intellectuelle non protegee ou contestee | Valeur intangible a risque | MOYEN |

### 3.3 Red Flags Sociaux

| Red Flag | Explication | Gravite |
|---|---|---|
| Litiges prud'homaux massifs (> 5 dossiers) | Cout potentiel + climat social deteriore | ELEVE |
| Personnes cles deja parties ou sur le depart | Perte de savoir-faire operationnel | CRITIQUE |
| Convention collective couteuse non anticipee | Surcout salarial post-reprise | MOYEN |
| Salaries proteges nombreux | Complexite des licenciements | MOYEN |
| Competences critiques concentrees sur 1-2 personnes | Risque operationnel majeur | ELEVE |

### 3.4 Red Flags Operationnels

| Red Flag | Explication | Gravite |
|---|---|---|
| Fournisseurs critiques ayant coupe les livraisons | Risque de rupture d'activite immediate | CRITIQUE |
| Client > 30% du CA perdu ou menacant de partir | Effondrement du CA post-reprise | CRITIQUE |
| Equipements critiques en fin de vie | CAPEX obligatoire non budgete | ELEVE |
| Passif environnemental (sols pollues, amiante, ICPE) | Cout de depollution potentiellement > prix d'achat | CRITIQUE |
| Systemes IT obsoletes ou non maintenus | Risque operationnel + cout de remplacement | MOYEN |
| Aucun carnet de commandes post-cession | Pas de visibilite revenue | ELEVE |

---

## 4. Timing et Process

### 4.1 Data Room : ce qu'on peut attendre

**Contenu typique d'une data room en procedure collective** :

| Document | Disponibilite | Fiabilite |
|---|---|---|
| Bilans et comptes de resultat (3 ans) | Generalement oui | Moyenne (souvent non audites) |
| Balances generales | Souvent oui | Variable |
| Liste des salaries et contrats | Oui (AJ le fournit) | Bonne |
| Liste des contrats en cours | Partielle | A verifier |
| Etat du passif declare | Oui (greffe) | Bonne (mais peut etre incomplet) |
| Baux commerciaux | Generalement oui | Bonne |
| Inventaire des stocks | A demander/faire soi-meme | Faible (souvent obsolete) |
| Etats des immobilisations | Variable | Faible |
| Previsionnel de tresorerie | Rarement | A construire soi-meme |
| Audit environnemental | Tres rarement | A faire soi-meme |

**Acces** : signature prealable d'un **engagement de confidentialite** (NDA) aupres de l'AJ/liquidateur.

### 4.2 Acces au Site et aux Equipes

- **Visite du site** : a demander a l'AJ. Generalement accordee avec escorte.
- **Entretiens avec le management** : soumis a accord de l'AJ. Souvent limites.
- **Management presentations** : rares en LJ, parfois en RJ. Le management peut ne plus etre en poste.
- **Entretiens avec les salaries** : delicats (confidentialite, anxiete). Possibles avec accord AJ et CSE.
- **Acces aux clients/fournisseurs** : generalement refuse avant jugement (risque de destabilisation).

### 4.3 Timeline Type

#### Liquidation Judiciaire (LJ) -- Sprint

```
Jour 0       : Publication BODACC / appel d'offres
Jour 1-3     : Prise de contact AJ, NDA, acces data room
Jour 3-7     : Quick scan financier + visite site
Jour 7-14    : DD ciblee (tresorerie, RH, contrats cles)
Jour 14-21   : Redaction et depot de l'offre
Jour 21-28   : Surencheres possibles (48h avant audience)
Jour 28-35   : Audience au tribunal, jugement
Jour 35+     : Prise de possession immediate
```

#### Redressement Judiciaire (RJ) -- Marathon Court

```
Semaine 1-2  : Prise de contact, NDA, data room
Semaine 2-4  : DD financiere et operationnelle
Semaine 4-6  : DD juridique, sociale, fiscale
Semaine 6-8  : Construction de l'offre et du business plan
Semaine 8    : Depot de l'offre (15j min avant audience)
Semaine 10   : Audience, jugement
Semaine 10+  : Prise de possession
```

---

## 5. Application Brantham

### 5.1 Quick Scan 48h (LJ)

Framework de triage rapide pour decider si une opportunite LJ merite une offre. Temps total : 48 heures.

**Heure 0-4 : Screening initial**
- [ ] BODACC : nature de la procedure, date, tribunal
- [ ] Infogreffe : bilans disponibles, effectif, CA
- [ ] Societe.com / Pappers : historique, dirigeants, actionnariat
- [ ] Premier contact AJ : disponibilite data room, DLDO

**Heure 4-12 : Analyse financiere express**
- [ ] Derniers bilans : CA, marge brute, EBE, resultat net
- [ ] Estimation du passif : dettes fournisseurs + fiscales + sociales + bancaires
- [ ] Tresorerie actuelle (si disponible)
- [ ] Scoring Brantham : note globale deal (pipeline existant)

**Heure 12-24 : Visite + RH + Contrats**
- [ ] Visite du site (si possible)
- [ ] Liste des salaries : effectif, masse salariale, personnes cles
- [ ] Contrats critiques : bail, top 5 clients, top 5 fournisseurs
- [ ] Red flags immediats ? (environnement, litiges, passif cache)

**Heure 24-36 : Valorisation et Structuration**
- [ ] Estimation actif net reel (actifs - passif repris)
- [ ] CAPEX necessaire au retournement
- [ ] BFR (besoin en fonds de roulement) post-reprise
- [ ] Prix cible vs. prix marche (moyenne : 3% du CA en LJ)

**Heure 36-48 : Decision Go/No-Go**
- [ ] Synthese : forces, faiblesses, risques, opportunites
- [ ] Decision : offre / pas d'offre / besoin de plus d'info
- [ ] Si go : redaction de l'offre

### 5.2 DD Complete 2-4 Semaines (RJ)

Framework de due diligence approfondie pour les cessions en RJ avec plus de temps.

**Semaine 1 : Financiere + Operationnelle**
- DD financiere complete (cf. checklist 2.1)
- Visite de site detaillee
- Entretiens management (si disponible)
- Construction du 13-week cash flow

**Semaine 2 : Juridique + Sociale**
- DD juridique complete (cf. checklist 2.2)
- DD sociale complete (cf. checklist 2.3)
- Identification des contrats a reprendre/abandonner
- Analyse de la periode suspecte

**Semaine 3 : Fiscale + Environnementale**
- DD fiscale (cf. checklist 2.4)
- DD environnementale (cf. checklist 2.5)
- Phase I ESA si necessaire
- Consolidation des risques identifies

**Semaine 4 : Synthese + Offre**
- Red flag report final
- Valorisation et structuration du prix
- Business plan post-reprise (3 ans)
- Redaction et depot de l'offre

### 5.3 Template de Scoring DD

Grille de notation rapide pour comparer les opportunites :

| Critere | Poids | Score (1-5) | Note |
|---|---|---|---|
| Qualite de l'information disponible | 10% | | |
| Sante de la tresorerie | 15% | | |
| Ecart passif declare/reel | 15% | | |
| Qualite des actifs (equipements, stock) | 10% | | |
| Solidite du portefeuille clients | 15% | | |
| Risque social (effectif, litiges) | 10% | | |
| Risque environnemental | 10% | | |
| Risque juridique (contrats, litiges) | 10% | | |
| Complexite du retournement | 5% | | |
| **TOTAL** | **100%** | | |

**Seuils** :
- Score >= 3.5 : Opportunite solide, deposer une offre
- Score 2.5-3.5 : A approfondir, DD ciblee sur les points faibles
- Score < 2.5 : Passer. Trop de risques pour le rendement attendu.

---

## 6. Annexes

### 6.1 Articles de Reference (Code de Commerce)

| Article | Objet |
|---|---|
| L620-1 et s. | Sauvegarde |
| L631-1 et s. | Redressement judiciaire |
| L640-1 et s. | Liquidation judiciaire |
| L632-1 | Nullites de droit (periode suspecte) |
| L632-2 | Nullites facultatives (periode suspecte) |
| L642-1 a L642-17 | Cession de l'entreprise (plan de cession) |
| L642-3 | Restrictions sur le repreneur |
| L642-5 | Criteres de selection de l'offre |
| L1224-1 (Code du travail) | Transfert des contrats de travail |
| L512-17 (Code de l'environnement) | Responsabilite du dernier exploitant |

### 6.2 Interlocuteurs Cles

| Role | Mission | Contact typique |
|---|---|---|
| Administrateur judiciaire (AJ) | Gere l'entreprise en RJ, centralise les offres | CNAJMJ, Infogreffe |
| Liquidateur judiciaire | Vend les actifs en LJ | CNAJMJ, Infogreffe |
| Juge-commissaire | Supervise la procedure, autorise les actes | Tribunal de commerce |
| Ministere public (Parquet) | Veille a l'interet general | Tribunal |
| CSE / representants du personnel | Consultes sur la cession | Via AJ |
| AGS/CGEA | Garantit le paiement des salaires | Delegation regionale |

### 6.3 Sources d'Information

| Source | Utilite |
|---|---|
| BODACC (bodacc.fr) | Publications legales : ouvertures, plans, jugements |
| Infogreffe (infogreffe.fr) | Bilans, K-bis, procedures en cours |
| Pappers / Societe.com | Donnees financieres, dirigeants, actionnariat |
| CNAJMJ (cnajmj.fr) | Annuaire des AJ et mandataires, offres de cession |
| CessionGreffe (cessiongreffe.com) | Offres de reprise publiees par les greffes |
| BASIAS / BASOL (georisques.gouv.fr) | Sites industriels et sols pollues |
| InfoCessions (infocessions.com) | Plateforme d'offres de reprise |

---

*Document cree le 2026-03-26. A mettre a jour regulierement en fonction des retours terrain et de l'evolution legislative.*
