---
type: strategy
created: 2026-03-16
updated: 2026-03-16
project: mirofish-oasis
status: active
---

# MiroFish / OASIS — Roadmap Swarm Intelligence M&A

---

## Concept

Simuler un marche M&A avec des agents LLM autonomes qui evaluent, biddent et negotient des deals. Le consensus emergent de 25-50 agents produit un signal predictif complementaire au scoring quant (Cox, Bayesian, MC). C'est du prediction market applique au M&A distressed, avec des agents au lieu de traders humains.

**Analogie** : ce que Polymarket fait avec des parieurs humains, MiroFish le fait avec des agents LLM specialises — chacun a un profil, un thesis, des contraintes de capital. Le prix de marche emergent = probabilite de cession.

---

## Etat actuel (v0.1 — mars 2026)

### Ce qui marche
- 7 ActionTypes (BID, WATCH, PASS, DD, NEGOTIATE, WITHDRAW, DO_NOTHING)
- 27 archetypes d'investisseurs + import buyers reels depuis PostgreSQL
- DealMarketplacePlatform avec SQLite trace + aggregation consensus
- SwarmRunner sequentiel via llama-cpp-python (qwen2.5:7b, Metal partiel)
- 5 endpoints API (/swarm/run, /status, /predictions, /timeline, /agents)
- Frontend SwarmPage (3 tabs: predictions, timeline, agents)
- Test OK: 3 agents x 2 rounds → consensus coherent (FoodTech score 91 = STRONG_BUY)

### Limitations
- **Lent** : ~8s/agent/round → 25 agents x 12 rounds = ~40 min
- **Pas de memoire** : agents oublient entre les rounds (stateless)
- **Pas calibre** : aucune validation contre outcomes reels
- **Pas d'interactions** : agents ne voient pas les actions des autres en detail
- **Modele petit** : qwen2.5:7b, pas optimal pour raisonnement financier
- **Ollama casse** : Metal bfloat bug sur M5, fallback llama-cpp-python

---

## Architecture cible

```
                    ┌──────────────────────────────────┐
                    │         MARKET DESIGNER           │
                    │  Parametres: rules, fees, info    │
                    │  asymmetry, round timing          │
                    └──────────┬───────────────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
     ┌────────▼──────┐ ┌──────▼───────┐ ┌──────▼───────┐
     │  BUYER AGENTS  │ │ SELLER AGENT │ │  OBSERVER    │
     │  (25-50)       │ │ (mandataire) │ │  AGENTS      │
     │                │ │              │ │              │
     │ - Profile      │ │ - Reserve    │ │ - Analyst    │
     │ - Thesis       │ │ - Urgency    │ │ - Regulator  │
     │ - Capital      │ │ - Preference │ │ - Market     │
     │ - History      │ │              │ │   maker      │
     │ - Reputation   │ │              │ │              │
     └────────┬───────┘ └──────┬───────┘ └──────┬───────┘
              │                │                │
              └────────────────┼────────────────┘
                               │
                    ┌──────────▼───────────────────────┐
                    │       MARKETPLACE ENGINE          │
                    │                                   │
                    │  Rounds: Discovery → DD → Bid →   │
                    │          Negotiate → Close/Fail   │
                    │                                   │
                    │  Mechanics: sealed bids, auction,  │
                    │  info revelation, due diligence    │
                    │  costs, reputation effects         │
                    └──────────┬───────────────────────┘
                               │
                    ┌──────────▼───────────────────────┐
                    │       CONSENSUS ENGINE            │
                    │                                   │
                    │  Aggregation: bid distribution,   │
                    │  interest ratio, price discovery,  │
                    │  confidence intervals             │
                    │                                   │
                    │  Output: P(cession), EV range,    │
                    │  buyer profile, timeline estimate  │
                    └──────────┬───────────────────────┘
                               │
                    ┌──────────▼───────────────────────┐
                    │       CALIBRATION LOOP            │
                    │                                   │
                    │  Backtest vs real outcomes         │
                    │  Adjust agent weights, biases      │
                    │  Track: Brier score, accuracy      │
                    └──────────────────────────────────┘
```

---

## Roadmap

### v0.2 — SPEED + MEMORY (avril 2026)

Rendre la simulation utilisable en production.

| Tache | Detail | Impact |
|-------|--------|--------|
| **Batched inference** | Grouper les prompts agents, single forward pass avec llama-cpp-python batch API | 5-10x plus rapide |
| **Modele upgrade** | Passer a `qwen2.5:14b` ou `llama3:8b` quand Ollama fix Metal M5 (ou compiler llama.cpp from source avec Metal fix) | Meilleur raisonnement |
| **Agent memory** | Chaque agent garde un historique de ses actions passees (derniers 3 rounds). Injecte dans le prompt : "Last round you BID on X at 3M, there are now 4 competing bids" | Comportement realiste |
| **Inter-agent visibility** | Les agents voient les actions anonymisees des autres ("3 bids on this deal, avg 2.5M") — information de marche | Price discovery |
| **Streaming SSE** | Streamer les actions en temps reel vers le frontend via SSE pendant la simulation | UX |
| **Resume simulation** | Pouvoir reprendre une simulation arretee (serialiser l'etat marketplace + agent states en JSON) | Robustesse |

### v0.3 — MARKET MECHANICS (mai-juin 2026)

Passer d'un scoring passif a une vraie simulation de marche.

| Tache | Detail | Impact |
|-------|--------|--------|
| **Phases de deal** | 5 phases par deal : Discovery → Due Diligence → Bid → Negotiation → Close/Fail. Chaque phase a des regles differentes | Realisme |
| **Cout de DD** | La due diligence coute du "capital reputation" a l'agent. Force des decisions non-triviales | Strategic depth |
| **Sealed bid auction** | Phase finale : encheres scellees, revelation simultanee, winner's curse dynamics | Price discovery |
| **Seller agent** | Agent mandataire avec reserve price, urgency level, preference acheteur (emploi, secteur, taille). Peut rejeter des offres | Two-sided market |
| **Deal lifecycle** | Un deal passe par des etapes : nouveau → en analyse → offres en cours → sous exclusivite → cede/echoue. Timeline realiste | Temporal dynamics |
| **Information asymmetry** | Certains agents ont plus d'info que d'autres (tier 1 = full financials, tier 2 = summary only, tier 3 = public info) | Realistic market |

### v0.4 — CALIBRATION (juillet-aout 2026)

Le swarm doit battre un coin flip, sinon ca sert a rien.

| Tache | Detail | Impact |
|-------|--------|--------|
| **Backtest historique** | Lancer le swarm sur les 600+ deals archives ou l'outcome est connu. Mesurer : prediction swarm vs outcome reel | Validation |
| **Brier score tracking** | Pour chaque deal : `(prediction - outcome)^2`. Tracker dans le temps. Comparer : swarm seul vs quant seul vs ensemble | Metrique de qualite |
| **Agent weight learning** | Les agents qui ont historiquement raison pesent plus dans le consensus. Les agents systematiquement faux sont down-weightes | Precision |
| **Ensemble integration** | Integrer le signal swarm dans le scoring global : `P(cession) = 0.25*MC + 0.30*Cox + 0.15*Bayes + 0.15*Swarm + 0.15*AgentMath` | Production ready |
| **Confidence intervals** | Au lieu d'un P(cession) point, produire un intervalle : `[0.35, 0.55]` avec 80% confidence. Base sur la dispersion des bids agents | Decision quality |
| **Sector specialists** | Agents calibres par secteur (l'archetype "Specialist Manufacturing" performe mieux sur deals industrie → bonus de poids) | Precision sectorielle |

### v0.5 — SOCIAL DYNAMICS (sept-oct 2026)

Le swarm devient un ecosysteme.

| Tache | Detail | Impact |
|-------|--------|--------|
| **Reputation system** | Chaque agent a un score de reputation base sur ses predictions passees. Les agents voient les reputations des autres | Wisdom of crowds |
| **Herding detection** | Detecter quand les agents "suivent le troupeau" sans analyse independante. Penaliser le herding, recompenser la conviction contrarian | Signal quality |
| **Network effects** | Graphe social entre agents : certains se font confiance, certains sont rivaux. Influence les decisions (si mon "trusted peer" bid, je regarde plus attentivement) | Emergent intelligence |
| **Agent evolution** | Les profils agents evoluent : un agent qui a close 5 deals industriels devient plus agressif sur l'industrie. Son thesis evolue | Adaptation |
| **Coalition detection** | Identifier quand des groupes d'agents convergent sur un deal → signal fort. Divergence totale → signal faible/noise | Signal extraction |
| **Market sentiment index** | Aggreger l'activite swarm en un indice : "appetit acheteur" par secteur et taille. Equivalent du VIX pour le M&A distressed | Market intelligence |

### v1.0 — PREDICTION MARKET (2027)

Le swarm devient un produit.

| Tache | Detail | Impact |
|-------|--------|--------|
| **Real buyers as agents** | Les vrais acheteurs dans la DB (143) deviennent des agents avec leur historique reel (acquisitions passees, prix, secteurs) | Ground truth |
| **Continuous simulation** | Le swarm tourne en continu (pas on-demand). Chaque nouveau deal BODACC est injecte dans le marketplace. Les agents reagissent en temps reel | Always-on intelligence |
| **Price discovery** | Le swarm produit un "market price" pour chaque deal — pas juste P(cession) mais aussi VE estimee par le marche d'agents | Valorisation |
| **Scenario analysis** | "Que se passe-t-il si le CA baisse de 20% ?" → re-run swarm avec donnees modifiees → delta predictions | Decision support |
| **External signal ingestion** | Feed les agents avec presse, LinkedIn posts, signaux macro (taux, confiance PME, defaillances sectorielles) | Context awareness |
| **White-label API** | Exposer le swarm comme service : "donnez-moi une entreprise en difficulte, je vous donne P(cession) + EV + profil acheteur ideal + timeline" | Revenue |

### v2.0 — AUTONOMOUS MARKET (2028+)

Le swarm fait des deals.

| Tache | Detail |
|-------|--------|
| **Agent-to-human bridge** | Quand un agent virtuel BID, proposer automatiquement le deal au vrai acheteur le plus proche du profil agent |
| **Negotiation simulation** | Agents negocient entre eux : offre/contre-offre, conditions suspensives, clauses de garantie. Output : term sheet draft |
| **Multi-asset simulation** | Un acheteur peut bid sur plusieurs deals simultanement, avec contrainte de capital total. Portfolio optimization emergent |
| **Cross-border** | Agents representant des acheteurs internationaux (UK, Germany, Spain) avec preferences differentes |
| **Regulatory agent** | Agent "tribunal de commerce" qui valide/refuse les offres selon criteres legaux (maintien emploi, prix minimum) |
| **Self-improving** | Le swarm s'auto-calibre : apres chaque outcome reel, ajuste les poids, retire les agents non-performants, en genere de nouveaux |

---

## Metriques de succes

| Phase | Metrique cle | Cible |
|-------|-------------|-------|
| v0.2 | Temps simulation 25 agents x 12 rounds | < 5 min |
| v0.3 | Deals avec price discovery (bid dispersion < 30% CV) | > 60% |
| v0.4 | Brier score swarm vs coin flip (0.25) | < 0.20 |
| v0.4 | Ensemble (quant+swarm) vs quant seul — accuracy lift | > +5% |
| v0.5 | Herding rate (% agents qui copient sans analyser) | < 20% |
| v1.0 | Correlation swarm P(cession) vs outcome reel | > 0.70 |
| v1.0 | Temps moyen detection → prediction | < 1h |

---

## Contraintes techniques

| Contrainte | Etat | Solution |
|-----------|------|----------|
| Ollama Metal M5 crash | Bloquant | llama-cpp-python (workaround), attendre fix Ollama ou compiler llama.cpp custom |
| Inference speed (8 tok/s) | Limitant | Batch inference, modele plus petit pour screening + gros pour decisions finales |
| Contexte LLM (2048 tokens) | Limitant | Compression des deal feeds, hierarchie : resume → detail on-demand |
| Python 3.14 compat | OK | llama-cpp-python 0.3.16 fonctionne |
| RAM Metal (7.8 GB dispo) | OK pour 7B | 14B necessitera gestion memoire (offload partiel CPU) |

---

## Inspirations

| Projet | Ce qu'on prend |
|--------|---------------|
| **OASIS (camel-ai)** | Architecture agent graph + social simulation |
| **Polymarket** | Prediction market mechanics, price discovery par consensus |
| **Robin Hood (Citadel)** | Market making, order flow analysis |
| **AlphaFold** | Self-play pour decouvrir des structures — ici des valuations |
| **MiroFish** | Swarm intelligence, comportement emergent, stigmergie |
| **Mesa (ABM)** | Agent-based modeling framework, step/collect paradigm |

---

*Le swarm est le seul composant de Brantham qui ne peut PAS etre replique par un concurrent sans la data (184K procs + outcomes) ET l'infrastructure (agents calibres). C'est le moat ultime.*

## Related
- [[brantham/_MOC]]
