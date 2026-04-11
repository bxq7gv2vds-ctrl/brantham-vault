# Session auto-enrichment — 2026-04-11

**Type** : Cycle enrichissement 3h  
**Execution** : 2026-04-11 09:46 CEST

---

## Resultats

| Metrique | Valeur |
|---------|--------|
| Fichier AJ (age) | 0.7h (frais, pas de rescrape) |
| Total opportunites JSON | 1393 |
| Nouvelles eligibles (CA >= 500K) | 408 |
| Opportunites traitees | 10 |
| Dossiers crees (deals/) | 10 |
| Enrichissement Pappers | 10 (retour vide — noms generiques) |
| Repreneurs identifies (API gouv) | 50 (5 par deal) |
| Erreurs | 0 |

## Deals traites

- `saj-recherche-repreneurs-le-marche-des-saisons-a-pornic` — RECHERCHE REPRENEURS - LE MARCHÉ DES SAISONS A PORNIC (989 246€ au 31/10/2024Résultat, PORNIC (44)Personnel : 5 salariésChiffre)
- `saj-recherche-repreneurs-restaurant-a-la-baule-44` — RECHERCHE REPRENEURS - RESTAURANT A LA BAULE (44) (864 949€ au 31/12/2024Résultat, LA BAULE (44)Personnel : 4 salariésChiff)
- `meynet-commerce-de-detail-12888` — Commerce de détail #12888 (6.870.276,00 €, Date limite de dépôt des offres :)
- `meynet-m-g-b-a` — M.G.B.A. (2.555.000,00 €, 38890 Salagnon)
- `aj-specialises-recherche-de-repreneurs-dans-le-cadre-d-un-rj-transport-routier` — Recherche de repreneurs dans le cadre d’un RJ - Transport routier (2 193 000.00, )
- `aj-specialises-viand-oc` — VIAND OC (1 996 851.00, )
- `meynet-industrie-14207` — Industrie #14207 (1 213 808,69, 74300 CLUSES)
- `meynet-sp-lyon-7` — SP LYON 7 (872 322,96 €, 69007 LYON)
- `ajilink-cap-alliance` — CAP ALLIANCE (805 835.82 €, SISTERON Type de cession envisagée : Maj)
- `meynet-sp-vileurbanne` — SP VILEURBANNE (567.480,45 €, 69100 VILLEURBANNE)

## Notes

- API localhost:8000 down (FastAPI non demarre) — matching 4D non disponible, remplacement par API gouv.fr
- Pappers lookup par nom retourne vides (noms trop generiques type "RECHERCHE REPRENEURS")
- 408 nouvelles opportunites CA >= 500K en attente d'enrichissement complet
- Rescrape non necessaire (fichier frais)

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
- Deep enrichment termine a 09:50
---

## Cycle 10:51

- **Scrape AJ** : lancement...
  - OK : 463 opportunites scrapees
