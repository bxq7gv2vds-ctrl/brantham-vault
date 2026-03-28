---
title: Roadmap Brantham Data Platform — 2026
type: strategy
date: 2026-03-28
tags: [roadmap, platform, distressed-ma, intelligence]
---

# Roadmap Brantham Data Platform — 2026

## Vision

La plateforme la plus précise et actionnable sur les procédures collectives françaises. Cible : les fonds distressed, restructureurs, acheteurs d'actifs — qui ont besoin d'un signal fiable, rapide, et contextualisé sur 180K+ dossiers actifs.

---

## ✅ Livré — Sprint 1-3 (mars 2026)

### Infrastructure data
- [x] Pipeline quotidien complet (BODACC → SIRENE → Scores → Stats → Macro → EW → IBSE → Analytics)
- [x] 43 tables, 1.8M annonces, 184K procédures, 194K bilans
- [x] Score de qualification 0-100 (9 composantes)
- [x] Full-text search PostgreSQL ts_vector + GIN index — `007_fts.sql`
- [x] Cache API corrigé (TTL par entrée, plus de bug silencieux)

### Frontend SPA
- [x] 7 pages : Briefing, Volumes, Secteurs, Géo, M&A, Acteurs, Scoring
- [x] Fiche procédure complète (timeline, bilans, comparables, scoring détaillé, waterfall VE)
- [x] Search avancée + export CSV
- [x] Freemium gating (FREE/PREMIUM, watchlist, Cmd+K)
- [x] Dark mode complet
- [x] Kanban pipeline M&A (drag & drop, localStorage)
- [x] Alertes configurables (simulation, dispatch email)
- [x] Page Transactions + Reports (Deal Memo PDF)
- [x] **Zéro dépendances charts** — 35 SVG custom (ApexCharts supprimé, -1.2MB)
- [x] Service Worker + PWA (cache-first)

### API
- [x] 26 endpoints FastAPI
- [x] Rate limiting (120 req/60s sliding window)
- [x] Email alerts + digest via Resend (httpx REST, zéro SDK supplémentaire)
- [x] `/api/pipeline/trigger` avec auth Bearer

### Qualité / Infra
- [x] Test suite pytest (31 tests smoke + validation)
- [x] GitHub Actions : daily pipeline (cron 5h30 UTC) + tests sur PR
- [x] Vercel headers moderne (cache, security, no legacy `routes`)

---

## 🔴 Sprint 4 — Auth & Billing (priorité max)

**Objectif : premier abonnement payant**

### Auth réelle (Clerk ou Supabase Auth)
- [ ] Remplacer le freemium localStorage par une vraie session JWT
- [ ] Login/Register UI (modal ou page dédiée)
- [ ] `user_id` sur chaque requête API → Row-Level Security PostgreSQL
- [ ] Plans : FREE (3 résultats search), STARTER (100/mois), PRO (illimité + exports)

### Stripe billing
- [ ] Webhook `/api/billing/webhook` (signature vérifiée)
- [ ] `subscription_status` dans DB → propagé au frontend
- [ ] Upgrade flow in-app (modal → Stripe Checkout)
- [ ] Customer portal (auto-géré via Stripe)

### Environnement prod séparé
- [ ] Variables d'env prod vs staging (Vercel env vars)
- [ ] DB prod séparée (Railway ou Supabase)
- [ ] Seed script pour démo sans données réelles

---

## 🟠 Sprint 5 — Intelligence & ML

**Objectif : moat data — ce que Bloomberg ne peut pas faire**

### Scoring ML (LightGBM)
- [ ] Feature engineering sur historique procédures clôturées
- [ ] Variables cibles : issue (plan/cession/liquidation), durée, taux de recouvrement
- [ ] Train sur 5 ans BODACC (2019-2024), validation temporelle
- [ ] Remplacer score heuristique par proba ML + intervalle confiance
- [ ] SHAP values pour expliquer le score (affichage dans fiche)

### NLP BODACC
- [ ] Extraction automatique d'actifs depuis texte BODACC (regex + spaCy)
- [ ] Tags : `immobilier`, `fonds_commerce`, `marques`, `machines`, `stocks`
- [ ] Filtres dans Search : "avec actifs immobiliers", "avec marques déposées"
- [ ] Alertes sur keywords dans nouvelles annonces

### Signal précoce (T-90)
- [ ] Veille sur annonces légales hors BODACC (INPI dépôts, RNCS modifications)
- [ ] Indicateur pré-difficulté : RCS modifications capital + mandataires nommés avant procédure
- [ ] Agrégation Pappers/Société.com pour crosscheck données

---

## 🟡 Sprint 6 — Collaboration & Workflow

**Objectif : devenir l'outil de travail quotidien des équipes**

### CRM distressed intégré
- [ ] Module "Deal room" : fiches procédure avec notes d'équipe, statut custom, contacts
- [ ] Assignation deals à des membres (accès multi-user)
- [ ] Historique d'actions (viewed, noted, passed, bid)
- [ ] Sync Notion/HubSpot (webhook sortant)

### Partage & collaboration
- [ ] Partage de fiche procédure par lien (token temporaire, vue publique limitée)
- [ ] Export Deal Memo en vrai PDF (Puppeteer serverless ou WeasyPrint)
- [ ] Rapport hebdo automatique par email (digest top 10 opportunités)

### Webhooks sortants
- [ ] `webhook_url` sur chaque alert_config
- [ ] Payload JSON standardisé → Slack/Teams/Zapier
- [ ] Retry logic avec backoff exponentiel

---

## 🟢 Sprint 7 — Scale & Monitoring

**Objectif : zéro downtime, observabilité complète**

### Monitoring
- [ ] Sentry (erreurs JS + Python) avec `SENTRY_DSN`
- [ ] Uptime check (BetterUptime ou UptimeRobot sur `/api/health`)
- [ ] Dashboard Grafana : latence API, count requêtes, erreurs 5xx
- [ ] Alertes PagerDuty si pipeline échoue

### Performance DB
- [ ] Partitioning `procedure_collective` par année (`date_jugement_ouverture`)
- [ ] Materialized views refresh parallèle
- [ ] Connection pooling PgBouncer (actuellement asyncpg direct)
- [ ] VACUUM + ANALYZE automatique sur tables chaudes

### API v2
- [ ] Versioning `/api/v2/` avec deprecation notices
- [ ] Pagination cursor-based (remplace OFFSET pour grandes collections)
- [ ] GraphQL endpoint optionnel (Strawberry) pour requêtes flexibles côté client
- [ ] SDK Python client (pour intégrations custom chez clients)

---

## 🔵 Sprint 8+ — Expansion

**Objectif : autres marchés, autres produits**

### Données complémentaires
- [ ] Intégration Altares/Creditsafe pour scoring financier temps réel
- [ ] Orbis/Dealroom pour M&A context (comparables secteur, multiples récents)
- [ ] Flux RSS tribunaux de commerce (scraping légal)
- [ ] Données cadastrales pour actifs immobiliers identifiés

### Internationalisation
- [ ] Belgique (BCE + SECAL)
- [ ] Espagne (BORME + Registro Mercantil)
- [ ] Italie (CCIAA + Fallimenti)
- [ ] Interface EN + DE

### Produits adjacents
- [ ] API publique documentée (Swagger + sandbox) → clients directs (banques, cabinets avocats)
- [ ] White-label pour cabinets de conseil en restructuration
- [ ] Flux de données brut (pour hedge funds qui construisent leur propre modèle)

---

## KPIs cibles 2026

| Métrique | Aujourd'hui | Q2 2026 | Q4 2026 |
|---|---|---|---|
| Procédures indexées | 184K | 200K | 220K |
| Précision score | heuristique | AUC 0.78 | AUC 0.84 |
| Latence API p95 | ~200ms | <100ms | <50ms |
| Uptime | ~95% | 99.5% | 99.9% |
| Abonnés payants | 0 | 10 | 50 |
| ARR | 0 | 15K€ | 75K€ |

---

## Décisions d'architecture prises

| Décision | Rationale |
|---|---|
| Single-file SPA | Déploiement Vercel statique, zéro infra JS |
| Zéro dépendances charts | -1.2MB, contrôle total, pas de CVE ApexCharts |
| httpx pour Resend | Pas de SDK supplémentaire, déjà dans stack |
| ts_vector GIN | Full-text natif PG, plus rapide qu'ILIKE sur 200K+ rows |
| LightGBM vs Neural | Interprétable (SHAP), fast to train, bon sur tabular |

---

## Related

- [[brantham/_MOC]]
- [[brantham/strategy]]
- [[brantham/sessions/2026-03-28]]
- [[_system/MOC-decisions]]
