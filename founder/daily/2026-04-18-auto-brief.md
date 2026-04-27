---
type: daily-brief
date: 2026-04-18
generated: auto
---

# Brief Matinal — 2026-04-18

## Pipeline (nb deals actifs, valeur estimée, statuts)

- **319 deals** dans le workspace `/deals/`
- **285 avec analyse** (34 sans analyse)
- **215 avec acheteurs identifiés** (104 sans matching 4D)
- **0 teaser généré** — goulot d'étranglement critique sur tout le pipeline
- 1 deal complet (apels) : analyse + teaser + enrichissement + dataroom
- 88 825 procédures actives en base (en_cours + plan_en_cours)

## Nouvelles Opportunités (top 3 avec détails)

Scrape AJ du 18/04 : **930 annonces** (source unique `aj_annonces.json`, toutes horodatées aujourd'hui). Top 3 par intérêt structurel :

**1. POLYTECHNYL** — AJ UP, ref 57182
- Secteur : chimie spécialisée (polyamide 6.6, plasturgie)
- Effectif : 537 salariés — Sites : Saint-Fons (69) + Valence (26)
- CA : 605 M€ (2024), 647 M€ (2023), 1 089 M€ (2022) — déclin significatif
- Deadline offres : 23/02/2026 (passée — à vérifier si toujours active)

**2. ADIAMAS** — AJ UP, ref 56103
- Secteur : fabrication lames/disques inox (préparateurs culinaires)
- Effectif : 58 salariés — Localisation : Palladuc (63)
- CA : 7,67 M€ (2024) — actif immobilier + parc machines propriétaire
- Deadline : 27/10/2025 (passée — deal historique visible)

**3. TRANSPORTS BALLET** — AJ UP, ref 55687
- Secteur : transport routier (lots, Bourgogne-Franche-Comté)
- Effectif : 45 salariés — Localisation : Frotey-Les-Lure (70)
- CA : 5 401 K€
- Deadline : 07/02/2025 (passée)

Note : l'ensemble des annonces avec date_limite ont des échéances déjà dépassées. Le scraper capture des dossiers historiques encore visibles en ligne. Aucune deadline imminente (< 7 jours) détectée dans le feed actuel.

## Deadlines Proches

- **PostgreSQL** : aucune procédure avec `date_jugement_ouverture` dans les 7 prochains jours (18–25 avril 2026).
- **AJ annonces** : 139 annonces avec `date_limite` entre janvier et avril 2026 — toutes échues. Signaux à surveiller si les AJs relancent des appels d'offres.
- Recommandation : lancer un re-scrape ciblé sur les sites AJ pour détecter de nouvelles publications fraîches.

## Actions Recommandées (priorité, impact)

| Priorité | Action | Impact |
|----------|--------|--------|
| 1 — CRITIQUE | Générer les teasers pour les 285 deals analysés (via `generate_teaser.py` batch) | Débloquer l'outreach — 0 teaser est un blocage total |
| 2 — HAUTE | Lancer le matching 4D (`enrich_v2.py --phase repreneurs`) sur les 104 deals sans acheteurs | Identifier les repreneurs qualifiés avant expiration |
| 3 — HAUTE | Traiter en priorité BRANDT FRANCE (score 84) et les 4 deals score 82 en base — analyse + teaser + matching | Ce sont les meilleures opportunités actives |
| 4 — MOYENNE | Compléter les 34 deals sans analyse (`analyze_opportunity.py`) | Pré-requis pour le teaser |
| 5 — MOYENNE | Re-scraper les 40 sites AJ pour détecter nouvelles publications fraîches | Le feed actuel ne contient que des dossiers anciens |

## Métriques (score moyen, enrichissement, couverture)

| Métrique | Valeur | Objectif |
|----------|--------|----------|
| Annonces AJ scrapées (aujourd'hui) | 930 | > 20 nouvelles/jour |
| Procédures actives en base | 88 825 | — |
| Score moyen (en_cours) | 36 / 100 | — |
| Score max (en_cours) | 84 / 100 (BRANDT FRANCE) | — |
| Deals avec analyse | 285 / 319 (89 %) | > 80 % |
| Deals avec acheteurs | 215 / 319 (67 %) | > 80 % |
| Deals avec teaser | 0 / 319 (0 %) | 100 % |
| Enrichissement financier (session 03h13) | 441 opportunités traitées | — |
| Deals clôturés | 0 | 1 avant fin avril |

---
*Généré automatiquement par Claude Code — 2026-04-18 07:55*
*Sources : aj_annonces.json, PostgreSQL brantham, /deals/ workspace, vault/brantham/sessions/auto-enrichment-2026-04-18.md*
## Related
