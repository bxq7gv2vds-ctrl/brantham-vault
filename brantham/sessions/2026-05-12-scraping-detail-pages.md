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
- `AJ Spécialisés`: remplacement du parser generique par un parser dedie des fiches detail (`Secteur d'activite`, `Chiffre d'affaire`, `Effectif`, `Date limite des offres`, `Locatlisation`).
- `Abitbol & Rousselet`: extraction `1er juin 2026`, DLDO depuis les notes robustes, localisation par departement/code postal entre parentheses.

## Changements transverses

- Notes scraper conservees jusqu'a 2000 caracteres au lieu de 300.
- Parsing des dates courtes `DD/MM/YY`.
- Parsing des formulations deadline type `au plus tard le ...`, `Date limite depot des offres ...`, `DLDO le ...`.
- Backfill localisation rendu plus conservateur: rejet des fragments de montant/effectif/rue et des codes postaux seuls non contextualises.
- Helpers localisation: extraction departement `(38)`, code postal `(13510)`, et `dans le 06`.
- Import: archivage automatique des anciennes opportunites `nouveau` d'une source qui repond OK/empty mais ne les renvoie plus.
- Quality gate `cockpit.scrape_quality`:
  - pre-import sur JSON de scan (`--scan`) pour detecter erreurs/chutes avant auto-archive;
  - post-import DB pour verifier coverage DLDO/secteur/localisation/CA/effectif;
  - branche dans `daily_scrape.sh` en `--warn-only` avant import et apres purge.

## Dernier run

Run final: `scan-20260512-153655`

- 30 sources tentees
- 23 OK
- 7 vides
- 0 erreurs
- 124 opportunites a jour dans le scan
- 124 opportunites actives/non-poubelle apres nettoyage cockpit

Completeness actives:

- DLDO: 121/124
- CA: 65/124
- Effectif: 71/124
- Localisation: 113/124
- Secteur: 116/124

Points notables:

- `AJ Spécialisés`: 6/6 actifs avec DLDO, secteur, localisation, CA, effectif.
- `Abitbol & Rousselet`: 4/4 actifs avec DLDO, secteur, CA, effectif; 3/4 localisation.
- Aucun faux positif localisation detecte (`ETP`, `Mail`, `Salariés Voir`).
- Quality gate pre-import: OK.
- Quality gate DB: OK.

## Verification

- Tests subset pipeline: 82 passed (`scrape_quality`, `hunters_pipeline`, `postparse_notes`, `scraper_extractors`, `cron_outreach_idempotence`).

## Related

- [[brantham/_MOC]]
- [[brantham/cockpit/roadmap-2026-05-05]]
- [[brantham/sessions/2026-05-12-cockpit-coverage-monitoring]]
