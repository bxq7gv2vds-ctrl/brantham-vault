---
type: moc
project: website
updated: 2026-03-16
---

Brantham Partners website + SEO content machine.

Project location: `/Users/paul/zura-inspired/`

### Status (2026-03-16)
- SEO Technique : ~93/100 — canonical, meta, Twitter Cards, OG fixes across all pages
- AI Visibility : ~4.2/5 — llms.txt rewrite, +3 AI bots robots.txt, 100+ "Brantham Partners" declarative phrases
- UX/Performance : ~96/100 (was 92) — CSS unifie 20 pages, WCAG AA tap targets, 1 seul bloc CSS par page, FAQ unifie Type A, focus-visible + reduced-motion
- Pages live : 19 indexables (accueil, article, glossaire, barometre, pillar, sourcing proprietaire, due diligence acceleree, execution audience, valorisation, liquidation judiciaire, redressement judiciaire, plan de cession, reprise a la barre, insights, mentions legales, confidentialite, CGU, cookies, avertissement) + equipe (noindex)
- Glossaire : 192 termes (was 142) — domination semantique M&A/procedures collectives/finance/valorisation
- Schemas JSON-LD accueil : 6 (Organization, ProfessionalService, FAQPage, HowTo, WebSite, BreadcrumbList)
- Cible : 100+ pages, DA > 30, #1 keywords distressed M&A, cite par 50%+ AI

### Stack
- SEO Machine: Claude Code workspace with custom commands + agents + Python analytics
- Commands: /article, /research, /write, /optimize, /publish-draft, /analyze-existing, /landing-pages
- 9 specialized agents + 30+ marketing skills
- Python pipeline: search_intent_analyzer, keyword_analyzer, readability_scorer, seo_quality_rater
- Data integrations: GA4, Google Search Console, DataForSEO, WordPress REST API

### Design System
- Colors: cream #FAFAF8, off #F4F3F0, ink #0F0F0E, navy #001F54, navy-hover #00153D
- Fonts: DM Sans (300-700 variable), DM Mono (400-500), Instrument Serif (normal+italic)
- Contrast: --t3 #6A6A66, --t4 #767672 (WCAG AA compliant)
- Border radius: 12px default, 16px md, 20px lg, 40px pills

### Pages Live
| Page | URL | Schemas |
|------|-----|---------|
| Accueil | / | Organization, ProfessionalService, FAQPage (10Q), HowTo, WebSite, BreadcrumbList |
| Glossaire M&A | /glossaire-ma.html | DefinedTermSet (192 termes), FAQPage (8Q), BreadcrumbList |
| Barometre Defaillances | /barometre-defaillances.html | Dataset, Article, FAQPage, BreadcrumbList |
| Page Equipe | /equipe.html | Person (Paul Roulleau), BreadcrumbList |
| Pillar Page | /rachat-entreprise-difficulte.html | Article, FAQPage (8Q), BreadcrumbList |
| Article defaillances | /article.html | Article |
| Mentions legales | /mentions-legales.html | - |
| CGU | /cgu.html | - |
| Politique confidentialite | /politique-confidentialite.html | - |
| Politique cookies | /politique-cookies.html | - |
| Sourcing proprietaire | /sourcing-proprietaire.html | Service, FAQPage (8Q), BreadcrumbList |
| Due diligence acceleree | /due-diligence-acceleree.html | Service, FAQPage (8Q), BreadcrumbList |
| Execution en audience | /execution-audience.html | Service, FAQPage (8Q), BreadcrumbList |
| Valorisation distressed | /valorisation-entreprise-difficulte.html | Service, FAQPage (8Q), BreadcrumbList |
| Redressement judiciaire | /redressement-judiciaire.html | Article, FAQPage (10Q), BreadcrumbList |
| Avertissement / Disclaimer | /avertissement.html | - |
| Insights (index) | /insights.html | CollectionPage, BreadcrumbList |

### AI Visibility Infrastructure
- llms.txt : live (instructions directes aux crawlers AI)
- robots.txt : GPTBot, ClaudeBot, PerplexityBot, Applebot-Extended, CCBot, Google-Extended, OAI-SearchBot, Meta-ExternalAgent, cohere-ai autorises
- Contenu : "Brantham Partners" comme sujet de phrases declaratives
- Tables HTML sr-only pour stats (parsable par AI)
- FAQ : 10 questions (accueil) + FAQ sur chaque page

### Playbook Strategie
- Source : `/Users/paul/Downloads/science-seo-geo-brantham.docx`
- 5 principes : Source Primaire Irreplacable, Semantic Completeness, Citation-Ready Content, E-E-A-T Stacking, Freshness Loop
- Architecture cible : 6 clusters, 90+ pages
- Paper reference : Princeton KDD 2024 (Aggarwal et al.) — GEO

### TODO Code
- [x] Glossaire 192 termes (done 2026-03-15, was 142, was 88)
- [x] 3 guides longs : liquidation, plan de cession, reprise a la barre (done 2026-03-15)
- [x] Page service : sourcing proprietaire
- [x] Page service : execution en audience
- [x] Page service : due diligence acceleree
- [x] Liens internes homepage vers pages service (done 2026-03-15)
- [x] Sitemap mis a jour avec 3 pages service (done 2026-03-15)
- [x] SEO overhaul complet : canonical, meta, Twitter Cards, OG, navbar/footer harmonises (done 2026-03-15)
- [x] llms.txt rewrite complet (done 2026-03-15)
- [x] robots.txt +3 AI bots (done 2026-03-15)
- [x] Page service : valorisation (done 2026-03-15)
- [x] Page blog/insights index (done 2026-03-15)
- [x] CSS unification 20 pages + WCAG AA + FAQ unifie (done 2026-03-16)
- [ ] 3-5 cas d'etude anonymises
- [ ] Mentions legales : remplir placeholders
- [ ] Contenu EN pour "French distressed M&A"
- [ ] Barometre : actualiser donnees mensuellement

### TODO Hors Code (Paul)
- [ ] Google Business Profile
- [ ] Google Search Console + Bing Webmaster Tools
- [ ] 5-10 avis Google
- [ ] LinkedIn posts barometre
- [ ] Pitch presse (Les Echos, La Tribune)
- [ ] Wikipedia
- [ ] Annuaires (Pages Jaunes, Societe.com, CCI, Village de la Justice)

### Sessions
- [[website/sessions/2026-03-16]] — CSS unification 20 pages, WCAG AA, FAQ unifie, blocs dupliques supprimes
- [[website/sessions/2026-03-15]] — SEO overhaul complet (4 audit + 5 fix agents) + glossaire 88 termes
- [[website/sessions/2026-03-14]] — Pages service sourcing proprietaire + execution audience + due diligence acceleree creees
- [[website/sessions/2026-03-13]] — Mega audit + implementation + 4 pages creees

### Links
- [[website/architecture]]
- [[website/seo-strategy]]
- [[website/brand-voice]]
- [[website/decisions/2026-03-13-geo-strategy-ai-visibility]]
- [[website/patterns/geo-ai-content-optimization]]
- [[website/patterns/seo-subagent-audit-fix]]
