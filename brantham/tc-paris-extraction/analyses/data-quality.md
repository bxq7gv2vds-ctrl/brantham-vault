---
type: analysis
project: brantham
created: 2026-05-15
tags: [tc-paris, data-quality, ocr, doublons]
---

# Data quality — TC Paris dataset

Audit qualité des données extraites. À traiter avant analyses fines.

## 1. PDFs scannés / OCR à refaire

Dossiers où au moins un PDF n'a pas pu être extrait nativement (scan illisible, OCR à effectuer) :

- `09 - EZIN & STRAUUS` — `offre_07` FIDUCIAIRE VALUE image-only
- `12 - ALDADDY` — PDF principal scanné corrompu, lu via JPGs associés
- `41 - LA PETITE PARISIENNE` — PDF requête forclusion, aucune offre dedans
- `45 - COLLEGE DE PARIS` — offre `45-17` (58 pages) non lue intégralement, placeholder créé
- `51 - BOULANGERIE BO` — 3 PDFs sur 4 sont des scans (tesseract absent, lecture visuelle)
- `63 - AUBERGES JEUNES` — offre `63-12` (245 KB) non lue

**Action** : relancer ces dossiers avec OCR tesseract / pdfplumber + Vision API si besoin.

## 2. Doublons techniques (même PDF déposé plusieurs fois)

Pattern récurrent au greffe : même offre déposée sous plusieurs noms de fichiers, ou offres rééditées avec Docusign Envelope ID identique. Détectés sur :

- `03 - SCI INSULA` — mismatch PDFs (offre HOUSEBASE retrouvée aussi dans SEGI)
- `04 - SCI DANTON-LILAS` — PDF DANTON-01 cible en fait SNC ADONIA (PDF mal classé)
- `08 - HAWKSWELL` — 4 PDFs = 2 offres réelles (doublons MD5)
- `11 - CLAYE` — 2 PDFs = 1 offre (doublons MD5)
- `14 - COLMAR DENTAIRE` — 6 PDFs = 3 offres uniques
- `15 - ENGHIEN` — 8 PDFs = 4 offres uniques après dédoublonnage
- `18 - 3S OPTIC` — 2 PDFs = 1 offre
- `21 - SYM OPTIC` / `22 - SYM LAB` / `20 - SYM TECH` — offres identiques (offre globale unique LOM)
- `24 - LA BELLE FORÊT` — 8 PDFs = 4 offres uniques
- `27 - LA GRANDE LISSE` — 4 doublons techniques
- `34 - LPC` — offre3 = offre4 (même Docusign envelope)
- `35 - DME` — 6 PDFs = 3 offres uniques
- `35 - SICA` — offre3=offre6, offre2=offre4 (2 paires doublons)
- `36 - LVL POMANJOU` — offres 2/4 doublons exacts (ADVANTAGE Malte)
- `37 - VOLTAIRE` — offre 04 et 05 doublons stricts d'offre 03 (Amsterdam Air)
- `37 - COOP` — offres 1-4 = 4 exemplaires Docusign de la même offre améliorée
- `45 - COLLEGE DE PARIS` — 4 paires de doublons détectées (45-02≡19, 45-03≡16, 45-04≡05, 45-06≡07)
- `50 - EURODIF` — offre10 = offre9 (TDU GROUP doublon)
- `57 - PLESSE` — offre4 = offre5 doublons d'offre3 (CELHER)
- `60 - DENIOLAY` — 2 paires doublons (60-01≡02, 60-04≡05)
- `62 - CHAUSSEE` — 3 doublons consortium INNATIS + 2 doublons CELHER
- `66 - VAULEARD` — — vérifié, pas de doublon explicite

**Action** : pour analyses agrégées, dédoublonner par `Docusign Envelope ID` ou hash MD5. Champ `notes` mentionne le doublon.

## 3. Variantes orthographiques repreneurs

Noms de repreneurs avec variations à consolider :

- "CASTEL INVEST + LEROY FRERES ET SOEUR + VCAPITAL" / "CONSORTIUM CASTEL INVEST..." / "Consortium LEROY FRERES ET SŒUR / VCAPITAL / CASTEL INVEST" → **19 offres au total**, même groupement
- "HOUSEBASE" / "HOUSEBASE — HORS PÉRIMÈTRE" → 36 occurrences (les "HORS PÉRIMÈTRE" sont des PDFs mal classés)
- "SARL CELHER" / "SARL CELHER (BOUJUAU)" / "SARL CELHER (sub. CELHER)" → même entité
- "FEMINA STYL" / "FEMINA STYL + MARENGO" / "FEMINA STYL conjointement avec MARENGO" → même

**Action** : ajouter colonne `nom_repreneur_normalise` au master CSV pour analyses.

## 4. Anomalies signalées dans `notes`

- `35 - DME` offre QASTI : auto-contradictoire ("aucune condition suspensive" alors que 4 listées)
- `36 - DN ASSOCIES` offre Yource : "soixante mille euros" en lettres pour 75 000 € chiffres
- `61 - BEAUVALLO` : RCS discordant (786 216 702 vs 786 213 702) — retenu 786213702
- `11 - CLAYE` offre MEDIVI : prix laissé en placeholders `[3]€` (techniquement non chiffré)
- `03 - SEGI` offre SIMA : inclut lots 1 et 2 alors qu'ils ont déjà été vendus à Albin Michel en 2023

## 5. Champs souvent manquants

D'après le scan rapide :

| Champ | Taux remplissage estimé |
|---|---|
| `nom_repreneur` | ~95% |
| `prix_total_eur` | ~85% |
| `emplois_repris` | ~70% |
| `date_offre` | ~85% |
| `rcs_repreneur` | ~60% |
| `ca_repreneur_eur` | ~30% |
| `dldo` | ~70% |
| `juge_commissaire` | ~50% |

**Action** : enrichir via Pappers API (RCS → CA/résultat) en post-traitement.

## 6. Dossiers sans offre réelle

- `41 - LA PETITE PARISIENNE` : LJ simplifiée, requête forclusion bailleur (pas d'AAP)
- `31 - CSA CONSULTING` : pas de jugement d'ouverture dans le PDF, pas de DLDO/MJ/JC

## Pistes amélioration

1. **OCR systématique** des scans (tesseract + Vision API)
2. **Dédoublonnage** par hash MD5 + Docusign Envelope ID
3. **Normalisation noms** repreneurs (entity resolution)
4. **Enrichissement Pappers** RCS → données financières repreneurs
5. **Re-lecture des dossiers** où le rapport agent indique des informations partielles
6. **Validation manuelle** des prix > 1 M€ et < 100 € (outliers à confirmer)

## Related

- [[../_MOC|TC Paris MOC]]
- [[repreneurs-recurrents]]
- [[groupes-distressed]]
