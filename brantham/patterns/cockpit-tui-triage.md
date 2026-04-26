---
projet: brantham
type: pattern
tags: [tui, textual, sqlite, cockpit, triage]
date: 2026-04-26
---

# Pattern — Cockpit TUI triage opportunités

## Contexte
Quand on a beaucoup d'items à trier (opps AJ, deals, leads…) avec actions répétitives (shortlist/poubelle/note), un TUI Textual avec DB SQLite locale bat un dashboard web pour la vélocité d'usage en solo.

## Solution
Architecture en 4 modules séparés :
1. **`db.py`** — schéma SQLite (WAL + foreign keys), helpers `connect()` / `session()` context manager
2. **`import_*.py`** — upsert depuis source externe → DB. **Préserve les champs `user_*`** entre runs (status, note). Audit log dans table `events`.
3. **`enrich_*.py`** — parallèle `ThreadPoolExecutor`, mise à jour incrémentale (skip déjà OK sauf `--force`)
4. **`tui.py`** — Textual app, lecture/écriture directe sur la DB

## Clés du TUI Textual
- **DataTable + Header + Footer + Static stats bar** — layout simple
- Bindings courts (1 char) qui mappent à `action_*` methods
- Modal screens (`ModalScreen[T | None]`) pour notes/recherche
- `Text.style` pour couleurs urgence (J-7 rouge gras, J-30 jaune…)
- Cursor row → `self.row_ids[table.cursor_row]` pour mapping vers ID

## Persistance
- Tous les changements UI → `UPDATE` immédiat dans la DB
- Re-imports d'un scan préservent les statuts user (UPDATE conditionnel)
- `events` table = audit log (kind, target_id, payload JSON)

## Filtres
- **Status** (cycle) : all / nouveau / shortlist / archive
- **Vie** (cycle) : actives / expirees / sans_dldo / tout
- **Search** libre via modal Input
- **Bin toggle** (cache poubelle par défaut)

Footer affiche live le compte des visibles vs total + breakdown par status.

## Anti-patterns évités
- ❌ Pas de microservices / API REST → DB locale = source unique de vérité
- ❌ Pas de framework web → terminal direct, raccourcis 1 char
- ❌ Pas de YAML/JSON config → tout en code Python
- ❌ Pas de tests automatisés sur le TUI (Textual `run_test` pour smoke seulement)

## Test pilot Textual
```python
async with app.run_test(size=(180, 50)) as pilot:
    await pilot.pause()
    await pilot.press('s', 'down', 'd')
    # vérifier état DB
```

## Lancer
```bash
python3 -m cockpit          # TUI
python3 -m cockpit.import_scan
python3 -m cockpit.enrich_dldo --force
```

## Origine
Né de la session [[brantham/sessions/2026-04-26-cockpit-aj]] pour trier 200+ opportunités AJ par DLDO ascendant.

## Related
- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
- [[brantham/sessions/2026-04-26-cockpit-aj]]
- [[brantham/patterns/dldo-extraction-regex-fr]]
