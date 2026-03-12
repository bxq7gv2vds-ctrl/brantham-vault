---
type: reference
project: brantham
updated: 2026-03-12
component: dashboard
---

# Dashboard -- Map of Content

Interface de pilotage Brantham Partners. Implementation dans `/Users/paul/internal-tool/`.

## Stack

| Technology | Version |
|---|---|
| React | 19 |
| TypeScript | 5.9 |
| Vite | 7 |
| Zustand | 5 |
| React Router | 7 |

## Routes

| Route | Description |
|---|---|
| `/dashboard` | Vue d'ensemble, KPIs, top opportunites |
| `/agents` | Statut des 6 agents, activite recente |
| `/pipeline` | Pipeline des deals (kanban par statut) |
| `/veille` | Feed BODACC, nouvelles procedures |
| `/analyse` | Analyses M&A en cours et terminees |
| `/chat` | Chat avec agent2 (assistant M&A) |
| `/office` | Espace de travail documents |
| `/memory` | Vue du vault et de la memoire partagee |
| `/dossier/:slug` | Fiche dossier detaillee (analyse, teaser, matching) |

## State Management (Zustand)

| Store | Responsabilite |
|---|---|
| `useOpportunitiesStore` | Liste des opportunites, filtres, tri, selection |
| `useUIStore` | Theme, sidebar, modals, notifications |
| `useAgentsStore` | Statut agents, activite, logs |
| `useChatStore` | Historique chat, messages, streaming |

## Design Tokens

| Token | Valeur | Usage |
|---|---|---|
| `white` | `#FAFAF8` | Background principal |
| `off` | `#F4F3F0` | Background secondaire, cards |
| `ink` | `#0F0F0E` | Texte principal |
| `red` | `#C8251A` | Accents, alertes, CTA |
| `indigo` | `#5E54F0` | Liens, elements interactifs |

> **Pas de violet/purple.** Design sobre, professionnel, M&A.

## Typographie

| Font | Poids | Usage |
|---|---|---|
| DM Sans | 300, 400, 500, 600 | Corps de texte, UI |
| DM Mono | 300, 400, 500 | Code, donnees, scores |
| Instrument Serif | italic | Titres, accroches |

## Data Flow

```
[FastAPI Backend]
       |
       |--- GET OPPORTUNITIES.json (polling 8s)
       |--- GET activity.json (polling 6s)
       |--- SSE /api/stream (real-time events)
       |
[Zustand Stores]
       |
[React Components]
```

- **Polling**: OPPORTUNITIES.json toutes les 8 secondes, activity.json toutes les 6 secondes
- **SSE**: `/api/stream` pour evenements real-time (nouveau deal, agent status change, QC result)

## API Endpoints

Voir [[brantham/dashboard/api-endpoints]] pour la reference complete (26+ endpoints).

### Categories

- Pipeline (4 endpoints)
- Deals (5 endpoints)
- Market Intel (6 endpoints)
- Knowledge (4 endpoints)
- NAF (4 endpoints)
