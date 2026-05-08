---
type: fiche-mastery
module: finance
ordre: 4
project: brantham
date: 2026-05-08
---

# Finance #4 — EBITDA normalisé : les retraitements

## Définition en 1 phrase
> L'**EBITDA normalisé** (ou ajusté) est l'EBITDA retraité de tous les éléments **non récurrents**, **non opérationnels** ou **non normatifs** afin de présenter la profitabilité **réelle et reproductible** de l'entreprise pour un acquéreur.

## Pourquoi c'est central en distressed M&A
- L'EBITDA réel d'une entreprise distressed est **rarement représentatif** de son potentiel.
- Le repreneur valorise sur l'**EBITDA normalisé** post-reprise.
- L'écart entre EBITDA reporté et EBITDA normalisé peut être de **+50 % à +200 %** en distressed.

## Logique du retraitement

```
EBITDA reporté (= EBE comptable)
    │
    ├── (+) Charges non récurrentes (ex: litiges one-shot)
    │
    ├── (+) Rémunération dirigeant excessive (vs marché)
    │
    ├── (+) Loyers hors marché (immobilier dirigeant)
    │
    ├── (+) Coûts liés à la procédure (avocats, AJ)
    │
    ├── (-) Coûts qu'un repreneur DEVRA supporter (ex: salaire DG si famille en place)
    │
    ├── (+/-) Retraitements stocks / créances douteuses
    │
    │
    ▼
EBITDA NORMALISÉ
```

## Les 10 retraitements principaux (Top of Mind)

### 1. Rémunération du dirigeant
**Cas typique** : dirigeant familial qui se rémunère 250 k€/an alors que le marché serait à 120 k€.

```
EBITDA reporté          200 k€
+ Sur-rémunération      130 k€  (250 - 120 normatif)
─────                  ───────
EBITDA normalisé        330 k€
```

**Source data** : grilles INSEE rémunérations dirigeants par secteur/taille, ou benchmark sectoriels (ANDRH, APEC).

### 2. Loyers hors marché
**Cas typique** : SCI familiale loue à l'opérationnelle 120 k€/an pour un local qui se louerait 80 k€ au marché.

```
+ Sur-loyer = 40 k€/an à ré-intégrer dans EBITDA normalisé
```

**Inverse** : si le loyer est sous-évalué (familial), il faut **prévoir une augmentation** pour le repreneur (impact négatif).

### 3. Charges exceptionnelles non récurrentes
**Cas** : litiges, indemnités prud'homales one-shot, sinistre, déménagement.

→ À ré-intégrer (charges qui ne reviendront pas).

### 4. Coûts liés à la procédure
**Cas** : honoraires AJ, avocats restructuring, conseils, frais de justice payés sur l'exercice.

→ À ré-intégrer (n'existeront plus post-reprise).

### 5. Frais financiers hors EBITDA mais charge effective
**Cas** : commissions bancaires, frais de découvert, frais d'affacturage classés en charges externes.

→ Souvent ces "charges externes" sont en réalité des frais financiers déguisés. À analyser.

### 6. Rémunération de la famille (cousins, conjoints)
**Cas** : conjoint en CDI rémunéré 80 k€ pour un job réellement à 30 k€.

→ Ré-intégrer le surplus.

### 7. Frais privés payés par l'entreprise
**Cas** : voitures de fonction de luxe, voyages, restos, abonnements perso, assurance vie dirigeant.

→ Ré-intégrer (5-50 k€/an typique).

### 8. Provisions exceptionnelles ou sous-dotées
**Cas A** : provision exceptionnelle pour risque qui ne se réalisera pas → à reprendre (impact +)
**Cas B** : provisions insuffisantes (clients douteux non provisionnés) → à doter (impact -)

### 9. Stocks déprécié à mettre à jour
**Cas** : stocks dormants > 12 mois non dépréciés.

→ Provisionner (impact négatif sur EBITDA normalisé).

### 10. Synergies négatives ou positives post-reprise
**Cas synergies positives** : repreneur supprimera des fonctions support (RH, compta) déjà chez lui.
**Cas synergies négatives** : repreneur devra embaucher un DG si famille sort.

→ Ces "**synergies**" sont en théorie l'EBITDA **post-reprise** vu par le repreneur, à ne pas confondre avec EBITDA normalisé stricto sensu.

## Tableau de retraitement type

```
ENTREPRISE INDUSTRIELLE PME, CA 8 M€, EBITDA reporté 200 k€

Élément                              Montant     Direction
─────────                            ──────      ─────────
EBITDA reporté                        200       
+ Sur-rémunération dirigeant         +130       (250 → 120 normatif)
+ Sur-loyer SCI                       +40       (120 → 80 marché)
+ Litige one-shot indemnité            +60       (sinistre 2024)
+ Honoraires restructuring             +50       (avocats, AJ)
+ Frais perso passés en EX             +25       (voyages, voitures)
─────                                ─────
EBITDA NORMALISÉ                      505       (+150 % vs reporté)


Sous-jacents post-reprise :
- Repreneur paie un DG 120 k€ (déjà intégré)
- Repreneur paie le loyer marché 80 k€ (déjà intégré)
- Pas de litiges récurrents
- Pas de procédure
- Pas de frais perso

→ EBITDA normalisé reflète bien la profitabilité reproductible
```

## Les pièges classiques du retraitement

### Piège 1 — Trop optimiste
**Erreur** : ré-intégrer toutes les "charges optimisables" sans réalisme.
**Conséquence** : valorisation surévaluée → désillusion post-reprise.

**Règle** : ne ré-intégrer que ce qui est **vérifiable** et **factuel**.

### Piège 2 — Oublier les retraitements négatifs
**Erreur** : oublier que certaines économies (loyer SCI sous-évalué, dirigeant non remplacé) seront des coûts post-reprise.

**Règle** : faire les retraitements dans **les deux sens**.

### Piège 3 — Confondre EBITDA normalisé et synergies
**EBITDA normalisé** = profitabilité de la **cible seule**, retraitée.
**Synergies** = effet de l'**intégration** dans le repreneur.

**Règle** : valoriser sur l'EBITDA normalisé, pas sur les synergies (qui restent au repreneur).

### Piège 4 — Manquer les retraitements de stocks et créances
**Erreur** : se concentrer sur les retraitements "visibles" (rémunération) et oublier les retraitements "comptables" (provisions).

**Règle** : chaque ligne du bilan doit être interrogée.

## Workflow du retraitement (1h chrono)

1. **Lire le PV CA / rapport de gestion** (10 min) — y a-t-il une mention d'éléments exceptionnels ?
2. **Auditer la rémunération dirigeant** vs benchmark (10 min)
3. **Auditer les loyers** vs marché (5 min)
4. **Auditer charges externes** : sous-traitance, honoraires, voyages (10 min)
5. **Auditer résultat exceptionnel** : récurrent ou one-off ? (5 min)
6. **Ajuster provisions** stocks et créances (10 min)
7. **Compiler tableau de retraitement** (10 min)

## Application valorisation

```
EBITDA normalisé : 500 k€
Multiple sectoriel (industrie PME) : 4-5x
─────
Valeur d'entreprise (EV) théorique : 2-2,5 M€

Décote distressed : -30 à -50 %
─────
EV distressed : 1-1,75 M€

- Dette nette à reprendre (généralement 0 en plan de cession)
+ Actifs hors exploitation (immobilier non utilisé, etc.)
─────
Prix d'offre cible : 1-1,5 M€
```

## Question piège

> "Pourquoi l'EBITDA reporté ne suffit pas pour valoriser une entreprise distressed ?"

**Réponse modèle (75 sec)** :
> "Parce qu'en distressed, l'EBITDA reporté contient énormément de **bruit** qui ne reflète pas la profitabilité réelle reproductible. Trois grandes catégories de bruit. **Premièrement**, des **charges non récurrentes** liées à la crise elle-même : honoraires d'avocats, frais d'AJ, indemnités de litiges, sinistres ponctuels — qui peuvent peser 50 à 200 k€ sur un PME et qu'un repreneur ne reverra plus. **Deuxièmement**, des **éléments non normatifs** liés au dirigeant familial : sur-rémunération, loyers payés à une SCI familiale au-dessus du marché, voitures de luxe, voyages perso, conjoint sur-rémunéré. C'est très fréquent en PME française et ça peut représenter 100 à 300 k€/an de charges qu'un repreneur professionnel coupera immédiatement. **Troisièmement**, des **provisions sous-évaluées** : stocks dormants non dépréciés, créances douteuses non provisionnées, indemnités de fin de carrière sous-dotées. Ces trois catégories combinées peuvent faire passer un EBITDA reporté de 200 k€ à un EBITDA normalisé de 500 ou 600 k€. C'est le delta sur lequel on valorise la cible — pas le chiffre comptable affiché."

## À retenir absolument
- EBITDA normalisé = EBITDA retraité du non-récurrent, non-opérationnel, non-normatif
- 10 retraitements clés : rémunération, loyer, charges except., procédure, etc.
- Faire les retraitements dans les **deux sens** (positifs et négatifs)
- Ne pas confondre avec synergies (= effet intégration)
- Décote distressed sur multiple : -30 à -50 %
- Valoriser sur EBITDA normalisé, pas sur EBITDA reporté

## Related
- [[brantham/mastery/finance/_MOC]]
- [[brantham/mastery/finance/02-compte-resultat-distressed]]
- [[brantham/mastery/finance/05-multiples-valorisation]]
- [[brantham/knowledge/finance/valorisation-distressed]]
