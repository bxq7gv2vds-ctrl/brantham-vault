---
type: bug-fix
project: website
date: 2026-03-19
status: resolved
---

# SEO Meta Titles, Descriptions et JSON-LD Fix (8 pages)

## Probleme
- Title tags > 60 chars sur 6 pages (Google tronque)
- Meta descriptions > 155 chars ou sans CTA
- og:type "article" sur pages service (devrait etre "website")
- H1 execution-audience.html manquait le mot-cle cible "execution en audience"
- H1 insights.html trop generique (anglais)
- JSON-LD urls sans .html dans glossaire-ma.html et barometre-defaillances.html
- Hierarchie headings barometre : saut H2 > H4 dans section Methodologie
- CSS selector .baro-method-item h4 desynchronise apres fix heading

## Resolution
8 fichiers edites :
- **index.html** : meta description avec CTA
- **sourcing-proprietaire.html** : title raccourci, og:type article->website, descriptions alignees
- **due-diligence-acceleree.html** : title raccourci, og:type article->website, descriptions alignees
- **execution-audience.html** : title raccourci, og:type article->website, H1 avec "execution en audience", descriptions alignees
- **glossaire-ma.html** : title avec "192 Definitions", descriptions raccourcies, JSON-LD urls corrigees (.html ajoute sur ~400 URLs)
- **insights.html** : title raccourci, H1 descriptif en francais, descriptions avec CTA
- **barometre-defaillances.html** : title raccourci, description <155 chars, JSON-LD urls corrigees, H4->H3, CSS selector mis a jour
- **article.html** : title raccourci, descriptions avec CTA

## Impact
Meilleure indexation Google (titles non tronques), coherence JSON-LD, hierarchie headings correcte.
