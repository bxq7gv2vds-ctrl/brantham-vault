---
type: strategy
created: 2026-03-17
updated: 2026-03-17
project: mirofish-oasis
status: active
priority: high
---

# MiroFish — Vision: Simulateur de Monde M&A Distressed

---

## Ce que c'est

MiroFish n'est PAS un prediction market. C'est un **simulateur d'environnement virtuel** qui reproduit le marche M&A distressed francais a grande echelle avec des agents autonomes.

**Analogie** : SimCity pour le M&A distressed. Un monde virtuel ou des milliers/millions d'agents (repreneurs, mandataires, tribunaux, banques, salaries) vivent, interagissent, prennent des decisions — et ou des patterns emergents revelent des verites sur le marche reel.

---

## Principes fondamentaux

1. **Environnement virtuel** — pas des agents qui votent, un MONDE qui tourne
2. **Agents autonomes** — chaque agent a un etat, une memoire, des strategies qui evoluent
3. **Decisions basees sur filtres/parametres** — les regles du monde sont configurables
4. **Echelle massive** — milliers a millions d'agents, pas 25-50
5. **Conclusions emergentes** — le produit c'est les milliers de conclusions qu'on tire des simulations, pas un score unique

---

## L'environnement

Le monde simule reproduit la realite du M&A distressed en France :

- **70 000 procedures/an** injectees dans l'environnement (basees sur data reelle BODACC)
- **Entreprises** avec attributs reels : secteur NAF, CA, effectif, localisation, type de procedure (RJ/LJ/SV), passif, actifs, causes de defaillance
- **Temps** qui avance : les procedures evoluent (observation → plan/cession/liquidation), les deadlines expirent, les offres arrivent
- **Contraintes legales** : delais legaux, role du tribunal, conditions de cession (maintien emploi, prix minimum)
- **Flux d'information** : qui sait quoi, quand (asymetrie d'info realiste)
- **Conditions macro** : taux d'interet, confiance PME, defaillances sectorielles

---

## Les agents (milliers/millions)

### Types d'agents

| Type | Nombre | Comportement |
|------|--------|-------------|
| **Repreneurs industriels** | Milliers | Cherchent acquisitions strategiques dans leur secteur |
| **Fonds PE / LBO** | Centaines | Tickets plus gros, criteres financiers stricts |
| **Family offices** | Centaines | Long terme, secteurs specifiques, conservateurs |
| **Serial acquirers** | Dizaines | Agressifs, multi-secteur, volume |
| **Mandataires judiciaires** | Centaines | Gerent les procedures, cherchent repreneurs, deadlines |
| **Tribunaux de commerce** | Dizaines | Valident/refusent les offres, criteres legaux |
| **Banques / creanciers** | Centaines | Interets financiers, negocient les dettes |
| **Salaries / CSE** | Milliers | Preference maintien emploi, poids dans les decisions |
| **Conseillers M&A** | Centaines | Intermediaires, mettent en relation |
| **Concurrents** | Variable | Reagissent aux acquisitions dans leur secteur |

### Architecture hybride (echelle)

- **99% agents legers** : rule-based, heuristics, decision trees — rapides, scalables
- **1% agents LLM** : qwen/llama local pour les decisions complexes (negociations, evaluations strategiques)
- Chaque agent a : etat, memoire, filtres de decision, contraintes, historique

---

## Filtres et parametres configurables

L'utilisateur configure le monde avant de lancer une simulation :

### Parametres macro
- Nombre de procedures/an (baseline: 70K, scenario crise: 120K)
- Taux d'interet / conditions de financement
- Confiance economique par secteur
- Taux de defaillance par secteur/region

### Filtres agents
- Distribution des types de repreneurs (plus de PE ? plus d'industriels ?)
- Capacite de capital par type
- Appetit sectoriel (sur-representation industrie vs tech)
- Agressivite / risk tolerance
- Contraintes geographiques

### Regles du monde
- Delais legaux (acceleres vs normaux)
- Criteres de validation tribunal (strict vs souple sur emploi)
- Niveau d'asymetrie d'information
- Couts de due diligence
- Friction de marche (temps pour trouver un repreneur)

---

## Conclusions extractibles (milliers)

Chaque simulation produit des conclusions sur :

### Dynamiques de marche
- Taux de cession par secteur/taille/region
- Delai moyen detection → cession
- Prix d'equilibre par type de deal
- Nombre moyen d'offres par deal
- Taux d'echec et causes

### Strategies optimales
- Quel profil de repreneur reussit le mieux sur quel type de deal ?
- Timing optimal pour faire une offre
- Prix optimal vs prix de marche
- Strategies gagnantes vs perdantes

### Scenarios what-if
- "Que se passe-t-il si les defaillances augmentent de 30% ?"
- "Impact d'une hausse des taux sur le marche M&A distressed ?"
- "Si on double le nombre de PE actifs, les prix montent de combien ?"
- "Effet d'un raccourcissement des delais legaux sur le taux de cession ?"

### Predictions sur deals reels
- Injecter un vrai deal dans l'environnement → observer comment les agents reagissent
- P(cession), profil acheteur probable, prix estime, timeline probable
- Plus fiable qu'un modele statistique car les interactions sont simulees

### Intelligence de marche
- Secteurs "chauds" (sur-demande) vs "froids" (sous-demande)
- Gaps geographiques (regions mal couvertes par les repreneurs)
- Inefficiences de marche (deals sous-evalues, niches non exploitees)
- Signaux avances de tendances

---

## Architecture technique cible

```
┌─────────────────────────────────────────────────┐
│              WORLD CONFIGURATOR                  │
│  Parametres macro, filtres agents, regles monde  │
│  UI: sliders, presets scenarios, custom configs   │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│           SIMULATION ENGINE                      │
│                                                  │
│  ┌──────────────┐  ┌─────────────────────────┐  │
│  │ ENVIRONMENT  │  │ AGENT POPULATION        │  │
│  │              │  │                         │  │
│  │ Time steps   │  │ Rule-based (99%)        │  │
│  │ Deal pool    │  │ LLM-powered (1%)        │  │
│  │ Info flow    │  │ State + memory          │  │
│  │ Legal rules  │  │ Decision filters        │  │
│  │ Macro vars   │  │ Interactions            │  │
│  └──────────────┘  └─────────────────────────┘  │
│                                                  │
│  ┌──────────────────────────────────────────┐   │
│  │ INTERACTION ENGINE                       │   │
│  │ Agent ↔ Agent, Agent ↔ Environment       │   │
│  │ Matching, negotiation, deal formation    │   │
│  └──────────────────────────────────────────┘   │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│           ANALYTICS ENGINE                       │
│                                                  │
│  Aggregation statistique sur N simulations       │
│  Pattern detection, clustering, anomalies        │
│  Scenario comparison (A vs B vs C)               │
│  Confidence intervals sur chaque conclusion      │
│                                                  │
│  Output: milliers de conclusions structurees     │
│  Format: filtrable, exportable, queryable        │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│           CONCLUSION EXPLORER                    │
│                                                  │
│  UI interactive pour explorer les conclusions    │
│  Filtres par secteur, taille, region, scenario   │
│  Drill-down: conclusion → agents → interactions  │
│  Export: rapports PDF, API, dashboards           │
└─────────────────────────────────────────────────┘
```

---

## Difference avec v0.1 actuel

| Aspect | v0.1 (actuel) | Vision MiroFish |
|--------|--------------|-----------------|
| Nature | Prediction market | Simulateur de monde |
| Agents | 25-50, LLM chacun | Milliers/millions, hybride |
| Decisions | BID/PASS sur deals | Strategies complexes, interactions |
| Output | P(cession) par deal | Milliers de conclusions |
| Parametres | Fixes | Configurables, scenarios |
| Environnement | Pas d'environnement | Monde complet avec regles |
| Echelle compute | ~40 min pour 25 agents | Secondes pour millions (rule-based) |
| Data input | Top 50 deals | 184K procedures + macro |

---

## Repo de reference : MiroFish (666ghj/MiroFish)

**URL** : https://github.com/666ghj/MiroFish.git
**Description** : "A Simple and Universal Swarm Intelligence Engine, Predicting Anything"
**Stars** : 30K+ | **License** : AGPL-3.0 | **Langue** : Python + TypeScript

### Ce que fait MiroFish

MiroFish est un moteur de prediction par simulation de monde. Le workflow :

1. **Seed input** — upload de data (rapport d'analyse, document, news)
2. **Graph construction** — extraction d'entites/relations, knowledge graph (GraphRAG + Zep memory)
3. **Environnement** — generation auto de profils agents, config de simulation via LLM
4. **Simulation** — double plateforme parallele (Twitter + Reddit simulees via OASIS), agents autonomes avec memoire long-terme
5. **Report** — ReportAgent interagit avec l'environnement post-simulation, genere un rapport de prediction
6. **Deep interaction** — dialogue avec n'importe quel agent du monde simule

### Architecture MiroFish

```
backend/
├── app/
│   ├── api/              # Endpoints (graph, report, simulation)
│   ├── config.py         # Config (LLM, Zep, paths)
│   ├── models/           # Project, Task dataclasses
│   ├── services/
│   │   ├── graph_builder.py              # Knowledge graph builder
│   │   ├── ontology_generator.py         # Ontologie entities/relations
│   │   ├── oasis_profile_generator.py    # Generation profils agents
│   │   ├── simulation_config_generator.py # Config auto via LLM
│   │   ├── simulation_runner.py          # Orchestration OASIS
│   │   ├── simulation_manager.py         # State management
│   │   ├── simulation_ipc.py            # Inter-process comm
│   │   ├── report_agent.py              # Generation rapport prediction
│   │   ├── text_processor.py            # Parsing documents
│   │   ├── zep_graph_memory_updater.py  # Memoire graph Zep
│   │   ├── zep_entity_reader.py         # Lecture entites Zep
│   │   └── zep_tools.py                 # Outils Zep
│   └── utils/
│       ├── llm_client.py   # Client LLM (OpenAI-compatible)
│       ├── file_parser.py  # Parser fichiers
│       └── logger.py
├── scripts/
│   ├── run_parallel_simulation.py  # Simulation parallele
│   ├── run_twitter_simulation.py   # Twitter sim
│   ├── run_reddit_simulation.py    # Reddit sim
│   └── action_logger.py           # Log actions agents
└── run.py
```

### Concepts cles a reprendre

| Concept MiroFish | Adaptation Brantham |
|---|---|
| Seed input (news, rapport) | Data BODACC + bilans + scoring 9D |
| Knowledge graph (Zep) | Graph procedures/entreprises/acteurs/tribunaux |
| Profils agents auto-generes | Profils investisseurs depuis PostgreSQL (143 reels + archetypes) |
| Simulation config via LLM | Config parametrable (macro, filtres agents, regles marche) |
| Double plateforme (Twitter + Reddit) | **Marketplace M&A** (deals, bids, offres, negotiations) |
| ReportAgent | Agent rapport de prediction M&A |
| Zep long-term memory | Memoire agents persistante entre simulations |
| GraphRAG | RAG sur knowledge graph M&A distressed |

### Stack MiroFish

| Composant | Techno |
|---|---|
| Backend | Python (uv), FastAPI |
| Frontend | TypeScript, Next.js |
| LLM | OpenAI SDK format (any provider) |
| Memory | Zep Cloud (graph memory) |
| Simulation engine | OASIS (camel-ai) |
| Knowledge graph | GraphRAG + Zep |

### Contrainte Python

MiroFish requiert Python >=3.11, <=3.12. Notre backend est en 3.14. **MiroFish doit tourner dans un venv separe** ou on monte la version de compat.

---

## Le moat

Le simulateur est irreplicable sans :
1. **La data** : 184K procedures + outcomes + financials + acteurs reels
2. **Les regles calibrees** : parametres du monde valides contre la realite
3. **Les profils agents** : bases sur les vrais acteurs du marche
4. **L'historique de calibration** : chaque simulation passee ameliore la suivante

*C'est le seul outil au monde qui permet de "jouer" le marche M&A distressed francais en simulation avant d'y participer pour de vrai.*

---

*Derniere mise a jour : 17 mars 2026*
