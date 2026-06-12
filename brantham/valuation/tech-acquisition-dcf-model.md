---
name: dcf-tech-acquisition-model
description: Modèle de valorisation DCF rapide pour acquisition tech
type: pattern
date: 2026-06-12
---

# Modèle de Valorisation DCF - Acquisition Tech

**Usage** : Évaluation rapide en 30 minutes pour screening préliminaire  
**Précision** : ±15% pour prise de décision initiale  
**Format** : Calculateur Excel/Google Sheets compatible

---

## 🎯 Vue d'ensemble du Modèle

### Hypothèses Clés (Modifiables)
- **Période de projection** : 5 ans
- **Croissance terminal** : 3% (défaut = croissance long terme)
- **Taux d'actualisation** : 12-15% (risque tech = +prime)
- **Tax rate** : 21% (US corporate tax)

### Métriques d'Entrée
```
Current Revenue: $[montant]
Revenue Growth: [pourcentage]%
Gross Margin: [pourcentage]%
Operating Margin: [pourcentage]%
Working Capital %: [pourcentage]%
```

---

## 📊 Calcul DCF Simplifié

### Étape 1 : Projections de Flux de Trésorerie

| Année | Revenue | Op. Income | Capex | ΔWorking Capital | FCF |
|-------|---------|------------|-------|------------------|-----|
| **Year 1** | $[R1] | $[OI1] | $[C1] | $[WC1] | $[FCF1] |
| **Year 2** | $[R2] | $[OI2] | $[C2] | $[WC2] | $[FCF2] |
| **Year 3** | $[R3] | $[OI3] | $[C3] | $[WC3] | $[FCF3] |
| **Year 4** | $[R4] | $[OI4] | $[C4] | $[WC4] | $[FCF4] |
| **Year 5** | $[R5] | $[OI5] | $[C5] | $[WC5] | $[FCF5] |
| **Terminal** | - | - | - | - | $[Terminal] |

### Formules Clés
```
Revenue Growth = [croissance]%
FCF = Operating Income × (1 - Tax Rate) - Capex - ΔWorking Capital
Terminal Value = Year 5 FCF × (1 + Terminal Growth) / (Discount Rate - Terminal Growth)
Enterprise Value = PV(FCF Years 1-5) + PV(Terminal Value)
```

---

## 🔄 Méthodes de Comparaison

### Multiples Sectoriels SaaS
| Multiple | Valeur Typique | Application |
|----------|----------------|-------------|
| **Revenue Multiple** | 6-8x récurrent | Early stage |
| **EBITDA Multiple** | 12-18x | Growth stage |
| **User Multiple** | $200-500/user | Marketplaces |
| **ARPA Multiple** | 8-12x × ARPA | SaaS pure |

### Peer Group Comparaison
```markdown
- **SaaS Growth**: [Nom] - [multiple]x EV/Revenue
- **SaaS Enterprise**: [Nom] - [multiple]x EV/Revenue  
- **Marketplace**: [Nom] - [multiple]x GMV
- **Average**: [multiple]x EV/Revenue
```

---

## 📈 Analyse de Sensibilité

### Scénarios Base
- **Base Case** : Croissance [croissance]%, margin [margin]%
- **Upside** : +20% growth, +5% margin
- **Downside** : -10% growth, -3% margin

### Sensibilité Clés
| Taux d'actualisation | Valeur | Sensibilité |
|----------------------|--------|--------------|
| **12%** | $[V1] | +[pourcentage]% |
| **14%** (base) | $[V2] | - |
| **16%** | $[V3] | -[pourcentage]% |

---

## 🎛️ Facteurs de Correction

### Green Factors (+ valeur)
- [ ] **Tech moat** : +[pourcentage]%
- [ ] **Revenue quality** : Récurrent >80% → +[pourcentage]%
- [ ] **Team strength** : Key hires retained → +[pourcentage]%
- [ ] **Market position** : Leader → +[pourcentage]%

### Risk Factors (- valeur)
- [ ] **Customer concentration** : >20% from one client → -[pourcentage]%
- [ ] **Tech debt** : >30% maintenance → -[pourcentage]%
- [ ] **Competition** : Intense competition → -[pourcentage]%
- [ ] **Regulatory** : Changing rules → -[pourcentage]%

---

## 📊 Évaluation Finale

### Valeur Calculée
- **DCF Enterprise Value** : $[montant]
- **Less Net Debt** : -$[montant]
- **Equity Value** : $[montant]

### Prix d'Acquisition Suggéré
- **Range Basse** : $[montant] ([multiple]x revenue)
- **Prix Cible** : $[montant] ([multiple]x revenue)  
- **Range Haute** : $[montant] ([multiple]x revenue)

### Indicateurs de Risque
- **Risk Score** : [échelle 1-5]
- **Confidence Level** : [pourcentage]%
- **Key Assumptions** : [liste des 3 plus importants]

---

## 🚀 Quick Wins Checklist

Pour validation rapide :
- [ ] **Revenue visibility** : Contrats signés >80% next 12 months
- [ ] **Unit economics** : LTV/CAC >3x, churn <5%
- [ ] **Cash burn** : Runway >18 months
- [ ] **Team** : No key person dependency
- [ ] **Tech** : Scalable architecture, no single points of failure

---

## 📋 Template Excel/Google Sheet

```excel
# Section 1: Inputs
A1: "Current Revenue", B1: [montant]
A2: "Revenue Growth %", B2: [pourcentage]  
A3: "Gross Margin %", B3: [pourcentage]
A4: "Op Margin %", B4: [pourcentage]
A5: "Capex %", B5: [pourcentage]
A6: "Working Capital %", B6: [pourcentage]
A7: "Discount Rate %", B7: 14
A8: "Terminal Growth %", B8: 3

# Section 2: Calculations
A10: "Year 1 Revenue", B10: =B1*(1+B2)
A11: "Year 2 Revenue", B11: =B10*(1+B2)
... (extend to Year 5)

A20: "Year 1 FCF", B20: =(B4*B10)*(1-0.21)-B5*B10-B6*(B10-B1)
A21: "Year 2 FCF", B21: ... (formula)
... 
A25: "Terminal Value", B25: =B24*(1+B8)/(B7/100-B8/100)

A27: "PV FCF Years 1-5", B27: =NPV(B7/100, B20:B24)
A28: "PV Terminal Value", B28: =B25/(1+B7/100)^5
A29: "Enterprise Value", B29: =B27+B28
A30: "Net Debt", B30: [montant]  
A31: "Equity Value", B31: =B29-B30
```

---

## Related
[[_system/MOC-patterns]]
[[brantham/_MOC]]
[[brantham/valuation/comparable-company-analysis]]
[[brantham/deals/acquisition-workflow]]