---
type: moc
project: website
updated: 2026-04-27
---

Brantham Partners website + SEO content machine.

Project location: `/Users/paul/zura-inspired/`

### Recent
- **2026-04-27** : Audit cohérence/orthographe + corrections en masse + deploy prod. Voir [[sessions/2026-04-27-audit-coherence-orthographe-deploy]]. 141 pages traitées, ~6 800 changements (orthographe + casse Tribunal + insécables FR). Pattern réutilisable : [[../patterns/html-mass-corrections-safe-replacement]].

### Status (2026-03-28)
- SEO Technique : **99/100** — geo.position + ICBM sur 95/95 pages, modified_time 2026-03-28 partout
- Structured Data : **100/100** — 0 erreur JSON-LD, HowTo valide sur toutes pages, FAQPage clean
- AI Citability (GEO) : **97/100** — llms.txt, 14 AI crawlers, 715 citations-ready, speakable partout
- Content Quality : **95/100** — Selon critique réduit (financement 4, prepack 4, modele 5)
- Performance : **93/100** — TTFB ~180ms, HSTS, CSP, cache CDN
- Brand Authority : **35/100** — ZERO backlinks, pas de Wikipedia/YouTube/Reddit
- **GEO Score global : ~84/100**
- Pages live : **95 pages** (20 geo + 42 secteur + 33 manuelles)
- Sitemap : **95 URLs** (lastmod 2026-03-28)
- IndexNow : 95 URLs soumises 2026-03-28 → 200 OK
- Glossaire : 192 termes
- Schemas JSON-LD : 6 types sur homepage, speakable sur 62 pages
- Cible : DA > 30, #1 keywords distressed M&A, cite par 50%+ AI
- Indexation Google : pages principales soumises GSC 18/03, re-soumettre avec nouvelles pages

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
- [x] Audit SEO/GEO complet + remediation (done 2026-03-21)
- [x] Deduplication contenu geo/secteur (done 2026-03-21)
- [x] equipe.html avec Person schema (done 2026-03-21)
- [x] procedure-collective.html 14K mots (done 2026-03-21)
- [x] CSP header + cache optimise (done 2026-03-21)
- [x] Speakable sur toutes les pages contenu (done 2026-03-21)
- [x] Organization standalone sur toutes les pages (done 2026-03-21)
- [x] Viewport WCAG fix (done 2026-03-21)
- [ ] Paul : relire contenu genere et envoyer corrections
- [ ] 3-5 cas d'etude anonymises
- [ ] Mentions legales : remplir placeholders
- [ ] Contenu EN pour "French distressed M&A"
- [ ] Barometre : actualiser donnees mensuellement

### TODO Contenu (Priorite 1 — DONE 2026-03-18)
- [x] `/trouver-entreprise-difficulte-racheter.html` — ~7170 mots
- [x] `/financement-rachat-entreprise-difficulte.html` — ~4800 mots
- [x] `/risques-rachat-entreprise-difficulte.html` — ~3955 mots
- [x] `/modele-offre-reprise-plan-cession.html` — ~8800 mots
- [x] `/purge-passif-plan-cession.html` — ~3000 mots
- [x] `/garantie-actif-passif-entreprise-difficulte.html` — ~3000 mots

### TODO Contenu (Priorite 2 — DONE 2026-03-18)
- [x] `/calendrier-procedure-collective.html` — ~3200 mots
- [x] `/difference-sauvegarde-redressement-judiciaire.html` — ~3500 mots
- [x] `/role-administrateur-judiciaire-acquereur.html` — ~3200 mots
- [x] `/droits-salaries-plan-cession.html` — ~3000 mots
- [ ] `/due-diligence-entreprise-difficulte-guide.html` — enrichir page service existante

### TODO Contenu (Priorite 3 — prochaines sessions)
- [ ] Pages sectorielles : rachat-restaurant-difficulte, rachat-commerce-difficulte, rachat-btp-difficulte
- [ ] Lead magnets PDF : modele offre reprise, checklist due diligence, calculateur budget
- [ ] Cluster expansion : sauvegarde-judiciaire, conciliation-mandat-ad-hoc, sort-contrats-plan-cession
- [ ] Cas d'etude anonymises (3-5 minimum)
- [ ] Guide "100 jours post-reprise"
- [ ] Contenu EN pour "French distressed M&A"

### Pages existantes enrichies (DONE 2026-03-18)
- [x] rachat-entreprise-difficulte.html : +H2 "Comment racheter en LJ"
- [x] cout-rachat-entreprise-liquidation.html : +H2 "Cout en RJ"
- [x] valorisation-entreprise-difficulte.html : +H2 "DCF inadapte"
- [x] reprise-a-la-barre.html : +H2 "Cas pratiques reussis"

### TODO Hors Code (Paul)
- [x] Google Search Console + soumettre sitemap (pages principales faites 2026-03-18)
- [ ] GSC : indexer les 10 nouvelles pages + sectorielles + geographiques
- [ ] IndexNow API (Bing/Yandex)
- [ ] Google Business Profile
- [ ] Page LinkedIn Brantham Partners + premier post
- [ ] Bing Webmaster Tools
- [ ] Inscription annuaires : Crunchbase, Medium, Pages Jaunes, Societe.com, Twitter/X
- [ ] Inscription annuaires pro : CRA, Fusacq, BPI Bourse Transmission
- [ ] 5-10 avis Google
- [ ] Pitch presse (Les Echos, La Tribune, JDN)
- [ ] Guest post Village de la Justice
- [ ] Wikipedia
- [ ] Renommer /article.html → /defaillances-entreprises-2025.html

### Strategie
- [[website/strategies/2026-03-18-fast-ranking-strategy]] — Plan complet fast indexation + ranking (5 phases, calendrier 6 mois)

### Audits
- [[website/audits/2026-03-21-seo-geo-audit]] — Audit GEO complet (framework geo-seo-claude), score 42→82

### Sessions
- [[website/sessions/2026-03-21]] — Audit SEO/GEO multi-agents + deduplication contenu + 2 pages creees + remediation complete
- [[website/sessions/2026-03-18]] — Fast ranking strategy + 10 pages creees + 4 pages enrichies + fixes techniques + sitemap/llms.txt/insights updates
- [[website/sessions/2026-03-16]] — CSS unification 20 pages, WCAG AA, FAQ unifie, blocs dupliques supprimes
- [[website/sessions/2026-03-15]] — SEO overhaul complet (4 audit + 5 fix agents) + glossaire 88 termes
- [[website/sessions/2026-03-14]] — Pages service sourcing proprietaire + execution audience + due diligence acceleree creees
- [[website/sessions/2026-03-13]] — Mega audit + implementation + 4 pages creees

### Research
- [[website/research/2026-03-18-indexation-ranking-audit]] — Audit complet : 0 page indexee, 38 keywords analyses, 12 concurrents cartographies, plan d'action 3 mois
- [[website/research/2026-03-18-keyword-research-distressed-ma]] — 20 keywords analyses, 6 pages priorite 1 identifiees, 4 concurrents profiles

### Links
- [[website/architecture]]
- [[website/seo-strategy]]
- [[website/brand-voice]]
- [[website/decisions/2026-03-13-geo-strategy-ai-visibility]]
- [[website/patterns/geo-ai-content-optimization]]
- [[website/patterns/seo-subagent-audit-fix]]
- [[website/patterns/geo-seo-audit-swarm]]
- [[website/bugs/2026-03-21-contenu-duplique-geo-secteur]]
## Related
## Related
## Related
## Related
