# Session auto-enrichment — 2026-03-28

**Heure**: 10:45 CET
**Budget utilise**: ~$0.47/$0.50

---

## Resultats

### 1. Scrape AJ
- Fichier precedent: 2026-03-28 04:18 (6.5h — depasse seuil 3h)
- Nouveau scrape: 462 opportunites
- 359 expirees supprimees
- 25 sites OK, 6 vides, 0 erreurs

### 2. Opportunites identifiees
- Eligible (CA > 500K, sans dossier existant): 17
- Top 10 selectionnees pour enrichissement

### 3. Dossiers crees (10/10)

| Slug | Societe | CA | SIREN | NAF |
|------|---------|-----|-------|-----|
| ajup-polytechnyl | POLYTECHNYL | >10M | 815232848 | 20.16Z |
| ajup-solarwatt-france | SOLARWATT FRANCE | >10M | 493420434 | 46.52Z |
| ajup-sogran | SOGRAN | >10M | 330714007 | 49.41A |
| ajup-saint-loc | SAINTELOC | >10M | 480532746 | 45.11Z |
| ajup-garage-des-stuarts | GARAGE DES STUARTS | >10M | 493719231 | 45.11Z |
| ajilink-grandest-fonderie-de-niederbronn | FONDERIE DE NIEDERBRONN | >10M | 499026169 | 24.51Z |
| bma-societe-d-application-des-silicones-alimentaires | SASA | >10M | N/A | N/A |
| p2g-groupe-sp-cialis-dans-la-valorisation-des-projets-d-effi | Groupe CEE | >10M | N/A | N/A |
| aj-specialises-aed | AED | 1.22M | 909690927 | 45.20B |
| meynet-sa-ugi-pain | SA UGI-PAIN | 1.02M | 304690910 | 10.71A |

### 4. Enrichissement Pappers
- Enrichis avec SIREN: 8/10
- Sans SIREN (noms trop generiques): 2 (SASA, Groupe CEE)
- Fichiers generes: enrichment.json + analyse.md par dossier

### 5. Matching repreneurs
- FastAPI (localhost:8000): DOWN — endpoint matching indisponible
- API gouvernement (fallback): 429 sur premiers appels, partiel ensuite
- Repreneurs identifies: 2/10 avec resultats (AED: 5, UGI-PAIN: 5)
- Reste: acheteurs.json crees avec 0 ou peu de resultats

### 6. Pipeline mis a jour
- vault/brantham/pipeline/QUEUE.md: update avec 10 nouvelles opportunites

## Erreurs / Points d'attention

- FastAPI down: relancer avec `cd /Users/paul/Desktop/brantham-partners/api && source .venv/bin/activate && uvicorn main:app`
- API gouv rate-limit: espacer les requetes (2s min)
- 2 societes sans SIREN: enrichissement manuel requis

## Related

[[brantham/_MOC]] | [[brantham/pipeline/QUEUE]]
- Deep enrichment termine a 10:50
---

## Cycle 13:29

- **Scrape AJ** : lancement...
  - OK : 463 opportunites scrapees

## Cycle 16:29

- **Scrape AJ** : lancement...
  - OK : 463 opportunites scrapees

## Cycle 16:50

- **Scrape AJ** : lance a 16:50 — 463 opportunites (25 OK, 6 vides, 0 erreurs)
- **Nouvelles opportunites qualifiees** : 0 (tous les deals CA>500K ou score>60 ont deja un dossier)
- **FastAPI** : DOWN (matching repreneurs indisponible)
- **QUEUE.md** : pas de mise a jour necessaire (pipeline inchange)
- **Action** : aucune creation de dossier — todos de session couverts

- Deep enrichment termine a 16:53
---
