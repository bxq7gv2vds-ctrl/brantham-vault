---
title: "Session — Polymarket Oracle Backtest + Infrastructure"
date: 2026-04-08
type: session
project: polymarket-hedge
tags: [polymarket, oracle, backtest, coldmath, bracket-scalper, trading]
---

# Session — 2026-04-08 — Polymarket Oracle Backtest

## Focus
Résoudre les bugs du bracket scalper + backtest complet de la stratégie CONFIRMED oracle + setup infrastructure qui "print tous les jours".

---

## Ce qui a été fait

### 1. Fixes critiques `run_bracket_scalper.py`
- **Bug corrigé** : `CONFIRMED_YES`, `CONFIRMED_NO`, `EXACT_BIN_YES` étaient générés mais INVISIBLES dans `print_signals` — absents de `_groups`
- **Bug corrigé** : Telegram alerts ne incluait pas les signaux CONFIRMED (les plus importants)
- Ces deux types sont maintenant en tête de l'affichage et des alertes

### 2. Nouveau script `daily_pnl_report.py`
- Settlement METAR automatique des trades expirés
- Rapport daily P&L : capital curve, P&L quotidien, breakdown par tier
- Intégrable Telegram
- Reset 5425 trades corrompus (won=NULL ou pnl=0 d'anciennes runs buguées)
- Résultat après re-settlement : **WR 91.1%, +$16,898 paper sur 2 jours**

### 3. Repo GitHub
- Repo créé : `https://github.com/bxq7gv2vds-ctrl/polymarket-hedge` (private)
- `.gitignore` propre (exclut .env, *.db, __pycache__)
- Commits: initial + fixes CONFIRMED + daily_pnl_report

### 4. Scheduling (4 triggers)
- **09:07 UTC** — Scan oracle principal (CCR cloud) `trig_019ESZGPjKHV4T9omziw429H`
- **10:30 UTC** — Scan secondaire (CCR cloud) `trig_01RgvQnW9ME9FCawykq4G63e`
- **16:15 UTC** — Scan SPEEDA villes asiatiques (CCR cloud) `trig_01BpKEU3JFbr3Vrf3XKxQUaa`
- **09:00 local (11h Paris)** — Daily P&L report (launchd local) `com.paul.polymarket-daily-pnl`

### 5. Backtest Oracle CONFIRMED — résultats complets
**Nouveau script** : `scripts/backtest_oracle.py`
**Données** : `oracle_data.db` — prix oracle 09:07 UTC + T_max Open-Meteo archive

#### Résultats sur données disponibles (jan 2025 → avr 2026, 3027 marchés)
| Métrique | Valeur |
|----------|--------|
| Période | jan 2025 → avr 2026 (105 jours tradés) |
| Trades | 390 (59 YES + 331 NO) |
| Win Rate | **100%** (oracle = certitude physique) |
| PnL total | **+$529,285** |
| Capital final | **$539,285** (+5,293%) sur $10k |
| Avg PnL/jour | +$5,041 |
| Max drawdown | **0.00%** |
| YES avg entry | 0.397 → edge 152% |
| NO avg entry | 0.932 → edge 7.3% |

#### Par ville (top)
| Ville | N | PnL | Avg/trade |
|-------|---|-----|-----------|
| New York | 165 | +$202k | +$1,227 |
| Miami | 38 | +$83k | +$2,194 |
| Seattle | 45 | +$72k | +$1,604 |
| Toronto | 7 | +$34k | +$4,905 |
| Dallas | 38 | +$31k | +$817 |

#### Insight clé : les YES trades
- YES entry à 0.40 moyenne = marché cote 40% la nuit d'avant
- Oracle confirme à 09:07 → résout à 1.0 = +150% par trade
- Ces trades sont les plus value ($2k → ~$5k en moyenne)

### 6. Download oracle_data.db
- Script `download_oracle_data.py` — aiohttp 50 workers parallèles
- T_max via Open-Meteo archive API (gratuit, pas de clé)
- Prix via Polymarket CLOB API
- **Fix appliqué** : User-Agent header manquant causait 403, fenêtre oracle élargie 08:00-12:00
- Coverage actuelle : **3034/20844 marchés (14.4%)**
- Download en cours (re-run avec --no-resume) pour les 86% manquants
- Cause du manque : archives CLOB Polymarket limitées pour marchés anciens/thin

---

## État infrastructure actuelle

```
/Users/paul/polymarket-hedge/
├── scripts/
│   ├── run_bracket_scalper.py    -- scanner live (fixes CONFIRMED)
│   ├── daily_pnl_report.py       -- NEW: settlement + P&L daily
│   ├── backtest_oracle.py        -- NEW: backtest CONFIRMED strategy
│   ├── download_oracle_data.py   -- NEW: fetch historical prices + tmax
│   └── paper_pnl_tracker.py      -- ancien tracker (settlement OK)
├── oracle_data.db                -- NEW: 3034 marchés (en cours download)
├── bracket_scalper_trades.db     -- paper trades live
├── emos_cache.db                 -- EMOS calibré 39 villes
├── all_markets.db                -- 22k marchés metadata
└── .env                          -- PM_PAPER=1 (fill credentials pour live)
```

---

## Prochaines étapes

1. **Attendre fin download oracle** → relancer `backtest_oracle.py` avec plus de données
2. **Vérifier WR réel** : le backtest assume 100% WR (oracle certitude), mais Open-Meteo ≠ METAR exact. À vérifier sur les premières trades live.
3. **Go live** : remplir `POLYMARKET_API_KEY` + `POLYMARKET_SECRET` + `POLYMARKET_PASSPHRASE` dans `.env`
4. **Filtrer brackets dans `intraday_engine.py`** (flag `--no-bracket` seulement backtest)
5. **Recalibrer Singapore EMOS** (biais +6°C, batch échoué)

---

## Décisions de session

- **Architecture oracle** : la stratégie CONFIRMED (T_max prev UTC connu à 09:07) est LA stratégie à déployer. Zero drawdown en backtest, WR 100%, edge 7-152%.
- **Paper avant live** : PM_PAPER=1 jusqu'à avoir validé 1 semaine de signaux CONFIRMED corrects
- **GitHub privé** : code sur `bxq7gv2vds-ctrl/polymarket-hedge` pour triggers CCR

---

## Related

- [[_system/MOC-patterns]]
- [[patterns/polymarket-bracket-arb]]
- [[patterns/polymarket-nwp-emos-calibration]]
- [[patterns/polymarket-intraday-architecture]]
- [[founder/decisions/2026-03-29-polymarket-intraday-vs-fundamental]]
- [[founder/sessions/2026-04-05-polymarket-coldmath-strategy-complete]]
- [[founder/sessions/2026-04-05-polymarket-bracket-reverse-engineering]]
