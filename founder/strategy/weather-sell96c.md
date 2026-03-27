---
type: strategy
project: weather-alpha
created: 2026-03-18
tags: [trading, weather, kalshi, polymarket, quantitative]
---

# Weather Alpha — Strategie SELL 96c

## Le Concept en 30 Secondes

Sur Kalshi et Polymarket, des gens parient sur la meteo. Par exemple :
"Est-ce que la temperature max a NYC va depasser 90F (32.2C) demain ?"

Le contrat trade a 96 centimes. Ca veut dire que le marche pense qu'il y a **96% de chances** que ca arrive.

Nous, on a 6 modeles meteo (3 classiques + 3 IA) qui disent : "En fait, c'est plutot 70%."

On **vend** ce contrat a 96c. Si l'evenement n'arrive pas, on garde les 96c. S'il arrive, on paie 4c.

```
  LE MARCHE                          NOUS
  =======                           ====

  "96% de chances"                   "70% de chances"

  Prix: 96c                          Fair value: 70c
         \                          /
          \    ECART = 26 centimes /
           \    (c'est l'EDGE)   /
            +-------------------+

  Le marche surpaie.
  On vend cher, l'evenement n'arrive pas souvent, on empoche.
```

---

## Comment Marchent Les Contrats Meteo

### Mecanique d'un Contrat Binaire

Un contrat binaire vaut **$1 si l'evenement arrive, $0 sinon**.
Le prix est entre 0c et 100c. C'est aussi la probabilite implicite.

```
  CONTRAT: "NYC max temp > 90F?"
  ==============================

  Prix YES = 96c     -->  "96% de chances" (selon le marche)
  Prix NO  = 4c      -->  "4% de chances que ca n'arrive PAS"

  YES + NO = 100c = $1 toujours


  ACHETEUR YES (le marche)         VENDEUR YES (nous)
  ========================         ===================

  Paie 96c                         Recoit 96c
  Si evenement arrive:             Si evenement arrive:
    Recoit $1                        Paie $1
    Profit: +4c                      Perte: -4c

  Si evenement n'arrive PAS:       Si evenement n'arrive PAS:
    Recoit $0                        Paie $0
    Perte: -96c                      Profit: +96c


  L'acheteur risque beaucoup (96c) pour gagner peu (4c).
  Le vendeur risque peu (4c) pour gagner beaucoup (96c).
```

### Les Types de Contrats Qu'on Trade

On ne trade que 2 types :

```
  HIGH_TEMP (Temperature Above)
  ==============================
  "Est-ce que le max du jour va depasser X degres ?"

  Exemples reels:
  - "NYC max temp > 95F (35C)?"     prix: 92c
  - "Phoenix max temp > 115F (46C)?" prix: 88c
  - "Chicago max temp > 90F (32C)?" prix: 96c

  Resolution: temperature max officielle du jour (station ASOS)


  LOW_TEMP (Temperature Below)
  ==============================
  "Est-ce que le min du jour va descendre sous X degres ?"

  Exemples reels:
  - "Denver min temp < 32F (0C)?"   prix: 89c
  - "Boston min temp < 20F (-7C)?"  prix: 94c

  Resolution: temperature min officielle du jour
```

### Pourquoi Ces Contrats Sont Surpayes

```
  4 RAISONS POUR LESQUELLES LE MARCHE A TORT
  ============================================

  1. BIAIS PSYCHOLOGIQUE
  +--------------------------------------------------+
  | Les gens surestiment les evenements extremes.     |
  | "Il a fait 95F hier, donc ca va continuer."       |
  | En realite, la meteo revient vers la moyenne.     |
  +--------------------------------------------------+

  2. ASYMETRIE D'INFORMATION
  +--------------------------------------------------+
  | Les traders retail regardent l'app meteo de leur  |
  | telephone. Nous, on a 6 modeles NWP + IA dont    |
  | le HRRR a 3km de resolution (pas sur votre app). |
  +--------------------------------------------------+

  3. MARCHE ILLIQUIDE
  +--------------------------------------------------+
  | Volume faible = pas de market makers pro.         |
  | Les prix s'eloignent de la fair value sans que    |
  | personne ne corrige.                              |
  +--------------------------------------------------+

  4. FRAIS ASYMETRIQUES
  +--------------------------------------------------+
  | Kalshi: 7% sur les PROFITS seulement.             |
  | Quand on vend a 96c et qu'on gagne 96c,          |
  | on paie 7% x 96c = 6.7c de frais.                |
  | Mais le retail qui achete a 96c pour gagner 4c    |
  | paie 7% x 4c = 0.3c. Ca l'encourage a acheter.  |
  +--------------------------------------------------+
```

---

## Nos 6 Modeles

### Vue d'Ensemble

```
  MODELES PHYSIQUES (NWP)               MODELES IA (ML)
  ======================                ===============

  GFS         HRRR        ECMWF        GraphCast   Pangu    GenCast
  (NOAA)      (NOAA)      (Europe)     (Google)    (Huawei) (Google)
  25km        3km         10km         25km        25km     25km
  maj/6h      maj/1h      maj/12h      on-demand   ...      ...
    |           |            |            |          |        |
    |     Le + precis        |            |          |        |
    |     a court terme      |            |          |        |
    |     (convection,       |       Diversite       |        |
    |      orages)           |       non-lineaire    |        |
    |                   Le + fort         |          |        |
    |                   sur les           |          |        |
    |                   blocages          |          |        |
    |                   (vagues de        |          |        |
    |                    chaleur)         |          |        |
    +--------+----------+---+---+--------+-----+----+--------+
             |               |                 |
             v               v                 v
         PREVISION       PREVISION         DIVERSITE
         CONVECTIVE      GRANDE ECHELLE    COMPLEMENTAIRE
```

### Pourquoi 6 Modeles et Pas 1 ?

```
  UN SEUL MODELE = DANGEREUX
  ===========================

  Chaque modele a des biais specifiques :

  +----------+------------------+---------------------------+
  | Modele   | Fort sur         | Faible sur                |
  +----------+------------------+---------------------------+
  | GFS      | Flux d'ouest     | Evenements locaux         |
  |          | (zonal flow)     | Biais: +0.1C en zonal     |
  +----------+------------------+---------------------------+
  | HRRR     | Convection,      | Previsions > 18h          |
  |          | orages,          | (trop peu de recul)       |
  |          | chaleur locale   |                           |
  +----------+------------------+---------------------------+
  | ECMWF    | Blocages atmos-  | Resolution plus grossiere |
  |          | pheriques (vagues| que HRRR en local         |
  |          | de chaleur qui   |                           |
  |          | durent)          |                           |
  +----------+------------------+---------------------------+
  | IA       | Patterns non-    | Pas de physique, peut     |
  | (3 mod.) | lineaires,       | halluciner en regime      |
  |          | transitions      | rare                      |
  +----------+------------------+---------------------------+

  EN COMBINANT LES 6 : on compense les faiblesses de chacun.
```

---

## Le Super-Ensemble Bayesien

C'est le coeur du systeme. On ne fait pas une simple moyenne des 6 modeles.
On fait une **moyenne ponderee dont les poids changent** selon :
- La ville (station meteo)
- Le regime atmospherique (8 types)
- La performance recente de chaque modele

### Comment Ca Marche

```
  ETAPE 1: CHAQUE MODELE DONNE SA PREVISION
  ==========================================

  Pour NYC, contrat "max > 90F (32.2C)":

  GFS:       moyenne = 33.0C, incertitude = 1.5C
  HRRR:      moyenne = 32.8C, incertitude = 1.2C
  ECMWF:     moyenne = 32.5C, incertitude = 1.8C
  GraphCast: moyenne = 32.6C, incertitude = 1.6C
  Pangu:     moyenne = 32.7C, incertitude = 1.4C
  GenCast:   moyenne = 32.4C, incertitude = 1.7C


  ETAPE 2: ON PONDERE SELON LE REGIME
  ====================================

  Regime detecte: "Transitional" (changement de pattern)

  Poids optimises pour (NYC, Transitional):
    GFS:       0.15  (moins fiable en transition)
    HRRR:      0.30  (le plus fin, capte le changement)
    ECMWF:     0.25  (bon en grande echelle)
    GraphCast: 0.15
    Pangu:     0.10
    GenCast:   0.05

  Ces poids sont calcules par minimisation du CRPS
  (Continuous Ranked Probability Score) sur les 200
  derniers cas verifies pour ce couple (station, regime).


  ETAPE 3: ON CALCULE LA DISTRIBUTION MELANGE
  =============================================

  La distribution finale est un melange de Gaussiennes:

    P(T) = 0.15 x N(33.0, 1.5)     <-- contribution GFS
         + 0.30 x N(32.8, 1.2)     <-- contribution HRRR
         + 0.25 x N(32.5, 1.8)     <-- contribution ECMWF
         + 0.15 x N(32.6, 1.6)     <-- contribution GraphCast
         + 0.10 x N(32.7, 1.4)     <-- contribution Pangu
         + 0.05 x N(32.4, 1.7)     <-- contribution GenCast

  Moyenne du melange:
    mu = 0.15x33.0 + 0.30x32.8 + 0.25x32.5 + ... = 32.69C

  On applique ensuite la calibration EMOS (correction des biais):
    mu_cal = a + b x mu_raw = 0.1 + 0.95 x 32.69 = 31.2C
    sigma_cal = sqrt(c + d x variance_raw) = 1.5C


  ETAPE 4: PROBABILITE DE DEPASSEMENT
  ====================================

  "Quelle est la probabilite que T > 32.2C ?"

  Formule mathematique:
    P(T > seuil) = somme des w_k x Phi((mu_k - seuil) / sigma_k)

  Avec nos chiffres calibres:
    Z = (32.2 - 31.2) / 1.5 = 0.67
    P(T > 32.2C) = 1 - Phi(0.67) = 0.25

  RESULTAT: notre modele dit 25% de chances.
  Le marche dit 96%.

  EDGE = 96% - 25% = 71 points de pourcentage.
```

### Les 8 Regimes Atmospheriques

Le regime atmospherique change les poids des modeles ET la taille des positions.

```
  +---------------------+-------+------------------------------------------+
  | Regime              | Multi | Ce que ca veut dire                      |
  +---------------------+-------+------------------------------------------+
  | ZONAL               | 1.0x  | Flux d'ouest normal. Les modeles sont    |
  |                     |       | tres fiables. On mise normalement.       |
  +---------------------+-------+------------------------------------------+
  | ARCTIC OUTBREAK     | 0.5x  | Irruption d'air arctique. Tres           |
  |                     |       | imprevisible, les modeles gallerent.     |
  |                     |       | On divise les positions par 2.           |
  +---------------------+-------+------------------------------------------+
  | RIDGE AMPLIFICATION | 0.7x  | Dome de chaleur. Les modeles captent     |
  |                     |       | le phenomene mais ont un biais chaud.    |
  |                     |       | On reduit de 30%.                        |
  +---------------------+-------+------------------------------------------+
  | TRANSITIONAL        | 0.8x  | Changement de pattern. Incertitude       |
  |                     |       | elevee sur le timing. On reduit de 20%.  |
  +---------------------+-------+------------------------------------------+
  | ATLANTIC BLOCK      | 0.6x  | Blocage atlantique. Duree imprevisible.  |
  |                     |       | On reduit de 40%.                        |
  +---------------------+-------+------------------------------------------+
  | PACIFIC BLOCK       | 0.6x  | Blocage pacifique. Meme logique.         |
  +---------------------+-------+------------------------------------------+
  | CUTOFF LOW          | 0.7x  | Goutte froide isolee. Position exacte    |
  |                     |       | difficile a prevoir.                     |
  +---------------------+-------+------------------------------------------+
  | TROPICAL            | 0.8x  | Influence tropicale (humidite, orages).  |
  |                     |       | Volatilite elevee.                       |
  +---------------------+-------+------------------------------------------+

  Concretement:
    En regime ZONAL avec une position calculee a $500 --> on mise $500
    En regime ARCTIC OUTBREAK                         --> on mise $250
```

---

## L'Arme Secrete: Le Time Decay

C'est notre plus gros avantage. Plus on se rapproche de l'heure de resolution du contrat, plus on sait si l'evenement va arriver ou pas. Et on met a jour nos probabilites en temps reel. Le marche, lui, reagit en retard.

### Le Principe

```
  A T-48h (2 jours avant):
  =========================
  On s'appuie surtout sur les MODELES METEO.
  Ils ont 2 jours pour se tromper.
  Notre avantage est faible.

  model: 70%  |##############################              |
  obs:   10%  |####                                        |
  climo: 20%  |########                                    |


  A T-6h (6 heures avant):
  ==========================
  Les OBSERVATIONS commencent a peser.
  On voit la temperature reelle, le vent, l'humidite.
  Le marche price encore sur les previsions du matin.

  model: 30%  |############                                |
  obs:   50%  |####################                        |
  climo: 20%  |########                                    |


  A T-1h (1 heure avant):
  =========================
  On SAIT quasiment le resultat.
  La temperature actuelle + la tendance diurne
  donnent une prevision tres precise.
  Le marche n'a pas encore ajuste.

  model:  5%  |##                                          |
  obs:   85%  |##################################          |
  climo: 10%  |####                                        |


  A T-15min:
  ===========
  On LIT la temperature sur le capteur.
  C'est presque de l'information parfaite.

  model:  0%  |                                            |
  obs:   95%  |######################################      |
  climo:  5%  |##                                          |
```

### Comment On Extrapole la Temperature

Quand il reste 2 heures, on ne se contente pas de regarder la temperature actuelle. On extrapole en utilisant le **cycle diurne** :

```
  CYCLE DIURNE TYPIQUE
  =====================

  Temperature
  (C)
  35 |              .  .  .
     |           .           .
  30 |        .                 .
     |     .                       .
  25 |  .                             .
     |.                                  .
  20 +--+--+--+--+--+--+--+--+--+--+--+--+--
     0  2  4  6  8  10 12 14 16 18 20 22 24
                     Heure (UTC)

     MIN vers 5h (11 UTC)    MAX vers 14h (20 UTC)

  Formule:
    T(t) = T_moy + Amplitude x cos(2 x pi x (t - t_max) / 24)

  Exemple a 18 UTC (2h avant le max):
    T actuelle = 31.1C
    Tendance = +0.8C/h (on approche du max)
    T prevue a 20 UTC = 31.1 + 2 x 0.4 = 31.9C
    Incertitude = 0.4C (faible, car on est proche)

  Donc P(T > 32.2C) = 1 - Phi((32.2 - 31.9) / 0.4)
                     = 1 - Phi(0.75)
                     = 23%

  Le marche dit encore 96%. On vend.
```

### L'Amplificateur d'Edge

Plus on est pres de la resolution, plus notre edge est amplifie pour le sizing :

```
  Heures    Amplificateur    Pourquoi
  ------    -------------    --------
  T-48h     1.0x             Avantage normal
  T-24h     1.1x             Leger avantage
  T-12h     1.3x             Observations commencent a peser
  T-6h      1.8x             On voit la tendance reelle
  T-3h      2.2x             Forte conviction
  T-2h      2.5x             Quasi-certitude
  T-1h      2.8x             On lit le thermometre
  T-0       3.0x             Information quasi-parfaite

  Concretement:
    Edge de base: 20% --> position $300
    Meme edge a T-2h:  --> position $300 x 2.5 = $750
    (avec les caps de risque qui s'appliquent toujours)
```

---

## Le Calcul de l'Edge

### Formule Complete

```
  EDGE BRUT = Probabilite_modele - Prix_marche
  =============================================

  Exemple:
    Notre modele:   P = 0.25 (25%)
    Prix marche:    M = 0.96 (96c)

    Edge = 0.25 - 0.96 = -0.71

    Negatif = le marche SURESTIME = on VEND


  EDGE NET = |Edge brut| - Friction
  ==================================

  Friction = Spread/2 + Frais de plateforme

  Kalshi:
    Spread bid-ask moyen: 2c  --> Spread/2 = 1c = 0.01
    Frais d'entree: ~1.5%    --> 0.015
    Frais de settlement: 7% sur le profit
    Friction totale entree: 0.01 + 0.015 = 0.025

  Polymarket:
    Spread: ~2c              --> 0.01
    Frais taker: ~1%         --> 0.01
    Friction totale: 0.02

  Avec notre exemple (Kalshi):
    Edge net = 0.71 - 0.025 = 0.685 (68.5% net!)


  EDGE EN POURCENTAGE = |Edge| / Prix_marche
  ============================================

    Edge% = 0.71 / 0.96 = 74%

    Seuil minimum: 20% --> 74% passe largement
```

### Les 11 Portes de Validation

Avant d'executer un trade, les 11 conditions doivent etre remplies :

```
  SIGNAL GENERE
       |
       v
  +----+------------------------------------------+-------+--------+
  | #  | Condition                                | Seuil | Check  |
  +----+------------------------------------------+-------+--------+
  |  1 | Edge net > minimum                       | 15%   |  [x]   |
  |  2 | Confiance modele > minimum               | 30%   |  [x]   |
  |  3 | Nombre de modeles d'accord >= quorum     | 3/6   |  [x]   |
  |  4 | Ecart entre modeles < maximum             | 25%   |  [x]   |
  |  5 | Temps avant resolution > minimum          | 2h    |  [x]   |
  |  6 | Prevision recente (pas perimee)           | <24h  |  [x]   |
  |  7 | Prix marche recent (pas stale)            | <5min |  [x]   |
  |  8 | Exposition journaliere < plafond          | <15%  |  [x]   |
  |  9 | Exposition par station < plafond          | <10%  |  [x]   |
  | 10 | Circuit breaker non declenche             | <8%DD |  [x]   |
  | 11 | Cash disponible suffisant                 | >$0   |  [x]   |
  +----+------------------------------------------+-------+--------+
       |
       | Tous passent?
       |
    OUI |            NON --> REJETE (on log la raison)
       |
       v
  TRADE PLAN GENERE --> ORDRE ENVOYE
```

---

## Le Sizing: Kelly Criterion

### La Formule

Le critere de Kelly dit combien miser pour maximiser la croissance du capital a long terme.

```
  FORMULE KELLY POUR CONTRAT BINAIRE
  ===================================

  f* = (p x b - q) / b

  ou:
    p = probabilite de gagner (notre modele)
    q = 1 - p = probabilite de perdre
    b = ratio gain/mise = combien on gagne pour 1$ mise


  POUR UN SELL YES A 96c:
  ========================

  Si on vend YES a 96c:
    - On recoit 96c immediatement
    - Si l'evenement N'ARRIVE PAS: on garde les 96c (gain = 96c)
    - Si l'evenement ARRIVE: on paie $1, perte nette = 4c

  Donc:
    Mise (risque) = 4c par contrat
    Gain potentiel = 96c par contrat
    b = 96 / 4 = 24

  Avec notre modele qui dit 25% de chances (donc 75% de gagner):
    p = 0.75 (probabilite qu'il fasse PAS 90F)
    q = 0.25
    b = 24

    f* = (0.75 x 24 - 0.25) / 24
       = (18 - 0.25) / 24
       = 17.75 / 24
       = 0.74 = 74%

  Kelly dit de miser 74% du capital! C'est enorme et dangereux.


  KELLY FRACTIONNEL (25%)
  ========================

  On ne mise que 25% du Kelly optimal = fraction conservative.

    f_reel = 0.74 x 0.25 = 0.185 = 18.5%

  Sur un bankroll de $10,000:
    Position = 0.185 x $10,000 = $1,850

  MAIS on a un cap a 5% du bankroll par trade:
    Max position = 0.05 x $10,000 = $500

    Position finale = min($1,850, $500) = $500


  PUIS ON AJUSTE PAR LE REGIME:
    Regime "Transitional": multiplicateur = 0.8x
    Position = $500 x 0.8 = $400

  ET PAR LE TIME DECAY (amplificateur):
    A T-6h: amplificateur = 1.8x
    Position = $400 x 1.8 = $720
    Mais re-cap a $500 (max par trade)

    Position finale = $500
```

---

## La Gestion du Risque

### Architecture en 4 Niveaux

```
  NIVEAU 1: PAR TRADE
  ====================

  +---------------------------------------------------------+
  |                                                         |
  |  Kelly fractionnel 25%                                  |
  |  = on mise 1/4 de l'optimum mathematique                |
  |                                                         |
  |  Cap a 5% du bankroll par position                      |
  |  = sur $10,000, max $500 par trade                      |
  |                                                         |
  |  Ordre LIMIT seulement (pas de market order)            |
  |  Slippage max: 1%                                       |
  |  TTL: 60 secondes (l'ordre expire si pas execute)       |
  |                                                         |
  +---------------------------------------------------------+


  NIVEAU 2: PAR STATION / PAR JOUR
  ==================================

  +---------------------------------------------------------+
  |                                                         |
  |  Exposition daily totale: max 15% du bankroll           |
  |  = max $1,500 en jeu sur tous les trades du jour        |
  |                                                         |
  |  Exposition par station: max 10% du bankroll            |
  |  = max $1,000 en jeu sur NYC par exemple                |
  |                                                         |
  |  Max 5 contrats qui resolvent le meme jour              |
  |  = decorrelation temporelle forcee                      |
  |                                                         |
  |  Pourquoi?                                              |
  |  Si tous les contrats NYC resolvent le meme jour        |
  |  et qu'il y a un evenement meteo surprise,              |
  |  on ne perd pas tout d'un coup.                         |
  |                                                         |
  +---------------------------------------------------------+


  NIVEAU 3: CIRCUIT BREAKER (COUPE-CIRCUIT)
  ==========================================

  +---------------------------------------------------------+
  |                                                         |
  |  Bankroll peak: $10,500 (plus haut historique)          |
  |  Bankroll actuel: $9,660                                |
  |  Drawdown: ($10,500 - $9,660) / $10,500 = 8%           |
  |                                                         |
  |  8% = SEUIL ATTEINT --> CIRCUIT BREAKER DECLENCHE       |
  |                                                         |
  |  Actions immediates:                                    |
  |  1. Diviser TOUTES les positions par 2                  |
  |  2. Cooldown de 30 minutes (aucun nouveau trade)        |
  |  3. Logger l'evenement                                  |
  |                                                         |
  |  Reset: quand le bankroll fait un nouveau sommet        |
  |  (au-dessus de $10,500 dans cet exemple)                |
  |                                                         |
  +---------------------------------------------------------+


  NIVEAU 4: VALUE AT RISK (VaR) MONTE CARLO
  ===========================================

  +---------------------------------------------------------+
  |                                                         |
  |  On simule 10,000 scenarios du portefeuille.            |
  |                                                         |
  |  Pour chaque scenario:                                  |
  |  - On tire au sort si chaque contrat est gagne/perdu    |
  |  - On prend en compte les CORRELATIONS entre stations   |
  |    (si NYC fait chaud, Boston aussi souvent)             |
  |  - On calcule le P&L total du portefeuille              |
  |                                                         |
  |  Resultat:                                              |
  |  VaR 95% = -$320                                        |
  |    "Dans 95% des cas, on perd max $320"                 |
  |                                                         |
  |  VaR 99% = -$680                                        |
  |    "Dans 99% des cas, on perd max $680"                 |
  |                                                         |
  |  Regle: VaR 99% doit rester < 8% du bankroll            |
  |  $680 < $800 (8% de $10k) --> OK                        |
  |                                                         |
  |  Si VaR depasse: on bloque les nouveaux trades          |
  |  jusqu'a ce que des positions se ferment.               |
  |                                                         |
  +---------------------------------------------------------+
```

---

## Exemple Complet: Un Trade de A a Z

```
  SITUATION
  =========
  Date: 15 juillet 2026, 14h UTC (10h NYC)
  Contrat: "NYC max temp > 95F (35C)?"
  Plateforme: Kalshi
  Prix marche: 96c (le marche dit 96%)
  Resolution: 16 juillet a 06 UTC (dans 16 heures)
  Temperature actuelle a NYC: 32.8C (91F)
  Regime atmospherique: Ridge Amplification (dome de chaleur)


  ETAPE 1: LES 6 MODELES DONNENT LEUR PREVISION
  ================================================

  GFS:       max prevu = 34.2C, sigma = 1.8C
  HRRR:      max prevu = 33.8C, sigma = 1.3C   <-- le + precis
  ECMWF:     max prevu = 34.5C, sigma = 2.0C
  GraphCast: max prevu = 34.0C, sigma = 1.5C
  Pangu:     max prevu = 33.9C, sigma = 1.6C
  GenCast:   max prevu = 34.1C, sigma = 1.7C


  ETAPE 2: SUPER-ENSEMBLE (regime = Ridge Amp)
  =============================================

  Poids pour (NYC, Ridge_Amp):
    GFS: 0.15, HRRR: 0.35, ECMWF: 0.15
    GraphCast: 0.15, Pangu: 0.12, GenCast: 0.08

  Moyenne ponderee: 34.0C
  Apres calibration EMOS: mu = 33.5C, sigma = 1.6C


  ETAPE 3: PROBABILITE DE DEPASSEMENT
  ====================================

  P(T > 35C) = 1 - Phi((35 - 33.5) / 1.6)
             = 1 - Phi(0.94)
             = 0.174
             = 17.4%


  ETAPE 4: TIME DECAY (T-16h)
  ============================

  A 16h de la resolution:
    model_weight = 0.55
    obs_weight = 0.25
    climo_weight = 0.20

  Observation-based probability (32.8C actuel, max prevu ~34.5C):
    P_obs(T > 35C) = 0.22 (avec extrapolation diurne)

  Climatologie historique pour NYC mi-juillet:
    P_climo(T > 35C) = 0.08 (rare, historiquement)

  Probabilite melangee:
    P = 0.55 x 0.174 + 0.25 x 0.22 + 0.20 x 0.08
    P = 0.096 + 0.055 + 0.016
    P = 0.167 = 16.7%

  Edge amplifier a T-16h: 1.15x (faible, on est loin)


  ETAPE 5: CALCUL DE L'EDGE
  ==========================

  Notre probabilite: 16.7%
  Prix marche: 96%

  Edge brut = 0.167 - 0.96 = -0.793 (negatif = SELL)
  |Edge| = 79.3%!

  Friction Kalshi:
    Spread/2 = 0.01
    Fee entree = 0.015
    Total: 0.025

  Edge net = 0.793 - 0.025 = 0.768 (76.8%)
  Edge% = 0.793 / 0.96 = 82.6%


  ETAPE 6: LES 11 CHECKS
  ========================

  [x] Edge net 76.8% >= 15%           PASSE
  [x] Confiance 0.52 >= 30%           PASSE
  [x] 5 modeles d'accord >= 3         PASSE
  [x] Spread modeles 4.2% <= 25%      PASSE
  [x] TTR 16h >= 2h                   PASSE
  [x] Forecast age 2h <= 24h          PASSE
  [x] Prix age 30s <= 300s            PASSE
  [x] Expo daily 5% <= 15%            PASSE
  [x] Expo station NYC 3% <= 10%      PASSE
  [x] Circuit breaker OK              PASSE
  [x] Bankroll $10,200 > $0           PASSE

  --> TOUS LES 11 PASSENT


  ETAPE 7: KELLY SIZING
  ======================

  p = 0.833 (probabilite de gagner = 1 - 0.167)
  q = 0.167
  b = payout/cost = 0.96 / 0.04 = 24

  f* = (0.833 x 24 - 0.167) / 24
     = (20 - 0.167) / 24
     = 0.826 = 82.6%

  Fractional Kelly (25%):
    f = 0.826 x 0.25 = 0.207 = 20.7%

  Position brute:
    $10,200 x 0.207 = $2,111

  Cap 5% bankroll:
    max = $10,200 x 0.05 = $510

  Regime adjustment (Ridge Amp = 0.7x):
    $510 x 0.7 = $357

  Edge amplifier (T-16h = 1.15x):
    $357 x 1.15 = $411

  Position finale: $411


  ETAPE 8: ORDRE
  ===============

  Type: LIMIT SELL YES
  Prix: 96c (prix actuel)
  Montant: $411
  Nombre de contrats: $411 / $0.04 (risque par contrat) = 10,275 contrats
  TTL: 60 secondes
  Slippage max: 1%
  Exit: hold to resolution


  ETAPE 9: SCENARIOS DE RESOLUTION
  =================================

  SCENARIO A: Le max NYC atteint 94.8F (34.9C) - PAS 95F
  --------------------------------------------------------
  L'evenement n'arrive pas. Le contrat expire a $0.
  On garde les 96c par contrat.
  Profit: 10,275 x $0.96 = $9,864
  Frais Kalshi (7% du profit): $690
  Profit net: $9,174

  SCENARIO B: Le max NYC atteint 96.1F (35.6C) - DEPASSE 95F
  ------------------------------------------------------------
  L'evenement arrive. Le contrat expire a $1.
  On paie $1 - $0.96 = $0.04 par contrat.
  Perte: 10,275 x $0.04 = $411
  (Pas de frais Kalshi car on a perdu)
  Perte nette: -$411


  EXPECTED VALUE:
  ===============
  EV = 0.833 x $9,174 + 0.167 x (-$411)
     = $7,642 - $69
     = +$7,573 sur ce trade
```

---

## Chiffres Cles de la Strategie

```
  +----------------------------------+---------+
  | Parametre                        | Valeur  |
  +----------------------------------+---------+
  | Edge minimum pour trader         | 20%     |
  | Edge net minimum (apres frais)   | 15%     |
  | Confiance modele minimum         | 30%     |
  | Quorum de modeles                | 3 sur 6 |
  | Kelly fractionnel                | 25%     |
  | Max par trade                    | 5%      |
  | Max exposition par jour          | 15%     |
  | Max exposition par station       | 10%     |
  | Circuit breaker (drawdown)       | 8%      |
  | Cooldown apres circuit breaker   | 30 min  |
  | Contrats resolving meme jour     | max 5   |
  | Temps min avant resolution       | 2h      |
  | Side autorise                    | SELL    |
  | Types de contrats                | HI/LO   |
  | Prix minimum pour vendre         | 85c     |
  | Nombre de modeles                | 6       |
  | Nombre de stations               | 15      |
  | Frais Kalshi                     | ~1.5%+7%|
  | Frais Polymarket                 | ~1%     |
  +----------------------------------+---------+
```

---

## En Une Phrase

**On utilise 6 modeles meteo pour identifier les contrats ou le marche surestime un evenement de temperature extreme, on les vend a 96c, et on gagne 96c quand l'evenement n'arrive pas (ce qui arrive plus souvent que le marche le pense).**

## Related
- [[_system/MOC-master]]
