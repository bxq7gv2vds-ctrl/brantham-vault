---
name: BeSoft Initial State T0
description: Exact starting state of the company before T1 — all values from BeSoft parameters and screenshots. Source of truth for the business game briefing.
type: reference
---

# BeSoft — Etat initial T0

Toutes les equipes partent avec exactement la meme entreprise.

## Tresorerie & bilan

| Poste | Valeur | Notes |
|-------|--------|-------|
| Cash | 67,666 EUR | Faible — risque decouvert T1 |
| Creances clients | 483,840 EUR | Encaissees en T1 |
| Stock MP | 6,200 u a 35.65 EUR/u = 221,001 EUR | |
| Stock PF ATOM | 2,898 u a 135.94 EUR/u = 393,947 EUR | |
| Dettes fournisseurs | 356,454 EUR | A payer en T1 |
| Hypotheque | 216,000 EUR | 9,000 EUR/trim, 1.25%/trim |
| Capital | 1,080,000 EUR | |
| Reserves | 245,296 EUR | |
| Total actif | 1,922,454 EUR | |
| Total equity | 1,325,296 EUR | |

## Equipement

| Element | Quantite | Capacite | Depreciation |
|---------|----------|----------|--------------|
| Machine D | 1 | 7,200 u/trim (fixe) | 108K/40 trim |
| Machines F anciennes | 4 | 750 u/machine T1-T4, 720 T5-T8, 685 T9-T12 | 54K chacune/40 trim |
| Machine F neuve (achat) | 0 | 900 u, degrade -5u/trim | 77,760 EUR, 40 trim |
| Capacite totale T1 | | 3,000 u/trim | |

## Personnel

| Poste | Nb | Salaire/trim | Notes |
|-------|-----|-------------|-------|
| Ouvriers | 20 | 7,488 (T1-T4), 7,862 (T5-T8), 8,237 (T9-T12) | Anciennete 5 ans |
| Contremaitre | 1 | 9,446 | Max 32 ouvriers |
| Dir. technique | 1 | 18,900 | |
| Dir. admin | 1 | 18,900 | |
| Secretaire | 1 | 6,754 | |
| Vendeurs | 2 | 10,800 (+500/trim) | Quota 750, comm 4.32 EUR/u |
| Frais divers | | 1,346/trim | |

Conge: 1.5 mois salaire x annees anciennete (ouvriers: 5 ans)

## Couts

| Type | Montant | Notes |
|------|---------|-------|
| Couts fixes/trim | ~217,000 EUR | Salaires + admin + hypotheque |
| Cout variable/unite | ~72.4 EUR | MP (71.30) + maintenance (1.08) |
| Cout unitaire a 3,000 u | ~144 EUR | Fixe: 72 + variable: 72 |
| Cout unitaire a 2,000 u | ~180 EUR | Fixe: 108 + variable: 72 |

## Matieres premieres

| Prix | Valeur | Notes |
|------|--------|-------|
| Base contrat | 37.80 EUR/u | Min 2,000/livraison |
| Spot (urgence) | 54.00 EUR/u | +43% vs contrat |
| Optimal (6K x 4 livr.) | 32.96 EUR/u | Remise 12.8% |

### Table de remises
| Qty/livraison | 1 livr. | 2 livr. | 4 livr. |
|--------------|---------|---------|---------|
| 2,000-6,999 | 0% | 9.3% | 12.8% |
| 7,000-9,999 | 3.5% | 9.3% | 12.8% |
| 10,000-14,999 | 5.7% | 10.0% | 14.3% |
| 15,000+ | 8.6% | 11.4% | 15.7% |

## Taux d'interet

| Type | Taux | Duree |
|------|------|-------|
| Hypotheque | 1.25%/trim | 24 trim restants |
| MLT | base + 1% = 3% | 6 trimestres |
| CT | base + 3% = 5% | 1 trimestre |
| Decouvert | base x 4 = 8% | Automatique |
| Base rate | 2.0%/trim | Variable par le jeu |

## Fiscalite
- IS: 25% sur EBT
- Depreciation batiment: 432K / 160 trim = 2,700 EUR/trim
- Depreciation machines: 324K / 40 trim = 8,100 EUR/trim

## Storage costs
```
1,000 + 1% * (0-180K) + 2% * (180K-540K) + 4% * (>540K)
```

## Saisonnalite
| Q1 (T1,T5,T9) | Q2 (T2,T6,T10) | Q3 (T3,T7,T11) | Q4 (T4,T8,T12) |
|----------------|-----------------|-----------------|-----------------|
| 107 | 108 | 101 | 84 |

Q4 = -19% de demande. Adapter les prix.

## Production
- Heures/trim: 520 (8h/jour x 65 jours)
- Overtime equipe 1: max +20%, taux 1.5x
- Overtime equipe 2: max +5%, taux 1.5x
- Ouvriers/machine D: 8
- Ouvriers/machine F: 3
- MP par ATOM: 2 unites
- MP par BOLT: 2 unites

## Alerte T1
Sans emprunt MLT, l'entreprise tombe en decouvert (8% vs MLT 3%).
Emprunt recommande: 80,000-120,000 EUR.
