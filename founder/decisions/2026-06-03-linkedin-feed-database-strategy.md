---
name: LinkedIn feed — stratégie capture + base de données
type: decision
date: 2026-06-03
status: approved
tags: [brantham, linkedin, data]
---

# LinkedIn feed — capture humaine + SQLite locale

**Date**: 2026-06-03  
**Status**: Approved  
**Decision Maker**: Paul + agent

## Context

Besoin : construire une grosse base de signaux du feed LinkedIn pour générer des commentaires intelligents, des idées de posts, et du contexte éditorial Brantham — sans risque de ban.

Contrainte légale/ToS : LinkedIn interdit le scraping automatisé du feed connecté, le pilotage de navigateur, et l'automatisation des actions (like, comment, scroll).

## Options Considered

1. **Scraper le feed (Puppeteer, cookies, API non officielle)** : volume élevé mais risque ban + violation ToS. Rejeté.
2. **LinkedIn Official API (Marketing / Community)** : pas d'accès au feed personnel, orienté pages/ads. Rejeté pour ce use case.
3. **Capture humaine + pipeline local** : Paul navigue, sélectionne, Cmd+C ; OCR ou email en complément ; stockage Obsidian + SQLite. Choisi.
4. **Services tiers (PhantomBuster, etc.)** : même risque ban, dépendance externe. Rejeté.

## Decision

**Chosen**: Option 3 — human-in-the-loop capture avec double stockage :
- **Obsidian** (`writing-vault/linkedin/feed-capture/inbox.md`) = journal lisible, édition manuelle
- **SQLite** (`content-engine/data/linkedin.db`) = requêtes, dédup, stats, scale

**Reasoning** : répond au vrai besoin (intelligence sur *ce que Paul lit*), zéro automation LinkedIn, réutilise l'infra déjà en prod (clipboard watcher actif).

## Architecture (4 phases)

| Phase | Statut | Livrable |
|-------|--------|----------|
| 1 Capture | **Actif** | `linkedin-watch-start`, OCR, inbox Obsidian |
| 2 Structure | **En cours** | `linkedin_db.py`, sync, indexes, dedup hash |
| 3 Intelligence | À faire | embeddings, ranking, comment scoring LLM |
| 4 Engagement | Manuel | queue commentaires → publication humaine |

## Action Items

- [x] Valider que le watcher tourne et remplit l'inbox
- [x] Créer `linkedin_db.py` + sync depuis inbox
- [ ] Activer notifications email LinkedIn → Gmail (feed partiel)
- [ ] Phase 3 : embeddings locaux (QMD collection `linkedin-feed`)
- [ ] Apprendre SQL via requêtes réelles sur `linkedin.db`

## Related

- [[_system/MOC-decisions]]
- [[brantham/_MOC]]
- [[writing-vault/linkedin/SYSTEME-LINKEDIN-BRANTHAM]]
