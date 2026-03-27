---
type: knowledge
project: brantham
category: finance
topic: restructuration de dette et financement en crise
level: avance
updated: 2026-03-26
sources:
  - https://www.daf-mag.fr/Thematique/fonction-finance-1242/gouvernance-strategie-2125/Breves/restructurer-dette-financiere-cadre-amiable-474898.htm
  - https://iclg.com/practice-areas/restructuring-and-insolvency-laws-and-regulations/france
  - https://www.legal500.com/guides/chapter/france-restructuring-insolvency/
  - https://cms.law/en/int/expert-guides/cms-expert-guide-to-restructuring-and-insolvency-law/france
  - https://www.whitecase.com/insight-alert/amendment-french-restructuring-and-insolvency-laws-new-balance-between-stakeholders
  - https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044052555
  - https://www.varoclier-avocats.com/privilege-de-conciliation-new-money/
  - https://readingsphere.com/le-privilege-de-new-money-dans-une-procedure-de-conciliation/
  - https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044052591
  - https://ideolegis.com/ideoblocs/47/creances-convertibles-en-capital-debt-equity-swap
  - https://expertfiscal.fr/augmentation-capital-conversion-de-creances-guide/
  - https://www.banque-france.fr/system/files/2024-04/823415-Fiche-431.pdf
  - https://www.vernimmen.net/ftp/Chapitre_50.pdf
  - https://www.cf-2c.fr/blog/ceder-npl-banque/
  - https://www.moneysmart.fr/p/la-france-nouvelle-frontiere-du-marche-des-creances-douteuses
  - https://www.affacturage.fr/guide/affacturage-restructuring/
  - https://www.affacturage.fr/lease-back/
  - https://www.factor.bpce.fr/informations/laffacturage-une-solution-pertinente-en-periode-de-restructuring-financier/
  - https://www.wallstreetprep.com/knowledge/demystifying-the-13-week-cash-flow-model-in-excel/
  - https://www.fe.training/free-resources/restructuring/13-week-cash-flow-model-twcf/
  - https://www.proskauer.com/alert/private-credit-deep-dives-covenant-cures
  - https://harogage.com/gage-applications-pratiques-reforme-droit-des-suretes/
  - https://cms.law/fr/fra/news-information/reforme-des-suretes-et-financement-d-entreprise
  - https://www.village-justice.com/articles/reflexions-sur-creation-fiducie-prevention,39243.html
  - https://www.pwc.fr/fr/expertises/transactions/entreprises-en-difficulte.html
related:
  - valorisation-distressed
  - mandat-ad-hoc-conciliation
  - rang-des-creances
---

# Restructuration de dette et financement en crise -- Guide exhaustif

Ce document couvre l'ensemble des techniques de restructuration financiere utilisables dans le contexte M&A distressed PME France. Niveau expert, orientation praticien.

---

## 1. Techniques de restructuration de dette

### 1.1 Standstill / Moratoire

**Definition** : Accord temporaire par lequel les creanciers suspendent l'exercice de leurs droits (exigibilite, poursuites, acceleration) pour donner au debiteur un delai de respiration ("breathing space").

**Cadre juridique francais** :
- En **[[brantham/knowledge/procedures/mandat-ad-hoc-conciliation|mandat ad hoc]]** (L611-3) et **[[brantham/knowledge/procedures/mandat-ad-hoc-conciliation|conciliation]]** (L611-4+) : le standstill est demande systematiquement par le mandataire/conciliateur des l'ouverture. C'est une pratique de marche, pas une obligation legale.
- Depuis l'ordonnance du 15 septembre 2021 (transposition Directive UE 2019/1023), le tribunal peut imposer un **moratoire force** aux creanciers qui refusent le standstill, y compris sur des creances non encore echues, pour la duree de la conciliation (max 5 mois).
- En procedure collective, l'**arret des poursuites individuelles** (L622-21) produit un effet standstill automatique et generalise.

**Duree typique** :
- Mandat ad hoc : 3 a 6 mois (renouvelable, pas de duree legale max)
- Conciliation : 4 mois + 1 mois de prolongation = max 5 mois
- Moratoire force judiciaire : jusqu'a 2 ans (L611-10-1) si le creancier a mis en demeure ou poursuivi le debiteur

**Contenu standard d'un accord de standstill** :
- Suspension des echeances en capital (parfois aussi interets)
- Non-acceleration des credits malgre un event of default
- Maintien des lignes de credit existantes (pas de denonciation)
- Engagement du debiteur a fournir un reporting financier renforce (souvent hebdomadaire)
- Clause de sortie ("termination events") en cas de deterioration significative
- Obligation de ne pas contracter de nouvelle dette sans accord des creanciers

**Chiffres** : Dans la pratique francaise, ~90% des conciliations commencent par un standstill bancaire. La Banque de France note un taux de reussite des mediations de credit de ~65%.

---

### 1.2 Waiver (renonciation a un event of default)

**Definition** : Acte par lequel le(s) creancier(s) renonce(nt) formellement a invoquer un cas de defaut (covenant breach, impaye, cross-default) qui leur donnerait le droit d'accelerer la dette.

**Mecanisme** :
- Le debiteur notifie le breach au pool bancaire via un compliance certificate
- Le debiteur demande un waiver (renonciation) assorti ou non de conditions
- Decision du pool bancaire selon les regles de majorite du contrat de credit (generalement 2/3 des encours)
- Le waiver peut etre : inconditionnel, temporaire (limited waiver), ou conditionne a des mesures correctives

**Cout typique** :
- Waiver fee : 0.25% a 1.00% de l'encours total du credit
- Augmentation de la marge (spread increase) : +25bps a +200bps
- Mise en place de garanties supplementaires
- Renforcement du reporting (passage de trimestriel a mensuel voire hebdomadaire)

**Attention** : Un waiver n'est PAS un amendment. Il ne modifie pas les termes du contrat — il renonce simplement a exercer un droit ne du breach. Si le meme breach se reproduit, il faudra un nouveau waiver (sauf si le waiver est permanent, ce qui est rare).

**Jurisprudence** : En droit francais, le silence du creancier ne vaut pas renonciation a invoquer un default. Il faut un acte positif explicite (Cass. Com. principe constant).

---

### 1.3 Amendment & Extend (A&E)

**Definition** : Modification formelle du contrat de credit pour adapter les termes financiers a la nouvelle realite de l'entreprise, accompagnee generalement d'une extension de la maturite.

**Termes typiquement renegocies** :
- **Maturite** : extension de 1 a 5 ans (souvent 2-3 ans en PME)
- **Profil d'amortissement** : passage de lineaire a bullet, ou report des echeances
- **Covenants financiers** : reset des ratios (leverage, DSCR, interest cover) avec trajectoire descendante
- **Marge** : augmentation de +50bps a +300bps pour compenser le risque accru
- **Garanties** : ajout de [[brantham/knowledge/legal/suretes-en-procedure-collective|suretes]] supplementaires (nantissement titres, hypotheque, gage stocks)
- **Cash sweep** : mecanisme de remboursement anticipe si le cash flow depasse un certain seuil

**Processus en France** :
1. Diagnostic financier independant (IBR - Independent Business Review) commande par les banques
2. Business plan a 5 ans avec scenarios base/downside
3. [[brantham/knowledge/finance/financial-modeling-distressed|13-week cash flow]] pour valider la liquidite court terme
4. Negociation du term sheet amende
5. Redaction des documents definitifs par les conseils juridiques
6. Signature et mise en oeuvre

**Cout** : Amendment fee 0.5% a 2% + frais juridiques (200K-500K EUR pour un dossier mid-cap) + IBR (50K-150K EUR)

**Delai** : 3 a 9 mois du diagnostic a la signature, selon la complexite et le nombre de creanciers.

---

### 1.4 Debt-to-Equity Swap (conversion de creances en capital)

**Definition** : Transformation de creances en titres de capital (actions ou parts sociales), faisant basculer le creancier de la position de preteur a celle d'actionnaire.

**Cadre juridique francais** :
- Art. L225-146 Code de commerce : seules les creances **liquides, certaines et exigibles** peuvent etre converties. La liberation par compensation doit etre certifiee par un notaire ou commissaire aux comptes.
- Decision de l'AGE (assemblee generale extraordinaire) a la majorite des 2/3
- Le commissaire aux apports verifie la valeur des creances converties (obligatoire si l'apport depasse certains seuils)
- Possibilite de forcer la conversion dans le cadre des **classes de parties affectees** (reforme 2021, Art. L626-30-2) avec le mecanisme de **cram-down** inter-classes

**Parite de conversion** :
- En general, la conversion se fait avec une **decote significative** (30% a 70%) par rapport au nominal de la creance
- Exemple [[brantham/knowledge/market/cas-orpea-emeis|Orpea]] (2023) : 3.8 milliards EUR de dette convertis en capital, reduisant la dette nette de 60%. Les creanciers ont recu des actions valorisees bien en dessous du nominal des creances.
- Pour une PME en RJ : la decote peut atteindre 50-80% car la valeur de l'equity est souvent proche de zero

**Avantages** :
- Reduction immediate du levier financier (deleverage)
- Amelioration du bilan et des ratios de solvabilite
- Alignement d'interets creanciers/actionnaires
- Signal fort aupres des tiers (clients, fournisseurs)

**Inconvenients** :
- Dilution massive des actionnaires existants (souvent quasi-totale en distressed)
- Les creanciers deviennent actionnaires et doivent gerer un actif illiquide
- Fiscalite : le debiteur peut realiser un profit imposable (boni de dette) sauf exceptions

**Fiscalite en France** :
- Le boni de dette (ecart entre nominal et valeur de conversion) est en principe imposable a l'IS au taux normal (25%)
- Art. 209-II CGI : possibilite de sursis d'imposition si la conversion s'inscrit dans un accord de conciliation homologue ou un plan de sauvegarde/redressement
- Les creanciers constatent une perte deductible sur la fraction de creance abandonnee

---

### 1.5 Haircut (reduction du nominal de la dette)

**Definition** : Abandon partiel de creance par lequel le creancier accepte de renoncer a une partie du montant nominal qui lui est du.

**Cadre juridique** :
- En amiable (mandat ad hoc, conciliation) : l'abandon de creance est **purement consensuel** et s'inscrit dans l'accord negocie
- En procedure collective : l'abandon peut etre impose dans le cadre d'un plan de [[brantham/knowledge/procedures/sauvegarde]]/[[brantham/knowledge/procedures/redressement-judiciaire|redressement]] vote par les classes de parties affectees, y compris par cram-down
- Art. L626-30-2 al. 5 : le tribunal peut imposer le plan a une classe dissidente si les conditions du "best interest test" et du "relative priority test" sont remplies

**Ampleur typique** :
- Conciliation : haircut de 0% a 30% (les banques francaises sont historiquement resistantes aux haircuts)
- Plan de sauvegarde : 20% a 50%
- Plan de redressement : 30% a 70%
- LJ / cession : le passif est purge, donc pas de haircut a proprement parler — les creanciers recueillent un dividende sur l'actif realise (souvent 5% a 20% du chirographaire)

**Traitement fiscal** :
- Pour le debiteur : le gain est en principe imposable sauf si l'entreprise est en deficit (imputable sur les deficits reportables, avec plafond de 1M EUR + 50% au-dela)
- Pour le creancier : la perte est deductible si elle est definitive et n'est pas constitutive d'un acte anormal de gestion (clause anti-abus : la renonciation doit servir l'interet du creancier, ex: recuperer davantage que dans un scenario de liquidation)

**Cas PME** : En pratique, les banques francaises preferent l'allongement de maturite ou le taux reduit au haircut pur. Les fonds de dette et les creanciers mezzanine sont plus ouverts a la decote.

---

### 1.6 Debt Buy-Back avec decote

**Definition** : Le debiteur (ou une entite liee) rachete sa propre dette sur le marche secondaire a un prix inferieur au nominal, beneficiant ainsi de la decote de marche.

**Mecanisme** :
1. La dette est cotee ou negociable sur un marche secondaire (rare pour les PME, plus courant pour les mid/large caps ou les creedits syndiquest)
2. Le debiteur rachete sa dette a la valeur de marche (ex: 40 centimes pour 1 EUR de nominal)
3. La difference (60 centimes) constitue un gain qui ameliore le bilan

**Contraintes juridiques** :
- Les contrats de credit syndiquest interdisent souvent au debiteur de racheter sa propre dette ("borrower buy-back prohibition"). Il faut un waiver ou utiliser un vehicule tiers
- En France, l'utilisation d'une societe holding ou d'un fonds affilie est une pratique courante pour contourner cette restriction
- Attention aux regles de droit des societes (abus de bien social) et fiscales (prix de transfert)

**Prix de marche typique de la dette distressed** :
- Pre-procedure : 70-90 centimes/EUR
- Mandat ad hoc/conciliation : 50-80 centimes/EUR
- Redressement judiciaire : 20-50 centimes/EUR
- Liquidation judiciaire : 5-20 centimes/EUR

**Exemple** : Dans les LBO distressed, les sponsors PE rachetent parfois la dette senior a 60 centimes par l'intermediaire d'un vehicule ad hoc, puis convertissent cette dette en equity de la holding, realisant un gain comptable significatif.

---

### 1.7 Titrisation NPL / Cession de creances douteuses

**Definition** : Cession par les banques de portefeuilles de prets non performants (NPL - Non Performing Loans) a des investisseurs specialises ou dans des vehicules de titrisation.

**Marche francais** :
- La France detient **115 milliards EUR de NPL** (2024-2025), soit **32% du total europeen** (vs 21% en 2019)
- Le portefeuille NPL des PME francaises croit le plus vite en Europe : **+13%/an**, atteignant **37 milliards EUR**
- Historiquement, les banques francaises sont **culturellement reticentes** a ceder leurs NPL (contrairement a l'Italie ou la Grece qui ont massivement utilise les schemas GACS/Hercules)
- La tendance evolue : la vague post-PGE (2025-2027) pousse les banques francaises a s'ouvrir au marche secondaire

**Schema de titrisation type** :
1. La banque identifie un portefeuille de NPL (criteres : anciennete, secteur, taille, garanties)
2. Cession a un SPV (Special Purpose Vehicle) a prix decote (typiquement 10-30% du nominal pour du chirographaire, 40-60% pour du garanti)
3. Le SPV emet des tranches de dette (senior, mezzanine, equity) adossees aux flux de recouvrement
4. Les servicers specialises gerent le recouvrement

**Acheteurs de NPL en France** :
- Fonds specialises : Cerberus, Bain Capital Credit, Arrow Global, Intrum, iQera
- Societes de recouvrement : EOS, Hoist Finance, CCSF
- Banques : certaines banques rachetent les NPL d'autres banques pour diversification

**Opportunite Brantham** : Les portefeuilles NPL PME sont une source de deal flow. Les entreprises sous-jacentes peuvent etre des cibles de reprise si le fonds NPL cherche a sortir du dossier plutot qu'a recouvrer.

---

## 2. Financement en crise

### 2.1 New money + privilege L611-11 (conciliation)

**Texte fondateur** : Art. L611-11 Code de commerce (modifie par ordonnance du 15/09/2021)

**Principe** : Les personnes qui consentent un **nouvel apport en tresorerie** ou fournissent un **nouveau bien ou service** au debiteur dans le cadre d'une conciliation ayant abouti a un **accord homologue** beneficient d'un **privilege de paiement** prioritaire sur (presque) toutes les autres creances en cas de procedure collective ulterieure.

**Conditions cumulatives** :
1. La conciliation doit aboutir a un **accord** (constate ou homologue)
2. L'accord doit etre **homologue** par le tribunal pour que le privilege joue pleinement
3. L'apport doit etre **effectif** (new money reel, pas un simple engagement)
4. L'apport doit viser la **poursuite d'activite** et la **perennite** de l'entreprise

**Rang du privilege** (Art. L611-11 renvoie a L622-17 et L643-8) :
1. Super-privilege des salaries (L625-8)
2. Frais de justice post-ouverture
3. **Privilege new money L611-11**
4. Privilege de post-money (L622-17)
5. Autres privileges et suretes

**Points d'attention** :
- Le privilege ne couvre **pas** les apports en capital (equity) — uniquement les apports en tresorerie ou biens/services
- Le privilege **survit** a l'ouverture d'une procedure collective ulterieure, ce qui est tout son interet : il securise le preteur qui finance une entreprise deja fragile
- En cas de conciliation **constatee** (vs homologuee), les creanciers beneficient d'un privilege de rang inferieur (le privilege de conciliation simple)
- Depuis 2021, le juge qui homologue l'accord peut fixer le **montant plafond** du privilege

**Application PME** :
- Montant typique new money : 0.5M a 5M EUR pour une PME de 5-20M EUR de CA
- Preteurs : banques existantes (souvent sous pression de la Banque de France/mediateur du credit), BPI France, parfois fonds de dette specialises
- Taux : Euribor + 300-600bps (la prime de risque est compensee par le privilege)
- Duree : 12 a 36 mois
- Garanties supplementaires souvent exigees malgre le privilege (nantissement, hypotheque)

---

### 2.2 Bridge loans / prets-relais

**Definition** : Financement court terme destine a couvrir un besoin de liquidite immediat en attendant une solution structurelle (cession, augmentation de capital, refinancement).

**Caracteristiques** :
- Duree : 3 a 12 mois
- Montant : couverture du cash burn sur la periode + marge de securite (typiquement 1.2x a 1.5x le besoin identifie)
- Taux : tres eleve en situation de crise : 8% a 15% annualise, parfois plus
- Garanties : souvent sur-garanti (nantissement actifs, delegation d'assurance, garantie personnelle dirigeant)

**Sources en France** :
- BPI France : prets de soutien a la tresorerie (garantie Etat)
- Banques existantes du pool : souvent conditionnees a un plan de restructuration credible
- Fonds de dette specialises : Tikehau, Kartesia, MV Credit
- Family offices avec appetit pour le distressed

**Risque** : Le bridge loan est un pari sur la realisation d'un evenement futur (cession, levee de fonds). Si l'evenement n'a pas lieu, le bridge aggrave la situation en ajoutant de la dette supplementaire.

---

### 2.3 DIP financing equivalent francais

**Le droit francais n'a pas de DIP financing formel** au sens du Chapter 11 americain. Cependant, plusieurs mecanismes produisent un effet similaire :

**a) Privilege de post-money (Art. L622-17)** :
Les creances nees **regulierement apres le jugement d'ouverture** pour les besoins du deroulement de la procedure ou de la periode d'observation, ou en contrepartie de prestations fournies au debiteur, sont payees a leur echeance. En cas de non-paiement, elles beneficient d'un **privilege de priorite** devant toutes les autres creances (sauf super-privilege salaries et frais de justice).

**b) Privilege new money L611-11** (voir section 2.1 ci-dessus) : joue un role equivalent en phase pre-collective.

**c) Autorisation du juge-commissaire** (Art. L622-7) : Le debiteur peut, avec l'accord du juge-commissaire, contracter des emprunts pendant la periode d'observation. Ces emprunts beneficient du privilege L622-17.

**Limites vs Chapter 11** :
- Pas de super-priorite negociable (pas de "priming lien")
- Pas de marche organise du DIP financing en France
- Les montants sont beaucoup plus faibles que dans les DIP americains
- L'administrateur judiciaire a un role central dans la decision de financement

---

### 2.4 BPI France en restructuring

**Role** : BPI France intervient comme banque publique d'investissement avec un mandat de soutien aux PME/ETI en difficulte.

**Outils disponibles** :
- **Pret Atout** : pret sans garantie de 50K a 5M EUR, duree 3-7 ans, taux fixe
- **Garantie de credit** : BPI garantit jusqu'a 70% du montant d'un pret bancaire classique, permettant a la banque de preter malgre le risque eleve
- **Pret Rebond** : specifiquement destine aux entreprises post-procedure (en sortie de plan de sauvegarde/redressement), 10K a 300K EUR
- **Fonds de renforcement des PME** : prise de participation minoritaire (quasi-equity) dans des PME en retournement
- **Mediation du credit** : BPI coordonne avec la Banque de France pour debloquer les situations de credit

**Conditions** :
- L'entreprise doit demontrer une viabilite structurelle (le probleme est financier, pas operationnel)
- Un plan de retournement credible doit etre presente
- Les actionnaires doivent contribuer (pas de bail-out sans effort propre)

**Chiffres** : BPI France a garanti ~3 milliards EUR de prets en 2024-2025 pour des entreprises en difficulte. Taux de survie des entreprises accompagnees : ~65% a 3 ans.

---

### 2.5 Affacturage de dernier recours

**Definition** : Cession de creances clients a un factor en echange d'un financement immediat (avance de 80-95% du montant des factures).

**Pourquoi en crise** :
- Acces quasi-instantane a la liquidite (mise en place en 2-4 semaines)
- Base sur la qualite des debiteurs (clients), pas sur la sante du cedant
- Pas besoin de garanties sur le patrimoine de l'entreprise
- Compatible avec une procedure amiable (mandat ad hoc, conciliation)

**Limites en situation distressed** :
- Le factor analyse le risque sur les debiteurs cedes : si les clients sont eux-memes fragiles, refus
- Cout eleve : commission d'affacturage 0.5-3% du CA cede + taux de financement 3-8%
- Le factor peut denoncer le contrat a tout moment (preavis 3 mois en general)
- En procedure collective : le contrat d'affacturage est un contrat en cours (L622-13) — l'administrateur peut exiger sa poursuite

**Acteurs principaux** :
- Filiales bancaires : BNP Factor, BPCE Factor, CGA (Credit Agricole), SG Factoring
- Independants : Bibby Factor, ABN AMRO Commercial Finance, Factofrance
- Specialises distressed : Ellisphere, certains courtiers

**Montant typique PME** : Financement de 60-90% du poste clients (net des provisions), soit pour une PME a 10M EUR de CA : ~1.5-3M EUR de liquidite disponible.

---

### 2.6 Sale & Leaseback (cession-bail)

**Definition** : L'entreprise cede un actif corporel (immobilier, equipement industriel, parc vehicules) a un investisseur/bailleur et le reprend immediatement en location.

**Pourquoi en crise** :
- Generation de cash immediate (liberation de la valeur des actifs immobilises)
- Pas de modification du bilan en termes de capacite productive (l'actif reste utilise)
- Souvent la **derniere source de financement** quand les banques refusent de preter
- N'aggrave pas l'endettement financier (c'est un loyer, pas une dette — sauf IFRS 16)

**Actifs typiquement concernes** :
- **Immobilier** : murs commerciaux, entrepots, usines (le plus courant, valeurs de 500K a plusieurs M EUR)
- **Equipement industriel** : machines-outils, lignes de production (200K-2M EUR)
- **Parc vehicules** : flottes de camions, vehicules utilitaires (50K-500K EUR)
- **Materiel informatique** : serveurs, equipements IT (rare en PME)

**Valorisation** :
- L'actif est evalue par un expert independant (valeur venale en etat d'occupation)
- Le prix de vente est generalement 70-85% de la valeur de marche (decote pour risque locataire + illiquidite)
- Le loyer est fixe pour que le rendement investisseur soit de 6-10% brut (immobilier) ou 8-15% (equipement)

**Acteurs en France** :
- Immobilier : Gecina, Icade, fonds SCPI, family offices
- Equipement : Natixis Lease, Franfinance, De Lage Landen
- Specialises distressed : certains fonds opportunistes

**Points d'attention** :
- Risque de requalification en pret deguise si le prix de rachat est trop faible
- En procedure collective, le bail est un contrat en cours (L622-13) — protege
- L'actif cede sort du patrimoine : il ne peut plus servir de garantie aux creanciers existants (attention aux negative pledge clauses dans les contrats de credit)

---

## 3. LBO distressed

### 3.1 Quand le LBO tourne mal

**Signaux d'alerte** :
- **Covenant breach** : le ratio leverage (dette nette/EBITDA) depasse le seuil contractuel (typiquement 4-6x en mid-market francais). Premier signal, souvent a 12-18 mois post-acquisition.
- **Cash flow insuffisant** : le DSCR (Debt Service Coverage Ratio) passe sous 1.0x — l'entreprise ne genere pas assez de cash pour servir sa dette
- **Deterioration operationnelle** : perte de clients majeurs, pression sur les marges, disruption sectorielle
- **Matrice de risque PGE** : de nombreux LBO francais 2019-2021 ont ete structures avec du PGE comme quasi-equity. Le remboursement du PGE (2023-2027) cree un stress additionnel
- **Taux d'interet** : hausse de l'Euribor de 0% (2021) a 3.5-4% (2023-2024) a double le cout de la dette variable, comprimant le free cash flow

**Statistiques LBO France** :
- ~250 LBO par an en France (mid-market, tickets 10-200M EUR)
- Taux de defaut estime : 8-12% a 5 ans post-acquisition (source : Banque de France, etude 2000-2010 extrapolee)
- Les LBO en distress representent ~15-20% du pipeline de restructuring des grandes etudes d'AJ

**Structure typique LBO mid-market France** :
| Tranche | Montant typique | Ratio | Rang |
|---|---|---|---|
| Equity sponsor | 30-40% TEV | — | Junior |
| Dette senior (Term Loan A/B) | 3.0-4.5x EBITDA | Euribor + 250-500bps | Senior secured |
| Ligne revolving (RCF) | 0.5-1.0x EBITDA | Euribor + 200-400bps | Senior secured |
| Mezzanine / unitranche | 1.0-2.0x EBITDA | 8-14% cash + PIK | Subordinated |
| Vendor loan | 0.5-1.0x EBITDA | 4-8% (souvent PIK) | Junior/subordonne |

---

### 3.2 Restructuration dette senior / mezzanine

**Sequence typique de restructuration LBO** :

**Phase 1 : Waiver et diagnostic (semaines 1-8)**
- Le sponsor notifie le breach aux banques
- Nomination d'un conseil financier independant (IBR) par les banques : Alvarez & Marsal, FTI Consulting, PwC Deals, Eight Advisory
- Standstill de 3-6 mois pour permettre le diagnostic
- Cout IBR : 80K-200K EUR

**Phase 2 : Plan de retournement (semaines 8-16)**
- Business plan revise avec 3 scenarios (base, downside, upside)
- 13-week cash flow pour valider la liquidite
- Identification des quick wins (voir section 5)
- Negociation des termes de restructuration

**Phase 3 : Execution (semaines 16-36)**
Selon la gravite, les options sont (par ordre croissant de severite) :

a) **A&E simple** : extension de maturite + reset covenants. Le sponsor ne met pas d'argent frais.
   - Faisable si le probleme est temporaire et le business fondamentalement sain

b) **Injection d'equity + A&E** : le sponsor injecte du capital frais en echange d'un allongement. Les banques acceptent un deleveraging progressif.
   - Typique si leverage 5-7x et DSCR 0.8-1.2x

c) **Debt-to-equity swap partiel** : une partie de la dette mezzanine est convertie en equity de la holding. Le sponsor est dilue mais conserve une position.
   - Typique si leverage >7x, mezzanine sous l'eau

d) **Cram-down / wipe-out** : les creanciers seniors prennent le controle de l'equity. Le sponsor et les mezzaneurs sont essuyes.
   - Typique si leverage >8-10x, l'entreprise ne vaut pas plus que la dette senior

e) **Cession a un tiers** : l'entreprise est vendue (souvent en pre-pack via L611-7 ou en [[brantham/knowledge/legal/plans-de-cession|plan de cession]] L642-1+) a un repreneur industriel ou un autre sponsor.
   - Dernier recours si aucun accord n'est possible entre sponsor et creanciers

---

### 3.3 Equity cure, sponsor support

**Equity cure** : Mecanisme contractuel (prevu dans le contrat de credit) par lequel le sponsor PE injecte des fonds propres dans le groupe pour "guerir" un breach de covenant financier.

**Mecanisme detaille** :
1. Le compliance certificate revele un breach (ex: leverage 5.2x vs covenant 5.0x)
2. Le sponsor dispose d'un delai de grace (typiquement 15-20 jours ouvrables en Europe)
3. Le sponsor injecte du cash dans la holding qui le descend a l'emprunteur
4. Le cash injecte est ajoute au calcul de l'EBITDA ("deemed EBITDA cure") ou soustrait de la dette nette ("balance sheet cure")
5. Si le ratio recalcule passe le seuil, le breach est repute guerir

**Limites contractuelles standard** :
- Max 2 cures par periode de 12 mois
- Pas de cures consecutives (pas 2 trimestres de suite)
- Nombre total de cures sur la vie du credit : 3-5
- Le montant injecte doit etre permanent (pas de remontee par dividende dans les 12 mois)

**Sponsor support au-dela du cure** :
- **Management fee waiver** : le sponsor renonce temporairement a ses fees de gestion (typiquement 1-2% du CA)
- **Shareholder loan** : pret d'actionnaire subordonne a taux PIK, souvent injecte en amont de la holding
- **Apport en fonds propres** : augmentation de capital de la holding, dilue les co-investisseurs mais pas les creanciers
- **Garantie personnelle du sponsor** : extremement rare mais existe dans les fonds "skin in the game"

**Calcul economique du sponsor** : Le sponsor decide de "curer" ou non en comparant le cout du cure (cash injecte a fonds perdus) a la valeur residuelle de son equity. Si l'equity est sous l'eau (valeur de l'entreprise < dette), il est rationnel de ne PAS curer et d'abandonner le deal.

---

### 3.4 LBO secondaire distressed

**Definition** : Rachat d'une entreprise sous LBO distressed par un nouveau sponsor PE, souvent a un prix significativement inferieur au prix d'entree initial.

**Mecanisme** :
1. Le sponsor initial n'arrive plus a gerer la situation et/ou refuse d'injecter du capital supplementaire
2. Un nouveau sponsor identifie l'opportunite (souvent via les banques ou les AJ/MJ)
3. Le nouveau sponsor negocie le rachat de la dette (a decote) et/ou de l'equity
4. La transaction peut prendre la forme de :
   - **Rachat de dette** : le nouveau sponsor rachete la dette senior a 50-70 centimes, puis negocie un A&E ou une conversion
   - **Rachat d'equity** : le nouveau sponsor achete les parts du sponsor initial pour un euro symbolique et s'engage a recapitaliser
   - **Pre-pack cession** (L611-7) : le nouveau sponsor fait une offre dans le cadre d'une conciliation, validee par le tribunal
   - **Plan de cession** (L642-1+) : le nouveau sponsor fait une offre au tribunal dans le cadre d'un RJ/LJ

**Fonds actifs sur le segment distressed en France** :
- Butler Industries (France, specialise PME distressed)
- Perceva (France, mid-market distressed)
- Cerberus (Europe, large distressed)
- Attestor Capital
- Alcentra / BNY Mellon
- ICG (restructuring)
- Tikehau Capital (opportunistic)

**Multiple d'entree** : Typiquement 3-5x EBITDA normalise (vs 7-10x pour un LBO primaire sain), soit une decote de 40-60%.

**Risques specifiques** :
- Le precedent echec LBO signale un probleme structurel (pas uniquement financier)
- La dette residuelle peut etre complexe (multiple tranches, conditions croisees)
- Les equipes management sont souvent epuisees et demotivees
- Le fonds sortant peut retenir des informations cles

---

## 4. Cash management en crise

### 4.1 13-Week Cash Flow (structure complete)

**Definition** : Prevision hebdomadaire de tresorerie sur 13 semaines (1 trimestre), methode directe (encaissements - decaissements). Outil standard mondial du restructuring.

**Pourquoi 13 semaines** :
- Assez court pour etre fiable (horizons >3 mois sont speculatifs en crise)
- Assez long pour identifier les pics/creux de tresorerie
- Couvre un trimestre complet (saisonnalite)
- Standard de marche demande par les banques, AJ, tribunaux et investisseurs

**Structure complete du modele** :

```
SEMAINE                    S1    S2    S3    ...   S13   TOTAL
=================================================================
SOLDE INITIAL              XXX

--- ENCAISSEMENTS ---
  Encaissements clients     XX    XX    XX          XX
  Autres produits            X     X     X           X
  Cession d'actifs           -     -     X           -
  Apport new money           -     -     -           X
TOTAL ENCAISSEMENTS         XX    XX    XX          XX     XXX

--- DECAISSEMENTS ---
  Fournisseurs matières      XX    XX    XX          XX
  Sous-traitance              X     X     X           X
  Salaires + charges soc     XX    -     -          XX
  Loyers + charges locatives  X    -     -           X
  Impots et taxes             -    -     X           -
  TVA                         -    X     -           -
  Cotisations sociales       XX    -     -          XX
  Honoraires (AJ, avocats)    X    X     X           X
  Assurances                  -    X     -           -
  Service dette (interets)    -    -     X           -
  Service dette (capital)     -    -     X           -
  CAPEX minimum vital         X    -     X           -
  Autres decaissements        X    X     X           X
TOTAL DECAISSEMENTS         XX    XX    XX          XX     XXX

--- FLUX NET ---
  Flux net de la semaine     XX    XX    XX          XX

--- TRESORERIE ---
  Solde avant tirage RCF    XXX   XXX   XXX        XXX
  Tirage/remboursement RCF    -     X     -           -
  SOLDE FIN DE SEMAINE       XXX   XXX   XXX        XXX

--- ALERTES ---
  Solde minimum requis       XXX   XXX   XXX        XXX
  Headroom (+) / Deficit (-)  XX    XX    XX          XX
```

**Regles de construction** :
- Methode **directe** uniquement (encaissements/decaissements, PAS le resultat net ajuste)
- Chaque ligne doit etre etayee par une **piece justificative** (bon de commande, echeancier fournisseur, contrat de travail)
- **Mise a jour hebdomadaire** avec reconciliation semaine precedente (realise vs previsionnel, explication des ecarts)
- Distinction obligatoire entre flux **certains** (salaires, loyers, echeances de dette) et flux **estimatifs** (encaissements clients, ventes)
- Le modele doit identifier le **cash minimum** (seuil en-dessous duquel l'entreprise ne peut plus operer : paiement des salaires + fournisseurs critiques)

**Erreurs frequentes** :
- Oublier la TVA (decalage TVA collectee/deductible peut creer un trou de 2-4 semaines)
- Sous-estimer le DSO (delai d'encaissement reel vs theorique, souvent +10-15j en crise car les clients sentent la fragilite)
- Ne pas integrer les frais de procedure (AJ, avocats, experts : 200K-500K EUR sur la duree d'un RJ)
- Ignorer les clauses de cross-default (un impaye declenche l'acceleration d'autres credits)

---

### 4.2 Cash conservation measures

**Actions immediates (semaine 1-2)** :

| Action | Impact tresorerie | Delai |
|---|---|---|
| Gel des depenses non essentielles (dons, sponsoring, R&D non critique) | 2-5% des decaissements | Immediat |
| Gel des embauches et des remplacements | 3-8% | Immediat |
| Renegociation des contrats de maintenance/service | 1-3% | 2-4 semaines |
| Arret des dividendes et fees de gestion | Variable | Immediat |
| Report des investissements non critiques | 5-15% | Immediat |
| Centralisation des paiements (approbation DAF pour tout decaissement >5K EUR) | 3-5% | 1 semaine |
| Rapatriement de cash des filiales | Variable | 1-4 semaines |

**Actions court terme (semaines 2-8)** :
- Negociation delais fournisseurs (voir 4.4)
- Acceleration encaissements clients (relance, escompte pour paiement anticipe 1-2%)
- Reduction des stocks (destockage agressif, promotions)
- Sale & leaseback d'actifs non strategiques
- Mise en place affacturage express

**Actions moyen terme (semaines 8-26)** :
- Restructuration effectifs (PSE si >50 salaries, licenciement economique sinon)
- Renegociation des baux commerciaux
- Externalisation de fonctions non-core
- Cession d'actifs non strategiques (marques, brevets, filiales)

---

### 4.3 Gestion BFR en crise

**Le BFR en crise est le premier levier de survie**. Formule : BFR = Stocks + Creances clients - Dettes fournisseurs.

**Objectif** : Reduire le BFR de 10-30% en 8-12 semaines.

**Levier 1 : Reduction des stocks**
- Audit stock mort (articles sans mouvement depuis >6 mois) : liquider a prix coutant ou en dessous
- Reduction du stock de securite : passer de 4-6 semaines a 2-3 semaines
- Arret des commandes de produits a faible rotation
- Negociation de consignation avec fournisseurs cles
- Impact typique : liberation de 10-20% de la valeur de stock en cash

**Levier 2 : Acceleration encaissements clients (reduction DSO)**
- Relance systematique a J+0 de la date d'echeance (pas J+15 comme habituellement)
- Escompte pour paiement anticipe : offrir 1-2% de remise pour paiement a 10j vs 60j
- Passage en paiement d'avance pour nouveaux clients
- Acomptes sur commandes (30-50%) pour projets longs
- Affacturage selectif sur les plus gros clients
- Impact typique : reduction DSO de 5-15 jours = gain de 1-4% du CA en cash

**Levier 3 : Allongement delais fournisseurs (augmentation DPO)**
- La loi LME plafonne les delais a 60 jours date de facture (ou 45 jours fin de mois)
- En pratique, en crise, negocier des echeanciers de reglement avec les fournisseurs cles
- Identifier les fournisseurs critiques (pas d'alternative) vs non critiques (substituables) : payer en priorite les critiques
- Amendes DGCCRF pour retard de paiement : max 2M EUR (4M en recidive) — risque a evaluer vs gain de tresorerie
- Impact typique : +5-15 jours de DPO = gain equivalent a 1-3% du CA en cash

**Formule d'impact** : Pour une PME a 10M EUR de CA avec BFR a 25% (2.5M EUR), une reduction de 20% du BFR = 500K EUR de cash libere — souvent la difference entre la survie et la cessation de paiement.

---

### 4.4 Negociation fournisseurs / clients

**Avec les fournisseurs** :

*Strategie* :
- Classer les fournisseurs en 3 categories : **critiques** (pas d'alternative, rupture = arret production), **importants** (alternative existe mais couteuse), **substituables** (facilement remplacables)
- Negocier en priorite avec les substituables (levier maximal) et les importants
- Proteger la relation avec les critiques a tout prix (les payer en premier)

*Techniques* :
- Demander un echeancier de reglement du retard (3-6 mois)
- Proposer un nantissement ou une garantie en echange d'un delai
- Offrir une exclusivite ou un volume garanti en echange de conditions de paiement etendues
- Utiliser le levier de la conciliation : le juge peut imposer un moratoire force (L611-10-1)

**Avec les clients** :
- Ne JAMAIS reveler la situation de crise aux clients (risque de fuite massif)
- Renforcer la qualite de service et le suivi commercial pour fideliser
- Proposer des contrats cadre avec engagements de volume en echange de paiements anticipates
- Diversifier le portefeuille clients pour reduire la dependance (top 3 clients <30% du CA)

---

## 5. Business plan de retournement

### 5.1 Structure type

Le business plan de retournement est le document central demande par les banques, l'AJ, le tribunal et les investisseurs. Il doit etre credible, detaille et realiste.

**Structure standard** :

```
1. RESUME EXECUTIF (2 pages max)
   - Situation actuelle en chiffres cles
   - Causes de la crise
   - Mesures proposees et impact attendu
   - Besoin de financement

2. DIAGNOSTIC
   2.1 Historique financier (3-5 ans)
       - CA, EBITDA, resultat net, cash flow
       - Evolution du BFR et de l'endettement
   2.2 Analyse des causes de la crise
       - Internes : management, produit, cout, organisation
       - Externes : marche, concurrence, reglementation
   2.3 Positionnement concurrentiel
       - Forces et faiblesses vs concurrents directs
   2.4 Matrice SWOT de crise
       - Focus sur les menaces immediates et les opportunites de retournement

3. PLAN D'ACTION
   3.1 Mesures d'urgence (0-3 mois) — Quick wins
   3.2 Mesures structurelles (3-12 mois) — Transformation
   3.3 Mesures strategiques (12-36 mois) — Repositionnement
   3.4 Calendrier detaille avec jalons

4. PROJECTIONS FINANCIERES
   4.1 Hypotheses detaillees (ligne par ligne)
   4.2 Compte de resultat previsionnel (M+1 a M+36)
   4.3 Bilan previsionnel
   4.4 Tableau de flux de tresorerie
   4.5 13-week cash flow (court terme)
   4.6 Trois scenarios : base, downside, upside

5. BESOIN DE FINANCEMENT
   5.1 Cash gap identifie (13WCF)
   5.2 Montant new money necessaire
   5.3 Structure de financement proposee
   5.4 Plan de remboursement
   5.5 Garanties offertes

6. GOUVERNANCE ET SUIVI
   6.1 Equipe de retournement (CRO, DAF interim, conseil)
   6.2 Reporting mensuel avec KPIs
   6.3 Comite de pilotage (composition, frequence)
   6.4 Triggers pour escalade
```

---

### 5.2 Hypotheses base / downside / upside

**Scenario Base** (probabilite 50-60%) :
- CA : stabilisation puis croissance moderee (+2-5%/an)
- Marge : amelioration progressive grace aux quick wins (+1-3pts EBITDA sur 12 mois)
- BFR : reduction de 15-20% en 6 mois
- CAPEX : maintenance uniquement (2-3% du CA)
- Hypotheses macro : pas de recession, taux stables

**Scenario Downside** (probabilite 20-30%) :
- CA : baisse supplementaire de -5 a -15%
- Perte d'1-2 clients majeurs
- Marge : degradation supplementaire (-1 a -2pts EBITDA)
- BFR : pas d'amelioration significative
- Test : l'entreprise survit-elle dans ce scenario ? Si non, il faut plus de new money ou un plan de cession

**Scenario Upside** (probabilite 10-20%) :
- CA : rebond rapide (+10-15%)
- Gain de parts de marche sur concurrents en difficulte
- Marge : retour au niveau pre-crise
- Remboursement anticipe partiel de la dette

**Regle d'or** : Les banques et les tribunaux jugent le plan sur le scenario downside. Si le plan ne tient pas en downside, il est rejete.

---

### 5.3 Quick wins vs transformations structurelles

**Quick wins (impact 0-90 jours, effort faible/moyen)** :
| Quick win | Impact EBITDA typique | Delai |
|---|---|---|
| Arret des depenses discretionnaires | +0.5-1.5% CA | Immediat |
| Renegociation contrats fournisseurs top 10 | +1-3% achats | 4-8 semaines |
| Reduction interimat / CDD non renouveles | +0.5-1% CA | Immediat |
| Optimisation prix de vente (hausse selective) | +1-3% CA | 2-6 semaines |
| Reduction stock mort | Cash +5-15% stock | 4-8 semaines |
| Arret activites/produits deficitaires | +0.5-2% CA | 4-12 semaines |

**Transformations structurelles (impact 3-18 mois, effort eleve)** :
| Transformation | Impact EBITDA typique | Delai |
|---|---|---|
| PSE / reorganisation | +3-8% CA (masse salariale) | 6-12 mois |
| Fermeture site non rentable | +1-5% CA | 6-18 mois |
| Migration IT / digitalisation | +1-2% CA | 12-24 mois |
| Refonte supply chain | +2-5% achats | 6-18 mois |
| Repositionnement produit/marche | Variable | 12-36 mois |
| M&A defensif (rachat concurrent) | Variable | 12-24 mois |

---

### 5.4 KPIs de suivi

**KPIs financiers (suivi hebdomadaire en crise)** :
- **Cash position** : solde de tresorerie fin de semaine
- **Cash burn rate** : vitesse de consommation du cash (semaines de survie restantes)
- **Headroom** : marge de manoeuvre par rapport au cash minimum vital
- **DSO** : delai moyen d'encaissement clients (jours)
- **DPO** : delai moyen de paiement fournisseurs (jours)
- **DIO** : duree moyenne de rotation des stocks (jours)
- **Cash conversion cycle** : DSO + DIO - DPO

**KPIs operationnels (suivi mensuel)** :
- **CA mensuel** vs budget et N-1
- **Marge brute** et **marge EBITDA** mensuelles
- **Carnet de commandes** (pipeline commercial)
- **Taux d'utilisation capacite** (industrie)
- **Productivite par ETP** (CA/ETP ou VA/ETP)
- **Taux de service client** (livraisons a temps, reclamations)
- **Turnover employes** (signal de fuite des talents)

**KPIs de transformation (suivi mensuel)** :
- Avancement des quick wins (% realise vs plan)
- Economies realisees vs prevues
- New money debloque vs plan
- Covenants financiers : trajectoire de retour dans les clous

**Tableau de bord type** :
Un reporting hebdomadaire de 2 pages max est envoye au comite de pilotage :
- Page 1 : 13WCF mise a jour + ecarts vs semaine precedente
- Page 2 : KPIs cles + commentaires sur les 3 sujets prioritaires

---

## 6. Garanties et suretes

### 6.1 Nantissement de fonds de commerce

**Definition** : Surete reelle portant sur les elements incorporels du fonds de commerce (clientele, achalandage, enseigne, droit au bail, nom commercial). Les elements corporels (materiel, stock) en sont exclus sauf convention contraire.

**Constitution** :
- Acte notarie ou sous seing prive
- Inscription au greffe du tribunal de commerce dans les 15 jours
- Duree d'inscription : 10 ans (renouvelable)

**Rang** : Confere un droit de preference et un droit de suite sur le fonds greve.

**En procedure collective** :
- Le nantissement ne donne pas le droit de realiser le fonds pendant la periode d'observation
- En cas de cession (L642-1+), le prix est reparti selon le rang des creanciers inscrits
- Le nantissement est **purge** par le plan de cession — le creancier est reporte sur le prix

**Valeur en distressed** : Tres faible si l'entreprise est en crise. Le fonds de commerce d'une entreprise defaillante vaut souvent 10-30% de sa valeur en exploitation normale (perte de clientele, deterioration de l'achalandage).

---

### 6.2 Nantissement de parts sociales / actions

**Definition** : Surete portant sur les titres de participation (actions de SA/SAS ou parts de SARL/SNC) detenus par le constituant.

**Utilisation en LBO** : C'est la garantie principale dans les montages LBO. Les parts de la cible sont nanties au profit des banques senior. En cas de defaut, les banques peuvent realiser le nantissement et prendre le controle de la cible.

**Constitution** :
- Parts sociales (SARL/SNC) : inscription au registre des suretes mobilieres (depuis 01/01/2023, reforme 2021)
- Actions (SA/SAS) : inscription en compte-titres + declaration au registre

**En procedure collective** :
- Le nantissement est gele pendant la periode d'observation (pas de realisation)
- Droit de retention du creancier nanti reconnu par la Cour de cassation
- En plan de cession : purge du nantissement, creancier reporte sur le prix

**Valeur en distressed** : La valeur des titres suit la valeur de l'entreprise. En distressed, si l'equity est sous l'eau (valeur d'entreprise < dette), le nantissement vaut zero en pratique. Les banques le conservent surtout comme levier de negociation.

---

### 6.3 Hypotheque

**Definition** : Surete reelle immobiliere conferant au creancier un droit de preference et un droit de suite sur l'immeuble greve.

**Types** :
- **Conventionnelle** : consentie par le proprietaire, acte notarie obligatoire
- **Legale** : au profit de certains creanciers (Tresor public, vendeur d'immeuble)
- **Judiciaire** : ordonnee par le juge (mesure conservatoire)

**Cout** : Droits d'enregistrement (~0.715% du montant garanti) + emoluments notaire + contribution de securite immobiliere (0.10%)

**En procedure collective** :
- L'hypotheque est inopposable si constituee pendant la periode suspecte (L632-1)
- Le creancier hypothecaire est paye sur le prix de l'immeuble avec son rang
- En plan de cession : purge de l'hypotheque, creancier reporte sur le prix
- Le droit de retention du creancier hypothecaire non-possessoire est discute en jurisprudence

**Valeur en distressed** : L'immobilier conserve generalement une valeur tangible, contrairement au fonds de commerce. Decote de 15-30% en vente forcee vs valeur de marche. C'est la surete la plus solide en restructuring.

---

### 6.4 Cautionnement du dirigeant

**Definition** : Engagement personnel du dirigeant a payer la dette de la societe en cas de defaillance de celle-ci.

**Cadre juridique** :
- Art. L341-1 et suivants du Code de la consommation (protection du cautionnaire)
- Le cautionnement doit etre **proportionne** aux revenus et patrimoine du dirigeant (a peine de reduction judiciaire)
- Mention manuscrite obligatoire (montant, duree, solidarite)
- Information annuelle obligatoire du cautionnaire (montant restant du, capital, interets, commissions)

**Realite en PME** :
- Quasi-systematique pour les credits bancaires aux PME (80-90% des cas)
- Montant : generalement 25-50% de l'encours du credit
- Les banques l'exigent meme quand d'autres garanties existent (sureti complementaire)
- BPI France propose des contre-garanties (couverture de 40-70% du cautionnement) via le fonds de garantie FGIF

**En restructuring** :
- Le dirigeant caution est souvent un obstacle a la restructuration : il refuse les solutions qui le mettent en risque personnel
- La conciliation peut inclure un abandon ou une reduction du cautionnement dans le package
- En plan de sauvegarde/redressement, le dirigeant beneficie des memes delais que le debiteur principal pour les creances incluses dans le plan
- En LJ, le cautionnement est appele — le dirigeant peut se retrouver en surendettement personnel

**Astuce repreneur** : Lors d'une reprise en plan de cession, le repreneur n'est PAS tenu par les cautionnements du precedent dirigeant. C'est un argument de vente pour le dirigeant cedant : la cession purge sa responsabilite personnelle.

---

### 6.5 Fiducie-surete (L611-16 et Art. 2011+ Code civil)

**Definition** : Transfert temporaire de propriete d'un actif (immobilier, comptes bancaires, creances, titres) du constituant (debiteur) vers un fiduciaire (generalement une banque ou un avocat) a titre de garantie.

**Particularite** : Contrairement aux suretes classiques, la fiducie-surete **transfere la propriete** de l'actif au fiduciaire. Le creancier-beneficiaire n'a pas besoin de saisir l'actif en cas de defaut — il en est deja proprietaire economique.

**Constitution** :
- Contrat de fiducie ecrit obligatoire
- Publicite au registre national des fiducies
- Le constituant peut conserver la jouissance de l'actif via une **convention de mise a disposition**

**En procedure collective** (L622-23-1) :
- La fiducie-surete est **neutralisee** pendant la procedure : le fiduciaire ne peut pas realiser l'actif
- Si un plan est adopte, les echeances de paiement du plan s'imposent
- Si le plan echoue ou en LJ : le fiduciaire peut enfin realiser l'actif, mais seulement apres les creanciers super-privilegies

**En conciliation (L611-16)** : La loi interdit les clauses contractuelles qui aggravent les conditions du debiteur du seul fait de l'ouverture d'une conciliation. Cela protege le debiteur contre l'activation automatique de la fiducie-surete en cas de procedure.

**Interet en restructuring** :
- Outil de garantie puissant car il sort l'actif du patrimoine du debiteur (patrimoine d'affectation distinct)
- Utilise principalement par les grands groupes et les operations mid-cap+
- Rare en PME car couteuse a mettre en place (frais juridiques 50K-150K EUR)
- De plus en plus utilisee en complément du privilege new money dans les conciliations

---

### 6.6 Gage sur stocks

**Definition** : Surete mobiliere portant sur des biens meubles corporels (stocks de marchandises, matieres premieres, produits finis) remis au creancier ou conserves par le constituant.

**Reforme 2021 (Ordonnance du 15 septembre 2021)** :
- L'ancien regime special du gage des stocks (Code de commerce) est **supprime** depuis le 01/01/2022
- Desormais, tout gage sur stocks est soumis au **droit commun du Code civil** (Art. 2333+)
- Publicite obligatoire au **registre des suretes mobilieres** (cree au 01/01/2023)

**Gage sans depossession sur biens fongibles** (cas des stocks) :
- Le constituant peut utiliser et vendre les marchandises gagees
- Il doit les **remplacer** par une quantite et qualite equivalente (rotation des stocks)
- Le creancier a un droit de preference sur le prix en cas de realisation

**En procedure collective** :
- Le gage est gele pendant la periode d'observation
- Le creancier nanti sur stocks a un droit de retention (puissant levier de negociation)
- En LJ, le liquidateur peut obtenir la mainlevee du gage en payant le creancier

**Valeur en distressed** :
- Les stocks d'une entreprise en crise se deprecient rapidement (obsolescence, deterioration, perte de valeur commerciale)
- Valeur de realisation forcee : typiquement 20-50% de la valeur comptable
- Les matieres premieres conservent mieux leur valeur que les produits finis
- Les stocks perissables ou de mode ont une valeur quasi-nulle en liquidation

---

## 7. Application Brantham

### 7.1 Comment analyser la dette d'une cible

**Checklist d'analyse de dette pour scoring Brantham** :

**Etape 1 : Cartographie du passif (jour 1)**
- [ ] Montant total de l'endettement financier (emprunts, decouverts, credits-bails, affacturage)
- [ ] Passif social (salaires dus, conges payes provisionnes, contentieux prud'homaux)
- [ ] Passif fiscal (TVA, IS, CFE, taxes non payees)
- [ ] Passif fournisseurs (montant, anciennete, fournisseurs critiques en impaye)
- [ ] Passif AGS (si procedure collective ouverte : montant avance par l'AGS a rembourser)
- [ ] PGE : montant residuel, echeancier, conditions

**Etape 2 : Structure de la dette (jour 1-2)**
- [ ] Rang de chaque creance (privilegiee, garantie, chirographaire)
- [ ] Suretes existantes : hypotheques, nantissements, gages, fiducies
- [ ] Cautionnements personnels des dirigeants
- [ ] Clauses contractuelles cles : cross-default, change of control, negative pledge, material adverse change
- [ ] PGE : garantie Etat (90%), condition de remboursement

**Etape 3 : Calcul des ratios (jour 2-3)**
- [ ] Leverage : dette nette / EBITDA normalise (target : <4x pour reprise viable)
- [ ] DSCR : cash flow operationnel / service de la dette annuel (target : >1.2x)
- [ ] Interest cover : EBITDA / charges d'interet (target : >2.5x)
- [ ] Gearing : dette nette / fonds propres (contexte seulement — FP souvent negatifs en distressed)

**Etape 4 : Waterfall analysis (jour 3-5)**
- [ ] Construire la cascade de distribution en cas de liquidation (L643-8)
- [ ] Calculer le recovery rate par classe de creancier
- [ ] Identifier la fulcrum security (la tranche de dette ou la valeur de l'entreprise "coupe")
- [ ] Estimer la decote realisable en rachats de creances

---

### 7.2 Red flags structure de financement

**Red flags critiques** (deal-breaker potentiel) :

| Red flag | Risque | Impact scoring |
|---|---|---|
| PGE >30% du CA | Surendettement post-COVID non resolu | -2 points |
| Leverage >6x EBITDA normalise | Insoutenable sans haircut massif | -3 points |
| DSCR <0.8x | Cash flow ne couvre pas le service de dette | -2 points |
| Cross-default active | Un impaye declenche l'acceleration generalisee | -1 point |
| Cautionnement dirigeant >50% patrimoine | Dirigeant bloque, decisions sous stress | -1 point |
| Pas d'actif immobilier en garantie | Rien a monetiser en sale-leaseback | -1 point |
| Clause change of control dans credits | Risque d'acceleration si cession | -2 points |
| Multiples tranches de dette (>3 creanciers financiers) | Negociation complexe, risque de holdout | -1 point |
| Passif fiscal >6 mois de CA | Le Tresor sera creancier prioritaire agressif | -2 points |
| AGS avancee importante (>500K EUR) | Remboursement AGS = priorite absolue post-reprise | -1 point |

**Red flags operationnels lies a la dette** :
- Cash burn rate >4 semaines de tresorerie : risque de cessation de paiement imminente
- DSO en forte hausse : les clients sentent la fragilite et retardent les paiements
- Fournisseurs passent en paiement comptant : signal que le credit fournisseur est epuise
- Impossibilite de renouveler l'assurance-credit : signal de marche sur la solvabilite

---

### 7.3 Opportunites LBO distressed

**Criteres de filtrage Brantham pour cibles LBO distressed** :

| Critere | Seuil | Raison |
|---|---|---|
| CA | >3M EUR | Masse critique pour interesser un repreneur professionnel |
| EBITDA normalise | >0 (meme faible) | L'entreprise a un potentiel de profitabilite |
| Effectif | >20 salaries | Critere tribunal pour maintien de l'emploi |
| Leverage actuel | 4-8x EBITDA | Zone de restructuration (trop bas = pas distressed, trop haut = insauvable) |
| Actifs tangibles | >1M EUR | Securise le financement et offre un plan B (sale-leaseback) |
| Secteur | Non-cyclique ou en bas de cycle | Potentiel de retournement avec la reprise du cycle |
| Nombre de creanciers | <5 financiers | Negociation simplifiee |
| Dirigeant cooperatif | Oui | Facilite la transition et la due diligence |

**Schema type d'acquisition distressed via Brantham** :

```
1. SOURCING (pipeline automatise)
   - Scan BODACC/infogreffe/AJ pour RJ/LJ avec CA >3M
   - Scoring automatique (agent Brantham)
   - Pre-qualification (agent Director)

2. APPROCHE (J+1 a J+7)
   - Contact AJ/MJ responsable
   - Data room express (comptes, contrats, effectifs)
   - Go/No-go rapide basé sur la checklist 7.1

3. STRUCTURATION (J+7 a J+21)
   - Offre en plan de cession (L642-2) :
     * Prix de cession = valeur liquidative + prime pour continuite
     * Engagements sociaux : maintien emploi, formation
     * Engagements investissement : CAPEX, BFR
   - OU offre en conciliation/pre-pack (L611-7) :
     * Rachat de dette a decote + recapitalisation
     * A&E de la dette restante

4. FINANCEMENT
   - Equity : repreneur industriel ou fonds PE
   - New money : banques existantes (privilege L611-11) + BPI France
   - Sale-leaseback : monetisation actifs immobiliers
   - Affacturage : financement BFR immediat

5. POST-ACQUISITION (M+1 a M+12)
   - Mise en place 13-week cash flow
   - Quick wins (voir section 5.3)
   - Business plan de retournement (voir section 5.1)
   - Reporting mensuel au comite de pilotage
```

**Fee structure Brantham** :
- Retainer : 5K-15K EUR/mois pendant la phase de recherche
- Success fee : 3-5% du TEV (Total Enterprise Value) de la transaction
- Minimum fee : 50K EUR par transaction completee
- Fee additionnelle pour structuration financiere : 1-2% du montant restructure

---

## Annexe : Glossaire des termes cles

| Terme | Definition |
|---|---|
| A&E | Amendment & Extend — modification des termes du credit avec extension de maturite |
| AGS | Association pour la Gestion du regime de garantie des creances des Salaries |
| AJ | Administrateur judiciaire |
| BFR | Besoin en fonds de roulement |
| BP | Business plan |
| Cash sweep | Remboursement anticipe base sur l'excedent de tresorerie |
| Cram-down | Imposition d'un plan a une classe de creanciers dissidente |
| CRO | Chief Restructuring Officer |
| Cross-default | Clause provoquant le defaut sur un credit en cas de defaut sur un autre |
| DIO | Days Inventory Outstanding |
| DIP | Debtor-In-Possession (financement post-procedure, concept US) |
| DPO | Days Payable Outstanding |
| DSCR | Debt Service Coverage Ratio |
| DSO | Days Sales Outstanding |
| Fulcrum security | Tranche de dette ou la valeur de l'entreprise coupe — ses detenteurs controlent la negociation |
| Haircut | Reduction du nominal d'une creance |
| Headroom | Marge de manoeuvre entre le cash disponible et le minimum vital |
| IBR | Independent Business Review |
| LJ | Liquidation judiciaire |
| MJ | Mandataire judiciaire |
| New money | Apport frais de tresorerie dans le cadre d'une conciliation |
| NPL | Non Performing Loan (pret non performant) |
| PIK | Payment-In-Kind (interet capitalise, pas paye en cash) |
| PSE | Plan de sauvegarde de l'emploi |
| RCF | Revolving Credit Facility |
| Recovery rate | Taux de recouvrement d'une creance |
| RJ | Redressement judiciaire |
| SPV | Special Purpose Vehicle |
| TEV | Total Enterprise Value |
| TWCF | Thirteen-Week Cash Flow |
| Waiver | Renonciation du creancier a invoquer un event of default |
| Waterfall | Cascade de distribution du prix entre creanciers par rang |

---

## Voir aussi

- [[brantham/knowledge/finance/valorisation-distressed]] — Methodes de valorisation et decotes par procedure
- [[brantham/knowledge/procedures/mandat-ad-hoc-conciliation]] — Procedures amiables et privilege new money
- [[brantham/knowledge/legal/rang-des-creances]] — Ordre de priorite et suretes en procedure
- [[brantham/knowledge/finance/financial-modeling-distressed]] — Waterfall analysis et recovery rates
- [[brantham/knowledge/legal/plans-de-cession]] — Cadre legal de la cession d'entreprise
- [[brantham/knowledge/finance/fiscalite-restructuration]] — Traitement fiscal des abandons de creances et conversions
- [[brantham/knowledge/legal/suretes-en-procedure-collective]] — Nantissements, hypotheques et gages
- [[brantham/knowledge/acteurs/banques-cellules-restructuring]] — Acteurs bancaires du restructuring
- [[brantham/knowledge/process/turnaround-operationnel]] — Plan de retournement et cash management
- [[brantham/knowledge/glossary/glossaire-distressed]] — Terminologie M&A distressed

## Related
- [[brantham/_MOC]]
- [[brantham/knowledge/procedures/sauvegarde-acceleree-sfa]]
- [[brantham/knowledge/finance/assurance-credit]]
- [[brantham/knowledge/market/cas-casino-groupe]]
- [[brantham/knowledge/process/integration-post-acquisition]]
