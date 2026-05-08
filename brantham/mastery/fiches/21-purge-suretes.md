---
type: fiche-mastery
couche: 5
jour: 26
project: brantham
date: 2026-05-08
---

# J26 — Purge des sûretés en plan de cession

## Définition en 1 phrase
> La purge des sûretés (article **L642-12** du Code de commerce) est le mécanisme qui éteint les sûretés grevant les biens repris en plan de cession, en transférant le droit des créanciers garantis du **bien** au **prix de cession**.

## Texte clé (L642-12)
> "Lorsque la cession porte sur des biens grevés d'un privilège spécial, d'un nantissement ou d'une hypothèque, **une quote-part du prix est affectée par le tribunal à chacun de ces biens** pour la répartition du prix et l'exercice du droit de préférence."

## Le mécanisme illustré

```
AVANT CESSION                            APRÈS CESSION (L642-12)
─────────────                            ───────────────────────

Bien (immobilier ex.)        Bien      ───►    Bien (libre, propriété repreneur)
   │                                            
   │ grevé hypothèque                          
   ▼                                            
Banque créancière                    Banque créancière
(rang 1, hypothèque)                 (perd l'hypothèque sur le bien)
                                     (mais conserve droit sur la
                                      QUOTE-PART du prix attribuée
                                      au bien dans la cession)
```

## Les sûretés visées par la purge L642-12

### Listées par l'article
1. **Privilège spécial** (priorité sur un bien spécifique)
2. **Nantissement** (sur fonds de commerce, parts sociales, équipements, etc.)
3. **Hypothèque** (sur immeubles)

### Effet
- Sur le **bien** : extinction de la sûreté
- Sur le **prix** : le créancier garanti récupère sa créance dans la limite du prix attribué au bien (et selon l'ordre des privilèges)

## Les sûretés QUI NE SONT PAS purgées (= qui suivent le bien)

C'est la **NUANCE CRITIQUE** souvent oubliée. Certaines sûretés **subsistent** post-cession :

### 1. Crédit-bail (= leasing)
- Le crédit-bailleur reste **propriétaire** du bien
- Le repreneur doit choisir : continuer le contrat ou rendre le bien
- Article L622-13 : le repreneur peut demander la continuation
- **Ou** : option d'achat à lever pour devenir propriétaire

### 2. Réserve de propriété
- Le vendeur **reste propriétaire** jusqu'au paiement intégral
- Article L624-16 : revendication possible dans 3 mois
- Pour le repreneur : payer le solde ou rendre le bien

### 3. Gage avec dépossession
- Le créancier détient le bien en garantie
- Le bien lui revient si non paiement
- Le repreneur doit racheter la créance pour récupérer le bien

### 4. Droit de rétention
- Créancier qui détient un bien (réparateur, transporteur)
- Conserve le droit de rétention même en procédure
- Doit être payé pour libérer le bien

### 5. Fiducie-sûreté (récente, L622-23-1)
- Le bien est **hors patrimoine** de l'entreprise (fiduciaire)
- Pas de purge possible
- Le repreneur doit racheter au fiduciaire si veut le bien

### 6. Privilège fiscal (parfois)
- Privilège du Trésor sur certains biens
- À examiner au cas par cas selon nature

## Tableau résumé : ce qui suit / ne suit pas

| Sûreté | Purgée par L642-12 ? | Action repreneur |
|--------|---------------------|------------------|
| Hypothèque | Oui | Bien repris libre |
| Nantissement fonds commerce | Oui | Bien repris libre |
| Nantissement parts sociales | Oui | Bien repris libre |
| Gage sans dépossession | Oui | Bien repris libre |
| Privilège spécial mobilier | Oui | Bien repris libre |
| **Crédit-bail** | **Non** | Continuer ou rendre |
| **Réserve de propriété** | **Non** | Payer ou rendre |
| **Gage avec dépossession** | **Non** | Racheter créance |
| **Droit de rétention** | **Non** | Payer pour libérer |
| **Fiducie-sûreté** | **Non** | Racheter au fiduciaire |

## Procédure de purge (L642-12 al. 2)

### Étape 1 : Identification des biens grevés
- L'AJ liste les biens repris avec leurs sûretés
- Le tribunal en prend connaissance avant le jugement de cession

### Étape 2 : Affectation d'une quote-part du prix
- Le tribunal **attribue** dans le jugement une quote-part du prix de cession à chaque bien grevé
- Critère : **valeur respective** des biens (proportionnellement)

### Étape 3 : Effet de la purge
- Le repreneur reçoit le bien **libre**
- Le créancier garanti récupère sur la quote-part attribuée
- Si la quote-part > sa créance : il est payé intégralement
- Si la quote-part < sa créance : il devient chirographaire pour le solde

### Étape 4 : Distribution
- Le MJ distribue selon l'ordre des créanciers (privilèges respectés)

## Cas pratique de purge

```
PRIX DE CESSION : 1 000 k€
Composition du périmètre :

ACTIF                    VALEUR    SÛRETÉ              QUOTE-PART
─────                    ───────   ─────                ──────────
Immobilier               500 k€    Hypothèque banque   500 k€
                                    (créance 700 k€)
Fonds de commerce        300 k€    Nantissement       300 k€
                                    (créance 200 k€)
Stocks                   150 k€    Aucune             150 k€
Créances clients         50 k€     Cession Dailly     50 k€
                                    (créance 80 k€)
─────                    ───────                       ──────────
TOTAL                    1 000 k€                      1 000 k€

DISTRIBUTION
─────────────
Banque hypothèque       : reçoit 500 k€ (vs créance 700 k€) 
                          → 200 k€ chirographaires sur autres biens
                          
Créancier nantissement  : reçoit 300 k€ (vs créance 200 k€)
                          → reçoit intégralement, EXCÉDENT 100 k€ → distribué
                          
Cession Dailly          : reçoit 50 k€ (vs créance 80 k€)
                          → 30 k€ chirographaires
                          
Stocks (libre)          : 150 k€ + excédent 100 k€ + chirographaires
                          → distribués selon ordre L621-2 et autres privilèges
```

## L'enjeu pour le repreneur

### Ce qu'il faut auditer en DD
1. **Liste exhaustive** des sûretés sur tous les biens repris
2. **Distinction** : sûretés purgeables vs non purgeables
3. **Valorisation** des sûretés non purgées (à intégrer dans le coût total)
4. **Stratégie** : racheter, continuer, ou rendre

### Coût caché classique
- Crédit-bail machines : valeur **marché** souvent inférieure à la valeur du contrat → continuer = surpayer
- Réserve de propriété stocks : montant à payer pour libérer = peut être > valeur réelle
- Droit de rétention : créancier négocie cher pour libérer

### Optimisation
- **Négocier** le rachat des sûretés non purgées avant l'audience
- **Désigner précisément** dans l'offre : "Le repreneur reprend X bien sous condition de purge / continuation crédit-bail / rachat créance"
- **Sécurité juridique** : audit des sûretés par avocat spécialisé

## La fiducie-sûreté — le piège moderne

### Fonctionnement
- Le débiteur transfère **la propriété** d'un bien à un fiduciaire (souvent une banque)
- Le bien sort du patrimoine du débiteur
- Si défaillance : la banque-fiduciaire devient propriétaire
- Article L622-23-1 : la fiducie-sûreté **résiste** à la procédure collective

### Pour le repreneur
- Si l'actif convoité est en fiducie-sûreté : **il n'est plus dans le patrimoine** de l'entreprise cédée
- Pas de purge possible
- Doit **racheter au fiduciaire** (banque) ou y renoncer
- À identifier en DD très tôt

## Question piège

> "Pourquoi un repreneur en plan de cession doit-il auditer scrupuleusement les sûretés ?"

**Réponse modèle (90 sec)** :
> "Parce que la purge automatique de l'article L642-12 ne couvre **pas toutes les sûretés**. C'est l'erreur classique du repreneur novice qui pense que tout est purgé en plan de cession et qui se retrouve à devoir payer des sommes considérables post-cession pour récupérer des biens essentiels à l'exploitation. Concrètement : **trois grandes catégories de sûretés résistent à la purge**. **Premièrement les sûretés-propriété** : crédit-bail, réserve de propriété, fiducie-sûreté. Le bien n'est tout simplement pas dans le patrimoine du débiteur — il appartient au crédit-bailleur, au vendeur, ou au fiduciaire. La purge ne peut pas s'exercer sur un bien qui n'appartient pas à l'entreprise. **Deuxièmement les sûretés avec dépossession** : gage avec dépossession, droit de rétention. Le créancier détient physiquement le bien et n'a aucune obligation de le restituer sans paiement. **Troisièmement les fiducies-sûretés modernes**, qui sont sorties du droit commun depuis l'ordonnance de 2021 — l'article L622-23-1 confirme leur résistance à la procédure. En pratique, sur un dossier industriel typique, le repreneur peut découvrir 200 à 500 mille euros de **dette cachée** liée à ces sûretés non purgées : machines en crédit-bail à racheter, stocks sous réserve de propriété à régler, créances clients faisant l'objet de cessions Dailly. Si ce coût n'est pas intégré dans le prix d'offre, l'opération bascule en perte. C'est pour ça qu'on demande systématiquement, dans la data room, l'**état des sûretés détaillé**, et qu'on fait passer un audit avocat spécialisé sûretés avant le dépôt d'offre."

## À retenir absolument
- L642-12 = mécanisme de purge des sûretés en plan de cession
- Purge = transfert droit du créancier du bien au prix
- Sûretés purgées : hypothèque, nantissement, gage sans dépossession, privilège spécial
- Sûretés NON purgées : crédit-bail, réserve propriété, gage avec dépossession, droit rétention, fiducie-sûreté
- Quote-part du prix attribuée à chaque bien grevé
- Pour le repreneur : audit sûretés critique avant offre
- Coût caché possible : 200-500 k€ sur dossier industriel typique

## Related
- [[brantham/mastery/curriculum]]
- [[brantham/mastery/fiches/22-asset-vs-share]]
- [[brantham/knowledge/legal/suretes-en-procedure-collective]]
- [[brantham/knowledge/legal/plans-de-cession]]
