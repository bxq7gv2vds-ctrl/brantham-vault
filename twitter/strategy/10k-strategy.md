---
type: strategy
project: twitter
created: 2026-03-28
goal: 10K followers in 6 months
status: active
---

# Stratégie Twitter — 10K en 6 Mois

## TL;DR

10K followers en 6 mois = possible. Condition : 70% replies + first-mover breaking news + builder logs chiffrés + knowledge graph auto-améliorant. Ce doc est la feuille de route complète.

---

## Ce qui existe déjà (ne pas reconstruire)

- **Voice card** : persona Paul entièrement définie (`agent/voice-card.md`)
- **Cowork prompt** : agent Twitter complet avec routine quotidienne (`agent/COWORK-PROMPT.md`)
- **Tier list** : 40+ comptes classés (`agent/accounts/tier-list.md`)
- **Pattern library** : hooks, formats, anti-patterns (`agent/patterns/`)
- **Architecture** : Cowork + Playwright + vault + QMD + claude-peers
- **Weekly digest** : 1 digest déjà généré (26/03)

**Ce qui manque** : le knowledge graph auto-améliorant, le performance tracker, le dashboard review, et surtout — **l'exécution quotidienne**.

---

## Architecture Cible — Écosystème Multi-Agents

```
┌─────────────────────────────────────────────────────────────┐
│                     PAUL (orchestrateur)                     │
│              Review 5 min/jour → Approve/Reject              │
└─────────────────────┬───────────────────────────────────────┘
                      │ claude-peers
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              AGENT TWITTER (Cowork + Playwright)             │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ SCRAPER  │  │ ANALYST  │  │ DRAFTER  │  │ TRACKER  │  │
│  │          │→ │          │→ │          │→ │          │  │
│  │feed+news │  │patterns  │  │3-5 drafts│  │metrics   │  │
│  │bookmarks │  │topics    │  │per day   │  │learning  │  │
│  │trending  │  │hooks     │  │          │  │          │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
└─────────────────────┬───────────────────────────────────────┘
                      │ Read/Write
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE GRAPH                           │
│              vault/twitter/ + SQLite + QMD                  │
│                                                             │
│   accounts ──── tweets ──── patterns ──── topics           │
│        │            │            │            │             │
│        └────────────┴────────────┴────────────┘            │
│                    (mis à jour quotidiennement)              │
└─────────────────────────────────────────────────────────────┘
```

### Les 4 Agents

**1. SCRAPER AGENT** (run 3x/jour : 8h, 13h, 19h)
- Browser Playwright → x.com/home (50-100 tweets)
- x.com/search pour 8 keywords AI/agents
- x.com/explore → trending
- 10-15 comptes Tier 1 → leurs derniers tweets
- Fallback : `clix feed --json`
- Output → `vault/twitter/digests/YYYY-MM-DD.md`

**2. ANALYST AGENT** (run après chaque scan)
- Extrait : engagement, format, hook type, topic
- Détecte : breaking news (réagir < 30min), threads viraux, account à reply
- Met à jour : `agent/niche/topics-ranking.md`, `agent/patterns/`
- Identifie : opportunités de reply à fort impact

**3. DRAFTER AGENT** (run 1x/jour, 10h)
- Génère 5-8 drafts : 1 breaking react, 2 builder logs, 2-3 replies, 1 thread optionnel
- Filtre BLACKLIST systématique
- Burstiness check (longueur phrases variée)
- Voice check (Voice Card)
- Soumet à Paul via claude-peers
- Output → `agent/drafts/YYYY-MM-DD.md`

**4. TRACKER AGENT** (run 1x/jour, 22h)
- Lit les métriques des tweets postés (via browser x.com/handle)
- Enregistre : likes, RT, replies, bookmarks, impressions
- Corrèle : format vs engagement, topic vs engagement, timing vs reach
- Génère rapport hebdo `agent/metrics/weekly-YYYY-WXX.md`
- Met à jour les poids des patterns dans le KG

---

## Le Knowledge Graph — Architecture Technique

### Storage : SQLite + vault + QMD

```
vault/twitter/
  knowledge-graph/
    tweets.db          ← SQLite principal
    accounts.json      ← Cache profils comptes
    patterns.json      ← Poids des patterns (mis à jour hebdo)
    topics.json        ← Score topics par période

  agent/metrics/
    YYYY-MM-DD.md      ← Métriques du jour
    weekly-YYYY-WXX.md ← Rapport hebdo
```

### Schéma SQLite

```sql
-- Tweets postés + performance
CREATE TABLE tweets (
  id TEXT PRIMARY KEY,
  content TEXT,
  format TEXT,           -- single|thread|reply|quote
  topic TEXT,            -- ai_agents|llm|builders|news|hot_take
  hook_type TEXT,        -- prediction|builder_flex|breaking|hot_take|humor
  time_posted DATETIME,
  likes INTEGER DEFAULT 0,
  retweets INTEGER DEFAULT 0,
  replies INTEGER DEFAULT 0,
  bookmarks INTEGER DEFAULT 0,
  impressions INTEGER DEFAULT 0,
  engagement_rate REAL,
  paul_approval TEXT,    -- approved|rejected|edited_minor|edited_major
  paul_edit_delta REAL,  -- 0=no change, 1=rewritten entirely
  notes TEXT
);

-- Comptes analysés
CREATE TABLE accounts (
  handle TEXT PRIMARY KEY,
  tier INTEGER,
  follower_count INTEGER,
  avg_likes REAL,
  avg_rt REAL,
  dominant_format TEXT,
  dominant_topic TEXT,
  best_hook_type TEXT,
  post_frequency TEXT,   -- posts/day
  style_notes TEXT,
  last_analyzed DATE
);

-- Tweets inspirants (de la niche, pas postés par Paul)
CREATE TABLE inspiration_tweets (
  id TEXT PRIMARY KEY,
  author_handle TEXT,
  content TEXT,
  likes INTEGER,
  retweets INTEGER,
  bookmarks INTEGER,
  format TEXT,
  hook_type TEXT,
  topic TEXT,
  why_it_works TEXT,     -- analyse courte
  date_collected DATE
);

-- Patterns performants
CREATE TABLE patterns (
  name TEXT PRIMARY KEY,
  type TEXT,             -- hook|format|topic|timing
  description TEXT,
  examples TEXT,         -- JSON array
  success_rate REAL,     -- % des tweets avec ce pattern qui performent > avg
  avg_engagement REAL,
  sample_size INTEGER,
  last_updated DATE
);
```

### Boucle d'auto-amélioration

```
Semaine N :
  PostTweet(draft_v1, patterns_from_week_N-1)
  → track performance 24h
  → Analyst: corrèle performance avec patterns
  → update patterns.json (upweight winners, downweight losers)

Semaine N+1 :
  Drafter utilise patterns_updated_week_N
  → drafts meilleurs en moyenne
  → répéter
```

Après 8 semaines : le system a statistiquement validé les patterns. Après 16 semaines : les patterns sont stables, le style est identifié au niveau micro.

---

## Roadmap 6 Mois — Milestones

### MOIS 1 (Semaine 1-4) — Fondations & Apprentissage
**Objectif : 500 followers**

**Semaine 1-2 : Phase Observation**
- Observer sans poster (ou 1-2 tweets/jour max)
- Scanner 500+ tweets niche
- Analyser 30 comptes Tier 1/2 en profondeur
- Alimenter le knowledge graph initial
- Calibrer la voix avec Paul (5 drafts/jour, 0 postés — juste feedback)

**Semaine 3-4 : Premier posts**
- 5-8 tweets/jour : 1-2 originaux + 5-6 replies
- 70% replies sous tweets viraux (< 30min après publication)
- 20+ likes/jour sur comptes cibles
- Objectif semaine 4 : 200 followers

**KPIs Mois 1 :**
- 200 tweets postés (dont 80% replies)
- Engagement rate > 3% sur tweets originaux
- 30 comptes analysés et dans le KG
- 500 followers fin mois

**Contenu typique Mois 1 :**
- Replies courtes et sharp sous @karpathy, @levelsio, @RoundtableSpace
- Builder logs avec chiffres ("mon pipeline vient de processer X en Y sec")
- Hot takes sur Claude vs GPT
- Réactions instantanées aux news Claude/Anthropic

---

### MOIS 2 (Semaine 5-8) — First Mover + Réactions Rapides
**Objectif : 2000 followers**

**Tactique principale : Breaking News Sprint**
- Crucix OSINT → alerte sur breaking news AI/tech
- Cowork réagit dans les 30 premières minutes
- Format : CAPS hook + explication + opinion personnelle
- Exemple : "@RoundtableSpace a 80K views sur ses breaking news → nous on en capture 1-5K avec une reply

**Tactique secondaire : Thread hebdomadaire**
- 1 thread/semaine, 5-8 tweets
- Sujet : ce que Paul build concrètement
- Ex: "Comment j'ai construit un pipeline qui scrape 3900 procédures judiciaires/jour — thread"
- Threads : 40% du total impressions pour 10% du volume de posts

**KPIs Mois 2 :**
- 1 tweet > 500 likes (objectif)
- Engagement rate moyen > 5%
- 2000 followers fin mois
- 20+ comptes ingestés dans le KG (100+ total)

---

### MOIS 3 (Semaine 9-12) — Premier Viral + Builder Brand
**Objectif : 4000 followers**

**Le pivot : passer de reply-guy à builder reconnu**
- Les 2 premiers mois construisent la crédibilité via les replies
- Mois 3 : les gens commencent à follow pour les posts originaux
- Tactique : "Builder Log" régulier avec chiffres précis + learnings
- Exemple: "2 mois de pipeline data. 184,000 procédures scrapées. Voici ce que j'ai appris."

**1 viral ciblé :**
- Identifier le meilleur tweet candidat via le KG (patterns validés)
- Optimiser le timing (soirée FR + US west coast overlap = 19h-21h FR)
- Objectif : 1 tweet > 1000 likes

**KPIs Mois 3 :**
- 1 tweet > 1000 likes
- 4000 followers
- KG a 200+ tweets analysés → patterns statistiquement fiables
- Paul edite < 20% des drafts (calibration quasi-complète)

---

### MOIS 4 (Semaine 13-16) — Amplification & Réseau FR
**Objectif : 6500 followers**

**Tactique : Ecosystem FR tech/AI**
- @Frenchiee, @melvynx, @0xmaxou, @thismacapital — ces comptes sont le levier
- Reply en français = niche underserved (peu de AI builders FR actifs)
- Quote tweets leurs posts avec analyse → cross-pollination audience
- Objectif : mentions mutuelles avec 3+ comptes FR Tier 2

**Tactique : Quote Tweet avec analyse**
- Prendre un tweet viral → quote avec angle inattendu
- Format: "tout le monde parle de X. le truc que personne mentionne : Y"
- Fort engagement (la réponse génère sa propre discussion)

**KPIs Mois 4 :**
- 3+ collaborations organiques avec FR accounts
- 200+ likes/tweet en moyenne sur originaux
- 6500 followers

---

### MOIS 5 (Semaine 17-20) — Régularité + Communauté
**Objectif : 8500 followers**

**Le flywheel tourne :**
- Le compte a une identité claire
- Les gens follow pour une raison précise (Paul = builder AI qui dit des trucs vrais)
- Objectif : chaque tweet original fait > 100 likes en moyenne

**Nouvelles tactiques :**
- Reply à ses propres threads quand l'info évolue (+ engagement naturel)
- Polls sur des choix tech ("Claude Code ou Cursor — pourquoi ?" → données + engagement)
- "Ask me anything" sessions (1x/mois)

**KPIs Mois 5 :**
- Engagement rate stable > 8% sur originaux
- 50+ follows/jour organiques
- 8500 followers

---

### MOIS 6 (Semaine 21-24) — Scale & Préparer le Compte 2
**Objectif : 10K+ followers**

**Compte perso atteint la masse critique.**
**Commencer à poser les bases du compte Analyse Tech/AI.**

**Tactiques finales :**
- 2-3 mega-threads de fond (threads qui restent pertinents 6 mois)
- Collaboration officielle avec 1-2 gros comptes FR
- Début de teasing du compte analyse tech

**KPIs Mois 6 :**
- 10,000 followers ✓
- 1+ tweet > 5000 likes (objectif stretch)
- KG > 500 tweets analysés, patterns stables
- Base posée pour compte 2

---

## La Formule 10K — Les 5 Lois

### Loi 1 : 70% replies, 30% originaux
**Pourquoi :** Sans audience, tes tweets originaux sont vus par 0 personnes.
Une reply sous un tweet viral avec 100K views = potentiellement 5K impressions.
C'est le seul levier gratuit. Chaque reply est une pub gratuite sur un gros compte.

### Loi 2 : First mover < 30 minutes
**Pourquoi :** L'algo X booste les premiers commentaires (= dwell time sur le post original).
30 minutes après = 10x moins de reach. 6 heures après = invisible.
**Crucix** alerte sur les breaking news → Cowork réagit immédiatement.

### Loi 3 : Chiffres précis = crédibilité
**Mauvais :** "j'ai build un pipeline qui scrape des procédures judiciaires"
**Bon :** "mon pipeline a scrapé 3,918 procédures en 47 secondes ce matin. 6 agents. 0 intervention."
Les chiffres exacts signalent l'authenticité. Impossible à inventer.

### Loi 4 : Jamais de lien externe dans les tweets
**Pourquoi :** X pénalise les liens externes (= sortie de la plateforme).
Solution : thread, puis mets le lien dans la reply de ton propre thread.

### Loi 5 : Le KG améliore les drafts semaine après semaine
Mois 1 : draft approval rate = 60% (Paul en corrige beaucoup)
Mois 3 : 80% (le système a appris)
Mois 6 : 95% (presque jamais besoin d'éditer)

---

## Compte 2 — Tech/AI Analyst (Préparer dès Mois 3)

### Différenciation
- **Compte perso** : Paul builder, personnel, opinion, franglais, authentique
- **Compte analyste** : objectif, données, finéco de l'AI, bilingual FR/EN, institutionnel

### Positionnement Compte 2
- Style : analyses de 5-10 tweets avec données, pas d'opinions personnelles
- Format dominant : threads d'analyse (comme @binance research meets AI news)
- Niche : "le Bloomberg de l'AI" — data-driven, rigoureux, zéro hype
- Fréquence : 3-5 posts/jour vs 8-10 pour le compte perso

### Architecture Compte 2
- Nouveau Cowork dédié (avec son propre COWORK-PROMPT)
- Partage le même KG que le compte perso (sources communes)
- Sources spécifiques : Arxiv, LessWrong, AI Safety papers, funding rounds
- Voice card séparée : moins de "mes frères", plus de "$" et de "study shows"

### Timeline
- Mois 3 : créer le compte, voix, structure
- Mois 4-5 : croissance parallèle en mode calme (3 posts/jour, 0 pression)
- Mois 6+ : accélérer quand le compte perso est établi

---

## Dashboard Review Paul — UX

Paul doit passer **5 minutes max** par jour sur le review.

### Interface (simple, terminal ou web)
```
=== DRAFTS DU 28/03 — 5 tweets en attente ===

[1] HOT TAKE — 10h30 recommandé
    "Claude Code vient de sortir les memory contexts. Les gens vont enfin
    comprendre que le vrai LLM ops c'est pas les prompts, c'est la persistance."
    [A]pprove [E]dit [R]eject [S]kip

[2] REPLY @buccocapital — urgent (tweet viral depuis 45min)
    En réponse à "Claude Cowork is blowing my mind. But..."
    "et c'est exactement la que ca devient interessant — un agent qui browse
    twitter pour un autre agent. on est litteralement a t+1 de IA²"
    [A]pprove [E]dit [R]eject

[3] BUILDER LOG — 19h recommandé
    "jour 47 du pipeline. 184,218 procedures scrapees. 6 agents.
    le truc qu'on realise : les donnees judiciaires publiques sont
    enormement sous-exploitees en France. genere un edge considérable."
    [A]pprove [E]dit [R]eject

...
```

### Règle d'or
- Paul approuve, l'agent poste
- Paul édite → l'agent apprend (signal = pattern à corriger)
- Paul rejette → l'agent apprend (signal = éviter ce type de draft)
- JAMAIS de post sans approbation les 4 premières semaines

---

## Métriques de Suivi

### Par semaine
| Semaine | Followers | Tweets postés | Avg likes | Replies | Approval rate |
|---------|-----------|---------------|-----------|---------|---------------|
| 1       | 100       | 35            | 5         | 80%     | 60%           |
| 4       | 500       | 35            | 15        | 70%     | 75%           |
| 8       | 2000      | 40            | 40        | 65%     | 85%           |
| 12      | 4000      | 45            | 80        | 60%     | 90%           |
| 16      | 6500      | 50            | 120       | 55%     | 92%           |
| 20      | 8500      | 50            | 150       | 50%     | 95%           |
| 24      | 10000+    | 50            | 200+      | 50%     | 97%           |

### Signaux d'alarme (revoir la stratégie)
- Engagement rate < 2% sur 2 semaines consécutives → audit du KG
- < 50 follows/semaine après mois 2 → revoir le mix replies/originaux
- > 50% des drafts rejetés → recalibrer la voix
- Block rate > 0.5% → ralentir l'engagement automatique

---

## Ce Qu'Il Faut Builder (ordre de priorité)

### P0 — Immédiat (cette semaine)
1. **SQLite knowledge graph** (`vault/twitter/knowledge-graph/tweets.db`)
2. **Scraper script** (clix + vault write, cron 3x/jour)
3. **Draft generator** (prompt Drafter Agent + quality gates)
4. **Approval queue** (fichier markdown formaté pour review Paul)

### P1 — Semaine 2
5. **Performance tracker** (browser → lire les métriques → vault)
6. **Pattern updater** (corrèle métriques → met à jour patterns.json)
7. **Weekly report generator**

### P2 — Mois 2
8. **Breaking news detector** (Crucix → alerte + draft auto en < 15min)
9. **Account analyzer** (analyse N comptes, extrait style → KG)
10. **Dashboard web** (optional — le markdown suffit au début)

### P3 — Mois 3+
11. **Compte 2 infrastructure** (clone de l'architecture, voix différente)
12. **Cross-account KG** (même patterns.json pour les 2 comptes)

---

## Related

- [[twitter/_MOC]]
- [[twitter/agent/COWORK-PROMPT]]
- [[twitter/agent/voice-card]]
- [[twitter/agent/accounts/tier-list]]
- [[twitter/agent/patterns/hooks-that-work]]
- [[_system/MOC-master]]
