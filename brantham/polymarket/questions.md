---
name: Questions critiques Polymarket Hedge Fund
description: 40+ questions que je me pose systématiquement pour ne rien oublier (business, market, data, model, risk, execution, backtest)
type: framework
created: 2026-04-17
tags: [polymarket, questions, framework]
---

# Questions Critiques — Framework Hedge Fund

Framework systématique pour ne rien oublier. À revisiter à chaque itération majeure.

## BUSINESS

1. **Capital réel disponible ?** ⏳ À confirmer ($500-$2k phase 1)
2. **Objectif P&L annuel concret ?** $200-400k visé
3. **Tolérance max drawdown ?** À définir (cap kill switch à 10% daily, 20% total)
4. **Jurisdiction légale ?** Polymarket bloqué US, OK EU avec compliance
5. **Time to monitor ?** Auto 24/7, check 2x/jour
6. **Horizon ?** Multi-mois, potentiel scale multi-année
7. **Re-invest ou sortir ?** Re-invest jusqu'à $50k, puis sortie partielle
8. **Infra budget ?** VPS ~$20-100/mois, tout data gratuit, total <$150/mois
9. **Compte Polymarket existant ?** ⏳ À confirmer (private key nécessaire)

## POLYMARKET (règles critiques)

10. Fees : **0% maker, 0% taker** depuis v2 — ✅ pas de friction
11. Position limits : ~$50k/wallet sur weather — OK pour small start
12. Spread typique : **2-5c** sur bins liquides
13. Settlement source : UMA oracle + WUnderground pour weather
14. **Dispute window : 48h** — risque rare mais destructive
15. Matching : CLOB sur Polygon Matic, gas minimal
16. Oracle resolver : WUnderground → ICAO stations spécifiques
17. Unit : °F pour US cities, °C pour ailleurs (attention conversion)
18. Tie-breaker : si exactly boundary, "above" wins (convention)
19. Time window : D+0 = same calendar day LOCAL time
20. Resolution time : typically 00:00 UTC next day

## DATA (couverture)

21. **USA best NWP** : HRRR 3km (NOMADS + Open-Meteo)
22. **Europe best NWP** : ECMWF 9km + AROME 1.3km + ICON-EU 6.5km
23. **Asie best NWP** : ECMWF + JMA MSM 5km
24. **Ensemble** : GEFS 31 membres + ECMWF ENS 51 (Copernicus CDS)
25. **Obs** : METAR + Mesonet (US) + OGIMET (historical)
26. **Radar** : NEXRAD/MRMS (US via AWS), OPERA (EU)
27. **Satellite** : GOES (US via AWS), Meteosat (EU), Himawari (Asia)
28. **Reanalysis training** : ERA5 (Copernicus) 5 ans
29. **Polymarket** : CLOB WebSocket + REST (API key needed)
30. **Coût total data** : $0 (tout gratuit)

## MODÈLE (ML stack)

31. **EMOS** : baseline robuste, calibrer par station × mois
32. **BMA** : weights Bayésiens entre NWP sources, update online
33. **XGBoost post-proc** : features riches (NWP + obs + radar + climato)
34. **DRN** (Rasp & Lerch 2018) : neural dist regression — SOTA
35. **ANET/D-TGN** : transformer ensemble — SOTA 2024
36. **GraphCast/Pangu/AIFS** : overkill (on n'a pas besoin gridded)
37. **Analog regression** : k-NN pour events rares (heat wave, cold snap)
38. **Kalman online** : update intra-day bias station
39. **Training data** : ERA5 5 ans + METAR history + NWP archive
40. **Retraining** : monthly per station

## EDGES (lesquels prioriser)

41. **Model vs market** (core) — 3-7% edge durable
42. **Sum-to-1 arb** (math) — near-zero risk mais fill leg risk
43. **CONFIRMED oracle** — ~100% WR quand triggered, rare
44. **Orderbook imbalance** — latency edge
45. **Cross-market pairs** — diversification
46. **Nowcast 0-6h** — valeur proche expiry

## RISK (qu'est-ce qui peut tuer ?)

47. **Fat finger** (size 100x intended) → unit tests sizing obligatoires
48. **Model drift** (edge disparaît) → realtime WR monitoring + kill switch
49. **Oracle dispute** (trade resolves wrong) → diversification markets
50. **Flash crash** (liquidity evaporates) → inventory caps
51. **RPC/API down** → multi-RPC fallback (Infura + Alchemy + own)
52. **Concentration** (single market blow-up) → per-market caps
53. **Correlation** (10 corr positions = 1 real position) → corr-adj Kelly
54. **Regime change** → regime detection + pause option
55. **Fat finger 2** : CANCEL orders mal formattés → confirmations
56. **Legal** → jurisdiction awareness permanente

## EXECUTION

57. **Latency requirement ?** <500ms pour competitive
58. **WebSocket ou polling ?** WebSocket CLOB obligatoire pour speed
59. **Maker vs taker ?** Maker preference → capture spread
60. **Retry logic ?** Exponential backoff + max 3 retries
61. **Cancel-replace ?** Si prix drift >2c du signal, cancel + replace
62. **Order size limits ?** Match orderbook depth (slippage model)
63. **Fill monitoring ?** Log fill price + slippage auto-calibration
64. **Multi-RPC ?** Primary + backup obligatoire
65. **Monitoring ?** Grafana + Prometheus + Telegram
66. **Health check ?** Every 30s, failover si 3 échecs

## BACKTEST (validation)

67. **In-sample vs OOS ?** Walk-forward obligatoire, jamais pure in-sample
68. **Purged K-fold ?** Éviter label leakage temporel (Lopez de Prado)
69. **Paper shadow ?** 30 jours minimum avant real money
70. **Slippage model ?** Calibré sur orderbook historique
71. **Regime stratification ?** Perfs par mois/saison/heure/ville
72. **Monte Carlo ?** Bootstrap 1000 sims pour CI sur annual PnL
73. **Parameter sensitivity ?** Test robustness ±20%
74. **Hold-out final ?** Last 20% jamais touché jusqu'au deploy
75. **Attribution ?** Per-alpha, per-city, per-hour breakdown
76. **Tail analysis ?** Worst case week, worst trade, fat tails

## OPERATIONAL

77. **Monitoring fréquence ?** Real-time pour trading, daily pour review
78. **Reporting ?** Daily auto-report vers vault
79. **Logging ?** Toutes signaux + trades + slippage + rejects
80. **Backup ?** DB daily backup + cloud offsite
81. **Model versioning ?** Git tag chaque release + changelog
82. **A/B testing ?** Shadow mode new models avant replace
83. **Retraining automation ?** Cron monthly + eval gates
84. **Alerts priorities ?** Critical > Telegram + email, Info > Telegram only

## SYSTÈME

85. **Code parity research-prod ?** Même signal generator pour backtest et live
86. **Module decoupling ?** Chaque alpha indépendant, testable isolé
87. **Configuration ?** YAML externalisé, pas hardcoded
88. **Dependencies ?** Minimal (pandas + numpy + xgboost + aiohttp)
89. **Python version ?** 3.13
90. **Package manager ?** uv
91. **Dev environment ?** macOS M5 local + VPS remote parity
92. **CI/CD ?** Pour plus tard, pas phase 1
93. **Documentation ?** Vault markdown + docstrings inline

## Questions résiduelles ⏳ (besoin input utilisateur)

- Capital exact phase 1 ?
- Private key Polymarket existante ou à créer ?
- Jurisdiction (France OK) ?
- VPS existant ou à provisioner ?
- Time zone pour cron jobs ?
- Tolérance drawdown exacte (%) ?
- Notification préférences (Telegram OK) ?
- Budget dev time par jour ?

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture]]
- [[roadmap|Roadmap]]
- [[risk-management|Risk management détaillé]]
