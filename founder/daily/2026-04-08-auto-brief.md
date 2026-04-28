---
type: daily-brief
date: 2026-04-08
generated: auto
---

# Brief Matinal -- 2026-04-08

## Infrastructure

**ALERTE : PostgreSQL hors ligne.** Docker n'est pas actif (socket introuvable). Scores DB indisponibles.
Commande de relance : `docker start brantham-data-postgres-1`

---

## Pipeline

- **Deals workspace** : 208 dossiers au total
- **Sans analyse** : 32 dossiers (15%)
- **Sans teaser** : 208 dossiers (100% -- teaser.md absent dans tous)
- **Sans acheteurs** : 72 dossiers (35%)
- **Deals complets** : 0 (hors `apels` qui reste la reference)
- **Valeur pipeline** : non calculable (DB offline)

---

## Nouvelles Opportunites (top 3 -- scrape du jour)

Scrape effectue ce matin a 05h00, **1804 annonces** en base.

**1. ADIAMAS -- AJ UP (63)**
Fabrication de lames et disques acier inox pour preparateurs culinaires. CA 7.67 M€, 58 salaries.
Actif immobilier proprietaire + parc machines industriel (decoupe, emboutissage, polissage, soudure).
Date limite : 27/10/2025 (passee -- verifier si toujours active).

**2. ATELIER DE L'EYRIEUX -- ajilink-ihdf**
Entreprise du Patrimoine Vivant. CA 9 M€.
Date limite : **10/04/2026** -- J+2. Prioritaire.

**3. TRANSPORTS BALLET -- AJ UP (70)**
Transport routier national, Bourgogne-Franche-Comte. CA 5.4 M€, 45 salaries.
Reseau regulier regional etabli. Date limite passee (07/02/2025) -- verifier statut.

---

## Deadlines Proches (< 7 jours)

| Entreprise | Date limite | CA | Note |
|---|---|---|---|
| MONTE CARLO (SNC) | 08/04 -- AUJOURD'HUI | 881 k€ | Carpentras |
| Redressement judiciaire (anonyme) | 08/04 -- AUJOURD'HUI | 6.6 M€ | Urgence |
| RELAIS COLIS | 09/04 | n/d | |
| SAS MENAPS | 09/04 | n/d | |
| ATELIER DE L'EYRIEUX | 10/04 | 9 M€ | Patrimoine Vivant -- prioritaire |
| DDA-MPC | 10/04 | 494 k€ | |
| MECANIC WORKER | 13/04 | 2.9 M€ | Garage industriel |
| Papier et electricite | 13/04 | 151 M€ | Tres grand -- adossement |
| TOWT (transport voile) | 14/04 | n/d | Le Havre -- niche |
| Boulangerie Lyon | 14/04 | 3.4 M€ | CA solide |
| GARAGE DES STUARTS | 15/04 | n/d | |
| CAELI ENERGIE | 15/04 | n/d | |
| Cloud Computing | 15/04 | 2.3 M€ | 40 sal. -- actifs tech |

**Total deadlines <= 7j : 26 annonces**

---

## Actions Recommandees

| Priorite | Action | Impact |
|---|---|---|
| 1 | Relancer Docker / PostgreSQL | Bloquant -- scores et DB indisponibles |
| 2 | Analyser ATELIER DE L'EYRIEUX avant le 10/04 | Deadline J+2, CA 9M€, EPV |
| 3 | Verifier statut RJ anonyme CA 6.6M€ (deadline aujourd'hui) | Fenetre ferme ce soir |
| 4 | Lancer `generate_teaser.py` sur les deals avec analyse existante | 0 teaser sur 208 dossiers |
| 5 | Lancer matching acheteurs sur les 72 deals sans `acheteurs.json` | Revenue driver |
| 6 | Relancer scraper AJ (prochain cycle 3h) pour mise a jour | 1804 annonces en base |

---

## Metriques

| Metrique | Valeur | Objectif |
|---|---|---|
| Annonces AJ en base | 1 804 | -- |
| Scrape du jour | oui (05h00) | cycle 3h |
| Deals workspace | 208 | -- |
| Deals avec analyse | 176 / 208 (85%) | -- |
| Deals avec teaser | 0 / 208 (0%) | prioritaire |
| Deals avec acheteurs | 136 / 208 (65%) | -- |
| Deadlines <= 7j | 26 annonces | -- |
| Score moyen DB | n/d (DB offline) | -- |
| Rapport enrichissement | absent | cycle 3h |
| PostgreSQL | OFFLINE | relancer |

---

*Brief genere automatiquement -- 2026-04-08 07:55*
*Sources : aj_annonces.json (1804 entrees), deals/ (208 dossiers), PostgreSQL indisponible*
## Related
## Related
