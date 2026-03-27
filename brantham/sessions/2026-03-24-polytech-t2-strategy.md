---
name: Session T2 Strategy 24 Mars 2026
description: T1 real results analysis, T2 decision optimization, Scenario 4 machine strategy, BOLT analysis
type: session
---

# Session 24 Mars 2026 — T2 Strategy & Machine Analysis

## T1 Real Results (joue 24/03 matin)

### P&L
- CA: 614,819 (3,664 u @ 167.80)
- COGS: 492,041
- Marge brute: 122,778
- Frais vente: 45,128 (salaires 21,600 + comm 9,348 + travel 10,080 + pub 4,100)
- Frais generaux: 27,000
- EBIT: 50,650
- Frais financiers: 2,700
- NI: **35,962** (avg industrie: 32,642 = +10%)

### Concurrence T1 Real
| Firme | CA | Prix ATOM |
|-------|-----|----------|
| F1 | 585,140 | 170.00 |
| **F2 (nous)** | **614,819** | **167.80** |
| F3 | 564,332 | 172.00 |
| F4 | 615,888 | 168.00 |
| F5 | 640,341 | 169.00 |

### Tresorerie
- Encaissements: 568,840 (creances 483,840 + CT 85,000)
- Decaissements: 633,616
- Cash fin: **2,889** (positif, zero decouvert)
- CT 85K au lieu de MLT 120K = decision optimale (3,613 total interet vs 12,152)

### Bilan
- Creances: 614,819
- Disponibilites: 2,889
- Autres Emprunts: 85,000 (CT, rembourse T2)
- Hypothecaire: 207,000

## Precision modele
- Demande predite: ~3,665 u
- Reel: 3,664 u
- **Erreur: <0.1%**

## Documents T2
- **Journal**: Croissance 7% PNB mais ralentissement prevu H2 (T3-T4)
- **Etude BOLT**: 28% favorables, 46% sceptiques. Demande BOLT/ATOM: ~4% en P1 post-launch, monte lentement
- **Annonce BOLT**: licence 18K, machines F only, priorite ATOM, prix suggere 202+

## Analyse BOLT — NE PAS LANCER EN T2

### Historique Paul P2 (6 firmes)
- F1 (gagnant): PAS de BOLT, prix 164, NI **43,877** (meilleur)
- BOLT total: 988 u sur 5 firmes = ~200/firme
- Firmes avec BOLT: NI moyen ~30-35K

### Historique Leo P2 (5 firmes)
- F4 (Leo): effort BOLT 0.05, produit 500, **vendu 55** → 445 stock mort
- NI: 40,760

### Conclusion: BOLT est un piege en T2. Lancer en T3 (comme le gagnant historique).

## Analyse Machine — Scenario 4 retenu

### Scenarios compares
| Scenario | Total vendu T1-T7 | Perdu | NI cumule | Risque |
|----------|------------------|-------|-----------|--------|
| 0 machine | 23,658 | 3,156 | ~197K | DESASTRE T5-T7 |
| 1 machine T3 | 26,518 | 296 | ~256K | Rupture T7 |
| 1 machine T2 | 26,814 | 0 | ~264K | Tendu T6-T7 |
| **1 T2 + 1 T4** | **26,814** | **0** | **~271K** | **ZERO** |

### Capacites Scenario 4
| Trim | Machines | Capacite |
|------|---------|----------|
| T1 | 4F (750) | 3,000 |
| T2 | 4F + 1 new (900) | 3,900 |
| T3 | 5F | 3,900 |
| T4 | 5F + 1 new (900) | 4,800 |
| T5 | 4F@730 + 1@900 + 1@900 | 4,720 |
| T6 | 4@730 + 1@880 + 1@900 | 4,700 |
| T7 | 4@730 + 1@880 + 1@900 | 4,700 |

## Decision T2 (a jouer)

| Champ | Valeur |
|-------|--------|
| Effort BOLT | 0.00 |
| Prix ATOM | 167 |
| Prix BOLT | 0 |
| Vendeurs | 2 |
| Salaire | 11,300 |
| Quota | 750 |
| Commission | 4.32 |
| Travel | 5,040 |
| Pub | 4,500 |
| Production ATOM | 3,900 |
| Production BOLT | 0 |
| Machines F actives | 5 |
| Taux utilisation | 1.00 |
| Commande MP | 0 (contrat) |
| Machines achetees | 1 |
| Machines vendues | 0 |
| Emprunt CT | 0 |
| Emprunt MLT | 100,000 |

## Webapp updates
- SCENARIOS T1-T7 mis a jour pour Scenario 4
- DEFAULT_PARAMS = T2 (decision active)
- Capacites stock-projection: [3000, 3900, 3900, 4800, 4720, 4700, 4700]
- Scenario cards: affichent production, machines, BOLT info
- T3 annonces: storage costs T3+ (1000 + 1%/2%/4% tiers), journal ralentissement

## Related
- [[brantham/_MOC]]
