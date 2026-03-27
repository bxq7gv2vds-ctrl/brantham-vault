---
title: "Audit SEO & GEO Complet — branthampartners.fr"
date: 2026-03-21
type: audit
project: website
author: Claude (audit automatise)
---

# Audit SEO & GEO Complet — branthampartners.fr

**Date**: 2026-03-21
**Site**: https://branthampartners.fr
**Source code**: `/Users/paul/zura-inspired/`
**Framework GEO**: geo-seo-claude (scoring composite 0-100, 6 categories ponderees)

---

## Resume Executif

**GEO Score estime: 42/100** — Le site a des fondations SEO techniques solides mais est quasi-invisible pour les moteurs IA (ChatGPT, Perplexity, Google AI Overview, Gemini, Bing Copilot).

**Architecture**: Site statique HTML genere par Python/Jinja2, deploye sur Vercel. 68 pages (17 geo + 15 secteurs + 36 pages manuelles). PAS un site Next.js.

| Categorie | Poids | Score | Pondere |
|-----------|-------|-------|---------|
| AI Citability & Visibility | 25% | 45/100 | 11.25 |
| Brand Authority Signals | 20% | 15/100 | 3.00 |
| Content Quality & E-E-A-T | 20% | 55/100 | 11.00 |
| Technical Foundations | 15% | 82/100 | 12.30 |
| Structured Data | 10% | 50/100 | 5.00 |
| Platform Optimization | 10% | 25/100 | 2.50 |
| **TOTAL GEO** | **100%** | | **45/100** |

**Verdict**: Fondations techniques excellentes, contenu riche, mais l'absence totale de signaux d'entite (Organization schema, sameAs, Wikipedia, YouTube, LinkedIn) rend le site invisible aux moteurs IA. Les corrections critiques peuvent faire passer le score a 70+ en 2-3 semaines.

---

## I. SEO Technique

### A. Meta Tags — Score: 95/100

**Excellent**. Coverage 100% sur les 68 pages.

| Element | Status | Detail |
|---------|--------|--------|
| `<title>` | OK | Unique par page, 50-60 chars |
| `<meta description>` | OK | 150-220 chars, keyword-rich |
| `<meta keywords>` | OK | 8-10 keywords par page |
| `<meta author>` | OK | "Paul Roulleau" |
| `<meta robots>` | OK | `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1` |
| `<html lang="fr">` | OK | Correct |
| `<meta http-equiv="content-language">` | OK | `fr` |
| `<meta name="geo.region">` | OK | `FR` + `geo.placename` variable par ville |

**Probleme mineur**: `geo.position` (lat/long) absent sur les pages geo — ameliorerait le ciblage local.

### B. Open Graph & Twitter Cards — Score: 90/100

Coverage 100%. OG types differencies (`website`, `article`, `dataset`). Twitter `summary_large_image`.

**Probleme**: Une seule image OG (`og-image.png`) pour les 68 pages. Les pages geo et secteur devraient avoir des images distinctes pour un meilleur CTR social.

### C. Canonical URLs — Score: 100/100

Parfait. URLs absolues, self-referential, pas d'incoherence trailing slash.

### D. Hreflang — Score: 90/100

`fr-FR` + `x-default` sur toutes les pages. Correct pour un site monolingue. Pas de version EN prevue pour l'instant.

### E. Sitemap & Robots — Score: 90/100

**robots.txt** (bien configure):
```
User-agent: *          → Allow: /
User-agent: GPTBot     → Allow: /
User-agent: ClaudeBot  → Allow: /
User-agent: PerplexityBot → Allow: /
User-agent: Google-Extended → Allow: /
Disallow: /swarm/
Sitemap: https://branthampartners.fr/sitemap.xml
```

**sitemap.xml**: 67 URLs avec `lastmod`, `changefreq`, `priority`. Coverage OK (1 page test exclue volontairement).

**Manquant**:
- Pas de `User-agent: OAI-SearchBot` (ChatGPT search specifique)
- Pas de `User-agent: ChatGPT-User` (mode browsing)
- Pas de `User-agent: Amazonbot`
- Pas de `User-agent: Bytespider`
- Pas de `User-agent: Applebot-Extended`
- Pas de `User-agent: Cohere-ai`

→ **Recommandation**: Ajouter les 14 AI crawlers identifies par le framework GEO explicitement en `Allow`.

### F. Performance & Securite — Score: 92/100

**Security headers (vercel.json)**: Excellent.
- HSTS 2 ans + preload + subdomains
- X-Content-Type-Options: nosniff
- X-Frame-Options: SAMEORIGIN
- Referrer-Policy: strict-origin-when-cross-origin
- Permissions-Policy: camera=(), microphone=(), geolocation=()

**Caching**: Optimal (1 an immutable pour assets, must-revalidate pour HTML).

**Font loading**: Exemplaire (preconnect + preload + swap + noscript fallback). Fonts: Instrument Serif, DM Sans, DM Mono.

**Problemes mineurs**:
- Pas de `Content-Security-Policy` header (CSP)
- Pas de critical CSS inline
- Pas de `dns-prefetch` pour domaines externes

### G. Images — Score: 40/100

**Faible**. Peu d'images mais mal optimisees:
- Pas de `srcset` / responsive images
- Pas de `loading="lazy"`
- Pas de format WebP
- OG image unique (19.3K PNG, taille OK 1200x630)
- Logo SVG (bon choix)

---

## II. SEO On-Page

### A. Structure des Titres — Score: 90/100

- 1 seul `<h1>` par page
- Hierarchie logique H1 > H2 > H3
- IDs semantiques sur les H2 (navigation in-page)
- Page pillar (rachat-entreprise-difficulte.html): 7 H2, 30+ H3, ~8000-12000 mots

### B. Internal Linking — Score: 95/100

**Excellent**. Strategie en pillar/cluster bien executee:

| Page | Liens entrants |
|------|---------------|
| rachat-entreprise-difficulte.html | 292 |
| insights.html | 202 |
| due-diligence-acceleree.html | 185 |
| sourcing-proprietaire.html | 171 |
| plan-de-cession.html | 152 |
| execution-audience.html | 141 |
| valorisation-entreprise-difficulte.html | 137 |
| glossaire-ma.html | 116 |

Liens relatifs dans le HTML, absolus dans les schemas. Refs externes vers Legifrance (autorite).

### C. Contenu — Score: 85/100

**Points forts**:
- Pillar pages: 8,000-12,000 mots (au-dessus du seuil de 2,000 pour guides)
- Glossaire: 192 termes definis (DefinedTermSet schema)
- Barometre: donnees quantitatives avec schema Dataset
- References legales (articles du Code de commerce)
- FAQ structurees (4-5 Q&A par page avec schema FAQPage)

**Points faibles**:
- Contenu programmatique (geo + secteur) potentiellement thin/duplicatif
- Pas de date de derniere mise a jour visible dans le HTML (seulement en schema)
- Pas de byline auteur visible sur les pages
- Pas de section "Sources" ou bibliographie explicite

### D. Keyword Strategy — Score: 80/100

Bonne couverture du champ semantique "distressed M&A France":
- Termes primaires: rachat entreprise en difficulte, reprise a la barre, plan de cession
- Termes secondaires: procedure collective, liquidation judiciaire, redressement judiciaire
- Long-tail geo: rachat entreprise [ville]
- Long-tail secteur: rachat [secteur] liquidation

**Manquant**: Pas de contenu "how-to" / "guide pour debutants" qui cible les queries informationnelles des LLMs.

---

## III. Structured Data — Score: 50/100

### Ce qui existe (bien fait)

| Schema | Pages | Quality |
|--------|-------|---------|
| Article | 30+ guides | Bon — headline, datePublished, author, publisher, image |
| BreadcrumbList | 68 pages | Bon — 2-3 niveaux, URLs absolues |
| FAQPage | 35+ pages | Bon — 4-5 Q&A par page |
| DefinedTermSet | Glossaire | Excellent — 192 termes avec descriptions |
| Dataset | Barometre | Bon — temporalCoverage, spatialCoverage |
| SiteNavigationElement | Homepage | OK — 8 items |

### Ce qui manque (CRITIQUE pour GEO)

| Schema manquant | Impact GEO | Priorite |
|----------------|------------|----------|
| **Organization** (avec sameAs) | CRITIQUE — sans ca, les AI ne reconnaissent pas l'entite "Brantham Partners" | P0 |
| **Person** (auteur avec sameAs, jobTitle, knowsAbout) | HAUT — signaux E-E-A-T pour credibilite | P0 |
| **WebSite + SearchAction** | MOYEN — signal de structure pour sitelinks | P1 |
| **speakable** property sur Articles | MOYEN — marque explicitement les sections pour AI assistants | P1 |
| **LocalBusiness** | MOYEN — si Brantham a une adresse physique | P2 |
| **Service** | BAS — pour les pages services | P2 |

### Organization Schema a implementer (URGENT)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Brantham Partners",
  "url": "https://branthampartners.fr",
  "logo": "https://branthampartners.fr/logo.svg",
  "description": "Cabinet specialise dans le rachat d'entreprises en difficulte en France. Sourcing proprietaire, due diligence acceleree, execution en audience.",
  "founder": {
    "@type": "Person",
    "name": "Paul Roulleau",
    "jobTitle": "Fondateur & Managing Partner",
    "url": "https://branthampartners.fr",
    "sameAs": [
      "https://www.linkedin.com/in/paulroulleau/",
      "https://twitter.com/branthamfr"
    ],
    "knowsAbout": ["Distressed M&A", "Procedures collectives", "Plan de cession", "Rachat entreprise en difficulte"]
  },
  "sameAs": [
    "https://www.linkedin.com/company/brantham-partners/",
    "https://twitter.com/branthamfr"
  ],
  "areaServed": {
    "@type": "Country",
    "name": "France"
  },
  "knowsAbout": ["Distressed M&A", "Procedures collectives", "Rachat entreprise en difficulte"]
}
```

→ **`sameAs` est la propriete la plus importante pour le GEO** — elle permet aux modeles IA de construire le graphe d'entite et verifier l'identite.

---

## IV. GEO (Generative Engine Optimization) — Score: 30/100

C'est le point faible majeur du site. Le contenu est riche mais pas structure pour etre cite par les moteurs IA.

### A. AI Citability — Score: 45/100

**Points forts**:
- Headings en format question ("Qu'est-ce que...?", "Quelles sont...?") → bon pour extraction
- FAQ schemas avec reponses directes
- Contenu factuel avec references legales
- Bonne densite statistique (barometre)

**Points faibles**:
- Blocs de contenu trop longs — les passages optimaux pour citation IA sont de **134-167 mots**, auto-contenus, avec des faits specifiques
- Pas de pattern "definition directe" en debut de paragraphe ("X est..." dans les 60 premiers mots)
- Densite de pronoms elevee (beaucoup de "il", "elle", "on") → reduit la capacite de parsing standalone
- Pas de marquage `speakable` pour guider les assistants IA
- Pas de fichier `llms.txt` (standard emergent pour guider les crawlers IA)

### B. llms.txt — ABSENT

Fichier `/llms.txt` a la racine du domaine : **inexistant**. Ce fichier aide les crawlers IA a comprendre la structure du site.

**A creer**:
```
# Brantham Partners
> Cabinet specialise dans le rachat d'entreprises en difficulte en France

## Services
- [Sourcing Proprietaire](https://branthampartners.fr/sourcing-proprietaire.html): Identification et sourcing d'opportunites de rachat
- [Due Diligence Acceleree](https://branthampartners.fr/due-diligence-acceleree.html): Analyse rapide des cibles en procedure collective
- [Execution en Audience](https://branthampartners.fr/execution-audience.html): Accompagnement lors des audiences au tribunal
- [Valorisation](https://branthampartners.fr/valorisation-entreprise-difficulte.html): Methodes de valorisation specifiques au distressed

## Guides
- [Rachat Entreprise en Difficulte](https://branthampartners.fr/rachat-entreprise-difficulte.html): Guide complet pour acquereurs
- [Liquidation Judiciaire](https://branthampartners.fr/liquidation-judiciaire.html): Comprendre la procedure
- [Redressement Judiciaire](https://branthampartners.fr/redressement-judiciaire.html): Cadre legal et opportunites
- [Plan de Cession](https://branthampartners.fr/plan-de-cession.html): Mecanisme et redaction d'offre

## Ressources
- [Glossaire M&A](https://branthampartners.fr/glossaire-ma.html): 192 termes definis
- [Barometre Defaillances](https://branthampartners.fr/barometre-defaillances.html): Donnees 2026
- [Insights](https://branthampartners.fr/insights.html): Articles et analyses
```

### C. Platform-Specific Readiness

| Plateforme | Score | Raison |
|-----------|-------|--------|
| **Google AI Overview** | 40/100 | Bon contenu structure, headings Q&A, mais pas de ranking traditionnel fort (site jeune?) |
| **ChatGPT Search** | 15/100 | Pas de Wikipedia, pas de Wikidata, Organization schema absent. 47.9% des citations ChatGPT viennent de Wikipedia |
| **Perplexity** | 20/100 | Pas de presence Reddit, pas de source primaire reconnue. PerplexityBot autorise (bien) |
| **Google Gemini** | 25/100 | Pas de YouTube, pas de Knowledge Graph, pas de Google Business Profile |
| **Bing Copilot** | 30/100 | Pas de IndexNow, pas de Bing Webmaster Tools, pas de LinkedIn company forte |

### D. AI Crawler Access — Score: 70/100

```
GPTBot          → ALLOWED ✅
ClaudeBot       → ALLOWED ✅
PerplexityBot   → ALLOWED ✅
Google-Extended → ALLOWED ✅
OAI-SearchBot   → NOT SPECIFIED ⚠️
ChatGPT-User    → NOT SPECIFIED ⚠️
Amazonbot       → NOT SPECIFIED ⚠️
Bytespider      → NOT SPECIFIED ⚠️
Applebot-Extended → NOT SPECIFIED ⚠️
Cohere-ai       → NOT SPECIFIED ⚠️
```

→ 4/14 crawlers explicitement autorises. Les non-specifies heritent du `Allow: /` global, mais l'explicite est preferable.

---

## V. Brand Authority — Score: 15/100

**C'est le facteur #1 de visibilite IA** (correlation 3x plus forte que les backlinks).

| Signal | Status | Impact |
|--------|--------|--------|
| **Wikipedia** | ABSENT | CRITIQUE — 47.9% des citations ChatGPT viennent de Wikipedia |
| **Wikidata** | ABSENT | CRITIQUE — entite machine-readable pour AI |
| **YouTube** | ABSENT | HAUT — correlation 0.737 avec visibilite IA |
| **Reddit** | ABSENT/INCONNU | HAUT — 46.7% des citations Perplexity viennent de Reddit |
| **LinkedIn Company** | PROBABLE | MOYEN — signal pour Bing Copilot |
| **Google Business Profile** | INCONNU | MOYEN — signal pour Gemini |
| **Trustpilot / Avis** | ABSENT | BAS — validation sociale |

**Constat**: Brantham Partners est probablement **invisible comme entite** pour les modeles IA. Sans Wikipedia, Wikidata, et YouTube, le site ne sera pas cite meme si le contenu est excellent.

---

## VI. E-E-A-T — Score: 55/100

| Dimension | Score | Detail |
|-----------|-------|--------|
| **Experience** | 50/100 | Pas de "nous avons fait X", pas de cas concrets, pas de screenshots de deals |
| **Expertise** | 65/100 | References legales solides (Code de commerce), terminologie precise, profondeur technique |
| **Authoritativeness** | 40/100 | Pas de citations par des tiers, pas de presse, pas de conferences, pas de Wikipedia |
| **Trustworthiness** | 65/100 | HTTPS, HSTS, pages legales completes (CGU, mentions legales, RGPD, cookies), author nomme |

**Recommandations E-E-A-T**:
1. Ajouter des case studies anonymises ("Nous avons accompagne le rachat de X dans le secteur Y...")
2. Creer une page auteur `/about.html` ou `/equipe.html` avec credentials detaillees
3. Ajouter des temoignages clients
4. Publier sur des medias tiers (Les Echos, L'Usine Nouvelle, Option Finance)
5. Ajouter des dates visibles et bylines sur chaque article

---

## VII. Recommandations Prioritaires

### P0 — CRITIQUE (cette semaine)

| # | Action | Impact GEO estime |
|---|--------|-------------------|
| 1 | **Ajouter Organization schema** avec `sameAs` vers LinkedIn, Twitter, et toute presence externe | +8 pts |
| 2 | **Ajouter Person schema** pour Paul Roulleau avec `sameAs`, `jobTitle`, `knowsAbout` | +5 pts |
| 3 | **Creer `/llms.txt`** a la racine du site | +5 pts |
| 4 | **Ajouter WebSite + SearchAction schema** sur homepage | +2 pts |

### P1 — HAUTE PRIORITE (ce mois)

| # | Action | Impact GEO estime |
|---|--------|-------------------|
| 5 | **Creer une page Wikipedia** Brantham Partners (si notoriete suffisante) ou au minimum une entree Wikidata | +15 pts |
| 6 | **Lancer un canal YouTube** avec analyses de marche distressed M&A | +10 pts |
| 7 | **Presence Reddit** — participer a r/entreprendre, r/vosfinances, r/france avec expertise | +5 pts |
| 8 | **Reformater le contenu pour citability** — blocs de 134-167 mots, auto-contenus, debut par definition directe | +5 pts |
| 9 | **Ajouter `speakable` property** sur les Article schemas | +3 pts |
| 10 | **Expliciter les 14 AI crawlers** dans robots.txt | +2 pts |

### P2 — OPTIMISATIONS (prochain trimestre)

| # | Action | Impact |
|---|--------|--------|
| 11 | Images WebP + `srcset` + `loading="lazy"` | Performance |
| 12 | OG images distinctes par page geo/secteur | CTR social |
| 13 | Critical CSS inline | LCP |
| 14 | Content-Security-Policy header | Securite |
| 15 | IndexNow protocol (Bing) | Bing Copilot |
| 16 | Google Business Profile | Gemini local |
| 17 | Case studies / temoignages clients | E-E-A-T |
| 18 | Bylines et dates visibles dans le HTML | E-E-A-T |
| 19 | `geo.position` (lat/long) sur pages geo | SEO local |
| 20 | Publications presse/medias tiers | Authoritativeness |

### Impact projete

| Etape | Actions | GEO Score |
|-------|---------|-----------|
| Actuel | — | **45/100** |
| Apres P0 (1 semaine) | Schemas + llms.txt | **65/100** |
| Apres P1 (1 mois) | Wikipedia + YouTube + Reddit + content reformat | **80/100** |
| Apres P2 (3 mois) | Full optimization | **90/100** |

---

## VIII. Inventaire Technique Complet

### Pages (68 total)

- **Core**: 8 pages (home, 3 services, valorisation, pillar, glossaire, barometre)
- **Guides**: 25 pages (procedures, financement, risques, modeles, etc.)
- **Geo**: 17 pages (Paris, Lyon, Marseille, Toulouse, Nice, Nantes, Bordeaux, Lille, Strasbourg, Rennes, Grenoble, Rouen, Angers, Dijon, Clermont-Ferrand, Montpellier, Le Havre + Saint-Etienne, Toulon, Orleans)
- **Secteurs**: 15 pages (agro, auto, BTP, commerce, energie, immobilier, imprimerie, industrie, metallurgie, restauration, sante, services, tech, textile, transport)
- **Legal**: 4 pages (CGU, mentions, confidentialite, cookies)
- **Autres**: insights.html, article.html, avertissement.html

### Stack

- **Generateur**: Python + Jinja2 (`/generator/generate.py`)
- **Template**: `base.html.j2` (35KB)
- **Donnees**: cities.json (17), sectors.json (15), shared.json
- **Hosting**: Vercel (static)
- **Fonts**: Google Fonts (Instrument Serif, DM Sans, DM Mono)
- **CSS**: Custom (pas de framework)
- **JS**: Minimal (pas de framework frontend)

### Fichiers de reference

| Fichier | Contenu |
|---------|---------|
| `/Users/paul/zura-inspired/robots.txt` | Config crawlers |
| `/Users/paul/zura-inspired/sitemap.xml` | 67 URLs |
| `/Users/paul/zura-inspired/vercel.json` | Headers + caching |
| `/Users/paul/zura-inspired/generator/generate.py` | Generateur static |
| `/Users/paul/zura-inspired/generator/templates/base.html.j2` | Template principal |
| `/Users/paul/zura-inspired/generator/data/cities.json` | 17 villes |
| `/Users/paul/zura-inspired/generator/data/sectors.json` | 15 secteurs |

---

*Audit genere le 2026-03-21 a partir du framework geo-seo-claude et de l'analyse exhaustive du code source.*

## Related
- [[website/_MOC]]
- [[remember/2026-03-21]]
- [[website/patterns/geo-seo-audit-swarm]]
- [[website/bugs/2026-03-21-contenu-duplique-geo-secteur]]
- [[website/sessions/2026-03-21]]
- [[brantham/sessions/2026-03-21-scan]]
