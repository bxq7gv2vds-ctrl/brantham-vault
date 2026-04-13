---
name: Polymarket Tracking Infrastructure (Dashboard + Telegram)
type: pattern
date: 2026-04-13
project: polymarket-hedge
tags: [polymarket, infra, dashboard, telegram, gamma-api, monitoring]
---

# Polymarket Tracking Infrastructure

Infrastructure de monitoring pour une stratégie de trading sur Polymarket —
dashboard web terminal + bot Telegram avec commandes et notifications push.

## Contexte

Après la validation d'une stratégie (CONVEX_YES v2a dans ce cas), besoin de :
1. **Dashboard web sobre** pour visualiser les positions ouvertes avec prix live
2. **Bot Telegram** pour consultation mobile et alertes push
3. **Filtrage par stratégie** pour éviter la pollution du tracking par d'autres signaux
4. **Prix live et P&L mark-to-market** pour voir les mouvements en temps réel

## Architecture

```
bracket_scalper_trades.db
         │
         ├──→ scripts/web_dashboard.py  (FastAPI + HTML terminal)
         │         │
         │         ├── /api/summary  (KPIs)
         │         ├── /api/open     (async, batch fetch Gamma slugs)
         │         ├── /api/prices   (async, Gamma API outcomePrices)
         │         └── /api/settle   (METAR resolution → notify_settle)
         │
         ├──→ scripts/telegram_bot.py  (polling + commandes)
         │         │
         │         ├── /open   /pnl   /status   /today   /help
         │         └── Cache slugs Gamma
         │
         ├──→ scripts/telegram_notifier.py  (module push léger)
         │         │
         │         ├── send(text) — urllib, pas de deps lourdes
         │         ├── notify_open(...)
         │         └── notify_settle(...)
         │
         └──→ scripts/run_bracket_scalper.py
                   │
                   └── send_telegram() → aiohttp, alerte à chaque nouveau trade
```

## Composants clés

### 1. Dashboard web terminal

**Design** : fond noir, monospace (`JetBrains Mono`), aucun emoji/couleur vive.

**CSS minimal** :

```css
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#000;color:#c8c8c8;font-family:"JetBrains Mono",monospace;font-size:13px}
.dim{color:#444}  .lo{color:#666}  .hi{color:#eee;font-weight:bold}
.pos{color:#e8e8e8}  .neg{color:#666}
.up{color:#e8e8e8}.dn{color:#3a3a3a}
```

**KPIs** : capital, P&L réalisé, live P&L (MTM), open, expo.

**Table open** :

```
resolves | ttr | city (lien) | bracket | type | wr | entry | live | Δ | mtm | win | ev
```

- `live` = prix actuel (rafraîchi toutes les 10s via `/api/prices`)
- `Δ` = delta depuis entry (coloration pos/neg)
- `mtm` = `(size/entry) × current - size` = valeur à la revente maintenant

**JavaScript — update en place sans reload** :

```javascript
function updatePrices() {
  fetch('/api/prices').then(r => r.json()).then(data => {
    let totalMtm = 0, nPriced = 0;
    Object.entries(data).forEach(([sid, info]) => {
      const row = document.querySelector(`tr[data-sid="${sid}"]`);
      if (!row) return;
      const entry = parseFloat(row.dataset.entry);
      const size  = parseFloat(row.dataset.size);
      const mtm   = (size / entry) * info.current - size;
      totalMtm += mtm; nPriced++;
      // Update cells in place
      row.querySelector('[data-live]').textContent = (info.current * 100).toFixed(2) + '%';
      row.querySelector('[data-delta]').textContent = (info.delta >= 0 ? '+' : '') + (info.delta * 100).toFixed(2) + '%';
      row.querySelector('[data-mtm]').textContent = (mtm >= 0 ? '+' : '') + '$' + Math.abs(mtm).toFixed(2);
    });
    if (nPriced > 0) $('k-ev').textContent = (totalMtm >= 0 ? '+' : '-') + '$' + Math.abs(totalMtm).toFixed(2);
  });
}
setInterval(updatePrices, 10000);
```

### 2. Gamma API — prix live

L'API Gamma `https://gamma-api.polymarket.com/markets/{market_id}` retourne
`outcomePrices` comme **string JSON**, pas comme array Python :

```python
# Attention : outcomePrices est une string JSON
op = d.get("outcomePrices")  # '["0.0115","0.9885"]'
op_list = json.loads(op) if isinstance(op, str) else op
yes_price = float(op_list[0])
```

**Batch fetch async** :

```python
async def _fetch_gamma_prices(market_ids: list[str]) -> dict[str, float]:
    prices = {}
    sem = asyncio.Semaphore(10)  # max 10 requêtes concurrentes
    async def _one(sess, mid):
        async with sem:
            async with sess.get(f"{GAMMA_API}/markets/{mid}", timeout=4) as r:
                if r.status == 200:
                    d = await r.json(content_type=None)
                    op = d.get("outcomePrices")
                    if op:
                        op_list = json.loads(op) if isinstance(op, str) else op
                        prices[str(mid)] = float(op_list[0])
    async with aiohttp.ClientSession() as sess:
        await asyncio.gather(*[_one(sess, m) for m in market_ids])
    return prices
```

### 3. Gamma API — event slugs pour liens cliquables

Les slugs des **markets individuels** (ex: `highest-temperature-in-madrid-on-april-14-2026-23c`)
ne sont **pas** des URLs valides — ils retournent HTTP 404.

L'**event slug parent** (qui groupe tous les buckets de température) est le
slug du market sans le suffixe de température :
`highest-temperature-in-madrid-on-april-14-2026` → HTTP 200

**Fix — regex strip** :

```python
import re
_TEMP_SUFFIX = re.compile(
    r"-\d{1,3}(-\d{1,3})?[cf](or(higher|lower|below|above|more|less))?(deg)?$"
)

def market_slug_to_event(slug: str) -> str:
    return _TEMP_SUFFIX.sub("", slug)

# Tests :
# -23c               → strippé
# -10-11c            → strippé
# -90-91f            → strippé
# -29corhigher       → strippé
# -5corlower         → strippé
# -10corbelow        → strippé
# -15corabove        → strippé
```

**Contrainte importante** : `\d{1,3}` max 3 chiffres pour éviter de matcher
`-2026` (année) qui fait 4 chiffres.

**Cache** : stocker les event URLs dans un dict en mémoire (`_gamma_slugs: dict[str, str]`)
pour éviter les refetch.

### 4. Bot Telegram — notifier module léger

Pas de `python-telegram-bot` (lourd). Un module minimal avec `urllib` :

```python
import urllib.request, json

def send(text: str) -> bool:
    payload = json.dumps({
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.loads(r.read()).get("ok", False)
```

### 5. Bot Telegram — polling commandes

Long-polling simple avec `getUpdates` (`timeout=20`). Filtrer par `chat_id` pour ignorer
les messages des autres :

```python
def main():
    offset = 0
    while True:
        updates = get_updates(offset)
        for u in updates:
            offset = u["update_id"] + 1
            msg = u.get("message", {})
            if str(msg.get("chat", {}).get("id", "")) != str(CHAT_ID):
                continue
            text = msg.get("text", "")
            if not text.startswith("/"):
                continue
            reply = handle(text)
            if reply:
                send(reply)
        time.sleep(1)
```

### 6. Format messages Telegram — HTML sobre

**Notifications push** (trades) :

```
OPEN  convex_yes
━━━━━━━━━━━━━━━━━━━━
Tokyo  ·  15-16C
entry  1.85%   ttr  8.2h
size   $2.50    wr   17%
resolves  14/04 12:00
```

**Commandes** : mix de HTML `<b>`, `<code>`, `<a>` — mais **pas de `<pre>`**
avec des liens (Telegram ne supporte pas bien cette combinaison).

### 7. Filtrage par stratégie

Pour éviter que SPEEDA / LONGSHOT / COLDMATH polluent le tracking CONVEX_YES,
ajouter une constante et filtrer partout :

```python
STRAT_TYPES = ("CONVEX_YES",)
STRAT_PH    = ",".join("?" * len(STRAT_TYPES))

# Dans chaque query SQL :
conn.execute(f"""
    SELECT ... FROM scalper_signals
    WHERE ... AND signal_type IN ({STRAT_PH})
""", (*params, *STRAT_TYPES))
```

### 8. Hardcoded values pour tracking live

Pour isoler le tracking v2a des valeurs de config générales :

```python
TRACK_FROM = 1776038400.0   # 2026-04-13 00:00 UTC — hardcoded, pas datetime()
BANKROLL   = 100.0           # base de tracking v2a, pas PM_BANKROLL=$10k
STRAT_TYPES = ("CONVEX_YES",)  # une seule stratégie suivie
```

**Pourquoi** : `datetime(2026, 4, 13).timestamp()` peut renvoyer le timestamp
2025 selon le contexte (bug trouvé). Et `PM_BANKROLL=10000` dans `.env` est
la bankroll du compte, pas celle du tracking v2a ($100 isolé).

## Leçons apprises

1. **Ne jamais mixer `<pre>` et `<a>` dans un message Telegram** — les liens
   ne sont pas rendus dans un bloc `<pre>`.
2. **Gamma API retourne `outcomePrices` comme string JSON** — toujours
   `json.loads(op)` avant d'indexer.
3. **Polymarket n'a pas d'URL market individuelle** — seulement des events
   qui regroupent plusieurs buckets. Stripper le suffixe bracket avec regex.
4. **Regex avec `\d+` sans limite match trop** — utiliser `\d{1,3}` pour
   éviter de matcher `-2026` (année).
5. **Pour des KPIs live mis à jour en place, stocker les valeurs en dataset**
   (`data-entry`, `data-size`) sur chaque `<tr>` pour recalculer sans refetch.
6. **Un notifier léger avec `urllib` + `<b>/<code>/<a>` HTML** est plus
   maintenable que `python-telegram-bot` pour du push simple.

## Related

- [[_system/MOC-patterns]]
- [[patterns/polymarket-convex-yes-v2-optimization]]
- [[patterns/polymarket-intraday-architecture]]
- [[founder/sessions/2026-04-13-polymarket-tracking-infra]]
