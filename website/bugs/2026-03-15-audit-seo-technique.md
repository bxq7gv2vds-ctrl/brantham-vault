---
date: 2026-03-15
project: website
type: bug-audit
---

# Audit SEO Technique Brantham Partners — Issues Identifiées

## Critiques
- `og-barometre.png` référencé dans barometre-defaillances.html mais absent du répertoire
- 2 liens cassés dans `index.html`: `/multiples-ebitda-secteur-france-2026` et `/reprendre-entreprise-liquidation-judiciaire` (pages non créées)
- 1 lien relatif sans slash dans `index.html`: `href="article.html"` (doit être `/article.html`)
- 1 doublon de lien dans `index.html`: `/insights` ET `/insights.html` pointant vers la même page

## Importantes
- 10 pages indexables avec title > 60 chars
- 5 pages indexables avec description > 160 chars
- `twitter:site` absent sur 10 pages indexables (présent seulement sur 4)
- `skip-link` absent sur `redressement-judiciaire.html` (indexable)
- Pages de services (sourcing, due-diligence, execution, valorisation): pas de `twitter:site`
- `article.html` sans FAQPage schema
- 13 pages avec og:image générique (`og-image.png`) — seulement barometre a une image dédiée

## Mineures
- Canonical sans `.html` sur pages légales noindex (cohérence discutable mais pages noindex)
- Navbar simplifiée sur pages légales (comportement intentionnel possible)
- `avertissement.html` canonical sans `.html` (mais noindex)
- `glossaire-ma.html` sans FAQPage schema (a DefinedTermSet mais pas FAQPage)
- `insights.html` sans aucun schema de contenu spécifique à l'article

## Statut Sitemap
- 14 pages indexables dans sitemap: OK
- Pages légales (noindex) absentes du sitemap: CORRECT
- `sections-proposals.html`, `equipe.html`, `avertissement.html`: noindex, absentes: CORRECT
