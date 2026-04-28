---
date: 2026-04-27
project: brantham
type: session
tags: [cockpit-web, hunters, frontend, M&A]
---

# Session 2026-04-27 — Cockpit Web + Hunters v2

## Contexte
Pivot vers une **app web Next.js** comme cockpit principal (la TUI Textual hit son plafond UX). Décision prise lors de la session 2026-04-26.

## Ce qui a été construit

### 1. Cockpit web Next.js 15+ (Turbopack, Next 16.2)
**Location** : `/Users/paul/cockpit-web/`
**Lancement** : `cd /Users/paul/cockpit-web && PORT=3000 npm run dev`
**URL** : http://localhost:3000
**DB** : Supabase Postgres (mêmes credentials que `~/.brantham/cockpit.db` migré 04-26)

**Stack** :
- Next.js 16 App Router · React 19 · Tailwind 4 · TypeScript
- pg pool singleton, SWR cache, @tanstack/react-virtual
- Connexion Supabase via DATABASE_URL en env (server-only via `lib/db.ts`)

**5 onglets** : Opps · Pipeline · Deals · Finance · À faire (clone du TUI)

**Features câblées** :
- Tables virtualisées (gérent 459+ rows sans lag)
- Responsive avec column hiding par largeur (`hideUnder` per col)
- SWR keep-previous + dedup + revalidation
- Search debounced 250ms
- Action bus context (par onglet)
- Boutons inline par ligne (icon-only, compact)
- Toast feedback + undo (status/assign Opps)
- Modals : Note / NewTodo / AjFilter (multi-select)
- Lazy-load des onglets (next/dynamic)
- Mutations API : `/api/opps/[id]` POST + GET (drawer detail), `/api/deals/[id]` POST + GET + PATCH (édition inline), `/api/todos/[id]` POST, `/api/aj-sources`, `/api/scrape`, `/api/hunters` GET+POST

**Drawers détail** :
- **OppDrawer** (clic ligne Opps) : tout sur l'opp + section Repreneurs intégrée
- **DealDrawer** (clic ligne Pipeline/Deals) : édition inline fees/deadline/next action/notes + actions stage + section Repreneurs

### 2. Hunters v2 — module Python multi-sources
**Location** : `/Users/paul/Downloads/brantham-pipeline/cockpit/hunters_v2/`

**3-tier pipeline** :
1. **Tier 1 CURATED** : JSON files par NAF dans `curated_lists/` (acteurs majeurs hand-built)
2. **Tier 2 CONCURRENTS** : INSEE Sirene API (gratuit, illimité avec clé) — query NAF + dept + effectif >10
3. **Tier 3 ENRICH** : Pappers MCP (top 10) → CA, EBITDA, CEO, website
4. **Hunter.io** : email finder optionnel (utilisateur gère manuellement)

**Files créés** :
- `pipeline.py` — orchestrateur 3-tier + scoring + persist UPSERT
- `scoring_v2.py` — score multi-critères 0-100 (NAF/size/geo/tier/signals)
- `sources/insee.py` — Sirene API client (syntaxe `periode(activitePrincipaleEtablissement:93.13Z AND etatAdministratifEtablissement:A) AND (trancheEffectifsEtablissement:21 OR ...)`)
- `sources/curated.py` — JSON files par NAF avec fallback prefix
- `sources/pappers_wrap.py` — Pappers Pro API wrapper
- `sources/hunter_io.py` — email finder
- `curated_lists/93.13Z.json` — 12 chaînes fitness FR (Basic-Fit, Fitness Park, L'Orange Bleue, Keepcool, Neoness, Vita Liberté, On Air, CMG, Episod, MyClub, OneFit, Naveos)
- `SETUP.md` — doc clés API

**CLI** : `python3 -m cockpit.hunt_v2_one <opp_id>` (DB connection auto via DATABASE_URL env)

### 3. DB migration
`cockpit/migrations/004_hunters_v2.sql` (appliquée) — étend table `repreneurs` :
- `tier`, `email`, `ceo_name`, `linkedin_url`, `website`, `signals` (JSONB), `enrich_status`, `source_detail`

### 4. Daily scrape automatisé
- `daily_scrape.sh` (idempotent : import_scan dedup par id)
- `~/Library/LaunchAgents/com.brantham.daily-scrape.plist` (8h00 quotidien)
- `/api/scrape` POST → bouton "🔄 Scrape now" dans la barre Opps

### 5. RepreneursPanel — composant React partagé
`components/RepreneursPanel.tsx` réutilisé dans OppDrawer + DealDrawer pour cohérence design.

**UI** :
- Cards (pas table) — score badge gauche, tier badge, nom + CEO + NAF + dept + effectif, CA droite
- Mini-actions par card : ✉ mailto, 🌐 site, in LinkedIn (ou 🔍 google search fallback), AE annuaire entreprises
- Click card → expand : rationale + score breakdown + signals + SIREN + date
- Filtres tier en pills (Tous / ★ Curated / Concurrents / INSEE)
- État vide informatif avec liste à puce
- Spinner animé pendant hunt
- Toast statistique : "🎯 50 candidats · 12 curated · 38 concurrents · 10 enrichis"

## Configuration

`.env` dans `/Users/paul/Downloads/brantham-pipeline/` :
```
DATABASE_URL=postgresql://postgres.qjjrsxjmbcizusgvoxou:...@aws-0-eu-west-1.pooler.supabase.com:6543/postgres
INSEE_API_KEY=2ef32b9e-91d9-40be-b32b-9e91d990bebd  # configured 2026-04-27
HUNTER_IO_KEY=  # user gère manuellement
PAPPERS_API_KEY=  # optionnel — sinon MCP gratuit
```

`cockpit-web/.env.local` : `DATABASE_URL=...` (même credential)

## Tests réels effectués
- INSEE Sirene API marche : NAF 93.13Z + tranche 21+ retourne Basic-Fit France (SIREN 798233011) + Wellness Training
- Curated list 93.13Z chargée : 12 entries (Basic-Fit, Fitness Park, etc.)
- DB migration appliquée OK
- Tous endpoints Next 200
- Hunters v1 ancien (`hunt_one.py`) remplacé par v2 dans `/api/hunters`

## Reste à faire / pending
1. **launchctl load** par l'user : `launchctl load ~/Library/LaunchAgents/com.brantham.daily-scrape.plist`
2. **Test hunt v2 réel** depuis l'UI sur Magic Form Levallois (NAF 93.13Z exact match)
3. **Curated lists** pour les autres NAFs au fur et à mesure des deals (boulangerie, restauration, hôtellerie, transport...)
4. **Auth** : l'app est ouverte sur localhost — Soren ne peut pas l'utiliser. Clerk + Vercel deploy à faire.
5. **Server Components RSC** pour first paint (deferred — SWR client suffit)

## Décisions
- BODACC retiré de la stack (signal trop faible vs noise)
- Hunter.io & emails : user gère hors-app (pas de wiring obligatoire)
- LinkedIn : pas d'API gratuite légale, on s'arrête à google search fallback
- Pas de bypass paid services (Pappers/LinkedIn) — stack 100% légale + free

## Related
- [[brantham/_MOC]]
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/cockpit/cockpit-web]] (à créer)
- [[brantham/patterns/hunters-v2-3-tier]] (à créer)
