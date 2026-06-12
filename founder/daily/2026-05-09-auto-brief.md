---
type: daily-brief
date: 2026-05-09
generated: auto
---

# Brief Matinal -- 2026-05-09

## Pipeline

**Deals actifs : 2**

| Deal | Secteur | Statut | Manque |
|------|---------|--------|--------|
| ALPHOSA SAS (Lyon) | ESN Java, RJ | Acheteurs identifies | Outreach non lance |
| MULTI LOISIRS DISTRIBUTION | Vehicules loisirs, Cuinchy (62) | Teaser redige | Acheteurs, contacts, outreach -- date limite 17/03/2026 depassee |

Note : MLD a une date limite depassee (17/03). Verifier si la procedure est encore ouverte avant d'engager des ressources.

**Base de donnees** : 90 589 procedures actives (81 862 en_cours + 8 727 plan_en_cours). Score moyen : 36/100.

---

## Nouvelles Opportunites

714 annonces AJ en base (source : aj_annonces.json). 106 avec date limite >= 2026-05-01. Aucune score_pertinence calcule -- qualification manuelle necessaire.

**Top 3 par urgence/interet visible :**

1. **HOTEL SAINT QUENTIN "KYRIAD"** -- Hotelerie-restauration, 8 ETP (6 ETP). Date limite : 15/06/2026. Secteur porteur, fonds de commerce.

2. **ORPHEUS** -- Boulangerie-patisserie, 15 salaries. Date limite : 15/06/2026. Commerce alimentaire avec clientele etablie.

3. **NECTARGO** -- Secteur non renseigne. Date limite : 22/06/2026. A qualifier en priorite (SIREN non identifie).

---

## Deadlines Proches

Aucune procedure en_cours avec date_jugement_ouverture dans les 7 prochains jours detectee en base.

Attention : date limite AJ pour MLD = 17/03/2026 (depassee). Verifier si annonce toujours active sur bma-aj.com.

Prochaines dates AJ confirmees : 15/06/2026 (HOTEL KYRIAD + ORPHEUS).

---

## Actions Recommandees

**Priorite haute :**

1. **Outreach ALPHOSA** -- Acheteurs Tier 1 identifies (Sapaudia, IT Partner, Apollo SSC). Contacter Dominique Bayon (Sapaudia) en premier : retournement ESN Lyon, profil exact. Email : d.bayon@sapaudia.fr.

2. **Enrichir BRANDT FRANCE** -- Score 84/100, procedure en_cours depuis 01/10/2025. Electromenager (2751Z). Top 1 base. Lancer : `python3 enrich_v2.py --slug brandt-france`.

3. **Qualifier les 106 nouvelles AJ** -- Aucun score_pertinence calcule. Lancer scraper avec LLM : `python3 scraper_aj.py --llm --output /tmp/aj_scan.json`.

**Priorite moyenne :**

4. **Verifier MLD** -- Acceder a https://www.bma-aj.com/anonym/reprise/detail/10028645093. Si procedure encore ouverte : lancer Hunter (vehicules loisirs, Pas-de-Calais). Sinon : clore le deal.

5. **Enrichir top 5 DB** -- API TECH (82), CLINIQUE CHAMPS-ÉLYSEES (82), FTL INTER (81) : aucune donnee financiere confirmee. Lancer enrichissement batch.

---

## Metriques

| Metrique | Valeur |
|----------|--------|
| Procedures actives (DB) | 90 589 |
| Score moyen global | 36 / 100 |
| Score max | 84 (BRANDT FRANCE) |
| Annonces AJ totales | 714 |
| Annonces AJ recentes (>= mai 2026) | 106 |
| Deals en pipeline actif | 2 |
| Deals avec acheteurs identifies | 1 (ALPHOSA) |
| Deals avec outreach lance | 0 |
| Session auto-enrichment du jour | Absente |
| Score_pertinence calcule | 0 / 714 annonces |

**Couverture critique** : 0 % des annonces AJ sont qualifiees. Lancer le scoring LLM est l'action a plus fort levier aujourd'hui.

---

*Genere automatiquement le 2026-05-09 par Claude Code.*
## Related
## Related
## Related
## Related
