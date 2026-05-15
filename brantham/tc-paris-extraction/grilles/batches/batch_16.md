---
type: batch-log
batch_id: 16
date: 2026-05-15
agent: claude-opus-4.7
dossiers: [06-ATELIERS_VG, 10-CHINON, 18-JEAN_RENAUDIE]
nb_offres: 27
---

# Batch 16 — Trois gros dossiers TC Paris

## Dossiers traités

### Dossier 06 — SCI LES ATELIERS VILLEJUIF GENTILLY (9 offres immo)
- Portefeuille consolidé FHBX "Foncière Melot-Gouband / Affaire Balthazar" (26 entités SCI/SNC + 44 entités total en RJ vagues avril-décembre 2025).
- AJ : Maître Hélène BOURBOULOUX (SELARL FHBX) + RAYBAUD + CHARREY. MJ : SELAFA MJA (LELOUP-THOMAS). JC : J.-F. PONCET. DLDO 02/03/2026 (DDO offres améliorées).
- Bien rattaché : 2 ateliers-lofts 120 m² Villejuif (confirmé via PDF HOUSEBASE offre 9).
- 5 candidats distincts : MUVICO (Victor COHEN, 250-255K€ portion), VERDOSO SAS (groupe Luxembourg, 250 002€ provisoire global), LABRAX INVEST (Edouard LAMY, 21M€ portefeuille global 26 entités + appartement Paris 16e), GROUPE ARCANGE (Michael SFEDJ, 8,713M€ asset deal partiel détention 5 ans bon père de famille), HOUSEBASE (Philippe ZERR, 10K€ offre conservatoire dédiée).
- **Anomalie CSV** : offre 4 listée comme "hors périmètre cible SNC ADONIA" — PDF mal classé physiquement.
- **Anomalie CSV** : offre 1 = type UNKNOWN, non identifiée.
- Issue : EN ATTENTE (audience cession non datée publiquement).

### Dossier 10 — SARL LE CHINON (9 offres distinctes — restauration Montmartre)
- Brasserie 49 rue des Abbesses 75018 Paris (SIREN 420429029). CA 2024 ~1,2M€, perte 65K€, CP négatifs, 8 salariés. Bail sous-location Société Hôtelière de la Rue Audran (~46K€/an). Licence IV n°764-2004.
- AJ : Me Nicolas LOYER (SELARL AJ MEYNET & ASSOCIÉS). MJ : Me Sabine ROCHER (Astéren). JC : Olivier Duboureau. DLDO 03/02/2026 12h. Audience plan ≤ 30/03/2026.
- 9 candidats : HIPPO SF / Pierre Jean Pouletty (501K — dépôt 16/02 hors délai), DI CRESCENZO (100K, PP Café Gabrielle 17e, reprise 4/8), ANGELVY/BRIOUDE / BRIANGE GRANDE ARMÉE (200K, 4 étabs Paris, 8/8 — aucune CS), HAOUANOH (350K, Le Voltigeur 32 ans, 8/8 — aucune CS), JEMA / famille ALBARET (500,5K, 5/8), FINANCIÈRE DAUNOU 9 / FOUGEDOIRE (400K, 4 étabs Paris depuis 1990, 8/8 — aucune CS), XB HOLDING / BOUDOUMA (500K, groupe XB 4 brasseries dont XB Montmartre adjacent rue Tardieu, 8/8, 1 CS), PAMAJU / WILHELM (550K, Le Nazir + Le Saint-Jean même rue, 8/8, 6 CS lourdes), 4-M / CKM.18 / MONCAN+MAGNE (753K — plus haute offre, groupe Café Benjamin 1933 + La Succursale, 8/8, 5 CS, BP 3 ans complet).
- Pattern fort : grille de scoring offre Chinon = vrai cas d'école — 5 candidats restaurateurs historiques Paris 18e/Montmartre + 1 holding financière. Plus-haute-offre (4-M 753K€) cumule prix + reprise 8/8 + BP 3 ans + voisinage Montmartre + cohérence sectorielle.
- Issue : EN ATTENTE (audience ≤ 30/03/2026).

### Dossier 18 — SCI JEAN RENAUDIE (9 offres immo)
- Même portefeuille FHBX que dossier 06. Bien rattaché : 2 Ateliers Lofts 473 m² Ivry-sur-Seine (confirmé HOUSEBASE).
- MUVICO 160K€ initiale → 170K€ amélioré (portion). VERDOSO + LABRAX 21M€ portefeuille global + HOUSEBASE 10K€ dédiée.
- Issue : EN ATTENTE.

## Champs prioritaires renseignés

15/15 champs prioritaires extraits où la donnée existe. Confidence par dossier :
- LE CHINON : `high` sur 9/9 offres (CSV source extrêmement riche, PDFs exploitables)
- ATELIERS_VG : `medium` (VERDOSO, ARCANGE) à `high` (LABRAX, HOUSEBASE) ; `partial_pdf_only` pour MUVICO (PDFs >5MB non extraits) ; `low` pour offre 1 UNKNOWN et offre 4 mal classée.
- JEAN_RENAUDIE : `high` (LABRAX, HOUSEBASE) ; `medium` (VERDOSO) ; `partial_pdf_only` (MUVICO) ; `low` (offre 1 UNKNOWN, offre 7 doublon Docusign).

## Anomalies & suggestions

1. **PDFs MUVICO non extraits** (>5MB chacun) — les prix par entité viennent de la table de référence CSV (initiale 09/02/2026 + améliorée 02/03/2026). À retraiter avec OCR/Lit unifié si besoin de plus de granularité.
2. **PDF mal classé** : `06_..._offre4.pdf` cible la SNC ADONIA (501 600€, immeuble Cachan) et non la SCI Villejuif — doublon physique.
3. **Offres UNKNOWN** (06-01, 18-01) : type non reconnu dans CSV source, PDFs probablement déjà classés ailleurs ou rapports d'extraction.
4. **VERDOSO offre 7 dossier 18** : doublon Docusign EBE6E276 (vs CC859BA0 offre 5) — vraisemblablement offre initiale 09/02 vs améliorée 02/03 dans le même bundle PDF.
5. **LE CHINON HIPPO SF dépôt hors délai** : 16/02/2026 vs DLDO 03/02/2026 — risque irrecevabilité tribunal.
6. **LABRAX INVEST 21M€** : seule vraie offre globale ferme et indivisible **sans CS** — pattern fort pour Phase 2 (aucune_cs = True). Capital SAS 10K€ mais qualité de signature associés + visite réelle 30/10/2025 + 3 offres successives historiques.
7. **GROUPE ARCANGE 8,7M€ asset deal** : alternative à plan de cession — pattern intéressant pour Phase 2 ("asset deal vs plan de cession").
8. **Pattern LE CHINON** : 9 offres rapprochées entre 100K-753K€ illustre parfaitement la concurrence en restauration distressed Paris 18e. Plus-haute-offre 4-M = sérieux candidat à retenir comme proxy "gagnant probable".

## Fichiers produits

```
grilles/offres/06-ATELIERS_VG-01.json à 06-ATELIERS_VG-09.json
grilles/offres/10-CHINON-01.json à 10-CHINON-09.json
grilles/offres/18-JEAN_RENAUDIE-01.json à 18-JEAN_RENAUDIE-09.json
```

27 JSONs validés (json.load OK). Conformes au schéma `_schema.json`.

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
