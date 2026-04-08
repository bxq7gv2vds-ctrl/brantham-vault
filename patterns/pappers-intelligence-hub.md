---
name: Pappers Intelligence Hub
type: pattern
date: 2026-04-08
project: brantham
reusable: true
---

# Pappers Intelligence Hub

**Date Discovered**: 2026-04-08
**Maturity**: Experimental
**Reuse Count**: 0

## Description

Infrastructure vault complete pour cartographier les entreprises francaises via l'API Pappers (MCP gratuit 100 tokens/mois). Chaque entite (entreprise, dirigeant, beneficiaire, secteur, procedure, groupe) a son propre fichier vault avec wikilinks bidirectionnels, formant un knowledge graph navigable dans Obsidian.

## Problem It Solves

- Pas de base centralisee d'entreprises cibles et repreneurs
- Buyer mapping ad hoc et non persistant
- Data corporate dispersee (BODACC scrape, Google, LinkedIn)
- Aucune vision reseau (qui detient quoi, dirigeants communs)

## Implementation

### Architecture

```
vault/brantham/pappers/
  _MOC.md                           # Index central
  entreprises/{siren}-{slug}.md     # 1 par SIREN
  secteurs/{naf}-{slug}.md          # 1 par code NAF
  dirigeants/{slug}.md              # 1 par personne
  beneficiaires/{slug}.md           # 1 par beneficiaire effectif
  procedures-collectives/{slug}.md  # 1 par procedure
  financials/{siren}-{year}.md      # 1 par (SIREN, annee)
  cartographie/{slug}.md            # 1 par groupe
  recherches/{date}-{slug}.md       # Snapshots recherche
  scripts/                          # 6 scripts Python
```

### Graph Wikilinks

```
Entreprise <-> Dirigeants (mandats actifs/historiques)
Entreprise <-> Beneficiaires (% detention)
Entreprise <-> Secteur (code NAF)
Entreprise <-> Financials (comptes annuels)
Entreprise <-> Procedures (BODACC)
Entreprise <-> Cartographie (organigramme groupe)
Dirigeant <-> Dirigeant (mandats communs = reseau)
Procedure -> Deal Pipeline (scoring >= 60)
Secteur <-> Knowledge Playbook (expertise sectorielle)
```

### Workflow Type

1. **Monitoring BODACC** -> nouvelles procedures -> scoring automatique -> qualification deal
2. **Enrichissement deal** -> fiche entreprise + dirigeants + comptes + cartographie
3. **Mapping repreneur** -> recherche sectorielle -> top companies -> cartographie groupes
4. **Due diligence** -> financials multi-annees + beneficiaires + conformite PPE

### Strategie Tokens

100 gratuits/mois. Budget type:
- 30 tokens monitoring BODACC (3 recherches/semaine)
- 20 tokens enrichissement deals qualifies
- 20 tokens mapping repreneurs cibles
- 20 tokens analyses sectorielles
- 10 tokens reserve

## Trade-offs

- Avantages: data structuree persistante, knowledge graph compounding, gratuit
- Limites: 100 tokens/mois, data J-1, pas de temps reel, email pro requis

## Lessons Learned

- Le MCP Pappers supporte uniquement streamable-http (pas stdio)
- Toujours creer les fiches dirigeants/beneficiaires en meme temps que l'entreprise (atomicite)
- Le scoring deal sur les procedures BODACC permet de trier rapidement

## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[brantham/pappers/_MOC]]
- [[brantham/patterns/acheteur-mapping]]
