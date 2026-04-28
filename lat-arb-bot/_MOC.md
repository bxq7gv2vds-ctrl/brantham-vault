# LAT-ARB Bot v2 — MOC

> Bot d'arbitrage de latence sur Polymarket (BTC UP/DN, fenêtres 5 min)
> Repo : `~/vault/Downloads/lat_arb_bot/`

## Stack
- Python 3
- uvloop + orjson (Binance WebSocket)
- GARCH(1,1) pour σ live
- Rich (dashboard terminal)

## Architecture clé
1. `feed/btc_stream.py` — flux Binance bookTicker
2. `core/fair_value.py` — Brownian Bridge Φ(ret / σ√T)
3. `core/trader.py` — détection signal + entrée/sortie
4. `market/polymarket.py` — REST (Gamma/CLOB) + WS (prix temps réel)

## Contraintes design
- Ordres maker uniquement (taker fee trop élevé)
- Pas de stop-loss (contrats binaires, résolution 0/1)
- TP exige `ws_fresh=True` (jamais sur prix REST stale)

## Décisions
_Aucune décision enregistrée pour l'instant._

## Bugs résolus
_Aucun bug enregistré pour l'instant._

## Sessions
_Aucune session enregistrée pour l'instant._
## Related
## Related
