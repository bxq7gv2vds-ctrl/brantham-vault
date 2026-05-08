---
type: fiche-mastery
module: finance
ordre: 1
project: brantham
date: 2026-05-08
---

# Finance #1 — Lire un bilan distressed

## Définition rapide
Le **bilan** est une photo à un instant T du **patrimoine** de l'entreprise.
- **Actif** = ce que l'entreprise possède (emplois)
- **Passif** = comment c'est financé (ressources)
- **Actif = Passif** (toujours)

## Structure du bilan distressed

```
ACTIF                                 PASSIF
─────                                 ──────

ACTIF IMMOBILISÉ                      CAPITAUX PROPRES
─ Incorporel (marques, brevets)       ─ Capital social
─ Corporel (immeubles, machines)      ─ Réserves
─ Financier (titres, prêts LT)        ─ Report à nouveau
                                       ─ Résultat de l'exercice (souvent < 0)

ACTIF CIRCULANT                        DETTES FINANCIÈRES
─ Stocks                              ─ Emprunts bancaires LT
─ Créances clients                    ─ Concours bancaires CT
─ Autres créances                     ─ PGE
─ Disponibilités (cash)               ─ Crédit-bail
                                       ─ Dettes obligataires

CHARGES CONSTATÉES D'AVANCE            DETTES D'EXPLOITATION
                                       ─ Fournisseurs
                                       ─ Fiscales et sociales
                                       ─ Autres dettes
                                       ─ Produits constatés d'avance
```

## Les 4 lectures critiques en distressed

### Lecture 1 — Capitaux propres (= fonds propres)

```
Capitaux propres = Capital + Réserves + Report à nouveau + Résultat
```

| Niveau | Signal |
|--------|--------|
| Positifs et > 50 % du total bilan | Saine |
| Positifs mais < 25 % | Sous-capitalisée (tendue) |
| **Négatifs** | **Capitaux propres < 0 = perte > capital** |

**Article clé : L223-42 (SARL) / L225-248 (SA)** : si les capitaux propres deviennent **inférieurs à la moitié du capital social**, le dirigeant doit consulter les associés sous 4 mois pour décider de la dissolution ou de la régularisation. **À régulariser dans les 2 ans**, sinon dissolution.

→ En distressed, capitaux propres < 0 = très fréquent. C'est le **point de départ** de la procédure.

### Lecture 2 — Dettes financières / EBITDA (gearing)

```
Ratio gearing = Dette nette / EBITDA
Dette nette = Dettes financières - Trésorerie
```

| Ratio | Signal |
|-------|--------|
| < 2x | Saine |
| 2-3x | Acceptable |
| 3-4x | Tendue |
| 4-6x | Stressée |
| **> 6x** | **Distressed** (souvent insoutenable) |

→ En distressed, on voit régulièrement 8-15x. Au-delà, le service de la dette dépasse l'EBITDA = mort lente.

### Lecture 3 — Fonds de roulement (FR)

```
FR = Capitaux propres + Dettes LT - Actif immobilisé
   = Ressources stables - Emplois stables
```

→ FR positif = excédent de ressources stables → bon signe
→ FR négatif = financement court terme des immobilisations → signal d'alerte

### Lecture 4 — BFR

```
BFR = Stocks + Créances clients - Dettes fournisseurs - Dettes fiscales/sociales
```

→ BFR positif = besoin (saine si sous contrôle)
→ BFR qui **explose** = signal majeur de tension (clients qui paient mal, fournisseurs qui resserrent les délais)

### Trésorerie nette

```
TN = FR - BFR
```

| TN | Signal |
|----|--------|
| > 0 | Liquide |
| ≈ 0 | Tendue |
| **< 0** | **Cessation de paiements imminente** |

## Top 10 postes du bilan à auditer ligne par ligne

### 1. Immobilisations corporelles
- **Quoi auditer** : la VNC reflète-t-elle la valeur de marché ?
- **Red flag** : amortissement anormal (entreprise sous-investit)
- **Pour repreneur** : machines obsolètes = besoin CAPEX immédiat

### 2. Immobilisations incorporelles (marques, fonds de commerce)
- **Quoi auditer** : valorisation correcte ? Goodwill non amorti = parfois inflated
- **Red flag** : goodwill > 30 % du bilan = bombe potentielle (test de dépréciation à faire)

### 3. Stocks
- **Quoi auditer** : ancienneté, rotation, dépréciation
- **Red flag** : stocks qui montent + CA qui baisse = stocks dormants
- **Retraitement** : dépréciation à passer (souvent 20-50 % en distressed)

### 4. Créances clients
- **Quoi auditer** : DSO (Days Sales Outstanding) = créances / CA × 365
- **DSO normal** : 30-60 jours selon secteur
- **Red flag DSO > 90 j** : clients qui paient mal ou litiges
- **Provisionnement** : créances douteuses / CA total
- **Top 5 clients** : concentration excessive ?

### 5. Disponibilités (cash)
- **Quoi auditer** : cash réellement disponible vs cash bloqué (séquestre, garantie)
- **Red flag** : cash < 1 mois de charges fixes = mort imminente

### 6. Capitaux propres
- **Quoi auditer** : signe et évolution
- **Red flag** : négatifs ou en chute libre

### 7. Dettes bancaires
- **Quoi auditer** : échéancier, covenants, PGE
- **PGE** : à examiner systématiquement (échéance, garantie BPI 90 %, possibilité de gel)
- **Covenants** : ratios à respecter — déjà violés ?

### 8. Dettes fournisseurs
- **Quoi auditer** : DPO (Days Payable Outstanding) = dettes fourn. / achats × 365
- **DPO normal** : 30-60 jours selon secteur
- **Red flag DPO > 90-120 j** : signal majeur de tension cash (paie en retard pour gagner du temps)
- **Litiges fournisseurs** : combien, montant total ?

### 9. Dettes fiscales et sociales
- **Quoi auditer** : retards URSSAF, TVA, IS ?
- **Red flag** : retards = procédure imminente (cessation de paiements proche)
- **Privilège fiscal** : très protégé en procédure, à régler en priorité

### 10. Engagements hors-bilan
- **Quoi auditer** : cautions données, garanties, crédit-bail, leasing, engagements de retraite
- **Red flag** : engagements > 30 % du bilan = passif caché
- **Crédit-bail** : ne figure pas en dette mais c'est de la dette opérationnelle

## Tableau red flags express

| Poste | Red flag |
|-------|----------|
| Capitaux propres | Négatifs ou < 50 % du capital social |
| Goodwill | > 30 % du bilan, jamais déprécié |
| Stocks | Hausse + baisse CA |
| Créances clients | DSO > 90 j |
| Cash | < 1 mois de charges fixes |
| Dettes bancaires | Covenants violés ou PGE concentrés |
| Fournisseurs | DPO > 120 j |
| Fiscal/social | Retards URSSAF / TVA |
| Hors-bilan | Cautions massives non provisionnées |
| Évolution générale | Bilan qui se dégrade 3 ans de suite |

## Cas pratique : exemple de bilan distressed

```
Bilan PME industrielle CA 8 M€, en RJ depuis 6 mois (M€)

ACTIF                              PASSIF
─────                              ──────
Immo corporelles    2,5            Capitaux propres   -0,8 ← NÉGATIF
Immo incorporelles  1,2            Capital            1,0
                                    Réserves           0,5
Stocks              1,8 (en hausse) RAN               -1,3
Créances clients    1,5 (DSO 110j)  Résultat ex.      -1,0
Cash                0,1            
                                    PGE                1,5 (échéance 2026)
                                    Emprunts bancaires 0,8
                                    Découverts CT      0,4
                                    
                                    Fournisseurs       1,5 (DPO 130 j)
                                    Dettes fiscales    0,3
                                    Dettes sociales    0,4
                                    
                                    
TOTAL ACTIF         7,1            TOTAL PASSIF       7,1
```

**Diagnostic** :
- Capitaux propres **négatifs** → procédure ouverte logiquement
- Stocks en hausse + CA stable → invendus
- DSO 110 j → clients paient mal
- Cash 100 k€ pour ~7 M€ de charges annuelles → 1 semaine !
- DPO 130 j → fournisseurs déjà tendus
- Dettes fiscales/sociales en retard

→ **Reprise possible si** : actifs corporels (machines) ont valeur de marché, marques utilisables, base clients récupérable, périmètre social viable.

## Question piège

> "Comment savoir en 5 minutes si un bilan est sain ou pourri ?"

**Réponse modèle (60 sec)** :
> "Cinq lignes à regarder dans l'ordre. **Un**, les capitaux propres : s'ils sont négatifs ou inférieurs à 50 % du capital social, l'entreprise est en grande difficulté juridique (article L225-248 pour les SA). **Deux**, le ratio dette nette sur EBITDA : au-dessus de 4-5×, la dette n'est plus soutenable. **Trois**, la trésorerie : moins d'un mois de charges fixes, l'entreprise est en cessation de paiements imminente. **Quatre**, le DSO et le DPO : si les délais clients dépassent 90 jours et les délais fournisseurs 120 jours, l'entreprise est en stress cash sévère. **Cinq**, les dettes fiscales et sociales : tout retard URSSAF ou TVA est un signal rouge — le dirigeant gagne du temps en ne payant pas l'État, c'est typique d'une fin de cycle. En cinq minutes, ces cinq points te donnent un diagnostic juste à 80 %."

## À retenir absolument
- 4 lectures : capitaux propres, gearing, fonds de roulement, BFR/trésorerie
- Capitaux propres < 50 % capital social = obligation L225-248 / L223-42
- Gearing > 6x = distressed
- DSO > 90 j et DPO > 120 j = tension critique
- Retards fiscaux/sociaux = cessation paiements proche
- Toujours auditer le hors-bilan (cautions, crédit-bail)

## Related
- [[brantham/mastery/finance/_MOC]]
- [[brantham/mastery/finance/02-compte-resultat-distressed]]
- [[brantham/mastery/finance/03-bfr-trésorerie]]
- [[brantham/mastery/finance/06-red-flags-financiers]]
- [[brantham/knowledge/finance/comptabilite-crise]]
