---
type: daily-brief
date: 2026-04-21
generated: auto
---

# Brief Matinal — 2026-04-21

## Pipeline

- **Procédures actives** : 89 140 (statut en_cours ou plan_en_cours)
- **Scorées** : 89 630 — score moyen 37/100, max 84
- **Deals en workspace** : 260+ dossiers
- **0 teaser généré** dans tout le pipeline — goulot critique à débloquer avant fin avril

## Nouvelles Opportunités (scrape 05h00 — 1 865 annonces)

Cycle enrichissement : 466 annonces analysées, 15 qualifiées, 0 nouvelles sans dossier.

| Entreprise | Effectif | CA | Secteur | AJ |
|---|---|---|---|---|
| POLYTECHNYL | 537 sal. | 605 M€ (2024) | Chimie polyamide 6.6 — Saint-Fons (69) | AJ UP |
| Papier et Electricite (Abitol) | 268 sal. | 151 M€ (REX -1.4M€) | Industrie papier/energie | Abitol & Rousselet |
| Textiles (Ascagne) | 245 sal. | n.d. | Commerce detail textile | Ascagne |

POLYTECHNYL est le deal le plus significatif du scrape : leader europeen polyamide, 2 sites industriels, CA en déclin (1 089M€ → 605M€). Dossier AJ UP ref 57182, deadline passée (2026-02-23) — vérifier si encore actif.

## Top 10 Procédures DB (score)

| Entreprise | Score | NAF | Statut | Ouverture |
|---|---|---|---|---|
| BRANDT FRANCE | 84 | 2751Z | en_cours | 2025-10-01 |
| STAR'S SERVICE | 82 | 4941B | en_cours | 2025-01-30 |
| API TECH | 82 | 2899B | en_cours | 2025-07-03 |
| IDKIDS | 82 | 7010Z | en_cours | 2026-02-03 |
| CLINIQUE CHAMPS ELYSEES | 82 | 8610Z | plan_en_cours | 2025-12-01 |
| FTL INTER | 81 | 5229B | en_cours | 2025-11-25 |
| SILICONES ALIMENTAIRES | 81 | 2893Z | en_cours | 2025-10-01 |
| TRANSPORTS BONNARD | 80 | 4941A | en_cours | 2025-07-10 |
| COLISEE GROUP | 80 | 6420Z | en_cours | 2025-12-22 |
| ESSOR INGENIERIE | 80 | 7112B | en_cours | 2025-07-29 |

## Deadlines Proches

Aucune procédure avec date d'ouverture dans la fenêtre J-7/J+7 depuis la base BODACC.
Vérifier manuellement les date_limite dans aj_annonces.json — plusieurs champs vides ou dates passées.

## Actions Recommandées

| Priorité | Action | Impact | Délai |
|---|---|---|---|
| 1 | Générer les teasers — 0 teaser sur 260+ dossiers. Lancer `generate_teaser.py` sur les deals avec analyse + acheteurs (environ 150 éligibles). | Critique — objectif 1 deal closé fin avril | Aujourd'hui |
| 2 | Vérifier FastAPI port 8000 — down lors du cycle 05h00. Relancer si nécessaire. | Infrastructure | Maintenant |
| 3 | Matching acheteurs sur les ~40 deals avec analyse mais sans acheteurs.json. Priorité : deals industriels (SILICONES, API TECH type). | Pipeline | Ce soir |
| 4 | Qualifier POLYTECHNYL — 537 sal., CA 605M€, deal majeur. Vérifier si procédure encore ouverte, contacter AJ UP. | Opportunité haute valeur | Cette semaine |
| 5 | Lancer analyse sur les ~30 deals sans analyse (aj2m-biosency, aj2m-depixus, etc.). | Couverture pipeline | Cette semaine |

## Métriques

| Métrique | Valeur | Objectif |
|---|---|---|
| Annonces AJ (total base) | 1 865 | — |
| Procédures actives DB | 89 140 | — |
| Score moyen | 37/100 | — |
| Score max | 84/100 | — |
| Deals avec analyse | ~230 | — |
| Deals avec acheteurs | ~155 | — |
| Deals avec teaser | 0 | > 5 |
| Enrichissement CA couvert | 74% (1 388/1 865) | > 80% |
| Deals enrichis ce cycle | 2 | > 5/jour |

## Related

[[brantham/_MOC]] | [[founder/daily/2026-04-21]] | [[brantham/sessions/auto-enrichment-2026-04-21]]
