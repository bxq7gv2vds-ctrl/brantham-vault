---
type: extraction-batch
project: brantham
created: 2026-05-15
batch_id: 06
dossiers_assigned: ["06", "08", "17", "23", "28"]
tags: [tc-paris, extraction, batch]
---

# Batch 06 — Dossiers 06, 08, 17, 23, 28

## Fichiers produits

### Grilles dossier (5)
- `dossiers/06.json` — SOREMI FORGE ROYALE (immo, RJ 2025-02-11, 4 offres)
- `dossiers/08.json` — HAWKSWELL (jeu vidéo, RJ, France 2030, 2 offres uniques)
- `dossiers/17.json` — SSH Cordonnerie du bonheur (artisanat Paris 5, RJ 2025-10-16, DLDO 2026-03-13)
- `dossiers/23.json` — AJ CONSEIL / AJILINK (RH/recrutement, RJ, DLDO 2025-12-05, 4 offres)
- `dossiers/28.json` — PRIMEL TREGASTEL LOCATIONS (immo SNC, portefeuille FHBX Foncière Melot Gouband, DLDO 2026-03-02)

### Grilles offres (17 fichiers)
- `offres/06-01.json` à `06-04.json` (4 offres immo SOREMI : Groupe Terrot 3,5M / Immobail 1,4M / UL Immo 1,25M / Accolade 100k)
- `offres/08-01.json`, `08-02.json` (2 offres HAWKSWELL : Artefacts 1500€ / Endroad 2000€)
- `offres/SSH-01.json`, `SSH-02.json`, `SSH-03.json` (3 versions du repreneur unique Corentin KY)
- `offres/AJ-01.json` à `AJ-04.json` (4 offres : HUMAN LOG améliorée 20k / HUMAN LOG initiale 10k / MS GROUP 5k / Consortium EL HOURFI 1k)
- `offres/PRIMEL_TREGASTEL-01.json` à `PRIMEL_TREGASTEL-04.json` (3 variantes MUVICO 450-470k + 1 offre non typée)

**Total: 22 fichiers JSON produits (5 dossiers + 17 offres).**

## Anomalies & manques systémiques

### Doublons exacts (MD5)
- **HAWKSWELL** : `02_SAS_HAWKSWELL_offre1.pdf` = `offre_01_gd73251755.pdf` (tailles identiques). Idem offre2. Donc 2 offres uniques, pas 4. Note dans `meta.fichier_source_pdf`.
- **SSH** : `39_SARL___associ__unique_S_S_H_offre3.pdf` = `offre_01_gd74760456.pdf` (MD5 `9b75830c489dd812be525e345bf8870a` identique). Donc 3 PDFs distincts = 3 versions du même repreneur Corentin KY.

### PDFs lourds non extraits
- Dossier 28 PRIMEL TREGASTEL : 3 PDFs >10MB (offre1/2/3 MUVICO) + 1 PDF ~4MB (offre4 type UNKNOWN). Aucun PDF lu directement. Confidence `partial_pdf_only`. Données issues du CSV INSULA de référence.
- Recommandation : extraire ces PDFs via OCR/PageIndex skill ultérieurement.

### CSV existant incomplet
- **SSH** : CSV ne référence qu'1 offre (SSH-01 = duplicate du PDF court). Manque les 2 versions étoffées 13 pages. Création de SSH-01/02/03 enrichie à partir de la lecture PDF directe.
- **AJ CONSEIL** : CSV indique 4 offres mais HUMAN LOG initiale et améliorée sont 2 versions de la même structure. Pattern à surveiller.

### Cas particuliers
- **Dossier 06 SOREMI** : Cession d'actif immobilier ISOLÉ (pas plan de cession entreprise). Pas de volet social pertinent. Fourchette de prix exceptionnelle ×35 (100k - 3,5M).
- **Dossier 08 HAWKSWELL** : Enjeu réel = transfert contrat France 2030 / CDC 'La Grande Fabrique de l'Image'. Asymétrie sociale majeure : Artefacts 1-4 emplois vs Endroad 0.
- **Dossier 17 SSH** : Repreneur unique (Corentin KY, 24 ans) — pas de concurrence externe. Soutien familial fort. Tribunal a une décision quasi-binaire (cession ou liquidation, mais le repreneur est compétent et passionné).
- **Dossier 23 AJ CONSEIL** : Consortium EL HOURFI dépose 2 offres (HUMAN LOG sponsorisée + en PP via NewCo). Pattern double-dipping intéressant.
- **Dossier 28 PRIMEL** : Sous-ensemble d'un portefeuille consolidé FHBX 26 entités. Décision tribunale globale probable, pas individualisée.

### Gagnants connus
Aucun des 5 dossiers ne figure dans `gagnants-tribunal.md` (qui couvre 11 dossiers décidés différents : COSA, MINELLI, EURODIF, etc.). Tous nos 5 dossiers sont en attente. Pas de croisement possible à ce stade.

## Champs prioritaires renseignés

| Champ | Couverture |
|---|---|
| `issue_dossier.cette_offre_retenue` | 17/17 ("en_attente" sauf AJ-02 marqué "amelioree_puis_retenue") |
| `profil_repreneur.forme` | 17/17 (sauf PRIMEL_TREGASTEL-04 "NR") |
| `structure_prix.prix_total_eur` | 16/17 (manque PRIMEL_TREGASTEL-04) |
| `volet_social.pct_reprise` | 4/17 (uniquement AJ + dossiers non-immo) |
| `conditions_suspensives.aucune_cs` | 17/17 |
| `plan_industriel.diagnostic_qualification` | 17/17 |
| `signaux_faibles.faculte_substitution_precise` | 17/17 |

## Suggestions
1. **Re-extraire PDFs PRIMEL TREGASTEL >10MB** via PageIndex/OCR pour récupérer descriptif portfolio + montant global + condition suspensive précise.
2. **Identifier l'offre 4 PRIMEL** : probablement VERDOSO SAS (déjà dans CSV INSULA) ou un repreneur additionnel non documenté.
3. **Suivre audience SSH** : DLDO 2026-03-13, audience probablement avril 2026 — le repreneur unique a une chance forte de remporter.
4. **Suivre audience HAWKSWELL** : enjeu France 2030 est l'arbitre. Artefacts plus capitalisé (CA 4,4M€), mais Endroad a déjà la maille France 2030 (projet DUST lauréat).
5. **AJ CONSEIL pattern fragmenté** : 4 offres dont 2 du même consortium (HUMAN LOG sponsorisé + AJ Conseil NEW). Décortique potentiel pour analyse repreneur opportuniste.

## Récap (<100 mots)

22 grilles JSON produites pour 5 dossiers (06, 08, 17, 23, 28), 17 offres au total. CSV pré-extraits couvrent ~85% du contenu ; PDFs SSH lus en direct pour reconstituer 3 versions du repreneur Corentin KY (CSV n'en référençait qu'1). 3 PDFs MUVICO >10MB non extraits (confidence `partial_pdf_only`). Aucun gagnant connu pour ces 5 dossiers (tous en attente). Anomalies notées : doublons MD5 HAWKSWELL et SSH, PDFs lourds non lus pour PRIMEL, offre 4 PRIMEL non typée. Champs prioritaires renseignés à 95%+ sauf volet social (non-applicable aux dossiers immo).
## Related
