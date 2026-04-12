---
type: daily-brief
date: 2026-04-12
generated: auto
---

# Brief Matinal -- 2026-04-12

## Pipeline (deals actifs, statuts)

- **254 dossiers** dans le workspace deals
- **0 teaser généré** sur 254 -- goulot d'étranglement critique
- ~200 avec analyse.md, ~50 sans acheteurs.json
- ~50 dossiers sans analyse ni acheteurs (aucune action faite)
- 1 dossier complet : `aj2m-apels` (analyse présente, pas de teaser)
- Données PostgreSQL indisponibles : Docker arrêté, psql absent du PATH

## Nouvelles Opportunités (scraping du 2026-04-11)

Scraping : 31 sites couverts, 24 OK, 6 vides, 1 erreur -- 463 opportunités indexées.

**Top 3 à examiner (identification manuelle depuis le JSON) :**

1. **AV.CO. BOIS** -- Ajilink Sud-Ouest
   Construction bâtiments ossature bois. CA 3-10M, 50-250 salariés. 31 Haute-Garonne.
   Deadline : 13/02/2026. Type : cession. Fort potentiel acquéreurs industriels bois/BTP.

2. **CHÂTEAU DE SACY** -- Ajilink Sud-Ouest
   Hôtel 5 étoiles 12 chambres + restaurant bistronomique. 10-50 salariés. 51 Marne.
   Deadline : 30/01/2026. Type : cession. Actif rare, forte valeur patrimoniale.

3. **TELE MENAGER MORÉ** -- Ajilink Sud-Ouest
   Distribution électroménager gros et détail. CA 3-10M, 10-50 salariés. 81 Tarn.
   Deadline : 03/04/2026. Type : cession. Acquéreurs : GSS régionales, franchises.

Note : deadlines des opportunités ci-dessus sont dépassées -- vérifier si encore actives.

## Deadlines Proches

Données PostgreSQL inaccessibles -- impossible de requêter les deadlines DB.

Depuis aj_annonces.json, aucune deadline dans les 7 prochains jours identifiée automatiquement sur le scraping du 11/04.

Action requise : relancer Docker (`docker start brantham-data-postgres-1`) pour accéder aux vraies deadlines procédures.

## Actions Recommandées (par priorité)

| Priorité | Action | Impact |
|----------|--------|--------|
| 1 -- URGENT | Relancer Docker + PostgreSQL | Toute la data pipeline est aveugle sans DB |
| 2 -- URGENT | Générer teasers (0/254) | Bloque toute la chaîne de valeur outreach |
| 3 -- HAUT | Lancer `enrich_v2.py --batch 5` sur deals score > 50 sans acheteurs | Pipeline Hunter bloqué |
| 4 -- HAUT | Relancer scraping AJ (dernier : 11/04) | Manque 9 sites (7 vides + 1 erreur) |
| 5 -- MOYEN | Générer analyses pour ~50 dossiers sans analyse.md | aj2m-depixus, aj2m-gab-france-retail, aj2m-golf, etc. |

## Métriques

| Indicateur | Valeur | Objectif | Statut |
|-----------|--------|----------|--------|
| Opportunités détectées (scraping) | 463 | > 20/jour | OK |
| Deals en pipeline | 254 | > 5 | OK |
| Deals avec teaser | 0 | > 5 | CRITIQUE |
| Deals avec acheteurs | ~200 | > 80% | Partiel |
| Sites AJ couverts | 24/31 | 40 | En dessous |
| Session enrichissement 2026-04-12 | Aucune | -- | Manquant |
| PostgreSQL | Inaccessible | Uptime 99% | CRITIQUE |

## Related

- [[brantham/_MOC]]
- [[founder/daily/2026-04-12-auto-brief]]
