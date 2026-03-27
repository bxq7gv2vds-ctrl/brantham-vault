---
type: pattern
project: brantham
date: 2026-03-12
category: buyer-mapping
tags: [hunter, acheteurs, m-and-a]
---

# Acheteur Mapping Patterns

Patterns pour l'identification et le scoring des repreneurs potentiels. Utilises par l'agent Hunter.

## Types de Repreneurs

### Strategic Buyers (acheteurs strategiques)
- Meme secteur ou secteur adjacent
- Recherchent des synergies: clients, production, geographie, technologie
- Souvent prets a payer plus cher (valeur strategique)
- Cibles: concurrents directs, fournisseurs, clients, acteurs complementaires

### Financial Buyers (acheteurs financiers)
- Private equity (PE), family offices, fonds de retournement
- Recherchent un rendement financier
- Build-up strategy (consolidation sectorielle)
- Cibles: fonds specialises distressed, fonds sectoriels, holding familiales

## Taille Ideale du Repreneur

Regle: le repreneur ideal a **5 a 20x la taille du deal** (en CA ou en actifs sous gestion).

| Taille cible (CA) | Taille repreneur ideale |
|---|---|
| < 500K EUR | 2.5M - 10M EUR |
| 500K - 2M EUR | 5M - 40M EUR |
| 2M - 10M EUR | 10M - 200M EUR |
| 10M - 50M EUR | 50M - 1B EUR |

Un repreneur trop petit n'a pas les moyens. Un trop gros ne s'interessera pas.

## Scoring A/B/C

| Grade | Criteres | Cible |
|---|---|---|
| **A** | Meme secteur, bonne taille, historique d'acquisitions, geographie compatible | 3-5 par deal |
| **B** | Secteur adjacent, taille ok, interet potentiel | 5-10 par deal |
| **C** | Financier pur ou secteur eloigne mais profile possible | 5-10 par deal |

### Criteres de Scoring Detailles

| Critere | Poids | A | B | C |
|---|---|---|---|---|
| Fit sectoriel | 30% | Meme NAF ou adjacent direct | Secteur lie | Generalist |
| Fit taille | 25% | 5-20x | 3-30x | Hors range |
| Historique M&A | 20% | Acquisitions recentes | Quelques acquisitions | Aucune |
| Fit geographique | 15% | Meme region ou national | National/Europe | International uniquement |
| Capacite financiere | 10% | Confirmee | Probable | Inconnue |

## Volume par Deal

- **Objectif**: 10-20 repreneurs identifies par deal
- **Minimum**: 3 A + 5 B pour considerer le mapping comme suffisant
- **Si < 8 total**: elargir le perimetre sectoriel ou geographique

## Workflow

```
1. Identifier le secteur et la taille de la cible
2. Chercher les strategic buyers (concurrents, adjacent, build-up)
3. Chercher les financial buyers (PE distressed, family offices sectoriels)
4. Scorer chaque repreneur (A/B/C)
5. Valider la shortlist avec Director (QC 7/10)
6. Passer a Enricher pour validation contacts
7. Apres enrichissement → approche avec teaser (voir [[brantham/patterns/teaser-patterns]])
```

## Sources de Recherche

- Base `buyer_match_score` (841K+ scores precalcules)
- BODACC historique (repreneurs passes)
- Pappers / Societe.com (structure capitalistique, dirigeants)
- Secteur NAF adjacent (`/api/naf/adjacent`)
- LinkedIn (decision-makers)
- PitchBook / Dealroom (pour PE/VC)

## Anti-patterns

- Ne pas mapper uniquement des financiers (les strategiques payent mieux et closent plus vite)
- Ne pas ignorer les repreneurs individuels (managers, cadres en reconversion) pour les petits deals < 1M EUR
- Ne pas envoyer le teaser a un concurrent direct du mandataire (conflit d'interets)
- Verifier les liens capitalistiques pour eviter les repreneurs lies au cedant

## Related
- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[patterns/agent-orchestration]]
- [[patterns/gemweb-rss-parsing]]
- [[patterns/teaser-pptx-generation]]
- [[patterns/prefect-pipeline]]
- [[patterns/scraping-robust]]
- [[brantham/patterns/scoring-patterns]]
- [[brantham/patterns/teaser-patterns]]
- [[founder/journal/2026-03-12]]
- [[founder/decisions/2026-03-12-unified-vault]]
- [[website/bugs/2026-03-21-contenu-duplique-geo-secteur]]
- [[brantham/bugs/2026-03-02-matrice-aj-secteur-taux-cession]]
- [[brantham/bugs/2026-03-02-analyse-regionale-unique-constraint]]
- [[brantham/bugs/2026-03-06-agent-auth-401]]
