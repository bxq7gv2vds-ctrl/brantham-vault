---
name: Polymarket tracking infra — dashboard + telegram bot
date: 2026-04-13
project: polymarket-hedge
type: session
tags: [polymarket, infra, dashboard, telegram, gamma-api]
---

# Session — Tracking Infra CONVEX_YES v2a

## Contexte

Après déploiement de CONVEX_YES v2a (TTR 6-14h, 23 villes v3), construction
de l'infrastructure de tracking live pour suivre la stratégie sur plusieurs
semaines. Objectif : dashboard web sobre + bot Telegram pour consultation
mobile et alertes push.

## Réalisations

### 1. Dashboard web terminal (`scripts/web_dashboard.py`)

Design "terminal sobre" — fond noir, monospace, aucun emoji/couleur vive.

**Features :**
- KPIs : capital, p&l réalisé, live p&l (MTM), open positions, expo
- Tableau positions ouvertes avec colonnes : `resolves`, `ttr`, `city` (cliquable), `bracket`, `type`, `wr`, `entry`, `live`, `Δ`, `mtm`, `win @$2.5`, `ev`
- Prix live via Gamma API, rafraîchis toutes les 10s sans reload du tableau
- P&L mark-to-market par position = `(size/entry) × current - size`
- Liens Polymarket event-level par ville (via regex strip du suffixe température)
- Filtre `STRAT_TYPES = ("CONVEX_YES",)` — ignore SPEEDA/LONGSHOT/COLDMATH
- `BANKROLL = 100` hardcodé (bankroll de tracking live v2a, indépendant du compte)
- `TRACK_FROM = 1776038400.0` (2026-04-13 00:00 UTC) — hardcodé après bug datetime

**Endpoints API :**
- `GET /api/summary` — KPIs globaux
- `GET /api/open` — positions ouvertes (async, fetch slugs Gamma en parallèle)
- `GET /api/prices` — prix live via Gamma API (outcomePrices)

### 2. Bot Telegram (`scripts/telegram_bot.py` + `scripts/telegram_notifier.py`)

**Commandes** :
- `/open` — positions en cours (25 prochaines à expirer, total affiché)
- `/pnl` — P&L jour + total + capital
- `/status` — snapshot global
- `/today` — trades settlés aujourd'hui (W/L détaillé)
- `/help` — liste commandes

**Notifications push** (appelées depuis scalper + dashboard) :
- `notify_open(city, type, entry, size, bracket, ttr, resolve, wr, market_id, question)`
- `notify_settle(city, type, entry, size, won, pnl, day_pnl, n_settled, market_id, question)`

**Format HTML** :
- Titres en `<b>`, types en `<code>`
- Ville cliquable via `<a href="url">City</a>` (event slug Polymarket)
- Séparateurs `━━━━━━━━━━━━━━━━━━━━` pour délimitation visuelle
- Valeurs numériques en `<code>` pour monospace

**Credentials** : `.env` → `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID=1742199786`

### 3. Désactivation stratégies hors v2a

Dans `run_bracket_scalper.py` :
- `longshot_yes_enabled: bool = False` — désactivé (TTR > 48h, hors scope v2a)
- SPEEDA_EARLY / SPEEDA_YES : `if False and yes_price < 0.99` — désactivé par flag

Résultat : le scalper ne génère plus que des CONVEX_YES avec TTR 6-14h.

## Bugs résolus

### Bug 1 — `TRACK_FROM` année 2025 au lieu de 2026

`datetime(2026, 4, 13, tzinfo=timezone.utc).timestamp()` retournait
`1744502400.0` (13/04/2025). Fix : hardcoded `TRACK_FROM = 1776038400.0`.

### Bug 2 — Gamma API `outcomePrices` est une string JSON

La Gamma API retourne `outcomePrices: '["0.0115","0.9885"]'` (string JSON,
pas array Python). Le code faisait `float(op[0])` qui tentait de convertir
`'['` en float → `ValueError`. Fix : `json.loads(op) if isinstance(op, str) else op`.

### Bug 3 — Liens Polymarket `/event/{slug}` 404

Les slugs des markets individuels (ex: `highest-temperature-in-madrid-on-april-14-2026-23c`)
n'existent pas comme events sur Polymarket. L'event parent est `highest-temperature-in-madrid-on-april-14-2026`
(sans le suffixe `-23c`).

**Fix** : regex strip du suffixe température :

```python
_TEMP_SUFFIX = re.compile(
    r"-\d{1,3}(-\d{1,3})?[cf](or(higher|lower|below|above|more|less))?(deg)?$"
)
event_slug = _TEMP_SUFFIX.sub("", market_slug)
```

Contraintes :
- `\d{1,3}` max 3 chiffres pour éviter de matcher `-2026` (année)
- Support : `-23c`, `-10-11c`, `-90-91f`, `-29corhigher`, `-5corlower`, `-10corbelow`, `-15corabove`

Testé : 106/106 positions retournent `HTTP 200` sur les liens event.

### Bug 4 — Expo KPI ne cappait pas à $2.5

`api_summary()` utilisait `sum(size_usdc)` sans cap, affichant $3040 d'expo.
Fix : `sum(min(size_usdc, 2.5))` pour aligner sur le sizing live.

### Bug 5 — BANKROLL incohérent dashboard vs bot

Dashboard original : `BANKROLL=100` (défaut sans `load_dotenv`).
Bot : `BANKROLL=10000` (chargé depuis `.env`).
Fix : hardcodé `BANKROLL = 100.0` dans les deux (bankroll de tracking v2a).

## État final

- 106 positions CONVEX_YES ouvertes, 0 settled
- Capital $100, P&L $0
- Prochaine expiration : **14/04 12:00 UTC**
- Scalper live : 23 villes v3, TTR 6-14h, $2.5/trade
- Dashboard : <http://localhost:8765>
- Bot Telegram : commands live + notifications push

## Next

1. Observer les premiers settlements 14/04 12:00 UTC (WR attendu 8.5%)
2. Recalibrer WR live après N=50 puis N=200 trades settlés
3. Deploy sur VPS avec launchd pour 24/7 tracking
4. Passer en live trading après confirmation WR live ≥ 6%

## Related

- [[_system/MOC-patterns]]
- [[_system/MOC-bugs]]
- [[patterns/polymarket-convex-yes-v2-optimization]]
- [[patterns/polymarket-convex-yes-complete-breakdown]]
- [[patterns/polymarket-tracking-infrastructure]]
