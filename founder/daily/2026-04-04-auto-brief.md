---
type: daily-brief
date: 2026-04-04
generated: auto
---

# Brief Matinal -- 2026-04-04

## Pipeline

**169 dossiers actifs** dans `/deals/` — 0 teaser genere (blocage systematique Writer).

| Statut | Nb deals |
|--------|----------|
| Analyse OK, pas de teaser | ~140 |
| Analyse + acheteurs identifies | ~110 |
| Complet (analyse + teaser + acheteurs) | 0 |
| Sans analyse | ~29 |
| Sans rien (priorite basse) | 4 |

Valeur estimee du pipeline AJ : 458 opportunites scrapees, dont 321 qualifiees (CA > 500k ou score > 60).

## Nouvelles Opportunites

**458 opportunites** dans `aj_annonces.json` (scrape du 04-04, 31/40 sites).

Top 3 prioritaires issus de la session d'enrichissement 04h34 :

**1. CYFAC & MERAL Cycles** (`trajectoire-cyfac-meral`)
- Fabrication artisanale de cycles haut-de-gamme
- Dossier : analyse + acheteurs OK — SIREN a verifier manuellement
- Action : teaser a generer

**2. H&A LOCATION** (`ajilink-sudouest-sas-h-a-location`)
- Location de barriques viticoles — Gironde
- Deadline : 24 avril 2026 (20 jours)
- Dossier : analyse + acheteurs OK
- Action : teaser urgent + contact AJ

**3. Entreprise sante DOM/TOM** (`aj-specialises-2133`)
- CA 5.76M€ — 37 salaries — anonyme
- Dossier : analyse + acheteurs OK
- Action : teaser a generer

## Deadlines Proches

Aucune deadline < 7 jours identifiee dans la base BODACC (date_jugement_ouverture).

Deadline notable a surveiller :
- **H&A LOCATION** — 24 avril 2026 (J-20) — seul deal avec date explicite dans le scrape AJ

Procedures ouvertes recemment (score >= 70, toutes en RJ) :
- IDKIDS (score 82) — 03/02/2026 — groupe pret-a-porter enfant
- KLUBB FRANCE (score 78) — 03/02/2026 — materiels elevateur
- ID LOG (score 76) — 03/02/2026 — logistique groupe IDKIDS
- POMME DE PAIN (score 71) — 04/02/2026 — restauration boulangerie
- FRANCE GOURMET PRESTIGE (score 70) — 11/02/2026 — agroalimentaire premium

## Actions Recommandees

| Priorite | Action | Impact |
|----------|--------|--------|
| P0 | Relancer FastAPI port 8000 (hors service a 04h34) | Bloque matching 4D + endpoints deals |
| P1 | Lancer Writer sur top 10 deals (tous ont analyse) | Pipeline completement bloque sur teaser = 0 |
| P1 | H&A LOCATION : generer teaser + preparer email AJ | Deadline J-20 — deal avec acheteurs identifies |
| P2 | Scraper les 9 sites manquants (31/40 ce matin) | Couverture marche a 78% |
| P2 | Trouver SIREN CYFAC & MERAL + H&A LOCATION | Enrichissement Pappers bloque sans SIREN |
| P3 | IDKIDS (score 82, J-60 ouverture) : analyse + teaser | Deal a fort potentiel, groupe multimarques |
| P3 | BRANDT FRANCE (score 84, max DB) : verifier si dans pipeline | Meilleur score actuel — jamais traite |

## Metriques

| Metrique | Valeur | Objectif |
|----------|--------|----------|
| Opportunites detectees (scrape du jour) | 458 | > 20/jour |
| Sites AJ couverts | 31 / 40 (78%) | 40 |
| Deals en pipeline actif | 169 | > 5 |
| Teasers generes | 0 / 169 | 100% |
| Taux enrichissement (deals du jour) | 50% (5/10) | > 80% |
| Score moyen DB | 37 / 100 | -- |
| Score max DB | 84 (BRANDT FRANCE) | -- |
| Procedures actives (en_cours + plan) | 87 324 | -- |
| Procedures scorees | 89 630 | -- |
| FastAPI | Hors service | UP |

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
[[brantham/sessions/auto-enrichment-2026-04-04]]
