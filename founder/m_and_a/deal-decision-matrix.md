---
name: deal-decision-matrix
description: Buy/Build/Partner decision matrix avec critères de scoring et taille de deal
metadata:
  type: reference
---

# Deal Decision Matrix — Buy vs Build vs Partner

## Matrice de Décision (5 critères)

| Critère | BUY (Acquisition) | BUILD (Interne) | PARTNER (Intégration) |
|---------|------------------|-----------------|----------------------|
| **Temps au marché** | 3-6 mois | 12-24 mois | 2-3 mois |
| **Coût initial** | $M-$100M | $0.5-5M/an | $0-2M |
| **Risque d'exécution** | Moyen (intégration) | Haut (recrutement, R&D) | Bas (partenaire responsable) |
| **Contrôle IP/Tech** | 100% | 100% | Partiel (contrat) |
| **Risque de marché** | Bas (produit validé) | Moyen (pivot possible) | Haut (dépend du partenaire) |

---

## Deal Scoring Simple (0-100)

**Score = (Time_fit × 0.25) + (Cost_fit × 0.25) + (Tech_fit × 0.25) + (Team_fit × 0.25)**

### Time Fit (0-25)
- 25: Must-have en < 3 mois
- 15-20: Important, délai 6-12 mois
- 5-10: Nice-to-have, pas urgent
- 0: Peut attendre 24+ mois

### Cost Fit (0-25)
- 25: < $5M (1-2x ARR)
- 20: $5-15M (2-4x ARR)
- 10: $15-50M (4-10x ARR)
- 0: > $50M (> 10x ARR)

### Tech/Product Fit (0-25)
- 25: Complète l'offre core, zéro overlap
- 20: Renforce capability existante
- 10: Adjacent, partiellement utile
- 0: Hors stratégie, risqué

### Team Fit (0-25)
- 25: Founders/leads restent, culture alignée
- 20: Talent clé reste, intégration facile
- 10: Équipe partielle disponible
- 0: Turnover certain, culture clash

---

## Buy/Build/Partner : Guide Rapide

| Scénario | Recommandation | Exemple |
|----------|---|---|
| Score > 75 + Must-have feature | **BUY** | Acquisition d'une API de paiement si c'est critique |
| Score < 50 + Nice-to-have | **BUILD** interne | Faire soi-même une feature secondaire |
| Score 50-70 + Partenaire solide | **PARTNER** | Intégrer Stripe, Twilio, Datadog |
| Partenaire non aligné long-terme | **BUY** quand même | Acquérir plutôt que de dépendre |

---

## Taille de Deal : Classification

- **Micro-deal** : < $5M (< 1 FTE intégration)
- **Small** : $5-20M (1-2 months integration)
- **Mid-market** : $20-100M (full-time project manager)
- **Large** : $100M+ (steering committee, C-level time)

---

## Prochaines Étapes

1. Mapper les capabilities manquantes de votre roadmap 2026
2. Noter chaque capability sur la matrice (30 min)
3. Ranger par score : BUY candidates > PARTNER options > BUILD internally
4. Approuver avec leadership avant outreach
