---
date: 2026-04-26
project: brantham
tags: [pattern, db, postgres, sqlite, abstraction]
---

# Pattern : Abstraction DB SQLite ↔ Postgres avec HybridRow

## Quoi
Code Python qui parle indifféremment à SQLite local OU à Postgres distant (Supabase) via une **API unique** qui mime `sqlite3.Row`. Détection automatique du backend depuis `DATABASE_URL` env.

## Pourquoi
- Permet le dev local rapide (SQLite, microsec/query) et la prod collab (Postgres distant)
- Évite de réécrire des centaines de lignes de SQL
- Compatibilité descendante : code legacy SQLite continue de marcher

## Comment

### 1. Détection backend
```python
DATABASE_URL = os.environ.get("DATABASE_URL", "").strip() or None
USE_POSTGRES = bool(DATABASE_URL and DATABASE_URL.startswith(("postgres://", "postgresql://")))
```

### 2. HybridRow custom — clé du pattern
`sqlite3.Row` supporte 3 modes d'accès :
- `row[0]` (par index)
- `row["col_name"]` (par clé)
- `iter(row)` itère sur les **values** (pas les keys comme un dict normal)

`psycopg.rows.dict_row` ne fait que `row["col_name"]`. **`dict(rows_list)` casse en silence** : la fonction itère les keys du dict (= "col_name", "col_name", ...) au lieu des values.

Solution : Row class qui hérite de dict mais override `__iter__` :

```python
class HybridRow(dict):
    __slots__ = ("_columns",)

    def __init__(self, columns: list[str], values: tuple):
        super().__init__(zip(columns, values))
        self._columns = columns

    def __getitem__(self, key):
        if isinstance(key, int):
            return super().__getitem__(self._columns[key])
        return super().__getitem__(key)

    def __iter__(self):
        # Comme sqlite3.Row : itère les values dans l'ordre
        for col in self._columns:
            yield super().__getitem__(col)

    def keys(self):  return list(self._columns)
    def values(self): return [super().__getitem__(c) for c in self._columns]
    def items(self):  return [(c, super().__getitem__(c)) for c in self._columns]
```

Ainsi `dict(conn.execute("SELECT a, b FROM t").fetchall())` rend `{a_value: b_value}` pour chaque row 2-cols, comme avec sqlite3.Row.

### 3. Connection persistante singleton
Critique pour Postgres distant (latence Ireland 50-200ms par TCP+TLS handshake) :

```python
_PERSISTENT = {"conn": None}

def _get_persistent():
    c = _PERSISTENT["conn"]
    if c is None:
        c = _connect_postgres() if USE_POSTGRES else _connect_sqlite()
        _PERSISTENT["conn"] = c
    elif USE_POSTGRES:
        # Vérifie si vivante, reconnecte si cassée
        try: c._conn.execute("SELECT 1")
        except Exception:
            c.close()
            c = _connect_postgres()
            _PERSISTENT["conn"] = c
    return c

@contextmanager
def session():
    conn = _get_persistent()
    try:
        yield conn
        conn.commit()
    except Exception:
        if USE_POSTGRES:
            try: conn._conn.rollback()
            except Exception: close_persistent()
        raise
```

**Gain mesuré** : 152ms/query (persistante) vs 376ms/query (jetable) = ~2.5×.

### 4. Wrapper `?` → `%s`
Les SQL existants utilisent `?` (SQLite). Postgres veut `%s`. Wrapper qui traduit à la volée :

```python
class _PgConnWrapper:
    def execute(self, sql: str, params=None):
        sql_pg = sql.replace("?", "%s")  # naïf mais OK car nos SQL n'ont pas de ? littéraux
        cur = self._conn.cursor()
        if params is None: cur.execute(sql_pg)
        else: cur.execute(sql_pg, list(params) if not isinstance(params, (list,tuple)) else params)
        return _PgCursorWrapper(cur)
```

### 5. Helpers portables pour `date('now')`
SQLite-only : `date('now')`, `date('now', '+7 days')`. Solution : pré-calculer en Python :

```python
def today_iso() -> str:
    from datetime import date
    return date.today().isoformat()

def iso_offset(days: int) -> str:
    from datetime import date, timedelta
    return (date.today() + timedelta(days=days)).isoformat()
```

Et dans le SQL : `WHERE date_limite >= ?` avec `(today_iso(),)` en param.

## Pièges
- **`HAVING n` avec alias** : marche en SQLite, **pas en Postgres**. Toujours utiliser `HAVING COUNT(*) >= 5`.
- **`AUTOINCREMENT`** : SQLite spécifique. Postgres = `BIGSERIAL` ou `GENERATED ALWAYS AS IDENTITY`. Schéma adapté avec `s.replace("INTEGER PRIMARY KEY AUTOINCREMENT", "BIGSERIAL PRIMARY KEY")` au démarrage Postgres.
- **`CREATE INDEX IF NOT EXISTS`** : OK des deux côtés.
- **Foreign keys** : SQLite nécessite `PRAGMA foreign_keys = ON`. Postgres : ON par défaut.

## Where
- Code : `/Users/paul/Downloads/brantham-pipeline/cockpit/db.py`
- Migration script : `cockpit/migrate.py`
- Doc onboarding : `cockpit/INSTALL_SOREN.md`

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/bugs/2026-04-26-hybridrow-iter-postgres]]
- [[brantham/bugs/2026-04-26-postgres-having-alias]]
- [[founder/decisions/2026-04-26-supabase-vs-vps-hetzner]]
- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
