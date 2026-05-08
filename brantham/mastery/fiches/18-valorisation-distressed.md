---
type: fiche-mastery
couche: 4
jour: 22
project: brantham
date: 2026-05-08
---

# J22 — Valorisation distressed : 4 méthodes

## Définition en 1 phrase
> La valorisation distressed combine plusieurs méthodes (multiples, patrimoniale, DCF, liquidative) pour fixer un **prix d'offre crédible** dans un contexte d'asymétrie d'information et de deadline courte.

## Les 4 méthodes en distressed

```
                ┌────────────────────────────┐
                │  VALORISATION DISTRESSED   │
                └────────────┬───────────────┘
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
       ▼                     ▼                     ▼
   ① MULTIPLES         ② PATRIMONIALE         ③ DCF         ④ LIQUIDATIVE
   (sectoriels +       (actif net               (BP repreneur)  (valeur si tout
    décote)             réévalué)                                vendu en LJ)
   PRINCIPAL           BORNE BASSE             COMPLÉMENT      BORNE BASSE
```

### Méthode 1 — Multiples (principale)
- EBITDA normalisé × multiple sectoriel × (1 - décotes cumulées)
- Voir [[brantham/mastery/finance/05-multiples-valorisation]]
- **Méthode de référence** en distressed PME viable

### Méthode 2 — Patrimoniale (Actif Net Réévalué)
```
ANR = Σ Valeur de marché des actifs - Σ Dettes effectives
```
- Pertinente quand actifs identifiables forts (immobilier, machines, marques, brevets)
- Pertinente quand EBITDA négatif structurel
- **Borne basse** : si on rachète moins, on est en dessous de la simple valeur des actifs

### Méthode 3 — DCF ajusté distressed
- Free Cash Flow projetés sur 5-10 ans + valeur terminale
- **WACC distressed élevé** : 15-25 % (vs 8-12 % normal)
- Bêta levé : 1,5-2,5 (vs 1,0-1,5 normal)
- **Méthode complémentaire**, à utiliser pour "sanity check"

### Méthode 4 — Valeur liquidative
- Si tout est vendu à la découpe en LJ
- Décote 30-60 % sur valeur comptable des actifs
- **Plancher absolu** du prix offert

## Triangulation des méthodes

```
Méthode             Range (k€)        Pondération
─────────           ──────────        ────────────
Multiples           700-900           60 %
Patrimoniale        500-700           20 %
DCF                 800-1000          15 %
Liquidative         300-500            5 %
─────                                  
RANGE COMPOSITE     650-820           Médiane = 730
PRIX OFFRE CIBLE    750 k€            (médiane prudente)
```

## L'EBITDA normalisé — point de départ

Voir [[brantham/mastery/finance/04-ebitda-normalise]] pour le détail.

**En résumé** :
1. Partir de l'EBITDA reporté
2. Ré-intégrer les charges non récurrentes (procédure, litiges, sinistre)
3. Ré-intégrer la sur-rémunération dirigeant
4. Ajuster les loyers et charges hors marché
5. Provisionner les retraitements négatifs (stocks dormants, créances douteuses)
6. Obtenir l'EBITDA normalisé

## Les multiples sectoriels FR à connaître

| Secteur | Multiple sain | Multiple distressed |
|---------|--------------|---------------------|
| Tech / SaaS | 7-12x | 3-5x |
| Industrie spécialisée | 5-7x | 2-3x |
| Industrie manufacturière | 4-5x | 1,5-2,5x |
| Services pro | 5-7x | 2-3x |
| Distribution | 4-5x | 1,5-2,5x |
| Restauration | 3-5x | 1-2x |
| BTP | 3-4x | 1-2x |
| Automobile | 3-4x | 1-2x |

## Les décotes à appliquer

### Décote distressed (toujours)
- **30-50 %** du multiple sectoriel
- Justification : risque opérationnel, deadline, incertitude

### Décotes structurelles cumulables
- Concentration client (top 5 > 70 %) : -15 à -30 %
- Dépendance dirigeant fort : -20 à -40 %
- Petite taille (CA < 2 M€) : -10 à -25 %
- Marché en déclin : -15 à -30 %
- Pas de système de gestion : -10 à -15 %
- Manque préparation cession : -10 à -30 %

→ **Cumulées** : souvent 50-70 % de décote totale en distressed

## Workflow de valorisation (1 journée)

### Matin (4h)
1. Lecture bilan + P&L 3 ans (1h)
2. Calcul ratios + EBITDA normalisé (1h)
3. Identification multiple sectoriel (30 min)
4. Application décotes (30 min)
5. Calcul EV par méthode multiples (1h)

### Après-midi (4h)
6. Valeur patrimoniale : revaloriser actifs (2h)
7. DCF simplifié (1h)
8. Valeur liquidative (30 min)
9. Triangulation + range final (30 min)

## Cas pratique chiffré

```
ENTREPRISE INDUSTRIELLE METALLURGIE
- CA 6 M€ (vs 8 M€ il y a 3 ans)
- EBITDA reporté : -200 k€
- Capitaux propres : -500 k€
- Dette nette : 2,5 M€
- En RJ depuis 6 mois, plan de cession

ÉTAPE 1 — EBITDA NORMALISÉ
─────────────────────────
EBITDA reporté          -200
+ Sur-rémunération DG    +130
+ Sur-loyer SCI familiale +40
+ Litige one-shot        +60
+ Frais procédure        +50
+ Frais perso DG         +20
─────                    ─────
EBITDA normalisé          100 k€

ÉTAPE 2 — MULTIPLE
──────────────────
Multiple sectoriel "industrie manufacturière" : 4,5x
Décote distressed : -40 %
Décote concentration client (top 3 = 65 %) : -20 %
Décote taille (CA < 10M) : -10 %
─────
Multiple ajusté = 4,5 × 0,60 × 0,80 × 0,90 = 1,94x

ÉTAPE 3 — VALORISATION MULTIPLES
────────────────────────────────
EV multiples = 100 × 1,94 = 194 k€

ÉTAPE 4 — VALORISATION PATRIMONIALE
───────────────────────────────────
Actifs réévalués :
- Immobilier industriel : 800 k€ (valeur expert)
- Machines : 200 k€ (valeur de marché)
- Stocks : 150 k€ (après dépréciation 25 %)
- Marque : 100 k€ (valeur estimée)
- Créances clients récupérables : 100 k€ (DSO ajusté)
─────
TOTAL ACTIFS RÉÉVALUÉS : 1 350 k€

Mais en plan de cession : pas de reprise passif, donc on prend les actifs
ET on a une borne basse à 1 350 k€ → mais c'est contre-intuitif

→ En réalité, la valorisation patrimoniale donne le PRIX MAX que pourrait
  obtenir le tribunal en LJ découpe, mais en plan de cession on valorise
  l'activité globale (going concern), pas la somme des actifs.

ÉTAPE 5 — DCF SIMPLIFIÉ
────────────────────────
EBITDA normalisé an 1 : 100 k€
Hypothèses repreneur : amélioration 50 k€/an
EBITDA normalisé an 5 : 300 k€
WACC distressed : 18 %
Valeur terminale : 8x EBITDA an 5 = 2 400 k€

NPV ≈ 800-1000 k€

ÉTAPE 6 — TRIANGULATION
──────────────────────
Multiples            : 200 k€
Patrimoniale active  : 1 350 k€ (mais going concern)
DCF                  : 800-1000 k€
Liquidative          : 600-800 k€

→ RANGE COHÉRENT : 600-1000 k€
→ PRIX OFFRE CIBLE : 750-800 k€

PRIX/CA : ~13 % du CA → conforme distressed
```

## Erreurs classiques

### Erreur 1 : ne pas retraiter l'EBITDA
- Valoriser sur EBITDA reporté = sous-estimer de 50-200 %
- **Toujours** normaliser

### Erreur 2 : appliquer multiples sains
- Multiples sectoriels publics = entreprises **saines**
- En distressed, décote 30-50 % automatique

### Erreur 3 : oublier les décotes structurelles
- Distressed seul ne suffit pas
- Concentration, taille, marché : à intégrer

### Erreur 4 : oublier le BFR de reprise
- Prix d'offre + BFR de reprise = vrai apport
- Souvent BFR = 50-100 % du prix !

### Erreur 5 : se laisser piéger par la valeur patrimoniale
- Si EBITDA normalisé est bas, on tend à valoriser à la patrimoniale (haute)
- Mais le tribunal valorise l'**activité** (going concern), pas la somme des actifs

## Question piège

> "Comment résoudre la contradiction quand la valeur patrimoniale est très supérieure à la valeur multiples ?"

**Réponse modèle (90 sec)** :
> "C'est une situation classique en distressed sur les entreprises avec actifs lourds — industrie, immobilier, machines. La valeur patrimoniale donne par exemple 1,5 million pour les actifs réévalués, mais l'EBITDA normalisé multiplié donne seulement 200 ou 300 mille. **Il y a deux interprétations possibles**. **Première** : l'entreprise vaut effectivement plus en **liquidation découpée** qu'en going concern. C'est le signe que l'**activité elle-même détruit de la valeur** — l'EBITDA est faible parce que l'exploitation génère peu de cash, mais les actifs accumulés ont une valeur de marché. Dans ce cas, le tribunal pourrait préférer une LJ découpe à un plan de cession. **Deuxième** : l'entreprise est sous-exploitée, mal gérée, et un repreneur compétent peut faire bondir l'EBITDA. Là, la valeur DCF (sur projections du repreneur) capture mieux la valeur que les multiples sur EBITDA actuel. **Ma méthode** : quand le delta patrimoniale-multiples est important, je triangule avec un **DCF sur le BP du repreneur** — typiquement EBITDA normalisé an 1 plus amélioration de 30-50 % par an, valeur terminale à 8x EBITDA an 5, WACC à 18-22 %. Et je prends le **range croisé** avec la patrimoniale comme borne basse et le DCF comme cible. Le prix d'offre se cale dans ce range, biaisé vers la médiane. Pour le tribunal, l'argumentaire devient : 'on offre tant parce que la valeur patrimoniale est X, l'activité a un potentiel de Y, et on s'engage à investir Z pour récupérer ce potentiel.' Ça transforme un débat sur un chiffre en débat sur un projet industriel — ce qui joue en notre faveur sur le critère emploi/projet."

## À retenir absolument
- 4 méthodes : multiples (principal), patrimoniale (borne basse), DCF (complément), liquidative (plancher)
- EBITDA normalisé = point de départ obligatoire
- Multiples sectoriels FR : 4-5x industrie, 7-12x tech, 3-4x BTP
- Décote distressed : -30 à -50 %
- Décotes structurelles cumulables (concentration, taille, marché)
- Multiples ajustés finaux : souvent 2-3x EBITDA en distressed
- Trianguler 4 méthodes pour borner le range
- BFR de reprise = à provisionner en plus du prix

## Related
- [[brantham/mastery/curriculum]]
- [[brantham/mastery/finance/04-ebitda-normalise]]
- [[brantham/mastery/finance/05-multiples-valorisation]]
- [[brantham/knowledge/finance/valorisation-distressed]]
- [[brantham/knowledge/finance/financial-modeling-distressed]]
