---
type: strategy
project: website
date: 2026-03-18
status: active
---

# Strategie Fast Ranking — Brantham Partners

## Etat des lieux (18 mars 2026)

- **Domaine** : branthampartners.fr — cree le 11 mars 2026 (7 jours)
- **Indexation Google** : 0 pages indexees (`site:branthampartners.fr` = 0)
- **Backlinks** : 0
- **Pages live** : 17 (130 000+ mots au total)
- **Avantage** : contenu superieur a 100% des concurrents, schema markup avance, angle acquereur unique

## Positionnement unique

Brantham est le **seul acteur** qui combine :
- Angle 100% acquereur (vs juridique/dirigeant chez les concurrents)
- Data proprietaire (BODACC, barometre defaillances)
- Templates actionables (modeles d'offre, checklists)
- Expertise M&A pratique (pas juste du droit)

**Concurrents et leurs angles** :
| Concurrent | DA | Angle | Faiblesse |
|-----------|-----|-------|-----------|
| LegalStart | ~65 | Dirigeant en difficulte | Zero contenu acquereur |
| BPI Creation | ~80 | Repreneur generique | Pas specifique distressed |
| CaptainContrat | ~55 | Mixte dirigeant/repreneur | Pas technique M&A |
| Facchini Avocat | ~35 | Juridique pur | Pas de data, pas de deals |
| Deloitte Avocats | ~85 | Corporate/institutionnel | Articles courts, dates 2018 |
| Village de la Justice | ~70 | Juristes pour juristes | Pas d'angle business |

---

## PHASE 1 : Indexation forcee (Semaine 1 — 18-25 mars)

### Actions techniques

1. **Google Search Console**
   - Verifier que le site est ajoute et verifie
   - Soumettre sitemap.xml
   - Demander indexation URL par URL (17 pages)
   - Verifier qu'il n'y a pas d'erreurs de crawl

2. **IndexNow** (Bing/Yandex)
   ```
   POST https://api.indexnow.org/indexnow
   {
     "host": "branthampartners.fr",
     "key": "[API_KEY]",
     "urlList": [toutes les 17 URLs]
   }
   ```

3. **Ping Google sitemap**
   ```
   https://www.google.com/ping?sitemap=https://branthampartners.fr/sitemap.xml
   ```

4. **Fixes techniques**
   - Corriger inconsistances URL (certains liens sans `.html`)
   - Ajouter alt text sur toutes les images
   - Ajouter meta description sur les 5 pages qui n'en ont pas (sourcing, due diligence, execution, homepage OG)
   - Renommer `/article.html` → `/defaillances-entreprises-2025.html` (URL descriptive)

### Premiers signaux de confiance

5. **Profil LinkedIn Brantham Partners** → lien vers le site
6. **Profil LinkedIn Paul Roulleau** → lien vers le site + titre "Founder @ Brantham Partners"
7. **Google Business Profile** → creer et verifier
8. **Post LinkedIn** avec lien vers `/rachat-entreprise-difficulte.html`
9. **Twitter/X** → profil avec lien

---

## PHASE 2 : Blitz contenu long-tail (Semaines 2-5)

### 6 pages Priorite 1 (ROI maximum)

Pages a creer dans l'ordre — chacune cible un keyword ou personne ne parle a l'acquereur :

| # | URL | Keyword cible | Volume est. | Difficulte | Pourquoi |
|---|-----|---------------|-------------|------------|----------|
| 1 | `/trouver-entreprise-difficulte-racheter.html` | comment trouver entreprise en difficulte a racheter | 1K-5K/mois | Moyenne | Volume eleve, angle sourcing unique, pousse vers service Brantham |
| 2 | `/financement-rachat-entreprise-difficulte.html` | financement rachat entreprise en difficulte | 500-1K | Faible | Zero contenu specifique distressed (LBO, fonds retournement, BPI Transmission) |
| 3 | `/risques-rachat-entreprise-difficulte.html` | risques rachat entreprise en difficulte | 500-1K | Faible | Aucune matrice risques/mitigation par procedure |
| 4 | `/modele-offre-reprise-plan-cession.html` | offre de reprise plan de cession modele | 200-500 | Tres faible | Lead magnet — aucun template telechargeable sur le marche |
| 5 | `/purge-passif-plan-cession.html` | purge du passif plan de cession | 200-500 | Faible | Contenu existant = juridique pur, zero angle acquereur |
| 6 | `/garantie-actif-passif-entreprise-difficulte.html` | garantie actif passif entreprise difficulte | 200-500 | Faible | Gap enorme — personne n'explique l'absence de GAP en plan de cession |

**Format de chaque page** :
- 3 000-5 000 mots
- H1 = keyword exact
- 8-10 H2 sous forme de questions
- FAQ schema (8-10 Q&A)
- Article schema avec auteur nomme
- Breadcrumb schema
- 3+ "Selon Brantham Partners, [stat/fait]" (GEO optimization)
- 10+ liens internes vers pages existantes
- Citations Code de commerce avec liens Legifrance
- 1 tableau comparatif minimum
- CTA vers service Brantham pertinent

### 5 pages Priorite 2 (semaines 4-6)

| # | URL | Keyword cible |
|---|-----|---------------|
| 7 | `/calendrier-procedure-collective.html` | calendrier procedure collective france |
| 8 | `/difference-sauvegarde-redressement-judiciaire.html` | difference sauvegarde redressement judiciaire |
| 9 | `/role-administrateur-judiciaire-acquereur.html` | role administrateur judiciaire reprise |
| 10 | `/droits-salaries-plan-cession.html` | droits des salaries plan de cession |
| 11 | `/due-diligence-entreprise-difficulte-guide.html` | due diligence entreprise en difficulte guide |

### Optimisations pages existantes

| Page | Action |
|------|--------|
| `/rachat-entreprise-difficulte.html` | Ajouter H2 "Comment racheter une entreprise en liquidation judiciaire" (keyword secondaire fort) |
| `/cout-rachat-entreprise-liquidation.html` | Ajouter section "Cout en redressement judiciaire" (keyword distinct) |
| `/reprise-a-la-barre.html` | Enrichir pour depasser Deloitte (ajouter cas reels, comparatif prepack vs barre) |
| `/valorisation-entreprise-difficulte.html` | Ajouter "DCF impossible en distressed" + comparables ajustes |
| `/article.html` | Renommer URL → `/defaillances-entreprises-2025.html` |

---

## PHASE 3 : Backlinks agressifs (Semaines 2-8)

### Tier 1 — Backlinks faciles (semaines 2-3)

| Source | Action | DA est. |
|--------|--------|---------|
| LinkedIn (page entreprise) | Creer + publier 2 articles/semaine | 98 |
| LinkedIn (Paul Roulleau) | Posts reguliers avec liens | 98 |
| Google Business Profile | Creer fiche | 100 |
| Twitter/X | Profil + tweets reguliers | 94 |
| Medium | Republier extraits d'articles | 95 |
| Crunchbase | Creer profil entreprise | 91 |
| AngelList / Wellfound | Creer profil | 85 |
| Societe.com | Verifier presence | 65 |
| Pages Jaunes / PagesJaunes Pro | Creer fiche | 70 |

### Tier 2 — Annuaires professionnels (semaines 3-5)

| Source | Action | DA est. |
|--------|--------|---------|
| CRA (Cedants et Repreneurs d'Affaires) | Inscription | ~40 |
| Fusacq | Creer profil intermediaire | ~35 |
| CNCEF (si eligible) | Inscription annuaire | ~30 |
| BPI Bourse de la Transmission | Inscription | ~80 |
| Annuaire avocats-conseils.fr | Inscription | ~30 |
| Mappy / Yelp France | Fiches locales | ~60 |

### Tier 3 — Content marketing backlinks (semaines 4-8)

| Strategie | Details |
|-----------|---------|
| **Guest posts** | Proposer des articles a Village de la Justice (DA ~70), Le Journal du Net (DA ~85), Maddyness (DA ~70), FrenchWeb (DA ~60) |
| **Tribunes expert** | Proposer des tribunes a Les Echos, Le Figaro Eco, BFM Business |
| **HARO / Connectively** | Repondre aux journalistes qui cherchent des experts M&A/restructuring |
| **Interviews podcast** | Podcasts business/legal FR (Generation Do It Yourself, Contrepoint, etc.) |
| **Infographies partageables** | Barometre defaillances en infographie → pitche aux journalistes |
| **Citations presse** | Contacter journalistes qui couvrent defaillances (Les Echos, L'Usine Nouvelle) quand une grosse defaillance tombe |

### Tier 4 — Digital PR (mois 2-3)

| Action | Impact |
|--------|--------|
| Publier le barometre defaillances mensuellement | Les journalistes adorent les donnees exclusives |
| Creer un "Turnaround Index" proprietaire | Concurrent direct du 8 Advisory Turnaround Index (cite par Les Echos) |
| Commenter les grosses defaillances sur LinkedIn/Twitter | Visibilite + backlinks naturels |
| Wikipedia — contribuer aux articles procedures collectives | Pas de lien direct mais credibilite |

---

## PHASE 4 : Content machine (Mois 2-4)

### Rythme cible

- **Mois 1** : 2-3 pages/semaine (les 11 pages prioritaires ci-dessus)
- **Mois 2-3** : 2 pages/semaine + 2 posts LinkedIn/semaine
- **Mois 3-4** : 1-2 pages/semaine + pages programmatiques (geo, secteurs)

### Cluster expansion — Pages suivantes a creer

**Cluster Procedures (enrichir le cluster existant)** :
- `/sauvegarde-judiciaire.html` — procedure de sauvegarde (volume eleve)
- `/conciliation-mandat-ad-hoc.html` — procedures amiables
- `/cession-fonds-commerce-procedure-collective.html`
- `/sort-contrats-plan-cession.html` — continuation des contrats
- `/contestation-plan-cession.html` — recours et contestations

**Cluster Valorisation (enrichir)** :
- `/decote-valorisation-entreprise-difficulte.html`
- `/methode-dcf-entreprise-difficulte.html`
- `/valeur-liquidation-vs-going-concern.html`

**Cluster Pratique Acquereur (nouveau, unique)** :
- `/checklist-due-diligence-distressed.html` (lead magnet)
- `/100-jours-post-reprise.html` (zero contenu existant sur le marche)
- `/erreurs-rachat-entreprise-difficulte.html`
- `/negocier-avec-administrateur-judiciaire.html`
- `/preparer-audience-tribunal-commerce.html`

**Cluster Sectoriel (pages programmatiques)** :
- `/rachat-restaurant-difficulte.html`
- `/rachat-commerce-difficulte.html`
- `/rachat-entreprise-btp-difficulte.html`
- `/rachat-industrie-difficulte.html`
- `/rachat-startup-difficulte.html`
- `/rachat-franchise-difficulte.html`
- + 10 autres secteurs

**Cluster Geographique (pages programmatiques)** :
- `/rachat-entreprise-difficulte-paris.html`
- `/rachat-entreprise-difficulte-lyon.html`
- `/rachat-entreprise-difficulte-marseille.html`
- + 12 autres villes Tier 1

**Cluster Donnees/Actualites** :
- `/defaillances-entreprises-2026.html` (stats mensuelles mises a jour)
- `/defaillances-[secteur]-2026.html` × 5 secteurs
- `/tribunal-commerce-[ville]-procedures.html` × 5 villes

### Lead magnets a creer

| Lead magnet | Format | Page hote |
|-------------|--------|-----------|
| Modele d'offre de reprise | PDF editable | `/modele-offre-reprise-plan-cession.html` |
| Checklist due diligence distressed | PDF interactif | `/due-diligence-entreprise-difficulte-guide.html` |
| Calculateur budget total de reprise | Page interactive | `/cout-rachat-entreprise-liquidation.html` |
| Timeline procedure collective | Infographie SVG | `/calendrier-procedure-collective.html` |
| Guide "100 jours post-reprise" | PDF 20 pages | `/100-jours-post-reprise.html` |
| Matrice risques/mitigation | PDF | `/risques-rachat-entreprise-difficulte.html` |

---

## PHASE 5 : Signaux E-E-A-T (continu)

### Experience
- Cas d'etude anonymises (3-5 minimum)
- "Nous avons accompagne X acquisitions en procedure collective"
- Temoignages clients (meme anonymises)

### Expertise
- Page auteur Paul Roulleau avec bio, credentials, publications
- Schema Person avec sameAs (LinkedIn, etc.)
- Byline sur chaque article

### Autorite
- Citations dans la presse
- Backlinks depuis sites institutionnels
- Donnees proprietaires (barometre, index)
- Guest posts sur sites a forte autorite

### Fiabilite
- HTTPS (deja OK)
- Mentions legales completes
- Sources Legifrance sur chaque article
- Dates de mise a jour visibles

---

## Calendrier semaine par semaine

### Semaine 1 (18-25 mars) — INDEXATION
- [ ] Verifier GSC + soumettre sitemap + demander indexation 17 URLs
- [ ] IndexNow API pour Bing/Yandex
- [ ] Ping Google sitemap
- [ ] Corriger 5 meta descriptions manquantes
- [ ] Corriger inconsistances URLs (.html)
- [ ] Creer page LinkedIn Brantham Partners
- [ ] Creer Google Business Profile
- [ ] Premier post LinkedIn avec lien vers le site

### Semaine 2 (25 mars - 1 avril) — CONTENU #1
- [ ] Creer `/trouver-entreprise-difficulte-racheter.html` (5000 mots)
- [ ] Creer `/financement-rachat-entreprise-difficulte.html` (4000 mots)
- [ ] 2 posts LinkedIn
- [ ] Inscription 5 annuaires Tier 1 (Crunchbase, Medium, Pages Jaunes, Societe.com, Twitter)

### Semaine 3 (1-8 avril) — CONTENU #2
- [ ] Creer `/risques-rachat-entreprise-difficulte.html` (4000 mots)
- [ ] Creer `/modele-offre-reprise-plan-cession.html` (3500 mots + PDF modele)
- [ ] 2 posts LinkedIn
- [ ] Inscription 5 annuaires Tier 2 (CRA, Fusacq, BPI Bourse, Mappy)

### Semaine 4 (8-15 avril) — CONTENU #3
- [ ] Creer `/purge-passif-plan-cession.html` (3500 mots)
- [ ] Creer `/garantie-actif-passif-entreprise-difficulte.html` (3500 mots)
- [ ] Optimiser 4 pages existantes (H2 additionnels, sections enrichies)
- [ ] 2 posts LinkedIn
- [ ] Premier guest post pitch (Village de la Justice)

### Semaine 5 (15-22 avril) — CONTENU #4
- [ ] Creer `/calendrier-procedure-collective.html` (3500 mots + timeline visuelle)
- [ ] Creer `/difference-sauvegarde-redressement-judiciaire.html` (4000 mots)
- [ ] 2 posts LinkedIn
- [ ] Analyser premiers resultats GSC (impressions, clics, positions)

### Semaine 6 (22-29 avril) — CONTENU #5
- [ ] Creer `/role-administrateur-judiciaire-acquereur.html` (3000 mots)
- [ ] Creer `/droits-salaries-plan-cession.html` (3500 mots)
- [ ] Creer `/due-diligence-entreprise-difficulte-guide.html` (4000 mots)
- [ ] 2 posts LinkedIn
- [ ] Pitch tribune presse (Les Echos, JDN)

### Semaines 7-8 (avril fin) — CONSOLIDATION
- [ ] Publier barometre defaillances mensuel (donnees mars 2026)
- [ ] Creer 2 pages sectorielles (restaurant, BTP)
- [ ] Creer 2 pages geographiques (Paris, Lyon)
- [ ] 4 posts LinkedIn
- [ ] Suivre et relancer les demandes backlinks

### Mois 3 (mai) — ACCELERATION
- [ ] 8 nouvelles pages (sectorielles + geographiques + cluster expansion)
- [ ] 2 lead magnets (PDF checklist + calculateur)
- [ ] 8 posts LinkedIn
- [ ] 2 guest posts publies
- [ ] Infographie barometre → pitch presse

### Mois 4 (juin) — AUTORITE
- [ ] 6-8 nouvelles pages
- [ ] Cas d'etude anonymises (3 minimum)
- [ ] Page equipe / a propos enrichie
- [ ] Monitoring positions keywords → ajuster strategie

---

## KPIs cibles

| Metrique | M1 | M2 | M3 | M6 |
|----------|-----|-----|-----|-----|
| Pages indexees | 17 | 28 | 45 | 80+ |
| Backlinks | 15 | 35 | 60 | 120+ |
| Keywords top 100 | 20 | 60 | 150 | 300+ |
| Keywords top 10 | 0 | 3-5 | 10-15 | 25+ |
| Keywords top 3 | 0 | 0-1 | 3-5 | 8-12 |
| Visites organiques/mois | 0 | 200 | 1000 | 3000+ |
| Leads generes | 0 | 2-3 | 5-10 | 15-25 |
| DA (Domain Authority) | 0 | 5-10 | 15-20 | 25-35 |

---

## Keywords prioritaires — Vue complete

### Quick wins (faible concurrence, angle acquereur unique)

| Keyword | Volume est. | Page |
|---------|-------------|------|
| offre de reprise plan de cession modele | 200-500 | A creer |
| purge du passif plan de cession | 200-500 | A creer |
| garantie actif passif entreprise difficulte | 200-500 | A creer |
| multiple ebitda entreprise difficulte | 200-500 | Existe |
| cout rachat entreprise liquidation judiciaire | 500-1K | Existe |
| prepack cession avantages | 200-500 | Existe |
| due diligence acceleree procedure collective | 100-200 | Existe (service) |

### Mid-tail (concurrence moyenne, fort volume)

| Keyword | Volume est. | Page |
|---------|-------------|------|
| comment trouver entreprise difficulte a racheter | 1K-5K | A creer |
| financement rachat entreprise difficulte | 500-1K | A creer |
| risques rachat entreprise difficulte | 500-1K | A creer |
| difference sauvegarde redressement | 1K-5K | A creer |
| reprise a la barre tribunal | 500-1K | Existe |
| droits salaries plan de cession | 500-1K | A creer |

### Head keywords (concurrence forte, objectif 6 mois)

| Keyword | Volume est. | Page |
|---------|-------------|------|
| rachat entreprise en difficulte | 1.5K-3K | Existe (pillar) |
| liquidation judiciaire | 10K-50K | Existe |
| redressement judiciaire | 10K-50K | Existe |
| plan de cession | 1K-5K | Existe |
| procedure collective | 2K-5K | A enrichir |
| valorisation entreprise | 3K-5K | Existe |

---

## Regles de production contenu

1. **Minimum 3 000 mots** par page (5 000+ pour pillar pages)
2. **H1 = keyword exact**, H2 = questions utilisateur
3. **FAQ schema** 8-10 Q&A par page
4. **Article schema** avec auteur nomme (Paul Roulleau)
5. **Breadcrumb schema** sur toutes les pages
6. **3+ citations "Selon Brantham Partners"** par page (GEO)
7. **10+ liens internes** contextuels par page
8. **Citations Code de commerce** avec liens Legifrance
9. **1+ tableau comparatif** par page
10. **Date de publication et mise a jour** visibles
11. **Meta description** unique, 150-160 caracteres, keyword + CTA implicite
12. **Alt text** sur toutes les images
13. **CTA** vers service Brantham pertinent
14. **Zero keyword stuffing** — densite naturelle 1-2%
