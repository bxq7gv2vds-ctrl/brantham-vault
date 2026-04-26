---
name: Data layer NO tokens — fix data layer + backfill
description: Bug 4 du reverse-engineer-true-winners. all_markets.db.markets ne stockait que token_id_yes. ~70% du volume USDC (NO trades) était invisible. Fix W1.3 2026-04-26 — schema + backfill 5282 markets + scraper 1.28M trades NO.
type: bug
project: brantham/polymarket
created: 2026-04-26
status: fixed
priority: critical
tags: [polymarket, bug, data-layer, fix, scraper]
---

# Bug 4 — Data layer ne capturait que YES tokens

## Découverte

Reverse engineering top winners 2026-04-25/26 (`reverse-engineer-true-winners.md`).
`trades_onchain.db` était populé en ne fetchant que `token_id_yes` from
`all_markets.db`. Pour `0x4eb5` audit : YES vol $40k visible, **NO vol
$110k invisible** (~70% du volume).

## Cause racine

1. Schema `all_markets.markets` n'avait pas de colonne `token_id_no`
2. `fetch_trades_subgraph.py::list_tokens()` ne lisait que `token_id_yes`
3. Scraper Goldsky ne fetchait jamais le NO token

## Fix

### 1. Schema (DB)
```sql
ALTER TABLE markets ADD COLUMN token_id_no TEXT;
```

### 2. Backfill (script nouveau)
`scripts/backfill_token_id_no.py` :
- Fetch authoritative `clob.polymarket.com/markets/{cid}` per market
- Update `markets.token_id_no` from `tokens[1].token_id`
- Concurrent (12 workers, ~50 req/s)

Run : `--since 2026-03-27` → **5282/5296 markets backfilled (99.7%)**

### 3. Patch scraper
`scripts/fetch_trades_subgraph.py::list_tokens()` retourne maintenant
4-tuples `(token_id, city, date, side)` avec une row par side.

### 4. Re-run scraper sur 30j
- **3737 NO tokens fetched** (39 empty, 0 errors)
- **+1,284,104 NO trades insérés** en 39.5 min

## Validation empirique (since 2026-04-01)

| Métrique | NO | YES | NO ratio |
|---|---:|---:|---:|
| Trade count | 1,275,770 | 2,307,881 | 36% |
| **USDC volume** | **$31,505,560** | **$10,031,175** | **76%** |

**Confirme la hypothèse du reverse-engineering** : NO trades sont
individuellement plus grands (~$24.7/trade vs ~$4.3/trade pour YES) et
représentent **76% du volume USDC** sur weather Polymarket.

## Implications

- Les analyses passées sur `trades_onchain.db` étaient biaisées YES-only
- Top winner P&L re-calculé via activity API (cf [[reverse-engineer-true-winners]])
- Future signal generation peut maintenant utiliser orderbook NO direct
- Notre Tier S YES deep_OTM strategy ratait 76% du marché

## TODO suite

- Étendre backfill aux markets pre-2026-03-27 si besoin historique long
- Ajouter `token_id_no` à l'ingestion live (pas seulement backfill)
- Re-run analyses P&L par wallet pour identifier patterns NO winners
- Étendre scraper aux brackets non-`highest-temperature` (precip, snow, lowest-temp)

## Code

- Schema patch : `sqlite3 all_markets.db "ALTER TABLE markets ADD COLUMN token_id_no TEXT;"`
- Backfill : `scripts/backfill_token_id_no.py`
- Scraper patch : `scripts/fetch_trades_subgraph.py` (list_tokens)
- Logs : `logs/scrape-no-tokens.log`

## Related

- [[brantham/polymarket/reverse-engineer-true-winners]] — bug parent (4 bugs)
- [[brantham/polymarket/strategy-2026-04-26]] — strategy doc (W1.3)
- [[brantham/bugs/2026-04-26-dedup-not-applied-to-pnl-queries]] — bug sister
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
