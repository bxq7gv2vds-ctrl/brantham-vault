---
type: reference
project: brantham
updated: 2026-03-12
component: agents
---

# Agent Network -- Map of Content

Reseau de 6 agents LLM orchestres par le Director. Implementation dans `/Users/paul/Downloads/brantham-pipeline/` (server.js).

## Les 6 Agents

| Agent | Role | LLM | QC Threshold |
|---|---|---|---|
| **Director** | Orchestrateur, QC, decisions go/no-go | claude-opus-4 | N/A (decideur) |
| **Scout** | Veille BODACC, detection opportunites | claude-haiku-4 | N/A (feed) |
| **Analyst** | Analyse M&A, due diligence light | claude-sonnet-4 | 7/10 |
| **Writer** | Redaction teaser PPTX anonymise | claude-sonnet-4 | 7/10 |
| **Hunter** | Mapping acheteurs potentiels | claude-sonnet-4 | 7/10 |
| **Enricher** | Validation contacts, enrichissement donnees | claude-haiku-4 | 6/10 |

## Flow Standard

```
Scout (veille BODACC)
    |
    v
Director (score + decision)
    |
    v
Analyst (analyse M&A)
    |
    v
Writer + Hunter (parallele)
    |         |
    v         v
   Enricher (validation contacts)
    |
    v
Director (QC final)
```

1. **Scout** detecte une nouvelle procedure via BODACC
2. **Director** evalue le score, decide go/no-go (seuil 60+)
3. **Analyst** produit une analyse M&A structuree (secteur, actifs, risques, valorisation)
4. **Writer** et **Hunter** travaillent en parallele:
   - Writer redige le teaser anonymise (PPTX)
   - Hunter identifie 10-20 repreneurs potentiels (A/B/C scoring)
5. **Enricher** valide les contacts des repreneurs (email, telephone, decision-maker)
6. **Director** fait le QC final sur tous les livrables

## Quality Control

| Agent | Seuil QC | Si echec |
|---|---|---|
| Analyst | 7/10 | Renvoi avec feedback, max 2 retries |
| Writer | 7/10 | Renvoi avec corrections specifiques |
| Hunter | 7/10 | Renvoi pour elargir/affiner mapping |
| Enricher | 6/10 | Renvoi pour completer contacts manquants |

## Shared Memory

Fichiers partages entre agents dans `/Users/paul/Downloads/brantham-pipeline/`:

| Fichier | Role |
|---|---|
| `BRAIN.md` | Etat global du systeme, context partage |
| `PIPELINE.md` | Tracking des deals en cours (statuts, blocages) |
| `OPPORTUNITIES.md` | Feed des opportunites detectees par Scout |
| `SOUL.md` | Personnalite et ton des agents (M&A professionnel) |
| `HEARTBEAT.md` | Protocole de wake-up et health check |

## Director Rules

- **Max 2 analyses simultanees** (pour eviter surcharge LLM)
- **Max 3 deals actifs** en parallele
- **Priorite LJ** (liquidation judiciaire = urgence, deadlines courtes)
- Escalation automatique si deadline < 7 jours

## Agent Workspaces

Chaque agent a un repertoire de travail par deal:

```
/brantham-pipeline/
  agents/
    director/
      IDENTITY.md
    scout/
      IDENTITY.md
    analyst/
      IDENTITY.md
      workspaces/
        {deal-slug}/
    writer/
      IDENTITY.md
      workspaces/
        {deal-slug}/
    hunter/
      IDENTITY.md
      workspaces/
        {deal-slug}/
    enricher/
      IDENTITY.md
      workspaces/
        {deal-slug}/
```

`IDENTITY.md` contient les instructions specifiques de chaque agent (role, ton, limites, exemples).
