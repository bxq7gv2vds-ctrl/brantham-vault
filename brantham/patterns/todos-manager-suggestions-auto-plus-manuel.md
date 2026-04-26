---
date: 2026-04-26
project: brantham
tags: [pattern, todos, suggestions, productivity]
---

# Pattern : Todo manager auto+manuel pour résoudre la procrastination

## Quoi
Système de tâches qui combine :
- **Suggestions auto-générées** par règles métier (deadlines, pipeline endormi, doc manquante…)
- **Tâches custom manuelles** ajoutées à la volée

Avec **état persistant** (done / ignored / snoozed) qui survit aux redémarrages et est partagé entre Paul + Soren.

## Pourquoi
Paul a explicité : "j'ai un petit problème pour me bouger et savoir ce que je dois faire". Le TUI passif ("voici les opps") ne suffit pas — il faut un cockpit qui **dit quoi faire en premier**, dans l'ordre, avec ce qu'on peut décider de skipper.

## Comment

### Schéma DB
```sql
CREATE TABLE todos (
    id              TEXT PRIMARY KEY,        -- 'auto_<hash>' ou 'man_<uuid>'
    source          TEXT NOT NULL,           -- 'auto' | 'manual'
    title           TEXT NOT NULL,
    detail          TEXT,
    priority        TEXT,                    -- urgent / important / normal / info
    category        TEXT,                    -- deadline / pipeline / doc / veille / decision / custom
    target_kind     TEXT,                    -- deal | opp | NULL
    target_id       TEXT,
    assigned_to     TEXT,                    -- paul / soren / NULL
    due_date        TEXT,
    status          TEXT NOT NULL DEFAULT 'open',  -- open / done / ignored / snoozed
    snoozed_until   TEXT,                    -- ISO date
    created_at      TEXT NOT NULL,
    completed_at    TEXT,
    completed_by    TEXT
);
```

### ID stable pour les auto-suggestions
Pour qu'une même suggestion garde son état entre runs :
```python
def _make_auto_id(s: Suggestion) -> str:
    raw = f"{s.target_kind or ''}|{s.target_id or ''}|{s.category}|{s.title}"
    return "auto_" + hashlib.md5(raw.encode("utf-8")).hexdigest()[:16]
```

Si `MARTECH deadline J+1` est ignoré, le hash reste pareil au prochain run → pas réaffiché.

### Sync à chaque load
À chaque ouverture de l'onglet À faire :
1. `generate_suggestions()` calcule les nouvelles suggestions (basé sur état DB actuel)
2. Pour chaque sug : check si row déjà en `todos`. Si oui → skip. Si non → INSERT.
3. `list_open()` filtre : `status='open' OR (status='snoozed' AND snoozed_until <= today)`
4. Tri : urgent > important > normal > info, puis due_date, puis title

### Actions de management
| Touche | Action | DB update |
|---|---|---|
| Espace | ✓ Fait | `status='done', completed_at=now, completed_by=assignee` |
| `i` | ✕ Ignorer | `status='ignored'` (jamais réaffiché) |
| `z` | ⏰ Snoozer 3j | `status='snoozed', snoozed_until=today+3` |
| `+` | Ajouter manuel | INSERT avec `id='man_<uuid>'` |
| `@` | Cycler assignation | `assigned_to=paul/soren/NULL` |
| `F` | Cycler filtre vue | `assigned_to in (cur_user, NULL)` ou ALL |

### 7 catégories de détection auto
1. **Deadline** : deal deadline_offre J-3/J-7/passée
2. **Action en retard** : next_action_date < today
3. **Pipeline endormi** : stage in (mandat, sourcing, outreach, DD) + updated_at > 7-10j
4. **Documentation manquante** : deal sans next_action / sans notes / sans assignment
5. **Won sans rétro** : stage=won + notes vide
6. **Décision opps** : opps shortlistées DLDO J-7 non promues en deal
7. **Veille** : scan AJ > 2j ; source AJ silencieuse > 14j

### Filtre par assignation (collab)
3 modes cyclables :
- `ALL` : voit tout (par défaut)
- `paul` : ses propres tâches + non assignées
- `soren` : pareil pour Soren

Permet à chacun de voir uniquement ce qu'il doit faire sans noyade.

### Custom todos via modal
Touche `+` ouvre `NewTodoModal` avec champs :
- Titre (obligatoire)
- Détail (optionnel)
- Priorité (urgent/important/normal/info, défaut normal)
- Assigné à (paul/soren/vide)
- Échéance ISO (optionnelle)

Validé par ctrl+s.

## Pourquoi cette architecture
- **Auto + manuel** = couvre les obligations détectées par règles ET les tâches ad hoc
- **Persistant DB** = pas de perte d'état au crash/restart
- **ID stable hash** = la même suggestion garde son histoire (pas de spam de tâches "déjà ignorées")
- **Snooze** = permet de différer sans perdre la trace (ressort dans 3j)
- **Filtre par assignation** = chacun voit son scope, sans interférer

## Anti-patterns évités
- ❌ Régénérer les suggestions à chaque tick + perdre l'état → spam
- ❌ Suggestions seulement (pas de manuel) → trop rigide
- ❌ Manuel seulement → tout repose sur la mémoire du user (= sa procrastination)
- ❌ Pas de filtre @ → saturation visuelle quand 50+ tâches

## Where
- Code : `cockpit/suggestions.py` (génération) + `cockpit/todos.py` (persistance) + `cockpit/tui.py` (UI onglet À faire)
- Schema : `cockpit/db.py:_ensure_todos_table()` (idempotent SQLite + Postgres)

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
