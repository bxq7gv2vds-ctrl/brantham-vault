# Buyer Scoring Sheet — Qualification des Acquéreurs

**Objectif :** Matrix pour scorer acheteurs potentiels sur synergies, financement, timeline, et risques.

---

## Template de notation (à copier en Excel ou Google Sheets)

| Nom Acquéreur | Type | ARR Cible | Strategic Fit (1-5) | Financial Fit (1-5) | Cultural Fit (1-5) | Timeline (mois) | Risk Score (1-5) | **Global Score** | Notes |
|---|---|---|---|---|---|---|---|---|---|
| ACME Corp | Strategic | $2-5M | 5 | 4 | 3 | 3-4 | 2 | **4.2** | Fort overlap produit. Peut financer. |
| Axiom PE | PE Firm | Any | 3 | 5 | 2 | 6-9 | 4 | **3.8** | Rapide fermeture. Dû diligence lourde. |
| TechBridge Inc | Marché adjacent | $1-3M | 4 | 3 | 4 | 4-5 | 2 | **3.6** | Croissance compatible. Culture proche. |
| XYZ Consolidator | Consolidateur | $0.5-10M | 2 | 5 | 1 | 8-12 | 5 | **2.6** | Peu de synergies. Lenteur politique. |

---

## Guide de notation détaillé

### Strategic Fit (1–5)
- **5** : Produit directement complémentaire; clients overlap; roadmap alignée
- **4** : Bonne synérgie; cross-sell possible; peu de friction
- **3** : Fit acceptable; quelques synergies; pas évident
- **2** : Marginal; acquisition pour talent ou IP seul
- **1** : Aucune synérgie; candidat faible

**Exemples :**
- Slack + Salesforce = 5 (intégration native, même marché)
- Figma + Adobe = 4 (design tool, complémentaire)

### Financial Fit (1–5)
- **5** : Acquéreur dispose cash/crédit pour 2x+ notre valuation
- **4** : Peut financer 1.5-2x sans contrainte
- **3** : Financement possible mais non trivial
- **2** : Besoin earnout ou seller financing
- **1** : Aucune capacité connue

**À vérifier :**
- Liquidity récente (IPO, levée, free cash flow)
- Historique acquisition (taille, pricing)
- Dry powder de PE si applicable

### Cultural Fit (1–5)
- **5** : Culture très proche; founder heureux de rester; pas de churn talent
- **4** : Bonne compatibilité; some founders resteraient
- **3** : Acceptable; quelques frictions attendues
- **2** : Problèmes culturels visibles; talent risk
- **1** : Culture incompatible; team quittera

**Red flags :**
- Acquéreur a track record de founder exodus post-close
- Différences produit/go-to-market fondamentales
- Valeurs opposées (ex: open-source vs proprietary)

### Timeline (mois)
- **3-4** : Strategic + urgent (rare)
- **4-6** : Timeline normal (sweet spot)
- **6-9** : Processus de PE standard
- **9-12+** : Lenteurs politiques ou bureaucratiques

### Risk Score (1–5)
- **1** : Très peu de risques; processus clair; track record positif
- **2** : Risques mineurs; solvabilité confirmée
- **3** : Quelques red flags; DD peut révéler problèmes
- **4** : Risques significatifs (instabilité financière, litigation, churn)
- **5** : Très haut risque; pas recommandé

**Exemples de risques :**
- Acquéreur est lui-même en acquisition (instabilité)
- Founder team a quitté post-close (mauvais sign)
- Rumeurs de financial distress
- Procès en cours

### Global Score (moyenne simple)
```
Score = (Strategic + Financial + Cultural + (5 - Risk)) / 4
```

**Interprétation :**
- **4.5–5.0** : Candidat A-tier (poursuivre)
- **3.5–4.5** : Candidat B-tier (maintenir en pipeline)
- **2.5–3.5** : Candidat C-tier (option de repli)
- **<2.5** : Ne pas poursuivre (effort > gain)

---

## Workflow d'utilisation

1. **Brainstorm** : Lister 20-30 acquéreurs potentiels (top-down par segment)
2. **Research** : Crunchbase, SEC filings, Pitchbook, LinkedIn
3. **Score** : Remplir pour chaque (15 min par ligne)
4. **Pivot** : Garder top 10-15 (score > 3.0)
5. **Warm intro** : Chercher introduction via LinkedIn / common investors
6. **First call** : Utiliser template prospect email
7. **Update** : Baisser score si rejets ou bad signals

---

## Exemple — Pipeline réelle

| Nom | Type | Strategic | Financial | Cultural | Timeline | Risk | **Score** | Status |
|---|---|---|---|---|---|---|---|---|
| Acquireur A | Strategic | 5 | 4 | 4 | 4 | 2 | **4.3** | 🟢 Active |
| Acquireur B | Strategic | 4 | 4 | 3 | 5 | 3 | **3.8** | 🟢 Active |
| PE Firm C | PE | 3 | 5 | 2 | 8 | 3 | **3.4** | 🟡 Backlog |
| Consolidator D | Consolidator | 2 | 5 | 1 | 10 | 5 | **2.4** | 🔴 Pass |
| Adjacent E | Adjacent | 4 | 3 | 4 | 6 | 2 | **3.8** | 🟢 Active |

---

## Red flags à surveiller

- ❌ Acquireur demande révélation complète financière **avant** NDA
- ❌ Pas de réponse à emails pour 2+ semaines
- ❌ DD demande excessive de temps/documents pré-LOI
- ❌ Founder qui a exité d'un deal antérieur avec lui en dit peu bien
- ❌ Competitor qui cherche juste à saboter (due diligence theatre)

---

Créé : 2026-06-13 | Format: Markdown (copy/paste en Excel/Google Sheets)
