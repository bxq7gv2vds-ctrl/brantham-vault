# Valuation DCF — Template & Scenarios

**Utilité** : calcul d'enterprise value par approche flux de trésorerie actualisés (DCF).

## Inputs (5 ans forward forecast)

```
Year 1–5 Revenue forecast:
  - ARR croissance (%)
  - Gross margin (%)
  - EBITDA margin % (opex scaling)
  → Free cash flow = EBITDA − CapEx − tax − NWC change

Terminal year assumptions:
  - Perpetual growth rate g = 2–3% (ne pas > GDP growth)
  - Terminal EBITDA margin (mature-state)
  - Terminal CapEx/revenue
```

## Calculation

```
FCF Year N = (Revenue × EBITDA%) − Tax − CapEx − ∆NWC

Terminal Value (Perpetuity Growth) = FCF(Y5) × (1 + g) / (WACC − g)

Enterprise Value = Σ [FCF(Y1–Y5) / (1+WACC)^n] + TV / (1+WACC)^5

where WACC = Weighted Average Cost of Capital
  = (E/V × Re) + (D/V × Rd × (1 − Tc))
  
  Re = risk-free rate (3%) + beta (1.5–2.0 for SaaS) × market risk premium (5%)
     ≈ 10–13% for private SaaS
  Rd = cost of debt (5–7%)
  E/V = equity value weight, D/V = debt weight
```

## Scenarios (Base / Bull / Bear)

| Scenario | Y1 Growth | Terminal EBITDA% | WACC | Enterprise Value |
|----------|-----------|------------------|------|------------------|
| **Bear** | 15%       | 15%              | 14%  | 3.2× ARR         |
| **Base** | 25%       | 25%              | 12%  | 5.5× ARR         |
| **Bull** | 40%       | 30%              | 11%  | 8.2× ARR         |

---

## SaaS Shortcut (Règle des multiples)

```
Enterprise Value ≈ ARR × Multiple

Multiple drivers:
  - Growth rate: 40% growth → 7–9× multiple
  - Net Retention: >110% → +20% multiple
  - Churn <5%/an → +15% multiple
  - Customer concentration: >40% from top 5 → −25% multiple
  - Debt/CapEx heavy → discount WACC by +1–2%
```

**Benchmark SaaS B2B (2024):**
- Early stage ($1–5M ARR, 50%+ growth): 6–10× ARR
- Growth ($5–50M ARR, 30–50% growth): 5–8× ARR
- Mature ($50M+ ARR, <30% growth): 2–5× ARR

---

## Sensitivity Analysis

```
     WACC →
     ↓ Terminal g    11%      12%      13%
     2%            6.8×     5.5×     4.6×
     2.5%          7.5×     6.0×     5.0×
     3%            8.3×     6.5×     5.4×
```

**Levers sensibles** : growth rate (−5% → −30% EV), terminal margin (−5% → −20% EV).

---

**Usage** : 
- DCF = plancher (conservative)
- Comps = références marché
- Transaction = réalité (ce que buyer paie) = DCF × synergy uplift
