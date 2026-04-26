---
date: 2026-04-26
projet: brantham
type: bug-fix
tags: [scraper, ajilink, faux-positifs]
---

# Bug — Ajilink portail générait 25 faux positifs

## Symptôme
Le scraper "Ajilink" (type `js_only`, URL `https://ajilink.fr/offres/`) retournait 25 opportunités dont les noms étaient des villes ("Aix-En-Provence", "Bordeaux", "Créteil"…). DLDO 4% — anormal.

## Cause
La page `ajilink.fr/offres/` n'est PAS un listing d'opportunités : c'est un portail dispatcher qui pointe vers les sous-domaines régionaux du réseau Ajilink (provence.ajilink.fr, sudouest.ajilink.fr, ihdf.ajilink.fr, grand-est.ajilink.fr). Le scraper `scrape_js_only` extrayait les liens vers ces sous-domaines et les traitait comme des opportunités.

## Fix
- `scraper_aj.py:132` — site "ajilink" désactivé (commenté avec note d'explication)
- DB nettoyée : `DELETE FROM opportunities WHERE source_aj = 'Ajilink'` (25 lignes supprimées)

Les vraies offres sont déjà scrapées via Ajilink Provence, Ajilink Sud-Ouest, Ajilink IHDF, AJlink Grand Est.

## Résultat
- 25 faux positifs supprimés
- Total opps : 484 → 459
- Coverage DLDO : 87% → 91.3%

## Leçon
Avant d'ajouter un site au scraper, **valider qu'il liste effectivement des opportunités** et pas un portail de navigation. Vérifier qu'aucun autre site déjà scrapé ne couvre déjà le même contenu (doublon).

## Related
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[brantham/sessions/2026-04-26-cockpit-aj]]
