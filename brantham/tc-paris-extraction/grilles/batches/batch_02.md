---
type: batch-log
batch_id: 02
dossiers_traites: 8
offres_extraites: 7
date: 2026-05-15
agent: claude-agent
tags: [tc-paris, batch, extraction]
---

# Batch 02 — Dossiers 38 / 41 / 42 / 52 / 53 / 54 / 55 / 64

## Fichiers JSON crees

### Dossiers (8)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/38-CHOUETTE.json` — Agtech / Imaging viticulture (10 offres au master, 1 PDF transmis)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/41-LA-PETITE-PARISIENNE.json` — LJ simplifiee, 0 offre (pas de plan de cession possible)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/42-DIXIE-FROG.json` — Label musical (1 offre)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/52-PPA.json` — Imprimerie haut de gamme Montreuil (1 offre)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/53-DAVY.json` — Cafe des Halles (1 offre PP)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/54-MAISON-SOLAIRE-VOLTALIA.json` — Photovoltaique (48 offres au master, 1 PDF transmis)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/55-MYWINDPARTS.json` — Composants eolien (8 offres au master, 1 PDF transmis)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/64-BLACK-TIGER-FRANCE.json` — SaaS data prepack cession (1 offre)

### Offres (7)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/38-CHOUETTE-01.json` — AGREENCULTURE sur CHOUETTE (18,5k EUR + 339k charges, 3 emplois Bordeaux)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/42-01.json` — Music Box Publishing sur DIXIE FROG (6k EUR, 1 emploi, co-editrice historique)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/52-01.json` — STIPA sur PPA (39,6k EUR, 11/19 emplois, consolidation Montreuil)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/53-01.json` — Aissa DEBICHE sur SARL DAVY (215,5k EUR + 45k bail, 1 emploi puis 5, aucune CS)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/54-01.json` — GROUPE MULTI COP / SOLAR ONE sur MAISON SOLAIRE VOLTALIA (60k EUR + 530k BFR + 200k retournement, 14/48 emplois)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/55-01.json` — DREKAN ENERGY sur MYWINDPARTS (150k EUR dont 100k stocks, 8 emplois)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/64-01.json` — BLACK TIGER TECHNOLOGY sur BLACK TIGER FRANCE (500k EUR, 22/37 emplois, auto-cession intra-groupe Bloom)

## Anomalies detectees

1. **41 LA PETITE PARISIENNE = LJ simplifiee, 0 offre** : confirme. Le PDF de 55 pages compile uniquement la requete en releve de forclusion deposee par la bailleresse Mme DE POLHES (creance 50 984,40 EUR, declaration hors delai). Procedure LJ simplifiee ne permet pas de plan de cession — **aucune grille offre creee**, seule la fiche dossier (avec `issue_globale = "liquidation"`).

2. **CSV master-dossiers 54 MAISON SOLAIRE VOLTALIA : champs decales** : `dldo = "Nicolas Jufforgues"`, `effectif_total = "2026-04-08"`. Manifestement les valeurs juge_commissaire / DLDO / effectif_total ont glisse dans les colonnes voisines au scrape. Corrige dans le JSON dossier (juge_commissaire = Nicolas Jufforgues, dldo = 2026-04-08, effectif_total = 48 d'apres l'offre).

3. **54 et 55 partagent meme siege 84 bd Sebastopol Paris** : MAISON SOLAIRE VOLTALIA et MYWINDPARTS sont toutes deux filiales du groupe VOLTALIA, meme AJ (Lou Flechard CBF) et meme MJ (Demortier MJA). Decoupage probable du groupe distressed. **Pattern de batch a documenter** : VOLTALIA = groupe distressed parisien avec au moins 2 entites (MSV photovoltaique + MWP eolien).

4. **Nb_offres_concurrentes discordant** : pour 38 (10 offres master), 54 (48 offres), 55 (8 offres), seul 1 PDF a ete transmis. JSONs offre marquent `nb_offres_concurrentes = nb_offres_master - 1` mais les concurrents ne sont pas identifies. A reconstituer en Phase 2 si les autres PDFs sont fournis.

5. **64 BLACK TIGER FRANCE = auto-cession intra-groupe** : pattern interessant pour Phase 2. La cible (BTF) et la SASU cessionnaire (BTT) ont le meme actionnaire ultime (Bloom BT Holdings Inc., Delaware). Prepack cession art. L.611-7 al.1 + L.642-2 al.2. Pas de faculte de substitution car le projet vise explicitement la reunification. URSSAF (65% du passif public) a refuse abandon le 23/01/2026 — declencheur de la conciliation.

6. **52 PPA : RN STIPA 2024 negatif (-841k EUR)** : repreneur STIPA lui-meme en difficulte recente (EBITDA retraite 2024 -56k EUR), tente consolidation defensive avec PPA. Pattern : reprise par concurrent local en difficulte = signal faible negatif pour la robustesse de la reprise.

7. **38 CHOUETTE : valeur cite "5 704 342 EUR de total actif au bilan 2022"** alors que CA 2024 d'AGREENCULTURE est 3,14 MEUR — risque de confusion bilan groupe vs bilan SAS dans le PDF. A verifier en Phase 2.

8. **53 SARL DAVY : adresse repreneur incomplete** ("184 bis rue Edouard Tremblay" — pas de code postal). Erreur reduite (signature avocat Me FADLI valide l'identite).

9. **54 MAISON SOLAIRE VOLTALIA : seules pages 1-20 sur 38 lues** dans le CSV master — annexes financieres groupe MULTI COP et statuts apport en nature MEDIA SYSTEMS/FUTUR HABITAT partiellement extraits. Confidence "medium" sur cette offre.

## Patterns transversaux observes

- **Auto-cession intra-groupe (BTF/BTT, Bloom)** = pattern emergent pour les distressed tech / SaaS. Permet de purger le passif public (URSSAF) sans dilution du capital industriel.
- **Continuite editoriale / industrielle = signal positif** : Music Box (co-editrice historique de Dixie Frog), STIPA (concurrent local 10 min de PPA), DREKAN ENERGY (verticale eolien). Le tribunal n'a pas encore tranche mais le pattern est coherent avec Sym/LOM et Innatis/Vergers d'Anjou.
- **Reprise par holding industrielle a forte capacite financiere = signal positif** : AGREENCULTURE (leve 6 MEUR), GROUPE MULTI COP (CA 38 MEUR), DREKAN (8 MEUR liquidites). Probable consolidation sectorielle.
- **Prix tres bas + charges augmentatives importantes** = pattern visible sur CHOUETTE (18,5k + 339k charges) et MSV (60k + 530k BFR + 200k retournement). Le prix d'acquisition n'est plus le KPI principal sur les dossiers distressed tech / clean energy.

## Champs ou l'info manquait systematiquement

- `date_audience_cession` : jamais dans les PDFs (fixee post-DLDO)
- `juge_commissaire` : absent dans 6 dossiers sur 8
- `ca_an1_eur` / `ca_an2_eur` / `ca_an3_eur` : seuls CHOUETTE et DIXIE FROG et SARL DAVY (partiel) fournissent un BP 3 ans chiffre
- `cautionnement_personnel` : seul SARL DAVY (PP) le mentionne implicitement
- `nb_offres_concurrentes` : par construction du batch (1 PDF par dossier), pas verifiable depuis les PDFs — info issue du master-dossiers uniquement
- `engagement_maintien_emplois_duree_mois` : seul BTF/BTT le mentionne explicitement (12 mois)

## Suggestions Phase 2

1. **Ajouter champ `auto_cession_intra_groupe`** booleen dans le schema offre — capture le pattern BTF/BTT (cessionnaire = societe soeur).
2. **Ajouter `groupe_cible_lies`** au dossier — MSV 54 et MWP 55 sont liees a VOLTALIA. Detectable par siege identique 84 bd Sebastopol + meme AJ + meme MJ.
3. **Cross-check `RN_repreneur_eur < 0`** + score de robustesse — STIPA reprise PPA pourrait declencher un signal faible negatif.
4. **Conditions suspensives "indivisibilite de l'offre"** (MSV) merite categorie distincte — c'est une CS qui n'est pas suspensive (auto-protection juridique du repreneur).
5. **Pattern `licence_pre_existante` BTF/BTT** (Plateforme Master Data Platform deja sous licence BTT) = a documenter pour les SaaS distressed.

## Recap (<100 mots)

15 JSONs valides ecrits sur batch 02 (8 dossiers + 7 offres). Dossier 41 LA PETITE PARISIENNE = LJ simplifiee sans cession (aucune offre, PDF = requete forclusion bailleresse). Cas notables : auto-cession Bloom intra-groupe sur BLACK TIGER FRANCE (500k EUR), GROUPE MULTI COP sur MSV (60k EUR + 530k BFR, 14/48 emplois), consolidation locale STIPA sur PPA (39,6k EUR, 11/19 emplois). Master-dossiers 54 contient des champs decales (juge_commissaire/DLDO/effectif_total). MSV et MWP appartiennent toutes deux au groupe VOLTALIA (meme siege 84 bd Sebastopol, meme AJ+MJ). Tous les tribunaux en attente de jugement.

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_01]]
