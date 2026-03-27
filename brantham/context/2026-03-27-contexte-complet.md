---
type: context
project: brantham
date: 2026-03-27
updated: 2026-03-27
tags: [contexte, vue-ensemble, strategie, tech, pipeline, complet]
---

# Brantham Partners — Contexte Complet & Exhaustif

> Document de référence complet. Compilé depuis le vault (173 notes) le 27 mars 2026.
> Ce document est la source unique de vérité pour comprendre qui est Brantham, ce qu'on construit, comment, et pourquoi.

---

## Table des matières

1. [Identité, mission, vision](#1-identité-mission-vision)
2. [Le marché : M&A distressed en France](#2-le-marché--ma-distressed-en-france)
3. [Les procédures collectives — cours complet](#3-les-procédures-collectives--cours-complet)
4. [L'offre Brantham — services détaillés](#4-loffre-brantham--services-détaillés)
5. [Le moat — avantage concurrentiel](#5-le-moat--avantage-concurrentiel)
6. [Le pipeline opérationnel](#6-le-pipeline-opérationnel)
7. [Les 6 agents LLM — comment ça fonctionne](#7-les-6-agents-llm--comment-ça-fonctionne)
8. [Le scoring 9D — détail complet](#8-le-scoring-9d--détail-complet)
9. [Le matching acheteurs 4D](#9-le-matching-acheteurs-4d)
10. [Les deals — historique et actifs](#10-les-deals--historique-et-actifs)
11. [Architecture technique complète](#11-architecture-technique-complète)
12. [Le data pipeline — 9 étapes](#12-le-data-pipeline--9-étapes)
13. [La base de données — schéma complet](#13-la-base-de-données--schéma-complet)
14. [Le dashboard interne (web app)](#14-le-dashboard-interne-web-app)
15. [MiroFish — le projet vision](#15-mirofish--le-projet-vision)
16. [Swarm Intelligence — MiroFish / OASIS](#16-swarm-intelligence--mirofish--oasis)
17. [La concurrence — analyse détaillée](#17-la-concurrence--analyse-détaillée)
18. [SEO & présence digitale](#18-seo--présence-digitale)
19. [LinkedIn & personal brand](#19-linkedin--personal-brand)
20. [Business model & roadmap financière](#20-business-model--roadmap-financière)
21. [Roadmap technique par phase](#21-roadmap-technique-par-phase)
22. [Risques et mitigations](#22-risques-et-mitigations)
23. [Le flywheel](#23-le-flywheel)
24. [Brand voice & identité](#24-brand-voice--identité)
25. [North Star & métriques clés](#25-north-star--métriques-clés)

---

## 1. Identité, mission, vision

### Qui est Brantham Partners

**Brantham Partners** est un cabinet M&A spécialisé exclusivement dans les **entreprises en difficulté** (PME France). C'est une startup pré-revenue fondée par Paul Roulleau, combinant expertise M&A traditionnelle et infrastructure technologique avancée (IA, agents autonomes, modèles prédictifs).

Brantham ne fait **pas** du conseil généraliste, ne s'occupe **pas** des entreprises saines, et ne cherche **pas** à faire de la marketplace passive. C'est un acteur proactif qui va chercher les opportunités avant que tout le monde les voit.

### Mission

> Identifier, analyser, structurer et fermer des opérations de cession d'entreprises en procédure collective en France — plus vite et mieux que n'importe quel acteur humain du marché.

### Vision

> **Devenir le système nerveux du M&A distressed en France.** Chaque PME viable en procédure collective a un repreneur identifié et contacté en 48h.

Pas dans 5 ans. C'est ce qu'on construit maintenant.

### Statut actuel (mars 2026)

| Indicateur | Valeur |
|---|---|
| Revenue | **0 EUR** (pre-revenue) |
| Deals actifs | 1 (MLD) |
| Deals archivés | 600+ |
| Procédures en base | 184K+ |
| Records BODACC | 1.8M |
| Agents LLM opérationnels | 6 |
| Pipeline FastAPI | 3900+ lignes |
| Score SEO | 93/100 |

---

## 2. Le marché : M&A distressed en France

### Taille et volume

La France est un marché particulièrement actif pour les procédures collectives, alimenté par un cadre légal précis (Code de commerce) et une économie composée à 97% de PME/TPE.

| Métrique | Chiffre | Source |
|---|---|---|
| Procédures collectives ouvertes/an | ~70 000 | Altares |
| Dont aboutissant à une cession | ~12 000 | estimation Brantham |
| Fee moyen sur cession PME distressed | 3-8% du prix | marché |
| Prix de cession moyen PME en difficulté | 500K - 5M EUR | Brantham data |
| Marché total fees (estimation) | **~1.2 Md EUR/an** | calcul Brantham |
| Cible réaliste Brantham à 3 ans (1% du marché) | **12M EUR/an** | projection |

### Pourquoi ce marché est attractif

1. **Défaillances structurelles** : Depuis 2024, les défaillances ont rebondi après les années COVID/PGE. Le flux de procédures est prévisible et constant.
2. **Absence de tech** : Le marché est dominé par des acteurs traditionnels (cabinets AJ, mandataires) sans infrastructure data.
3. **Asymétrie d'information extrême** : Les repreneurs potentiels ne savent pas ce qui existe. Les mandataires ne savent pas qui contacter. Brantham comble ce gap.
4. **Urgence systémique** : Les procédures ont des deadlines légales. L'urgence crée de la valeur pour celui qui est en avance.
5. **Niche évitable par les grands** : Les Big 4 (EY, KPMG, Deloitte) ne touchent pas aux PME < 10M EUR. Le terrain est libre.

### Le BODACC — notre source primaire

Le **Bulletin Officiel Des Annonces Civiles et Commerciales (BODACC)** est le registre officiel publié au Journal Officiel. Il contient :
- Toutes les ouvertures de procédures collectives
- Les jugements de cession
- Les radiations d'entreprises
- Les ventes de fonds de commerce

Brantham scrappe et ingère le BODACC **daily à 07h00**, soit des dizaines d'heures avant que les acteurs concurrents l'aient lu manuellement.

### Les acteurs du marché

**Les mandataires judiciaires (MJ)** : représentent les créanciers. Cherchent à maximiser le remboursement du passif.

**Les administrateurs judiciaires (AJ)** : gèrent la période d'observation en RJ. Cherchent le meilleur plan (continuation ou cession).

**Le juge-commissaire** : supervise la procédure au quotidien.

**Le tribunal de commerce** : valide les offres, arbitre entre les plans.

**Les repreneurs** : industriels, fonds PE, family offices, entrepreneurs. Cherchent des opportunités sous-évaluées.

**Brantham** : intermédiation entre MJ/AJ et repreneurs. Le seul acteur data-driven sur ce segment.

---

## 3. Les procédures collectives — cours complet

### Vue d'ensemble

Il existe 5 procédures principales en France, classées par niveau d'urgence et de gravité :

```
Moins grave ←────────────────────────────────────────────────→ Plus grave
Mandat ad hoc  |  Conciliation  |  Sauvegarde  |  RJ  |  LJ
(confidentiel)    (confidentiel)   (publique)   (publique) (publique)
```

Les 3 procédures publiques (Sauvegarde, RJ, LJ) sont publiées au BODACC et constituent le terrain d'action de Brantham.

---

### Sauvegarde (SV)

**Définition** : procédure préventive ouverte à la demande exclusive du dirigeant quand l'entreprise fait face à des difficultés qu'elle ne peut surmonter seule, **avant** cessation de paiements.

**Particularité clé** : seul le dirigeant peut la déclencher. C'est un signal de proactivité, pas d'échec.

**Déroulement** :
1. Demande du dirigeant au tribunal
2. Jugement d'ouverture → gel des poursuites
3. Période d'observation : 6 mois (renouvelable → 12 mois max, exceptionnellement 18 mois)
4. Le dirigeant reste aux commandes (assisté d'un AJ, pas remplacé)
5. Élaboration d'un plan de sauvegarde avec les comités de créanciers
6. Issue : plan de sauvegarde (echeancier remboursement 10 ans max) ou conversion en RJ/LJ

**Scoring Brantham** : 40-60/100. Priorité basse. Peu de cessions en SV (c'est l'objectif opposé). Surveiller les conversions SV→RJ.

**Ce que ça signifie pour nous** : opportunité limitée à court terme. En revanche, un dirigeant en SV est accessible, coopératif, et peut chercher un partenaire stratégique (adossement partiel) même sans cession totale.

| Aspect | Détail |
|---|---|
| Cessation de paiements | Non |
| Initiative | Dirigeant seul |
| Dirigeant | Reste aux commandes |
| Objectif | Continuation et restructuration |
| Cession | Rare |
| Image | Positive ("proactif") |

---

### Redressement Judiciaire (RJ)

**Définition** : procédure collective curative. L'entreprise est en cessation de paiements (≤ 45 jours pour déposer le bilan) mais un redressement est envisageable. Objectif : poursuivre l'activité, maintenir l'emploi, apurer le passif.

**Déroulement** :
1. Ouverture (par le dirigeant, un créancier, ou le tribunal)
2. Période d'observation : 6-18 mois
   - L'activité continue
   - L'AJ évalue la situation
   - Bilan économique et social obligatoire
3. Issue : 3 scénarios
   - **Plan de continuation** : restructuration, remboursement étalé
   - **Plan de cession** : vente totale ou partielle à un repreneur → OPPORTUNITÉ BRANTHAM
   - **Conversion en LJ** : si redressement impossible

**Scoring Brantham** : 60-80/100. +10 si plan de cession annoncé. -10 si plan de continuation probable.

**Atouts du RJ pour Brantham** :
- Entreprise encore en activité (clients, salariés, fournisseurs toujours là)
- Plus de temps pour une due diligence sérieuse
- Meilleure qualité d'information (bilans récents, CAC, rapport AJ)
- Going concern : on rachète une entreprise qui tourne

**Risques** :
- Concurrence accrue (plus de temps = plus de repreneurs qui regardent)
- Le tribunal peut préférer la continuation à la cession
- Reprise de tous les salariés (pas de cherry-pick)

| Aspect | Détail |
|---|---|
| Cessation de paiements | Oui |
| Initiative | Dirigeant, créancier, ou tribunal |
| Dirigeant | Sous tutelle AJ |
| Objectif | Redressement ou cession |
| Cession | Fréquente |
| Durée | 6-18 mois d'observation |

---

### Liquidation Judiciaire (LJ)

**Définition** : procédure définitive. Le tribunal prononce la liquidation quand le redressement est manifestement impossible. Tous les actifs sont vendus pour désintéresser les créanciers.

**Déroulement** :
1. Jugement d'ouverture → désignation du liquidateur
2. Inventaire des actifs
3. Appel à offres publié au BODACC
4. Deadline fixée par le juge-commissaire (souvent 2-6 semaines)
5. Réception des offres
6. Sélection par le tribunal (pas forcément la plus haute — emploi compte)
7. Jugement de cession → transfert des actifs
8. Clôture → radiation

**Scoring Brantham** : 80-100/100. Flag URGENT si deadline < 14 jours. LJ toujours prioritaire à score égal.

**Atouts de la LJ pour Brantham** :
- Prix décotés (actifs en dessous de la valeur de marché)
- Moins de concurrence (repreneurs frileux)
- Possible de cherry-pick (machines, marques, clientèle sans reprendre les dettes)
- On négocie avec le liquidateur, pas avec le dirigeant (souvent plus simple)

**Risques** :
- Deadline ultra-courte → pipeline accéléré obligatoire
- Salariés : obligation de reprise selon convention collective
- Passif environnemental possible (peut suivre les actifs)
- Détérioration rapide (pas de maintenance en LJ)
- Le tribunal évalue la solidité du projet repreneur (emploi, continuité)

| Aspect | Détail |
|---|---|
| Cessation de paiements | Oui + redressement impossible |
| Acteur principal | Liquidateur judiciaire |
| Dirigeant | Dessaisi |
| Objectif | Vendre les actifs, rembourser les créanciers |
| Cession | Toujours (c'est l'objet) |
| Durée | 2-6 semaines pour la cession d'actifs |

---

### Tableau comparatif des 3 procédures

| Critère | Sauvegarde | Redressement Judiciaire | Liquidation Judiciaire |
|---|---|---|---|
| Cessation de paiements | Non | Oui | Oui |
| Redressement possible | — | Oui | Non |
| Urgence pour Brantham | Faible | Moyenne | Maximale |
| Score procédure | 40-60 | 60-80 | 80-100 |
| Qualité des actifs | Excellente | Bonne | Variable |
| Temps disponible | 6-18 mois | 6-18 mois | 2-6 semaines |
| Type d'acheteur | Partenaire / investisseur | Repreneur going concern | Acheteur d'actifs |
| Prix | Marché | Légèrement décoté | Très décoté |

---

## 4. L'offre Brantham — services détaillés

### 1. Sourcing propriétaire

Le cœur du différentiateur. Brantham détecte les opportunités avant tout le monde via :
- **BODACC daily** : toutes les nouvelles procédures ingérées à 07h00
- **Scraping AJ** : cabinets BMA, 2M&Associés, et autres publient leurs annonces sur leurs sites — Brantham scrappe automatiquement (5K+ annonces)
- **Early warning signals** : la table `early_warning` détecte des signaux faibles (bilans en dégradation, retards de publication) avant même l'ouverture d'une procédure
- **Scoring auto** : chaque nouvelle procédure est scorée dans les heures qui suivent sa publication

### 2. Analyse & Due Diligence

L'agent **Analyst** produit une analyse complète incluant :
- Contexte sectoriel (code NAF, tendances, marché)
- Analyse financière (bilans INPI, ratios, CA, EBITDA estimé)
- Diagnostic juridique (type de procédure, stade, mandataire, tribunal)
- Évaluation des actifs (immobilier, machines, stocks, PI, marques, clientèle)
- Identification des risques et des atouts
- Recommandation GO/NO-GO avec justification

La dataroom IA permet l'upload de PDF/Excel pour extraction automatique des KPIs clés.

### 3. Valorisation

Estimation de la Valeur d'Entreprise (VE) sur trois niveaux :
- **VE min** : valeur liquidative pure (actifs nets de dettes)
- **VE médiane** : méthode des comparables (multiples sectoriels)
- **VE max** : going concern (DCF simplifié si bilans disponibles)

Sources : multiples sectoriels internes, base `transaction_cession` (historique 600+ deals), et données sectorielles INPI.

### 4. Production de teasers

L'agent **Writer** produit un teaser anonymisé en PPTX et PDF. Structure standard :

1. **Accroche** (2-3 lignes) : hook percutant pour capter l'attention du repreneur
2. **Profil de l'entreprise** (5-8 lignes) : description anonymisée, positionnement, marché
3. **Atouts clés** (3-5 bullets) : points forts différenciants
4. **Contexte de cession** (3-5 lignes) : positivisation de la procédure
5. **Profil recherché** (3-5 lignes) : type de repreneur idéal
6. **Contact** : coordonnées Brantham Partners

**Règles d'anonymisation strictes** :
- Jamais de nom d'entreprise, de dirigeant, ou d'adresse précise
- Localisation : région ou département uniquement
- CA : fourchette si > 2M EUR
- Effectif : fourchette (ex: "15-25 collaborateurs")

**Positivisation des procédures** :
- LJ → "Dans le cadre d'une procédure de cession ordonnée par le tribunal..."
- RJ → "L'entreprise, en phase de restructuration, recherche un repreneur..."
- SV → "Dans une démarche proactive de réorganisation..."

### 5. Matching repreneurs (4D)

Le système de matching score chaque repreneur potentiel sur 4 dimensions :

| Dimension | Description |
|---|---|
| **Financial fit** | Capacité financière, taille cohérente (règle 5-20x), accès au financement |
| **Strategic fit** | Alignement sectoriel (NAF rings), synergies potentielles, positionnement |
| **Track Record** | Historique d'acquisitions, succès passés, experience distressed |
| **Operational fit** | Capacité à reprendre et opérer, géographie, disponibilité |

Base de données : **841K+ scores buyer_match précalculés** dans PostgreSQL.

### 6. Enrichissement des contacts

L'agent **Enricher** valide et enrichit les contacts des repreneurs identifiés :
- Décisionnaires identifiés (nom, poste, email, LinkedIn)
- Numéros directs vérifiés
- Taux de joignabilité estimé
- Alertes si contact outdated

### 7. Négociation & structuration

Accompagnement sur la forme de cession :
- Cession de fonds de commerce vs cession d'actifs (différences juridiques et fiscales)
- Structuration de l'offre (prix, conditions suspensives, garanties)
- Animation des échanges avec le mandataire judiciaire
- Rédaction des lettres d'intention

### 8. Intégration post-reprise

Accompagnement post-closing :
- Transition opérationnelle
- Gestion des salariés repris
- Relations fournisseurs / clients
- Reporting post-acquisition

---

## 5. Le moat — avantage concurrentiel

Brantham a 7 avantages structurels impossibles à répliquer rapidement :

### Avantage #1 — Asymétrie d'information

Brantham score 184K procédures **avant tout le monde**. Le pipeline daily (07h00) garantit que chaque nouvelle procédure est analysée et scorée avant que les acteurs humains aient ouvert le BODACC. C'est une avance de 24-72h systématique sur toutes les opportunités.

### Avantage #2 — Vitesse pipeline

Pipeline Scout → Teaser complet en **quelques heures** vs plusieurs semaines pour un cabinet traditionnel. Le temps est la ressource critique en LJ (deadlines 2-6 semaines). Un cabinet qui met 3 semaines à produire un teaser arrive trop tard.

### Avantage #3 — Prédictions Cox (C-index 0.84)

Le modèle Cox PH, calibré sur 165K+ procédures historiques, produit des probabilités de cession à 3, 6, 9 et 12 mois avec un C-index de **0.84** — discrimination excellente. Cela signifie qu'on sait QUELLES procédures vont aboutir, et on priorise le pipeline en conséquence. Un concurrent sans ce modèle investit du temps sur des deals qui n'aboutiront pas.

### Avantage #4 — Couverture totale

BODACC complet + scraping AJ multi-sites = **rien n'échappe à Brantham**. La table `early_warning` détecte même les signaux avant l'ouverture officielle d'une procédure.

### Avantage #5 — NAF Ring Model

Le modèle de rings NAF (5 rings, supply chain TES, 172K codes) permet un matching sectoriel d'une précision inatteinte. Un repreneur dans le secteur "adjacent ring 2" d'une cible est souvent un meilleur acheteur qu'un concurrent direct (moins de conflit d'intérêts, synergies supply chain).

### Avantage #6 — 841K scores buyer_match précalculés

Pour chaque procédure, des milliers de repreneurs potentiels ont déjà été scorés. L'agent Hunter ne part pas de zéro — il accède à une base de 841K scores précalculés et affinés par les critères spécifiques du deal. Vitesse de mapping = heures, pas jours.

### Avantage #7 — Zéro coût marginal

Une fois le pipeline en place, chaque deal additionnel ne coûte que des tokens LLM. Les concurrents ont des coûts fixes importants (équipes humaines, déplacements, dossiers papier). La scalabilité de Brantham est asymétrique.

---

## 6. Le pipeline opérationnel

Le pipeline Brantham transforme une procédure BODACC brute en opportunité closée via 8 étapes séquentielles.

### Les statuts

| Statut | Description | Agent responsable |
|---|---|---|
| `nouveau` | Découvert par Scout, pas encore analysé | Scout |
| `en_analyse` | Analyst en cours | Analyst |
| `analysé` | Analyse terminée, teaser à rédiger | Director |
| `teaser_redige` | Writer a produit le teaser | Writer |
| `acheteurs_identifies` | Hunter a trouvé les acheteurs qualifiés | Hunter |
| `contacts_enrichis` | Enricher a trouvé les contacts, prêt pour outreach | Enricher |
| `en_approche` | Emails envoyés, en attente de réponse | Paul |
| `clos` | Deal fait, pas d'acheteur trouvé, ou retiré | — |

### Le flux complet

```
BODACC / AJ scraper
       ↓
   Scout détecte
       ↓
   Director évalue (GO/NO-GO selon score)
       ↓
   Analyst analyse (score QC ≥ 7 → Writer)
       ↓
   Writer rédige le teaser PPTX/PDF
       ↓
   Hunter mappe les repreneurs (min 10-20 cibles)
       ↓
   Enricher valide les contacts (taux joignabilité)
       ↓
   Paul (outreach email + suivi)
       ↓
   Mise en relation + structuration + fee
```

### Les règles de priorisation (Director)

Le Director applique un ordre de priorité strict :

1. **Procédure** : LJ > SV > RJ (en termes d'urgence)
2. **Secteur stratégique** : industrie/agro > services
3. **CA** : 1-20M EUR sweet spot
4. **Délai légal restant** : < 14 jours = URGENT, flag rouge
5. **Score total** : ≥ 75 = pipeline complet immédiat

---

## 7. Les 6 agents LLM — comment ça fonctionne

### Architecture agents

L'orchestration est basée sur **server.js** avec 6 agents spécialisés. Le Director est le seul à avoir une vue globale. Les autres agents sont des workers spécialisés.

Stack agents : Claude Opus 4 (decisions complexes), Claude Sonnet 4 (production), Claude Haiku 4 (tâches simples), fallback OpenRouter.

### Scout — Le détecteur

**Rôle** : surveillance continue du BODACC et des sites AJ. Filtre les faux positifs (dossiers trop petits, dates dépassées, hors périmètre).

**Sources** :
- BODACC API officielle (daily 07h00)
- BMA (bma-aj.com) — scraping annonces
- 2M&Associés (aj-2m.com) — scraping annonces
- Autres cabinets AJ (en expansion)

**Output** : mise à jour de `OPPORTUNITIES.md` avec les nouvelles opportunités formatées.

**Filtres automatiques** :
- CA < 100K EUR → archiver
- Date limite dépassée → archiver
- Hors France → archiver
- Doublons → détecter et ignorer

### Director — Le cerveau

**Rôle** : orchestrateur principal. Lit BRAIN.md, PIPELINE.md, OPPORTUNITIES.md, puis agit sans demander la permission.

**Responsabilités** :
1. **Orchestration** : décider du GO/NO-GO sur chaque opportunité
2. **Contrôle qualité (QC)** : scorer chaque output d'agent sur 10, renvoyer si < 7
3. **Auto-amélioration** : analyser les patterns d'échec, proposer des modifications aux IDENTITY.md
4. **Gestion des blocages** : détecter les agents inactifs > 2h et alerter Paul
5. **Rapports** : alerter Paul uniquement quand c'est nécessaire (deal prêt, opportunité exceptionnelle, agent bloqué)

**Commandes Paul → Director** :
- `audit` → analyse complète des scores + propositions améliorations agents
- `statut` → résumé complet du pipeline
- `priorité [slug]` → passer un deal en tête de queue
- `pause [slug]` / `reprendre [slug]` → gestion du flux

**Ce que le Director NE fait PAS** : scrape, analyse, rédige, cherche des acheteurs. Il orchestre.

### Analyst — L'analyste

**Rôle** : analyse approfondie du dossier. Produit la note d'analyse complète qui servira de base au teaser et au mapping acheteurs.

**Input** : fiche opportunité dans OPPORTUNITIES.md + données PostgreSQL (bilans, scoring, historique mandataire).

**Output** : fichier `analyses/[slug].md` avec :
- Contexte sectoriel et marché
- Analyse financière (CA, résultats, ratios)
- Analyse juridique (procédure, stade, mandataire, tribunal)
- Évaluation des actifs
- Risques et atouts
- Recommandation : GO / RISQUÉE MAIS POSSIBLE / À ÉVITER

**QC Director** : score ≥ 7/10 sur : complétude financière, analyse juridique, diagnostic stratégique, recommandation claire.

### Writer — Le rédacteur

**Rôle** : transformer l'analyse en teaser anonymisé percutant. Produit PPTX (via `generate_teaser.py` + `Template Teaser.pptx`) et version email.

**Règles strictes** :
- Jamais de nom propre, d'adresse précise, de chiffre exact si < 2M EUR CA
- Positiviser la procédure (voir section 4)
- Format compact : 1 page pour petits deals, 2 pages pour > 5M EUR CA
- Accroche = la première phrase doit accrocher le repreneur en 5 secondes

**QC Director** : score ≥ 7/10 sur : accroche percutante, clarté, longueur, appel à l'action.

### Hunter — Le chasseur

**Rôle** : identifier et mapper les repreneurs potentiels. Min 10-20 cibles par deal.

**Sources** :
- Base `buyer_match_score` (841K+ scores précalculés)
- BODACC historique (repreneurs passés sur deals similaires)
- Pappers / Société.com (structure capitalistique, dirigeants)
- NAF adjacent API
- LinkedIn (décisionnaires)
- PitchBook / Dealroom (pour PE/VC)

**Classification ABC** :
- **Grade A** : même secteur, bonne taille, historique d'acquisitions, géographie compatible → cible 3-5 par deal
- **Grade B** : secteur adjacent, taille ok, intérêt potentiel → 5-10 par deal
- **Grade C** : financier pur ou secteur éloigné → 5-10 par deal

**Règle de taille** : le repreneur idéal a 5 à 20x la taille du deal en CA. Un repreneur trop petit = pas les moyens. Trop gros = pas intéressé.

**QC Director** : score ≥ 7/10 sur : pertinence sectorielle, taille cohérente, nombre ≥ 10, priorisation.

### Enricher — Le validateur

**Rôle** : valider et enrichir les contacts des repreneurs identifiés par Hunter.

**Output** : fichier `contacts/[slug]-contacts.json` avec pour chaque repreneur :
- Décisionnaire identifié (nom, poste)
- Email vérifié
- Téléphone direct si disponible
- LinkedIn
- Taux de joignabilité estimé
- Date de vérification

**QC Director** : score ≥ 6/10 sur taux de contacts joignables et qualité des décisionnaires.

---

## 8. Le scoring 9D — détail complet

### Vue d'ensemble

Chaque procédure collective est scorée automatiquement sur 100 via 9 composantes pondérées. Le score est calculé par `scorers/qualification.py` lors du pipeline daily.

```python
score_total = sum(composante_i * poids_i for i in 1..9)
```

### Les 9 composantes

| # | Composante | Poids | Range | Logique |
|---|---|---|---|---|
| 1 | **Taille** | **30%** | 0-100 | Sweet spot : PME 1-50M EUR CA, 10-200 salariés. Sous 500K = faible (peu de fees). Sur 50M = hors périmètre (Big 4 prennent). |
| 2 | **Secteur** | **25%** | 0-100 | Attractivité du code NAF. Industrie manufacturière (A à E) = 80-100. Agro-alimentaire = 85-100. Services génériques (consulting) = 30-40. |
| 3 | **Procédure** | **20%** | 0-100 | LJ = 80-100 (urgence = opportunité décotée). RJ plan de cession = 60-80. SV = 40-60. |
| 4 | **Fraîcheur** | **5%** | 0-100 | < 30 jours depuis le jugement = 100. 30-90 jours = 75. 90-180 jours = 40. > 180 jours = 0. |
| 5 | **Localisation** | **5%** | 0-100 | Bassins économiques denses = score élevé. ÎdF, Nord, Auvergne-Rhône-Alpes = 70-90. Zones rurales isolées = 30-50. |
| 6 | **Effectif** | **5%** | 0-100 | Optimal : 10-100 salariés (assez gros pour intéresser un repreneur, assez petit pour gérer). < 5 = 30. > 200 = 60 (trop gros). |
| 7 | **AFDCC** | **5%** | 0-100 | Score de défaillance AFDCC si disponible. Inversé : un AFDCC élevé = score Brantham faible (entreprise déjà très mal). |
| 8 | **Mandataire** | **3%** | 0-100 | Track record du MJ/AJ : taux de cession historique, délai moyen, volume. Les bons mandataires facilitent, les mauvais bloquent. |
| 9 | **Actifs** | **2%** | 0-100 | Qualité et valeur identifiée des actifs : immobilier, machines industrielles, brevets, marques, clientèle. |

### Seuils de décision

| Score | Action Director | Description opérationnelle |
|---|---|---|
| **75+** | URGENT | Pipeline complet lancé immédiatement. Analyst + Writer + Hunter en parallèle. Alert Paul si deadline < 7j. |
| **60-74** | LAUNCH | Pipeline standard séquentiel : Analyst → Director QC → Writer → Hunter → Enricher. |
| **50-59** | WATCH | Surveillance. Reval auto si nouveau BODACC sur la même entreprise. Pas de ressources allouées. |
| **< 50** | ARCHIVE | Archivage en base. Consultable mais inactif. |

### Gestion du CA manquant

Le CA n'est pas toujours disponible dans les premières heures post-publication. Règles :
1. Estimer depuis les actifs mentionnés
2. Estimer depuis le secteur (CA/salarié moyen NAF)
3. Estimer depuis l'effectif si connu
4. Utiliser l'estimation médiane avec flag `"estime"` en base
5. Jamais bloquer le scoring pour un CA manquant

### Le modèle Cox PH — prédictions temporelles

En complément du score instantané, un modèle de survie (Cox Proportional Hazards) produit des probabilités de cession dans le temps :

| Métrique | Description |
|---|---|
| `prob_cession_3m` | Probabilité de cession dans les 3 prochains mois |
| `prob_cession_6m` | Probabilité de cession dans les 6 prochains mois |
| `prob_cession_9m` | Probabilité de cession dans les 9 prochains mois |
| `prob_cession_12m` | Probabilité de cession dans les 12 prochains mois |
| **C-index** | **0.84** — discrimination excellente (> 0.80 = excellent) |

**Variables du modèle Cox** : type_procedure, ca, effectif, secteur, age_entreprise, localisation, mandataire_track_record.

**Backtest** : 165K+ lignes dans `backtest_scoring`. Comparaison score à date T vs outcome réel (cession oui/non, délai).

---

## 9. Le matching acheteurs 4D

### Principe

Pour chaque procédure active, le système identifie les repreneurs potentiels dans la base et les score sur 4 dimensions.

### Les 4 dimensions

**Dimension 1 — Financial fit (poids 25%)**
- Capacité financière disponible (estimation depuis CA repreneur)
- Règle 5-20x : le repreneur idéal a 5 à 20 fois la taille de la cible
- Accès au financement (historique d'acquisitions récentes)
- Pas de dette excessive propre

**Dimension 2 — Strategic fit (poids 30%)**
- Alignement sectoriel via NAF Ring Model :
  - Ring 0 : même code NAF (concurrent direct)
  - Ring 1 : secteur immédiatement adjacent (substituts/compléments)
  - Ring 2 : secteur lié supply chain (fournisseurs/clients)
  - Ring 3-4 : moins pertinent mais possible
- Synergies identifiées : clients, géographie, production, technologie
- Build-up sectoriel en cours (consolidateur actif ?)

**Dimension 3 — Track Record (poids 20%)**
- Nombre d'acquisitions passées documentées
- Succès vs échecs (outcomes connus)
- Expérience spécifique distressed (reprises à la barre, LJ)
- Taille des deals antérieurs (cohérente avec la cible)

**Dimension 4 — Operational fit (poids 25%)**
- Proximité géographique (même région = avantage)
- Capacité opérationnelle à reprendre (management disponible)
- Équipe intégration existante
- Secteur déjà géré ou à apprendre

### La base buyers

**841K+ scores buyer_match précalculés** dans PostgreSQL pour les combinaisons cible × repreneur. Ces scores sont recalculés chaque semaine via le weekly pipeline.

**143 repreneurs réels** documentés en base avec historique d'acquisitions, préférences sectorielles et capacité financière estimée.

---

## 10. Les deals — historique et actifs

### Pipeline actuel (mars 2026)

| Deal | Statut | Secteur | CA | Deadline | Priorité |
|---|---|---|---|---|---|
| **MLD** (Multi Loisirs Distribution) | `teaser_redige` | Véhicules de loisirs | < 1M EUR | 17/03/2026 | Haute |

### MLD — détail complet

**Entreprise** : MULTI LOISIRS DISTRIBUTION-MLD
**Localisation** : Cuinchy (62 Pas-de-Calais)
**Secteur** : Vente et location de véhicules de loisirs (camping-cars, caravanes, vans aménagés)
**Procédure** : Cession d'actifs (LJ)
**Source AJ** : Cabinet BMA
**Découverte** : 19 février 2026
**Deadline** : 17 mars 2026

**Pourquoi c'est intéressant** :
- Secteur vanlife / camping-car en croissance post-COVID (+10%/an)
- Bassin Nord de France dense (proximité Lille, axe A26)
- Actifs : stock véhicules, atelier/local commercial, fichier clients, marque locale
- Cession d'actifs = prix décoté, pas de reprise du passif

**Profils repreneurs ciblés** :
- **A (stratégique)** : concessionnaires véhicules loisirs régionaux/nationaux, groupes distribution auto avec diversification loisirs, loueurs camping-cars cherchant à intégrer la vente
- **B (adjacent)** : concessionnaires auto généralistes, spécialistes plein air/outdoor, réparateurs/aménageurs de vans
- **C (financier)** : family offices avec portefeuille auto/loisirs, entrepreneurs en reconversion (budget < 500K EUR)

**Historique pipeline** :
- 19/02 → Scout : découverte
- 19/02 → Director : qualification GO
- 20/02 → Analyst : analyse complétée
- 21/02 → Writer : teaser rédigé
- EN ATTENTE : Hunter (mapping acheteurs)

### Deals archivés (600+)

Historique complet disponible dans `/Users/paul/brantham-vault/`. Quelques exemples représentatifs :

| Deal | Secteur | CA | Statut final | Recommandation |
|---|---|---|---|---|
| D&L Commerce (Ecomiam) | Surgelés (3 magasins, 35) | ~2M EUR | teaser_redige | RISQUÉE MAIS POSSIBLE |
| GAB France Retail (Scotch & Soda) | Retail mode premium (13 magasins) | NC | teaser_redige | RISQUÉE — reconversion nécessaire |
| Breizhou Restauration | Restauration collective bio | ~480K EUR | analysé | À ÉVITER — date dépassée |
| GP Restauration | Restauration (59 Nord) | 1-3M EUR | clos | Date dépassée |
| CJ Diffusion | Menuiseries métalliques | 1,5M EUR | clos | Date dépassée — CA en croissance |
| Wexperience | Agence digitale | 680K EUR | clos | Date dépassée — baisse CA |
| Lilliris | Photographie artistique | 64K EUR | clos | Trop petit pour Brantham |
| Securinter | Sécurité téléphonique | 724K EUR | clos | Date dépassée |
| Artemis (Hippopotamus) | Restauration franchise | < 1M EUR | teaser_redige | RISQUÉE — délai très court |
| Alphosa | Deals actifs buyers mapping | — | en cours | — |

**Secteurs les plus fréquents dans le flux AJ** :
1. Restauration (le plus courant dans les cabinets AJ)
2. Retail/commerce de détail
3. Menuiseries/BTP
4. Services numériques
5. Véhicules/mobilité
6. Agro-alimentaire

---

## 11. Architecture technique complète

### Stack global

| Layer | Technology | Version | Usage |
|---|---|---|---|
| Backend API | Python + FastAPI | 3.12+ / FastAPI last | 3900+ lignes, 10+ routes |
| Base de données | PostgreSQL | 16 | 43 tables, 1.8M records |
| Cache / Queue | Redis | 7 | Cache queries, file d'attente agents |
| Orchestration pipeline | Prefect | — | Daily/weekly/monthly flows |
| Frontend (internal tool) | React + Vite + TypeScript | 19 / 7 / 5.9 | Dashboard interne Paul |
| State management | Zustand | 5 | 5 stores |
| Router | React Router | 7 | 13 pages |
| LLM (agents) | Anthropic Claude | Opus 4, Sonnet 4, Haiku 4 | Agents LLM + fallback OpenRouter |
| LLM local (swarm) | Ollama / llama-cpp-python | — | qwen2.5:7b, Metal (M5) |
| Conteneurisation | Docker Desktop | — | postgres, redis, pgadmin |
| Agent orchestration | server.js (Node) | — | 6 agents, handoff protocol |
| Simulation engine | Python + MLX | — | MiroFish, 995K agents |
| Frontend Next.js (site web) | Next.js | — | brantham-next/ |

### Déploiement

| Environnement | Infra | Services |
|---|---|---|
| Développement | Local macOS (M5) | Tout en local, Docker Desktop |
| Production backend | Hetzner VPS (95.216.198.143) | FastAPI + PostgreSQL + Redis |
| Production frontend (site public) | Vercel | Next.js SEO website |
| Production frontend (internal) | Local ou VPS | React dashboard |
| Cron pipeline | launchd macOS | `com.brantham.daily.plist` à 07h00 |

### Flux de données complet

```
BODACC API (officielle)
AJ scrapers (BMA, 2M&Associés...)
         ↓
  [Prefect Pipeline - 07h00]
  Step 0 : setup_schema
  Step 1 : bodacc_collectors
  Step 2 : ingest + déduplication
  Step 3 : SIRENE enrichment
  Step 4 : géocodage
  Step 5 : scoring 9D
  Step 6 : bilan_ratios (INPI)
  Step 7 : dossier_complet (84K)
  Step 8 : refresh materialized views
  Step 9 : stats + Cox PH + backtest + early warning + buyer match
         ↓
  PostgreSQL 16 ←→ Redis 7
         ↓
  FastAPI Backend (3900 lignes)
  ├── /api/opportunities → top deals
  ├── /api/score → scoring
  ├── /api/repreneurs/match → buyer match
  ├── /api/swarm → swarm intelligence
  ├── /api/agents → statuts agents
  └── SSE endpoints (temps réel)
         ↓
  ┌─────────────────────┬─────────────────────┐
  │ React Dashboard     │  Agent Pipeline      │
  │ (internal-tool)     │  (server.js)         │
  │                     │  ├── Scout           │
  │ Pipeline Kanban     │  ├── Director        │
  │ Chat agents         │  ├── Analyst         │
  │ Veille deals        │  ├── Writer          │
  │ Swarm page          │  ├── Hunter          │
  │ Repreneurs          │  └── Enricher        │
  └─────────────────────┴─────────────────────┘
```

### PostgreSQL — configuration importante

> **ATTENTION** : brew PostgreSQL@16 auto-restart via launchd. Toujours l'arrêter proprement avant de lancer le container Docker (conflit de ports) :
> ```bash
> pg_ctl stop -D /opt/homebrew/var/postgresql@16 -m fast
> ```

---

## 12. Le data pipeline — 9 étapes

Le pipeline Prefect s'exécute **chaque jour à 07h00** via launchd (`com.brantham.daily.plist`).

### Étapes du pipeline daily

| Step | Nom | Description | Output |
|---|---|---|---|
| 0 | `setup_schema` | Vérification/migration schéma PostgreSQL | Schema à jour |
| 1 | `bodacc_collectors` | Collecte BODACC (procédures, ventes, radiations) | Nouvelles annonces brutes |
| 2 | `ingest` | Ingestion + déduplication des nouvelles annonces | Records PostgreSQL |
| 3 | `sirene_enrichment` | Enrichissement SIRENE (nom, NAF, effectif, CA) | `entreprise` table |
| 4 | `geocoding` | Géocodage des adresses entreprises | lat/lon dans `entreprise` |
| 5 | `scoring` | Calcul des scores 9 composantes | `score_qualification` table |
| 6 | `bilan_ratios` | Calcul des ratios financiers depuis bilans INPI | `bilan_ratios` table |
| 7 | `dossier_complet` | Construction des dossiers enrichis complets (84K) | `dossier_complet` table |
| 8 | `refresh_views` | Rafraîchissement des materialized views | `mv_top_opportunites`, `mv_distressed_ma` |
| 9 | `stats_and_predictions` | Stats mandataires/tribunaux + Cox PH + backtest + early warning + buyer match + IBSE + cleanup | `cox_predictions`, `stats_mandataire`, `early_warning`, `buyer_match_score` |

### Pipeline weekly (chaque dimanche)

- Matrices de corrélation sectorielles
- Full refresh des materialized views
- Analyse de saisonnalité
- Buyer match re-run complet (recalcul 841K scores)

### Pipeline monthly (1er du mois)

- IBSE sectoriel (Indicateur de Stress par Secteur)
- Sector stress index update
- Rapport mensuel complet

---

## 13. La base de données — schéma complet

### Volumétrie

| Métrique | Volume |
|---|---|
| Tables | 43+ |
| Records BODACC | 1.8M |
| Procédures collectives | 184K |
| Bilans financiers | 194K |
| Dossiers complets | 84K |
| Buyer match scores | 841K |
| Backtest scoring | 165K+ lignes |

### Tables core

| Table | Colonnes clés | Description |
|---|---|---|
| `procedure_collective` | id, siren, type_procedure, date_jugement, tribunal, mandataire, statut | 184K procédures RJ/LJ/SV actives et historiques |
| `entreprise` | siren, denomination, naf, effectif, ca_dernier, adresse, lat, lon | Fiches enrichies SIRENE + géocodage |
| `bodacc_annonce` | id, type, siren, date_parution, contenu, source_url | 1.8M annonces BODACC brutes |

### Tables scoring & prédictions

| Table | Colonnes clés | Description |
|---|---|---|
| `score_qualification` | siren, score_total, score_taille, score_secteur, score_procedure, score_fraicheur, score_localisation, score_effectif, score_afdcc, score_mandataire, score_actifs, date_calcul | Score 9D par procédure |
| `cox_predictions` | siren, prob_cession_3m, prob_cession_6m, prob_cession_9m, prob_cession_12m, c_index | Probabilités de cession temporelles |
| `backtest_scoring` | siren, score_date, score_value, outcome, outcome_date | 165K+ lignes de backtest historique |
| `early_warning` | siren, signal_type, signal_date, severity, details | Signaux d'alerte précoce |
| `ibse_sectoriel` | naf, date, stress_index, nb_procedures, tendance | Indicateur de stress sectoriel |

### Tables financières

| Table | Colonnes clés | Description |
|---|---|---|
| `bilan_ratios` | siren, exercice, ca, resultat_net, ebitda, ratio_endettement, ratio_liquidite, ratio_solvabilite, bfr, tresorerie | Ratios calculés depuis 194K bilans INPI |
| `transaction_cession` | id, siren, date_cession, prix, type_cession, repreneur_siren | Historique des cessions réalisées |

### Tables matching & intelligence

| Table | Colonnes clés | Description |
|---|---|---|
| `buyer_match_score` | target_siren, buyer_siren, match_score, match_type, sector_fit, size_fit, geo_fit | 841K+ scores matching acheteur/cible |
| `stats_mandataire` | mandataire, nb_procedures, nb_cessions, taux_cession, delai_moyen | Track record par mandataire judiciaire |
| `stats_tribunal` | tribunal, nb_procedures, nb_cessions, taux_cession, secteurs_top | Track record par tribunal de commerce |
| `dossier_complet` | siren, denomination, secteur, ca, effectif, score, procedure, mandataire, synthese | 84K dossiers enrichis complets |

### Materialized views

| View | Description | Refresh |
|---|---|---|
| `mv_top_opportunites` | Top opportunités qualifiées (score > 60, procédure active) | Daily |
| `mv_distressed_ma` | Vue consolidée M&A distressed (dossier + score + prédiction) | Daily |

### Index principaux

Sur : `siren`, `date_jugement`, `type_procedure`, `score_total`, `naf`, `tribunal`, `mandataire`

---

## 14. Le dashboard interne (web app)

### Statut (mars 2026)

| Métrique | Valeur |
|---|---|
| Pages | 13 |
| Components | 28 |
| Stores Zustand | 5 (agents, opportunities, ui, chat, sync) |
| LOC total (src/) | ~15K |
| Tests | 0 |
| Maturité globale | ~60% |

### Pages disponibles

| Page | Description | État |
|---|---|---|
| Dashboard | KPI globaux, pipeline summary, activité | Charts vides (hasChartData = false) → à corriger |
| Pipeline | Kanban drag-and-drop par statut | Fonctionne bien |
| Veille | Liste des deals scorés + filtres + appel agents | Fonctionne bien |
| Dossier | Vue complète d'un deal (monolithe 1206 lignes) | Fonctionnel mais à découper |
| Agents | 6 agents, avatars, cards, drawer, status | Fonctionne bien |
| Chat | Conversationnel avec les agents | Fonctionne bien |
| Activity | Feed SSE temps réel | Fonctionne bien |
| Swarm | Predictions swarm, timeline, agents (3 tabs) | Nouveau, fonctionnel |
| Office | Canvas cosmétique | Pas de vraie fonctionnalité |
| Memory | Affichage vault | Basique |
| Analyse | Dataroom IA | Dépend backend |
| Repreneur | Table buyers | Basique, sans filtres avancés |
| Suivi | Liste contacts/emails | Simple |

### Roadmap webapp (6 phases)

**Phase 1 — Stabilisation** : splitter DossierPage (1206 lignes → 7 sous-composants), fixer Dashboard charts, error boundaries, loading states.

**Phase 2 — Polish UI** : responsive mobile, DataTable réutilisable, dark mode, Command Palette (Ctrl+K), animations.

**Phase 3 — Features core** : Dashboard V2 (KPIs cliquables, funnel, heatmap), Dataroom page, Email composer upgrade, Repreneur V2, Notification center.

**Phase 4 — Swarm integration** : SwarmBadge sur tous les deals, onglet Swarm dans Dossier, ensemble scoring visible, swarm auto-run nuit.

**Phase 5 — Robustesse** : tests E2E Playwright, tests unitaires Vitest, auth réelle (JWT), offline resilience, performance.

**Phase 6 — Avancé** : multi-user, portail mandataire, real-time collab, AI copilot, PWA, export reports, analytics.

---

## 15. MiroFish — le projet vision

### Qu'est-ce que MiroFish

MiroFish est le projet d'envergure long-terme de Brantham : un **simulateur de monde M&A distressed** fonctionnant à grande échelle avec des agents autonomes.

**Analogie** : SimCity pour le M&A distressed. Un monde virtuel où des milliers/millions d'agents (repreneurs, mandataires, tribunaux, banques, salariés) vivent, interagissent, et prennent des décisions — et où les patterns émergents révèlent des vérités sur le marché réel.

**Ce que ce N'EST PAS** : un prediction market (pas des agents qui votent). C'est un environnement simulé où les conclusions émergent des interactions.

### Performances actuelles (v0.3 — mars 2026)

| Métrique | Valeur |
|---|---|
| Agents simulés | 995K |
| Rounds | 100 |
| Temps total | **83.4 secondes** |
| Vitesse | 0.83s/round sur M5 |
| Modèle distillé | MLP 4293 params |
| Accuracy | 83.9% |
| Taille modèle | 17.2 KB |
| MLX GPU inference | **0.117s pour 1M agents** |
| Scénarios préconfigurés | 7 |

### Scénarios préconfigurés

1. `baseline` : conditions normales 2024
2. `crise_2008` : récession brutale, défaillances +80%
3. `boom_2021` : boom post-COVID, liquidités abondantes
4. `hausse_taux` : environnement taux élevés (BCE)
5. `reforme` : réforme des procédures collectives
6. `desert` : désertification d'un bassin économique
7. `million_agents` : stress test scale

### Les agents simulés

| Type | Nombre | Comportement |
|---|---|---|
| Repreneurs industriels | Milliers | Cherchent acquisitions stratégiques dans leur secteur |
| Fonds PE / LBO | Centaines | Tickets plus gros, critères financiers stricts |
| Family offices | Centaines | Long terme, secteurs spécifiques, conservateurs |
| Serial acquirers | Dizaines | Agressifs, multi-secteur, volume |
| Mandataires judiciaires | Centaines | Gèrent les procédures, cherchent repreneurs, deadlines |
| Tribunaux de commerce | Dizaines | Valident/refusent les offres |
| Banques / créanciers | Centaines | Intérêts financiers, négocient les dettes |
| Salariés / CSE | Milliers | Préférence maintien emploi |
| Conseillers M&A | Centaines | Intermédiaires |
| Concurrents | Variable | Réagissent aux acquisitions dans leur secteur |

**Architecture hybride** :
- 99% agents légers : rule-based, heuristics, decision trees → rapides, scalables
- 1% agents LLM : qwen/llama local pour les décisions complexes

### Ce que produit MiroFish

**Dynamiques de marché** :
- Taux de cession par secteur/taille/région
- Délai moyen détection → cession
- Prix d'équilibre par type de deal
- Nombre moyen d'offres par deal

**Stratégies optimales** :
- Quel profil de repreneur réussit le mieux sur quel type de deal ?
- Timing optimal pour faire une offre
- Prix optimal vs prix de marché

**Scénarios what-if** :
- "Que se passe-t-il si les défaillances augmentent de 30% ?"
- "Impact d'une hausse des taux sur le M&A distressed ?"
- "Si on double le nombre de PE actifs, les prix montent de combien ?"

**Prédictions sur deals réels** :
- Injecter un vrai deal dans l'environnement → observer comment les agents réagissent
- P(cession), profil acheteur probable, prix estimé, timeline

**Intelligence de marché** :
- Secteurs "chauds" (sur-demande) vs "froids" (sous-demande)
- Gaps géographiques (régions mal couvertes)
- Inefficiences de marché exploitables

### Le moat MiroFish

Le simulateur est irréplicable sans :
1. **La data** : 184K procédures + outcomes + financials + acteurs réels
2. **Les règles calibrées** : paramètres du monde validés contre la réalité
3. **Les profils agents** : basés sur les vrais acteurs du marché (143 acheteurs réels)
4. **L'historique de calibration** : chaque simulation passée améliore la suivante

*C'est le seul outil au monde qui permet de "jouer" le marché M&A distressed français en simulation avant d'y participer pour de vrai.*

---

## 16. Swarm Intelligence — MiroFish / OASIS

### Concept

Simuler un marché M&A avec des agents LLM autonomes qui évaluent, biddent et négocient des deals. Le consensus émergent de 25-50 agents produit un signal prédictif complémentaire au scoring quantitatif.

**Analogie** : ce que Polymarket fait avec des parieurs humains, le swarm le fait avec des agents LLM spécialisés — chacun a un profil, une thèse, des contraintes de capital. Le prix de marché émergent = probabilité de cession.

### État actuel (v0.1)

| Composant | État |
|---|---|
| 7 ActionTypes (BID, WATCH, PASS, DD, NEGOTIATE, WITHDRAW, DO_NOTHING) | ✅ |
| 27 archétypes investisseurs + import buyers réels depuis PostgreSQL | ✅ |
| DealMarketplacePlatform avec SQLite trace + agrégation consensus | ✅ |
| SwarmRunner séquentiel via llama-cpp-python (qwen2.5:7b) | ✅ |
| 5 endpoints API (/swarm/run, /status, /predictions, /timeline, /agents) | ✅ |
| Frontend SwarmPage (3 tabs) | ✅ |

**Limitation principale** : ~8s/agent/round → 25 agents × 12 rounds = ~40 minutes. Trop lent pour la production.

### Roadmap swarm

**v0.2 (avril 2026)** : batched inference (5-10x plus rapide), agent memory (les agents se souviennent des derniers 3 rounds), inter-agent visibility ("3 bids sur ce deal, avg 2.5M"), streaming SSE.

**v0.3 (mai-juin 2026)** : phases de deal (Discovery → DD → Bid → Negotiation → Close), coût de DD, sealed bid auction, agent mandataire avec reserve price, information asymmetry (tier 1/2/3).

**v0.4 (juillet-août 2026)** : backtest sur 600+ deals archivés, Brier score tracking, agent weight learning (ceux qui ont raison pèsent plus), intégration ensemble (swarm 15-30% du score final), confidence intervals.

**v0.5 (sept-oct 2026)** : reputation system, herding detection, network effects entre agents, agent evolution, coalition detection, market sentiment index.

**v1.0 (2027)** : vrais acheteurs comme agents, simulation continue (always-on), price discovery, white-label API.

### Intégration scoring ensemble (cible)

```
P(cession) = 0.25 × Monte-Carlo
           + 0.30 × Cox PH
           + 0.15 × Bayesian
           + 0.15 × Swarm
           + 0.15 × AgentMath
```

### Métriques de succès par version

| Phase | Métrique | Cible |
|---|---|---|
| v0.2 | Temps simulation 25 agents × 12 rounds | < 5 min |
| v0.3 | Deals avec price discovery | > 60% |
| v0.4 | Brier score swarm vs coin flip (0.25) | < 0.20 |
| v1.0 | Corrélation swarm P(cession) vs outcome réel | > 0.70 |

---

## 17. La concurrence — analyse détaillée

### Positionnement concurrentiel

| Acteur | Modèle | Contenu distressed | Tech | Audience |
|---|---|---|---|---|
| **Brantham Partners** | Data + IA + speed | **Core business** | Avancée | PME en procédure |
| La Boutique PME | Boutique M&A généraliste | **Absent** | Simulateur valorisation | Cédants sains |
| Actoria | Boutique M&A 7 pays | **Absent** | Xtravalue + diagnostics | International |
| In Extenso Finance | Expert-comptable + M&A | **Absent** | Diagnostics | PME généraliste |
| Fusacq | Marketplace M&A | ~5% | Annonces | Acheteurs/vendeurs |
| Repreneurs.com | Data procédures collectives | **Core data** | Veille/alertes | Repreneurs actifs |
| Alvo.market | Startup tech M&A | Minimal | IA matching | TPE < 15M EUR |

### Analyse détaillée des 6 concurrents principaux

#### La Boutique PME (laboutiquepme.com)
- 95+ articles de blog bien structurés, 50+ termes glossaire M&A
- Simulateur valorisation sous-domaine dédié (lead capture déguisée)
- **ZÉRO contenu distressed** — positionnement 100% entreprises saines
- Pas de FAQPage schema malgré des FAQ présentes → rich snippets manqués
- Faiblesses exploitables : zéro distressed, pas de pages géo dédiées, pas de données propriétaires

#### Actoria (actoria.fr)
- 7 pays, Méthode 7P propriétaire, 6500+ acheteurs en base
- Blog peu actif (20-30 articles vs 95+ chez La Boutique PME)
- **ZÉRO contenu distressed**
- Navigation complexe (50+ sous-pages) = UX difficile

#### In Extenso Finance
- 12 bureaux régionaux mais contenu templated (pas de vraie différenciation géo)
- M&A est un sous-produit de leur offre comptabilité
- Seul concurrent à avoir implémenté FAQPage schema correctement
- **ZÉRO contenu distressed**

#### Fusacq
- Marketplace avec 4565+ opportunités, 10 088 acheteurs
- 47K "articles" = en réalité tombstones + profils entreprises + UGC (qualité faible)
- Zéro structured data → SEO technique très faible
- Concurrent direct pour les deals (marketplace), pas juste pour le contenu
- ~5% de contenu distressed

#### Repreneurs.com
- **Seul concurrent spécialisé distressed M&A** — monitoring procédures collectives
- Opéré par Dealing-Room depuis 2016
- Abonnement EXPERT : €34 HT/mois — alertes par secteur, géographie, tribunal
- **Mais** : plateforme data pure, pas de conseil M&A. Zéro thought leadership. Interface 2010.
- Faiblesses : pas d'analyse, pas d'agents, pas de matching. Données brutes sans valeur ajoutée.

#### Alvo.market
- Startup tech ciblant TPE/PME < 15M EUR, 12 000+ utilisateurs
- IA matching, dataroom intégrée, podcast "Alvo Talk"
- 80+ articles mais rythme réduit depuis 2025
- **ZÉRO schema markup** = SEO technique très faible malgré le volume
- Ciblage TPE différent du mid-market Brantham

### Gaps collectifs exploitables

**Gap #1 — Contenu distressed (TOUS les laissent vide)** : Aucune boutique M&A ne publie de contenu éducatif sur redressement judiciaire, sauvegarde, cession à la barre, OPA pre-pack. Brantham = seule référence éditoriale distressed PME.

**Gap #2 — FAQPage schema** : La Boutique PME et Actoria ont des FAQ mais sans JSON-LD → rich snippets manqués. Brantham implémente → featured snippets Google.

**Gap #3 — Tombstone commentary** : Personne ne publie de "deal breakdown" éducatif sur des transactions closes. Format à créer.

**Gap #4 — Contenu géo avec vraie substance** : Personne n'a de vraies landing pages géo avec données sectorielles locales.

**Gap #5 — Données propriétaires** : +41% de visibilité IA pour les sources avec données exclusives (Princeton KDD 2024). Les 184K procédures + scoring = capital éditorial unique.

---

## 18. SEO & présence digitale

### Statut indexation (mars 2026)

**Problème critique identifié** : `site:branthampartners.fr` = 0 résultats Google. Le site est invisible malgré un contenu en avance sur tous les concurrents.

**Cause** : bug dans `robots.txt` (sitemap pointait vers `brantham.fr` au lieu de `branthampartners.fr`) — corrigé.

### Assets SEO disponibles

| Asset | Brantham | Meilleur concurrent |
|---|---|---|
| Pillar pages distressed | 5 (8 500 mots chacune) | **0** (personne) |
| Glossaire | 192 termes (~50K mots) | 45 termes (La Boutique PME) |
| Baromètre défaillances | Oui + Dataset schema | Non |
| FAQ schema | 8-10 par page | 3-8 (LegalStart seulement) |
| Schema markup types | 6+ (Article, FAQ, HowTo, Breadcrumb, DefinedTerm, Dataset) | 4 max |
| Pages service distressed | 4 | 1 page vide (8 Advisory = 404) |
| AI infrastructure | llms.txt + robots.txt 9 AI bots + speakable | **0** (personne) |

### La formule qui fait ranker (reverse-engineered)

1. **3 000-5 000+ mots** = prérequis pour top 3
2. **Citations Code de commerce** (L.642-x) = signal E-E-A-T #1 en juridique FR
3. **Auteur nommé + credentials** = obligatoire
4. **FAQ Schema** 5-10 questions = arme featured snippets
5. **Tableaux comparatifs** = format préféré des AI
6. **Dates fraîches** (2025-2026) = avantage vs contenu 2020
7. **H2 en format question** = match PAA direct
8. **Liens Legifrance** = signal autorité facile
9. **Maillage interne 10+** liens par page = topical authority
10. **Données propriétaires** = +41% visibilité IA (Princeton KDD 2024)

### Données GEO/AI (Generative Engine Optimization)

| Facteur | Impact sur visibilité IA |
|---|---|
| Statistiques dans le contenu | +41% |
| Citations d'experts | +30% |
| Sites peu connus + citations sources | +115% |
| Schema structured data | +30-36% dans AI Overviews |
| Corrélation DA/citation AI | r=0.18 (faible — qualité > autorité) |

**Distribution des citations IA** :
- Google AI Overviews : blogs dominent (46%)
- ChatGPT : Wikipedia (27%), news (27%), blogs (21%)
- Perplexity : blogs (38%), news (23%)

### Stratégie SEO (6 clusters thématiques)

1. Procédures collectives (RJ, LJ, SV — contenu juridique profond)
2. M&A distressed (cession à la barre, OPA pre-pack, reprise en LJ)
3. Guides repreneurs (comment reprendre, financer, due diligence)
4. Cas d'usage sectoriels (industrie, restauration, retail, tech)
5. Géographique (clusters par région : ÎdF, Hauts-de-France, AURA...)
6. Baromètre / data (défaillances mensuelles, tendances, chiffres exclusifs)

---

## 19. LinkedIn & personal brand

### Contexte

**Fondateur** : Paul Roulleau
**Situation LinkedIn (mars 2026)** : 0 post publié, zéro présence personal brand.

**Pourquoi c'est critique** :
- 90% des deals M&A viennent de referrals
- LinkedIn profil perso = 8x plus d'engagement qu'une page entreprise
- 95% des decision-makers sont plus réceptifs à l'outreach si le contactant publie du thought leadership
- Algorithme 2026 : 65% du feed = profils perso, 5% = pages entreprise

### Architecture de la stratégie

```
PROFIL PERSO (Paul)          PAGE ENTREPRISE (Brantham)
= 80% de l'effort            = 20% de l'effort
= Moteur de visibilité       = Proof point / crédibilité
= Générateur de confiance    = Hub de conversion
= Deal flow inbound          = Republication des best posts
```

### Piliers de contenu (7 thèmes)

| # | Pilier | Type | Fréquence |
|---|---|---|---|
| 1 | Pédagogie procédures | Éducatif | 2x/mois |
| 2 | Signaux faibles | Éducatif | 2x/mois |
| 3 | Études de cas anonymisées | Éducatif | 2x/mois |
| 4 | Macro & tendances | Thought leadership | 2x/mois |
| 5 | Coulisses du métier | Thought leadership | 1x/mois |
| 6 | Dimension humaine | Personnel | 1x/mois |
| 7 | Opinions contrarian | Thought leadership | 1x/mois |

### Formats et performances

| Format | Engagement | Usage |
|---|---|---|
| Carousel PDF | 6.60% (le meilleur) | Frameworks, guides, études de cas (6-9 slides) |
| Texte + image | Bon | Stories, analyses, leçons |
| Infographie | 3x reach, 6x saves | Data baromètre, stats défaillances |
| Vidéo courte | Variable | Face camera, 60s max, sous-titres |
| Poll | +200% reach | Questions sectorielles (parcimonie) |

**Règle critique** : JAMAIS de lien externe dans le post (-30 à -60% reach). Lien en commentaire uniquement.

**L'algorithme pèse les commentaires 15x plus que les likes** dans les 90 premières minutes.

### Cibles outreach

| Segment | Pourquoi | Volume cible |
|---|---|---|
| Mandataires judiciaires | Sources de mandats | 50-100 |
| Administrateurs judiciaires | Sources de mandats | 30-50 |
| Avocats d'affaires | Referrals | 100+ |
| Experts-comptables | Détection précoce | 100+ |
| Dirigeants PME (5-50M CA) | Deals directs | 200+ |
| Fonds PE / retournement | Buy-side | 50+ |
| Banquiers régionaux | Co-mandats | 50+ |
| CCI, BPI, médiateurs | Écosystème institutionnel | 30+ |

### Métriques objectifs

| Métrique | M1 | M3 | M6 |
|---|---|---|---|
| Posts/semaine | 4 | 4-5 | 5 |
| Impressions/post | 500 | 2 000 | 5 000+ |
| DMs inbound/mois | 5 | 15 | 30+ |
| Leads qualifiés/mois | 1-2 | 5 | 10+ |

---

## 20. Business model & roadmap financière

### Phase 1 — Intermédiaire (maintenant → Q4 2026)

```
Détection → Analyse → Teaser → Matching → Mise en relation → Fee
```

- **Success fee** : 4-6% du prix de cession (minimum 10K EUR)
- **Retainer** : 0 EUR (full success, zéro upfront)
- **Cible deals** : PME 1-20M EUR CA en RJ/LJ
- Pas de fee sur les deals qui n'aboutissent pas

### Phase 2 — Abonnement data (2027)

| Segment | Offre | Prix |
|---|---|---|
| Mandataires judiciaires | Accès matching acheteurs + scoring de leurs dossiers | 500-2000 EUR/mois |
| Repreneurs sériels | Alertes personnalisées + analyse auto | 200-800 EUR/mois |
| Fonds d'investissement | API accès + swarm predictions | 2000-5000 EUR/mois |

### Phase 3 — Plateforme transactionnelle (2028+)

- Marketplace privée : data room sécurisée, gestion d'offres, timeline deal
- Commission additionnelle 1-2% sur transaction
- Valorisation certifiée (rapport PDF) : produit standalone
- Due diligence IA : analyse 50+ documents, red flags automatisés
- Signature électronique intégrée

### Métriques financières par phase

| Phase | Période | Pipeline actif | Deals closés | Revenue |
|---|---|---|---|---|
| **0 — First Close** | Mar-Avr 2026 | 5 | 1 | 10-50K EUR |
| **1 — Pipeline Machine** | Mai-Juil 2026 | 15 | 3 | 100-300K EUR |
| **2 — Scale & Moat** | Août-Déc 2026 | 30+ | 8 | 500K-1M EUR |
| **3 — Plateforme** | 2027 | 50+ | 20+ | 2-5M EUR |
| **4 — Dominance** | 2028+ | 100+ | 50+ | 10M+ EUR |

### Ce qu'on ne fait PAS (mars 2026)

- Weather Alpha (projet hobby, hors scope)
- Nouveaux projets avant que Brantham génère du revenu
- Over-engineering mémoire/infrastructure
- CRM externe (le dashboard est le CRM)
- SaaS/API avant le premier revenu (l'intermédiaire d'abord)

---

## 21. Roadmap technique par phase

### PHASE 0 — FIRST CLOSE (mars-avril 2026)

| Priorité | Tâche | Impact |
|---|---|---|
| P0 | Closer MLD (lancer Hunter, 10 acheteurs, prise de contact) | Revenue |
| P0 | 5 deals supplémentaires dans le pipeline (score ≥ 65) | Pipeline |
| P0 | Automatiser flow complet Scout→Director→Analyst→Writer→Hunter→Enricher | Speed |
| P1 | Email automation (templates + envoi auto AJ et acheteurs) | Scale |
| P1 | Tracking réponses (CRM minimal dans dashboard) | Conversion |

### PHASE 1 — PIPELINE MACHINE (mai-juillet 2026)

| Priorité | Tâche | Impact |
|---|---|---|
| P0 | BODACC historique 2015-2023 (étendre de 3 à 11 ans) | Backtest + comparables |
| P0 | Scoring v2 (intégrer bilans INPI dans les 9 composantes) | Précision |
| P0 | Swarm predictions en production (top 50 deals/semaine) | Edge prédictif |
| P1 | Dataroom IA (upload PDF/Excel, extraction KPIs) | Vitesse analyse |
| P1 | Teaser auto-generation PPTX zero intervention | Scale |
| P1 | AJ relationship tracker | Conversion |
| P2 | Multi-source veille (Infogreffe, presse locale, alertes sectorielles) | Couverture |
| P2 | Matching v2 (enrichissement live Pappers, Société.com, LinkedIn) | Qualité acheteurs |

### PHASE 2 — SCALE & MOAT (août-décembre 2026)

| Priorité | Tâche | Impact |
|---|---|---|
| P0 | Ensemble prédictif complet (MC + Cox + Bayesian + AgentMath + Swarm) | Précision |
| P0 | Dashboard mandataire (vue dédiée AJ/MJ) | Distribution |
| P0 | API publique v1 (scoring + matching + prédictions) | Revenue SaaS |
| P1 | Knowledge graph M&A (entités + relations + historique temporel) | Intelligence |
| P1 | Swarm v2 (agents spécialisés secteur, calibration dynamique) | Précision swarm |
| P1 | SEO machine 100 pages (6 clusters, 90+ articles, DA > 30) | Inbound leads |
| P2 | Alertes intelligentes (push notifications match profil repreneur) | Engagement |
| P2 | Mobile PWA | Productivité |

### PHASE 3 — PLATEFORME (2027)

| Tâche | Impact |
|---|---|
| Marketplace privée (data room sécurisée, gestion offres structurées) | Plateforme transactionnelle |
| Due diligence IA (50+ documents, red flags, rapport structuré) | Service premium |
| Valorisation certifiée (backtest 10K+ cessions historiques) | Produit standalone |
| Signature électronique | Close-the-loop |
| Multi-pays (Belgique, Espagne, Italie) | Expansion géo |
| Scoring-as-a-Service (API pour banques, assureurs crédit) | B2B SaaS |

### PHASE 4 — DOMINANCE (2028+)

| Tâche | Impact |
|---|---|
| Marketplace publique (acheteurs s'inscrivent, définissent critères) | Network effects |
| Financement intégré (DIP financing, bridge loans via partenaires) | Revenue stream |
| Prédictions macro (indice propriétaire cité par la presse) | Brand + autorité |
| White-label (licensing moteur scoring/matching à des cabinets) | Revenue récurrent |
| Acquisition de cabinets M&A distressed | Consolidation |
| Agent autonome full-loop (BODACC → signature, zéro humain sauf validation légale) | Endgame |

---

## 22. Risques et mitigations

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| **Premier deal ne close pas** | Moyen | Moral + trésorerie | Pipeline diversifié (5+ deals), ne pas tout miser sur MLD |
| **Mandataires ne répondent pas** | Élevé | Pas de deal flow | LinkedIn personal brand, crédibilité via contenu, referrals post-1er deal |
| **Réglementation** (courtage M&A réglementé ?) | Faible | Blocage légal | Structurer comme conseil en cession (pas courtage), consulter avocat |
| **Concurrent tech émerge** | Faible | Érosion avantage | Avance data (184K procs + 11 ans historique), execution rapide |
| **Dépendance LLM externe** (Anthropic, OpenAI) | Moyen | Coût + disponibilité | Swarm local (llama-cpp), migration open-source possible |
| **Qualité scoring insuffisante** | Faible | Mauvais deals proposés | Backtest continu, Cox C-index 0.84 déjà solide, feedback loop |
| **Burnout solo founder** | Élevé | Tout s'arrête | Automatisation max, premier hire = ops/biz dev (pas dev), repos |
| **Ollama Metal M5 crash** | Actif | Swarm bloqué | llama-cpp-python (workaround actif), attendre fix Ollama |
| **Indexation Google** | Résolu | Visibilité zéro | Bug robots.txt corrigé |

---

## 23. Le flywheel

La mécanique de croissance de Brantham est un flywheel auto-renforçant :

```
Plus de deals dans le pipeline
        ↓
Plus de data (outcomes, prix, délais, repreneurs actifs)
        ↓
Meilleur scoring + prédictions Cox
        ↓
Meilleur matching acheteurs (841K scores → 1M+)
        ↓
Plus de cessions réussies
        ↓
Plus de fees + réputation + articles de presse
        ↓
Plus de mandataires qui envoient leurs dossiers
        ↓
Plus de repreneurs qui s'inscrivent en base
        ↓
Plus de deals dans le pipeline ←─── LOOP
```

**Point clé** : chaque deal closé renforce le système doublement :
1. Il améliore les modèles (nouvelle ligne dans `backtest_scoring`)
2. Il attire de nouveaux deals (mandataires voient le résultat → font confiance)

Les concurrents sans la data ne peuvent pas entrer dans ce flywheel.

---

## 24. Brand voice & identité

### Voix de marque (site web et communications)

- **Expert Practitioner** : connaissance profonde du terrain, pas académique
- **Direct** : aucun remplissage, autoritaire, va à l'essentiel
- **Data-First** : chiffres et preuves systématiques
- **Accessible Authority** : concepts complexes expliqués simplement
- **Français en priorité**, anglais pour termes techniques (LBO, IRR, DD...)
- Pas d'emojis, design sobre, pas de violet

### Design

- Couleurs : sobres, professionnelles, financières
- Typographie : sans-serif, clean
- Pas d'images stock génériques
- Données visuelles : tableaux, graphiques propres

### Voix de l'AI (agents, dashboard)

> Tu as des opinions. Fortes. Stop le "ça dépend" systématique — prends position.
>
> Ne commence jamais par "Bonne question" ou "Je serais ravi de vous aider".
>
> La brièveté est obligatoire. Si la réponse tient en une phrase, une phrase.
>
> Tu peux recadrer. Si on est sur le point de faire quelque chose de con, dis-le. Charme plutôt que cruauté, mais sans édulcorer.
>
> Les interlocuteurs sont des pros. Traite-les comme tels.

---

## 25. North Star & métriques clés

### North Star

> **"Chaque PME viable en France qui entre en procédure collective a un repreneur identifié et contacté en 48h."**

### Métriques de suivi

| Métrique | Actuel | Cible Q2 2026 | Cible Q4 2026 |
|---|---|---|---|
| Deals en pipeline | 1 (MLD) | 5+ | 15+ |
| Deals closés | 0 | 1+ | 5+ |
| Revenue | 0 EUR | Premier fee | 300K+ EUR |
| Pages website | 19 | 40+ | 100+ |
| Couverture BODACC | 2023-2026 | 2015-2026 | 2010-2026 |
| Score swarm predictions | MVP (3 agents) | Production (25 agents) | v2 calibré |
| Score SEO | 93/100 | Indexé Google | DA > 20 |
| Followers LinkedIn | 0 | +800 | +2000 |
| Leads qualifiés/mois | 0 | 5 | 10+ |

### Ce qui serait un échec

- Pas de premier deal avant Q3 2026 → pivot nécessaire
- Mandataires systématiquement non-répondants → revoir l'approche outreach
- Swarm Brier score > 0.25 (pire qu'un coin flip) après calibration → revoir architecture
- Burnout → automatiser davantage avant d'aller plus vite

### Ce qui serait un succès exceptionnel

- 3 deals closés avant fin 2026 → 200K+ EUR fees
- Mandataire qui envoie spontanément ses dossiers → distribution effect
- Article presse mentionnant Brantham comme référence distressed → brand
- Swarm predictions citées par un fonds d'investissement → B2B SaaS inbound

---

## Stack technique finale (cible 2027)

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
│  │  (full autonomous pipeline)                         │ │
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

*Document généré le 27 mars 2026 depuis le brantham-vault (173 notes).*
*Sections couvertes : identité, marché, procédures légales, offre, moat, pipeline, agents, scoring, matching, deals, architecture, data pipeline, BDD, dashboard, MiroFish, swarm, concurrence, SEO, LinkedIn, business model, roadmap, risques, flywheel, brand voice, métriques.*
