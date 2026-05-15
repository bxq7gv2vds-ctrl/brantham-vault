---
type: batch-log
batch: 14
date: 2026-05-15
agent: claude-agent
tags: [tc-paris, extraction, batch-log]
---

# Batch 14 — Extraction grilles JSON 3 gros dossiers (8 PDFs chacun)

## Dossiers traités

| Dossier | Folder | Offres | Strategie lecture |
|---|---|---|---|
| 05 | 05 - SARL à associé unique MY LITTLE FINGER | 8 | CSV complet (verbatim riche) + verif PDFs 05, 07, 08 accessibles |
| PIERRE_VALETTE | 07 - SCI 43-45 RUE PIERRE VALETTE | 8 | CSV + table reference MUVICO (PDFs >5MB non extractibles) |
| ISIS | 10 - SCI ISIS | 8 | CSV + table reference MUVICO (idem) |

**Total : 24 grilles offres + 3 fiches dossiers = 27 JSONs.**

## Constats clés

### Dossier 05 — MY LITTLE FINGER (RJ resto/club 8e arrondissement)
- 8 offres distinctes (vraiment 7 + 1 doublon 05-04 = 05-02 REGOLI Stephane).
- Saut de prix spectaculaire entre offres initiales (1 EUR REGOLI, 10k AURUM 8, 30k LE BRAS, 80k DAUNOU 9 et HENRIQUET) et offres ameliorees (281k FINANCIERE DAUNOU 9 / LE GAGA et 313k RAFA RESTAURATION).
- 2 patterns lutte finale : **groupe nightlife etabli (Guillaume de Bois) vs newco oenologie (Henriquet + 2 experts vin)**.
- Bail contentieux 16 av Friedland = enjeu majeur (procedure resiliation bailleur SCI).
- **AUCUNE source publique** sur le gagnant (RJ ouvert 2025-01-07, audience 2026-01-06).

### Dossier 07 (PIERRE_VALETTE) et 10 (ISIS) — Foncière Melot Gouband
- **2 SCI dans portefeuille consolide FHBX 'Affaire Balthazar' (26 entites)**. Patterns repreneurs identiques :
  - MUVICO (Victor COHEN) : offre globale 26 entites, 3 PDFs doublons sur ISIS, 2 sur PIERRE_VALETTE
  - LABRAX INVEST : offre 21M EUR portefeuille global
  - VERDOSO SAS : plan cession global 26 entites (docusign)
  - HOUSEBASE (Philippe ZERR Rennes) : PDF mal classe (cible SNC ADONIA) + offre dediee
  - AEB INVEST : SAS 75016 - SEULEMENT sur PIERRE_VALETTE (800k EUR dedie) - absent ISIS
- PDFs MUVICO >5MB **non extractibles** par pdftotext (corruption obj table). Donnees prix issues table reference CSV.
- PDF #2 = UNKNOWN dans les deux dossiers (offre non identifiee).
- Confidence forcement `medium`/`low` sur ces 2 SCI.

## Anomalies / limites

1. **PDFs MY LITTLE FINGER offre 06 LE BRAS** : pdftotext bloque (Syntax Warning: Invalid least number of objects). CSV notes tres detaillees compensent.
2. **3 doublons MUVICO sur ISIS** (vs 2 sur PIERRE_VALETTE) : pattern repetitif portefeuille global. Confidence `low` forcee.
3. **AEB INVEST absent sur ISIS** : alors que present sur PIERRE_VALETTE - donc AEB cible specifiquement le 43-45 rue PIERRE VALETTE.
4. **Aucune source publique** sur les 3 dossiers (verifie via gagnants-tribunal.md - ni Melot Gouband ni MY LITTLE FINGER tracés).

## Patterns transversaux observés

- **Resto Paris RJ** : offres initiales planchers (1 EUR a 80k) puis ameliorees a x3-x4 du plancher. Groupe etabli (Guillaume de Bois, 4 etablissements) bat newco prestige (Vachier-Lagrave/Henriquet).
- **Foncière distressed multi-SCI** : plateforme MUVICO/VERDOSO/LABRAX/HOUSEBASE en course pour portefeuille consolide. Offres "globales" = standard, offre "dediee" (AEB) = exception.
- **Patterns rejet predit** :
  - Offres a 1 EUR + 0 emploi (REGOLI 05-02, 05-04) = quasi certain rejet (cf. Minelli).
  - Offres globales VERDOSO sans ventilation par actif = risque rejet pour incompletude.

## Suggestions Phase 2

1. **Re-extraire les PDFs MUVICO** (>5MB) avec un outil OCR forcé (qpdf decrypt + tesseract) pour valider les structures de prix individualisees.
2. **Suivre BODACC** sur Melot Gouband / Balthazar pour le jugement consolide (probable mai-juin 2026, post-DLDO 02/03).
3. **Tracer MY LITTLE FINGER** post-jugement : LinkedIn Guillaume de Bois (FINANCIERE DAUNOU 9) + Antoine Henriquet (RAFA RESTAURATION) - le perdant lance peut-etre autre chose.
4. **AA Investments (HK) Ltd** confirmé recurrent (pattern fichier `gagnants-tribunal.md`) : non present sur ces 3 dossiers (logique - retail mode, pas resto ni immo).

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/groupes-distressed]]
- [[brantham/tc-paris-extraction/grilles/dossiers/05]]
- [[brantham/tc-paris-extraction/grilles/dossiers/PIERRE_VALETTE]]
- [[brantham/tc-paris-extraction/grilles/dossiers/ISIS]]
