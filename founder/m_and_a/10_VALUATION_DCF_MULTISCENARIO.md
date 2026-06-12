---
name: DCF Valuation 3-Scenario Model
description: Multi-scenario DCF (conservative/base/aggressive) with sensitivity analysis for M&A deal pricing
type: template
created: 2026-06-13
---

# DCF Valuation — 3-Scenario Model

## Key Assumptions (Fill In)

| Metric | Value | Source |
|--------|-------|--------|
| **Revenue (LTM)** | €XXX,XXX | Financials |
| **EBITDA Margin (current)** | X% | Audited |
| **Revenue Growth (Y1-5)** | X% | Guidance / Market |
| **Terminal Growth Rate** | 2.5% | Conservative |
| **WACC** | X% | 8-12% typical |
| **Tax Rate** | X% | Effective rate |
| **CapEx / Revenue** | X% | Industry avg |
| **NWC / Revenue** | X% | Historical |

---

## Scenario Model (5-Year DCF)

### **SCENARIO A: Conservative**
- Revenue growth: Y1-3 at **4%**, Y4-5 at **2%**
- EBITDA margin: **-50 bps** vs. current (customer churn risk)
- Capex: 5% of revenue
- NWC increase: 2% of revenue growth
- WACC: **10%**

| Year | Revenue | EBITDA | NOPAT | FCF | PV Factor | PV FCF |
|------|---------|--------|-------|-----|-----------|--------|
| 1 | € | € | € | € | 0.909 | € |
| 2 | € | € | € | € | 0.826 | € |
| 3 | € | € | € | € | 0.751 | € |
| 4 | € | € | € | € | 0.683 | € |
| 5 | € | € | € | € | 0.621 | € |
| **Total PV (Years 1-5)** | — | — | — | — | — | **€** |
| **Terminal Value** | — | — | — | — | 0.621 | **€** |
| **Enterprise Value (Conservative)** | — | — | — | — | — | **€** |

**Conservative Multiple:** {{ EV / LTM EBITDA }} x EBITDA

---

### **SCENARIO B: Base Case**
- Revenue growth: Y1-3 at **8%**, Y4-5 at **5%**
- EBITDA margin: **Flat** vs. current (operating leverage)
- Capex: 4% of revenue
- NWC increase: 1.5% of revenue growth
- WACC: **9%**

| Year | Revenue | EBITDA | NOPAT | FCF | PV Factor | PV FCF |
|------|---------|--------|-------|-----|-----------|--------|
| 1 | € | € | € | € | 0.917 | € |
| 2 | € | € | € | € | 0.842 | € |
| 3 | € | € | € | € | 0.772 | € |
| 4 | € | € | € | € | 0.708 | € |
| 5 | € | € | € | € | 0.649 | € |
| **Total PV (Years 1-5)** | — | — | — | — | — | **€** |
| **Terminal Value** | — | — | — | — | 0.649 | **€** |
| **Enterprise Value (Base Case)** | — | — | — | — | — | **€** |

**Base Multiple:** {{ EV / LTM EBITDA }} x EBITDA

---

### **SCENARIO C: Aggressive**
- Revenue growth: Y1-3 at **12%**, Y4-5 at **8%**
- EBITDA margin: **+100 bps** vs. current (scale, synergies)
- Capex: 3% of revenue
- NWC: Flat (strong cash conversion)
- WACC: **8%**

| Year | Revenue | EBITDA | NOPAT | FCF | PV Factor | PV FCF |
|------|---------|--------|-------|-----|-----------|--------|
| 1 | € | € | € | € | 0.926 | € |
| 2 | € | € | € | € | 0.857 | € |
| 3 | € | € | € | € | 0.794 | € |
| 4 | € | € | € | € | 0.735 | € |
| 5 | € | € | € | € | 0.681 | € |
| **Total PV (Years 1-5)** | — | — | — | — | — | **€** |
| **Terminal Value** | — | — | — | — | 0.681 | **€** |
| **Enterprise Value (Aggressive)** | — | — | — | — | — | **€** |

**Aggressive Multiple:** {{ EV / LTM EBITDA }} x EBITDA

---

## Valuation Range Summary

| Scenario | Enterprise Value | EV/EBITDA | $/Revenue |
|----------|------------------|-----------|-----------|
| **Conservative** | **€ XXX** | **X.Xx** | **X.Xx** |
| **Base Case** | **€ XXX** | **X.Xx** | **X.Xx** |
| **Aggressive** | **€ XXX** | **X.Xx** | **X.Xx** |
| **Average** | **€ XXX** | **X.Xx** | **X.Xx** |

### Recommended Asking Price Range
- **Floor (walk-away):** Conservative scenario
- **Target (realistic):** Base case + 10% = **€ XXX**
- **Ceiling (aspirational):** Aggressive scenario
- **Accept range:** Base ± 15% = **€ XXX - € XXX**

---

## Sensitivity Analysis

### Revenue Growth (±2pp impact on EV)

| Growth ↓ | Conservative | Base Case | Aggressive |
|----------|--------------|-----------|------------|
| 6% | € | € | € |
| 8% | € | € | € |
| 10% | € | € | € |
| 12% | € | € | € |

### WACC (±1pp impact on EV)

| WACC | PV Impact | Valuation |
|------|-----------|-----------|
| 7% | +12% | € |
| 8% | +5% | € |
| 9% | Base | € |
| 10% | -8% | € |
| 11% | -15% | € |

### EBITDA Margin (±100bp impact on FCF)

| Margin | Revenue Base | EBITDA | EV Impact |
|--------|--------------|--------|-----------|
| -1% | € | € | -8% |
| Current | € | € | Base |
| +1% | € | € | +9% |

---

## Use in Negotiation

### Pricing Framework
- **Initial Ask:** Aggressive scenario (€ XXX)
  - *Justification:* "Based on market synergies + LTV expansion we can achieve"
- **Rationale:** Base case + strategic premium (15-20%)
- **Walk-Away:** Conservative scenario (€ XXX)
  - *Trigger:* "Below this, we reject and remain independent"

### If Buyer Pushes Back
- Show conservative scenario first → demonstrates downside protection
- Reveal base case as "reasonable middle ground"
- Show aggressive scenario last → "upside for both parties"
- Stress-test WACC assumption (most sensitive lever)

### Earnout Negotiation
- **Upside target:** Aggressive - Base = **€ XXX**
- **Earnout structure:** Up to 20% of upside IF hitting YoY revenue target (e.g., 10% CAGR)
- **KPI:** Annual revenue @ threshold (e.g., €YYY by Year 2)

---

## Comparable Transactions

| Company | Revenue | EBITDA | EV | EV/Revenue | EV/EBITDA | Sector |
|---------|---------|--------|----|----|-----------|--------|
| Comp 1 | € | € | € | X.Xx | X.Xx | |
| Comp 2 | € | € | € | X.Xx | X.Xx | |
| Comp 3 | € | € | € | X.Xx | X.Xx | |
| **Your Co (Base)** | € | € | € | **X.Xx** | **X.Xx** | |

**Market Median Multiple:** X.Xx x EBITDA (Premium/Discount: ±X%)

---

## Notes

- DCF assumes no major M&A / capex beyond normal ops
- Terminal value assumes 2.5% perpetual growth (conservative)
- Earnout component can bridge gap between buyer/seller valuations
- Update quarterly as guidance / actuals change
- WACC = Rf + β(Rm - Rf) + Credit spread; adjust for business-specific risk
