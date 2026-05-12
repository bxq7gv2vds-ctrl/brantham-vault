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
- `Ajilink/Gemweb`: extraction de la derniere deadline, du departement et du secteur depuis les tables, en evitant les faux positifs type nom d'entreprise commencant par un numero.
- `AJRS`: extraction adresse + secteur depuis la structure de bloc detaillee.
- `BCM`: extraction `DLDO le ...` et departement quand presents dans le titre.
- `Maydaymag`: exclusion des articles de veille, conservation du titre et du texte detail dans les notes pour permettre le backfill.
- `ADJE`/`AJA`: suppression des faux positifs formulaire/chargement/categories.

## Changements transverses

- Notes scraper conservees jusqu'a 2000 caracteres au lieu de 300.
- Parsing des dates courtes `DD/MM/YY`.
- Parsing des formulations deadline type `au plus tard le ...`, `Date limite depot des offres ...`, `DLDO le ...`.
- Backfill localisation rendu plus conservateur: rejet des fragments de montant/effectif/rue et des codes postaux seuls non contextualises.
- Import: archivage automatique des anciennes opportunites `nouveau` d'une source qui repond OK/empty mais ne les renvoie plus.

## Dernier run

Run final: `scan-20260512-133538`

- 30 sources tentees
- 23 OK
- 7 vides
- 0 erreurs
- 148 opportunites a jour dans le scan
- 124 opportunites actives/non-poubelle apres nettoyage cockpit

Completeness actives:

- DLDO: 114/124
- CA: 61/124
- Effectif: 71/124
- Localisation: 103/124
- Secteur: 114/124

## Verification

- Tests subset pipeline: 70 passed (`hunters_pipeline`, `postparse_notes`, `scraper_extractors`, `cron_outreach_idempotence`).

## Related

- [[brantham/_MOC]]
- [[brantham/cockpit/roadmap-2026-05-05]]
- [[brantham/sessions/2026-05-12-cockpit-coverage-monitoring]]
