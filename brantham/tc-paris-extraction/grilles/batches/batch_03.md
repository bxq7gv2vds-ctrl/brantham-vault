---
type: batch_log
project: brantham
batch: 03
created: 2026-05-15
tags: [tc-paris, extraction, batch]
---

# Batch 03 — 8 dossiers TC Paris (4 NEW + 4 classiques)

## Dossiers traites

| Dossier | Folder | Nb offres | Confidence | PDF lu |
|---|---|---|---|---|
| NEW-SCOOT | NEW_32 - SARL SCOOT PARIS 16 | 1 | high | oui (4p) |
| NEW-MGL | NEW_47 - SAS MGL (Lolly's) | 1 | medium | non (PDF 102MB) |
| NEW-ARANA | NEW_57 - SAS ARANA FACILITIES | 1 | high | oui (20/24p) |
| NEW-AXIOVAL | NEW_62 - SAS AXIOVAL | 3 (offres successives) | high | oui (20p couvrant v1+v2) |
| 11-CLAYE | 11 - ASSOCIATION MEDICO DENTAIRE CLAYE SOUILLY | 1 | high | oui (15p) |
| 12 | 12 - SAS ALDADDY | 1 | medium | non (CSV exhaustif suffit) |
| 18 | 18 - SARL 3S OPTIC | 1 | high | oui (13p) |
| BAC | 19 - SAS BAC COMMUNICATION | 2 (initiale + amelioree) | high (BAC-01) / medium (BAC-02) | oui (8p BAC-01) |

**Total : 11 offres + 8 fiches dossier = 19 JSONs ecrits.**

## Fichiers JSON crees

### Offres (11)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/NEW-SCOOT-01.json` — Enis BEN TAARIT (PP, salarie CDD repreneur, scooter Paris 16)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/NEW-MGL-01.json` — YN INVEST (Yves TIRMAN, groupe YT CAPITAL / LA CHAISE LONGUE) sur Lolly's
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/NEW-ARANA-01.json` — GR WELCOME SERVICES (Stephane ACTIS, groupe GR) sur ARANA accueil B2B
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/NEW-AXIOVAL-01.json` — FCL v1 (13/04/2026, 4 emplois, rejetee par MJ)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/NEW-AXIOVAL-02.json` — FCL v2 amelioree (22/04/2026, +1 emploi, engagement non-licenciement 24 mois)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/NEW-AXIOVAL-03.json` — FCL v3 post-LJ (24/04/2026, redecomposition prix 28/2)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/11-CLAYE-01.json` — MEDIVI (Haddouk, reseau PLACE DENTAIRE 29 centres) sur centre dentaire
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/12-01.json` — BRUMES SAS (Charles YVON, Cherbourg) sur marque NUS
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/18-01.json` — SAS LEV / EYES ONE (Ilan LEVY, deja franchise EYESHOW) sur 3S OPTIC
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/BAC-01.json` — J.L 13 RUE GRANGE BATELIERE v1 (BERREBI, cousin 2e degre SITBON)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/BAC-02.json` — J.L 13 RUE GRANGE BATELIERE v2 amelioree

### Dossiers (8)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/NEW-SCOOT.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/NEW-MGL.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/NEW-ARANA.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/NEW-AXIOVAL.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/11-CLAYE.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/12.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/18.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/BAC.json`

## Patterns saillants extraits

### Pattern 1 — Repreneur "salarie en place" (NEW-SCOOT)
PP exerçant en CDD chez la cible, 25 ans de metier, offre 10k€ + 45k€ charges aug (travaux mise aux normes). Reprend 1/2 salaries (l'autre = ROUACH arret maladie 2 ans). Pas de vehicule juridique = exploitation directe par PP. Bailleur accepte verbalement — CS n°1 = confirmation ecrite. Document manuscrit ultra-leger (lettre + chèque consignation + L.642-3).

### Pattern 2 — Concurrent direct du meme secteur (NEW-ARANA / NEW-AXIOVAL)
Profil-robot du repreneur "gagnant probable" : meme NAF + meme zone geographique + groupe profitable avec RSE + reprise massive emplois (90%+) + BP synergique chiffre + avocat top tier (CMS pour ARANA / Guarrel pour AXIOVAL) + aucune CS exotique. ARANA = 24 pages structurees Docusign, AXIOVAL = 3 itérations (v1 → v2 reponse aux observations MJ → v3 confirmation post-LJ).

### Pattern 3 — Dirigeant créant société concurrente pendant procedure (BAC + AXIOVAL)
- **AXIOVAL** : Frédéric MALET crée CAP2-PUBLIC (RCS Saint-Quentin) le 04/03/2026 pendant le mandat ad hoc — exclu de la reprise via L.642-3. Repreneur exploite cette exclusion comme argument.
- **BAC** : Didier SITBON, pas de société concurrente mais offre proposée par cousin 2e degre (BERREBI) — application L.642-3 inverse = requete parquet.

### Pattern 4 — Offre "à compléter" avec placeholders (11-CLAYE)
MEDIVI dépose un dossier 10 pages très carré (Docusign Haddouk) avec **prix LAISSÉ EN PLACEHOLDERS [3]€ HT / [1]€ incorporels** — geste politique de marquer le terrain en attendant ARS/data room. Pattern à classer : "intention forte + chiffrage absent" = risque rejet pour défaut de prix sincère et serieux.

### Pattern 5 — Coquille à marque (12 - ALDADDY)
Société sans salariés à la date du depot. Périmètre = marque NUS + stocks + PI. Volet social neutralisé. Évaluation 100% commerciale (BP). Pattern complementaire au pattern Houseboard/marque pure : ALDADDY = lin/textile premium BtoB, repreneur BRUMES SAS holding ad hoc fresh (cap 1k€, créée 11/08/2025).

### Pattern 6 — Franchise existante + soutien fondateur (18 - 3S OPTIC)
Ilan LEVY exploite déjà magasin franchisé EYESHOW Boulogne (CA 1,4M€). Courrier soutien Cohen (fondateur EYESHOW) garantissant nouveau contrat franchise pour EYES ONE = signal massif crédibilité tribunal. Audience seulement 7 jours après dépôt (9 janv → 16 janv 2026) — timing extrêmement tendu. Prix 1k€ symbolique mais coût économique réel = 121k€ (dépôt bail).

### Pattern 7 — Cherry-picking multi-magasin (NEW-MGL)
YN INVEST cible 2/8 magasins Lolly's (Paris Forum Halles + Bordeaux Ste-Catherine). Pattern à risque vs Minelli (refus tribunal pour offres partielles 4/21). Difference cruciale ici : adossement LA CHAISE LONGUE (75 magasins, CA 168M€ groupe YT) = industriel sectoriel solide. Précédent positif : YT a déjà fait plan de cession ARTES → 12 magasins en 2021. À surveiller.

## Anomalies detectees

1. **MGL PDF 102MB** — non extractible directement (limite outil), informations issues du CSV très détaillé (340 pages comprenant 11 annexes : Kbis, plaquettes CMP+LCL, jugement TC Paris 08/04/2021, statuts, comptes consolidés YT CAPITAL 2024, comptes sociaux YN INVEST 2022/2023/2024, liste postes repris, passeport Tirman).

2. **CLAYE prix placeholders** — `[3] € HT` total ventilé en `[1] €` incorporels + `[1] €` corporels + `[1] €` stocks. Pattern critique à signaler : offre signée Docusign mais sans prix chiffré sincère et sérieux. À recouper avec ce qui s'est passé à l'audience (offre améliorée jamais déposée publiquement ou prix complété juste avant ?).

3. **3S OPTIC double fichier** — `40_SARL_3S_OPTIC_offre1.pdf` et `offre_01_gd72771489.pdf` font la même taille (938K) — probablement même MD5. Une seule offre extraite.

4. **ALDADDY 14 JPGs** — `offre_01_gd74678673-1_1.jpg` à `-14_1.jpg` + `offre_01_gd74678673.pdf`. Le CSV est suffisamment détaillé pour ne pas avoir à parcourir les JPGs un par un.

5. **AXIOVAL passage conciliation → LJ** — pattern intéressant : pré-pack cession qui bascule en LJ avec poursuite d'activité parce que le dirigeant régularise unilatéralement une déclaration de cessation des paiements. Sanchez-Sepval garde le dossier (mandataire ad hoc → conciliatrice → liquidatrice). Trois offres successives sur ~10 jours.

6. **CSV BAC séparateur ;** — `dossiers_BAC_COMMUNICATION.csv` utilise des `;` alors que les autres CSVs utilisent `,`. À normaliser pour la suite (script merge).

## Champs systematiquement vides sur ce batch

- `juge_commissaire` : absent dans 5 dossiers / 8
- `date_audience_cession` : absent dans 6 dossiers / 8 (seul 3S OPTIC explicite 16/01/2026 14h30)
- `effectif_total` (salaries cible) : absent dans 3 dossiers / 8 (CLAYE, ALDADDY, 3S OPTIC)
- `ca_dernier_exercice_eur` cible : absent dans 8/8 (ne figure que dans les comptes consolidés repreneur)
- `ca_an2_eur` / `ca_an3_eur` : seuls ALDADDY et BAC fournissent un BP 3 ans explicite
- `dldo` : absent NEW-SCOOT (PDF ne contient que l'offre, pas le cahier des charges) et plusieurs autres
- `cautionnement_personnel` : jamais mentionne
- `annexes_lettres_soutien_collectivites` : aucun cas sur ce batch
- `nb_offres_concurrentes` : 1 par dossier (par construction du dataset — 1 PDF par dossier)

## Issues / suggestions Phase 2

1. **AXIOVAL est un cas d'école 3 itérations rapides** — coder les "offres successives même repreneur" comme un mini-pipeline observable. La v2 répond exactement aux 3 reproches MJ (volet social, pérennité, prix insuffisant) → +1 emploi, BP chiffré, engagement non-licenciement 2 ans. La v3 ajuste juste la décomposition prix (28/2 vs 20/10) et étend frais rédacteur 1500→3000€. Pattern réutilisable : « comment passer de rejet MJ à plan retenu en 11 jours ».

2. **Pattern parenté L.642-3** (BAC) à indexer explicitement dans le schema dossier : `parente_repreneur_dirigeant_degre` (int, null par défaut). Distingue les cas qui nécessitent requête parquet. Précédent dans gagnants-tribunal : Sayada/Minelli L.642-3 alors qu'il était dirigeant historique de San Marina → rejet.

3. **Pattern "prix placeholders"** (CLAYE) — Phase 2 doit calculer combien d'offres déposent avec placeholders et regarder le taux d'acceptation. Hypothèse : faible (les TC veulent un prix sincère et sérieux ferme au dépôt).

4. **Pattern "charges augmentatives > prix"** — NEW-SCOOT 10k+45k (450%), 18-01 1k+120k (12000%) — chiffrer dans Phase 2 le ratio CA / prix vs CA / coût économique total pour les retail/optique avec bail. Le tribunal pourrait préférer le coût économique total.

5. **BAC offre "améliorée" qui RÉDUIT le volet social** (2→1 emplois) — anomalie. Compense par +200k€ relance commerciale, mais le tribunal regarde d'abord emplois. À surveiller comme contre-exemple du pattern AXIOVAL.

6. **NEW-MGL cherry-picking 2/8 magasins** vs Minelli cherry-picking 4/21 → comparer la decision tribunal sur Lolly's quand elle sera connue. Le pattern industriel sectoriel (LCL, 75 magasins) sera-t-il suffisant pour casser le pattern "rejet partiel" identifié sur Minelli ?

## Recap (<100 mots)

Batch 03 : 11 offres + 8 fiches dossier extraites pour 8 dossiers TC Paris. 7 patterns saillants identifiés (salarié-repreneur, concurrent direct sectoriel, dirigeant créant société concurrente, offre placeholders, coquille à marque, franchise+soutien fondateur, cherry-picking multi-magasin). Cas d'école AXIOVAL : 3 offres FCL successives répondant aux observations MJ → offre retenue probable. Anomalies critiques : MEDIVI prix placeholders `[3]€`, BAC repreneur cousin 2e degré (L.642-3 inversé), BAC v2 réduit emplois 2→1. PDF MGL 102MB non-extractible, fallback CSV exhaustif. Tous JSONs valides schéma.

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_01]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_22]]
