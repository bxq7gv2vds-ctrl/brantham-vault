---
type: strategy
created: 2026-03-16
updated: 2026-03-16
status: active
review_cadence: monthly
next_review: 2026-04-16
---

# Brantham Partners — Roadmap & Vision

---

## I. Vision

**Devenir le systeme nerveux du M&A distressed en France.**

Pas un cabinet de conseil. Pas une marketplace. Un systeme autonome qui detecte, analyse, score, connecte et ferme des deals de cession d'entreprises en difficulte — plus vite et mieux que n'importe quel acteur humain du marche.

L'objectif final : chaque procedure collective en France qui presente un potentiel de reprise passe par Brantham Partners, automatiquement, avant que les acteurs traditionnels aient meme ouvert le BODACC.

---

## II. Ou on en est

### Ce qui existe (mars 2026)

| Asset | Etat | Valeur |
|-------|------|--------|
| **Data pipeline** | Production (daily cron 07h) | 184K+ procedures, enrichissement SIRENE, geocodage, scoring auto |
| **Scoring 9D** | Calibre, backtest 165K lignes | C-index Cox 0.84, seuils valides, 9 composantes ponderees |
| **Cox PH predictions** | Production | P(cession) a 3/6/9/12 mois par procedure |
| **6 agents LLM** | Operationnels | Scout→Director→Analyst→Writer→Hunter→Enricher |
| **4D repreneur matching** | Production | Financial + Strategic + Track Record + Operational |
| **NAF ring model** | Production | 5 rings, supply chain TES, 172K codes |
| **AJ scraper** | Production | 5K+ annonces, multi-sites, cache JSON |
| **Dashboard** | Production | 10+ routes, SSE real-time, Zustand, React 19 |
| **Swarm Intelligence** | MVP (vient d'etre build) | Agents LLM locaux (qwen2.5:7b), consensus emergent |
| **Website SEO** | 19 pages live, 192 termes glossaire | SEO 93/100, AI visibility 4.2/5 |
| **Deals archives** | 600+ | Historique pour backtest et comparables |
| **Revenue** | **0 EUR** | Pre-revenue |

### Le deal actif

MLD (Multi Loisirs Distribution) — teaser redige, pret pour Hunter. Deadline 17/03/2026.

---

## III. Le marche

### Taille

- **~70 000** procedures collectives ouvertes par an en France (source: Altares)
- **~12 000** aboutissent a une cession totale ou partielle
- **Fee moyen** sur une cession PME distressed : **3-8% du prix** (fourchette basse car distressed)
- **Prix de cession moyen** PME en difficulte : **500K - 5M EUR**
- **Marche adressable** : 12K cessions x 2M EUR moyen x 5% fee = **~1.2 Md EUR** de fees annuels (total marche)
- **Cible realiste** Brantham (1% du marche en 3 ans) : **12M EUR/an**

### Concurrence

| Acteur | Modele | Force | Faiblesse |
|--------|--------|-------|-----------|
| **Cabinets AJ traditionnels** | Relations, carnet d'adresses | Reseau mandataires, legitimite | Zero tech, lent, petit perimetre |
| **Plateformes (Fusacq, Cessionpme)** | Marketplace annonces | Audience acheteurs | Pas de sourcing actif, pas d'analyse |
| **Big 4 restructuration** (EY, KPMG) | Conseil premium | Mandats gros dossiers | Ne touche pas aux PME <10M |
| **Mandataires judiciaires** | Monopole legal | Acces direct aux dossiers | Pas de prospection acheteurs structuree |
| **Brantham Partners** | Data + IA + speed | 184K procedures, scoring predictif, agents autonomes | Pre-revenue, 1 seul operateur |

### Notre avantage (moat)

1. **Asymetrie d'information** : on score 184K procedures avant tout le monde
2. **Vitesse** : pipeline Scout→Teaser en heures vs semaines chez les concurrents
3. **Predictions** : Cox C-index 0.84 = on sait QUELLES procedures vont aboutir
4. **Couverture** : BODACC complet + AJ scraper = rien ne nous echappe
5. **Matching** : 4D scoring + NAF rings + live API gouv.fr = acheteurs qualifies
6. **Zero cout marginal** : une fois le pipeline en place, chaque deal additionnel ne coute que des tokens LLM

---

## IV. Business model

### Phase 1 — Intermediation (maintenant → Q4 2026)

```
Detection → Analyse → Teaser → Matching acheteurs → Mise en relation → Fee
```

- **Success fee** : 4-6% du prix de cession (min 10K EUR)
- **Retainer** : 0 EUR (pas de fee upfront, full success)
- **Cible** : PME 1-20M EUR CA en RJ/LJ

### Phase 2 — Abonnement data (2027)

- **Abonnement SaaS** pour mandataires judiciaires et repreneurs seriel
  - Mandataire : acces au matching acheteurs + scoring = **500-2000 EUR/mois**
  - Repreneur : alertes personnalisees + analyse auto = **200-800 EUR/mois**
  - Fond d'investissement : API acces + swarm predictions = **2000-5000 EUR/mois**

### Phase 3 — Plateforme transactionnelle (2028+)

- Marketplace privee : data room, gestion d'offres, signature electronique
- Commission sur transaction (1-2% additionnel)
- Services ancillaires : valorisation certifiee, due diligence IA, rapport mandataire auto

---

## V. Roadmap technique

### PHASE 0 — FIRST CLOSE (mars-avril 2026)

**Objectif : fermer le premier deal et generer du revenu.**

| Priorite | Tache | Impact | Effort |
|----------|-------|--------|--------|
| P0 | **Closer MLD** (deadline 17/03) — lancer Hunter, identifier 10 acheteurs, prise de contact | Revenue | 2j |
| P0 | **5 deals supplementaires** dans le pipeline — seuil score 65+ | Pipeline | 1 sem |
| P0 | **Automatiser le flow complet** Scout→Director→Analyst→Writer→Hunter→Enricher sans intervention manuelle | Speed | 1 sem |
| P1 | **Email automation** — templates + envoi auto aux AJ et acheteurs identifies | Scale | 3j |
| P1 | **Tracking reponses** — CRM minimal dans le dashboard (suivi emails, relances) | Conversion | 3j |

### PHASE 1 — PIPELINE MACHINE (mai-juillet 2026)

**Objectif : 5+ deals actifs en permanence, conversion predictible.**

| Priorite | Tache | Impact |
|----------|-------|--------|
| P0 | **BODACC historique 2015-2023** — etendre la couverture de 3 ans a 11 ans | Backtest + comparables |
| P0 | **Scoring v2** — integrer bilans INPI (ratios financiers) dans les 9 composantes | Precision |
| P0 | **Swarm predictions en prod** — lancer simulation swarm sur top 50 deals/semaine, integrer dans le scoring ensemble (quant 70% + swarm 30%) | Edge predictif |
| P1 | **Dataroom IA** — upload PDF/Excel, extraction auto KPIs financiers, analyse Claude | Vitesse analyse |
| P1 | **Teaser auto-generation** — PPTX complet depuis analyse, zero intervention | Scale |
| P1 | **AJ relationship tracker** — historique interactions par mandataire, scoring relationnel | Conversion |
| P2 | **Multi-source veille** — Infogreffe, tribunaux de commerce, presse locale, alertes sectorielles | Couverture |
| P2 | **Matching v2** — enrichissement live (Pappers API, Societe.com scraping, LinkedIn) | Qualite acheteurs |

### PHASE 2 — SCALE & MOAT (aout-decembre 2026)

**Objectif : 10+ deals simultanes, revenus recurrents, avantage technologique inattaquable.**

| Priorite | Tache | Impact |
|----------|-------|--------|
| P0 | **Ensemble predictif complet** — MC + Cox + Bayesian + AgentMath + Swarm, weighted, backtest vs outcomes reels | Precision predictions |
| P0 | **Dashboard mandataire** — vue dediee pour les AJ/MJ : leurs dossiers, acheteurs identifies, rapports auto | Distribution |
| P0 | **API publique v1** — endpoints scoring + matching + predictions pour partenaires | Revenu SaaS |
| P1 | **Knowledge graph M&A** — entites (entreprises, AJ, tribunaux, secteurs, acheteurs) + relations + historique temporel | Intelligence structurelle |
| P1 | **Swarm v2** — agents specialises par secteur, apprentissage des outcomes passes, calibration dynamique | Precision swarm |
| P1 | **SEO machine 100 pages** — 6 clusters thematiques, 90+ articles, DA > 30 | Inbound leads |
| P2 | **Alertes intelligentes** — notifications push quand un deal match le profil d'un repreneur enregistre | Engagement |
| P2 | **Mobile app** (ou PWA) — acces pipeline on-the-go pour Paul + futurs associes | Productivite |
| P2 | **Rapport mandataire auto** — generer le rapport article 56 (bilan economique) automatiquement depuis les donnees | Valeur ajoutee AJ |

### PHASE 3 — PLATEFORME (2027)

**Objectif : devenir l'infrastructure du marche.**

| Tache | Impact |
|-------|--------|
| **Marketplace privee** — data room securisee, gestion d'offres structurees, timeline deal | Plateforme transactionnelle |
| **Due diligence IA** — analyse auto de 50+ documents, red flags, rapport structure | Service premium |
| **Valorisation certifiee** — modele de valorisation backteste sur 10K+ cessions historiques, rapport PDF | Produit standalone |
| **Signature electronique** — protocole de cession + acte de cession en ligne | Close-the-loop |
| **Multi-pays** — Belgique, Espagne, Italie (memes procedures collectives, reglementation UE) | Expansion geo |
| **Scoring-as-a-Service** — API pour banques, assureurs credit, cabinets conseil | B2B SaaS |
| **Agent autonome full-loop** — de la detection BODACC a la signature, zero humain (sauf validation legale) | Endgame |

### PHASE 4 — DOMINANCE (2028+)

| Tache | Impact |
|-------|--------|
| **Marketplace publique** — acheteurs peuvent s'inscrire, definir criteres, recevoir deals auto | Network effects |
| **Financement integre** — DIP financing, bridge loans via partenaires bancaires | Revenue stream |
| **Predictions macro** — predictions sectorielles de defaillances (indice proprietaire cite par la presse) | Brand + autorite |
| **White-label** — licensing du moteur scoring + matching a des cabinets conseil | Revenue recurrent |
| **Acquisition cabinets** — racheter des petits cabinets M&A distressed pour leur carnet d'adresses | Consolidation |

---

## VI. Metriques cles par phase

| Phase | Periode | Deals pipeline | Deals closes | Revenue | Equipe |
|-------|---------|---------------|-------------|---------|--------|
| 0 - First Close | Mar-Avr 2026 | 5 | 1 | 10-50K EUR | 1 (Paul) |
| 1 - Pipeline Machine | Mai-Juil 2026 | 15 | 3 | 100-300K EUR | 1-2 |
| 2 - Scale & Moat | Aout-Dec 2026 | 30+ | 8 | 500K-1M EUR | 2-3 |
| 3 - Plateforme | 2027 | 50+ | 20+ | 2-5M EUR | 5-8 |
| 4 - Dominance | 2028+ | 100+ | 50+ | 10M+ EUR | 10-15 |

---

## VII. Risques et mitigations

| Risque | Probabilite | Impact | Mitigation |
|--------|-------------|--------|------------|
| **Premier deal ne close pas** | Moyen | Moral + tresorerie | Pipeline diversifie (5+ deals), pas tout miser sur MLD |
| **Mandataires ne repondent pas** | Eleve | Pas de deal flow | LinkedIn personal brand, credibilite via contenu, referrals post-1er deal |
| **Reglementation** — activite de courtage M&A reglementee ? | Faible | Blocage legal | Structurer comme conseil en cession (pas courtage), consulter avocat |
| **Concurrent tech emerge** | Faible | Erosion avantage | Avance data (184K procs + 11 ans historique), execution rapide |
| **Dependance LLM externe** (Anthropic, OpenAI) | Moyen | Cout + disponibilite | Swarm local (llama-cpp), migration possible vers open-source |
| **Qualite scoring insuffisante** | Faible | Mauvais deals proposes | Backtest continu, Cox C-index 0.84 deja solide, feedback loop |
| **Burnout solo founder** | Eleve | Tout s'arrete | Automatisation max, premier hire = ops/biz dev, pas dev |

---

## VIII. Le flywheel

```
Plus de deals dans le pipeline
        |
        v
Plus de data (outcomes, prix, delais)
        |
        v
Meilleur scoring + predictions
        |
        v
Meilleur matching acheteurs
        |
        v
Plus de cessions reussies
        |
        v
Plus de fees + reputation
        |
        v
Plus de mandataires qui nous envoient des deals
        |
        v
Plus de deals dans le pipeline  ←──── LOOP
```

Chaque deal close renforce le systeme. Les concurrents qui n'ont pas la data ne peuvent pas entrer.

---

## IX. North Star

**"Chaque PME viable en France qui entre en procedure collective a un repreneur identifie et contacte en 48h."**

Pas dans 5 ans. C'est ce qu'on construit maintenant.

---

## X. Stack technique finale (cible 2027)

```
┌──────────────────────────────────────────────────────────┐
│                    BRANTHAM PLATFORM                      │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │ DATA LAYER  │  │ INTELLIGENCE│  │ DISTRIBUTION    │  │
│  │             │  │             │  │                 │  │
│  │ PostgreSQL  │  │ Scoring 9D  │  │ Dashboard       │  │
│  │ 184K+ procs │  │ Cox PH      │  │ API publique    │  │
│  │ BODACC live │  │ Swarm LLM   │  │ Email auto      │  │
│  │ SIRENE      │  │ 6 Agents    │  │ Alertes push    │  │
│  │ Bilans INPI │  │ Ensemble    │  │ Marketplace     │  │
│  │ AJ scraper  │  │ Knowledge   │  │ Mobile PWA      │  │
│  │ Orbis comps │  │   Graph     │  │ Mandataire vue  │  │
│  └─────────────┘  └─────────────┘  └─────────────────┘  │
│                                                          │
│  ┌─────────────────────────────────────────────────────┐ │
│  │              AUTOMATION LAYER                       │ │
│  │  Scout → Director → Analyst → Writer → Hunter →    │ │
│  │  Enricher → Email → Suivi → Close                  │ │
│  │  (full autonomous pipeline, human-in-the-loop       │ │
│  │   only for final validation + legal)                │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ WEBSITE/SEO  │  │ LINKEDIN     │  │ PARTNERSHIPS  │  │
│  │ 100+ pages   │  │ Personal     │  │ AJ network    │  │
│  │ DA > 30      │  │ brand        │  │ Fonds PE      │  │
│  │ AI visible   │  │ Thought      │  │ Banques       │  │
│  │ Inbound      │  │ leadership   │  │ Assureurs     │  │
│  └──────────────┘  └──────────────┘  └───────────────┘  │
└──────────────────────────────────────────────────────────┘
```

---

*Derniere mise a jour : 16 mars 2026*
*Prochaine review : 16 avril 2026*
