---
name: template_term_sheet
description: Term Sheet pour deal SaaS — valeurs clés, earnout, holdback, closing
metadata:
  type: reference
  format: financial_template
  version: 1.0
---

# Term Sheet — Deal Structure

**Vendeur :** [NOM] | **Acheteur :** [NOM] | **Date :** [JJ/MM/YYYY]

---

## **PRICING & STRUCTURE**

| Paramètre | Valeur |
|-----------|--------|
| **Enterprise Value (EV)** | €[X] |
| **Multiple** | [2.5x-4.5x] × ARR / [5x-8x] × EBITDA |
| **Base de calcul** | ARR [année N] : €[Y] |
| **Ajustements** | ± NWC (voir ci-dessous) |

---

## **PAIEMENT AU CLOSING**

```
Enterprise Value                    €[X.XXX]
- Dettes nettes                     €[(X)]
- Impôts à verser (DD)              €[(X)]
= Equity Value                      €[X.XXX]

Répartition Vendeur :
├─ Paiement cash closing            €[X] (60-70% usual)
├─ Holdback escrow                  €[X] (10-15%, 18 mois)
└─ Earnout contingent               €[X] (15-30%, voir supra)
```

---

## **EARNOUT (si applicable)**

**Trigger :** Rétention clients + croissance ARR

| Année | Métrique | Target | Payout si atteint |
|-------|----------|--------|-------------------|
| **Y1** | Client retention ≥ 85% | €[X] | €[Y] |
| **Y2** | ARR growth ≥ 10% | €[X] | €[Y] |
| **Y3** | Churn ≤ [X%] | €[X] | €[Y] |

*Vérification Q aux closing + 3/6/12/18 mois. Acheteur ne peut pas tuer clients volontairement pour réduire earnout.*

---

## **HOLDBACK (Escrow)**

- **Montant** : 10-15% de closing cash
- **Durée** : 18 mois post-closing
- **Motif** : Garantir reps & warranties, tax compliance
- **Libération** : 50% @ 12m, 50% @ 18m si aucune réclamation

---

## **NET WORKING CAPITAL (NWC) ADJUSTMENT**

```
Closing NWC Target    : €[X]
Actual NWC @ closing  : €[Y]
Variance              : €[(Y-X)]

Si positive → acheteur paie supplément
Si négative → vendeur paie rabais
```

---

## **REPS & WARRANTIES**

### Vendeur garantit :

1. **Titularité** — Propriété IP propre, pas de droits tiers
2. **Contrats clients** — Aucun changement-de-contrôle killer
3. **Employés** — Aucun accord non-disclosed, pas de compétition
4. **Finances** — Chiffres audités conformes (+/-5%)
5. **Taxes** — Déclarations et paiements à jour
6. **Contentieux** — Pas de litiges connus/matériels

**Durée** : 18 mois (sauf taxes : 3-6 ans per local law)

---

## **CONDITIONS PRÉCÉDENTES AU CLOSING**

- ✓ Due diligence complétée, pas de red flags matériels
- ✓ Financement en place (si acheteur)
- ✓ Approvals de clients clés ([%] ARR signent MOU)
- ✓ Employés clés signent retention agreement
- ✓ Aucun changement matériel post-LOI (MACA)

---

## **CALENDRIER**

```
[D0]       LOI signé
[D0+10j]   Data room ouvert, DD commence
[D0+35j]   Term sheet finalisé
[D0+60j]   SPA préparé, signatures amorces
[D0+90j]   Closing financier + transition
```

---

## **FRAIS**

- Chaque partie paie ses frais légal/audit
- Ou : acheteur paie tous les frais (courtage)
- Holdback peut couvrir frais non-prévus

---

**Notes :**
- Multiple SaaS-type : 3–5x ARR (selon croissance/churn)
- Earnout max 20-30% (sinon risque de méfiance)
- Rétention client est clé : structure earnout autour
- Réserver crédit fiscal/tax loss carryforward à négocier
## Related
## Related
## Related
