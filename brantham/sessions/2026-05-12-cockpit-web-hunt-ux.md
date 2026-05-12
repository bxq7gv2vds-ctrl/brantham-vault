---
date: 2026-05-12
project: brantham
type: session
tags:
  - cockpit-web
  - repreneurs
  - ux
status: done
---

# Cockpit Web Hunt UX

## Summary

Probleme utilisateur: la recherche de repreneurs dans le cockpit web ne fonctionnait pas de facon fiable et l'interface ne donnait pas envie de travailler dessus.

Diagnostic:

- Le bouton web appelait `cockpit.hunt_v2_one`.
- Le chemin v2 retournait `0` candidat sur une opportunite ou le moteur stable `cockpit.hunt_one` retournait `30` candidats.
- Le panneau repreneurs masquait les erreurs de chargement.
- L'input "Recherche" etait seulement un filtre local sur les candidats deja charges.
- Le premier ecran etait un brief/tableau de donnees, pas une file d'actions.

## Changes

- `app/api/hunters/stream/route.ts`
  - branchement du bouton web sur `cockpit.hunt_one`, le moteur stable api.gouv.
  - emission d'evenements NDJSON compatibles UI.
  - fin propre avec `done` ou `error`.
- `app/api/hunters/route.ts`
  - meme moteur stable sur le POST legacy.
  - correction de l'environnement: ne plus ecraser `DATABASE_URL` charge depuis `.env`.
- `components/HuntContext.tsx`
  - fallback si le stream se ferme sans resultat, pour eviter un etat running bloque.
- `components/RepreneursPanel.tsx`
  - affichage des erreurs API.
  - `opp_id` encode.
  - libelle clarifie: filtrage des candidats charges, pas recherche serveur.
  - filtre etendu a nom, SIREN, NAF, email, site, departement.
  - textes v2 remplaces par moteur stable api.gouv.
- `components/TodayView.tsx`
  - remplacement du "Brief du jour" par une file d'actions: opps J-7, relances repreneurs, deals avec action due, todos prioritaires.
  - coverage scrape deplacee plus bas.
- `components/OppsView.tsx`
  - colonnes renommees en vocabulaire metier.
  - barre d'action visible pour la ligne selectionnee: shortlister, ecarter, promouvoir en deal, assigner, ouvrir source.
- `cockpit/hunters/cache.py`
  - correction: ne plus fermer la connexion DB persistante dans `init_cache_schema`.
- `cockpit/db.py`
  - ajout des colonnes repreneurs manquantes au bootstrap SQLite local.

## Validation

- `npm run build` dans `cockpit-web`: OK.
- Tests Python cibles: 27 passes.
- Test reel Supabase:
  - `python3 -m cockpit.hunt_one aj2m-le-fournil-du-port-appel-d-offres`
  - 30 candidats retournes.
  - Top candidats: NAF exact `10.71C`, departement `29`, score `1.0`.
- Serveur dev relance:
  - `http://127.0.0.1:3000`

## Remaining

Le cockpit web est plus utilisable, mais l'UX n'est pas encore au niveau final.

Prochains chantiers:

1. Creer une vraie page/vue Repreneurs au lieu de tout cacher dans les drawers.
2. Brancher l'enrichissement Pappers/Hunter.io apres le moteur stable.
3. Ajouter un indicateur de confiance par candidat.
4. Refondre le drawer opportunite avec une synthese decisionnelle sticky.

## Related

- [[brantham/_MOC]]
- [[brantham/cockpit/roadmap-2026-05-05]]
- [[brantham/sessions/2026-05-12-repreneurs-hunters-accuracy]]
