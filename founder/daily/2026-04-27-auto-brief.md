---
type: daily-brief
date: 2026-04-27
generated: auto
---

# Brief Matinal -- 2026-04-27

## Pipeline (deals actifs)

- **374 dossiers** dans le workspace deals (brantham-pipeline/deals/)
- **0 dossier complet** (analyse + teaser + acheteurs simultanes)
- **341 deals avec analyse**, 0 avec teaser, 253 avec acheteurs
- Rapport d'enrichissement du jour : absent (auto-enrichment non execute aujourd'hui)
- AJ annonces : **1 853 annonces** chargees dans aj_annonces.json (pas de date de scraping disponible -- fraicheur inconnue)

## Nouvelles Opportunites (top 3 par score DB)

| Rang | Societe | Score | Secteur | Effectif | Statut | Ouverture |
|------|---------|-------|---------|----------|--------|-----------|
| 1 | **BRANDT FRANCE** | 84/100 | Electromenager (2751Z) | 500-999 sal. | en_cours | 01/10/2025 |
| 2 | **CLINIQUE DU ROND POINT DES CHAMPS ELYSEES** | 82/100 | Sante (8610Z) | 50-99 sal. | plan_en_cours | 01/12/2025 |
| 3 | **API TECH** | 82/100 | Industrie (2899B) | 250-499 sal. | en_cours | 03/07/2025 |

Egalement en score 82 : STAR'S SERVICE (transport, 2 000+ sal.) et IDKIDS (holding, ouverture fev. 2026).

## Deadlines Proches

Aucune procedure avec date limite dans les 7 prochains jours n'a ete identifiee en base. La requete sur les jugements recents (30 jours) n'a retourne aucun resultat -- verifier si la table `annonce_bodacc` contient des dates de cloture plus precises.

## Actions Recommandees (par priorite)

1. **[CRITIQUE] Generer les teasers** -- 374 deals ont une analyse mais aucun teaser. Lancer `generate_teaser.py` en batch sur les deals prioritaires (score > 70). Sans teaser, pas d'outreach possible.

2. **[HAUTE] Relancer le scraping AJ** -- La date de scraping des 1 853 annonces est inconnue. Executer `scraper_aj.py --output /tmp/aj_scan.json` et copier vers `api/aj_annonces.json` pour rafraichir la veille.

3. **[HAUTE] Completer le matching acheteurs** -- 121 deals sans `acheteurs.json`. Lancer `enrich_v2.py --batch 10 --phase repreneurs` sur les dossiers prioritaires.

4. **[MOYENNE] Enrichissement financier** -- Score moyen base : 37/100, seuil cible > 50. Identifier les procedures > 50 sans bilan via la requete du CONTEXT.md et enrichir via Pappers (quota ~100 req/jour).

5. **[SUIVI] Pipeline quotidien** -- Verifier que `orchestration/daily.py` a bien tourne cette nuit (BODACC delta, scoring, fraicheur). Aucun log de session detecte aujourd'hui.

## Metriques

| Metrique | Valeur | Objectif |
|----------|--------|----------|
| Procedures actives en base | 89 630 | -- |
| Procedures scorees | 89 630 | -- |
| Score moyen | 37/100 | -- |
| Score max (BRANDT FRANCE) | 84/100 | -- |
| Annonces AJ chargees | 1 853 | > 20 nouvelles/jour |
| Deals workspace | 374 | -- |
| Deals avec analyse | 341 (91%) | -- |
| Deals avec teaser | 0 (0%) | > 5 |
| Deals avec acheteurs | 253 (68%) | > 80% |
| Rapport enrichissement du jour | ABSENT | present |

## Related

- [[brantham/_MOC]]
- [[founder/daily/2026-04-27-auto-brief]]
