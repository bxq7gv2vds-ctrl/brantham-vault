---
batch: 09
date: 2026-05-15
agent: claude-opus-4-7
dossiers_traites: [48-MILORD, 49-SAINT_SULPICE, 14-COLMAR, 26-CHA, 27-OKABE]
nb_offres_extraites: 27
---

# Batch 09 — TC Paris extraction grilles JSON

## Dossiers traités

| # | Folder | Type | PDFs | Grilles offres créées | Confidence |
|---|---|---|---|---|---|
| 48 | SCI MILORD | SCI immo FHBX Balthazar | 5 | 5 (48-MILORD-01 à -05) | medium - PDFs >5MB sauf offres 3 (MUVICO extraite) et 5 (HOUSEBASE hors périmètre) |
| 49 | SCI SAINT SULPICE | SCI immo FHBX Balthazar | 5 | 5 (49-SAINT_SULPICE-01 à -05) | medium - même pattern, baisse 400→300 unique |
| 14 | ASSOCIATION MEDICO DENTAIRE COLMAR 68 | Santé / réseau DENTEKA | 3 | 3 (14-COLMAR-01 à -03) | high - CSV très détaillé |
| 26 | SCI C.H.A | Camping NEOCAMP | 6 | 6 (26-CHA-01 à -06) | high - 6 offres tracées CSV |
| 27 | SCI OKABE | SCI immo FHBX Balthazar | 6 | 6 (27-OKABE-01 à -06) | medium-low - PDFs >5MB, offre 3 PDF cassé |

**Total : 5 dossiers, 25 PDFs → 25 offres JSON + 5 dossiers JSON = 30 fichiers grilles.**

## Méthodologie

1. Lecture `_schema.json` (570 LOC) + `_workflow.md` + `gagnants-tribunal.md` + `decortique-offres-gagnantes.md` (référence rhétorique)
2. Lecture systématique des `dossiers_*.csv` + `offres_*.csv` (50-90% des champs déjà extraits)
3. Extraction PDF :
   - PDF MILORD-03 (MUVICO 2MB) : extraction réussie via `pdftotext -layout` → confirme prix individualisés portefeuille (MILORD 900k / OKABE 600k / SAINT SULPICE 400k initiales)
   - PDFs MILORD-05, SAINT_SULPICE-04, OKABE-02 : tous = HOUSEBASE offre SNC ADONIA 501,6k€ (confirmé via extraction directe, 3 fichiers identiques mal classés physiquement)
   - PDFs >5MB non extractibles via pdftotext (offres scanées probables)
   - PDF OKABE-03 (4MB) : erreur pdftotext "Invalid least number of objects" - PDF corrompu/scan
4. Référence INSULA déjà extraite par batch antérieur pour reconstituer le portefeuille FHBX 26 entités
5. Pour CHA et COLMAR : CSVs ultra-détaillés permettent extraction haute confiance sans relecture PDF

## Patterns observés

### Pattern FHBX 'Affaire Balthazar' (MILORD/SAINT SULPICE/OKABE)
- Portefeuille consolidé 26 SCI/SNC Foncière Melot-Gouband, DLDO 02/03/2026
- 4 offres globales récurrentes : **MUVICO** (initiale + améliorée, 13,9M€ FAI global), **VERDOSO** (offre globale), **LABRAX** (21M€ ferme indivisible), **CORTONA** (27 biens sous CS)
- Plus offres ciblées sur sous-portefeuilles (HOUSEBASE/SNC ADONIA, MIORCEC/AMIRAL+INSULA+RHEA)
- Caractéristiques typiques : asset deal hors passifs, vocation patrimoniale, 3 CS standardisées (audit/visite/transfert libre charges), pas de social
- **Anomalie SAINT SULPICE** : seul cas du portefeuille où MUVICO baisse son prix amélioré (400k → 300k = -25%). Signal négatif : audit terrain a probablement révélé décote (urbanisme/hypothèque/locataire)
- **Cas OKABE** : amélioration +8,3% (600 → 650k) - signal positif
- **Cas MILORD** : amélioration marginale +1,1% (900 → 910k)

### Pattern NEOCAMP/Camping Paradis (CHA)
- 7 procédures simultanées 12/11/2025 (ILO, ALPHA CAMPING, ACO, LA GRANDE LISSE, LORMED, L'ESCAPADE, CHA)
- 6 offres très diverses : opérateurs HPA (HOMAIR/ECG, HPA Mediterraneo, SEASONOVA, CAMPALDIA), investisseur murs-only (KBC), consortium PE+immo (FEMINA STYL+MARENGO partenariat Royon)
- Charges augmentatives chez HOMAIR (1,7M€ prêt+leasing+CP) montrent vrai coût (~2,5M€ total vs 800k€ nominal)
- **Gagnant confirmé** : SEASONOVA (Alpha Camping principal 15 sites) + MAEVA (franchises) selon `gagnants-tribunal.md`
- Indivisibilité offres connexes Lormed+ACO clé pour SCI CHA

### Pattern DENTEKA santé (COLMAR)
- **Monocandidat MEDIVI** - 3 versions successives : [3]€ → 1.300€ → 2.600€ HT
- 11/14 emplois repris (78,57% - non repris : implantologue, orthodontiste, 1 secrétaire)
- Charges augmentatives importantes : 50k€ DENTIGEST + 146,4k€ cession bail Nanterre = vrai coût ~200k€
- Substitution prévue : Association Centre Dentaire Colmar (créée 22/01/2026 W751282634, Président Ishac HADDOUK) + VIVA SANTE
- CS levée à offre définitive (accord principe GALIMMO obtenu) - reste seulement jugement
- Engagements forts : non-cession 2 ans + maintien conditions anciennes
- Agrément ARS 68 non transférable judiciairement - engagement à obtenir au plus tard 01/03/2026

## Anomalies & limitations

1. **PDFs MUVICO/VERDOSO/LABRAX/CORTONA dans dossiers MILORD/SAINT_SULPICE/OKABE** : copies physiques de la même offre globale portefeuille - chaque "offre N" du dossier individuel n'est pas une offre concurrente nouvelle. Si on agrège 5 dossiers × 5 offres = 25 grilles mais ne représentent que ~5 offres globales uniques en réalité.
2. **PDFs HOUSEBASE-SNC ADONIA mal classés** dans 3 dossiers SCI distincts (MILORD-05, SAINT_SULPICE-04, OKABE-02). Documenté dans notes.
3. **PDF OKABE-03 corrompu** : pdftotext échoue avec erreur "Invalid least number of objects".
4. **OKABE-06 PDF >5MB** non extrait : présumé doublon MUVICO améliorée (650k€) selon table de référence INSULA.
5. **Numéro VIVA SANTE incohérent** dans offres MEDIVI : 812 772 382 (offre 03) vs 817 772 382 (offre 02) — typo connue.

## Suggestions Phase 2

- **Déduplication offres globales** : agréger MUVICO/VERDOSO/LABRAX comme **offres uniques portefeuille** plutôt que comme N offres distinctes par dossier (sinon biais statistiques).
- **Cas SAINT SULPICE baisse de prix** : intéressant pour la Phase 2 analyse — détecter pattern "prix amélioré à la baisse" comme signal négatif (rare mais discriminant).
- **Cas DENTEKA mono-candidat** : pattern de monopole sectoriel (réseau) - dans ce cas la trajectoire de prix [3]€→1.300€→2.600€ est piloté par AJ et Tribunal, pas par concurrence. Distinct du multi-offres.
- **Indivisibilité offres** (NEOCAMP, DENTEKA Colmar+Enghien, FHBX portefeuille global) : variable critique à ajouter au schéma (booléen + dossiers liés).

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_01]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_22]]
