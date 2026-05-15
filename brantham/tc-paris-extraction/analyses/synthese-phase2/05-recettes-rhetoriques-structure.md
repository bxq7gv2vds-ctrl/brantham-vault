---
type: analyse
project: brantham
phase: phase2
livrable: 05
created: 2026-05-15
tags: [tc-paris, redaction, rhetorique, structure, format]
---

# 05 — Recettes rhétoriques et structure des offres retenues

Analyse du **format, du ton, de la longueur et du vocabulaire** des 47 offres retenues. Pour le rédacteur Brantham : ceci définit le « moule » externe d'une offre crédible.

## 1. Longueur — courte et dense

Nombre de pages total (n=18 winners avec valeur renseignée, n=14 losers) :

| | n | min | P25 | médiane | P75 | max |
|---|---|---|---|---|---|---|
| Retenues | 18 | 8 | 11 | **13,5** | 22 | 47 |
| Rejetées | 14 | 6 | 18 | **30,5** | 43 | 72 |

**Lecture** : la médiane des retenues est **13,5 pages** ; celle des rejetées est **30,5 pages**. Les rejetées sont plus longues, plus denses, plus indigestes.

Décomposition (n=12 retenues avec corps+annexes séparés) :

| Partie | médiane retenues |
|---|---|
| Corps de l'offre | 10 pages |
| Annexes | 4 pages |
| Total | 13-14 pages |

Le corps reste **autour de 10 pages**. Les annexes sont peu volumineuses (4 pages médiane) mais **multiples** (voir §4).

> ⚠️ Limite : n=18 retenues avec champs `nb_pages_*` complets. Certaines offres iconiques (Vergers d'Anjou 35-SICA-01 = 47 pages, 50-03 EURODIF ~50 pages) sortent largement de la médiane. Le pattern « court et dense » s'applique surtout aux offres < 1 M€. Les offres > 1 M€ et multi-sites montent à 30-50 pages mais restent claires.

## 2. Structure dominante

| Structure | Retenues | Rejetées |
|---|---|---|
| **Sommaire détaillé numéroté** | **89,1 %** | 66,7 % |
| Lettre simple | 10,9 % | 22,9 % |
| Mix / NR | 0 % | 10,4 % |

Le sommaire détaillé (sections 1 à 10 avec titres explicites) est **standard** chez les retenues.

## 3. Architecture-type d'une offre retenue (synthèse 47 winners)

Reconstruction à partir des PDFs analysés + cohérence avec le playbook v1 :

```
1. Préambule
   - Référence procédure (n° RG, date jugement RJ, AJ/MJ identifiés)
   - Objet : offre L.642-1 (plan de cession) ou L.642-19 (cession actifs)
   - Société débitrice (raison sociale, RCS, adresse)

2. Le candidat repreneur
   - Identité juridique complète (Kbis annexé)
   - Dirigeants (CNI annexées dans 25 % winners vs 1 % losers)
   - Groupe d'appartenance (organigramme cible annexé : 60 % winners vs 22 % losers)
   - Historique du groupe (CA, RN 3 ans annexés : 59 % winners vs 40 % losers)
   - Track record reprises (médiane 2 reprises antérieures chez winners)
   - Phrase positionnement (1-3 lignes max, voir §6)

3. Périmètre repris
   - Incorporels (médiane 5 489 € chez winners vs 1 000 € chez losers)
   - Corporels (médiane 17 500 € chez winners vs 10 000 € chez losers)
   - Stocks séparés
   - Contrats (bail, crédits-baux, clients critiques)
   - Filiales (le cas échéant)
   - EXCLUSIONS explicites (créances clients antérieures, dettes antérieures, contentieux)

4. Prix de cession
   - Ventilation incorporels / corporels / stocks
   - Net vendeur (vs TTC : préciser)
   - Charges augmentatives séparées (loyers, CP, dépôt garantie, L.642-12 al.4)
   - Modalités : COMPTANT À L'AUDIENCE (74,5 % winners)

5. Reprise des salariés
   - Nombre précis (X / Y)
   - Liste des postes (annexée)
   - Engagement non-licenciement (durée médiane : 24 mois)
   - L.1224-1 : maintien des conditions « oui total » (66 % winners)
   - Mention IRP/CSE (10 % winners — minoritaire mais discriminant)

6. Conditions suspensives
   - Idéalement AUCUNE (40 % winners) ou 1 seule (médiane winners = 1)
   - Si CS : numérotées, exhaustives, datées
   - Agressivité envers dirigeants : « aucune » (87 % winners)

7. Financement
   - Mode (fonds propres / emprunt / mixte)
   - Preuves jointes : attestation bancaire (50 % winners) ou lettre de confort (26 % winners)
   - RIB du compte d'apport (15 % winners)
   - Chèque de consignation si demandé par AJ

8. Faculté de substitution
   - Précise et nominative (80 % winners) — typiquement vers NewCo à constituer

9. Validité de l'offre
   - Date butoir (1-2 mois après audience)

10. Déclarations
    - L.642-3 (absence de lien dirigeants) — signée 77,8 % winners vs 31 % rejetées
    - L.642-12 al.4 (reprise prêts nantis) si applicable

Annexes (ordre typique)
   - Kbis repreneur (84 % winners)
   - CNI dirigeants (25 % winners)
   - CV dirigeants (37 % winners)
   - Attestation bancaire / RIB (50 % winners)
   - Comptes sociaux 3 ans (59 % winners)
   - Business plan détaillé (32 % winners)
   - Organigramme cible (60 % winners)
   - Attestations fiscale et sociale (21 % winners)
   - Lettres soutien (clients/banques/collectivités si pertinent)
   - Signature DocuSign (cas Vergers d'Anjou, 35-SICA)
```

## 4. Top annexes corrélées au succès

(repris de livrable 02 — utilité pour la rédaction)

| Annexe | %retenues | %rejetées | Δ | Recommandation |
|---|---|---|---|---|
| Kbis du repreneur | 84,1 % | 42,0 % | +42 | **Indispensable** |
| Attestation bancaire | 50,0 % | 7,9 % | +42 | **Indispensable si emprunt ou apport >50k€** |
| Organigramme cible | 60,0 % | 22,2 % | +38 | **Indispensable si groupe** |
| CNI dirigeants | 25,0 % | 1,4 % | +24 | Recommandé |
| CV dirigeants | 37,5 % | 15,4 % | +22 | Recommandé |
| Comptes sociaux 3 ans (repreneur) | 59,0 % | 40,3 % | +19 | **Indispensable si SAS / SARL existante** |
| Attestations fiscale et sociale | 21,2 % | 2,8 % | +18 | Recommandé |
| Business plan détaillé | 32,5 % | 18,1 % | +14 | Recommandé |

## 5. Vocabulaire récurrent dans les offres retenues — formules consacrées

Extraction manuelle des formulations qui reviennent chez les winners (verbatim conservé, source dossier en parenthèse) :

### Positionnement / mission

> « Réseau PLACE DENTAIRE / DENTEKA - 30 centres santé dentaire France, CA agrégé 39,3 M€, ~450 salariés »
> (14-COLMAR-02, 14-COLMAR-03, 15-01, 15-03 — formulation copiée x4 fois)

> « Les Opticiens Mobiles est la première entreprise de l'optique reconnue Entreprise Solidaire d'Utilité Sociale par l'agrément ESUS et société à mission. »
> (20-01, 21-SYM-OPTIC-01, 22-SYM-LAB-01 — formulation copiée x3 fois)

> « Coopérative LES VERGERS D'ANJOU — 73 exploitations adhérentes, ~1 600 ha, ~50 000 T fruits, ~50M CA, 26M capitaux propres »
> (35-SICA-01)

**Pattern de positionnement winner** : ouvre par **un chiffre fort** (nombre de centres, CA agrégé, capacité industrielle, label reconnu) → asseoit la légitimité en 1-2 lignes.

### Vision stratégique

> « La pérennité du fonds de commerce d'AXIOVAL passera par une gestion rigoureuse, une bonne considération des salariés et l'activation de synergies avec la société FCL. »
> (NEW-AXIOVAL-01)

> « Capacité stockage passe de 36 000 t à 49 000 t — consolidation amont/aval pôle ligérien »
> (35-SICA-01)

> « Slow tourisme, Clé Verte, Eco Label Européen, Coq Vert »
> (28B-ALPHA-04-SEASONOVA)

**Pattern vision winner** : **synergie chiffrée** ou **label institutionnel** + ouverture vers la pérennité de l'emploi.

### Engagement social

> « Le Repreneur propose de poursuivre l'ensemble des contrats de travail attachés au Fonds de Commerce »
> (01-01, MY LITTLE FINGER 05-08 etc.) — formule standard L.1224-1

> « Maintien emploi 24 mois sans licenciement économique »
> (MY LITTLE FINGER 05-08)

> « Confirme engagement non-licenciement 2 ans, prix 30 k€ ferme »
> (NEW-AXIOVAL-03)

> « 200k€ accompagnement social volontaire »
> (36-LVL-06, Vergers d'Anjou) — **wording « volontaire » est un marqueur winner**

### Justification du prix

> « 15 000 quinze mille euros sont affectés aux titres de participations de la filiale Tunisienne, la société COSA VOSTRA TUNIS »
> (34-01a, Agence IF) — **ventilation par filiale, jamais « ultérieurement »**

> « Actifs incorporels 20 000 € + Actifs corporels 10 000 € + Stock néant = TOTAL 30 000 € »
> (NEW-AXIOVAL-01) — **ventilation chiffrée nette**

### Faculté de substitution

> « Société à constituer (faculté de substitution art. L.642-9 al.3) »
> (formulation standard ~80 % winners)

> « Substitution introduite : ASSOCIATION CENTRE DENTAIRE COLMAR (créée 22/01/2026, Président Ishac HADDOUK) pour exploitation + VIVA SANTE pour reprise baux »
> (14-COLMAR-02) — **substitution nominative et datée**

### Différenciation explicite

> « Rapport qualité-prix supérieur (75k€ vs 40k€ consortium). »
> (37-COOP-03, CAVL — verbatim repris par le tribunal)

> « En France, le Repreneur a notamment, en juillet 2024, présenté une offre de reprise favorablement reçue par le Tribunal de commerce de Paris portant sur les actifs de la société SMALLABLE en plan de cession »
> (50-03, AA Investments HK) — **rappel d'un track record reconnu par le TC Paris**

## 6. Ton dominant des winners

| Ton | Retenues | Rejetées |
|---|---|---|
| **Mixte (juridique + commercial)** | **39,1 %** | 13,5 % |
| Juridique strict | 32,6 % | 47,9 % |
| Technique | 15,2 % | 12,5 % |
| Commercial pur | 8,7 % | 12,5 % |
| Narratif | 4,3 % | 3,1 % |

**Pattern winner** : juridique d'abord (forme L.642), commercial ensuite (vision industrielle, chiffres). Le tout-juridique est froid ; le tout-commercial est non-crédible. **Le mixte est la signature winning**.

Cf. également l'analyse `decortique-offres-gagnantes.md` qui détaille la rhétorique INNATIS / COSA / EURODIF.

## 7. Qualité rédactionnelle

| Qualité | Retenues | Rejetées |
|---|---|---|
| **Claire** | **80,9 %** | 40,2 % |
| Dense | 17,0 % | 38,3 % |
| Confuse | 0,0 % | 2,8 % |

80 % des retenues sont qualifiées de « claires » dans l'extraction (verbiage faible, structure logique, phrases courtes, pas de jargon excessif).

## 8. Signature DocuSign — marqueur de professionnalisme

Présent dans environ 25 % des winners (cas Vergers d'Anjou 35-SICA, 36-LVL, 57-02 ; AA Investments HK 50-03). Quasi-absent chez les losers. **Signal indirect de cabinet d'avocats sérieux** côté repreneur.

## 9. Personnalisation — preuves de due diligence

Les 3 marqueurs de personnalisation chez les winners :

| Marqueur | Retenues | Rejetées |
|---|---|---|
| Étude contrats clients/fournisseurs documentée | 76,9 % | 26,6 % |
| Visite de site | 34,1 % | 15,3 % |
| Rencontre des équipes | 24,3 % | 9,9 % |

Le marqueur **étude des contrats** est le plus discriminant (Δ +50 pts). Inclure une phrase explicite « Le Repreneur a étudié les contrats fournisseurs critiques X, Y, Z dont la continuité est requise pour le redémarrage » est un signal fort.

## 10. Synthèse recettes — ce que copier

Pour rédiger une offre Brantham, copier ces **9 réflexes** des winners :

1. **Sommaire numéroté** 10 sections, **corps 10 pages max**.
2. **Phrase de positionnement** ouvre par chiffre fort ou label.
3. **Vision stratégique** : synergie chiffrée + maintien emploi en 1 phrase.
4. **Prix ventilé** incorporels / corporels / stocks — **jamais « ultérieurement »**.
5. **Comptant à l'audience** ou séquestre — pas de crédit-vendeur.
6. **Aucune CS** ou 1 seule, jamais hostile aux dirigeants.
7. **Engagement non-licenciement 24 mois + L.1224-1 oui total**.
8. **Faculté de substitution précise et nominative**.
9. **Annexes 8 minimum** : Kbis, attestation bancaire, organigramme, comptes 3 ans, CV, CNI, BP, fiscale-sociale.

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/02-anatomie-winners-vs-losers]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/09-bibliotheque-extraits]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/playbook-redaction-offre]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/_index]]
