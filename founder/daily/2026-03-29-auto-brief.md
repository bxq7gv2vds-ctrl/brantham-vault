---
type: daily-brief
date: 2026-03-29
generated: auto
---

# Brief Matinal -- 2026-03-29

## Pipeline (procedures actives)

| Metrique | Valeur |
|---|---|
| Procedures en_cours | 77 977 |
| Procedures plan_en_cours | 8 727 |
| Total actives | 86 704 |
| Procedures scorees | 89 630 |
| Score moyen | 37 / 100 |
| Score max | 87 |
| Deals workspace | 85+ dossiers (scrape multi-AJ) |

Score concentre en bas de distribution (moy. 37). Seules 10 procedures atteignent score >= 79.

---

## Nouvelles Opportunites (AJ scrape 2026-03-28)

**463 opportunites detectees** -- 31 sites scrapes (25 ok, 6 vides). Toutes au statut "nouveau". Aucune qualification LLM effectuee. Top 3 par taille :

**1. AV.CO. BOIS** -- Ajilink Sud-Ouest
- Secteur : construction ossature bois / structures legeres
- Effectif : 50-250 salaries | CA : 3-10M EUR
- Type : cession | Departement : 31 Haute-Garonne
- Date limite scraped : 13/02/2026 (echue -- verifier actualite)

**2. USINE DE PANIFICATION (ref. 3330)** -- Ajilink Sud-Ouest
- Secteur : panification industrielle
- Effectif : 50-250 salaries | CA : 3-10M EUR
- Type : cession | Dataroom disponible

**3. ADIAMAS** -- AJ UP
- Effectif : 50-250 salaries | CA : 3-10M EUR
- Type : cession

Autres opportunites comparables : MGL (Lolly's, franchise retail) et organisme de formation numerique (P2G), meme gabarit.

---

## Top Procedures DB (score >= 79)

| Rang | Raison sociale | Score | NAF | Effectif | Statut | Ouverture |
|---|---|---|---|---|---|---|
| 1 | BRANDT FRANCE | 87 | 2751Z Electromenager | 500-999 | en_cours | 2025-10-01 |
| 2 | STE APPLIC. SILICONES ALIMENTAIRES | 83 | 2893Z Agro-ind. | 100-199 | en_cours | 2025-10-01 |
| 3 | CLINIQUE CHAMPS-ELYSEES | 82 | 8610Z Sante | 50-99 | plan_en_cours | 2025-12-01 |
| 4 | STAR'S SERVICE | 82 | 4941B Transport | 2000-4999 | en_cours | 2025-01-30 |
| 5 | API TECH | 82 | 2899B Industrie | 250-499 | en_cours | 2025-07-03 |
| 6 | FTL INTER | 81 | 5229B Logistique | 20-49 | en_cours | 2025-11-25 |
| 7 | COLISEE GROUP | 80 | 6420Z Holdings | 3-5 | en_cours | 2025-12-22 |
| 8 | ESSOR INGENIERIE | 80 | 7112B Ingenierie | 50-99 | en_cours | 2025-07-29 |
| 9 | TRANSPORTS BONNARD | 80 | 4941A Transport | 100-199 | en_cours | 2025-07-10 |
| 10 | IDKIDS | 79 | 7010Z Management | 10-19 | en_cours | 2026-02-03 |

---

## Deadlines Proches

Aucune procedure avec `date_fin_observation` dans les 7 prochains jours (requete DB retourne vide).

Pour les annonces AJ : AV.CO. BOIS avait une date limite au 13/02/2026 -- potentiellement echue, verifier directement sur le site AJ.

---

## Etat Deals Workspace (actions requises)

| Etat | Nombre |
|---|---|
| Sans analyse.md | 24+ |
| Sans teaser.md | 100+ (quasi-totalite) |
| Sans acheteurs.json | 36+ |
| Deal complet (analyse + teaser + enrichissement) | 1 (aj2m-apels) |

Rapport auto-enrichissement 2026-03-29 : absent (pipeline non execute ce matin).

---

## Actions Recommandees

**Priorite 1 -- immediat**
- Lancer scraping AJ aujourd'hui (dernier scrape date d'hier) : `python3 scraper_aj.py --output /tmp/aj_scan.json`
- Qualifier LLM les 463 annonces pour identifier les deals actionnables : `python3 scraper_aj.py --llm`

**Priorite 2 -- aujourd'hui**
- Enrichir BRANDT FRANCE (score 87, 500-999 sal.) via Pappers -- aucun bilan visible, fort potentiel
- Lancer analyse sur AV.CO. BOIS et USINE DE PANIFICATION (meilleur gabarit du scrape)
- Lancer matching acheteurs sur les 36 deals sans acheteurs.json

**Priorite 3 -- cette semaine**
- Verifier si le pipeline quotidien (Prefect) s'est execute ce matin -- rapport enrichissement absent
- Relancer `python3 orchestration/daily.py` si necessaire
- Reduire l'ecart teaser (100+ deals sans teaser -- bloquer sur les 5 meilleurs scores)

---

## Metriques

| Indicateur | Valeur | Objectif |
|---|---|---|
| Opportunites detectees (scrape J-1) | 463 | > 20 nouvelles/jour |
| Deals en pipeline actif | 85+ dossiers | > 5 actifs |
| Score moyen DB | 37 / 100 | -- |
| Enrichissement financier | non mesure ce matin | > 80% score > 50 |
| Rapport auto-enrichissement | absent | present chaque jour |
| Deal complet | 1 (apels) | -- |

---

*Genere le 2026-03-29 -- source : aj_annonces.json (463 opp.) + PostgreSQL (86 704 procedures actives)*
## Related
## Related
## Related
