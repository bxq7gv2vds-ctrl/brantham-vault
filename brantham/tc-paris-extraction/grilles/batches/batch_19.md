---
type: batch_log
project: brantham
batch: 19
created: 2026-05-15
tags: [tc-paris, extraction, batch, fhbx, balthazar]
---

# Batch 19 — INSULA (03) + MAUDAPHNE (12) + ATELIER URBAIN (23)

## Dossiers traites

| Dossier | Folder | Nb offres extraites | Confidence |
|---|---|---|---|
| 03-INSULA | SCI INSULA | 12 | high (INSULA-09 MIORCEC, 10 MIORCEC complement, 11 AEB, 12 HOUSEBASE - 4 PDFs lus) / medium (INSULA-08 LABRAX) / low (MUVICO/VERDOSO PDFs >5MB, CORTONA cut-off, scanne) |
| 12-MAUDAPHNE | SCI MAUDAPHNE | 11 | medium (MAUDAPHNE-11 LABRAX) / low (MUVICO/VERDOSO >5MB, JADO 23 pages non extraites, UNKNOWN/amelioree non identifiees, HOUSEBASE mal classe) |
| 23-ATELIER_URBAIN | SCI ATELIER URBAIN | 11 | medium (ATELIER_URBAIN-03 AEB INVEST 1M dedie) / low (MUVICO/VERDOSO >5MB, UNKNOWN, HOUSEBASE mal classe) |

**Total : 34 offres + 3 fiches dossier = 37 JSONs ecrits.**

## Lecture selective effectuee

3 PDFs INSULA lus integralement (pdfplumber + uv) :
- **INSULA-09 MIORCEC** (3,3MB, 2p) : email FHBX 27/02 + complement 02/03. Offre PP recentree fonds propres 673k total (AMIRAL 561k + INSULA 101k + RHEA 11k). Aucune CS. Verbatim extrait : "Dans un souci de parfaite securisation de l'operation, je souhaite donc recentrer mon positionnement sur un perimetre que je suis en mesure de financer integralement sur mes fonds propres".
- **INSULA-11 AEB INVEST** (124k, 4p) : proposition INDICATIVE 30k pour 12 parkings sur 3 adresses (Chevilly-Larue/Augustin Dumont/Arcueil). 7 hypotheses valorisation listees, 3 CS, faculte substitution filiale. Rattachement INSULA douteux (adresses ne matchent pas description INSULA).
- **INSULA-12 HOUSEBASE** (166k) : offre dediee SCI INSULA 10k EUR ('montant conservatoire'). Comptant fonds propres + comptes courants. Sans CS bancaire MAIS 3 CS (visite, audit tech, audit juridique). Faculte substitution.

## Cle - asymetrie de pricing flagrante

12 parkings SCI INSULA proposes a :
- **HOUSEBASE 10k** (dedie, conservatoire) - 1x base
- **MUVICO 40k initiale / 45k amelioree** (globale 26 entites)
- **AEB INVEST 30k** (indicatif, rattachement douteux)
- **MIORCEC 101k** (PP fonds propres aucune CS) - 10x HOUSEBASE

LABRAX 21M EUR portefeuille global indivisible englobe tous (prix individualise NR).

Note : MIORCEC offre PP fonds propres aucune CS = signal credibilite max sur petit deal immo dedie. A confronter au pattern AGENCE IF / continuite. Cf [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]].

## Pattern revalorisation MUVICO initiale -> amelioree

Variations par SCI dans cette amelioree MUVICO :
- **INSULA** : 40k -> 45k (+12,5%)
- **ATELIER URBAIN** : 850k -> 880k (+3,5%)
- **MAUDAPHNE** : 250k -> 250k (STABLE, anomalie)

MAUDAPHNE non revalorise dans l'amelioree alors que les autres SCI le sont = signal soit (a) actif moins attractif soit (b) MUVICO confiant prix MUVICO suffisant. A re-extraire pour confirmer.

## Anomalies detectees

1. **3 PDFs HOUSEBASE mal classes** : 03_offre1, 12_offre4, 23_offre2 ciblent SNC ADONIA (immeuble Cachan 501,600 EUR), pas INSULA/MAUDAPHNE/ATELIER URBAIN
2. **6 PDFs MUVICO redondants** (2 par dossier en moyenne sur 3) : 7-10MB chacun, non extraits, table reference utilisee
3. **6 PDFs VERDOSO** (2 par dossier - Docusigns CC859BA0 + EBE6E276 differents) : doublons ou 2 candidats distincts non identifies
4. **2 PDFs Groupe JADO** sur MAUDAPHNE (23 pages chacun) non extraits - prix individualises manquants
5. **1 PDF scanne illisible** : INSULA-02 (4,1MB) OCR a faire
6. **AEB INVEST** present 2 fois (INSULA-11 30k 12 parkings adresses douteuses / ATELIER_URBAIN-03 1M dedie) - signal AEB cible asset par asset
7. **4 candidats UNKNOWN/ameliorees non identifies** : MAUDAPHNE-01, MAUDAPHNE-03 (DDO 02/03), ATELIER_URBAIN-02 (DDO), ATELIER_URBAIN-05, ATELIER_URBAIN-11 (offre9)
8. **Encodage caracteres** : INSULA-11 PDF AEB INVEST a apostrophes mal restituees ('9' au lieu de ', '昀栀bx.eu' au lieu de fhbx.eu) - PDF post-OCR ou autre encodage

## Suggestions Phase 2

- **MIORCEC = cas d'ecole offre PP fonds propres aucune CS** : a coder explicitement comme reference (small ticket immo direct sans intermediaire). Phrase verbatim a stocker : "Dans un souci de parfaite securisation de l'operation, je souhaite donc recentrer mon positionnement sur un perimetre que je suis en mesure de financer integralement sur mes fonds propres".
- **AEB INVEST pattern asset-by-asset** : 2 propositions distinctes (INSULA 30k + ATELIER URBAIN 1M) - cibler les SCI individuelles avec proposition indicative. A documenter comme pattern alternatif a l'offre globale portefeuille.
- **Pattern HOUSEBASE 'conservatoire'** : INSULA-12 'montant conservatoire tient compte des informations parcellaires dont nous disposons' = signal classique de sous-evaluation volontaire pour ouvrir negociation. Different de MIORCEC offre PP fonds propres directe.
- **VERDOSO Docusigns differents** : verifier si 2 candidats distincts ou simple re-depot - implique sur le comptage des concurrents reels.
- **Recouper LABRAX 21M EUR vs somme MUVICO individualisee** : MUVICO amelioree (sur les SCI tracees) genere une somme partielle qui, extrapolee, est probablement < 21M LABRAX. Confronter pour evaluer credibilite des deux offres.
- **Re-traiter PDFs MUVICO >5MB** : table reference utilisee mais corps PDF avec mecanismes (paiement, garanties, CS, ton, annexes) non lu - critique pour scoring Phase 2.

## Recap (<100 mots)

34 offres + 3 fiches dossier extraites pour batch 19 : dossiers FHBX consolides 'Affaire Balthazar' (SCI INSULA 12, MAUDAPHNE 11, ATELIER URBAIN 11). Lecture selective 3 PDFs INSULA representatifs : MIORCEC PP fonds propres 101k aucune CS (signal credibilite max), HOUSEBASE 10k conservatoire avec 3 CS, AEB INVEST 30k indicatif adresses douteuses. Asymetrie pricing flagrante INSULA (10k-101k pour memes 12 parkings). Anomalies : 3 PDFs HOUSEBASE mal classes (cible ADONIA), 6 PDFs MUVICO/6 VERDOSO redondants >5MB non extraits, 4 candidats UNKNOWN/ameliorees non identifies. Tous JSON valides selon schema.

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_22]]
