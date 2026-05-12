---
date: 2026-05-12
project: brantham
type: session
tags: [cockpit, scraping, data-quality, aj]
status: done
---

# Scraping detail pages AJ

Objectif: ameliorer les informations extraites directement depuis les annonces, sans enrichissement externe.

## Sources ameliorees

- `2M&Associés`: lecture des pages detail WordPress. Extraction DLDO, activite, localisation, effectif, CA, contact email dans les notes.
- `CBF Associés`: lecture des pages detail dataroom. Extraction DLDO, secteur, region, contact procedure/email dans les notes.
- `Ascagne`: extraction des deadlines dans les blocs de la page liste (`DEVRONT ETRE DEPOSEES AU PLUS TARD...`). Les anciennes annonces expirees sont maintenant filtrees.
- `Asteren`: lecture des pages detail actif. Extraction type/secteur, localisation complete, contact/email et notes longues.

## Changements transverses

- Notes scraper conservees jusqu'a 2000 caracteres au lieu de 300.
- Parsing des dates courtes `DD/MM/YY`.
- Parsing des formulations deadline type `au plus tard le ...`.
- Import: archivage automatique des anciennes opportunites `nouveau` d'une source qui repond OK/empty mais ne les renvoie plus.

## Dernier run

Run: `scan-20260512-122104`

- 30 sources tentees
- 25 OK
- 5 vides
- 0 erreurs
- 231 opportunites a jour dans le scan
- 134 opportunites actives/non-poubelle apres nettoyage cockpit

Completeness actives:

- DLDO: 91
- CA: 67
- Effectif: 77
- Localisation: 97
- Secteur: 95

## Verification

- Tests extracteurs: 20 passed
- Tests subset pipeline: OK pendant la session precedente

## Related

- [[brantham/_MOC]]
- [[brantham/cockpit/roadmap-2026-05-05]]
- [[brantham/sessions/2026-05-12-cockpit-coverage-monitoring]]
