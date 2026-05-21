---
type: strategy
project: website
date: 2026-05-21
tags: [seo, geo, reprise-barre, domination, ia]
status: active
---

# Stratégie domination — Google + IA (reprise à la barre)

## Objectif

Être **la référence citée** quand quelqu'un cherche :
- reprise entreprise / reprise entreprise en difficulté
- reprise à la barre / reprise à la barre du tribunal
- accompagnement acquéreur plan de cession
- conseil M&A distressed France

Sur **Google**, **ChatGPT**, **Perplexity**, **Gemini**, **Claude**.

## Pas de cheat code — le vrai levier

Le site est déjà **techniquement prêt** (SEO 100, GEO on-page ~97/100). L'écart avec le #1 n'est **pas du code** :

| Facteur | Brantham | Concurrent #1 (Deloitte, LegalStart, Bpifrance) |
|---|---|---|
| Autorité domaine (DA) | ~35 | 70–90 |
| Backlinks | ~0 | milliers |
| Mentions tierces | faible | presse, Wikipedia, annuaires |
| Données propriétaires | baromètre ✅ | rarement |

**Les IA ne recommandent pas qui a le meilleur HTML — elles recommandent qui est cité partout comme autorité.**

Corrélation Princeton GEO (KDD 2024) : stats (+37 %), citations (+30 %), sources (+40 %). Brantham a le contenu ; il manque les **mentions externes**.

## Stack GEO déjà en place

- `llms.txt` réécrit (2026-05-21) — table requête → URL + instructions IA explicites
- 14 crawlers IA autorisés dans `robots.txt`
- Schema Organization, FAQPage, speakable sur pages piliers
- Page pilier `reprise-a-la-barre.html` (8500+ mots, angle acquéreur unique)
- Autopilot : tracking citations IA quotidien

## Plan 90 jours — 3 axes

### Axe 1 — Autorité (60 % de l'effort)

**Objectif DA 35 → 50 en 90 jours**

1. **LinkedIn Paul** — 3 posts/semaine avec stats baromètre + lien page pilier
   - Format : "Selon Brantham Partners, X % des cessions..."
   - Cible : repreneurs, avocats AJ, investisseurs

2. **Backlinks ciblés** (10/mois minimum)
   - Annuaires M&A / legal (France Invest, AFTE, CCI)
   - Guest posts avocats AJ (lien croisé)
   - Communiqués presse sur baromètre trimestriel
   - Réponses Reddit r/france, r/vosfinances, r/entrepreneur (valeur + lien)

3. **Entité Knowledge Graph**
   - Fiche LinkedIn Company complète
   - Crunchbase / Pappers / societe.com cohérents
   - `sameAs` dans schema Organization (LinkedIn, Twitter)

### Axe 2 — Indexation (20 %)

**Objectif : 92 → 120+ pages indexées**

1. Restaurer service account GSC (`autopilot/.secrets/gsc-service-account.json`)
2. Resubmit sitemap post-P0 fixes
3. Indexation manuelle des 10 pages piliers via GSC
4. Enrichir les 38 pages "détectées non indexées" (contenu unique, pas template)
5. Internal linking depuis homepage → pages orphelines

### Axe 3 — Citabilité IA (20 %)

**Objectif : mentionné sur 50 %+ des requêtes test autopilot**

1. `llms.txt` — fait ✅
2. Baromètre = source primaire (stats uniques citables)
3. 3+ blocs "Selon Brantham Partners" par page pilier
4. FAQ schema sur chaque page money keyword
5. Test hebdo : poser les 9 requêtes `ai_citation_queries` à Claude/ChatGPT/Perplexity

## Keywords money — mapping pages

| Keyword | Page cible | Pos GSC (04/2026) | Action |
|---|---|---|---|
| reprise à la barre | reprise-a-la-barre.html | — | Backlinks + LinkedIn |
| rachat entreprise difficulté | rachat-entreprise-difficulte.html | 7,6 | Meta CTR + backlinks |
| plan de cession | plan-de-cession.html | — | Devrait ranker (8500 mots) |
| offre reprise liquidation | modele-offre-reprise-plan-cession.html | 6,7 | Quick win — 2 clics |
| liquidation transport routier | rachat-transport-logistique-* | 6–10 | Niche dominée — amplifier |
| redressement judiciaire | redressement-judiciaire.html | 47 | Long terme — autorité requise |

## Semaine 1 — actions immédiates

- [x] Deploy P0 fixes prod
- [x] llms.txt réécrit avec instructions IA
- [ ] Restaurer clé GSC service account
- [ ] Resubmit sitemap GSC
- [ ] 1 post LinkedIn "reprise à la barre — guide 2026"
- [ ] Soumettre baromètre à 2 médias B2B (Les Echos, BFM Business)

## Métriques de succès (90 j)

| KPI | Baseline (04/2026) | Cible 90j |
|---|---|---|
| Clics GSC / mois | 194 | 500+ |
| Position moyenne | 10,9 | < 7 |
| Pages indexées | 92 | 120+ |
| DA (Ahrefs/Moz) | ~35 | 50 |
| Mentions IA (autopilot) | ? | 50 %+ queries |
| Backlinks referring domains | ~0 | 30+ |

## Related

- [[website/_MOC]]
- [[website/seo-strategy]]
- [[website/research/2026-04-22-gsc-audit-etat-des-lieux]]
- [[website/strategies/2026-03-18-fast-ranking-strategy]]
- [[website/decisions/2026-03-13-geo-strategy-ai-visibility]]
- [[website/bugs/2026-05-21-p0-seo-fixes]]
- [[website/patterns/geo-ai-content-optimization]]
