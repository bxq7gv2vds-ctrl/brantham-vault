---
date: 2026-04-15
type: session
projet: brantham
---

# Session auto-enrichment — 2026-04-15

## Résumé

| Métrique | Valeur |
|---------|--------|
| Opportunités qualifiées (CA >= 500K) | 573 |
| Sans dossier existant | 542 |
| Traitées ce cycle | 10 |
| Dossiers créés | 10 |
| Analyses générées | 10 |
| Matching repreneurs (api.gouv.fr) | 10/10 succès |
| Erreurs | 0 |

## Statut infrastructure

- aj_annonces.json : 2.2h — pas de re-scrape (seuil 3h non atteint)
- FastAPI port 8000 : DOWN — fallback api.gouv.fr utilisé pour repreneurs
- Pappers : tenté sur 7/10, aucun SIREN trouvé (noms anonymisés par AJ)

## Top 10 traitées (score/15)

1. Papier & Électricité (Abitol Rousselet) — 151,3 M€ — 13/15
2. Organisme formation insertion (Maydaymag) — 5-50M€ — 13/15
3. Produits métalliques haute précision (Maydaymag) — 5-50M€ — 13/15
4. Transport routier fret (Maydaymag) — 5-50M€ — 12/15
5-10. Maydaymag divers (chaussures, viti, BTP, solaire, formation, sol) — 10-11/15

## Notes

- Annonces Maydaymag anonymisées : CA par fourchette, pas de SIREN disponible
- Opportunité Papier & Électricité : potentiel doublon avec session 2026-04-09
- Matching repreneurs : résultats api.gouv.fr génériques, à affiner NAF

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]

## Cycle 09:41

- **Scrape AJ** : lancement...
  - OK : 458 opportunites scrapees

## Cycle 12:42

- **Scrape AJ** : lancement...
