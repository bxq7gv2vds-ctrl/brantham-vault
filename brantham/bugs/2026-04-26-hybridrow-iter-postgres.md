---
date: 2026-04-26
project: brantham
tags: [bug, db, postgres, fixed]
severity: high
---

# Bug : `dict(rows)` crash en Postgres car HybridRow itère les noms de colonnes

## Symptôme
Quand on switche d'onglet dans le TUI Cockpit (mode Postgres), crash systématique :
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
  in update_stats:
    stage_counts = dict(conn.execute("SELECT stage, COUNT(*) FROM deals GROUP BY stage").fetchall())
    total = sum(stage_counts.values())
```

Et sortie du TUI dans le shell — UX catastrophique.

## Cause racine
Différence de comportement entre `sqlite3.Row` et le `HybridRow` custom (qui hérite de `dict`) :

- `sqlite3.Row`: `iter(row)` renvoie les **values** dans l'ordre des colonnes
- `dict`: `iter(d)` renvoie les **keys**

Donc `dict([row1, row2])` :
- En SQLite : `dict([("won", 1), ("lost", 0)])` → `{"won": 1, "lost": 0}` ✓
- En HybridRow : Python tuple-unpack chaque row via `iter()` qui renvoie `("stage", "count")` (les noms de colonnes !) → `{"stage": "count"}` ✗

→ `stage_counts.values()` = `["count"]` (une string), `sum(["count"])` = TypeError.

## Fix
Override `__iter__` dans `HybridRow` pour mimer `sqlite3.Row` (itérer les values) :

```python
class HybridRow(dict):
    def __iter__(self):
        # Comme sqlite3.Row : itère les values dans l'ordre des colonnes
        for col in self._columns:
            yield super().__getitem__(col)
```

Aussi override `values()` et `items()` pour cohérence :
```python
def values(self):
    return [super(HybridRow, self).__getitem__(c) for c in self._columns]
def items(self):
    return [(c, super(HybridRow, self).__getitem__(c)) for c in self._columns]
```

## Vérification
Smoke test 10 tab switches enchaînés en mode Postgres → 0 crash après fix.

## Leçon
Dès qu'on hérite de `dict` pour mimer un autre Row type (sqlite3.Row, namedtuple…), il faut **explicitement override `__iter__`** sinon le dict.__iter__() prend le dessus et casse les usages legacy comme `dict(cursor.fetchall())`.

## Where
- Fichier : `/Users/paul/Downloads/brantham-pipeline/cockpit/db.py`
- Class : `HybridRow`
- Tests : smoke test enchaîné `pilot.press("2")...pilot.press("5")` → 0 erreur

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/patterns/db-abstraction-sqlite-postgres-hybridrow]]
- [[brantham/_MOC]]
- [[_system/MOC-bugs]]
