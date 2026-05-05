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

- `launchctl load com.brantham.daily-scrape.plist` ✓
- Bug fixé dans `daily_scrape.sh:30` : `import_scan "$SCAN"` → `import_scan --scan "$SCAN"` (signature flag)
- Scrape manuel + import Supabase : +40 new, 418 updated, **458 total**
- Cockpit live : actives 148 → 188, last_scrape_at à jour, new_24h = 40

**Blocage TCC** : launchd refuse d'exécuter le script dans `~/Downloads/` (`Operation not permitted` — protection macOS). Le job tournera à 8h demain seulement si on déplace le pipeline (étape 16 anticipée) ou si l'user donne Full Disk Access à `/bin/bash` via System Settings. Le scrape manuel via shell user marche, c'est juste launchd qui est bloqué.

## Étape 2 livrée

- Migration `007_purge_dldo_expired.sql` appliquée : colonne `auto_archived_at TIMESTAMPTZ` + index partiel
- Script idempotent `cockpit/cron_purge_expired.py` : auto-archive opps DLDO passé >7j en statut 'nouveau' uniquement (préserve tri user)
- Intégré au `daily_scrape.sh` : tournera après chaque scrape
- **263 opps archivées** en 1 run. Filtre Vue "⌫ archivées" déjà existant les retrouve toutes.

## Étape 4 livrée — fix hydration

`components/Cockpit.tsx:58` : `useState(() => new Date().toLocaleString())` exécuté SSR + CSR créait 1s de drift → React regenerait tout le tree à chaque render. Fix 2 edits : init `useState("")` + tick immédiat dans `useEffect`. Aucune erreur hydration dans les logs après reload.

**Étape 3 (clés API)** différée — action user requise (signup Pappers + Hunter.io).

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
