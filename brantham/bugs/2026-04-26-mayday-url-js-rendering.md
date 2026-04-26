---
date: 2026-04-26
projet: brantham
type: bug-fix
tags: [scraper, mayday, lightpanda]
---

# Bug — Maydaymag scraper retournait 0 opps

## Symptôme
`scraper_aj.py` retournait systématiquement 0 opp pour Maydaymag. Le scraper marquait "site vide" mais des opps existaient bel et bien.

## Cause
Deux problèmes cumulés :
1. **Mauvaise URL** : scraper attaquait la racine `https://www.maydaymag.fr/` qui est la homepage. Les annonces sont sur `/les-entreprises-a-reprendre/`.
2. **JS rendering manquant** : la page est une SPA hydratée en JS. `requests` voit du HTML vide, BeautifulSoup ne trouve aucun `<article>`. Il faut un browser headless qui exécute le JS.

## Fix
- `scraper_aj.py:138` — URL changée vers `/les-entreprises-a-reprendre/`
- `scraper_aj.py:697` — `scrape_maydaymag` réécrit pour utiliser `lp.fetch_html` (LightPanda) au lieu de `requests`. Parser via `<h2>` (pas `<article>`, le site n'en a pas) avec filtres de sentinelles ("MAYDAY", "Newsletter", "#Veille"...).

## Résultat
+11 opps réelles récupérées (Hôtellerie/restauration, boulangerie, conseil, prêt-à-porter, équipements FIA auto, filtration eau, clinique, etc.).

## Leçon
Pour un site qui retourne 0 opp, toujours vérifier en parallèle :
1. La page existe-t-elle (curl + check status) ?
2. Le contenu attendu est-il dans le HTML brut (curl) ou nécessite-t-il JS (LightPanda/Obscura) ?
3. Le scraper attaque-t-il la bonne URL ?

Le scraper actuel ne distinguait pas "vide intentionnel" vs "parser cassé" → ajout du **silent breakage detection** dans `diff_scan.py` pour catch ce cas en CI.

## Related
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[brantham/sessions/2026-04-26-cockpit-aj]]
- [[brantham/patterns/dldo-extraction-regex-fr]]
