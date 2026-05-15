---
type: index
project: brantham
created: 2026-05-15
tags: [tc-paris, index, master]
---

# TC Paris — Index Master

Point d'entrée unique pour toute l'analyse TC Paris. **104 dossiers d'offres de reprise** extraits, **566 grilles JSON** structurées, **10 livrables d'analyse transversale** (Phase 2 en cours).

## Vue d'ensemble

| Niveau | Fichier | Contenu |
|---|---|---|
| 1 | [[_MOC|MOC principal]] | Vue projet + clusters + stats |
| 2 | [[master-offres-csv|master-offres.csv]] | 570 offres consolidées brutes |
| 2 | `master-dossiers.csv` | 107 dossiers (méta procédure) |
| 3 | `grilles/offres/*.json` | 566 grilles structurées (~80 champs/offre) |
| 3 | `grilles/dossiers/*.json` | 101 fiches dossier méta |
| 4 | `analyses/*.md` | 8 analyses thématiques (voir ci-dessous) |
| 5 | `analyses/synthese-phase2/*.md` | 10 livrables transversaux (Phase 2) |

## Analyses thématiques (Phase 1)

### Stratégie & Drafting
- [[analyses/playbook-redaction-offre]] — **Playbook rédaction d'offre** (13 sections, règles confirmées par jugements, anti-patterns)
- [[analyses/decortique-offres-gagnantes]] — **Décortique rhétorique** des offres gagnantes vs perdantes (COSA, INNATIS, EURODIF — 5500 mots avec verbatims)
- [[analyses/audiences-acces-information]] — Audiences TC : sources publiques, ce qu'on récupère, monitoring automatisé

### Intelligence marché
- [[analyses/gagnants-tribunal]] — **7 dossiers décidés tracés** (COSA→Agence IF, INNATIS→Vergers d'Anjou, NEOCAMP→Seasonova+Maeva, SYM→LOM, EURODIF→AA Investments HK, MINELLI→liquidation)
- [[analyses/repreneurs-recurrents]] — Top repreneurs ≥2 dossiers (MUVICO 26, HOUSEBASE 16, VERDOSO 18, etc.)
- [[analyses/groupes-distressed]] — 6 clusters multi-entités (INNATIS, NEOCAMP, DENTEKA, SYM, COLLEGE DE PARIS, SEGI)

### Opérations
- [[analyses/vague-2026-05-15]] — Vague 2 : 11 nouveaux dossiers scrapés
- [[analyses/data-quality]] — Doublons, OCR à refaire, normalisation

## Phase 2 — Synthèse transversale ✅ LIVRÉE

3 insights majeurs émergents :
1. **Le prix médian ne discrimine PAS** (50 k€ médian retenues = 50 k€ médian rejetées). Ce qui discrimine, c'est la structure, l'absence de CS et la documentation du financement.
2. **La preuve de due diligence est le prédicteur n°1** : Δ +50,3 pts entre retenues (77%) et rejetées (27%) sur "le repreneur a-t-il documenté son étude des contrats clients/fournisseurs ?"
3. **5 kill-switches absolus** présents dans 0 retenue : périmètre marginal, indivisibilité "château de cartes", clause non-sollicitation hostile, charges augmentatives masquées, promesses renvoyées à "ultérieurement".


Folder : `analyses/synthese-phase2/`

| # | Livrable | Question |
|---|---|---|
| 1 | `01-stats-descriptives.md` | Répartition corpus par secteur/taille/procédure ? |
| 2 | `02-anatomie-winners-vs-losers.md` | Quelles variables distinguent stats retenues vs rejetées ? |
| 3 | `03-hierarchie-criteres-tribunal.md` | Verbatims jugements : motifs hiérarchisés |
| 4 | `04-portraits-robots-typologie.md` | 6 portraits-robots par typologie de cible |
| 5 | `05-recettes-rhetoriques-structure.md` | Longueur, structure, vocabulaire gagnant |
| 6 | `06-pieges-recurrents-rejetees.md` | Top 15 défauts d'offres rejetées |
| 7 | `07-signaux-credibilite-tribunal.md` | 20 signaux quantifiés (frequency winners vs losers) |
| 8 | `08-grille-scoring-100pts.md` | **Grille notation /100 d'une offre AVANT dépôt** ⭐ |
| 9 | `09-bibliotheque-extraits.md` | Formulations gagnantes par section (préambule, social, vision...) |
| 10 | `10-angles-morts.md` | Ce qu'on ne peut PAS conclure honnêtement |

## Données brutes

```
tc-paris-extraction/
├── _INDEX.md                  ← ce fichier
├── _MOC.md                    ← MOC du projet
├── _merge.py                  ← script consolidation CSV (rejouable)
├── _scrape_tc_paris.py        ← script scraping site Greffe TAE Paris
├── master-offres.csv          ← 570 offres (30 colonnes)
├── master-dossiers.csv        ← 107 dossiers (24 colonnes)
├── grilles/
│   ├── _schema.json           ← schéma JSON strict (~80 champs)
│   ├── _workflow.md           ← méthodologie d'extraction
│   ├── offres/                ← 566 grilles JSON par offre
│   ├── dossiers/              ← 101 grilles JSON par dossier
│   └── batches/               ← 23 logs d'extraction
├── raw-csv/                   ← 208 CSV individuels archivés
└── analyses/
    ├── audiences-acces-information.md
    ├── data-quality.md
    ├── decortique-offres-gagnantes.md
    ├── gagnants-tribunal.md
    ├── groupes-distressed.md
    ├── playbook-redaction-offre.md
    ├── repreneurs-recurrents.md
    ├── vague-2026-05-15.md
    └── synthese-phase2/       ← Phase 2 (10 livrables)
```

## Stats globales

- **104 dossiers** TC Paris (94 vague 1 + 10 vague 2 nouveaux)
- **570 offres** consolidées dans master CSV
- **566 grilles JSON** Phase 1 (47 retenues + 107 rejetées + 385 en attente + 27 NR)
- **6 clusters** corporate multi-entités identifiés
- **7 dossiers décidés** avec gagnant tracé (BODACC + presse + LinkedIn)
- **~30 repreneurs récurrents** ≥2 dossiers (= pipeline outreach Brantham)
- **Confidence Phase 1** : 67% high+medium, 33% low+partial

## Workflow rejouable

```bash
# Step 1 — Scraper la liste publique TC Paris
python3 vault/brantham/tc-paris-extraction/_scrape_tc_paris.py

# Step 2 — Spawn extraction agents (manuel pour l'instant — à automatiser)

# Step 3 — Re-consolider les CSV maîtres
python3 vault/brantham/tc-paris-extraction/_merge.py

# Step 4 — Re-indexer QMD
qmd update && qmd embed
```

## Related

- [[brantham/_MOC]]
- [[brantham/context/realite-business]]
- [[brantham/context/process-end-to-end]]
- [[brantham/patterns/onboarding-distressed-ma]]
- [[brantham/templates/lettre-de-mission]]
- [[_system/MOC-master]]
