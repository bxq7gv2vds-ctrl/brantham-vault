---
name: Recalibration modele BeSoft post-T1 test
description: Corrections au modele de demande et financier apres observation du T1 test live. Elasticite confirmee 85u/EUR (+0.4% erreur). Storage=0, impot meme periode, MLT interest T2+.
type: decision
---

# Decision: Recalibration modele BeSoft

## Contexte
T1 test joue le 23/03/2026. Resultats disponibles. Modele valide a +0.4% sur la demande.

## Corrections appliquees

### 1. Base demand: 3,300 → 3,340
- Marche total T1: 17,869 / 5 firmes / 1.07 seasonal = 3,340
- Ecart: +1.2% vs ancien 3,300

### 2. Storage costs: actifs → desactives T1-T2
- BeSoft montre 0 en storage costs a T1
- Le manuel dit "pas de frais de stockage au debut"
- A reactiver quand BeSoft commence a les facturer (probablement T3+)

### 3. Impot: reporte → meme periode
- Le P&L et la tresorerie montrent l'IS paye dans le meme trimestre
- Impact: ~11K de cash en moins par rapport a la prediction

### 4. MLT interest: T1 → T2+
- Les frais financiers T1 = 2,700 = hypotheque seule
- Le MLT de 120K n'est pas facture en T1
- Commence en T2 (remboursement sur 6 trims: T2-T7)

### 5. Taux de base: 2%/trim → 1.25%/trim (5% annuel)
- MLT: 2.25%/trim (pas 3%)
- CT: 4.25%/trim (pas 5%)
- Decouvert: 5%/trim (pas 8%)

### 6. Machine F necessaire en T3
- Sans machine: rupture de stock en T5-T6 (marche +41% vs T4)
- Decision: acheter 1 machine F en T3 (77,760 EUR, 10 trims ROI)
- Ajuster MP a 8,000/livraison × 4 a partir de T3

## Alternatives considerees
- Pas de machine: rupture T5-T6, perte de CA estimee 100K+
- Machine en T1: cash trop serre (67K)
- Machine en T2: possible mais pas confirme par les donnees live

## Impact
- Projections NI plus precises (erreur <5% vs <20% avant)
- Cash flow fiable (impot + storage + MLT corriges)
- Plan d'investissement machine cale sur le boom T5-T6

## Related
- [[_system/MOC-decisions]]
- [[_system/MOC-master]]
- [[brantham/sessions/2026-03-23-polytech-competition]]
- [[founder/strategy/current-strategy]]
