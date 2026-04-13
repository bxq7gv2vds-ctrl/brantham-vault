---
type: context
project: brantham
date: 2026-03-27
updated: 2026-03-27
tags: [contexte, business-model, realite, verite-terrain]
---

# Brantham Partners — La Realite du Business

> Ce document est la source de verite. Pas d'embellissement. C'est ce qui est VRAI au 27 mars 2026.

---

## Identite

- **Nom** : Brantham Partners
- **Forme juridique** : SAS
- **Fondateurs** : Paul Roulleau + Soren (associe)
- **Effectif** : 2 personnes
- **Revenue** : 0 EUR (pre-revenue)
- **Runway** : Pas de pression — revenus externes au business
- **Investisseurs** : Aucun. Bootstrapped. Pas de levee prevue.
- **Couts infra** : ~300$/mois (API Claude + serveurs + outils)
- **Enregistrements** : SAS uniquement. Pas encore enregistre comme intermediaire (ORIAS, CMA, etc.) — a faire pour la credibilite.

---

## Ce qu'on fait (en vrai)

**Brantham Partners est un intermediaire M&A specialise dans les entreprises en difficulte en France.**

On accompagne des **repreneurs** (notre client) dans l'acquisition d'entreprises en procedure collective (redressement judiciaire, liquidation judiciaire).

### Le flow reel

```
1. DETECTION : On scrape les sites de 30 administrateurs judiciaires (AJ) + BODACC
   → On detecte les entreprises en procedure qui sont a vendre (plans de cession, cession d'actifs)

2. QUALIFICATION : On evalue l'opportunite sur base d'infos publiques
   → BODACC, annonce AJ, bilans Pappers/Infogreffe
   → PAS de data room a ce stade (les AJ refusent sans mandat repreneur)

3. TEASER : On cree un document de presentation anonyme de l'opportunite
   → Base 100% sur infos publiques (pas de data room)
   → Sert a attirer l'attention d'un repreneur potentiel

4. SOURCING REPRENEUR : On cherche des repreneurs potentiels
   → Sources : Pappers, LinkedIn, base interne (en construction)
   → Criteres : connaissance du secteur + capacite financiere

5. OUTREACH : On contacte les repreneurs
   → ⚠️ PAS ENCORE FAIT — bloque par l'absence de plaquette de presentation
   → Templates email et scripts LinkedIn : A CREER

6. ENGAGEMENT : Le repreneur est interesse → on signe un mandat
   → Lettre de mission : A FORMALISER

7. DATA ROOM : On demande la data room a l'AJ au nom du repreneur
   → Les AJ exigent un mandat d'entreprise (repreneur) pour donner acces

8. ACCOMPAGNEMENT OFFRE : On aide le repreneur a structurer son offre
   → Premiere offre (depot) → 15-30k EUR upfront
   → Offre finale → 15-30k EUR second ticket
   → Variable : % sur cession OU forfait additionnel (negocie au cas par cas)

9. POST-RACHAT : Accompagnement restructuring
   → Conseil strategique, operationnel, financier
   → On a les competences en interne
   → Vision : devenir les experts #1 de l'ecosysteme
```

---

## Modele de revenus (REEL)

| Etape | Montant | Declencheur |
|---|---|---|
| Upfront #1 | 15-30k EUR | Depot premiere offre |
| Upfront #2 | 15-30k EUR | Offre finale |
| Variable | % du prix de cession OU forfait | Negocie au cas par cas |

**Revenue totale par deal** : 30-60k EUR fixe + variable selon taille du deal.

⚠️ Ce n'est PAS un modele "3-8% success fee uniquement" comme ecrit dans les anciens documents du vault. C'est un modele hybride avec du cash upfront.

---

## Ou on en est (la verite)

### Ce qui fonctionne
- Scraping 30 sites AJ : operationnel
- BODACC : operationnel
- Pipeline de detection : detecte des centaines d'opportunites
- Knowledge base : 49 sujets, complete
- Site SEO : lance, pas encore de leads
- Echanges AJ : on a parle a des AJ (demande data rooms)

### Ce qui ne fonctionne PAS encore
- **0 deal traite end-to-end** — les deals dans le workspace sont du test/scraping
- **0 repreneur contacte** — bloque par l'absence de plaquette
- **0 mandat signe** — pas de contrat type formalise
- **0 EUR de revenu**
- **Pas de plaquette de presentation** — PDF 5-6 slides premium/data-driven a creer
- **Pas de brand book / DA** — direction artistique a formaliser
- **Pas de templates outreach** — ni email ni LinkedIn
- **Pas de contrats types** — lettre de mission, CGV a formaliser
- **Pas d'enregistrements reglementaires** — a investiguer (ORIAS, etc.)
- **Les AJ refusent les data rooms** — sans mandat repreneur, pas d'acces
- **Repartition des roles floue** — Paul fait tout (tech + process + infra), Soren sous-utilise

### Les vrais blocages (par ordre de priorite)
1. **Over-engineering** : tendance a ameliorer les agents/la tech au lieu de vendre
2. **Pas de plaquette** : impossible de contacter des repreneurs sans support pro
3. **Pas de process de vente** : aucun playbook outreach, aucun template
4. **Pas de vision claire** : pas de document unique "voila ce qu'on doit faire maintenant"
5. **Roles non definis** : Paul porte tout, Soren pas assez implique

---

## Positionnement & Avantage concurrentiel

### Ce qu'on est
- Jeunes, vision differente du marche
- Data-driven + AI agents (personne d'autre ne fait ca dans le distressed FR)
- Vitesse de detection (scraping auto vs lecture manuelle)
- Ambition : banque d'affaires new gen, max automation

### Ce qu'on n'est PAS
- PAS un marketplace / SaaS / plateforme
- PAS un prediction market
- PAS mandate par les AJ (on est cote repreneur)
- PAS encore operationnel commercialement

### Concurrence
- Cabinets de restructuring classiques (avocats, Big 4 sur les gros deals)
- Intermediaires traditionnels (pas de tech, lents)
- **Personne ne fait du data-driven + AI dans ce segment en France**

---

## L'equipe

| Qui | Role actuel | Role ideal |
|---|---|---|
| **Paul** | Tout (tech, infra, process, strategie, product) | CTO / CPO — tech, agents, product, data |
| **Soren** | Sous-utilise | COO / Commercial — outreach, relations AJ, closing |

⚠️ Repartition a definir et formaliser.

---

## Les chiffres du marche

- **~70,000 procedures collectives/an** en France (record)
- **~21,000 redressements judiciaires/an** (le sweet spot)
- **~12,000 cessions realisees/an**
- **267,000 emplois menaces** en 2025
- **Segments dominants** : BTP (21%), Commerce (20%), Hotellerie (13%)
- **Cible Brantham** : PME 1-50M EUR CA en RJ/LJ avec plan de cession
- **PGE** : 38 Mds EUR en remboursement Q2-Q3 2026 → vague finale de defaillances

---

## Tech stack (pour reference)

| Composant | Tech | Status |
|---|---|---|
| Backend API | FastAPI Python | Operationnel |
| Base de donnees | PostgreSQL 16 (Docker) | Operationnel |
| Pipeline data | Prefect + scraping | Operationnel |
| Frontend dashboard | React 19 + Vite | ~60% |
| Agents LLM | 6 agents Claude (Scout/Director/Analyst/Writer/Hunter/Enricher) | Construits, pas en production autonome |
| Site SEO | Next.js 15 | Lance |
| MiroFish | Python + MLX + Vue | R&D long terme |

---

## Liens vault

- [[brantham/context/sow]] — Statement of Work & chantiers
- [[brantham/context/process-end-to-end]] — Process complet de A a Z
- [[brantham/context/roles-et-responsabilites]] — Qui fait quoi
- [[brantham/_MOC]] — Index technique du projet

## Related
- [[brantham/COWORK-PROMPT]]
