---
type: daily-brief
date: 2026-05-13
generated: auto
---

# Brief Matinal -- 2026-05-13

## Pipeline (19 deals actifs)

- **19 dossiers** dans `/deals/` — tous avec analyse présente
- **0 teaser** généré (blocage majeur : aucun dossier n'a de teaser.md)
- **10 deals** avec acheteurs identifiés, **9 sans** (matching à lancer)
- Valeur estimée globale : non calculable — PostgreSQL hors ligne (Docker arrêté)
- Rapport enrichissement du jour : absent (cycle 3h pas encore passé)

Statuts deal :

| Deal | Analyse | Teaser | Acheteurs | Enrichment |
|------|---------|--------|-----------|-----------|
| ajilink-grandest-debos-style | O | - | O | O |
| ajilink-grandest-ks-securite | O | - | O | O |
| ajilink-ihdf-ikomobi | O | - | O | O |
| ajilink-ihdf-pse-ar-val | O | - | O | O |
| ajilink-provence-prepack-cession | O | - | O | O |
| ajire-auroit | O | - | O | O |
| ajup-a-b-loisirs | O | - | O | O |
| ajup-recherche-partenaires | O | - | O | O |
| ajup-secat | O | - | O | O |
| ajup-transpaumance | O | - | O | O |
| aj2m-boulangerie-patisserie | O | - | - | O |
| aj2m-le-fournil-du-port | O | - | - | O |
| aj2m-enseignement-preparatoire | O | - | - | O |
| ajilink-grandest-construction | O | - | - | O |
| ajilink-ihdf-auto-consultant | O | - | - | O |
| ajilink-ihdf-doxense | O | - | - | O |
| ajilink-ihdf-open-bee-france | O | - | - | O |
| ajup-c2-alu | O | - | - | O |
| ajup-tilness | O | - | - | O |

## Nouvelles Opportunités (scrape 12/05/2026 -- 127 annonces, 30/40 sites)

**1. OPEN BEE FRANCE** -- Haute-Savoie (74)
- Secteur : logiciels / conseil informatique
- CA estimé : 3-10 M EUR | Effectif : 50-250 salariés
- Deadline : 03/06/2026 -- J+21
- Source : Ajilink IHDF
- Intérêt : taille significative, secteur tech, calendrier confortable

**2. PSE AR.VAL** -- Morbihan (56)
- Secteur : équipements industriels (process, manutention, traitement)
- CA estimé : >10 M EUR | Effectif : 50-250 salariés
- Deadline : non fixée (01/01/2100 -- en attente d'information)
- Source : Ajilink IHDF
- Intérêt : le plus gros CA du scan, actifs industriels potentiels

**3. BAC FILMS DISTRIBUTION / BAC FILMS FRANCE / MEDIAVORE** -- Paris (75)
- Secteur : distribution, production, coproduction cinéma/TV
- CA estimé : non renseigné | Effectif : non renseigné
- Deadline : 01/06/2026 -- J+19
- Source : AJ UP
- Intérêt : dossier multi-entités, secteur médias/culture, Paris

## Deadlines Proches (< 7 jours)

| Entreprise | Deadline | Jours restants | Secteur | Source AJ |
|-----------|----------|---------------|---------|-----------|
| SAS H&A LOCATION | 15/05/2026 | J-2 | Gestion parcs barriques (vitivinicole) | Ajilink Sud-Ouest |
| SAS TROUILLET CIE | 18/05/2026 | J-5 | Tissus/habillement (sauvegarde) | AJ UP |

Note : H&A LOCATION est en co-désignation CBF Associés / Maître CAVIGLIOLI.

## Actions Recommandées (par priorité)

1. **URGENT -- SAS H&A LOCATION (J-2)** : deadline 15/05. Décider si on monte un dossier repreneur aujourd'hui ou on passe. Secteur vitivinicole, Gironde. Accès dataroom sur Ajilink Sud-Ouest.

2. **URGENT -- TROUILLET CIE (J-5)** : deadline 18/05. Sauvegarde avec partenaires, CA 3-10M, textile habillement Loire. Profil intéressant pour repreneurs spécialisés.

3. **Relancer les teasers** : 19 dossiers ont une analyse, 0 teaser généré. Lancer `/api/deals/{slug}/generate-teaser` en batch -- priorité sur les deals avec acheteurs identifiés (10 deals).

4. **Matching acheteurs manquants** : 9 deals sans acheteurs.json -- lancer le matching 4D sur chaque.

5. **Redémarrer l'infrastructure** : Docker arrêté -- PostgreSQL et Redis inaccessibles. Lancer `docker start brantham-data-postgres-1` pour restaurer les scores et métriques DB.

6. **Scraping incomplet** : 30/40 sites scrapés (10 manquants). Relancer `scraper_aj.py` pour couvrir les sites restants.

7. **OPEN BEE FRANCE** : priorité haute, déposer dans le pipeline et lancer enrichissement Pappers dès que DB en ligne.

## Métriques

| Indicateur | Valeur | Objectif |
|-----------|--------|---------|
| Annonces scrapées (scan J-1) | 127 | >20/jour |
| Sites couverts | 30/40 (75%) | 40/40 |
| Deals en pipeline | 19 | >5 |
| Deals avec teaser | 0/19 | 19/19 |
| Deals avec acheteurs | 10/19 (53%) | >80% |
| Score moyen DB | N/A (DB offline) | -- |
| Taux enrichissement | 19/19 (100%) | >80% |
| Infrastructure | PostgreSQL DOWN | uptime >99% |
| Deadlines <7j | 2 annonces | monitoring |

---

*Généré automatiquement le 2026-05-13 -- PostgreSQL hors ligne, scores DB indisponibles.*
*Sources : aj_annonces.json (scan 2026-05-12), deals/ (19 dossiers), CONTEXT.md*
## Related
## Related
