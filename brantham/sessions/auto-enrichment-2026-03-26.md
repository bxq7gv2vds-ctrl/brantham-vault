# Session auto-enrichment — 2026-03-26

## Resultats

| Metrique | Valeur |
|----------|--------|
| Scrape AJ (40 sites) | OK — 468 opportunites |
| Opportunites expireees supprimees | 355 |
| Opportunites qualifiees (CA>500K) | 50 |
| Nouvelles sans dossier | 10 |
| Dossiers crees | 10 |
| Enrichis Pappers | 5/10 |
| SIREN identifies | 5 (348398918, 462200403, 845074020, 514498039, 930134390) |
| Repreneurs identifies | 24 sur 8 deals |
| Erreurs | 0 |

## Deals traites

1. Commerce textile (Ascagne) — 19.4M — 1 repreneur
2. SOHNEJ (AJRS) — 1.5M — 5 repreneurs — DL 17/04/2026
3. Transport commissionnaire (Abitbol) — 1.5M — SIREN:348398918
4. Equipements thermiques (Abitbol) — 1.4M — SIREN:462200403 — 4 repreneurs
5. Agence pub sport (Ascagne) — 1.2M — Paris 75016
6. LA BIO N'AVENTURE (Meynet) — 1.0M — SIREN:845074020 — Saint-Ismier
7. ARRIS tabac (Ajilink Provence) — 1.0M — SIREN:514498039 — BdR
8. Medico-chirurgical (Ajilink Provence) — 1.0M — 5 repreneurs — DL 16/04/2026
9. ROYALHAIR (Ajilink IHDF) — 1.0M — 5 repreneurs — Yvelines
10. LAMIAN LATIAN (Ajilink IHDF) — 1.0M — SIREN:930134390 — Paris — 4 repreneurs

## Actions suivantes recommandees

- PRIORITE : Commerce textile 19.4M — dossier le plus important, contacter Ascagne
- DEADLINE proche : medico-chirurgical DL 16/04/2026
- DEADLINE proche : SOHNEJ DL 17/04/2026
- Enrichir SIREN manquants (SOHNEJ, textile Ascagne, pub sport)
- API FastAPI down — relancer pour matching 4D complet

## Infrastructure

- FastAPI (port 8000) : DOWN — relance necessaire
- Scraper AJ : OK
- Pappers : OK (rate limit: ~95 req restantes)
- Deep enrichment termine a 19:42
---

## Cycle 23:10

- **Scrape AJ** : lancement...
  - OK : 468 opportunites scrapees

## Related
- [[brantham/_MOC]]
