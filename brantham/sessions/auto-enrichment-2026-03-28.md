# Session Auto-Enrichment — 2026-03-28

**Date** : 2026-03-28 22:53 CET  
**Type** : Pipeline automatique — scrape + enrichissement + matching  

---

## Resultats

| Metrique | Valeur |
|----------|--------|
| Fichier aj_annonces.json | 463 opportunites (scraper relance en background) |
| Opportunites eligibles identifiees | 73 (CA > 3M€, sans dossier existant) |
| Top 10 selectionnes | 10 |
| Dossiers crees | 10 |
| Enrichissement Pappers reussi | 5/10 |
| Enrichissement Pappers echec (nom anonyme) | 5/10 |
| Repreneurs identifies | 3 deals (rate limit API govt 429) |

## Deals traites

1. **ajup-transports-ballet** — TRANSPORTS BALLET | SIREN 442534640 | Transport routier 70 | 5 repreneurs
2. **ajup-adiamas** — ADIAMAS | SIREN 305823403 | Fabrication acier inox 63
3. **ajup-gba-enseigne-3-bois** — GBA ENSEIGNE 3 BOIS | Granulés bois 03 | Pappers non trouve
4. **ajup-aciers-coste** — ACIERS COSTE | SIREN 745880369 | Laminage acier 63 | Deadline: 18/03/2026
5. **ajup-ppa** — PPA | SIREN 491115499 | Imprimerie 93 | Deadline: 30/03/2026 | 1 repreneur
6. **ajup-mgl-enseigne-lolly-s** — MGL Lolly's | Distribution confiserie Paris | Pappers non trouve
7. **ajup-tubindus** — TUBINDUS | SIREN 909130379 | Tubes industriels 39 | Deadline: 20/04/2026
8. **p2g-organisme-de-formations-aux-m-tiers-du-num-rique** — Formation numérique Paris | 5 repreneurs
9. **trajectoire-parfumerie-sous-traitance-industrielle** — Parfumerie ST | Loiret 45
10. **trajectoire-2025-05-2562pc** — Stockage industriel | Indre-et-Loire 37

## Alertes

- ACIERS COSTE (ajup-aciers-coste) : deadline 18/03/2026 DÉPASSÉE — verifier statut
- PPA (ajup-ppa) : deadline 30/03/2026 dans 2 jours — URGENT
- API gouvernement rate-limited (429) pour 7/10 deals — repreneurs incomplets

## Actions suivantes

- Acceder dataroom PPA avant 30/03/2026
- Relancer matching repreneurs (espacer les requetes)
- Enrichir les 5 deals sans SIREN via recherche manuelle

## Related

- [[brantham/_MOC]]
- [[brantham/pipeline/QUEUE]]
- Deep enrichment termine a 22:57
---
