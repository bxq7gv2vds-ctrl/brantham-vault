---
type: batch_log
project: brantham
batch: 20
created: 2026-05-15
tags: [tc-paris, extraction, batch, fhbx, balthazar, immobilier]
---

# Batch 20 — FHBX Balthazar : ARCUEIL MONTREUIL (08) + COROT (16) + FS ET CIE (47)

## Contexte commun

Les 3 dossiers font partie du **groupe consolidé FHBX "Foncière Melot-Gouband / Affaire Balthazar"** (26 entités SCI/SNC/SC immobilières). Vagues RJ entre 29/04/2025 et 23/12/2025. DLDO unique : **02/03/2026**. Organes uniques :
- AJ : Maître Hélène BOURBOULOUX (SELARL FHBX, Neuilly) avec F. RAYBAUD et P. CHARREY
- MJ : Maître Valérie LELOUP-THOMAS (SELAFA MJA)
- Juge-commissaire : Monsieur Jean-François PONCET
- Tribunal : Tribunal des Activités Économiques de Paris

Groupe de fait Melot-Gouband fondé 1997 (~50 sociétés), porté par SC Balthazar Invest (assignée 20/02/2025 par société de crowdfunding). Crise immo post-2022 (hausse taux 1%→4%) + refinancements onéreux + montages intra-groupe complexes = défaillance en chaîne.

## Dossiers traités

| Dossier ID | Folder | Nb offres extraites | Confidence |
|---|---|---|---|
| 08-SCI-ARCUEIL | 08 - SCI ARCUEIL MONTREUIL | 12 | high (LABRAX, VERDOSO) / low (MUVICO >5MB, JADO, UNKNOWN) |
| 16-SNC-COROT | 16 - SNC COROT | 12 | high (LABRAX, VERDOSO, LALEYE) / low (MUVICO >5MB, JADO, UNKNOWN) |
| 47-SC-FS-CIE | 47 - SC FS ET CIE | 12 | high (LABRAX, VERDOSO) / low (MUVICO >5MB, JADO, UNKNOWN) |

**Total : 36 offres + 3 fiches dossier = 39 JSONs écrits.**

Note d'ID : utilisation des suffixes descriptifs `-SCI-ARCUEIL`, `-SNC-COROT`, `-SC-FS-CIE` pour éviter conflit avec les dossiers 08 (SAS HAWKSWELL) et 16 (SAS UMAKAYU) déjà présents dans `offres/`.

## Repreneurs récurrents (FHBX)

5 archétypes apparaissent systématiquement sur les 3 dossiers (12 offres = mêmes candidats que sur AMIRAL MAIGRET / ADELE FIRMIN du batch 22) :

### 1. LABRAX INVEST — offre globale 21M€ portefeuille
- SAS 10k€ capital, RCS 901813741 Paris. Président Edouard LAMY.
- Offre Finale 02/03/2026 : **21.000.000€ net vendeur, indivisible, AUCUNE CS** (sauf conditions de droit vente d'immeuble).
- Périmètre = Offre Initiale 09/02 + appartement lot 35 av Théophile Gautier Paris 16e.
- **Options de repli détaillées Trouville-sur-Mer** : Option 1 (SNC Amiral Maigret + SNC Corot 6 Place F. Mourreaux) 1.3M€ ; Option 2 (Amiral Maigret seul) 1.025M€. Visite 30/10/2025. 3 offres antérieures (15/10, 14/11, 01/12/2025).
- Fonds propres déclarés suffisants. Dépôt 5% à promesse.
- 2 pages, lettre simple, ton juridique propre. PDF léger (124k).

### 2. VERDOSO SAS — plan de cession 26 entités
- SAS 3.249.428€ capital, RCS 789095999 Paris. Société mère Verdoso Investments SA (Luxembourg). Fondé 1997 par Franck Ullmann (Mines Paris + Wharton).
- **Track record : Compte R (2024), The Kooples (2025), Geismar (2025), 34 opérations depuis 1997, 14 sociétés en portefeuille, CA agrégé >600M€, 3.000 emplois, 18 cessions, 300M€ fonds propres dont 50M€ disponibilités.**
- Prix : **250.002€ "provisoire"** mais valorisation économique des actifs repris déclarée à **11 millions d'euros**. Écart majeur à parfaire à l'amélioration.
- Faculté de substitution explicite. Docusign présent (CC859BA0... ou EBE6E276).
- 26 pages, sommaire détaillé, exécutive summary, KBIS + CNI en annexe. Audit non finalisé = condition implicite.

### 3. MUVICO (Victor COHEN) — asset deal par actif
- Groupe foncier patrimonial, 198 av Victor Hugo 75116 Paris.
- Offre globale Foncière Melot-Gouband en 2 vagues : **initiale 09/02/2026** + **améliorée 02/03/2026**.
- Prix individualisés par entité :
  - SCI ARCUEIL MONTREUIL : 280k€ initiale / 290k€ améliorée
  - SNC COROT : 120k€ initiale / 130k€ améliorée
  - SC FS ET CIE : non communiqué dans la table CSV
- PDFs **>5MB non extraits** — analyse qualitative impossible. 3 PDFs MUVICO par dossier (redondance multi-SCI).

### 4. Groupe JADO + PARTNER CONSULTANCY SERVICES FRANCE
- Alexandre-Igor (groupejado.com) + Stéphane ROIG.
- Avocat : **Me Augustin LACCOURS, MONCEY AVOCATS** (6 rue Léo Délibes 75116 Paris).
- Offre Balthazar VMoncey, 23 pages. Prix individualisés non extraits — PDF à retraiter.

### 5. HOUSEBASE (Philippe ZERR)
- SAS 49.780€, RCS 908068331 (20 Quai Duguay-Trouin Rennes).
- **PDF mal classé** dans plusieurs dossiers FHBX : offre cible en réalité SNC ADONIA (30 rue Étienne Dolet 94230 Cachan) à 501.600€.
- Offre dédiée distincte présente dans certains dossiers (08-04, 16-04) — détails à préciser.

### 6. Groupe LALEYE — UNIQUE au dossier COROT (offre 16-SNC-COROT-05)
- Groupe familial **30 ans** marchand de biens. Alidou LALEYE (Dauphine) + Brian LALEYE (ESCP).
- **Centaine d'opérations**, ~3M€ patrimoine, **11 dernières adjudications listées en annexe**, ~30 locataires gérés.
- Partenaires bancaires historiques : **Banque BCP + Caixa** (30 ans).
- **Asset deals isolés**, prix par actif :
  - SCI Danton-Lilas (2 rue Danton, Pré Saint-Gervais 93061) : **490.000€** — base loyer théorique 87k vs réel 43k @ 8%
  - SNC Amiral Maigret (14 rue Amiral Maigret Trouville) : **450.000€** — base 39.180€ @ 8%
  - SNC ADONIA (30 rue Étienne Dolet Cachan) : **450.000€** — base 36k @ 8%
  - **SNC Corot (4-12 bd Fernand Moureaux Trouville) : 320.000€** — base 31k @ 8% (local commercial Carrefour 81m² avec impayés 20k + T3 67,4m²)
- **Diagnostic structurel exceptionnel** par actif : historique acquisition, refinancement Quintet 2018, dette/valeur, état locatif, contentieux, amiante, taux perception.
- 20 pages, ton technique, BP cohérent loyer×rendement, déclaration L.642-3 signée. Annexes : adjudications + patrimoine + structure groupe + comptes 3 sociétés + CNI dirigeant.
- **Condition essentielle : purge intégrale des sûretés** (sinon offre privée d'effet).

## Anomalies détectées

1. **HOUSEBASE mal classé sur les 3 dossiers** (08-01, 16-01, 47-08) : cible SNC ADONIA, pas l'entité indiquée — récurrent (déjà vu sur AMIRAL MAIGRET + ADELE FIRMIN au batch 22).
2. **6 PDFs MUVICO >5MB non extraits** (offre2 + offre3 + offre5/6/7 sur 08, offres similaires 16/47) — redondance multi-SCI, table de référence CSV utilisée comme proxy.
3. **5 candidats UNKNOWN** (08-07, 16-03, 16-06, 47-01, 47-04, 47-06, 47-09, 47-12) — PDFs originaux à re-traiter pour identification auteur. Particulièrement nombreux sur FS ET CIE (5 UNKNOWN).
4. **LABRAX option 1 indivisible Amiral Maigret + Corot 1.3M€** alors que LABRAX porte aussi sur Arcueil et FS CIE individuellement via offre 21M€ globale — incohérence apparente : l'option 1 ne couvre QUE Trouville, pas tout le portefeuille.
5. **VERDOSO 250.002€ vs valorisation économique 11M€ déclarée** : écart factice de prix de cession affiché vs prix réel attendu — pattern à documenter (offre "provisoire" pour entrer dans la course et améliorer).
6. **Aucune offre LALEYE pour ARCUEIL MONTREUIL ni FS ET CIE** dans les CSV — LALEYE n'a déposé qu'une proposition multi-actifs où ARCUEIL et FS_CIE ne figurent pas dans les actifs ciblés (LALEYE cible Danton-Lilas, Amiral Maigret, Adonia, Corot uniquement).

## Suggestions Phase 2

- **Méta-dossier FHBX Balthazar** : à ce jour 5 dossiers FHBX traités dans les grilles (03 INSULA partielle + 09 AMIRAL MAIGRET + 30 ADELE FIRMIN + 08 ARCUEIL + 16 COROT + 47 FS CIE = **6 entités / 26**). Reste 20 entités à traiter. Phase 2 devra agréger ces dossiers pour une analyse globale (qui prend quoi dans le portefeuille 21M€).
- **Pattern "offre provisoire à parfaire"** (VERDOSO 250k€ vs 11M€) : à coder explicitement dans la grille de scoring — distinguer prix affiché vs prix attendu post-amélioration.
- **Pattern "options de repli stratifiées"** (LABRAX : portefeuille global ou Trouville indivisible ou Amiral Maigret seul) : prouve un travail réel sur le portefeuille, signal de sérieux. À valoriser dans scoring.
- **LALEYE comme cas d'école asset deal** : seul candidat avec diagnostic structurel par actif (loyer réel encaissé vs facial, taux perception CAF, impayés nommés, dette Quintet 2018, état technique). Le tribunal pourrait préférer ce niveau de granularité pour les actifs où la valorisation économique ≠ valorisation théorique.
- **Refinancement Quintet 2018** : récurrent sur tous les actifs FHBX (LALEYE le documente précisément). Hypothèses (cumulées par actif au 06/2025) à recouper pour évaluer le passif réellement purgeable.
- **À retraiter pour Phase 2** : 8 PDFs UNKNOWN/améliorations + 6 PDFs MUVICO + 3 PDFs JADO (23p).

## Recap (<100 mots)

36 offres + 3 fiches dossier extraites pour 3 SCI/SNC/SC FHBX (Balthazar Melot-Gouband). 5 repreneurs récurrents : LABRAX 21M€ aucune CS (options Trouville 1.3M / 1.025M), VERDOSO 250k€ provisoire vs 11M€ valorisation déclarée (track Compte R/Kooples/Geismar), MUVICO asset deal (280-290k Arcueil / 120-130k Corot), JADO via cabinet Moncey (PDFs partiels), HOUSEBASE mal classé (cible Adonia). LALEYE unique au COROT à 320k € (asset deal 4-12 bd F. Moureaux Trouville, diagnostic locataires exceptionnel). 6 MUVICO PDFs >5MB non extraits, 5 UNKNOWN à retraiter, HOUSEBASE mal classé sur les 3 dossiers. Issue globale en attente.

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_22]]
