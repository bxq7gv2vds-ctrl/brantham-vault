---
type: index
project: brantham
phase: phase2
created: 2026-05-15
tags: [tc-paris, synthese, index, phase2]
---

# Synthèse Phase 2 — Analyse transversale TC Paris

Index des 10 livrables produits à partir de 566 offres + 101 dossiers extraits du TAE Paris, fenêtre septembre 2024 — avril 2026.

## Corpus

- **566 offres** dans `grilles/offres/*.json` (47 retenues, 107 rejetées, 385 en attente, 27 NR)
- **101 dossiers** dans `grilles/dossiers/*.json` (114 issues `plan_cession_arrete`, 6 `liquidation`, 446 `en_attente`)
- Schéma : `grilles/_schema.json`
- Pickle de travail : `synthese-phase2/offres.pkl` + `dossiers.pkl`
- Scripts : `synthese-phase2/_run_analysis.py`, `_compute_stats.py`, `_compute_motifs.py`, `_extracts_winners.py`
- Report JSON : `synthese-phase2/stats_report.json`

## Les 10 livrables

| # | Livrable | Objet | Statut |
|---|---|---|---|
| 1 | [[01-stats-descriptives]] | Distributions secteur, taille, procédure, repreneur, prix, pct reprise | OK |
| 2 | [[02-anatomie-winners-vs-losers]] | 50+ variables comparées entre 47 retenues et 107 rejetées | OK |
| 3 | [[03-hierarchie-criteres-tribunal]] | Thématisation des motifs tribunal — pérennité (45 %) dominante | OK |
| 4 | [[04-portraits-robots-typologie]] | 6 typologies (retail multi-sites, industriel, service B2B, tech, réglementé, foncière) | OK |
| 5 | [[05-recettes-rhetoriques-structure]] | Longueur médiane 13,5 p, sommaire 89 %, ton mixte, vocabulaire winning | OK |
| 6 | [[06-pieges-recurrents-rejetees]] | Top 15 défauts, kill-switches absolus, cas iconique MINELLI | OK |
| 7 | [[07-signaux-credibilite-tribunal]] | 24 signaux hiérarchisés Tier S/A/B/C — Kbis, attestation bancaire, étude contrats | OK |
| 8 | [[08-grille-scoring-100pts]] | **Grille opérationnelle 32 critères /100 calibrée sur corpus** | OK |
| 9 | [[09-bibliotheque-extraits]] | Verbatims winning pour préambule, vision, social, prix, substitution, CS | OK |
| 10 | [[10-angles-morts]] | 7 catégories de limites — sélection, doublons, secteurs, post-cession, ressort, temps, technique | OK |
| 11 | [[11-tests-statistiques-et-analyses-residuelles]] | Tests chi-deux/Fisher/Mann-Whitney, réplication sous-corpus fiable, cabinet/AJ/délai v1-v2, contre-vérification ML de la grille | OK |

## Trois insights majeurs émergents

### Insight 1 — Le prix médian ne discrimine PAS retenues vs rejetées

Médiane prix retenues = 50 k€. Médiane prix rejetées = 50 k€. **Identiques.** Ce qui discrimine, c'est :
- la **structure du prix** (ventilation incorporels/corporels/stocks, modalités comptant, transparence des charges augmentatives) ;
- l'**absence de conditions suspensives** (40 % winners vs 8 % losers — facteur ×5) ;
- la **documentation du financement** (attestation bancaire : 50 % winners vs 8 % losers).

→ Coller un prix élevé sur une offre mal documentée ne gagne pas. Coller un prix faible mais bien structuré et bien documenté peut gagner.

### Insight 2 — La preuve de due diligence est le prédicteur n°1

Le marqueur le plus discriminant du corpus n'est ni le prix, ni le pct de reprise — c'est **« le repreneur a-t-il documenté son étude des contrats clients et fournisseurs ? »** : 76,9 % chez retenues vs 26,6 % chez rejetées, Δ +50,3 points.

Suivent dans le top 5 : déclaration L.642-3 signée (Δ +46,8 pts), Kbis annexé (Δ +42,1 pts), attestation bancaire (Δ +42,1 pts), soutien banques historiques (Δ +37,6 pts).

→ Une offre Brantham doit **dédier un paragraphe explicite à la DD opérée** — contrats clients étudiés (avec noms), visite de site mentionnée, rencontre équipes datée. C'est gratuit à produire et c'est le top de la grille.

### Insight 3 — Les 5 kill-switches qui condamnent une offre

Cinq erreurs présentes dans 0 retenue mais récurrentes chez les rejetées :

1. **Périmètre marginal vs concurrent connu plus large** (17 cas observés, 0 retenue)
2. **Indivisibilité « château de cartes »** (14 cas, 0 retenue) — cas CASTEL+LEROY+VCAPITAL avec 11 offres indivisibles
3. **Clause non-sollicitation imposée aux dirigeants sortants** (cas COSA / DATASOLUTION, kill-switch sec)
4. **Charges augmentatives masquées** (cas DATASOLUTION 745 k€ BFR non listés)
5. **Promesses renvoyées à plus tard** (« caractéristiques NewCo communiquées ultérieurement », « BP en cours », « liste salariés en cours »)

→ Avant tout dépôt Brantham, faire un **check pré-dépôt** sur ces 5 kill-switches.

## Application immédiate

- **Magic Form Levallois** (premier deal signé, deadline 21/05/2026 12h) : appliquer la [[08-grille-scoring-100pts|grille de scoring]] à l'offre projetée avant dépôt. Cibler 75/100 minimum.
- **Mises à jour du playbook** : intégrer les 9 réflexes de [[05-recettes-rhetoriques-structure|recettes rhétoriques]] dans `vault/_system/templates/note-cadrage-deal.md` et la lettre-de-mission.
- **Open Bee France** (deadline 03/06/2026 16h00) : appliquer la grille au dossier — vérifier que les offres pré-déposées (Konica défensif, Yooz/Sword, Tessi/HLD) sont analysées sous l'angle des 5 kill-switches.

## Pipeline de mise à jour

À mesure que les 385 offres en attente passent en audience (printemps-été 2026) :
1. Relancer `_run_analysis.py` puis `_compute_stats.py` pour reconstruire les pickles
2. Mettre à jour les chiffres dans les livrables 01-02-07-08
3. Re-calibrer la grille de scoring (livrable 08) si les pondérations doivent évoluer
4. Tracker chaque winner ajouté dans `vault/brantham/post-cession/` pour le suivi post-cession

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/playbook-redaction-offre]]
- [[brantham/tc-paris-extraction/analyses/data-quality]]
- [[brantham/deals/active/magic-form-levallois/_MOC]]
- [[brantham/deals/active/open-bee-france/_MOC]]
