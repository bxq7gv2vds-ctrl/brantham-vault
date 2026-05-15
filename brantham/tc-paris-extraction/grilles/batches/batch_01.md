---
type: batch-log
batch_id: 01
dossiers_traites: 8
offres_extraites: 8
date: 2026-05-15
agent: claude-agent
tags: [tc-paris, batch, extraction]
---

# Batch 01 — Dossiers 01 / 04 / 20 / 21 / 22 / 31-CSA / 32-AJA / 32-SOPI

## Fichiers JSON crees

### Offres (8)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/01-01.json` — Malo BOUCHARDEAU sur FRAN AND JO (Bonjour Bonsoir)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/DT-01.json` — Pauline PECUNE sur DUE TORRI (Capucci)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/20-01.json` — LOM sur SYM TECH
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/21-SYM-OPTIC-01.json` — LOM sur SYM OPTIC France
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/22-SYM-LAB-01.json` — LOM sur SYM LAB GROUP
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/31-CSA-01.json` — OAKLEN CONSULTING (Foalks Group) sur CSA CONSULTING
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/32-AJA-01.json` — HG Holding (LBPP) sur AJA (Akrame)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/offres/32-SOPI-01.json` — EURL P E L sur SOPI (Buvette)

### Dossiers (8)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/01.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/DT.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/20.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/21-SYM-OPTIC.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/22-SYM-LAB.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/31-CSA.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/32-AJA.json`
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/32-SOPI.json`

## Anomalies detectees

1. **SYM x3 : meme offre, 3 dossiers** — l'offre LOM du 27/01/2026 cible explicitement les trois societes du groupe (SYM LAB GROUP + SYM OPTIC + SYM TECH) en bloc. Les 3 PDFs de 369K sont quasi identiques. JSONs distincts crees pour respecter la convention "1 offre par dossier" mais le contenu reste largement dupliquesources.
2. **CSA CONSULTING : PDF unique = offre seule, pas de jugement d'ouverture** — donnees procedure (date RJ, MJ, juge commissaire, tribunal) absentes du PDF. Aussi : les donnees financieres affichees dans la fiche offre sont celles d'Oaklen Consulting (RCS 439455890), pas celles de CSA (la cible).
2bis. **SOPI : meme pattern de "compte d'autrui"** — donnees financieres du repreneur fournies = celles de SAS FRANCOEUR / Les Collonges (holding constituee 11/12/2024 sans comptes approuves). Pattern interessant pour Phase 2 : jeunes holdings ad hoc qui empruntent les comptes d'une societe operationnelle pour justifier leur capacite.
3. **FRAN AND JO : offre tres mince** — sections 3.1 et 3.2 (Previsions activite + financement) explicitement renvoyees a une communication ulterieure. Aucun BP. Profil 28 ans en reconversion sans experience restauration formelle.
4. **DUE TORRI : section "Sort du depot de garantie" vide** (juste un tiret horizontal). Repreneuse mentionne candidature anterieure pour GTME (candidate seriale a la barre).
5. **Encodage SYM PDF abime** : MaÓtre / PÈnÈlope / ´ª — PDF probablement OCR'e ou converti. Bilan date 31/06/2025 = impossible (probablement 30/06/2025).
6. **AJA prix tres bas (20K) sur CA 1M** — valeur economique reelle = 369K avec engagement renovation 300K. Pattern interessant : "prix vitrine bas + enveloppe travaux importante" pour gestion du discours tribunal.

## Champs ou l'info manquait systematiquement

- `date_audience_cession` : jamais dans les PDFs (fixee post-DLDO par le tribunal)
- `juge_commissaire` : absent dans 4 dossiers sur 8
- `cible_siren` : 5 dossiers sur 8 sans SIREN explicite
- `ca_an1_eur` / `ca_an2_eur` / `ca_an3_eur` : seul SOPI et SYM (partiel) fournissent un BP 3 ans
- `cautionnement_personnel` : jamais mentionne
- `ebitda_an3_eur` : presque jamais chiffre
- `nb_offres_concurrentes` : par construction du dataset (1 PDF/dossier dans ce batch), toujours 0 — mais ne reflete pas la realite du tribunal
- `annexes_lettres_soutien_*` : aucune offre n'en a (sur ce batch)

## Issues confirmees (gagnants-tribunal.md)

- **SYM GROUP (dossiers 20, 21, 22) = retenu par le tribunal** : repreneur LOM, gouvernances Sym/LOM independantes. Source Acuite + L'Informe + gagnants-tribunal.md case 8. Marque `cette_offre_retenue: "amelioree_puis_retenue"` + `issue_globale_dossier: "plan_cession_arrete"`.
- 5 autres dossiers : `en_attente` (pas de source publique sur l'issue).

## Suggestions d'amelioration du schema

1. **Ajouter champ `groupe_dossiers_lies`** dans le schema dossier : permet de tagger les dossiers SYM TECH + SYM OPTIC + SYM LAB comme appartenant au meme deal. Idem pour les groupes futurs (Neocamp, Innatis...).
2. **Ajouter `offre_porte_sur_groupe`** booleen dans l'offre : signale qu'une offre cible plusieurs dossiers a la fois (cas LOM).
3. **Ajouter `comptes_repreneur_societe_proxy`** dans `profil_repreneur` : permet de noter quand les comptes fournis ne sont pas ceux de la holding repreneuse (cas Oaklen->Foalks, P E L->Francoeur).
4. **Renforcer `signaux_faibles.erreurs_apparentes`** avec sous-categories typees (encodage / dupplication / dates / nominale / chiffre). Faciliterait le scoring Phase 2.
5. **Ajouter `prix_total_ECONOMIQUE_eur`** dans `structure_prix` distinct du prix de cession (cas AJA : 20K prix + 300K travaux + 39K depot + 10K droits = 369K valeur eco).

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
