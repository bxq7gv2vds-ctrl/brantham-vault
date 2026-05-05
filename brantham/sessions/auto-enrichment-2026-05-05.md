# Auto-enrichment — 2026-05-05

**Heure** : 16:32  
**Type** : Cycle 3h — Scrape + Enrich + Deals

---

## Résultats

| Métrique | Valeur |
|---------|--------|
| Opportunités dans aj_annonces.json | 452 |
| Opportunités scraper AJ (après refresh) | 452 |
| Candidats CA>500K ou score>60 sans dossier | 8 |
| Dossiers deals/ créés | 8 |
| Enrichissements Pappers réussis | 7/8 (KYRIAD sans SIREN) |
| Analyses.md générées | 8/8 |
| Repreneurs identifiés (API Entreprises) | 5 pour KYRIAD |
| Erreurs | 0 |

## Opportunités traitées

| Slug | Nom | CA | SIREN | Statut |
|------|-----|----|-------|--------|
| ajire-auroit | AUROIT | 3-10M | 401278379 | enrichi + analysé |
| ajilink-ihdf-ikomobi | IKOMOBI | 1-3M | 514418748 | enrichi + analysé |
| ajilink-provence-desiree | DESIREE | <1M | 428774822 | enrichi + analysé |
| ajilink-provence-noemys-arles | NOEMYS ARLES | <1M (CA 477K) | 948310461 | enrichi + analysé |
| ajilink-provence-noemys-neris | NOEMYS NERIS | <1M (CA 620K) | 523274777 | enrichi + analysé |
| ajilink-provence-le-grill-saint-andre | LE GRILL SAINT ANDRE | <1M | 978861243 | enrichi + analysé |
| ajilink-ihdf-nectargo | NECTARGO | <1M | 902686997 | enrichi + analysé |
| ajup-hotel-saint-quentin-kyriad | HOTEL KYRIAD | <1M | N/A | analysé (pas SIREN) |

## Notes

- Scraper AJ : 452 opportunités à jour (355 expirées supprimées)
- Score pertinence = 0 pour toutes (pas de run LLM — mode rapide)
- Matching repreneurs via API Entreprises publique (localhost:8000 non testé)
- Pappers rate limit : 8 lookups consommés

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
