---
type: strategy
created: 2026-03-16
updated: 2026-03-16
project: internal-tool
status: active
---

# Web App (internal-tool) — Roadmap

---

## Etat actuel (mars 2026)

| Metrique | Valeur |
|----------|--------|
| Pages | 13 (Dashboard, Pipeline, Veille, Agents, Dossier, Chat, Office, Memory, Analyse, Activity, Suivi, Repreneur, Swarm) |
| Components | 28 |
| Stores Zustand | 5 (agents, opportunities, ui, chat, sync) |
| LOC pages | ~6 870 |
| LOC components | ~7 340 |
| LOC total (src/) | ~15K |
| Stack | React 19, Vite 7, TypeScript 5.9, Zustand 5, React Router 7, Tailwind |
| Tests | 0 |
| Mobile | Non responsive |
| Auth | LoginScreen cosmetic (pas de vrai auth) |
| Maturite globale | ~60% |

### Ce qui marche bien
- Pipeline drag-and-drop (colonnes Kanban)
- Chat agents conversationnel
- Activity feed SSE temps reel
- Status transitions sur Dossier
- Agents page (6 agents, avatars, cards, drawer)
- Sidebar navigation fluide
- Swarm page (nouveau, 3 tabs)
- Veille avec scoring + filtres + appel agents

### Ce qui est casse ou incomplet
- **DossierPage** : monolithe 1206 lignes, RepreneurMatchWidget importe mais jamais affiche correctement, analyse progress fragile
- **DashboardPage** : graphiques vides (hasChartData = false), KPI calculs dependants de data
- **OfficePage** : canvas cosmetique, pas de vraie fonctionnalite
- **MemoryPage** : affichage basique, pas d'edition
- **AnalysePage** : dependance backend dataroom pas toujours disponible
- **RepreneurPage** : table basique, pas de filtres avances
- **SuiviPage** : liste simple, pas de stats

---

## Phase 1 — STABILISATION (Sprint 1-2)

Rendre fiable ce qui existe. Zero nouvelles features.

| Tache | Detail | Fichiers | Effort |
|-------|--------|----------|--------|
| **Splitter DossierPage** | Decomposer le monolithe 1206 lignes en sous-composants: DossierHeader, DossierAnalyse, DossierTeaser, DossierContacts, DossierEmails, DossierDataroom, DossierNotes | `DossierPage.tsx` → 7 fichiers dans `components/dossier/` | 1j |
| **Fixer Dashboard charts** | Remplacer la logique `hasChartData` par des vraies visualisations (recharts ou chart.js). 4 charts: pipeline par status, score distribution, timeline cessions, fees potentiels | `DashboardPage.tsx` | 0.5j |
| **RepreneurMatchWidget visible** | Le widget est importe dans DossierPage mais jamais rendu correctement. Connecter au vrai endpoint `/api/repreneurs/match/{slug}` | `DossierPage.tsx`, `RepreneurMatchWidget.tsx` | 0.5j |
| **Error boundaries** | Ajouter un ErrorBoundary global + par page. Actuellement un crash dans un composant casse toute l'app | `components/ui/ErrorBoundary.tsx`, `AppLayout.tsx` | 0.5j |
| **Loading states** | Ajouter des skeletons/spinners pour toutes les pages qui fetchent de la data. Beaucoup de pages flashent vide avant load | Toutes les pages | 0.5j |
| **Fix analyse progress** | Le tracking des etapes d'analyse (5 steps) est fragile — dependance sur keywords dans le stream. Refactorer avec un vrai state machine | `DossierPage.tsx` → `components/dossier/DossierAnalyse.tsx` | 0.5j |
| **API error handling** | Ajouter try/catch + toast notifications sur tous les appels API. Actuellement les erreurs sont silencieuses | `lib/api.ts`, pages | 0.5j |

**Critere de sortie** : toutes les pages loadent sans crash, data visible, erreurs catchees.

---

## Phase 2 — POLISH UI (Sprint 3-4)

L'app doit avoir l'air professionnel.

| Tache | Detail | Fichiers | Effort |
|-------|--------|----------|--------|
| **Responsive mobile** | Sidebar collapsible, tables → cards sur mobile, breakpoints Tailwind sm/md/lg sur toutes les pages. Actuellement score mobile 2/10 | Toutes les pages + `Sidebar.tsx`, `Topbar.tsx` | 2j |
| **Table component reutilisable** | Creer un composant `<DataTable>` avec tri, pagination, filtres. Actuellement chaque page reimplemente ses propres tables | `components/ui/DataTable.tsx` → utilise dans Veille, Pipeline, Repreneur, Suivi | 1j |
| **Dark mode** | Tailwind dark: classes. Toggle dans Topbar. Persistance localStorage | Toutes les pages, `uiStore.ts` | 1j |
| **Keyboard shortcuts** | `Ctrl+K` command palette (recherche globale deals + agents + pages). Navigation rapide | `components/ui/CommandPalette.tsx`, `AppLayout.tsx` | 1j |
| **Transitions et animations** | Page transitions (fade), list animations (stagger), modal enter/exit. Actuellement tout est instantane et brut | CSS + framer-motion ou Tailwind transitions | 0.5j |
| **Typographie coherente** | Audit et normaliser: heading sizes, spacing, font weights. Quelques inconsistances entre pages | Tailwind config + pages | 0.5j |
| **Toast system upgrade** | Le Toast.tsx existe mais basique. Ajouter: types (success/error/warning), auto-dismiss configurable, stack multiple | `components/ui/Toast.tsx` | 0.5j |
| **Empty states** | Chaque liste/table vide doit avoir un empty state design (illustration + CTA). Actuellement: vide = rien | Toutes les pages avec listes | 0.5j |

**Critere de sortie** : score mobile 7/10, look professionnel, navigation fluide.

---

## Phase 3 — FEATURES CORE (Sprint 5-8)

Nouvelles fonctionnalites business-critical.

| Tache | Detail | Fichiers | Effort |
|-------|--------|----------|--------|
| **Dashboard V2** | Refonte complete: 4 KPI cards cliquables, pipeline funnel chart, heatmap activite semaine, top 5 deals par score, agents status ring, revenue tracker (fees potentiels) | `DashboardPage.tsx` refonte | 2j |
| **Dataroom page** | Upload PDF/Excel dans un dossier, extraction auto KPIs (via backend agent), visualisation documents, preview inline | `pages/DataroomPage.tsx`, route `/dossier/:slug/dataroom` | 2j |
| **Email composer** | EmailModal existe (819 lignes!) mais needs upgrade: templates pre-remplis (teaser, relance, intro acheteur), preview HTML, tracking ouverture, historique par contact | `EmailModal.tsx` refonte, `components/email/` | 2j |
| **Repreneur V2** | Filtres avances (secteur, taille, geo, historique acquisitions), vue carte geographique, scoring 4D visible, export CSV, detail page par repreneur | `RepreneurPage.tsx` refonte, `pages/RepreneurDetailPage.tsx` | 2j |
| **Notifications center** | Bell icon Topbar, dropdown notifications: nouveau deal score 65+, agent termine, email reponse, deadline proche. SSE depuis backend | `components/ui/NotificationCenter.tsx`, `Topbar.tsx`, `store/notificationStore.ts` | 1j |
| **Suivi V2** | Timeline complete par deal: toutes les actions (agent runs, emails envoyes, reponses, status changes). Vue calendrier optionnelle | `SuiviPage.tsx` refonte | 1j |
| **Search global** | Full-text search across deals, repreneurs, agents, emails. Resultats groupes par type. Endpoint backend `/api/search` | `components/ui/CommandPalette.tsx` upgrade | 1j |
| **Bulk actions** | Multi-select sur Pipeline et Veille: changer status, assigner agent, exporter. Checkbox + action bar | `PipelinePage.tsx`, `VeillePage.tsx` | 1j |

**Critere de sortie** : toutes les fonctionnalites metier utilisables au quotidien.

---

## Phase 4 — SWARM INTEGRATION (Sprint 9-10)

Connecter le swarm dans toute l'app.

| Tache | Detail | Fichiers | Effort |
|-------|--------|----------|--------|
| **Swarm badge partout** | Sur chaque deal card/row: mini badge swarm (BUY/WATCH/PASS) avec couleur. Visible dans Pipeline, Veille, Dashboard, Dossier | `components/deal/SwarmBadge.tsx`, toutes les pages deal | 1j |
| **Dossier tab Swarm** | Onglet dans DossierPage: predictions swarm pour CE deal specifique, timeline des agents, bids, profil acheteurs les plus probables | `components/dossier/DossierSwarm.tsx` | 1j |
| **Ensemble scoring visible** | Afficher le score ensemble (quant 70% + swarm 30%) a cote du score 9D existant. Tooltip decomposition par modele | `components/deal/ScoreBadge.tsx` upgrade | 0.5j |
| **Swarm auto-run** | Lancer le swarm automatiquement sur les top 50 deals chaque nuit (cron). Resultats pre-calcules, pas de run manual necessaire | Backend cron + `SwarmPage.tsx` mode "latest results" | 1j |
| **Swarm comparison** | Page comparaison: quant predictions vs swarm predictions vs ensemble. Scatter plot, correlation, delta per deal | `pages/SwarmPage.tsx` tab "Comparison" | 1j |

**Critere de sortie** : le swarm est visible et utile dans le workflow quotidien.

---

## Phase 5 — ROBUSTESSE (Sprint 11-12)

L'app doit etre fiable pour un usage intensif.

| Tache | Detail | Fichiers | Effort |
|-------|--------|----------|--------|
| **Tests E2E** | Playwright tests sur les 5 flows critiques: login → dashboard, pipeline drag-drop, dossier → analyse → teaser, swarm run, email send | `tests/e2e/` | 2j |
| **Tests unitaires** | Vitest sur stores, utils, dealStatus, api calls. Coverage > 60% sur lib/ | `tests/unit/` | 1j |
| **Auth reelle** | Remplacer LoginScreen cosmetique par un vrai auth: JWT + refresh token. Proteger routes. Session timeout | `lib/auth.ts`, `components/auth/`, middleware backend | 2j |
| **Offline resilience** | Les stores Zustand persistent en localStorage (zustand/middleware persist). L'app fonctionne partiellement offline | Tous les stores | 0.5j |
| **Performance** | Lazy load toutes les pages (pas juste 3). Virtualiser les longues listes (react-virtual). Memoize les calculs lourds dans Dashboard | Routes, pages avec listes | 1j |
| **Accessibilite** | Audit WCAG: focus management, aria labels, keyboard navigation complete. Score actuel 3/10, cible 7/10 | Toutes les pages | 1j |
| **Logging frontend** | Capturer les erreurs JS + API failures vers un endpoint `/api/frontend-logs`. Debug en prod sans console | `lib/logger.ts`, `ErrorBoundary.tsx` | 0.5j |

**Critere de sortie** : zero crash en 7 jours d'usage intensif, tests green.

---

## Phase 6 — AVANCEE (Q3 2026+)

Features differenciantes.

| Tache | Detail | Effort |
|-------|--------|--------|
| **Multi-user** | Roles (admin, analyst, viewer), permissions par page, audit log des actions. Prerequis: auth reelle | 3j |
| **Mandataire portal** | Vue dediee pour les AJ/MJ: leurs dossiers, acheteurs identifies, rapports generes. Login separe, branding neutre | 5j |
| **Real-time collab** | Curseurs partages sur DossierPage (Liveblocks ou Y.js). Notes collaboratives | 3j |
| **AI copilot** | Chat sidebar contextuel: "analyse ce deal", "trouve des acheteurs similaires", "compare avec deal X". Claude API direct | 3j |
| **PWA** | Service worker, install prompt, push notifications, icone dock. L'app tourne depuis l'ecran d'accueil mobile | 2j |
| **Export reports** | Generer PDF de l'analyse complete (DossierPage → PDF), export pipeline Excel, rapport mandataire auto | 2j |
| **Dashboard customizable** | Drag-and-drop widgets, chaque utilisateur configure son dashboard. GridStack ou react-grid-layout | 3j |
| **Analytics** | Mixpanel/Posthog embedded: tracking usage par page, temps passe par deal, conversion funnel | 1j |

---

## Priorite globale

```
Phase 1 (STABILISATION)    ████████████ NOW — critique
Phase 2 (POLISH)           ████████████ Sprint 3-4
Phase 3 (FEATURES)         ████████████████████ Sprint 5-8
Phase 4 (SWARM)            ██████████ Sprint 9-10
Phase 5 (ROBUSTESSE)       ██████████ Sprint 11-12
Phase 6 (AVANCEE)          ████████████████████████████ Q3 2026+
```

**Effort total estime** : ~55 jours de dev (Phases 1-5), ~22 jours (Phase 6).

---

## Fichiers les plus critiques a refactorer

| Fichier | LOC | Probleme | Priorite |
|---------|-----|----------|----------|
| `DossierPage.tsx` | 1206 | Monolithe, logique mixte UI/data/state | P0 |
| `RapportAnalyse.tsx` | 1351 | Le plus gros composant, hard-coded | P1 |
| `VeillePage.tsx` | 886 | Trop dense, needs pagination + filtres | P1 |
| `DrawerDossier.tsx` | 895 | Duplique de la logique DossierPage | P1 |
| `EmailModal.tsx` | 819 | Templates hard-coded, pas de preview | P2 |
| `ModalLaunch.tsx` | 657 | Complex state, needs simplification | P2 |
| `RepreneurPage.tsx` | 627 | Basique, needs filtres avances | P2 |
| `ModalAnalyseAj.tsx` | 541 | Scraping UI, tightly coupled | P3 |

---

## Tech debt actuel

| Probleme | Impact | Fix dans |
|----------|--------|----------|
| 0 tests | Regressions silencieuses | Phase 5 |
| Pas de lazy loading (10/13 pages eager) | Bundle size, first load | Phase 5 |
| LoginScreen cosmetique (pas de vrai auth) | Pas de securite | Phase 5 |
| Pas d'error boundaries | Un crash = app morte | Phase 1 |
| Tables reimplementees N fois | Inconsistance, maintenance | Phase 2 |
| Pas de mobile responsive | Inutilisable sur telephone | Phase 2 |
| mockData.ts importe dans certaines pages | Data reelle vs mock confusion | Phase 1 |
| Console.log residuels | Bruit en prod | Phase 5 |

---

*Derniere mise a jour : 16 mars 2026*

## Related
- [[brantham/_MOC]]
