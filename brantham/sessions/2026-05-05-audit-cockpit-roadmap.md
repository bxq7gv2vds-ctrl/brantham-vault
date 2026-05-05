---
date: 2026-05-05
project: brantham
type: session
tags: [cockpit-web, audit, roadmap, M&A]
---

# Session 2026-05-05 — Audit cockpit + roadmap 20 étapes

## Contexte

Reprise après session 2026-04-28 (minimalisme + outreach tracker). Demande user : audit complet sur 4 axes — coverage marché DLDO, workflow process end-to-end, sourcing acquéreurs, qualité produit / vendabilité SaaS.

## Audit (4 agents parallèles)

1. **Coverage marché** — 33 AJ scrapés, 8 cassés silencieusement, cron `daily-scrape` pas chargé (48h sans scrape), 67% des DLDO passés non purgés, BODACC API absent. Score 50-60%.
2. **Workflow process** — 6 phases sur 10 forcent à sortir du cockpit (extension NDA, LdM, teaser, NDA repreneur, envoi mails, data room, offres+facturation). Score 45%.
3. **Sourcing acquéreurs** — 0/148 NAF en DB réelle (vs 44% claim STATE.md), `PAPPERS_API_KEY` et `HUNTER_IO_KEY` absentes du `.env` → 0 enrichissement contact. Score 25%.
4. **Qualité produit** — Path `/Users/paul/Downloads/brantham-pipeline` hardcodé `hunters/stream/route.ts:5`, 0 auth, 0 multi-tenant, 0 tests, hydration mismatch `Cockpit.tsx:58`, RepreneursPanel.tsx 1448 lignes monolithe. Score 4/10.

## Roadmap

20 étapes en 7 blocs (A→G) — voir [[brantham/cockpit/roadmap-2026-05-05]].

## Étape 1 livrée

`launchctl load ~/Library/LaunchAgents/com.brantham.daily-scrape.plist` + `launchctl start com.brantham.daily-scrape` pour scrape immédiat. Le job tourne désormais à 8h chaque jour, alimente Supabase via `cockpit.import_scan`. Distinct de `com.brantham.scrape-enrich` (existant, toutes les 3h, alimente l'ancien dashboard `brantham-partners/api/`).

## Décisions

- Roadmap exécutée séquentiellement (pas en swarm parallèle) pour éviter les conflits multi-fichiers.
- Priorité semaine 1 : étapes 1-4 (quick wins) + étape 8 (teaser) pour Magic Form J-16 (deadline 21/05).
- Blocs F (déploiement) + G (SaaS) repoussés mois 2-3.

## Related

- [[brantham/_MOC]]
- [[brantham/cockpit/roadmap-2026-05-05]]
- [[brantham/sessions/2026-04-28-cockpit-minimalisme-outreach]]
- [[brantham/deals/active/magic-form-levallois/_MOC]]
- [[_system/MOC-decisions]]
