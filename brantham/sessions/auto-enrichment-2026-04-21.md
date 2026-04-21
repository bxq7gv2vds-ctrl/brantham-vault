---
date: 2026-04-21
type: session
projet: brantham
---

# Session auto-enrichment — 2026-04-21

## Résumé

| Métrique | Valeur |
|----------|--------|
| Heure | 14h07 CEST |
| Opportunités traitées | 10 |
| Enrichies Pappers | 10 (100%) |
| Erreurs | 0 |
| Repreneurs trouvés via API | 0 (API gouv sans résultats) |

## Scraper AJ

- Fichier aj_annonces.json avait 7h (seuil : 3h) — relancé
- Résultat : 0 opportunités (26 erreurs réseau, DNS failures)
- Données issues de PostgreSQL (89K+ procédures)

## Deals créés

1. `brandt-france` — BRANDT FRANCE — score 84 — CA 291M€
2. `idkids` — IDKIDS — score 82 — CA 724M€
3. `star-s-service` — STAR'S SERVICE — score 82 — CA 119M€
4. `api-tech` — API TECH — score 82 — CA 67M€
5. `clinique-du-rond-point-des-champs-elysees` — score 82 — CA 10.5M€
6. `ftl-inter` — FTL INTER — score 81 — CA 141M€
7. `ste-d-application-des-silicones-alimentaires` — score 81 — CA 43M€
8. `colisee-group` — COLISEE GROUP — score 80 — CA 1.58Md€
9. `transports-bonnard` — score 80 — CA 24M€
10. `essor-ingenierie` — score 80 — CA 23M€

## Fichiers créés par deal

Chaque dossier contient : `enrichment.json` (Pappers) + `analyse.md` + `acheteurs.json`

## Points d'attention

- API repreneurs (gouv.fr) : 0 résultats — paramètres nature_juridique/tranche_effectif trop restrictifs
- Pappers : 18 champs par lookup, token gratuit (100 req/jour consommé partiellement)
- Scraper AJ : sites inaccessibles — vérifier DNS / réseau

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]

## Cycle 21:03

- **Scrape AJ** : lancement...
  - OK : 468 opportunites scrapees
