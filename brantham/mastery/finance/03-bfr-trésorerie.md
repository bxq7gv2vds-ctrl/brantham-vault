---
type: fiche-mastery
module: finance
ordre: 3
project: brantham
date: 2026-05-08
---

# Finance #3 — BFR, trésorerie, 13-week cash flow

## Définition rapide
Le **BFR** (Besoin en Fonds de Roulement) est le **besoin permanent de cash** pour faire tourner l'exploitation. Il vient du décalage entre encaissements (clients) et décaissements (fournisseurs, salaires).

## Formule

```
BFR = (Stocks + Créances clients) - (Dettes fournisseurs + Dettes fiscales/sociales)
```

ou en jours de CA :
```
BFR en jours = BFR / CA × 365
```

## Le triangle infernal du BFR

```
       STOCKS
    ↗         ↘
   /           \
  /             \
CRÉANCES ── DETTES FOURN.
CLIENTS

Si stocks ↑ : BFR ↑ (cash bloqué dans inventaire)
Si DSO ↑ : BFR ↑ (clients paient en retard)
Si DPO ↑ : BFR ↓ MAIS signal de tension (on tient les fournisseurs)
```

## Cycle d'exploitation et trésorerie

### Schéma classique entreprise industrielle

```
J0    J+30      J+90       J+120         J+180         J+270
─    ────      ────       ─────         ─────         ─────

Achat   Stock        Production          Vente           Encaissement
matière temporaire   transformation      à crédit        client
        30j          stocké 90j          90j paiement    
                                                          
        ◄─────── 270 jours d'argent immobilisé ────────►
```

→ Si l'entreprise paie ses fournisseurs à 30 jours et est payée par ses clients à 60 jours, elle a 240 jours de besoin de cash.

## Les ratios à connaître par cœur

### DSO — Days Sales Outstanding

```
DSO = Créances clients / CA × 365
```

| DSO | Signal |
|-----|--------|
| 30-45 j | Normal commerce/industrie B2C |
| 45-60 j | Normal industrie B2B |
| 60-90 j | Normal services/conseil grand compte |
| **> 90 j** | **Tension cash, clients qui paient mal** |
| **> 120 j** | **Crise, litiges fréquents** |

### DPO — Days Payable Outstanding

```
DPO = Dettes fournisseurs / Achats × 365
```

| DPO | Signal |
|-----|--------|
| 30-60 j | Normal |
| 60-90 j | Tension contrôlée |
| **> 90 j** | **L'entreprise paie en retard** |
| **> 120 j** | **Tension critique, risque de rupture livraisons** |
| **> 150 j** | **Procédure imminente** |

### DIO — Days Inventory Outstanding

```
DIO = Stocks / (Achats / 365)
```

| DIO | Signal |
|-----|--------|
| < 60 j | Bonne rotation |
| 60-120 j | Normal selon secteur |
| **> 120 j** | **Stocks dormants, à déprécier** |

### Cash conversion cycle (CCC)

```
CCC = DSO + DIO - DPO
```

→ Le CCC mesure le **temps en jours pendant lequel l'entreprise immobilise du cash**.

| CCC | Signal |
|-----|--------|
| < 30 j | Excellent (négatif possible : Amazon, Apple) |
| 30-60 j | Acceptable |
| 60-120 j | Tendu |
| **> 120 j** | **Crise de cash, BFR insoutenable** |

## L'explosion du BFR — pattern type distressed

```
N-3 : BFR =  60 jours CA
N-2 : BFR =  75 jours CA  ← début de tension
N-1 : BFR =  95 jours CA  ← rouge
N   : BFR = 130 jours CA  ← procédure imminente
```

**Causes typiques d'explosion BFR** :
1. **Clients en retard** (DSO ↑) — souvent perte de pricing power
2. **Stocks qui s'accumulent** (DIO ↑) — invendus, surproduction
3. **Fournisseurs qui resserrent** (DPO ↓) — confiance perdue
4. **Combinaison des trois** = mort certaine

## Le 13-week cash flow forecast (13WCF)

### Pourquoi 13 semaines
- Un trimestre = 13 semaines
- Suffisamment court pour être réaliste, suffisamment long pour anticiper
- En distressed, c'est **L'OUTIL CENTRAL** de pilotage

### Ce qu'on suit chaque semaine

```
                     S+1    S+2    S+3    ... S+13   TOTAL
─────────────────    ───    ───    ───    ─── ────   ─────
Solde ouverture     100    
+ Encaissements      
  Clients factures  +50    +60    +40    +30        +X
  Autres recettes   +5     +0     +0     +0
─────────────────
- Décaissements
  Salaires nets    -30     0     -30     0
  Charges sociales  0     -25     0     -25
  Fournisseurs    -40    -45    -35    -40
  TVA, IS          0      0     -20     0
  Loyers, énergie -8      0     -8      0
  Banque (intérêts)-5      0     -5      0
  Autres          -2     -3     -2     -2
─────────────────
= SOLDE FIN SEM    +70   +57    -3    -67          ← !! ROUGE
```

### Ce que ça permet de voir
1. **Date exacte de la cessation des paiements** anticipée (semaine X)
2. **Pic de tension** (souvent vers semaine 5-8)
3. **Sensibilités** : que se passe-t-il si un client clé paie en retard ?
4. **Levier de redressement** : où peut-on récupérer du cash ?

### Les leviers cash en distressed (action court terme)

| Levier | Délai | Impact | Risque |
|--------|-------|--------|--------|
| Affacturage | 2 sem | +50-70 % créances | Coût 1-3 % |
| Cession Dailly | 1 sem | +80 % créances | Engagement banque |
| Sale & lease-back | 4-8 sem | +cash sur immo | Loyer LT |
| Étalement URSSAF (CCSF) | 1-2 mois | +1-3 mois TVA/charges | Demande à faire |
| Médiation crédit BdF | 2-4 sem | Préserve concours | Engagement de plan |
| Loi Sapin 2 (paiement clients) | Légal | Force paiement clients en retard | Litige |

## Le 13WCF en distressed M&A — l'outil de DD repreneur

### Ce qu'on demande à l'AJ post-NDA
- 13WCF actuel + historique
- Hypothèses sous-jacentes
- Stress tests (perte d'un client clé)

### Ce qu'on en fait
1. **Valider la viabilité** : l'entreprise tient-elle jusqu'au closing ?
2. **Identifier le BFR repreneur** : combien d'apport en plus du prix ?
3. **Calculer le pic de tension** : quand le repreneur doit-il avoir injecté du cash ?
4. **Stress tester l'offre** : si CA -10 % à la reprise, on tient ?

## Le calcul du BFR de reprise (CRITIQUE)

```
Total apport repreneur = Prix de cession + BFR de reprise + CAPEX immédiat + provision restructuration
```

**Erreur classique du repreneur novice** : calculer uniquement le prix.

**En réalité** :
- Prix de cession : 500 k€
- BFR à reconstituer : **300-800 k€** (souvent !)
- CAPEX urgent (machines obsolètes) : 100-200 k€
- Provision restructuration (indemnités) : 100-300 k€
- **Total apport réel : 1-1,8 M€**

→ C'est pour ça que les repreneurs sous-financés échouent dans les 6 mois post-reprise.

## Cas pratique : 13WCF d'une PME en RJ

```
PME en RJ, 6 sem avant deadline offre. Solde initial 50 k€.

Semaine    S+1   S+2   S+3   S+4   S+5   S+6   S+7   S+8
─────       ───   ───   ───   ───   ───   ───   ───   ───
Solde init  50    35    -10   25    -45   10    -20   -85
                  ↑           ↑           ↑           ↑
                  Salaires    Salaires    Salaires    AGS prend
                              + URSSAF    + URSSAF    le relais
+ Encaiss.  60    40    50    40    65    35    50    20
- Salaires  0    -45    0    -50    0    -25    0     0
- Sociales  0     0    -25    0    -25    0    -10    0
- Fourn.   -25   -20   -15   -25   -15   -25   -45   -10
- Autres   -50   -20    -5   -35   -20    -5   -10    -10
─────       ───   ───   ───   ───   ───   ───   ───   ───
Solde fin   35   -10   -5   -45    -40  -10   -35    -85
            ↑                ↑           ↑           ↑
            OK                ROUGE       ROUGE       AGS
```

**Lecture** :
- Pic de tension semaine 4-5 (-45 k€)
- Sans intervention, mort à semaine 7-8
- AGS prend le relais sur les salaires non payés (super-privilège)
- Repreneur doit **injecter ~80-100 k€ minimum** au closing pour stabiliser

## Question piège

> "Pourquoi le BFR explose toujours en pré-procédure ?"

**Réponse modèle (60 sec)** :
> "C'est mécanique et c'est l'un des signaux les plus fiables d'une entreprise en pré-faillite. Trois forces se combinent. **Premièrement**, les **clients sentent le danger** et profitent pour payer en retard — le DSO augmente. **Deuxièmement**, les **fournisseurs sentent aussi le danger** et exigent d'être payés plus vite, voire en avance, sinon ils coupent les livraisons. Donc le DPO **diminue**. **Troisièmement**, l'entreprise **gonfle ses stocks** pour assurer la production face aux ruptures fournisseurs, ou parce que les ventes ralentissent et que la production continue par inertie. Donc le DIO augmente. Le cash conversion cycle peut passer de 60 jours à 130 jours en l'espace de quelques mois, ce qui veut dire qu'il faut deux fois plus de BFR pour faire tourner la même boîte. Comme l'entreprise n'a plus accès au financement bancaire à ce stade, elle se retrouve mécaniquement en cessation des paiements. C'est pour ça que dans une DD repreneur, **on regarde le BFR avant l'EBITDA**."

## À retenir absolument
- BFR = (Stocks + Clients) - (Fournisseurs + Fiscal/Social)
- DSO normal 30-60 j, > 90 j = tension
- DPO > 120 j = procédure imminente
- DIO > 120 j = stocks dormants
- Cash conversion cycle > 120 j = crise
- 13WCF = outil central de pilotage distressed
- BFR de reprise = souvent égal au prix de cession (à provisionner !)
- AGS prend le relais sur les salaires en cas de cessation de paiements

## Related
- [[brantham/mastery/finance/_MOC]]
- [[brantham/mastery/finance/01-bilan-distressed]]
- [[brantham/mastery/finance/02-compte-resultat-distressed]]
- [[brantham/knowledge/finance/restructuration-dette]]
