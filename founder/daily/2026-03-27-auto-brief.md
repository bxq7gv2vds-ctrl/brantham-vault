---
type: daily-brief
date: 2026-03-27
generated: auto
---

# Brief Matinal -- 2026-03-27

## Pipeline

- **45 deals** dans le workspace (brantham-pipeline/deals/)
- 29 avec analyse / 1 avec teaser / 20 avec acheteurs identifies / 36 enrichis
- **0 deal complet** (analyse + teaser + acheteurs)
- PostgreSQL inaccessible ce matin (Docker non demarre) -- scores et volumes globaux indisponibles

## Nouvelles Opportunites (AJ Scraping)

Source : `aj_annonces.json` date 2026-03-26 -- 31 sites, 25 ok, 6 vides.

**468 annonces actives** (toutes statut "nouveau", pas de qualification LLM ce cycle).

Top 3 a traiter en priorite (deadlines aujourd'hui) :

1. **POMME DE PAIN SAS** (FHBX) -- date limite 2026-03-27 -- restauration/franchise
2. **KRYSAL'ID SARL** (AJRS) -- date limite 2026-03-27
3. **CASSITRANS** (AJRS) -- date limite 2026-03-27

## Deadlines Proches (< 7 jours)

| Entreprise | Source AJ | Date limite |
|---|---|---|
| POMME DE PAIN SAS | FHBX | 2026-03-27 (aujourd'hui) |
| KRYSAL'ID SARL | AJRS | 2026-03-27 (aujourd'hui) |
| CASSITRANS | AJRS | 2026-03-27 (aujourd'hui) |
| STE D'ETUDES ET D'APPLICATIONS MECANIQUES | FHBX | 2026-03-27 (aujourd'hui) |
| LES INVITES AU FESTIN ASSOCIATION | AJRS | 2026-03-31 |
| MECADEP SAS | AJRS | 2026-03-31 |
| Diffusion marques streetwear | AJRS | 2026-03-31 |
| CABASSE SA | FHBX | 2026-04-02 |
| TECH POWER ELECTRONICS | AJRS | 2026-04-03 |
| THIERRY BEURON / TRANSFRIGO 11 SAS | FHBX | 2026-04-03 |

**4 deadlines aujourd'hui** -- action immediate requise.

## Actions Recommandees

**Urgent (aujourd'hui)**
1. Traiter les 4 deals avec deadline 2026-03-27 : verifier datarooms, contacter AJ si pas de dossier complet.
2. Demarrer Docker pour restaurer l'acces PostgreSQL et les scores qualification.

**Haute priorite (cette semaine)**
3. Generer les teasers manquants : 28 deals ont une analyse complete mais zero teaser. Lancer `generate_teaser.py` en batch sur les plus avances.
4. Identifier les acheteurs : 9 deals ont analyse mais pas d'acheteurs -- lancer matching 4D.
5. Qualifier les 468 annonces AJ avec LLM (`scraper_aj.py --llm`) pour obtenir des scores pertinence > 0.

**Normal**
6. Relancer le pipeline quotidien Prefect (BODACC delta + scoring) une fois Docker actif.
7. Enrichir les 16 deals entierement vides (analyse + teaser + acheteurs absents).

## Metriques

| Metrique | Valeur | Objectif |
|---|---|---|
| Opportunites AJ detectees | 468 | > 20/jour |
| Deals en pipeline | 45 | > 5 |
| Deals avec analyse | 29 (64%) | - |
| Deals avec teaser | 1 (2%) | - |
| Deals enrichis | 36 (80%) | > 80% |
| Deals complets | 0 | > 1 |
| Score moyen DB | N/A (Docker down) | - |
| Session enrichissement | Aucune aujourd'hui | Cycle 3h |
| Infrastructure | PostgreSQL/Docker DOWN | 99% uptime |

## Related
- [[_system/MOC-master]]
- [[brantham/context/2026-03-27-contexte-complet]]
