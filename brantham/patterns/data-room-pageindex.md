---
title: Pattern data-room PageIndex
date: 2026-05-05
type: pattern
tags: [pattern, brantham, data-room, rag, tooling]
---

# Pattern : indexation data-room avec PageIndex

## Contexte

Quand on reçoit une data room d'un AJ pour un deal actif, elle contient typiquement :
- Comptes annuels (3 à 5 ans) — 50-200 pages chacun
- Liasse fiscale détaillée — 100+ pages
- Pacte d'associés / statuts — 30-80 pages
- Jugement RJ-LJ + ordonnances — 20-50 pages
- Audits passés (commissaire aux comptes) — 50-150 pages
- Contrats clés (bail commercial, fournisseurs stratégiques) — variable

Volume cumulé : souvent **500-2000 pages**. Claude direct devient lent et coûteux pour Q&A répété.

## Solution

Indexer chaque PDF lourd via PageIndex → tree JSON hiérarchique → Q&A reasoning-based avec citations page-level.

## Workflow

### 1. Réception data room

Dump dans `~/Downloads/<deal-slug>-dataroom/` (hors vault, raw materials).

### 2. Indexation batch

```bash
cd ~/Downloads/<deal-slug>-dataroom
for pdf in *.pdf; do
  brantham-pageindex <deal-slug> "$pdf"
done
```

Chaque PDF génère un tree dans `vault/brantham/deals/active/<deal>/_dataroom/<pdf>.tree.json` et auto-ajoute le wikilink dans le `_MOC.md` du deal.

### 3. Q&A pendant la due dil

Dans Claude Code, sur le deal actif :

```
/pageindex
```

Puis poser des questions ciblées :
- "Quel est le BFR à fin 2024 et son évolution sur 3 ans ?"
- "Trouve les clauses de drag-along dans le pacte"
- "Liste les baux commerciaux et leurs échéances"
- "Quel est le passif fournisseur > 90 jours ?"

Claude charge le tree JSON, raisonne sur les titres + summaries, descend dans les nodes pertinents, et cite les pages PDF.

### 4. Capture des findings

Notes structurées dans `vault/brantham/deals/active/<deal>/notes/YYYY-MM-DD-<topic>.md` avec wikilink vers le tree source.

## Critères pour utiliser ce pattern

OUI :
- PDF > 100 pages
- Q&A répété sur le même corpus
- Besoin de citations page-level pour rapports clients

NON :
- PDF court → Claude direct
- Doc déjà markdown structuré → QMD vault
- Données structurées → API Pappers JSON

## Coûts observés

À documenter après premier usage réel sur ITFI ou Magic Form :
- Tokens par tree generation
- Tokens par session Q&A
- Temps wall-clock indexation

## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[founder/decisions/2026-05-05-pageindex-data-rooms]]
- [[brantham/context/process-end-to-end]]
- [[brantham/patterns/onboarding-distressed-ma]]
