---
type: knowledge
project: brantham
domain: corporate-finance
topic: valorisation-distressed
date: 2026-03-26
status: active
tags: [valorisation, distressed, M&A, liquidation, DCF, EBITDA, multiples, procedures-collectives]
sources:
  - https://groupeca2.fr/evaluation-entreprise/evaluer-entreprise-difficulte/
  - https://valorisationentreprise.fr/comment-valoriser-une-entreprise-en-difficulte-avant-une-vente/
  - https://www.maydaymag.fr/eclairage-comment-valoriser-une-entreprise-en-difficulte/
  - https://the-big-win.com/distressed-ma/
  - https://www.sostene-avocats.com/les-fiches-pratiques-du-dirigeant/articles/determiner-le-prix-de-cession-d-une-societe-en-redressement-ou-liquidation-judiciaire-mode-d-emploi
  - https://financyal.fr/multiple-ebitda-valorisation-2026/
  - https://clfi.co.uk/insights/ebitda-multiples-by-industry-uk-2025/
  - https://www.wallstreetprep.com/knowledge/demystifying-the-13-week-cash-flow-model-in-excel/
  - https://entreprise-decisions.fr/normaliser-ebitda-ebit-cadre-valorisation-entreprise/
  - https://www.houdart-ac.fr/nos-articles/audit/la-mission-de-due-diligence-et-les-retraitements-de-lebitda/
  - https://www.cfnews.net/L-actualite/Marche-General/Paroles-d-expert/Du-M-A-classique-au-distressed-M-A-329209
---

# Valorisation d'entreprises en difficulte — Guide exhaustif

## Pourquoi la valorisation distressed est differente

La valorisation d'une entreprise en difficulte differe fondamentalement de la valorisation classique pour cinq raisons structurelles :

**1. Incertitude sur la continuite d'exploitation**
Le presuppose de base de toute methode de valorisation standard (DCF, multiples) est que l'entreprise continue d'operer indefiniment. En distressed, cette hypothese est remise en cause (cf. [[comptabilite-crise|continuite d'exploitation]]). L'entreprise peut disparaitre a tout moment, ce qui rend les projections financieres intrinsequement fragiles.

**2. Asymetrie d'information**
Le vendeur (souvent sous pression du tribunal, des creanciers, ou de l'administrateur judiciaire) detient des informations que le repreneur ne peut pas verifier dans les delais imposes. Les comptes sont souvent degrades, les reportings incomplets, les provisions sous-estimees. Le risque de "cadavre dans le placard" (dette cachee, litige non provisionne, contrat toxique) est eleve. La [[due-diligence-distressed]] doit etre priorisee sur les sujets critiques.

**3. Urgence temporelle**
Les procedures collectives imposent des delais stricts. En LJ, le tribunal fixe une date limite pour les offres. En RJ, l'administrateur a une periode d'observation limitee (6 mois renouvelable une fois, max 18 mois). Cette pression temporelle reduit le pouvoir de negociation de l'acquereur mais aussi la qualite de la due diligence.

**4. Contrainte de la purge du passif**
En plan de cession (Art. L.642-1 et suivants du Code de commerce), le cessionnaire acquiert les actifs libres de toute charge. Le passif est purge. Cela signifie que le prix n'a pas a couvrir le passif total — il reflète la valeur des actifs repris et les engagements pris (emploi, investissement, activite).

**5. Nombre limite d'acheteurs**
Le pool de repreneurs potentiels est restreint : la plupart des acheteurs classiques fuient le risque procedural. Moins de competition = prix plus bas. En pratique, beaucoup de cessions se font avec un seul candidat.

---

## Methode 1 : Valeur liquidative (approche patrimoniale)

### Principe
Evaluer chaque actif individuellement a sa valeur de realisation en cas de vente forcee, puis soustraire les dettes. C'est le plancher de valorisation : ce que l'entreprise vaut si on la demantele.

### Quand l'utiliser
- Liquidation judiciaire sans repreneur
- Entreprise dont l'activite est definitivement arretee
- Benchmark minimum pour toute offre de reprise

### Decotes typiques par type d'actif

| Type d'actif | % de recuperation vs valeur comptable | Commentaire |
|---|---|---|
| Tresorerie | 100% | Seul actif sans decote |
| Creances clients | 65-80% | Depend de l'anciennete et de la solvabilite des debiteurs. Creances > 90j : 30-50% max |
| Creances douteuses | 0-30% | Souvent irrecouvrables en contexte distressed |
| Stocks matieres premieres | 50-75% (moy. 67%) | Depend de la perissabilite et de la specificite |
| Stocks produits finis | 30-60% | Forte decote si produits specifiques au client |
| Stocks obsoletes | 0-15% | Quasi zero si pas de marche secondaire |
| Immobilier (propriete) | 60-90% | Depend de l'emplacement. Prime areas : jusqu'a 100%+ si foncier bien situe |
| Immobilier (bail) | 0-50% | Valeur du droit au bail selon emplacement et duree restante |
| Machines et equipements generiques | 20-50% | Meilleure recuperation si marche d'occasion actif |
| Machines specifiques/sur-mesure | 5-20% | Quasi pas de marche secondaire |
| Vehicules | 40-70% | Argus + decote vente rapide |
| Informatique et mobilier | 5-15% | Depreciation tres rapide |
| Marques et PI | 0-100% | Tres variable. Marque connue = valeur. Brevet non exploite = zero |
| Fonds de commerce | 10-50% | Depend de la clientele residuelle et de l'emplacement |
| Goodwill | 0% | En liquidation, le goodwill vaut zero. Il n'existe que dans un contexte going concern |

### Formule simplifiee

```
Valeur liquidative = SUM(Actifs x Taux de recuperation) - Passif privilegié residuel - Couts de liquidation
```

Les couts de liquidation incluent : honoraires du liquidateur (bareme legal), frais de vente aux encheres (10-20% du prix), couts de licenciement du personnel restant, loyers residuels, depollution eventuelle.

**Regle empirique** : la valeur liquidative represente generalement 15-35% de la valeur comptable nette des actifs.

---

## Methode 2 : Going concern / DCF ajuste

### Principe
Projeter les cash flows futurs de l'entreprise en supposant qu'elle est reprise et restructuree, puis les actualiser a un taux refletant le risque eleve.

### Quand l'utiliser
- Redressement judiciaire avec plan de continuation ou de cession
- Entreprise dont le core business est viable mais mal gere ou surendette
- Quand le repreneur a un plan de retournement credible

### Ajustements specifiques au distressed

**Taux d'actualisation (WACC ajuste)**

| Profil d'entreprise | WACC typique |
|---|---|
| Entreprise saine, cotee | 8-10% |
| PME non cotee, saine | 12-15% |
| Entreprise en difficulte, plan credible | 15-20% |
| Entreprise en difficulte, plan incertain | 20-30% |
| Startup early-stage / retournement tres risque | 25-50% |

Le WACC distressed se decompose ainsi :
- Taux sans risque : ~3% (OAT 10 ans)
- Prime de marche actions : 5-7%
- Prime de taille (PME) : 3-5%
- Prime de risque specifique (distressed) : 4-10%
- Prime d'illiquidite : 2-4%

**Cash flows ajustes**
- Utiliser les cash flows normalises (voir section EBITDA normalise ci-dessous)
- Modeliser 3 scenarios : pessimiste, base, optimiste
- Ponderer les scenarios (ex: 40% pessimiste, 40% base, 20% optimiste)
- Horizon explicite court (3-5 ans) car la visibilite est limitee
- Valeur terminale : multiple de sortie conservateur OU taux de croissance perpetuelle faible (0-1%)

**Formule**

```
VE = SUM(t=1 to n) [FCF_t / (1 + WACC)^t] + VT / (1 + WACC)^n

ou VT = FCF_n+1 / (WACC - g) si croissance perpetuelle
ou VT = EBITDA_n x Multiple de sortie
```

### Exemple chiffre

Entreprise industrielle en RJ, EBITDA normalise retournement = 500K EUR/an a partir de Y3.

| Annee | FCF projete | Facteur d'actualisation (18%) | FCF actualise |
|---|---|---|---|
| Y1 | -200K | 0.847 | -169K |
| Y2 | +100K | 0.718 | +72K |
| Y3 | +400K | 0.609 | +244K |
| Y4 | +500K | 0.516 | +258K |
| Y5 | +550K | 0.437 | +240K |
| VT (5x EBITDA) | 2 750K | 0.437 | +1 202K |
| **Total VE** | | | **1 847K** |

Avec une decote d'execution de 20-30% (risque de retournement), on arrive a une fourchette de 1 300K - 1 480K EUR.

---

## Methode 3 : Comparables distressed (multiples)

### Principe
Appliquer des multiples observes dans des transactions similaires (meme secteur, meme taille, meme type de procedure) a l'EBITDA normalise ou au CA de l'entreprise cible.

### Multiples EV/EBITDA par secteur — Marche mid-market Europe (2025)

| Secteur | Multiple sain (mid-market) | Multiple distressed estime |
|---|---|---|
| Software / SaaS | 7.7-8.8x | 3.0-5.0x |
| Healthcare / Pharma | 7.4-7.6x | 3.5-5.0x |
| IT Services | 7.0-7.6x | 3.0-4.5x |
| E-commerce | 6.0-6.4x | 2.5-4.0x |
| Services aux entreprises | 5.5-5.9x | 2.5-3.5x |
| Industrie / Manufacturing | 5.0-5.3x | 2.0-3.5x |
| Agroalimentaire | 5.0-5.3x | 2.5-3.5x |
| Media / Communication | 4.0-4.1x | 1.5-2.5x |
| Hotellerie / Tourisme | 4.0-4.1x | 1.5-2.5x |
| Transport / Logistique | 4.0-4.3x | 1.5-3.0x |
| Construction / BTP | 3.5-3.8x | 1.5-2.5x |
| Commerce de gros | 3.3-3.5x | 1.5-2.5x |
| Commerce de detail | 3.0-3.4x | 1.0-2.0x |

**Decote distressed typique** : 40-60% par rapport au multiple sain du meme secteur.

### Impact de la taille sur les multiples

| EBITDA normalise | Multiple moyen (sain) | Multiple distressed estime |
|---|---|---|
| 200K EUR | 3.1x | 1.5-2.0x |
| 500K EUR | 4.1x | 2.0-2.5x |
| 1M EUR | 5.1x | 2.5-3.0x |
| 2M EUR | 5.5x | 2.5-3.5x |
| 5M EUR | 7.1x | 3.5-4.5x |
| 10M EUR | 8.5x | 4.0-5.5x |

### Multiples EV/CA (quand EBITDA negatif)
Quand l'EBITDA est negatif ou non significatif, on utilise le multiple de CA :
- Industrie distressed : 0.2-0.5x CA
- Services distressed : 0.3-0.7x CA
- Tech distressed : 0.5-1.5x CA
- Commerce distressed : 0.1-0.3x CA

### Decotes additionnelles

| Facteur | Decote supplementaire |
|---|---|
| Dependance au dirigeant | -15 a -20% |
| Illiquidite (pas de marche, PME) | -20 a -30% |
| Concentration client (>30% un client) | -10 a -20% |
| Risque d'execution du retournement | -10 a -30% |
| Litige en cours | -5 a -25% selon montant |

---

## Methode 4 : Valeur de remplacement (cout de reconstitution)

### Principe
Estimer combien il couterait de recreer l'entreprise de zero : acheter les memes machines, recruter les memes equipes, obtenir les memes autorisations, developper la meme clientele.

### Quand l'utiliser
- Entreprise avec des actifs strategiques difficilement reproductibles (autorisations, certifications, clientele captive, savoir-faire)
- Benchmark pour verifier que le prix d'acquisition est inferieur au cout de construction from scratch
- Particulierement pertinent en industrie reglementee (dechets, sante, agro ICPE)

### Composantes du cout de remplacement

| Element | Methode d'estimation |
|---|---|
| Immobilier | Cout de construction neuf - depreciation physique et fonctionnelle |
| Equipements | Prix catalogue neuf - obsolescence |
| Autorisations/licences | Cout et delai d'obtention (souvent le plus gros poste en industries reglementees) |
| Equipe en place | Cout de recrutement + formation + courbe d'apprentissage (6-18 mois de salaires) |
| Clientele | Cout d'acquisition client x nombre de clients (CAC x base) |
| Systemes IT | Cout de reimplementation |
| Marque/reputation | Investissement marketing cumule sur 3-5 ans |

### Regle empirique
Si prix d'acquisition < 50% du cout de remplacement, c'est une bonne affaire. En distressed M&A France, c'est frequemment le cas — les reprises a la barre permettent d'acquerir des actifs a 20-40% de leur cout de reconstitution.

---

## EBITDA normalise : comment le calculer en distressed

L'EBITDA normalise est la pierre angulaire de toute valorisation par les multiples ou le DCF. En distressed, les retraitements sont plus nombreux et plus significatifs que dans une transaction classique.

### Retraitements systematiques

**Categorie 1 — Charges non recurrentes (a rajouter)**
- Frais de restructuration (plan social, fermeture de sites)
- Honoraires d'avocats et mandataires lies a la procedure
- Provisions exceptionnelles pour litiges
- Pertes sur creances liees a la crise (ex: faillite d'un client majeur)
- Amendes et penalites ponctuelles
- Couts de depart de dirigeants
- Depreciations d'actifs exceptionnelles
- Cout de la sous-activite (capacite non utilisee pendant la crise)

**Categorie 2 — Produits non recurrents (a retrancher)**
- Reprises de provisions exceptionnelles
- Plus-values de cession d'actifs
- Subventions ou aides ponctuelles (CICE arriere, remises de dettes)
- Indemnites d'assurance exceptionnelles

**Categorie 3 — Corrections de niveau (normalisation)**
- Remuneration du dirigeant : ajuster au marche. Un dirigeant-fondateur de PME peut se payer 30K ou 300K — normaliser au cout d'un DG salarie (120-180K pour une PME de 5-20M CA selon secteur)
- Loyers intra-groupe : si le dirigeant possede les murs et facture un loyer non marche, corriger au prix du marche
- Contrats avec parties liees : tout contrat entre l'entreprise et le dirigeant/ses societes doit etre revu et ajuste au prix de marche
- Participations aux benefices : inclure dans l'EBITDA normalise en France (charge obligatoire)
- Credit-bail (leasing) : reclasser si necessaire pour comparabilite. L'EBITDA avec beaucoup de leasing surestime la rentabilite economique reelle

**Categorie 4 — Corrections de BFR**
- Stocks : provisionner la part obsolete ou invendable. Surstockage pre-procedure = gonflement artificiel de l'actif
- Creances : ajuster pour les impayes reels et pas seulement les provisions comptables
- Fournisseurs : si l'entreprise etait en retard de paiement (signe de stress), le BFR normalise sera plus eleve car il faudra revenir a des conditions normales

### Formule

```
EBITDA normalise = EBITDA comptable
  + Charges non recurrentes
  - Produits non recurrents
  +/- Ajustement remuneration dirigeant
  +/- Ajustement loyers
  +/- Ajustement contrats parties liees
  + Provision stocks obsoletes
  + Provision creances irrecouvrables supplementaires
```

### Exemple

| Poste | Montant |
|---|---|
| EBITDA comptable | -150K |
| + Frais de restructuration | +280K |
| + Honoraires procedure | +90K |
| + Perte exceptionnelle client | +120K |
| - Subvention ponctuelle | -50K |
| + Ajustement salaire dirigeant (sous-paye) | -60K |
| + Ajustement loyer (sur-facture) | +30K |
| - Stock obsolete non provisionne | -40K |
| **= EBITDA normalise** | **+220K** |

Un EBITDA comptable de -150K se transforme en un EBITDA normalise de +220K. C'est exactement le type de situation ou le distressed M&A cree de la valeur : l'entreprise apparait moribonde mais le core business genere un profit recurrent de 220K.

---

## Decotes par procedure et impact sur le prix

### Procedures et leur impact

| Procedure | Impact sur le prix | Purge du passif | Reprise salaries | Delai typique offre |
|---|---|---|---|---|
| Mandat ad hoc | Decote faible (10-20%). Negociation amiable. | Non | Non applicable | Libre |
| Conciliation | Decote moderee (15-25%). Confidentiel. | Non | Non applicable | 4-5 mois |
| Sauvegarde | Decote 20-35%. Plan arrete par tribunal. | Partielle (plan d'apurement) | Oui (tous) | 6-18 mois |
| Redressement judiciaire (plan de cession) | Decote 30-50%. Offre au tribunal. | Oui (totale pour cessionnaire) | Oui (choisis par repreneur, min fixe par tribunal) | 2-6 mois |
| Liquidation judiciaire (cession activite) | Decote 50-70%. Urgence max. | Oui (totale) | Possible mais pas obligatoire | 1-3 mois |
| Liquidation judiciaire (actifs isoles) | Decote 60-85%. Vente aux encheres. | Oui | Non | Immediat |

### Purge du passif = valeur cachee pour l'acheteur

En plan de cession, le repreneur acquiert les actifs sans reprendre les dettes. Concretement :
- Les dettes fournisseurs sont purgees
- Les dettes fiscales et sociales sont purgees
- Les emprunts bancaires sont purges
- Les cautionnements et suretes sont purges (sauf immobilier inclus dans la cession)
- Les litiges anterieurs restent a la charge de l'ancienne entite

**Cela signifie que le "vrai prix" pour le repreneur est :**

```
Prix reel = Prix de cession paye au tribunal
          + Investissements d'urgence (BFR, maintenance)
          + Couts de restructuration post-reprise
          - Economie de passif (=valeur des dettes purgees)
```

Si une entreprise a 2M de dettes et que le tribunal accepte une offre a 400K avec purge du passif, le repreneur "economise" 1.6M de dettes — c'est l'avantage structurel de la reprise a la barre.

### Ce que regarde le tribunal (Art. L.642-5 du Code de commerce)

Le prix n'est pas le seul critere. Le tribunal evalue :
1. Le maintien de l'emploi (nombre de postes repris)
2. La perennite de l'activite (plan d'affaires credible)
3. Le prix offert (couverture du passif = mieux, mais pas obligatoire)
4. Les garanties de paiement (cautions, sequestre)
5. Les investissements prevus
6. La credibilite du repreneur (experience, moyens financiers)

En pratique, une offre avec plus d'emplois repris mais un prix inferieur peut l'emporter sur une offre plus genereuse financierement mais qui licencie davantage.

---

## 13-Week Cash Flow : structure et utilisation

Le 13-week cash flow (TWCF) est l'outil de reference en restructuring. Il projette les flux de tresorerie hebdomadaires sur 13 semaines (un trimestre).

### Structure type

```
SEMAINE                    | S1  | S2  | S3  | ... | S13 | TOTAL
========================== |===  |===  |===  |===  |===  |======
ENCAISSEMENTS              |     |     |     |     |     |
  Encaissements clients    |     |     |     |     |     |
  Autres encaissements     |     |     |     |     |     |
  Produits de cession actif|     |     |     |     |     |
  Tirage ligne de credit   |     |     |     |     |     |
TOTAL ENCAISSEMENTS        |     |     |     |     |     |
                           |     |     |     |     |     |
DECAISSEMENTS              |     |     |     |     |     |
  Fournisseurs MP          |     |     |     |     |     |
  Sous-traitance           |     |     |     |     |     |
  Salaires nets            |     |     |     |     |     |
  Charges sociales         |     |     |     |     |     |
  Loyers                   |     |     |     |     |     |
  Energie / utilites       |     |     |     |     |     |
  Assurances               |     |     |     |     |     |
  Honoraires (avocats, AJ) |     |     |     |     |     |
  Impots et taxes          |     |     |     |     |     |
  Service de la dette      |     |     |     |     |     |
  Capex urgents            |     |     |     |     |     |
  Autres charges           |     |     |     |     |     |
TOTAL DECAISSEMENTS        |     |     |     |     |     |
                           |     |     |     |     |     |
FLUX NET HEBDOMADAIRE      |     |     |     |     |     |
TRESORERIE DEBUT           |     |     |     |     |     |
TRESORERIE FIN             |     |     |     |     |     |
                           |     |     |     |     |     |
DISPONIBLE SUR LIGNE CREDIT|     |     |     |     |     |
BESOIN DE FINANCEMENT      |     |     |     |     |     |
```

### Schedules support (sous-modeles)

1. **Roll-forward creances clients** : solde debut + facturation - encaissements = solde fin. Base sur le DSO (Days Sales Outstanding) historique, ajuste pour le stress
2. **Roll-forward stocks** : solde debut + achats - COGS = solde fin. Base sur le DIOH (Days Inventory on Hand)
3. **Roll-forward fournisseurs** : solde debut + achats - paiements = solde fin. Base sur le DPO (Days Payable Outstanding)
4. **Roll-forward salaires** : masse salariale brute mensuelle / 4.33 = charge hebdomadaire, ajustee des decalages de paie
5. **Borrowing base** : calcul de la capacite de tirage sur la ligne de credit en fonction des actifs eligibles (% des creances + % des stocks)

### Utilisation

- **Negociation avec les creanciers** : prouver que l'entreprise a assez de cash pour survivre pendant la restructuration
- **Demande de DIP financing** : justifier le besoin de financement interimaire
- **Decision du tribunal** : le TWCF est souvent demande par l'administrateur judiciaire pour evaluer la viabilite
- **Pilotage de crise** : identifier la semaine ou le cash tombe a zero ("cash wall")
- **Mise a jour hebdomadaire** : comparer reel vs previsionnel, ajuster les projections

### Red flags dans un TWCF
- DSO qui s'allonge (clients qui retardent les paiements = perte de confiance)
- DPO qui raccourcit (fournisseurs qui exigent du cash = perte de confiance supply chain)
- Ecart systematique reel vs previ (management trop optimiste)
- Tresorerie fin < 0 sans plan de financement
- Pas de capex du tout (l'entreprise cannibalise ses actifs)

---

## Business plan de retournement : structure et hypotheses

### Structure type

1. **Resume executif** (2 pages max)
   - Situation actuelle en une phrase
   - Diagnostic des causes de la difficulte
   - Mesures prises / a prendre
   - Objectifs a 12 mois et 36 mois
   - Besoins de financement

2. **Diagnostic**
   - Analyse financiere (3 derniers bilans, compte de resultat, BFR, endettement)
   - Analyse operationnelle (capacite de production, taux d'utilisation, productivite)
   - Analyse commerciale (top clients, concentration, pipeline, tendances marche)
   - Analyse RH (effectif, competences cles, climat social)
   - Causes racines de la difficulte (marche ? management ? surendettement ? sinistre ?)

3. **Plan d'action detaille**
   - Actions court terme (0-6 mois) : mesures de cash (BFR, couts, prix)
   - Actions moyen terme (6-18 mois) : restructuration operationnelle
   - Actions long terme (18-36 mois) : repositionnement strategique
   - Responsable et deadline pour chaque action
   - Quick wins identifies et quantifies

4. **Projections financieres**
   - Compte de resultat previsionnel (3 ans, mensualise Y1)
   - Bilan previsionnel (3 ans)
   - Plan de tresorerie (13 semaines en detail, puis mensuel sur 3 ans)
   - Plan de financement (besoins et sources)
   - Analyse de sensibilite (3 scenarios)

5. **Hypotheses documentees**
   - Chaque hypothese doit etre explicitement listee, quantifiee, et justifiee
   - Source de chaque hypothese (benchmark, historique, contrat, devis)

### Hypotheses critiques a documenter

| Hypothese | Question a poser | Red flag |
|---|---|---|
| CA | Evolution du CA : baisse, stabilisation, croissance ? | Croissance > 10%/an en Y1 = irréaliste sauf preuve |
| Marge brute | La marge revient-elle au niveau historique ? | Marge Y1 > marge historique sans justification |
| Effectif | Combien de departs, recrutements ? | Plan sans reduction de couts mais avec hausse de marge |
| BFR | Comment evolue le BFR ? | BFR en baisse alors que le CA croît = suspect |
| Capex | Investissements necessaires au retournement ? | Zero capex sur 3 ans = l'outil va se degrader |
| Financement | Qui finance et a quelles conditions ? | Pas de source de financement identifiee |
| Clients | Les clients restent-ils apres la procedure ? | Hypothese 100% retention post-procedure = naif |
| Fournisseurs | Conditions de paiement post-reprise ? | DPO inchange alors que la confiance est rompue |

### Red flags dans un business plan de retournement
- Hockey stick : CA en chute puis explosion en Y2-Y3 sans actions concretes pour l'expliquer
- Pas de restructuration de couts : on garde tout le monde et ca passe quand meme
- Hypothese de marge en hausse sans action prix ou mix produit
- BFR sous-estime : oubli des acomptes fournisseurs exiges post-procedure
- Pas de plan B si le scenario base ne se realise pas
- Investissements non finances
- "Synergies" non quantifiees ni planifiees

---

## Exemples chiffres : fourchettes observees en distressed M&A France

### Cessions a la barre du tribunal — Prix payes

| Taille entreprise (CA) | Prix de cession typique | % du CA | % de la VE saine estimee |
|---|---|---|---|
| TPE < 1M EUR | 20-150K EUR | 5-20% du CA | 15-30% |
| PME 1-5M EUR | 100K-1M EUR | 5-25% du CA | 15-35% |
| PME 5-20M EUR | 300K-5M EUR | 5-30% du CA | 20-40% |
| ETI 20-100M EUR | 1-20M EUR | 5-25% du CA | 20-45% |
| Grande entreprise >100M | 5-50M+ EUR | Variable | 25-50% |

### Fourchettes de multiples observes (distressed, France, PME)

| Agregat | Fourchette basse | Fourchette moyenne | Fourchette haute |
|---|---|---|---|
| EV/EBITDA normalise | 1.5x | 2.5-3.5x | 5.0x |
| EV/CA | 0.1x | 0.2-0.4x | 0.7x |
| EV/Actif net revalue | 0.2x | 0.4-0.6x | 0.9x |
| Prix/Nombre emplois | 5-10K/emploi | 15-25K/emploi | 40-60K/emploi |

**Note** : le prix par emploi est un indicateur officieux mais tres utilise par les tribunaux de commerce pour jauger le serieux d'une offre. En dessous de 10K/emploi, l'offre est souvent jugee insuffisante sauf contexte tres degrade.

### Secteurs avec les plus fortes decotes en France
1. **Restauration/Hotellerie** : decote 40-60% vs valeur saine (moy ~30% en CHR confirme par les praticiens)
2. **Commerce de detail** : decote 50-70%, surtout physique (impact e-commerce)
3. **BTP** : decote 40-60%, fort alea sur les chantiers en cours
4. **Industrie lourde** : decote 40-55%, mais actifs tangibles offrent un plancher
5. **Services B2B** : decote 30-50%, meilleure retention client = meilleure valorisation

---

## Erreurs courantes de valorisation en distressed

### 1. Utiliser l'EBITDA comptable sans normaliser
L'EBITDA comptable en distressed est souvent negatif a cause de charges non recurrentes. Ne pas normaliser = sous-evaluer massivement l'entreprise (ou passer a cote d'un deal).

### 2. Appliquer des multiples sains a une situation distressed
Un multiple de 6x EV/EBITDA sectoriel applique sans decote distressed surévalue l'entreprise de 50-70%.

### 3. Ignorer le BFR post-reprise
L'acquereur doit financer le BFR de relance : reconstituer les stocks, payer les fournisseurs comptant (confiance rompue), financer le decalage creances. Ce cout de relance BFR est souvent egal ou superieur au prix de cession.

### 4. Sous-estimer les couts de restructuration
Licenciements, fermeture de sites, renegociation de baux, investissements de remise a niveau — ces couts post-acquisition peuvent representer 1 a 3x le prix de cession.

### 5. Ne pas verifier les dettes hors bilan
Garanties personnelles, engagements de credit-bail, provisions pour remise en etat (ICPE), litiges prud'homaux en cours. En distressed, ces postes sont souvent sous-documentes.

### 6. Surestimer la retention clients
Apres une procedure collective, 20-40% des clients partent dans les 12 premiers mois. Les plans qui supposent 100% de retention sont systematiquement faux.

### 7. Confondre valeur liquidative et prix plancher
La valeur liquidative est un plancher theorique. En pratique, les couts de liquidation (honoraires, temps, degorgement) font que le realisable net est souvent inferieur a la valeur liquidative calculee.

### 8. Ne pas integrer le cout du temps
Chaque mois de procedure consume du cash, erode la clientele, demotive les equipes. Le time value of distress est reel : une entreprise qui vaut 1M en mois 1 de RJ peut ne plus valoir que 600K en mois 6.

---

## Application Brantham : scoring de la valeur d'un deal

### Grille de scoring valeur (sur 100)

| Critere | Poids | Score 1 (mauvais) | Score 5 (excellent) |
|---|---|---|---|
| EBITDA normalise positif | 20 | EBITDA normalise < 0 | EBITDA normalise > 10% marge |
| Actifs tangibles vs prix demande | 15 | Actifs < 50% du prix | Actifs > 200% du prix (decote) |
| Cout de remplacement vs prix | 15 | Prix > 80% remplacement | Prix < 30% remplacement |
| BFR de relance estimé | 10 | BFR relance > 2x prix cession | BFR relance < 30% prix cession |
| Retention clients estimee | 10 | < 50% clients vont rester | > 80% clients sous contrat |
| Couts restructuration post-reprise | 10 | Restructuration > 2x prix | Restructuration < 30% prix |
| Multiple EV/EBITDA normalise | 10 | > 5x EBITDA normalise | < 2x EBITDA normalise |
| Qualite info financiere disponible | 5 | Pas de comptabilite fiable | Comptes audites disponibles |
| Procedure (urgence/competition) | 5 | LJ avec deadline 2 semaines | Mandat ad hoc, temps dispo |

### Interpretation du score

| Score | Signal | Action |
|---|---|---|
| 80-100 | Excellent deal potentiel | Fast track : offre rapide, due diligence acceleree |
| 60-79 | Bon deal si execution OK | Analyse approfondie du business plan retournement |
| 40-59 | Deal moyen, risque eleve | Seulement si angle strategique fort (client, technologie, equipe) |
| 20-39 | Mauvais ratio risque/rendement | Pass sauf si actifs seuls valent le prix |
| 0-19 | Destruction de valeur probable | Pass |

### Checklist rapide Brantham avant offre

- [ ] EBITDA normalise calcule (avec les 4 categories de retraitements)
- [ ] Valeur liquidative estimee (plancher)
- [ ] Cout de remplacement estime (plafond valeur strategique)
- [ ] Multiple EV/EBITDA normalise < multiple distressed sectoriel
- [ ] BFR de relance chiffre
- [ ] 13-week cash flow projete post-reprise
- [ ] 3 scenarios modelises (pessi/base/opti)
- [ ] Dettes hors bilan verifiees
- [ ] Retention clients estimee avec methode
- [ ] Total cost of acquisition (prix + BFR + restructuration + capex) calcule
