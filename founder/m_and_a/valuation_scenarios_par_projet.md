---
name: valuation-scenarios-par-projet
description: Matrice scénarios de valuation (low/mid/high) pour chaque projet — remplir avec chiffres réels
type: tool
date: 2026-06-13
---

# Valuation Scenarios — Par Projet

**Remplir les champs `[?]` avec vos métriques réelles, puis calcul auto de valuation**

---

## PROJET 1 : Alliance Coiffure (Next.js SaaS)

### Métriques à remplir :
- **ARR actuel :** `[? ex: $50k, $150k]`
- **MRR :** `[? ex: $5k]`
- **Growth rate :** `[? ex: 10% MoM, 5% MoM]`
- **Churn rate :** `[? ex: 2%, 5%]`
- **Nb clients :** `[? ex: 50, 150]`
- **Avg client value :** `[? ex: $1k/mois, $500/mois]`
- **Tech debt score :** `[LOW / MEDIUM / HIGH]`
- **Founder involvement :** `[FULL TIME / PART TIME / PASSIVE]`

### Valuation par scénario

| Scénario | Multiple | Calcul | Valuation |
|----------|----------|--------|-----------|
| **Conservative** (stagnant) | 2x ARR | `ARR × 2` | `[?]` |
| **Base** (10% growth persist) | 4x ARR | `ARR × 4` | `[?]` |
| **Aggressive** (acquire for growth) | 6-7x ARR | `ARR × 6.5` | `[?]` |

### Notes
- Tech debt = multiples baissent (-1x si HIGH)
- Churn >5% = discount (-0.5x)
- Founder full-time = premium (+1x pour continuity)

**Buyers probables :** `[Tuck-in SaaS? Strategic? Investor?]`

---

## PROJET 2 : LAT-ARB Bot (Python Trading)

### Métriques à remplir :
- **P&L annualisé (simulation) :** `[? ex: +56% YoY, +200% YoY]`
- **Capital requis minimum :** `[? ex: $100k]`
- **Consistency :** `[ex: Win Rate 65%, Sharpe 0.8]`
- **Latency improvement path :** `[CLEAR / UNCLEAR]`
- **Code maturity :** `[PROTOTYPE / MVP / PRODUCTION]`

### Valuation par scénario

| Scénario | Valorisation | Justification |
|----------|--------------|---------------|
| **Conservative** | `$50k–100k` | Proof-of-concept stage, unproven live track record |
| **Base** | `$200k–400k` | Solid backtests, 6+ months live data, repeatable edge |
| **Aggressive** | `$500k–1M` | Live P&L >$50k+, buyer sees platform/licensing upside |

### Notes
- Trading algos sans track record = très difficile à vendre (buyers veulent 12+ mois live)
- Acquéreur probable : Quant hedge fund, prop trader, fintech broker
- Deal structure : Earn-out obligatoire (80/20 cash/earnout)

**Buyers probables :** `[Hedge fund? Prop trading desk? Broker?]`

---

## PROJET 3 : [Autre projet ?]

### Métriques à remplir :
- **Revenu :** `[?]`
- **Traction :** `[?]`
- **Maturity :** `[?]`

### Valuation par scénario
| Scénario | Valuation |
|----------|-----------|
| Conservative | `[?]` |
| Base | `[?]` |
| Aggressive | `[?]` |

---

## Matrice synthèse — Tous projets

```
Projet                  Conservative    Base            Aggressive      Buyer fit
═══════════════════════════════════════════════════════════════════════════════════════
Alliance Coiffure       $100k–200k     $200k–400k     $400k–700k     Tuck-in SaaS
LAT-ARB Bot            $50k–100k      $200k–400k     $500k–1M       Quant/Fintech
[Projet 3]             [?]            [?]            [?]            [?]
```

---

## Règles de pouce pour multiples

| Type projet | Multiple type | Range |
|-------------|--------------|-------|
| SaaS B2B (stable, 10-30% growth) | ARR multiple | 3-5x |
| SaaS B2B (hyper growth 50%+) | ARR multiple | 6-10x |
| Algo/Trading (live P&L) | Annual P&L multiple | 3-5x |
| Marketplace / Platform | Revenue multiple | 2-3x (+ earnout) |
| API / Developer tool | ARR multiple | 2-4x |

---

## Scoring : "Vendre maintenant vs attendre ?"

Pour chaque projet, score de 1-10 :

- **Readiness (0-3)** : Code quality, financials clean, no big tech debt?
- **Buyer fit (0-3)** : Acquéreur cible intéressé? Strategic synergy?
- **Market (0-2)** : Cycle M&A chaud dans ton secteur?
- **Capital need (0-2)** : Besoin urgently? (OUI = score +2)

**Total:** Seuil vendre maintenant = **7+**

Exemple : Alliance Coiffure = Readiness 2 + Buyer fit 3 + Market 1 + Capital 1 = **7** → envisageable

