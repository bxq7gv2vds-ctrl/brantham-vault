---
type: batch_log
project: brantham
batch: 22
created: 2026-05-15
tags: [tc-paris, extraction, batch]
---

# Batch 22 — EURODIF (50) + AMIRAL MAIGRET (09) + ADELE ET FIRMIN (30)

## Dossiers traites

| Dossier | Folder | Nb offres extraites | Confidence |
|---|---|---|---|
| 50 | SAS associé unique EURODIF | 15 | high (50-03 gagnante, 50-13 AMONISS, 50-14 AA initiale) / medium (TDU, CASA IDEAS, JOVELET) / low (offres partielles) |
| 09 | SNC AMIRAL MAIGRET | 16 | medium (LABRAX, MIORCEC, AEB) / low (MUVICO non extraits >5MB, JADO, VERDOSO, UNKNOWN) |
| 30 | SCI ADELE ET FIRMIN | 18 | medium (LABRAX, AEB) / low (MUVICO >5MB, ameliorations a identifier, UNKNOWN) |

**Total : 49 offres + 3 fiches dossier = 52 JSONs ecrits.**

## Cle EURODIF (gagnant confirme)

AA INVESTMENTS HK (offre 50-03 amelioree) emporte le plan de cession :
- 25 baux / 185 emplois CDI (perimetre MAX vs concurrents)
- Prix 50k incorporels + 5k corporels + 300k stocks + 350k max stock Havre = 700k max
- **Mecanisme stock Havre co-construit** (350k repreneur + 1,4M procedure si accord 48 fournisseurs sous 60j) — innovation rhetorique qui a probablement fait basculer
- Track record visible : Smallable / Wethenew / L'Exception / Bazar Chic / Atlas For Men (5 reprises distressed en 18 mois sur Paris)
- 11 pages, ton juridique propre, aucune CS

Champ `cette_offre_retenue` = `amelioree_puis_retenue` pour 50-03 (et 50-14 initiale).

## Anomalies detectees

1. **EURODIF 50-09 / 50-10** : doublon EXACT (meme Docusign Envelope ID 55BB1506) - traite chacun mais flag dans signaux_faibles
2. **EURODIF 50-05 OTERA** : mentionne 'liquidation judiciaire' alors qu'on est en RJ
3. **09 AMIRAL_MAIGRET-01** + **30 ADELE_FIRMIN-15** : PDFs HOUSEBASE mal classes - ciblent SNC ADONIA, pas l'entite indiquee
4. **3 PDFs MUVICO par dossier 09 et 3 par dossier 30** : redondance — meme offre globale multi-SCI declinee en plusieurs fichiers (>5MB chacun, non extraits, valeurs issues de la table de reference INSULA)
5. **5 candidats UNKNOWN/ameliorations a identifier** sur ADELE_FIRMIN et 2 sur AMIRAL MAIGRET — PDFs originaux a re-traiter pour identifier auteur

## Suggestions Phase 2

- **EURODIF est un cas d'ecole** : le tribunal preferre le perimetre social (emplois + magasins repris) au prix de cession. A coder explicitement dans la grille de scoring : weighting `nb_salaries_repris` > `prix_total_eur` sur les dossiers retail multi-sites en RJ.
- **Co-construction tresorerie procedure** : mecanisme AA Investments stock Havre = pattern reutilisable. A documenter dans `vault/brantham/patterns/cession-mecanisme-stock-fournisseurs.md`.
- **Dossiers FHBX (09, 30, et 03 INSULA + autres SCI Melot-Gouband)** : le pricing par actif individualise est extrait des tables MUVICO/VERDOSO mais les PDFs >5MB n'ont pas ete lus. Pour la Phase 2, considerer ces 24+ entites comme un meta-dossier consolide et analyser globalement (qui prend quoi dans le portefeuille de 21M EUR LABRAX vs offre MUVICO multi-SCI).
- **Recouper LABRAX INVEST 21M EUR** : meme offre apparait sur AMIRAL_MAIGRET et ADELE_FIRMIN. La position de l'offre par rapport aux 24 autres SCI/SNC doit etre tracee pour evaluer le serieux (offre globale indivisible vs cession asset par asset).

## Recap (<100 mots)

49 offres + 3 fiches dossier extraites pour batch 22 : EURODIF (15 offres, gagnant AA Investments HK confirme, mecanisme stock Havre decisif), AMIRAL MAIGRET (16 offres FHBX dont 3 MUVICO redondants, MIORCEC offre concentree 673k aucune CS), ADELE ET FIRMIN (18 offres FHBX dont 5 UNKNOWN, AEB INVEST 1,5M sur asset specifique). Anomalies : 2 PDFs HOUSEBASE mal classes (cible ADONIA), 1 doublon TDU exact (50-09=50-10), 6 PDFs MUVICO >5MB non extraits. Tous JSON valides selon schema. Total batch : 52 fichiers.

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
