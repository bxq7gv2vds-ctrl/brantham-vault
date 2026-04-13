---
type: bug-fix
project: website
date: 2026-03-19
status: resolved
---

# SEO Fix : Pages Procedure + Legales + Sitemap

## Probleme
- Title tags > 60 chars sur 5 pages procedure (Guide 2026, [2026], | Brantham Partners)
- Meta descriptions avec "Par Brantham Partners." au lieu d'un CTA
- H4 au lieu de H3 dans sections accompagnement (liquidation, redressement, reprise-a-la-barre)
- prepack-cession.html : meta author "Paul Roulleau" au lieu de "Brantham Partners", lien equipe.html dans navbar
- 5 pages legales (noindex) avec canonical = signaux contradictoires
- Sitemap : lastmod pas a jour, priorities incorrectes sur 8 pages

## Resolution
12 fichiers edites :

### Pages procedure (5)
- **liquidation-judiciaire.html** : title 54 chars, description avec CTA, 6x H4->H3, og/twitter alignes
- **plan-de-cession.html** : title 55 chars, description avec CTA, og/twitter alignes
- **redressement-judiciaire.html** : title 52 chars, description avec CTA, 5x H4->H3, og/twitter alignes
- **reprise-a-la-barre.html** : title 48 chars, description avec CTA, 6x H4->H3, og/twitter alignes
- **prepack-cession.html** : title 49 chars, description avec CTA, meta author corrige, lien equipe.html supprime navbar+mobile, og/twitter alignes

### Pages legales (5)
- **mentions-legales.html** : canonical supprime (noindex)
- **cgu.html** : canonical supprime (noindex)
- **politique-confidentialite.html** : canonical supprime (noindex)
- **politique-cookies.html** : canonical supprime (noindex)
- **avertissement.html** : canonical supprime (noindex)

### Sitemap (1)
- **sitemap.xml** : tous lastmod -> 2026-03-19, priorities ajustees (4 pages procedure 0.8->0.9, insights 0.7->0.8, 4 articles blog 0.9->0.8)

## Impact
- Titles non tronques dans Google SERP
- Signaux SEO coherents (plus de canonical+noindex contradictoires)
- Hierarchie headings correcte (accessibilite + SEO)
- Sitemap reflete les priorities reelles du site

## Related
- [[_system/MOC-bugs]]
- [[website/_MOC]]
- [[website/bugs/2026-03-19-seo-meta-titles-descriptions-fix]]
- [[website/patterns/seo-subagent-audit-fix]]
