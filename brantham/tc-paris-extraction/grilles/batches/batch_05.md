---
type: batch-log
batch_id: 05
dossiers_traites: 7
offres_extraites: 21
date: 2026-05-15
agent: claude-agent
tags: [tc-paris, batch, extraction]
---

# Batch 05 — Dossiers 14-HBBS / 16-UMAKAYU / 36-DN / 58-LAUNAY / 65-LA-LOCO / 66-VAULEARD / NEW-FAIRSPACE

## Fichiers JSON crees

### Dossiers (7)
- `dossiers/14-HBBS.json` — SARL HEAD BODY BEST SECURITE (securite privee)
- `dossiers/16.json` — SAS UMAKAYU (Kintaro Cafe / Cafe Maru)
- `dossiers/36-DN.json` — SAS D&N ASSOCIES (Air Indemnite)
- `dossiers/58.json` — SCA DE LAUNAY (arboriculture INNATIS)
- `dossiers/65.json` — SAS LA LOCO (Le Wagon EdTech)
- `dossiers/66.json` — SCEA DOMAINE DE VAULEARD (arboriculture INNATIS)
- `dossiers/NEW-FAIRSPACE.json` — SAS FAIRSPACE (mobilier reconditionne ESUS)

### Offres (21)
- HBBS : `14-HBBS-01/02/03.json` (01=02 doublon GROUP CLEAR, 03 ALTER-PROTECT)
- UMAKAYU : `16-01/02/03.json` (BUHI BUHI, TCS HOLDING/NOKCHA, SUN x2)
- D&N : `36-DN-01/02/03.json` (INDEMNIFLIGHT, Reclamaciones Generales SL, Yource BV)
- LAUNAY : `58-01/02/03.json` (CASTEL+LEROY+VCAPITAL amelioree, CELHER amelioree, CASTEL+LEROY+VCAPITAL initiale)
- LA LOCO : `65-01/02/03.json` (STUDI/Galileo, FORMAPRIV, SIMPLON.CO)
- VAULEARD : `66-01/02/03.json` (CELHER amelioree, CELHER initiale, CASTEL+LEROY+VCAPITAL)
- FAIRSPACE : `NEW-FAIRSPACE-01/02/03.json` (BLUEDIGO NEXT — 3 PDFs doublons stricts, UNE seule offre unique)

## Anomalies detectees

1. **HBBS : doublon strict offre1 = offre2 (GROUP CLEAR)** — meme contenu, meme date 13/04/2026, memes annexes Kbis/plaquette/bilans. MD5 binaires differents mais contenu strictement identique. Probablement second depot greffe vs AJ. A ne pas comptabiliser comme deux offres distinctes pour la decision du Tribunal.
2. **HBBS asymetrie tres marquee** : GROUP CLEAR 10001 EUR + 54 emplois MAIS 4 CS dont non-application L.642-12 al.4 (= asset stripping) ; ALTER-PROTECT 50000 EUR + 22-25 emplois SANS CS. Pattern dilemme tribunal : maximiser emplois (CLEAR) vs securiser execution (ALTER-PROTECT).
3. **UMAKAYU triple compromis** : 3 offres ciblent des compromis incompatibles. BUHI BUHI 5K + tous (2 fonds 19 emplois) MAIS frere du dirigeant (L.642-3 derogation requise). TCS HOLDING 75K + UNIQUEMENT 57 Petits Champs avec 1 salarie sur 6. SUN 50K + Cafe Maru complet (2 adresses) + 6/7 salaries sans CS. Tribunal aura a arbitrer perimetre vs prix vs emplois.
4. **D&N pattern "asset stripping marque only" Reclamaciones Generales SL** : qualifiee expressement "cession d'actifs isoles" (marque + domaines + frontend uniquement). Evite L.642-7 transfert contrats globaux et reprise du fonds. Aucun salarie, aucun client repris. Pattern interessant : strategie pour eviter contraintes legales liees au fonds.
5. **D&N incoherences lettres vs chiffres Yource** : "soixante mille euros" en lettres pour 75000 chiffres et "quarante mille euros" en lettres pour 25000 chiffres. Possible source de contestation.
6. **D&N 36 = plan de cession SUITE A RESOLUTION DE PLAN DE SAUVEGARDE** — pattern rare. Le plan de sauvegarde du 22/08/2024 a ete resolu par jugement du 13/01/2026 du TAE Paris. Ouvre direct sur plan de cession (pas de RJ intermediaire).
7. **LAUNAY/VAULEARD/INNATIS — issue connue : Vergers d'Anjou cooperative retient le pole pour 7M EUR** (jugement 30/04/2026, source Reussir Fruits & Legumes + Les Echos). CELHER/BOUJUAU = apporteurs cooperative Vergers d'Anjou (proximite ANGERS) = bras armes apparent du repreneur final. CONSORTIUM CASTEL+LEROY+VCAPITAL (Sarthe 72 + Paris 75) = ECARTE. Argument tribunal verbatim : "Projet cooperatif local coherent ; capacite de stockage Les Vergers d'Anjou passe de 36 000 t a 49 000 t". Pattern fort : tribunal privilege LOCALISATION GEOGRAPHIQUE + COOPERATIVE LOCALE sur capacite financiere superieure du concurrent.
8. **LAUNAY meme prix 50K EUR entre les 2 offres concurrentes** (CELHER vs CASTEL+LEROY+VCAPITAL) — donc le tribunal a tranche sur QUALITATIF (emplois 3/3 vs 2/3 + CS 1 vs 7 + projet cooperatif local vs consortium financier). Bel exemple "prix egal mais qualite tres differente".
9. **LA LOCO (Le Wagon) — asymetrie x100000 sur le prix** : STUDI 200003 EUR vs FORMAPRIV 50K EUR vs SIMPLON 2 EUR. STUDI = GGE (CA 1.4Md, tresorerie 479M), BP detaille, discussions in bonis depuis novembre 2025. SIMPLON 2 EUR symboliques mais avec engagement maintien 12 mois (ESS/ESUS pure player). FORMAPRIV preliminaire incomplete (donnees recues la veille DLDO).
10. **VAULEARD CELHER paye 2x plus que pour LAUNAY** (100K vs 50K) pour des actifs comparables — explication probable : Vauleard a Feneu 49460 = proximite geographique forte avec le siege CELHER 49140 + 5 emplois (vs 3 LAUNAY). Signal de strategie cooperative : prix plancher reglementaire chez LAUNAY (50K = identique au concurrent ecarte) et premium chez VAULEARD pour montrer la conviction strategique.
11. **FAIRSPACE — 3 PDFs deposes au greffe IDENTIQUES (offre_01, offre_02, offre_03)** — meme envelope Docusign ID 3BEF6B84-1B0D-8270-839E-122C1F719760, memes images page par page (md5 PNG identiques), memes horodatages a la seconde pres (07/05/2026 10:27:05/06/07 CEST). Difference binaire MD5 = serialisation Ghostscript et non contenu. UNE seule offre unique BLUEDIGO NEXT. Pattern de depots multiples redondants (probablement exigence greffe x exemplaires).
12. **FAIRSPACE — offre plancher 10000 EUR + capex 100K EUR** : pattern "engagement par le capex post-reprise plutot que par le prix d'achat" — le repreneur signale sa conviction par l'enveloppe d'investissement immediate (gouvernance, reactivation pipeline, formation equipes, structuration process) plutot que par un prix d'acquisition eleve. Offre unique sans concurrence (effet rente de monopole sur l'offre repreneur). Repreneur tres aguerri : 3 reprises a la barre (Pramana 2023 cedee a PwC, Rutabago 2022 cedee Groupe Les Commis via RJ, BLUEDIGO 11/2024) + transformation BLUEDIGO triplement marge brute (8-12% -> 28%).

## Champs ou l'info manquait systematiquement

- `cible_siren` : absent dans HBBS et FAIRSPACE (PDFs scannes / champs non extraits)
- `dldo` : absent dans UMAKAYU et FAIRSPACE
- `juge_commissaire` : absent dans HBBS uniquement renseigne (M. SERERO) ; absent dans tous les autres
- `date_audience_cession` : absent partout sauf LAUNAY/VAULEARD (13/04/2026)
- `nb_pages_total/corps/annexes` : absent dans presque tout (PDFs scannes pour HBBS/FAIRSPACE/D&N — pdftotext renvoie 0 lignes)
- `qualite_redactionnelle` : marquee "NR" pour HBBS-01/02 (PDF non extractible)
- `ebitda_an3_eur` : presque jamais chiffre — seul UMAKAYU 16-01 donne 97K EUR an3
- `caution_dirigeant_*` : jamais renseigne sauf FAIRSPACE (Younes El Hajjami Garant L.626-10)

## Issues confirmees (gagnants-tribunal.md)

- **INNATIS Pole Val de Loire (LAUNAY + VAULEARD + 9 autres)** = Vergers d'Anjou retenu, CASTEL+LEROY+VCAPITAL ecarte. Marque `cette_offre_retenue: "oui"` pour 58-02 et 66-01 (CELHER apporteurs Vergers d'Anjou) + `"non"` pour 58-01/58-03/66-03 (consortium) + `"amelioree_puis_retenue"` pour 66-02 (initiale CELHER amelioree).
- 5 autres dossiers (HBBS, UMAKAYU, D&N, LA LOCO, FAIRSPACE) : `en_attente` (pas de source publique sur l'issue a date 2026-05-15).

## Hypotheses fortes a verifier post-jugement

1. **LA LOCO** : STUDI/GGE TRES probablement retenu (prix x100000 du concurrent ESS + 69 emplois preserves + BP detaille + discussions in bonis depuis novembre 2025 + capacite financiere ecrasante). Pattern Sym Group/COSA : tribunal privilegie continuite + emplois + financier solide.
2. **D&N** : INDEMNIFLIGHT vs Yource BV serait un choix difficile (memes 100K, memes 1 emploi repris). INDEMNIFLIGHT = repreneur FR avec actionnaires FRISKA/OPY ex-Umanis/CGI (tres solides). Yource BV = neerlandais avec CS approbation Holland Capital. Tribunal probablement INDEMNIFLIGHT (proximite FR + zero CS substantielle + due diligence aboutie + groupe ex-Umanis).
3. **HBBS** : ALTER-PROTECT en avance vs GROUP CLEAR (prix x5 + zero CS + offre claire et structuree vs offre doublon avec CS L.642-12 problematique). Toutefois GROUP CLEAR reprend 54 emplois vs 22-25 ALTER-PROTECT — peut etre l'argument decisif si le tribunal privilege le volume social pur. Pattern incertain.
4. **UMAKAYU** : tres incertain. BUHI BUHI a le perimetre le plus large (2 fonds + 19 emplois) mais L.642-3 derogation = signal politique negatif. TCS HOLDING le prix le plus haut (75K) mais perimetre tres limite (1 salarie sur 6). SUN equilibre (50K + 6/7 emplois + Cafe Maru complet) — probable favori.
5. **FAIRSPACE** : offre UNIQUE BLUEDIGO NEXT, donc retenue sauf rejet pour insuffisance — possible si le tribunal estime que 10K EUR prix + 100K capex est insuffisant pour preserver les 2 emplois. Pattern previsible : retenue par defaut.

## Suggestions d'amelioration du schema

1. **Ajouter champ `prix_par_emploi_repris`** dans `structure_prix` : `prix_total / nb_emplois` — particulierement parlant pour HBBS (CLEAR 185 EUR/emploi vs ALTER 2000 EUR/emploi) et VAULEARD (CELHER 20K/emploi vs LAUNAY 25K/emploi).
2. **Ajouter `enveloppe_capex_post_reprise_eur`** distinct de `capex_montant_eur` du BP : pattern FAIRSPACE (10K prix + 100K capex immediate) montre que le signal d'engagement peut etre dans le capex et non le prix.
3. **Ajouter `lien_familial_dirigeant`** booleen dans `profil_repreneur` : pattern UMAKAYU 16-01 BUHI BUHI (frere du dirigeant Umakayu — L.642-3 derogation requise).
4. **Ajouter `proximite_geographique_avec_cible_km`** dans `profil_repreneur` : pattern VAULEARD/LAUNAY ou la proximite (Boujuau 49 vs Castel/Leroy 72) est probablement decisive.
5. **Renforcer `meta.note_doublons`** comme champ standardise : pattern FAIRSPACE (3 PDFs Docusign identiques) et HBBS (2 PDFs GROUP CLEAR identiques) recurrent et meriterait un champ dedie pour traitement automatique aval.
6. **Ajouter `offre_preliminaire_incomplete`** booleen : pattern LA LOCO 65-02 FORMAPRIV (donnees recues la veille DLDO, conditions/previsions/financement non realises) et 65-03 SIMPLON (audit non finalise). Tribunal peut ecarter sur cette base.

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_01]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_22]]
