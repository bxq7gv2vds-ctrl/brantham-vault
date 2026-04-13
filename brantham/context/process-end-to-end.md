---
type: context
project: brantham
date: 2026-03-27
updated: 2026-03-27
tags: [process, workflow, operations, end-to-end]
---

# Brantham Partners — Process End-to-End

> Le workflow complet, de la detection d'une opportunite au cash encaisse. Chaque etape decrit QUI fait QUOI, avec QUELS outils, et QUEL output.

---

## Vue d'ensemble

```
DETECTION → QUALIFICATION → TEASER → SOURCING REPRENEUR → OUTREACH → ENGAGEMENT → DATA ROOM → OFFRE → CLOSING → POST-RACHAT
```

**Duree cible** : 2-6 semaines (de detection a depot d'offre)
**Facteur limitant** : deadline du tribunal (souvent 3-4 semaines)

---

## Phase 1 : DETECTION

### Objectif
Identifier les entreprises en procedure collective qui sont a vendre.

### Sources
| Source | Frequence | Volume | Outil |
|---|---|---|---|
| 30 sites AJ (administrateurs judiciaires) | Daily | ~468 opportunites/scan | Scraping Python + [[brantham/data-pipeline/_MOC|Prefect pipeline]] |
| BODACC | Daily 07h00 UTC | ~190 publications/jour | Scraping auto |
| Outils de synchro (pour AJ non scrapes) | Ad hoc | Variable | A structurer |

### Output
- Liste d'opportunites brutes avec : nom entreprise, secteur, CA estime, AJ source, deadline, type de procedure

### Qui
- **Machine** : 100% automatise (scraping + pipeline Prefect)
- **Humain** : 0% (sauf maintenance technique)

### Status actuel
✅ Operationnel — detecte des centaines d'opportunites par semaine

---

## Phase 2 : QUALIFICATION

### Objectif
Evaluer si l'opportunite vaut la peine d'etre traitee.

### Donnees disponibles (SANS data room)
| Source | Donnees |
|---|---|
| BODACC | Type de procedure, dates, tribunal, mandataires |
| Annonce AJ | Description activite, perimetre de cession, deadline |
| Pappers / Infogreffe | CA, effectif, bilans publics, dirigeants, liens capitalistiques |
| Societe.com | Donnees complementaires |

### Criteres de qualification
1. **Taille** : CA > 1M EUR (PME sweet spot : 1-50M)
2. **Secteur** : attractif pour repreneurs (BTP, industrie, commerce specialise)
3. **Deadline** : suffisamment loin pour agir (>2 semaines ideal)
4. **Viabilite apparente** : l'activite peut etre reprise (pas juste des actifs morts)
5. **Information** : assez de donnees publiques pour creer un teaser credible

### Scoring 9D (quand automatise)
| Dimension | Description |
|---|---|
| Viabilite | L'entreprise peut-elle etre sauvee ? |
| Taille/Ticket | CA, EBITDA, actifs |
| Attractivite sectorielle | Tailwinds du secteur |
| Urgence | Jours avant deadline |
| Qualite info | Completude des donnees publiques |
| Impact emploi | Nombre de salaries a risque |
| Isolement geographique | Moins de competition locale |
| Cooperation creanciers | Probabilite de process fluide |
| Accessibilite acheteur | Facilite a trouver un repreneur |

**Seuils** : 60+ = GO | 40-60 = WATCH | <40 = PASS

### Output
- Fiche opportunite qualifiee avec score et go/no-go

### Qui
- **Machine** : scoring auto (quand PostgreSQL + agents actifs)
- **Humain** : decision finale go/no-go (Paul ou Soren)

### Status actuel
⚠️ Partiellement operationnel — scoring auto construit mais pas en production continue. Qualification souvent manuelle.

---

## Phase 3 : TEASER

### Objectif
Creer un document de presentation ANONYME de l'opportunite pour attirer les repreneurs.

### Contenu du teaser
- Secteur d'activite (sans nommer l'entreprise)
- Localisation geographique (region, pas adresse exacte)
- CA et tendance
- Effectif
- Perimetre de cession (actifs, contrats, salaries inclus)
- Points forts de l'opportunite
- Deadline pour deposer une offre
- Contact Brantham Partners

### Contraintes
- **100% base sur infos publiques** (pas de data room)
- **Anonymise** : le nom de l'entreprise n'apparait pas
- Format : PDF one-pager ou 2-3 pages max

### Output
- PDF teaser pret a envoyer aux repreneurs

### Qui
- **Machine** : [[brantham/agents/_MOC|Agent Writer]] genere le teaser
- **Humain** : relecture et validation (Paul)

### Status actuel
⚠️ 1 seul teaser genere (MLD). Agent Writer construit mais pas en production batch. **Bottleneck majeur : 28+ deals analyses sans teaser.**

---

## Phase 4 : SOURCING REPRENEUR

### Objectif
Identifier 10-20 repreneurs potentiels pour chaque opportunite.

### Criteres repreneur
1. **Connaissance du secteur** : experience dans le meme business ou adjacent
2. **Capacite financiere** : budget d'acquisition suffisant pour le ticket
3. **Motivation strategique** : expansion, consolidation, diversification
4. **Capacite operationnelle** : equipe pour reprendre et restructurer

### Sources de recherche
| Source | Usage | Status |
|---|---|---|
| Pappers | Recherche entreprises par secteur/taille/geographie | ✅ Utilise |
| LinkedIn | Identification dirigeants et decision-makers | ✅ Utilise |
| Base interne | Profils repreneurs enrichis | 🔧 En construction |
| Reseau personnel | Contacts directs | Tres peu |

### Matching 4D
| Dimension | Facteurs |
|---|---|
| Secteur | Experience industrie, marches adjacents, cross-sell |
| Taille | Budget acquisition, historique de deals |
| Geographie | Presence regionale, ambitions d'expansion |
| Strategie | Synergies, these de consolidation, culture |

### Output
- Liste de 10-20 repreneurs qualifies avec : nom, entreprise, poste, raison du match, contact

### Qui
- **Machine** : [[brantham/agents/_MOC|Agent Hunter]] + Enricher pour le mapping
- **Humain** : validation de la pertinence (Paul ou Soren)

### Status actuel
⚠️ Agent construit, 143 profils scraped en base, mais **0 vrai sourcing fait sur un deal reel**.

---

## Phase 5 : OUTREACH

### Objectif
Contacter les repreneurs identifies et susciter l'interet.

### Supports necessaires
| Support | Status | Priorite |
|---|---|---|
| **Plaquette Brantham** (PDF 5-6 slides) | ❌ A creer | P0 |
| **Template email premiere approche** | ❌ A creer | P0 |
| **Script LinkedIn InMail** | ❌ A creer | P0 |
| **Template email teaser** | ❌ A creer | P0 |
| **Script telephonique** | ❌ A creer | P1 |

### Sequence d'outreach (a definir)
1. **J0** : Email d'introduction avec plaquette Brantham
2. **J0** : Teaser anonyme en piece jointe ou lien
3. **J+2** : Relance LinkedIn si pas de reponse
4. **J+5** : Appel telephonique
5. **J+7** : Derniere relance email

### Output
- Repreneur interesse → passer en Phase 6

### Qui
- **Humain** : Soren (role ideal) — appels, emails, LinkedIn
- **Machine** : CRM/tracking, templates pre-remplis, enrichissement contacts

### Status actuel
❌ **Bloque**. Pas de plaquette, pas de templates. 0 repreneur contacte a ce jour.

---

## Phase 6 : ENGAGEMENT

### Objectif
Formaliser la relation avec le repreneur interesse.

### Actions
1. **Call decouverte** : comprendre les criteres du repreneur, sa capacite, sa motivation
2. **Presentation detaillee** de l'opportunite (avec plus de details que le teaser)
3. **Signature lettre de mission** : mandat d'accompagnement
4. **Fee agreement** : 15-30k upfront premiere offre + 15-30k offre finale + variable

### Documents necessaires
| Document | Status |
|---|---|
| Lettre de mission type | ❌ A formaliser (modeles existants mais rien de concret) |
| CGV | ❌ A formaliser |
| NDA | ❌ A formaliser |

### Output
- Mandat signe + premier versement (si applicable)

### Qui
- **Humain** : Paul + Soren (negociation, signature)
- **Machine** : generation documents pre-remplis

### Status actuel
❌ Jamais fait. Contrats a formaliser.

---

## Phase 7 : DATA ROOM

### Objectif
Obtenir la data room aupres de l'AJ au nom du repreneur mandate.

### Process
1. Contacter l'AJ en presentant le repreneur (avec mandat)
2. Signer les NDA necessaires
3. Acceder a la data room (souvent via lien securise ou envoi physique)
4. Analyser les documents : bilans detailles, contrats, baux, contentieux, etc.

### Contrainte cle
⚠️ **Les AJ exigent un mandat d'entreprise (repreneur) pour donner acces.** Pas de client = pas de data room. C'est le probleme poule et oeuf central.

### Output
- Data room obtenue → analyse approfondie possible
- Due diligence rapide (48-72h) sur les elements cles

### Qui
- **Humain** : contact AJ (Paul ou Soren), analyse documents
- **Machine** : [[brantham/agents/_MOC|Agent Analyst]] pour analyse structuree

### Status actuel
❌ Aucune data room obtenue (refus AJ car pas de client).

---

## Phase 8 : STRUCTURATION D'OFFRE

### Objectif
Aider le repreneur a rediger et deposer son offre de reprise.

### Offre premiere (depot)
- Les 9 mentions obligatoires L642-2 du Code de Commerce
- Prix propose + plan de financement
- Engagements emploi (critere #1 du tribunal)
- Plan de continuation de l'activite
- Garanties d'execution

→ **Declenchement fee : 15-30k EUR upfront**

### Offre finale (audience)
- Offre revisee post-data room
- Negociations avec AJ/MJ
- Preparation audience tribunal
- Argumentaire oral

→ **Declenchement fee : 15-30k EUR second ticket**

### Voir aussi
- [[brantham/knowledge/process/structuration-offres-reprise]]
- [[brantham/knowledge/process/audience-tribunal]]
- [[brantham/knowledge/process/encheres-surencheres]]

### Output
- Offre deposee au tribunal

### Qui
- **Humain** : structuration avec le repreneur (Paul + Soren)
- **Machine** : templates d'offre, modeles financiers, scoring

### Status actuel
❌ Jamais fait sur un vrai deal.

---

## Phase 9 : CLOSING

### Objectif
Le tribunal accepte l'offre du repreneur.

### Process
- Audience de cession au tribunal
- Le tribunal choisit parmi les offres (criteres L642-5 : emploi, prix, viabilite)
- Jugement de cession
- Purge des suretes

### Fee variable
- % du prix de cession OU forfait additionnel (negocie au cas par cas avec le repreneur)

### Voir aussi
- [[brantham/knowledge/process/post-closing-execution]]
- [[brantham/knowledge/legal/plans-de-cession]]

### Output
- Deal close, fees collectees

### Qui
- **Humain** : accompagnement audience, negociation
- **Machine** : preparation documents, scoring, monitoring

### Status actuel
❌ Jamais fait.

---

## Phase 10 : POST-RACHAT

### Objectif
Accompagner le repreneur dans la restructuration post-acquisition.

### Services proposes
1. **Conseil strategique** : repositionnement, business plan
2. **Conseil operationnel** : integration, reorganisation, quick wins
3. **Conseil financier** : restructuration dette, relations bancaires, tresorerie

### Duree
- 3-12 mois selon complexite

### Fee
- A definir (forfait mensuel ou mission ponctuelle)

### Voir aussi
- [[brantham/knowledge/process/integration-post-acquisition]]
- [[brantham/knowledge/process/turnaround-operationnel]]

### Output
- Entreprise stabilisee, repreneur autonome

### Qui
- **Humain** : Paul + Soren (conseil direct)
- **Machine** : dashboards de suivi, KPIs, alertes

### Status actuel
❌ Jamais fait. Competences en interne, a structurer comme offre.

---

## Related

- [[brantham/context/realite-business]]
- [[brantham/context/sow]]
- [[brantham/_MOC]]
- [[brantham/knowledge/process/due-diligence-distressed]]
- [[brantham/knowledge/process/structuration-offres-reprise]]
- [[brantham/knowledge/process/audience-tribunal]]
- [[brantham/knowledge/process/post-closing-execution]]
- [[brantham/knowledge/process/integration-post-acquisition]]
- [[brantham/COWORK-PROMPT]]
- [[brantham/context/roles-et-responsabilites]]
