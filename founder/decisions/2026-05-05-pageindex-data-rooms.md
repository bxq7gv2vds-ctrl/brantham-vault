---
title: Adoption PageIndex pour data rooms M&A Brantham
date: 2026-05-05
status: adopted
type: decision
tags: [tooling, brantham, ma, data-room, rag]
---

# Adoption PageIndex pour data rooms M&A Brantham

## Décision

Adopter [PageIndex](https://github.com/VectifyAI/PageIndex) (Vectify AI) comme outil de RAG arborescent vectorless pour les data rooms M&A actives — uniquement sur PDFs lourds (> 100 pages) où Claude direct devient inefficace ou coûteux à parcourir plusieurs fois.

## Pourquoi

- Vector RAG classique est mauvais sur les docs financiers/juridiques longs : similarity ≠ relevance
- PageIndex score 98,7 % sur FinanceBench (rapports financiers SEC) — exactement le type de docs Brantham
- Retrieval reasoning-based avec citations page-level → traçable pour due dil
- Naturellement adapté à la structure hiérarchique des comptes annuels, jugements RJ-LJ, pactes d'associés

## Périmètre

**Cible** :
- Data rooms deals actifs (Magic Form, ITFI, futurs deals)
- Comptes annuels Pappers PDF, liasses fiscales
- Jugements DLDO, ordonnances tribunal de commerce
- Pactes d'associés (extraction clauses précises)

**Hors périmètre** :
- Vault interne markdown → [[brantham/_MOC]] couvert par QMD
- Données structurées Pappers → API JSON directe suffit
- PDFs courts (< 50 pages) → Claude lit en direct, plus rapide

## Architecture

- Code : `~/tools/pageindex/` (hors vault, code ≠ knowledge)
- Wrapper CLI : `brantham-pageindex <deal-slug> <pdf-path>` (dans `~/.local/bin/`)
- Output trees : `vault/brantham/deals/active/<deal-slug>/_dataroom/<pdf>.tree.json`
- Auto-link : wikilink ajouté dans `_MOC.md` du deal sous "Data room (PageIndex)"
- LLM : Claude Sonnet 4.5 via le CLI `claude` (auth Claude Code OAuth — **pas de clé API à gérer**)
- Backend custom : `pageindex/claude_cli_backend.py` remplace les appels LiteLLM par `subprocess` vers `claude -p`
- Skill Claude Code : `/pageindex` pour invocation naturelle

## Coûts

- Tokens LLM par tree generation : ~30-100k tokens selon taille PDF
- Tokens par Q&A : tree search consomme moins qu'une lecture full doc
- Setup : zéro (déjà installé)
- Recurring : clé API Anthropic (à renseigner dans `~/tools/pageindex/.env`)

## Action requise

Renseigner `ANTHROPIC_API_KEY` dans `~/tools/pageindex/.env` avant premier usage.

## Validation

À tester sur la data room ITFI dès réception de la version étendue. Si l'écart de précision vs lecture Claude directe justifie le setup → industrialiser sur tous les nouveaux deals. Sinon → restreindre aux pactes et liasses fiscales uniquement.

## Related

- [[_system/MOC-decisions]]
- [[brantham/_MOC]]
- [[brantham/patterns/data-room-pageindex]]
- [[brantham/deals/active/itfi-groupe/_MOC]]
- [[brantham/deals/active/magic-form-levallois/_MOC]]
