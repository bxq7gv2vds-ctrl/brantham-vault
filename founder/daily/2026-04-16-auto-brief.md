---
type: daily-brief
date: 2026-04-16
generated: auto
---

# Brief Matinal -- 2026-04-16

## Pipeline (deals actifs)

- **88 216** procédures actives en base (statut `en_cours` + `plan_en_cours`)
- **465** annonces AJ scrapées (scrape du 2026-04-15, 31 sites couverts)
- **26** nouvelles opportunités avec date limite en avril 2026
- **0** rapport d'enrichissement trouvé pour aujourd'hui (`auto-enrichment-2026-04-16.md` absent)

Deals workspace : pratiquement tous les dossiers sont **bloqués au stade "teaser"** — aucun teaser généré sur l'ensemble du pipeline.

---

## Nouvelles Opportunités (top sélection avril 2026)

| # | Entreprise | Secteur | Statut |
|---|-----------|---------|--------|
| 1 | TECH POWER ELECTRONICS | Électronique / tech | Nouveau, sans analyse |
| 2 | MARTECH | Marketing tech | Nouveau, sans analyse |
| 3 | INGEBIME | Ingénierie BIM | Nouveau, sans analyse |

26 nouvelles annonces entrées ce mois (date_limite avril 2026). Aucun score_pertinence calculé sur ces entrées — l'étape de qualification LLM n'a pas été lancée.

---

## Top 10 Procédures par Score (en_cours)

| Entreprise | Score | NAF | Ouverture |
|-----------|-------|-----|-----------|
| BRANDT FRANCE | **84** | 2751Z (électroménager) | 2025-10-01 |
| API TECH | 82 | 2899B (équipements industriels) | 2025-07-03 |
| IDKIDS | 82 | 7010Z (holding) | 2026-02-03 |
| STAR'S SERVICE | 82 | 4941B (transport) | 2025-01-30 |
| FTL INTER | 81 | 5229B (logistique) | 2025-11-25 |
| STE D'APPLIC. SILICONES ALIMENTAIRES | 81 | 2893Z (agroalimentaire) | 2025-10-01 |
| ESSOR INGÉNIERIE | 80 | 7112B (ingénierie) | 2025-07-29 |
| COLISEE GROUP | 80 | 6420Z (holding) | 2025-12-22 |
| TRANSPORTS BONNARD | 80 | 4941A (transport) | 2025-07-10 |
| EURODIF | 79 | 4751Z (textile) | 2026-01-30 |

---

## Deadlines Proches

26 annonces AJ avec date_limite en avril 2026. Pas de date_limite précise récupérée dans ce scan (champ vide sur la majorité). Priorité : **lancer le scrape avec `--llm`** pour qualifier et extraire les dates limites.

Procédures récentes à surveiller (ouverture < 3 mois) :
- **IDKIDS** (score 82, ouv. 2026-02-03) — holding, procédure active
- **EURODIF** (score 79, ouv. 2026-01-30) — textile, cession probable

---

## Actions Recommandées (par priorité)

| Priorité | Action | Impact |
|---------|--------|--------|
| 1 — CRITIQUE | Générer les teasers manquants sur les deals avec analyse existante (40+ dossiers bloqués) | Débloque tout l'outreach |
| 2 — HAUTE | Lancer `scraper_aj.py --llm` pour qualifier les 26 nouvelles annonces et extraire dates limites | Évite les deals ratés |
| 3 — HAUTE | Enrichir BRANDT FRANCE (score 84) + API TECH (82) — vérifier si dossiers deals existants | Deals prioritaires |
| 4 — MOYENNE | Lancer `enrich_v2.py --batch 5` sur les 5 deals les mieux scorés sans acheteurs | Avance matching 4D |
| 5 — MOYENNE | Relancer le pipeline d'enrichissement quotidien et logger dans vault/brantham/sessions/ | Couverture financière |

Deals les plus critiques (ni analyse ni acheteurs) :
- `abitbol-restauration`
- `aj2m-activit-accueil-collectif-de-jeunes-enfants`

---

## Métriques

| Indicateur | Valeur | Objectif |
|-----------|--------|---------|
| Procédures actives en base | 88 216 | -- |
| Score moyen (toutes procédures) | 37 / 100 | -- |
| Score max en base | 84 (BRANDT FRANCE) | -- |
| Annonces AJ scrapées | 465 (31 sites) | > 20 nouvelles/jour |
| Nouvelles annonces avril 2026 | 26 | -- |
| Deals avec analyse | ~40+ | -- |
| Deals avec teaser | 0 | Blocage critique |
| Enrichissement du jour | Aucun (session absente) | Cycle 3h non lancé |
| Uptime infra | PostgreSQL OK | -- |

---

*Généré automatiquement le 2026-04-16 — sources : PostgreSQL brantham, aj_annonces.json (2026-04-15), deals workspace*
