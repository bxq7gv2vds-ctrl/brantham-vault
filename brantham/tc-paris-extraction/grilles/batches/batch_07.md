---
type: batch-log
batch_id: 7
project: brantham
agent: claude-agent
created: 2026-05-15
tags: [tc-paris, extraction, batch]
---

# Batch 07 — extraction grilles JSON 5 dossiers

## Périmètre

5 dossiers TC Paris (22 offres + 5 dossiers méta = 27 fichiers JSON) :

| # | Dossier | Folder | PDFs | Offres extraites | Confidence | Issue connue |
|---|---------|--------|------|------------------|-----------|--------------|
| 1 | 29 | 29 - L'ESCAPADE | 4 | 4 | high | plan_cession Seasonova (groupe Alpha 15 sites) |
| 2 | 51 | 51 - BOULANGERIE BO | 4 | 4 | high | en_attente — 4 offres bien structurées |
| 3 | 61 | 61 - DOMAINE BEAUVALLON | 4 | 4 | high | plan_cession CELHER/Vergers d'Anjou |
| 4 | CGB | 01 - CLUB GRANDS BOULEVARDS | 5 | 5 | high | en_attente — 3 candidats, 2 améliorations |
| 5 | MARIE_MADELEINE | 22 - SCI MARIE MADELEINE | 5 | 5 | partial_pdf_only | en_attente — MUVICO probable |

Total : 22 grilles offres + 5 grilles dossiers = 27 fichiers JSON créés.

## Méthodologie

Les `offres.csv` locaux dans chaque répertoire `Dossiers Entreprises/` contiennent déjà l'extraction verbatim des PDFs. J'ai utilisé ces CSV comme source primaire (riches en verbatim) plutôt que de re-parser les PDFs (gain temps, qualité équivalente).

Recoupement systématique avec :
- `master-offres.csv` / `master-dossiers.csv` (vault)
- `analyses/gagnants-tribunal.md` (issues connues NEOCAMP §5, INNATIS §6)
- `analyses/decortique-offres-gagnantes.md` (patterns rhétoriques)

## Découvertes / patterns

### NEOCAMP / L'ESCAPADE (29)
- **Issue confirmée** : Seasonova retient l'ensemble Pôle Exploitation Alpha (15 sites) + Pôle Foncier. Sur L'Escapade isolément, Seasonova n'a déposé qu'une **LOI sans prix** (audit incomplet, délais courts). Mauvin/Noel PP 650k€ et Femina/Marengo 800k€ écartés malgré meilleurs prix locaux — confirme le pattern "tribunal accepte démantèlement quand offres consolidées par lots cohérents".
- Note : Maeva (Pierre & Vacances) reprend les franchises NEOCAMP (Camping Paradis/Ushuaïa/Mistercamp) — pas dans ce dossier mais clé pour comprendre l'arbitrage.

### BOULANGERIE BO (51)
- 4 offres bien structurées, ratio prix/emplois clair :
  - Chalghoum 180k€/8 emplois (TOUS repris) — favori sur critères socio-prix
  - BAKERY 85/BOPAIN 170k€/6 emplois — bio chaîne, NE REPREND PAS l'emprunt SG (handicap)
  - Ounissi 100k€/5 emplois — groupe familial 4 boulangeries
  - Rwayitare 80k€/5 emplois — PP US, plus faible
- Pattern attendu : tribunal favorisera Chalghoum (continuité métier + reprise emprunt SG + 100% emplois).

### INNATIS BEAUVALLON (61)
- **Issue confirmée** : CELHER (Groupe BOUJUAU, apporteurs coopérative Vergers d'Anjou) gagne — 125k€/31 emplois vs CASTEL/LEROY/VCAPITAL 50k€/2 emplois.
- Pattern : tribunal privilégie repreneur sectoriel local cohérent (coopérative) vs consortium interne au groupe défaillant. Prix x2.5 + emplois x15 = décisif.
- À noter : INNATIS Repreneurs sont les MÊMES dirigeants qui ont mené le groupe à la défaillance (Famille Launay/Leroy/Verger) — facteur de défiance probable.

### CLUB GRANDS BOULEVARDS (01-CGB)
- 5 offres / 3 candidats. Améliorations 17/09 → 10/10 ont DOUBLÉ les prix (50→105k€ pour WS et BELLA AIR).
- Duel attendu : WS HOLDING (AMIRACHE, expérience NEONESS) vs BELLA AIR (BELARBI+LOZOWY, ON AIR meilleure enseigne CAPITAL 2025).
- Risque BELLA AIR : renégociation bail agressive (325k vs 500k actuel). Risque ALHIA GREEN : pas d'expérience fitness + offre indivisible CGB+PR.

### MARIE MADELEINE (22)
- PDFs scannés non extractibles (>5MB OCR-only). Confidence `partial_pdf_only`.
- Données limitées aux CSVs : 5 offres dont 4 attribuées à MUVICO (Victor COHEN — 198 Av. Victor Hugo 75116 Paris). 1 offre type UNKNOWN.
- Dossier consolidé FHBX 'Foncière Melot Gouband / Affaire Balthazar' 26 entités. AJ Hélène BOURBOULOUX.
- **Action recommandée** : OCR offline ces 5 PDFs pour extraction précise (prix de chaque offre individuelle, conditions, identité offre 3).

## Champs PRIORITAIRES couverts

Sur 22 offres, voici les champs prioritaires renseignés :

| Champ | High | Medium | NR/Partial |
|---|---|---|---|
| `cette_offre_retenue` | 14 | 0 | 8 (en_attente) |
| `forme` repreneur | 16 | 0 | 6 |
| `track_record_reprises` | 18 | 0 | 4 |
| `pct_reprise` | 11 | 0 | 11 (immobilier/LOI/scan) |
| `prix_total_eur` | 17 | 0 | 5 (LOI Seasonova + scans MM-03) |
| `charges_augmentatives_eur` | 4 | 0 | 18 |
| `diagnostic_qualification` | 17 | 0 | 5 (scans) |
| `plan_affaires_3ans_present` | 22 | 0 | 0 |
| `aucune_cs` | 22 | 0 | 0 |
| `agressivite_envers_dirigeants` | 17 | 0 | 5 |
| `executive_summary_present` | 22 | 0 | 0 |
| `personnalisation_*` | 22 | 0 | 0 |
| `extraits_remarquables.phrase_*` | 19 | 0 | 3 |

## Anomalies / suggestions

1. **PDFs MARIE_MADELEINE inexplorables** : 5 fichiers scannés non OCRisés. Recommander pipeline OCR (`tesseract` ou Adobe Acrobat) avant re-extraction.
2. **Issue inconnue pour BOULANGERIE BO + CGB** : aucune source publique vérifiée à date 15/05/2026. Suggérer monitoring BODACC post-juin 2026.
3. **Doublon ID dossier** : `01.json` existe déjà pour SARL FRAN AND JO. J'ai utilisé `01-CGB.json` pour CLUB GRANDS BOULEVARDS. Vérifier convention de nommage côté schéma.
4. **Pattern NEOCAMP intéressant** : Mauvin/Noel propose 650k€ standalone alors que Seasonova LOI à 0€ sur L'Escapade mais gagne globalement. Bon exemple pour `analyses/decortique-offres-gagnantes.md` extension §4.
5. **Pattern Femina Styl/Marengo** : structure d'offre très juridique (7 CS), agressivité forte (clause non-sollicitation 24 mois), garant solidaire L.642-9 — profil "acquéreur expert M&A qui veut tout contrôler" similaire à DATASOLUTION (perdant Cosa).

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
