---
type: reference
project: brantham
updated: 2026-03-12
component: api
---

# API Endpoints Reference

FastAPI backend dans `/Users/paul/Desktop/brantham-partners/api/`. 26+ endpoints groupes par categorie.

---

## Pipeline

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/shared/OPPORTUNITIES.json` | Liste des opportunites actives (polled toutes les 8s) |
| GET | `/api/shared/activity.json` | Activite recente des agents (polled toutes les 6s) |
| GET | `/api/stream` | SSE stream d'evenements real-time |
| PATCH | `/api/opportunities/{id}/statut` | Mise a jour du statut d'une opportunite |

---

## Deals

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/deals/{slug}/launch-analyse` | Lancer l'analyse M&A par l'Analyst |
| GET | `/api/deals/{slug}/analyse-status` | Statut de l'analyse en cours |
| POST | `/api/deals/{slug}/generate-teaser` | Generer le teaser PPTX via Writer |
| POST | `/api/deals/{slug}/upload` | Upload de documents au dossier |
| GET | `/api/deals/{slug}/matching-repreneurs` | Liste des repreneurs matches pour ce deal |

---

## Market Intel

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/marche/kpis` | KPIs marche (volumes, tendances, taux cession) |
| GET | `/api/marche/volumes` | Volumes de procedures par periode |
| GET | `/api/secteurs/heatmap` | Heatmap sectorielle (stress index par NAF) |
| GET | `/api/tribunaux` | Statistiques par tribunal de commerce |
| GET | `/api/mandataires` | Statistiques par mandataire judiciaire |
| GET | `/api/procedures` | Liste et filtrage des procedures collectives |

---

## Knowledge

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/map/vault-deals` | Carte des deals dans le vault |
| POST | `/api/map/sync` | Synchronisation du vault |
| POST | `/api/agent2/chat` | Chat avec l'assistant M&A (agent2) |
| POST | `/api/agent2/summarize` | Resume automatique d'un dossier |

---

## NAF (Classification Sectorielle)

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/naf/adjacent` | Secteurs NAF adjacents (synergies potentielles) |
| GET | `/api/naf/search` | Recherche dans la nomenclature NAF |
| GET | `/api/naf/distance` | Distance sectorielle entre deux codes NAF |
| GET | `/api/naf/infer` | Inference du code NAF depuis description |

---

## Notes Techniques

- Toutes les reponses en JSON
- Authentification: a implementer (actuellement dev-only)
- Rate limiting: a implementer avant prod
- CORS: restreint en prod aux domaines autorises
- SSE stream: connexion persistante, events `deal_update`, `agent_status`, `qc_result`, `pipeline_step`
