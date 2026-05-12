---
date: 2026-05-12
project: brantham
type: session
tags:
  - cockpit
  - hunters
  - repreneurs
  - data-quality
status: done
---

# Repreneurs Hunters Accuracy

## Summary

Objectif: rendre le hunt repreneurs du cockpit nettement plus fiable en partant du chemin reel utilise par le TUI.

Constat cle: le TUI appelle encore `cockpit/hunters/` v1 via `cockpit.hunt_one`, pas `hunters_v2`. Le chantier a donc renforce le chemin actif au lieu de seulement ameliorer le pipeline v2 non cable.

## Changes

- Ajout d'un module partage `cockpit/opportunity_intel.py` pour inferer de facon conservatrice:
  - code NAF;
  - departement;
  - region via mapping existant.
- Ajout de `cockpit/backfill_opportunity_intel.py` pour backfiller les opportunites actives.
- Integration du backfill dans `daily_scrape.sh` apres `postparse_notes`.
- Hunters v1:
  - utilise maintenant le module partage pour NAF/departement;
  - active une recherche sur NAF voisins quand les resultats directs sont insuffisants;
  - persiste les repreneurs en UPSERT au lieu d'ignorer silencieusement les conflits.
- Hunters v2:
  - reutilise le meme module d'inference NAF pour eviter les divergences.
- Correction `cockpit/hunters/api_gouv.py`:
  - le nom entreprise etait parfois ecrase par le nom dirigeant pendant la normalisation;
  - tous les repreneurs persistants ont maintenant un nom.

## Validation

Mesure Supabase apres backfill:

- Opportunites actives: 124
- NAF renseigne: 104 / 124
- Departement renseigne: 79 / 124
- Region renseignee: 79 / 124
- Repreneurs persistants: 550
- Repreneurs avec nom: 550 / 550
- Repreneurs avec score: 550 / 550

Test reel:

- `python3 -m cockpit.hunt_one aj2m-le-fournil-du-port-appel-d-offres`
- 30 candidats repreneurs trouves et persistants.
- Top resultats coherents: boulangeries/patisseries, NAF exact `10.71C`, meme departement ou region.

Tests automatises:

- 96 tests passes.
- Ajout de tests pour:
  - inference NAF conservative;
  - pollution des notes scraper;
  - departement depuis localisation;
  - preservation du nom entreprise api.gouv.

## Remaining Risks

Ce n'est pas encore du 100%:

- Le cockpit ne stocke pas encore le SIREN de l'opportunite cible dans `opportunities`, donc le matching part encore d'une inference NAF/localisation.
- Le v1 ne fait pas encore l'enrichissement Pappers/Hunter.io complet: CA, dirigeants, emails et signaux restent limites.
- Le v2 plus riche n'est pas encore branche dans le TUI/web comme chemin principal.
- Les opportunites sans secteur/localisation explicite restent volontairement non inferees pour eviter les faux positifs.

## Next

1. Ajouter `siren` officiel sur `opportunities` et le remplir via extraction detail + API Entreprise/Pappers.
2. Brancher `hunters_v2` comme moteur principal du cockpit avec fallback v1.
3. Enrichir les top repreneurs avec Pappers/Hunter.io, puis afficher le niveau de confiance dans le cockpit.
4. Ajouter une quality gate repreneurs: chaque hunt doit avoir nom, SIREN, score, justification, source et timestamp.

## Related

- [[brantham/_MOC]]
- [[brantham/cockpit/roadmap-2026-05-05]]
- [[brantham/sessions/2026-05-12-scraping-detail-pages]]
