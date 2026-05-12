---
title: SEO branthampartners.fr — Pilotage Google Search Console
type: moc
project: brantham
created: 2026-05-12
tags: [seo, gsc, branthampartners]
---

# SEO branthampartners.fr — Pilotage GSC

Objectif unique : faire baisser la **position moyenne** vers 1, le plus vite possible, en s'appuyant sur les données réelles Google Search Console (exports CSV manuels).

## Cadence
- Point tous les **3 jours**.
- À chaque point : nouvel export CSV → analyse → rapport daté dans `reports/` → actions concrètes.
- KPI nord : `avg_position` global + `avg_position` sur le cluster de requêtes "money" (intentions repreneur / cession entreprise en difficulté).

## Exports GSC attendus (à chaque point)

Depuis [Search Console](https://search.google.com/search-console) → propriété `branthampartners.fr` → **Résultats de recherche** → période **3 derniers mois** (pour le contexte) ET **28 derniers jours** (pour le récent). Pour chaque période, exporter les 4 onglets via le bouton **Exporter** (Google Sheets ou CSV) :

1. **Requêtes** (`Queries`) → `exports/YYYY-MM-DD-queries-90d.csv` et `-28d.csv`
2. **Pages** → `exports/YYYY-MM-DD-pages-90d.csv`
3. **Pays** → `exports/YYYY-MM-DD-countries-90d.csv` (vérifier que le trafic est FR)
4. **Dates** → `exports/YYYY-MM-DD-dates-90d.csv` (courbe de tendance)

Colonnes utiles : Query/Page, Clicks, Impressions, CTR, Position.

Bonus utile si dispo :
- Export **Couverture / Pages indexées** (combien d'URLs indexées vs soumises).
- `sitemap.xml` et `robots.txt` de prod (je peux les fetch directement si le site est en ligne).

## Méthode d'analyse (ce que je fais à chaque point)

1. **Striking distance** : requêtes en position 5–20 avec impressions > seuil → plus gros ROI pour gagner des places. On les attaque en priorité (titre, H1, contenu, maillage interne).
2. **Position 1–3 à consolider** : requêtes presque au top → micro-optimisations (CTR : title/meta, FAQ schema, fraicheur).
3. **Cannibalisation** : 2 pages qui rankent sur la même requête → consolider.
4. **Quick wins CTR** : bonne position mais CTR sous la courbe attendue → réécrire title + meta description.
5. **Gaps de contenu** : requêtes à fortes impressions sans page dédiée → nouvelle page.
6. **Technique** : indexation, vitesse, mobile, sitemap, données structurées (Organization, FAQ, Service).
7. **Trend** : la position moyenne baisse-t-elle vraiment vs le point précédent ? Sinon, pourquoi.

## Journal des points
<!-- Ajouter une ligne par rapport : [[reports/YYYY-MM-DD-point]] — avg pos X.X → Y.Y -->
- 2026-05-12 — [[brantham/seo/reports/2026-05-12-point-01|Point #1 baseline]] — position France **13.3** (global ~10.5), 333 clics / 15.8k impr / 90j. Breakout cluster transport. Prochain : 2026-05-15.
- 2026-05-12 — [[brantham/seo/reports/2026-05-12-actions-batch-01|Batch actions #1]] — fix www→non-www (vercel.json), de-orphaning 21 pages (section maillage sur rachat-entreprise-difficulte), suppression page cassée rachat-entreprise-0, nettoyage robots/sitemap. Non déployé.
- 2026-05-12 — [[brantham/seo/reverse-engineering-pourquoi-pas-premier|Reverse engineering]] — pourquoi pas #1 : domaine 2 mois + 0 backlink + pages villes programmatiques + pas de fraîcheur. On-page déjà bon. Plan Tier 1 (codable) / Tier 2 (contenu) / Tier 3 (off-page = goulot).
- 2026-05-12 — Batch actions #2 — bloc fraîcheur "mai 2026" + maillage régional + lastmod/priorité bumpés sur rachat-transport-logistique-redressement.html ; blocs AEO "En bref" + dates rafraîchies sur redressement-judiciaire / liquidation-judiciaire / procedure-collective. Non déployé.
- 2026-05-12 — [[brantham/seo/plan-link-building|Plan link building]] — playbook off-page (citations/annuaires, contenu linkable, newsjacking/RP, partenariats AJ-MJ). À exécuter.
- 2026-05-12 — [[brantham/seo/plan-consolidation-pages-villes|Plan consolidation villes]] — 28 pages villes → 12 régionales + 16 × 301. Mapping défini. À exécuter (gros chantier rédactionnel).
- 2026-05-12 — **Déploiement prod fait** (vercel --prod) : www→non-www 308, redirect rachat-entreprise-0, sitemap à jour, blocs AEO, fraîcheur transport — tout vérifié live. Reste : soumettre sitemap + demander indexation dans GSC.
- 2026-05-12 — [[brantham/seo/off-page-kit|Kit off-page clé en main]] + [[brantham/seo/annuaires-pret-a-coller|annuaires prêt-à-coller]] + [[brantham/seo/journalistes|fichier journalistes]] — tout rédigé (NAP, 13 annuaires/fiches avec données prêtes, baromètre mensuel, modèles téléchargeables, pitchs presse, CP, tribunes, partenariats). Exécution = Paul/Soren (création de comptes + soumissions ; Claude ne peut pas piloter le navigateur ici — extension Chrome non connectée — ni créer de drafts Gmail — scope insuffisant).

## Related
- [[brantham/_MOC]]
- [[_system/MOC-master]]
- [[website/seo-strategy]]
