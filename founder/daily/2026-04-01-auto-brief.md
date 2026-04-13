---
type: daily-brief
date: 2026-04-01
generated: auto
---
# Brief Matinal -- 2026-04-01

## Pipeline (deals actifs, valeur estimee, statuts)

- **78 331** procedures en_cours en base (+ 8 727 plan_en_cours)
- **129 deals** dans le workspace local (`deals/`)
  - 103 avec analyse | 0 avec teaser | 89 avec acheteurs
  - 26 deals entierement vierges (aucun des trois elements)
  - 0 deals complets (analyse + teaser + acheteurs) -- seul `apels` avait les 4 elements selon CONTEXT.md
- Feed AJ scrape du 2026-03-31 : **459 opportunites** (31 sites, 25 ok, 6 vides)
  - 342 cessions | 110 redressements | 4 liquidations | 3 sauvegardes
- Session auto-enrichment du jour : 2 cycles executes (03h26 : 454 opps | 06h26 : 453 opps)

## Nouvelles Opportunites (top 3 AJ, grandes entreprises)

1. **GROUPE JOTT - JOTT OPERATIONS** (Ajilink Provence)
   - Secteur : Commerce d'habillement specialise | CA : Plus de 10M | Effectif : Plus de 250
   - Type : Cession | Date limite AJ : 05/02/2026 a 16h00 (passee -- dossier a requalifier)
   - Region : 13 Bouches-du-Rhone

2. **AV.CO. BOIS** (Ajilink Sud-Ouest)
   - Secteur : Bois/materiaux | CA : 3-10M | Effectif : 50-250
   - Type : Cession | Pas de date limite renseignee

3. **CANAL** (Ajilink IHDF)
   - Secteur : Non renseigne | CA : 1-3M | Effectif : 50-250
   - Type : Cession | Pas de date limite renseignee

Note : aucune opportunite n'a de score_pertinence renseigne (LLM qualification desactivee au scrape).

## Deadlines Proches (procedures AJ dans les 7 jours)

Deadlines critiques issues du feed AJ (< 7 jours depuis aujourd'hui) :

| Entreprise | Date limite | Source |
|---|---|---|
| CABASSE SA | 2026-04-02 | AJ |
| Fonds de commerce -- Maisons Laffitte | 2026-04-03 | AJ |
| TECH POWER ELECTRONICS | 2026-04-03 | AJ |
| THIERRY BEURON / TRANSFRIGO 11 SAS | 2026-04-03 | AJ |
| Materiel ou mobilier -- GAMBAIS | 2026-04-03 | AJ |

Note DB : le champ `date_jugement_ouverture` ne correspond pas a une deadline de cession. Les procedures retournees par la requete "deadline <= 7 jours" ont des dates d'ouverture historiques (2000-2021) -- pas de vrai deadline imminent identifiable via la DB seule.

## Actions Recommandees (priorite, impact)

| Priorite | Action | Impact |
|---|---|---|
| URGENT | Contacter AJ pour CABASSE SA avant le 02/04 | Deal potentiel J+1 |
| URGENT | Verifier TECH POWER ELECTRONICS et TRANSFRIGO 11 avant 03/04 | 3 deals deadline demain |
| HAUTE | Lancer generation teaser sur les 103 deals avec analyse | 0 teaser = 0 deal closable |
| HAUTE | Activer LLM qualification au scrape (--llm flag) | Score pertinence absent sur 459 opps |
| HAUTE | Enrichir les 26 deals vierges (analyse manquante) | `enrich_v2.py --batch 5` |
| MOYENNE | Lancer matching 4D sur deals avec analyse mais sans acheteurs (14 deals) | Accelerer pipeline |
| MOYENNE | Qualifier GROUPE JOTT -- date limite passee, statut a verifier | CA > 10M, 250+ employes |

## Metriques (score moyen, enrichissement, couverture)

| Metrique | Valeur | Objectif |
|---|---|---|
| Procedures en_cours DB | 78 331 | -- |
| Procedures scorees | 89 630 | -- |
| Score moyen global | 37 / 100 | -- |
| Score max observe | 84 / 100 (BRANDT FRANCE) | -- |
| Deals workspace total | 129 | > 5 actifs |
| Taux couverture analyse | 80% (103/129) | > 80% |
| Taux couverture teaser | 0% (0/129) | Cible : 100% des analyses |
| Taux couverture acheteurs | 69% (89/129) | > 80% |
| Opportunites AJ scrapees | 459 (31 mars) | > 20/jour |
| Sites AJ en erreur | 0 (6 vides) | 0 |
| Enrichissement session | 2 cycles (03h26, 06h26) | Cycle 3h OK |
