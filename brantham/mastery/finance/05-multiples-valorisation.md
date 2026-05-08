---
type: fiche-mastery
module: finance
ordre: 5
project: brantham
date: 2026-05-08
---

# Finance #5 — Multiples valorisation FR & décotes distressed

## Définition rapide
La méthode des **multiples** valorise une entreprise en appliquant un multiple sectoriel à un agrégat (EBITDA, CA, EBIT) issu de transactions comparables.

## Formule de base

```
Valeur d'entreprise (EV) = EBITDA × Multiple sectoriel

Valeur des fonds propres = EV - Dette nette + Cash + Actifs hors exploitation
```

## Multiples PME France 2025 — par secteur

| Secteur | Multiple EBITDA médian (PME saine) |
|---------|-----------------------------------|
| **Tech / SaaS** | 7-12x (jusqu'à 15x si ARR fort) |
| **Health / Services santé** | 7-9x |
| **Conseil / Audit / Comptabilité** | 5-7x |
| **Industrie spécialisée** | 5-7x |
| **Commerce de détail spécialisé** | 4-6x |
| **Industrie manufacturière classique** | 4-5x |
| **Distribution / wholesale** | 4-5x |
| **Logistique / transport** | 4-5x |
| **Restauration** | 3-5x |
| **BTP / construction** | 3-4x |
| **Automobile / réparation** | 3-4x |

**Multiple PME médian France 2024** : ~5,3x EBITDA toutes tailles confondues.
**Q1 2025** : index en légère baisse à ~9,5x (tendance générale, multi-tailles).

## Décotes structurelles à appliquer

| Décote | Impact |
|--------|--------|
| **Distressed (procédure)** | **-30 à -50 %** |
| Dépendance dirigeant fort | -20 à -40 % |
| Concentration client (top 5 > 70 %) | -15 à -30 % |
| Petite taille (CA < 2 M€) | -10 à -25 % |
| Marché en déclin | -15 à -30 % |
| Pas de système de gestion (ERP, CRM) | -10 à -15 % |
| Gouvernance familiale non structurée | -10 à -20 % |
| Manque de préparation à la cession | -10 à -30 % |

→ Les décotes se **cumulent** (souvent 40-60 % total en distressed).

## Méthode des multiples — pas à pas

### Étape 1 — Calculer EBITDA normalisé
Voir [[brantham/mastery/finance/04-ebitda-normalise]]

### Étape 2 — Identifier multiple sectoriel cible
Sources :
- **Argos Mid-Market Index** (trimestriel, mid-cap européens)
- **EpsilonResearch** (transactions PME France)
- **Indices Pappers** (transactions BODACC)
- **Études sectorielles** (CCI, fédérations)
- **Cabinets M&A** : Argos Wityu, Capital Mind, In Extenso, BM&A

### Étape 3 — Appliquer décotes
```
Multiple ajusté = Multiple sectoriel × (1 - décote distressed) × (1 - autres décotes)
```

### Étape 4 — Calculer EV puis Equity value
```
EV = EBITDA normalisé × Multiple ajusté
Equity Value = EV - Dette nette à reprendre + Actifs hors exploitation
```

**En plan de cession** : la dette ne suit pas, donc Equity Value ≈ EV.

## Cas pratique chiffré

```
PME industrielle métallurgie, CA 6 M€, en RJ
EBITDA reporté : 150 k€
EBITDA normalisé : 400 k€ (après retraitement rémunération + loyer + procédure)

Multiple sectoriel "industrie manufacturière classique" : 4,5x médian

Décotes :
- Distressed : -40 %
- Petite taille (CA < 2 M€) : non applicable (CA 6 M€)
- Concentration client (top 3 = 60 %) : -20 %
- Manque de préparation (procédure) : -10 %
─────
Multiple ajusté = 4,5 × (1-0,40) × (1-0,20) × (1-0,10)
                = 4,5 × 0,60 × 0,80 × 0,90
                = 1,94x

EV = 400 k€ × 1,94 = 776 k€
Dette reprise (plan de cession) : ~0
─────
Prix d'offre cible : ~750-800 k€
```

→ Soit ~13 % du CA — cohérent avec les standards distressed (5-15 % CA).

## Méthodes alternatives — à connaître

### Méthode patrimoniale (actif net réévalué)
Pertinente quand :
- L'entreprise a beaucoup d'**actifs identifiables** (immobilier, machines, marques)
- L'EBITDA est négatif
- Le repreneur valorise principalement les actifs

```
Actif Net Réévalué = Σ Valeur de marché des actifs - Σ Dettes
```

→ En distressed, cette méthode peut **diverger fortement** des multiples. À utiliser comme **borne basse**.

### DCF (Discounted Cash Flow)
- Pertinente si on a un **business plan crédible** post-reprise
- Taux d'actualisation très élevé en distressed (15-25 % WACC ajusté)
- À utiliser comme **complément**, pas méthode primaire en distressed

### Méthode des comparables boursiers
- Pour les grandes capitalisations
- En PME : peu utile direct, sert à **trianguler** les multiples sectoriels

## Triangulation des méthodes

```
Méthode             Résultat (k€)
─────────           ─────────────
Multiples           750-800
Patrimoniale        500-700  (selon réévaluation actifs)
DCF (BP repreneur)  900-1100 (optimiste)
─────
RANGE INDICATIF     500-1100
PRIX OFFRE CIBLE    700-850   (médiane prudente)
```

## Le "fair price" pour le tribunal

Le tribunal n'est pas tenu de retenir l'offre la plus chère (L642-5 : emploi prime). Mais :
- Une offre à **5 % du CA** sur un dossier viable = sera vue comme **insuffisante** vs créanciers
- Une offre **trop basse** sera attaquée par MJ, procureur, créanciers
- Sweet spot pratique : **8-15 % du CA** pour une cible viable

## Multiples par taille (effet taille)

| Taille (CA) | Décote vs grand groupe |
|-------------|------------------------|
| > 50 M€ | Référence |
| 20-50 M€ | -10 à -15 % |
| 5-20 M€ | -20 à -30 % |
| 1-5 M€ | -30 à -40 % |
| < 1 M€ | -40 à -50 % |

→ Les TPE valorisent moins haut parce que **risque idiosyncratique** plus fort.

## Question piège

> "Comment vous calculez votre prix d'offre ?"

**Réponse modèle (75 sec)** :
> "On utilise systématiquement la méthode des multiples sectoriels, retraitée. Le point de départ, c'est l'**EBITDA normalisé** — donc l'EBITDA reporté retraité de toutes les charges non récurrentes liées à la procédure et de l'éventuelle sur-rémunération du dirigeant ou des loyers familiaux. Sur cet EBITDA normalisé, on applique un **multiple sectoriel médian** — par exemple 4 à 5 fois pour une industrie manufacturière classique, 5 à 7 fois pour de l'industrie spécialisée, 3 à 5 fois pour de la distribution. À ce multiple, on applique trois familles de décotes. **Une décote distressed** de 30 à 50 % parce que l'entreprise est en procédure. **Des décotes structurelles** : concentration client, dépendance dirigeant, taille, qualité du système de gestion. **Des décotes de marché** : déclin sectoriel ou pression concurrentielle. Au final, le multiple effectif est souvent **2 à 3 fois moins élevé** que le multiple sectoriel saine. Pour fixer le prix final, on triangule avec la valeur patrimoniale — donc l'actif net réévalué — et on cale le prix dans un range qui doit rester crédible pour le tribunal : typiquement 8 à 15 % du chiffre d'affaires sur une cible viable."

## À retenir absolument
- Multiple PME médian FR 2024 : ~5,3x EBITDA
- Tech 7-12x, Industrie 4-5x, BTP 3-4x, Restau 3-5x
- Décote distressed : -30 à -50 %
- Décotes additionnelles : concentration, taille, marché
- Multiple ajusté final souvent 2-3x EBITDA en distressed
- Prix indicatif distressed : 5-15 % du CA
- Trianguler 3 méthodes : multiples, patrimoniale, DCF

## Related
- [[brantham/mastery/finance/_MOC]]
- [[brantham/mastery/finance/04-ebitda-normalise]]
- [[brantham/knowledge/finance/valorisation-distressed]]
- [[brantham/knowledge/finance/financial-modeling-distressed]]
