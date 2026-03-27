---
type: knowledge
project: brantham
category: finance
topic: modelisation financiere en M&A distressed
level: avance
created: 2026-03-27
updated: 2026-03-27
sources:
  - https://www.wallstreetprep.com/knowledge/recovery-analysis-waterfall-payment-structure-restructuring/
  - https://www.wallstreetprep.com/knowledge/demystifying-the-13-week-cash-flow-model-in-excel/
  - https://www.wallstreetprep.com/knowledge/wacc/
  - https://www.wallstreetprep.com/knowledge/loss-given-default-lgd/
  - https://www.wallstreetprep.com/knowledge/cost-of-equity/
  - https://www.wallstreetprep.com/knowledge/equity-value-to-enterprise-value-bridge/
  - https://www.alvarezandmarsal.com/thought-leadership/the-13-week-cash-flow
  - https://pages.stern.nyu.edu/~adamodar/pdfiles/country/distresspres.pdf
  - https://www.distressed-debt-investing.com/2009/09/simplified-distressed-debt-recovery.html
  - https://www.debexpert.com/blog/how-to-value-distressed-debt-portfolios-a-step-by-step-guide
  - https://www.degruyterbrill.com/document/doi/10.1515/jbvela-2020-0002/html
  - https://corporatefinanceinstitute.com/resources/career-map/sell-side/risk-management/expected-loss-definition-calculation-importance/
  - https://corporatefinanceinstitute.com/resources/commercial-lending/loss-given-default-lgd/
  - https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/
  - https://macabacus.com/valuation/dcf-wacc
  - https://macabacus.com/valuation/dcf-unlevered-fcf
  - https://auxocapitaladvisors.com/working-capital-peg-ev-to-equity-bridge/
  - https://www.mondaq.com/maprivate-equity/1372194/the-equity-bridge-from-enterprise-value-to-equity-value
  - https://365financialanalyst.com/knowledge-hub/credit-analysis/expected-loss-and-its-components-probability-of-default-loss-given-default-and-exposure-at-default/
  - https://en.wikipedia.org/wiki/Loss_given_default
related:
  - valorisation-distressed
  - restructuration-dette
  - quick-scan-diagnostic
---

# Modelisation financiere en M&A distressed -- Guide exhaustif

Ce document couvre l'ensemble des techniques de modelisation financiere specifiques au M&A distressed : DCF ajuste, waterfall analysis, recovery analysis, 13-week cash flow, bridge equity-to-EV, LBO distressed, NPL pricing, et le scoring model Brantham. Niveau expert, orientation praticien.

---

## 1. DCF ajuste pour situation distressed

### 1.1 Pourquoi le DCF classique echoue en distressed

Le DCF classique repose sur trois hypotheses qui sont violees en situation distressed :

1. **Continuite d'exploitation** : l'entreprise peut cesser d'exister. Le terminal value (50-80% de la valeur dans un DCF classique) n'a aucun sens si la probabilite de survie a 5 ans est de 40%.
2. **Cash-flows previsibles** : en restructuration, les cash-flows sont chaotiques. Un mois positif peut suivre un mois a -500K EUR.
3. **Taux d'actualisation stable** : le risque evolue dramatiquement dans le temps (tres eleve en phase aigue, decroissant si le retournement reussit).

### 1.2 WACC distressed : construction

Le WACC distressed differe fondamentalement du WACC classique :

**Formule WACC classique** :

WACC = (E / V) x Ke + (D / V) x Kd x (1 - t)

Ou :
- E = valeur de marche des capitaux propres
- D = valeur de marche de la dette
- V = E + D
- Ke = cout des capitaux propres
- Kd = cout de la dette
- t = taux d'imposition effectif

**Ajustements distressed** :

#### a) Cout des capitaux propres (Ke)

Ke = Rf + Beta_releve x ERP + SRP + DRP

Ou :
- Rf = taux sans risque (OAT 10 ans France, ~3.0-3.5% en 2025-2026)
- Beta_releve = beta ajuste pour le risque distressed
- ERP = Equity Risk Premium (prime de risque marche, ~5.5-6.5% pour la France)
- SRP = Small/Size Risk Premium (prime de taille, 3-8% pour les PME)
- DRP = Distress Risk Premium (prime de restructuration, 5-15%)

**Estimation du beta distressed** :

1. Identifier 5-10 comparables cotes (meme secteur)
2. Obtenir leur beta leve (observe sur 2-5 ans)
3. Deleverager : Beta_unlev = Beta_lev / (1 + (1 - t) x (D/E))
4. Calculer la mediane des betas deleverages
5. Releverager avec la structure de capital cible distressed :
   Beta_relev = Beta_unlev x (1 + (1 - t) x (D_distressed / E_distressed))

**En pratique** : pour une PME industrielle distressed en France, le beta releve est typiquement entre 2.0 et 3.5 (vs 0.8-1.2 pour une entreprise saine du meme secteur).

**Ke resultant** : generalement 20-35% pour une PME distressed (vs 8-12% saine).

#### b) Cout de la dette (Kd)

En distressed, le cout de la dette n'est pas le taux facial des emprunts existants. C'est le rendement observe (yield-to-maturity) sur la dette existante ou le taux que le marche exigerait pour preter :

- **Si dette cotee** : utiliser le YTM observe sur le marche secondaire
- **Si dette non cotee (PME)** : estimer via le spread de credit :
  - Kd = Rf + Spread de credit
  - Spread typique : 800-2000 bps pour du B/CCC, 2000-4000 bps pour du CC/D
- **Si dette en procedure** : utiliser le prix de marche de la dette (si echangee entre fonds NPL)

**Kd resultant** : typiquement 10-25% pour une PME distressed.

#### c) Ponderation (D/V et E/V)

En distressed, utiliser les valeurs de marche, pas les valeurs comptables :
- Si les capitaux propres sont negatifs au bilan -> E (marche) peut etre proche de zero
- Si la dette se negocie a 40 centimes/EUR -> D (marche) = 40% x D (nominale)
- Attention : structure de capital volatile. Certains praticiens utilisent une structure "cible" post-restructuration.

#### d) Bouclier fiscal

Le bouclier fiscal (Kd x (1 - t)) est theoriquement limite si l'entreprise ne paye pas d'impot (deficits reportables). En pratique :
- Si deficits reportables > 5 ans de resultat prevu -> ignorer le bouclier fiscal
- Si retour a la profitabilite prevu en 2-3 ans -> appliquer un bouclier fiscal partiel

**WACC distressed typique pour PME France** : 15-25% (vs 8-12% saine).

### 1.3 Terminal Value distressed

**Methode classique** : Gordon Growth Model -> TV = FCFn x (1 + g) / (WACC - g)

**Problemes en distressed** :
- g (taux de croissance perpetuel) n'a pas de sens si l'entreprise peut ne pas exister
- Le FCFn (derniere annee projetee) peut etre negatif
- L'horizon explicite est souvent trop court (3-5 ans vs 5-10 ans en classique)

**Approche ajustee : Probability-Weighted Terminal Value**

TV_ajuste = P(survie) x TV_going_concern + P(faillite) x Valeur_liquidative

Ou :
- P(survie) = probabilite que l'entreprise survive au-dela de l'horizon explicite
- TV_going_concern = terminal value classique (Gordon Growth ou Exit Multiple)
- P(faillite) = 1 - P(survie)
- Valeur_liquidative = valeur de liquidation actualisee des actifs

**Estimation de P(survie)** :
- Modeles statistiques (Altman Z-Score, Ohlson O-Score)
- Jugement expert base sur la qualite du plan de retournement
- Benchmarks sectoriels (taux de survie a 5 ans post-restructuration : 40-60% selon les secteurs)

### 1.4 Probability-Weighted Scenarios (PWDCF)

C'est l'approche recommandee en distressed. Au lieu d'un seul scenario DCF, on construit 3 a 5 scenarios ponderes :

| Scenario | Description | Poids | FCF | TV |
|----------|-------------|-------|-----|-----|
| **Upside** | Retournement reussi, croissance retrouvee | 15-20% | Projections optimistes | Going concern |
| **Base** | Stabilisation, rentabilite modeste | 40-50% | Projections centrales | Going concern reduit |
| **Downside** | Echec partiel, stagnation | 20-25% | Projections pessimistes | Exit multiple bas |
| **Liquidation** | Fermeture, vente des actifs | 10-20% | Zero apres fermeture | Valeur liquidative |
| **Deep crisis** | Procedure collective a nouveau | 5-10% | Zero | Valeur de casse |

**Valeur = Somme(Poids_i x VAN_i)**

**Exemple** :
- Upside : VAN = 8M, poids = 15% -> contribution = 1.2M
- Base : VAN = 4M, poids = 45% -> contribution = 1.8M
- Downside : VAN = 1.5M, poids = 25% -> contribution = 0.375M
- Liquidation : VAN = 0.5M, poids = 10% -> contribution = 0.05M
- Deep crisis : VAN = -0.2M, poids = 5% -> contribution = -0.01M

**Valeur probability-weighted = 3.415M EUR**

---

## 2. Waterfall analysis

### 2.1 Principe

La waterfall analysis (analyse en cascade) determine comment la valeur d'une entreprise est distribuee entre les differentes classes de creanciers selon leur rang de priorite. C'est l'outil central du restructuring pour negocier les recoveries.

### 2.2 Rang des creances en droit francais

En procedure collective francaise, l'ordre de priorite (simplifie) est :

| Rang | Creancier | Fondement |
|------|-----------|-----------|
| 1 | **Super-privilege des salaires** | Art. L.3253-2 Code du travail (60 derniers jours, plafond mensuel) |
| 2 | **Frais de justice** | Art. L.622-17 C.com (creances utiles a la procedure) |
| 3 | **Privilege de conciliation (new money)** | Art. L.611-11 C.com (apports frais dans le cadre d'une conciliation homologuee) |
| 4 | **AGS** (avances salaires) | Art. L.3253-6 Code du travail (subrogation dans super-privilege) |
| 5 | **Privilege de la procedure** | Art. L.622-17 C.com (creances posterieures utiles) |
| 6 | **Creances garanties par surete reelle speciale** | Hypotheque, nantissement, gage (selon rang d'inscription) |
| 7 | **Privilege general du Tresor public** | Art. 1929 quater CGI |
| 8 | **Privilege general URSSAF** | Art. L.243-4 CSS |
| 9 | **Privilege general des salaires** | Art. L.3253-3 Code du travail (6 derniers mois) |
| 10 | **Creanciers chirographaires** | Fournisseurs, obligataires non garantis, etc. |
| 11 | **Creanciers subordonnes** | Dette mezzanine, pret participatif |
| 12 | **Actionnaires** | En dernier ressort |

### 2.3 Construction du waterfall

**Etape 1** : Estimer la valeur totale disponible pour distribution (enterprise value ou produit de liquidation)

**Etape 2** : Lister toutes les creances par rang avec leur montant nominal

**Etape 3** : Distribuer la valeur en cascade :

```
Valeur disponible : 10M EUR

Rang 1 - Super-privilege salaires : 0.8M EUR
    Paiement : 0.8M (100%) | Reste : 9.2M

Rang 2 - Frais de justice : 0.3M EUR
    Paiement : 0.3M (100%) | Reste : 8.9M

Rang 3 - New money conciliation : 2.0M EUR
    Paiement : 2.0M (100%) | Reste : 6.9M

Rang 4 - AGS (subrogation) : 1.5M EUR
    Paiement : 1.5M (100%) | Reste : 5.4M

Rang 5 - Creances posterieures : 1.0M EUR
    Paiement : 1.0M (100%) | Reste : 4.4M

Rang 6 - Surete reelle (banque hypothecaire) : 3.0M EUR
    Paiement : 3.0M (100%) | Reste : 1.4M

Rang 7 - Tresor public : 1.2M EUR
    Paiement : 1.2M (100%) | Reste : 0.2M

Rang 8 - URSSAF : 0.8M EUR
    Paiement : 0.2M (25%) | Reste : 0.0M

Rang 9+ : 0 EUR disponible -> recovery = 0%
```

### 2.4 Break point analysis

Le **break point** (ou fulcrum security) est la tranche de dette dans laquelle la valeur disponible "s'arrete" — c'est-a-dire la classe qui est partiellement remboursee.

**Identification** : la tranche qui recoit un recovery entre 0% et 100%.

Dans l'exemple ci-dessus : le break point est l'URSSAF (rang 8) avec 25% de recovery.

**Importance strategique** :
- Les creanciers au-dessus du break point sont "in the money" -> ils seront integralement rembourses
- Les creanciers au break point sont la "fulcrum security" -> ils ont le plus d'influence dans la negociation
- Les creanciers en dessous du break point sont "out of the money" -> recovery nulle ou quasi-nulle

**Pour l'acquereur** : le break point determine qui a le pouvoir dans la negociation de la restructuration. Si la dette senior est au-dessus du break point, les banquiers seniors n'ont pas d'incitation a negocier (ils seront rembourses). Ce sont les creanciers au break point qui negocient le plus durement.

### 2.5 Simulation par scenario

Construire le waterfall sous 3 scenarios de valeur pour voir comment les recoveries evoluent :

| Classe | Nominal | Recovery (pessimiste 6M) | Recovery (base 10M) | Recovery (optimiste 15M) |
|--------|---------|-------------------------|---------------------|-------------------------|
| Super-privilege | 0.8M | 100% | 100% | 100% |
| Frais justice | 0.3M | 100% | 100% | 100% |
| New money | 2.0M | 100% | 100% | 100% |
| AGS | 1.5M | 100% | 100% | 100% |
| Post. utiles | 1.0M | 100% | 100% | 100% |
| Banque hyp. | 3.0M | 13% | 100% | 100% |
| Tresor | 1.2M | 0% | 100% | 100% |
| URSSAF | 0.8M | 0% | 25% | 100% |
| Salaires gen. | 0.5M | 0% | 0% | 100% |
| Chirographaires | 4.0M | 0% | 0% | 50% |
| Subordonnes | 1.0M | 0% | 0% | 0% |

---

## 3. Recovery analysis

### 3.1 Expected recovery rate par tranche

Le taux de recovery attendu est l'element central du pricing en distressed. Il depend de :

**Facteurs determinants** :
1. **Rang de la creance** : plus le rang est eleve, meilleur est le recovery
2. **Type de surete** : hypotheque immobiliere > nantissement fonds de commerce > chirographaire
3. **Type de procedure** : sauvegarde > RJ > LJ (taux de recovery decroissants)
4. **Secteur d'activite** : industrie avec actifs tangibles > services > tech
5. **Taille de l'entreprise** : les grandes entreprises ont de meilleurs recovery rates (plus d'actifs, plus de repreneurs potentiels)
6. **Juridiction** : la France a des recovery rates inférieurs a l'UK ou l'Allemagne pour les chirographaires

### 3.2 Benchmarks de recovery France

| Tranche | Recovery moyen (RJ) | Recovery moyen (LJ) |
|---------|---------------------|---------------------|
| Creances super-privilegiees | 95-100% | 90-100% |
| Creances hypothecaires | 60-85% | 40-70% |
| Creances nanties (fdc) | 30-60% | 15-40% |
| Tresor public | 20-50% | 5-20% |
| URSSAF | 15-40% | 5-15% |
| Chirographaires | 5-25% | 2-10% |
| Subordonnes | 0-5% | 0-2% |
| Actionnaires | 0% | 0% |

**Benchmark global** : le taux de recovery moyen tous creanciers confondus en France est d'environ 30-40% en RJ et 10-20% en LJ (source : Banque de France, etudes empiriques). La Banque Mondiale place la France autour de 75 centimes/EUR pour les procedures formelles de grandes entreprises, mais ce chiffre est biaise vers le haut.

### 3.3 Methodologie de calcul du recovery

**Approche asset-by-asset** (pour la liquidation) :

Pour chaque actif, appliquer une decote de liquidation :

| Actif | Valeur comptable nette | Decote liquidation | Valeur realisable |
|-------|----------------------|--------------------|--------------------|
| Immobilier | VNC | 20-40% | VNC x 0.60-0.80 |
| Machines/equipement | VNC | 40-70% | VNC x 0.30-0.60 |
| Stock MP/PF | VNC | 30-60% | VNC x 0.40-0.70 |
| Creances clients | VNC | 10-30% | VNC x 0.70-0.90 |
| Tresorerie | Nominale | 0% | 100% |
| Marque/brevets | VNC ou estime | 60-90% | VNC x 0.10-0.40 |
| Fonds de commerce | VNC | 50-80% | VNC x 0.20-0.50 |
| Goodwill | VNC | 100% | 0 |

**Total valeur liquidative** = Somme des valeurs realisables - Couts de liquidation (honoraires liquidateur 5-15%, frais de vente, conservation)

**Approche going-concern** (pour la reorganisation) :

Recovery = min(Creance nominale, Part de valeur attribuee dans le plan) / Creance nominale

### 3.4 Matrice de sensibilite

Construire une matrice recovery = f(valeur entreprise, rang) pour identifier les zones de negociation :

```
                    EV = 5M   EV = 8M   EV = 10M  EV = 12M  EV = 15M
Senior secured       100%      100%      100%      100%      100%
Mezzanine             0%       40%       80%      100%      100%
Chirographaires        0%        0%        0%       25%       63%
```

---

## 4. 13-week cash flow (TWCF) avance

### 4.1 Structure du modele

Le 13-Week Cash Flow (TWCF) est le modele de tresorerie a court terme le plus utilise en restructuration. Il couvre 13 semaines (~1 trimestre) avec un detail hebdomadaire.

**Architecture** :

```
SECTION 1 : ENCAISSEMENTS (RECEIPTS)
  Encaissements clients (par profil de paiement)
  Autres recettes d'exploitation
  Produits financiers
  Encaissements exceptionnels (cessions, subventions)
  = TOTAL ENCAISSEMENTS

SECTION 2 : DECAISSEMENTS (DISBURSEMENTS)
  Fournisseurs et sous-traitants
  Salaires et charges sociales
  Charges externes (loyers, assurances, energie)
  Impots et taxes
  TVA (decaissements nets)
  Interets et remboursement dette
  Capex (investissements)
  Autres decaissements
  = TOTAL DECAISSEMENTS

SECTION 3 : FLUX NET HEBDOMADAIRE
  = Total encaissements - Total decaissements

SECTION 4 : TRESORERIE
  Tresorerie debut de semaine
  + Flux net
  + Tirage / remboursement revolving
  = Tresorerie fin de semaine
  Lignes disponibles (non tirees)
  = Liquidite totale disponible
```

### 4.2 Regles de construction

**Encaissements clients** :
- Ne PAS projeter a partir du CA previsionnel (approche indirecte). Utiliser l'approche directe : analyser la balance agee clients et projeter les encaissements semaine par semaine.
- Classer les clients par profil :
  - Payeurs reguliers (delai moyen, faible dispersion)
  - Payeurs lents (delai moyen + 30j)
  - Payeurs a risque (probabilite de non-paiement > 20%)
- Haircut global sur les encaissements : 5-10% pour les imprevisibles

**Decaissements fournisseurs** :
- Partir des commandes en cours et des engagements connus
- Distinguer :
  - Fournisseurs strategiques (on les paye en priorite pour maintenir l'approvisionnement)
  - Fournisseurs reportables (paiement decalable de 1-2 semaines)
  - Fournisseurs compressibles (negociation possible)

**Salaires et charges** :
- Calendrier precis : salaires fin de mois, charges le 15 du mois suivant
- Inclure primes, conges payes, 13eme mois si applicable

**TVA** :
- Regime reel mensuel ou trimestriel
- Attention aux credits de TVA (remboursables mais avec delai de 3-6 mois)

### 4.3 Cash sweeps et revolving

**Cash sweep** : mecanisme par lequel l'excedent de tresorerie au-dela d'un seuil minimum est automatiquement affecte au remboursement de la dette.

Modele :
```
Si Tresorerie_fin > Seuil_minimum :
    Cash_sweep = Tresorerie_fin - Seuil_minimum
    Remboursement_anticipee += Cash_sweep
    Tresorerie_fin = Seuil_minimum
```

**Revolving facility** :
- Ligne de credit tiree/remboursee au besoin pour lisser la tresorerie
- Modele :
```
Si Tresorerie_fin < Seuil_minimum :
    Tirage = min(Seuil_minimum - Tresorerie_fin, Revolving_disponible)
    Revolving_utilise += Tirage
Si Tresorerie_fin > Seuil_confort ET Revolving_utilise > 0 :
    Remboursement = min(Tresorerie_fin - Seuil_confort, Revolving_utilise)
    Revolving_utilise -= Remboursement
```

### 4.4 Covenant compliance

Integrer dans le TWCF le suivi des covenants bancaires :

| Covenant | Definition | Seuil | Formule de suivi |
|----------|-----------|-------|-----------------|
| **Minimum cash** | Tresorerie minimale | Ex: 500K | Tresorerie_fin >= 500K |
| **Maximum leverage** | Dette nette / EBITDA | Ex: < 4.0x | (Dette brute - Cash) / EBITDA_12m |
| **Minimum DSCR** | Debt Service Coverage Ratio | Ex: > 1.2x | Cash-flow dispo / Service de la dette |
| **Capex cap** | Plafond d'investissement | Ex: < 1M/an | Cumul capex annuel |
| **Interest coverage** | Couverture des interets | Ex: > 2.0x | EBITDA / Charges d'interet |

**Alerte automatique** : si le TWCF projette un breach de covenant dans les 4-6 prochaines semaines, notification immediate pour demander un waiver ou renogocier.

### 4.5 Stress testing

Appliquer des stress tests au TWCF pour tester la resilience :

| Stress | Description | Impact |
|--------|-------------|--------|
| **Retard encaissements** | Decalage de 2 semaines sur 30% des clients | Tresorerie minimum atteinte ? |
| **Perte client majeur** | Le top client (15% CA) ne paye plus | Breach covenant ? |
| **Hausse cout matiere** | +15% sur achats MP | Semaine de rupture ? |
| **Retrait ligne bancaire** | Revolving annulee | Nombre de semaines de survie ? |
| **Combine** | Retard encaissements + hausse MP | Semaines avant cessation paiements ? |

**Metric cle** : le "cash runway" = nombre de semaines avant que la tresorerie atteigne zero sous chaque scenario de stress.

---

## 5. Bridge equity-to-EV distressed

### 5.1 Formule standard

Enterprise Value = Equity Value + Dette nette + Minoritaires + Actions preferentielles

Ou :

Equity Value = Enterprise Value - Dette nette - Minoritaires - Actions preferentielles

Avec :

Dette nette = Dette financiere brute - Tresorerie et equivalents

### 5.2 Ajustements specifiques distressed

En M&A distressed, le bridge standard necessite de nombreux ajustements supplementaires :

#### a) Dette financiere brute (ajustee)

Inclure dans la dette financiere :
- Emprunts bancaires (CT + LT)
- Obligations et emprunts obligataires
- Credit-bail / leasing financier (capitalise IFRS 16)
- Comptes courants d'associes remboursables
- Dettes fournisseurs echues et non payees (= dette implicite)
- Interets courus non payes
- Penalites et majorations de retard (URSSAF, Tresor)

**Specifique distressed** :
- Valoriser la dette a sa valeur de marche si elle se negocie avec decote (ex: dette a 40 centimes -> valeur = 40% du nominal)
- Inclure les penalites de remboursement anticipe si elles s'appliquent
- Ajouter le cout de sortie des contrats onéreux (baux non rentables, contrats d'approvisionnement au-dessus du marche)

#### b) Provisions (ajustees)

| Type de provision | Traitement |
|-------------------|-----------|
| Provision pour restructuration | Ajouter a la dette nette (decaissement certain) |
| Provision pour litiges | Estimer la probabilite et le montant -> ajouter en debt-like |
| Provision pour garantie donnee | Evaluer le risque d'appel -> ajouter si probable |
| Provision pour remise en etat | Ajouter integralement (obligation legale) |
| Provision retraites / IDR | Ajouter le deficit actualise (ecart entre obligation et actifs du fonds) |
| Provision pour pertes a terminaison | Ajouter en dette nette |

#### c) Contingent liabilities (passifs eventuels)

Les passifs eventuels ne figurent pas au bilan mais peuvent avoir un impact significatif :

- Litiges en cours (prudhommes, contentieux commercial, fiscal)
- Garanties de passif donnees a des acquereurs precedents
- Cautions et avals
- Responsabilite environnementale (depollution)
- Risque fiscal (redressement en cours ou probable)
- Risque social (requalification de contrats, travail dissimule)

**Approche** : pour chaque contingent, estimer Probabilite x Montant et l'ajouter en ajustement debt-like.

#### d) BFR normatif

Le BFR normatif est le niveau de BFR necessaire pour faire tourner l'activite a son niveau "normal" :

BFR normatif = (Stocks normatifs + Creances clients normatives + Autres creances) - (Dettes fournisseurs normatives + Autres dettes d'exploitation)

**Ajustement** :

Ajustement BFR = BFR reel (a la date de closing) - BFR normatif

- Si BFR reel > BFR normatif : l'acquereur a trop de BFR -> ajustement positif (credit pour l'acquereur)
- Si BFR reel < BFR normatif : l'acquereur devra injecter du cash pour reconstituer le BFR -> ajustement negatif

**En distressed** : le BFR est quasi-systematiquement sous son niveau normatif (stocks epuises, fournisseurs au comptant, creances clients deteriorees). L'ajustement BFR est donc presque toujours negatif et significatif.

**Estimation** : BFR normatif = 15-25% du CA pour l'industrie, 5-15% pour les services, 25-35% pour le commerce.

#### e) Tresorerie (ajustee)

Ne pas prendre le solde bancaire au bilan. Ajuster pour :
- Cash trap : tresorerie bloquee (nantie, a l'etranger, sur des comptes restreints)
- Cheques emis non debites
- Tresorerie minimale operationnelle (incompressible pour faire tourner l'activite)
- Decouverts bancaires (a reclasser en dette financiere)

**Tresorerie nette ajustee** = Cash brut - Cash trap - Cash minimum operationnel - Cheques emis non debites

### 5.3 Tableau recapitulatif du bridge

```
Enterprise Value (issu du DCF ou des multiples)        12,000K
- Dette bancaire (valeur marche)                        -4,500K
- Credit-bail capitalise                                  -800K
- Comptes courants d'associes                             -300K
- Dettes sociales/fiscales echues                         -600K
- Provision restructuration                               -400K
- Provision litiges (prob-weighted)                       -250K
- Deficit retraite                                        -150K
- Contingent liabilities (prob-weighted)                  -200K
+ Tresorerie nette ajustee                               +1,200K
- Ajustement BFR (BFR reel < normatif)                    -800K
- Cout de sortie contrats onereux                         -300K
= EQUITY VALUE                                           4,900K
```

---

## 6. LBO distressed

### 6.1 Specificites du LBO distressed

Le LBO distressed differe du LBO classique sur plusieurs points :

| Dimension | LBO classique | LBO distressed |
|-----------|--------------|----------------|
| **Cible** | Entreprise saine, cash-flows stables | Entreprise en difficulte, cash-flows incertains |
| **Levier** | 3-6x EBITDA | 1-3x EBITDA (si EBITDA positif) |
| **Prix d'entree** | 6-10x EBITDA | 2-4x EBITDA (voire achat pour 1 EUR symbolique) |
| **Source de rendement** | Desendettement + croissance + expansion multiple | Retournement operationnel + restructuration dette |
| **Equity check** | 30-50% du prix | 50-100% (moins de dette disponible) |
| **Duration** | 3-5 ans | 5-7 ans (retournement + croissance) |
| **Risque** | Modere | Tres eleve |
| **Rendement cible** | IRR 15-25% | IRR 25-50% (pour compenser le risque) |

### 6.2 Acquisition de dette decotee (loan-to-own)

Strategie ou un fonds achete la dette d'une entreprise en difficulte sur le marche secondaire a un prix decote, puis convertit cette dette en equity pour prendre le controle :

**Mecanique** :
1. La dette nominale de 10M EUR se negocie a 40 centimes (prix marche = 4M EUR)
2. Le fonds achete pour 4M EUR de dette nominale
3. En procedure (ou dans le cadre d'un accord amiable), la dette est convertie en equity via un debt-equity swap
4. Le fonds detient 100% des actions pour 4M EUR

**Rendement** :
- Si l'entreprise vaut 8M EUR post-retournement : IRR = (8/4)^(1/3) - 1 = 26% sur 3 ans
- Si l'entreprise vaut 15M EUR post-retournement : IRR = (15/4)^(1/5) - 1 = 30% sur 5 ans

**Risques** :
- L'entreprise vaut moins que la dette achetee -> perte
- Les creanciers prioritaires absorbent toute la valeur -> recovery zero
- La conversion en equity est contestee par d'autres creanciers ou le tribunal

### 6.3 Equity check et structure de financement

**Sources de financement en LBO distressed** :

| Source | Montant typique | Cout | Conditions |
|--------|----------------|------|-----------|
| Equity sponsor | 40-70% du prix | IRR cible 25-50% | Capital a risque |
| Dette senior (nouvelle) | 20-40% | 6-12% | Suretees de premier rang |
| Mezzanine / PIK | 0-20% | 12-18% (cash + PIK) | Subordonnee |
| Vendor note | 0-30% | Variable | Paiement differe au vendeur |
| Earn-out | 0-20% | Performance-based | Conditionne aux resultats |

**Specificite France** : en plan de cession (L.642-1+ C.com), le prix est fixe par le tribunal. Le repreneur paye en cash. Pas de leverage sur l'acquisition elle-meme. Le LBO distressed se structure differemment :
- Le repreneur cree une holding (NewCo)
- NewCo leve de la dette (adossee aux actifs repris ou aux cash-flows futurs)
- NewCo acquiert les actifs via le plan de cession
- Le levier est dans NewCo, pas dans la cible

### 6.4 Modele de rendement

**IRR (Internal Rate of Return)** :

IRR = taux r tel que : Somme_t (CF_t / (1+r)^t) = 0

Ou CF_0 = -Equity investi et CF_T = Equity value a la sortie + dividendes recus

**Money-on-Money (MoM)** :

MoM = (Valeur totale recue) / (Equity investie)

**Exemple modele LBO distressed** :

```
HYPOTHESES
  Prix d'acquisition             : 3,000K (4x EBITDA normatif de 750K)
  Equity                         : 2,000K (67%)
  Dette senior                   : 1,000K (33%, 7%, amortissable 5 ans)
  Horizon                        : 5 ans
  EBITDA annee 1                 : 400K (phase de retournement)
  EBITDA annee 2                 : 700K (stabilisation)
  EBITDA annee 3                 : 900K (croissance)
  EBITDA annee 4                 : 1,100K
  EBITDA annee 5                 : 1,200K
  Multiple de sortie             : 5x EBITDA
  Capex maintenance              : 200K/an
  Variation BFR                  : -100K A1, -50K A2, 0 apres

CALCUL RENDEMENT
  EV sortie = 1,200K x 5 = 6,000K
  Dette residuelle a 5 ans       : 0K (amortie)
  Equity value sortie            : 6,000K - 0 = 6,000K

  MoM = 6,000 / 2,000 = 3.0x
  IRR = (3.0)^(1/5) - 1 = 24.6% (simplifie, hors dividendes intermediaires)
```

### 6.5 Debt capacity analysis

Evaluer la capacite d'endettement de la cible post-acquisition :

**DSCR (Debt Service Coverage Ratio)** :
DSCR = Cash-flow disponible / Service de la dette (principal + interets)
- Minimum requis : 1.2x (tolerance en distressed : 1.0x les 2 premieres annees)

**Leverage ratio** :
Leverage = Dette nette / EBITDA
- Maximum prudent en distressed : 2-3x EBITDA normatif

**Interest coverage** :
ICR = EBITDA / Charges d'interets
- Minimum requis : 2.0x (tolerance en distressed : 1.5x)

**Regle empirique** : en LBO distressed PME France, la dette maximale prudente = 2x l'EBITDA normatif post-retournement. Au-dela, le risque de re-default est trop eleve.

---

## 7. NPL pricing

### 7.1 Framework Expected Loss

Le pricing de Non-Performing Loans (NPL / creances douteuses) repose sur le framework Expected Loss :

**Formule fondamentale** :

Expected Loss (EL) = PD x LGD x EAD

Ou :
- **PD** (Probability of Default) : probabilite que le debiteur fasse defaut dans un horizon donne
- **LGD** (Loss Given Default) : part de l'exposition perdue en cas de defaut (= 1 - Recovery Rate)
- **EAD** (Exposure At Default) : montant total expose au moment du defaut

### 7.2 Composantes detaillees

#### a) Probability of Default (PD)

**Estimation** :

Pour un portefeuille NPL, la PD est souvent = 100% (les creances sont deja en defaut). La question devient : quelle est la probabilite de cure (retour a performing) ?

P(cure) = 1 - PD_residuelle

Facteurs influencant le cure rate :
- Type de debiteur (entreprise vs particulier)
- Anciennete du defaut (plus c'est vieux, moins le cure rate est eleve)
- Presence de suretes
- Secteur d'activite
- Juridiction et efficacite des tribunaux

**Benchmarks cure rate France** :
- NPL < 6 mois : cure rate 15-25%
- NPL 6-12 mois : cure rate 5-15%
- NPL > 12 mois : cure rate 2-8%
- NPL en procedure collective : cure rate ~0% (mais recovery via dividende)

#### b) Loss Given Default (LGD)

LGD = 1 - Recovery Rate

**Facteurs determinants** :
- Type de surete (immobilier > equipement > rien)
- Ratio LTV (Loan-to-Value) au moment du defaut
- Juridiction (efficacite du recouvrement)
- Couts de recouvrement (honoraires, frais judiciaires)
- Temps de resolution (actualisation)

**Formule detaillee** :

LGD = 1 - [(Valeur recouvree actualisee - Couts de recouvrement) / EAD]

**Benchmarks LGD France (NPL corporate)** :
| Type de surete | LGD moyen | Recovery moyen |
|---------------|-----------|----------------|
| Hypotheque immobiliere | 25-40% | 60-75% |
| Nantissement fonds de commerce | 50-70% | 30-50% |
| Caution personnelle | 60-80% | 20-40% |
| Chirographaire | 70-90% | 10-30% |
| Subordonnee | 85-100% | 0-15% |

#### c) Exposure At Default (EAD)

EAD = Principal outstanding + Interets courus + Penalites + Facilites non tirees x CCF

Ou CCF = Credit Conversion Factor (probabilite de tirage des lignes non utilisees avant defaut).

Pour les NPL : EAD = solde total de la creance (principal + interets + penalites).

### 7.3 Pricing d'un portefeuille NPL

**Methode 1 : Static Pool Analysis**

Analyser les performances historiques de portefeuilles similaires :

1. Prendre un portefeuille NPL historique similaire (meme profil de debiteurs, memes suretes)
2. Observer les cash-flows de recouvrement reels sur 3-7 ans
3. Construire une courbe de recovery cumulative
4. Appliquer cette courbe au portefeuille a pricer
5. Actualiser les cash-flows projetes au taux de rendement cible

**Methode 2 : DCF Granulaire**

Pour chaque creance du portefeuille :

1. Estimer le recovery attendu (montant et timing)
2. Appliquer un taux d'actualisation :
   - Taux de rendement cible du fonds NPL : 12-25% selon le risque
   - Inclut la prime de liquidite, le risque operationnel de recouvrement, et le cout de portage
3. Calculer la VAN
4. Prix = Somme des VAN

**Methode 3 : Monte Carlo**

Pour les gros portefeuilles (>100 creances) :

1. Pour chaque creance, definir des distributions de probabilite pour :
   - Le montant de recovery (distribution beta ou triangulaire)
   - Le timing de recovery (distribution exponentielle ou Weibull)
2. Simuler N iterations (10 000+)
3. Obtenir la distribution des cash-flows du portefeuille
4. Calculer la VAN a differents percentiles

**Prix typiques** :

| Type de portefeuille NPL | Prix (% du nominal) | Recovery attendu | Rendement implicite |
|--------------------------|--------------------|-----------------|--------------------|
| NPL corporate garanti (immo) | 30-50% | 50-70% | 12-18% |
| NPL corporate garanti (autre) | 15-30% | 25-45% | 15-22% |
| NPL corporate chirographaire | 3-15% | 8-25% | 18-30% |
| NPL retail garanti (immo) | 40-60% | 55-75% | 10-15% |
| NPL retail non garanti | 1-5% | 5-15% | 20-35% |

### 7.4 Recovery curves

Les recovery curves montrent le pourcentage cumule de recouvrement en fonction du temps depuis l'acquisition :

```
Annee | Recovery cumule (garanti) | Recovery cumule (chirographaire)
  0   |         0%                |          0%
  1   |        25%                |         15%
  2   |        50%                |         30%
  3   |        70%                |         45%
  4   |        80%                |         55%
  5   |        88%                |         62%
  6   |        93%                |         66%
  7   |        95%                |         68%
```

**J-curve** : les cash-flows de recovery sont concentres sur les 2-3 premieres annees (les cas les plus faciles sont resolus en premier). La queue de distribution (annees 4+) contient les cas contentieux longs.

---

## 8. Scoring model Brantham

### 8.1 Architecture du scoring

Le scoring model Brantham integre les differentes analyses financieres dans un score global de deal :

**Score global = Somme(Poids_i x Score_i) pour i = 1..N composantes**

Chaque composante est notee de 1 (tres defavorable) a 5 (tres favorable).

### 8.2 Composantes et ponderations

| # | Composante | Poids | Source modele |
|---|------------|-------|---------------|
| 1 | Valeur d'actifs (liquidative) | 15% | Recovery analysis |
| 2 | Potentiel retournement (DCF PWDCF) | 20% | DCF ajuste distressed |
| 3 | Structure de la dette (waterfall) | 10% | Waterfall analysis |
| 4 | Capacite de desendettement | 10% | Debt capacity, DSCR |
| 5 | Solidite du BFR et tresorerie | 15% | 13-week CF, bridge |
| 6 | Risque fournisseur / assurance-credit | 10% | cf. assurance-credit.md |
| 7 | Qualite des actifs (tangibilite) | 5% | Asset-by-asset |
| 8 | Risque juridique | 10% | Contingent liabilities |
| 9 | Marche et positionnement | 5% | Analyse sectorielle |

### 8.3 Seuils de decision

| Score global | Decision |
|-------------|----------|
| 4.0 - 5.0 | **Go** : deal attractif, poursuivre la DD complete |
| 3.0 - 3.9 | **Go conditionnel** : deal potentiel mais risques a mitiger |
| 2.0 - 2.9 | **Watch** : risques significatifs, besoin de clarification majeure |
| 1.0 - 1.9 | **No-go** : risques excessifs, passer |

**Red flags eliminatoires** (no-go automatique quel que soit le score) :
- Passifs environnementaux non bornes
- Fraude averee non sanctionnee
- Actifs principaux non cessibles (bail personnel du dirigeant, licence intuitu personae)
- EBITDA normatif negatif sans plan de retournement credible
- Risque fournisseur extreme (voir assurance-credit.md, seuil eliminatoire)

### 8.4 Integration dans le workflow

```
Quick scan (24-48h)
    |
    v
Score rapide (composantes 1, 5, 6, 7, 9)
    |
    v
Si score rapide >= 2.5 -> DD approfondie
    |
    v
Score complet (toutes composantes)
    |
    v
Decision Go / No-go / Conditionnel
    |
    v
Si Go -> Offre de reprise (structuration)
```

---

## 9. Outils et templates

### 9.1 Excel / Spreadsheet

**Templates essentiels** :

| Template | Contenu | Usage |
|----------|---------|-------|
| TWCF_template.xlsx | 13-week cash flow + stress tests | Tresorerie court terme |
| Waterfall_template.xlsx | Distribution creanciers + sensibilite | Negociation restructuration |
| DCF_distressed.xlsx | PWDCF 5 scenarios + bridge EV-Equity | Valorisation |
| LBO_model.xlsx | Sources & uses, returns, debt schedule | Structuration acquisition |
| Scoring_Brantham.xlsx | Score multi-criteres + red flags | Decision pipeline |

### 9.2 Python / pandas

**Modules utiles** :

```python
# 13-week cash flow automatise
import pandas as pd
import numpy as np

def build_twcf(receipts_schedule, disbursements_schedule,
               opening_cash, revolving_limit, min_cash):
    """
    Build 13-week cash flow model.

    Parameters:
    - receipts_schedule: pd.DataFrame with weekly receipts by category
    - disbursements_schedule: pd.DataFrame with weekly disbursements
    - opening_cash: float, cash at start of week 1
    - revolving_limit: float, max revolving facility
    - min_cash: float, minimum cash threshold
    """
    weeks = range(1, 14)
    results = []

    cash = opening_cash
    revolving_used = 0

    for w in weeks:
        total_receipts = receipts_schedule.loc[w].sum()
        total_disbursements = disbursements_schedule.loc[w].sum()
        net_flow = total_receipts - total_disbursements
        cash_before_revolving = cash + net_flow

        # Revolving logic
        if cash_before_revolving < min_cash:
            draw = min(min_cash - cash_before_revolving,
                       revolving_limit - revolving_used)
            revolving_used += draw
            cash = cash_before_revolving + draw
        elif cash_before_revolving > min_cash * 2 and revolving_used > 0:
            repay = min(cash_before_revolving - min_cash * 2, revolving_used)
            revolving_used -= repay
            cash = cash_before_revolving - repay
        else:
            cash = cash_before_revolving

        results.append({
            'week': w,
            'receipts': total_receipts,
            'disbursements': total_disbursements,
            'net_flow': net_flow,
            'revolving_used': revolving_used,
            'closing_cash': cash,
            'liquidity': cash + (revolving_limit - revolving_used)
        })

    return pd.DataFrame(results)
```

```python
# Waterfall analysis
def waterfall(enterprise_value, claims):
    """
    Distribute value through creditor waterfall.

    Parameters:
    - enterprise_value: float, total value available
    - claims: list of dicts with 'name', 'amount', 'rank' (1=highest)
    """
    sorted_claims = sorted(claims, key=lambda x: x['rank'])
    remaining = enterprise_value
    results = []

    for claim in sorted_claims:
        payment = min(claim['amount'], remaining)
        recovery = payment / claim['amount'] if claim['amount'] > 0 else 0
        remaining -= payment
        results.append({
            'name': claim['name'],
            'rank': claim['rank'],
            'nominal': claim['amount'],
            'payment': payment,
            'recovery_pct': recovery * 100,
            'remaining_value': remaining
        })

    return pd.DataFrame(results)
```

```python
# Monte Carlo NPL pricing
def price_npl_portfolio(loans, n_simulations=10000, discount_rate=0.15,
                        horizon=5):
    """
    Monte Carlo pricing for NPL portfolio.

    Parameters:
    - loans: list of dicts with 'ead', 'recovery_mean', 'recovery_std',
             'time_mean', 'time_std', 'secured'
    - n_simulations: int
    - discount_rate: float, annual
    - horizon: int, years
    """
    portfolio_values = []

    for _ in range(n_simulations):
        total_pv = 0
        for loan in loans:
            # Recovery amount (beta distribution)
            recovery_pct = np.clip(
                np.random.normal(loan['recovery_mean'],
                                 loan['recovery_std']),
                0, 1
            )
            recovery_amount = loan['ead'] * recovery_pct

            # Recovery timing (exponential)
            recovery_time = np.clip(
                np.random.exponential(loan['time_mean']),
                0.5, horizon
            )

            # PV of recovery
            pv = recovery_amount / (1 + discount_rate) ** recovery_time
            total_pv += pv

        portfolio_values.append(total_pv)

    return {
        'mean_value': np.mean(portfolio_values),
        'median_value': np.median(portfolio_values),
        'p5': np.percentile(portfolio_values, 5),
        'p25': np.percentile(portfolio_values, 25),
        'p75': np.percentile(portfolio_values, 75),
        'p95': np.percentile(portfolio_values, 95),
        'std': np.std(portfolio_values)
    }
```

### 9.3 Ratios cles — aide-memoire

| Ratio | Formule | Seuil sain | Seuil distressed | Interpretation |
|-------|---------|-----------|-------------------|---------------|
| **DSCR** | CF dispo / Service dette | > 1.5x | > 1.0x | Capacite a rembourser |
| **ICR** | EBITDA / Charges interet | > 3.0x | > 1.5x | Couverture des interets |
| **Leverage** | Dette nette / EBITDA | < 3.0x | < 5.0x | Endettement relatif |
| **Current ratio** | Actif CT / Passif CT | > 1.5 | > 0.8 | Liquidite court terme |
| **Quick ratio** | (Cash + Creances) / Passif CT | > 1.0 | > 0.5 | Liquidite immediate |
| **BFR / CA** | BFR / CA annuel | 10-20% | Variable | Intensite BFR |
| **DSO** | Creances clients / CA x 365 | 30-60j | Variable | Delai encaissement |
| **DPO** | Dettes fournisseurs / Achats x 365 | 30-60j | Variable | Delai paiement |
| **DIO** | Stocks / COGS x 365 | 30-90j | Variable | Rotation stocks |
| **Cash conversion** | DSO + DIO - DPO | < 60j | Variable | Cycle de tresorerie |
| **EBITDA margin** | EBITDA / CA | > 10% | > 5% | Rentabilite operationnelle |
| **FCF yield** | FCF / EV | > 5% | > 10% | Rendement cash |
| **Altman Z-Score** | 1.2A + 1.4B + 3.3C + 0.6D + 1.0E | > 2.99 | < 1.81 | Risque de faillite |

**Altman Z-Score detaille** :
- A = Working Capital / Total Assets
- B = Retained Earnings / Total Assets
- C = EBIT / Total Assets
- D = Market Value Equity / Total Liabilities
- E = Sales / Total Assets

Zone grise : 1.81 < Z < 2.99. En distressed : Z < 1.81 est quasi-systematique.

---

## 10. Workflow de modelisation par type de deal

### 10.1 Plan de cession en LJ (cas le plus frequent Brantham)

```
Etape 1 : Quick scan financier (24-48h)
  - Ratios cles sur 3 derniers exercices
  - Altman Z-Score
  - Estimation flash de la valeur liquidative
  -> Score rapide : go/no-go/conditionnel

Etape 2 : 13-week CF (si go)
  - Construire le TWCF a partir de la balance agee
  - Identifier le cash runway
  - Estimer les besoins de tresorerie post-reprise

Etape 3 : Valorisation (DCF PWDCF)
  - Construire le BP retournement (5 scenarios)
  - Calculer le WACC distressed
  - Determiner la fourchette de valeur probability-weighted

Etape 4 : Waterfall analysis
  - Lister toutes les creances par rang
  - Distribuer la valeur sous 3 scenarios
  - Identifier le fulcrum security

Etape 5 : Bridge EV-to-Equity
  - Ajustements distressed complets
  - Determiner l'equity value residuelle
  - Chiffrer le BFR de redemarrage

Etape 6 : Structuration de l'offre
  - Prix propose = Equity value x decote negociation (10-30%)
  - Sources de financement (equity, dette, vendor note)
  - Engagements emploi et investissement
  -> Depot de l'offre
```

### 10.2 Rachat de dette en conciliation

```
Etape 1 : Identification de l'opportunite
  - Dette cotee ou echangee (marche secondaire)
  - Prix de marche vs valeur nominale
  - Estimation du recovery attendu

Etape 2 : Waterfall + Recovery analysis
  - Rang de la dette ciblee
  - Scenarios de recovery sous differents outcomes
  - Break point analysis

Etape 3 : NPL pricing
  - EL = PD x LGD x EAD
  - DCF granulaire sur les cash-flows de recovery
  - Prix maximum = VAN des recoveries au taux de rendement cible

Etape 4 : Strategie
  - Loan-to-own : convertir en equity via DES dans le plan
  - Hold and collect : conserver la dette et encaisser les dividendes du plan
  - Flip : revendre la dette a un prix superieur apres stabilisation
  -> Decision basee sur le MoM et l'IRR selon chaque strategie
```

### 10.3 Acquisition d'un portefeuille NPL

```
Etape 1 : Screening du portefeuille
  - Composition (garanti/chirographaire, secteur, taille, anciennete)
  - Quality tape : donnees disponibles par creance

Etape 2 : Stratification
  - Segmenter par profil de recovery (garanti/non garanti, taille, anciennete defaut)
  - Appliquer des benchmarks de recovery par segment

Etape 3 : Pricing
  - Static pool analysis (historique de portefeuilles similaires)
  - DCF granulaire (pour les grosses creances > 500K)
  - Monte Carlo (pour le portefeuille agrege)
  - Stress tests (recovery -20%, timing +12 mois)

Etape 4 : Offre
  - Prix = VAN des recoveries au taux cible (15-25%)
  - Marge de securite : prix offert = 80-90% de la VAN calculee
  - Structure : paiement initial + earn-out lie aux recoveries reelles
  -> Bid competitif ou negociation bilaterale avec la banque vendeuse
```

### 10.4 Reprise de PME industrielle en RJ (plan de continuation ou cession partielle)

```
Etape 1 : Diagnostic operationnel
  - EBITDA normalise (retraitements : salaire dirigeant, cout exceptionnel, one-off)
  - Identification des branches rentables vs deficitaires
  - Estimation du BFR normatif par branche

Etape 2 : Modelisation financiere
  - BP retournement 5 ans (scenarios) :
    - Arret des branches deficitaires
    - Restructuration des couts fixes
    - Plan de relance commercial
  - 13-week CF pour la phase de transition
  - DCF PWDCF sur le perimetre retenu

Etape 3 : Structuration
  - Plan de continuation : proposition de dividendes aux creanciers (8-10 ans max)
  - Cession partielle : acquisition des branches rentables
  - LBO distressed : financement de l'acquisition

Etape 4 : Scoring Brantham
  - Score complet toutes composantes
  - Decision formelle documentee

Etape 5 : Execution
  - Offre de reprise ou proposition de plan
  - Negociation avec les creanciers (classes de parties affectees si SFA)
  - Audience tribunal
  -> Jugement homologation
```

---

## Glossaire

| Terme | Definition |
|-------|-----------|
| **Beta** | Mesure du risque systematique d'un actif par rapport au marche |
| **Break point** | Tranche de dette ou la valeur disponible s'epuise (fulcrum security) |
| **Cash runway** | Nombre de semaines/mois avant epuisement de la tresorerie |
| **Cash sweep** | Affectation automatique de l'excedent de tresorerie au remboursement |
| **CCF** | Credit Conversion Factor (probabilite de tirage d'une ligne non utilisee) |
| **Cure rate** | Probabilite qu'un NPL redevienne performing |
| **DES** | Debt-Equity Swap (conversion de dette en capital) |
| **DIP financing** | Debtor-In-Possession financing (financement en procedure) |
| **DSCR** | Debt Service Coverage Ratio |
| **EAD** | Exposure At Default |
| **ERP** | Equity Risk Premium |
| **EV** | Enterprise Value |
| **FCF** | Free Cash Flow |
| **Fulcrum security** | Tranche de dette partiellement remboursee dans le waterfall |
| **ICR** | Interest Coverage Ratio |
| **IRR** | Internal Rate of Return (taux de rendement interne) |
| **LGD** | Loss Given Default |
| **Loan-to-own** | Strategie d'achat de dette pour prendre le controle |
| **MoM** | Money-on-Money (multiple de rendement) |
| **NPL** | Non-Performing Loan (creance douteuse) |
| **PD** | Probability of Default |
| **PIK** | Payment-In-Kind (interets capitalises) |
| **PWDCF** | Probability-Weighted DCF |
| **SRP** | Size Risk Premium (prime de taille) |
| **TWCF** | Thirteen-Week Cash Flow |
| **WACC** | Weighted Average Cost of Capital |
| **YTM** | Yield-To-Maturity (rendement a maturite) |
| **Z-Score** | Score d'Altman pour la prediction de faillite |

---

## Voir aussi

- [[valorisation-distressed]] — Methodes de valorisation et multiples distressed
- [[restructuration-dette]] — Techniques de restructuration et pricing de la dette
- [[rang-des-creances]] — Ordre de priorite pour la waterfall analysis
- [[due-diligence-distressed]] — Construction du 13-week cash flow en DD
- [[comptabilite-crise]] — Comptes en procedure et valeur liquidative
- [[quick-scan-diagnostic]] — Diagnostic rapide et scoring
- [[turnaround-operationnel]] — Business plan de retournement et KPIs
- [[structuration-offres-reprise]] — Determination du prix dans l'offre
- [[glossaire-distressed]] — Terminologie M&A distressed
