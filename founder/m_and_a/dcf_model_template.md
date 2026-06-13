---
name: dcf_model_template
description: Discounted Cash Flow 3-scenarios (conservative/base/bull) pour valuation
metadata:
  type: template
  created: 2026-06-12
---

# DCF Model — 3-Scenario Valuation (Conservative / Base / Bull)

**Quick version:** Build in Excel, test 3 growth scenarios, discount back to today

---

## **Inputs (Fill These In)**

### **Year 0 Financials (TTM = Trailing Twelve Months)**

```
Current Year Revenue (ARR):           $_____ (e.g., $500k)
Current Year EBITDA:                  $_____ (e.g., $75k = 15%)
Growth Rate (next 3 years):           ___% (e.g., 50% YoY)
Terminal Growth Rate:                 ___% (e.g., 3%, inflation)
WACC (Discount Rate):                 ___% (e.g., 12%, typical SaaS)
Forecast Period:                      _____ years (e.g., 5 years)
Tax Rate:                             ___% (e.g., 21% federal)
```

### **Growth Assumptions (Adjust per scenario)**

| Year | Conservative | Base Case | Bull Case |
|-----|---|---|---|
| 0 (Current) | $500k | $500k | $500k |
| 1 | $600k (20%) | $750k (50%) | $900k (80%) |
| 2 | $720k (20%) | $1,125k (50%) | $1,620k (80%) |
| 3 | $864k (20%) | $1,688k (50%) | $2,916k (80%) |
| 4 | $1,037k (20%) | $2,531k (50%) | $5,249k (80%) |
| 5 | $1,244k (20%) | $3,796k (50%) | $9,448k (80%) |

---

## **DCF Calculation (Year-by-Year)**

### **Conservative Scenario (Low Growth)**

| Year | Revenue | EBITDA Margin | EBITDA | Tax Rate | NOPAT | + D&A | - CapEx | = FCF | Discount @ 12% | PV of FCF |
|-----|---------|---|---|---|---|---|---|---|---|---|
| 1 | $600k | 12% | $72k | 21% | $56.9k | $10k | $(15k) | $51.9k | 0.893 | $46.3k |
| 2 | $720k | 13% | $93.6k | 21% | $74.0k | $10k | $(15k) | $69.0k | 0.797 | $55.0k |
| 3 | $864k | 14% | $121k | 21% | $95.8k | $10k | $(15k) | $90.8k | 0.712 | $64.6k |
| 4 | $1,037k | 15% | $155.5k | 21% | $123k | $10k | $(20k) | $113k | 0.636 | $71.9k |
| 5 | $1,244k | 15% | $186.6k | 21% | $147.6k | $10k | $(20k) | $137.6k | 0.567 | $78.0k |

**Terminal Value** (Year 5 perpetuity growth at 3%):
```
Terminal Value = FCF(Y5) × (1 + g) / (WACC - g)
               = $137.6k × 1.03 / (0.12 - 0.03)
               = $1,574k

PV of Terminal Value = $1,574k × 0.567 = $892k
```

**Sum of PV of FCFs (Years 1-5):** $315.8k
**+ PV of Terminal Value:** $892k
**= Enterprise Value (Conservative):** **$1,207.8k ≈ $1.2M**

---

### **Base Case (Medium Growth)**

| Year | Revenue | EBITDA % | EBITDA | NOPAT | D&A | CapEx | FCF | Discount | PV |
|-----|---|---|---|---|---|---|---|---|---|
| 1 | $750k | 15% | $112.5k | $89k | $12k | $(20k) | $81k | 0.893 | $72.3k |
| 2 | $1,125k | 18% | $202.5k | $160k | $15k | $(30k) | $145k | 0.797 | $115.6k |
| 3 | $1,688k | 22% | $371k | $293k | $20k | $(40k) | $273k | 0.712 | $194.4k |
| 4 | $2,531k | 25% | $633k | $501k | $25k | $(50k) | $476k | 0.636 | $303k |
| 5 | $3,796k | 28% | $1,063k | $841k | $30k | $(60k) | $811k | 0.567 | $459.6k |

**Terminal Value:**
```
$811k × 1.03 / 0.09 = $9,256k
PV = $9,256k × 0.567 = $5,248k
```

**Sum of PVs:** $1,145k
**+ Terminal:** $5,248k
**= EV (Base Case):** **$6,393k ≈ $6.4M**

---

### **Bull Case (High Growth)**

| Year | Revenue | EBITDA % | EBITDA | NOPAT | D&A | CapEx | FCF | Discount | PV |
|-----|---|---|---|---|---|---|---|---|---|
| 1 | $900k | 12% | $108k | $85k | $14k | $(25k) | $74k | 0.893 | $66.1k |
| 2 | $1,620k | 18% | $291.6k | $230k | $18k | $(35k) | $213k | 0.797 | $169.8k |
| 3 | $2,916k | 24% | $700k | $553k | $25k | $(50k) | $528k | 0.712 | $376k |
| 4 | $5,249k | 30% | $1,575k | $1,246k | $35k | $(80k) | $1,201k | 0.636 | $764k |
| 5 | $9,448k | 32% | $3,023k | $2,392k | $45k | $(120k) | $2,317k | 0.567 | $1,313k |

**Terminal Value:**
```
$2,317k × 1.03 / 0.09 = $26,528k
PV = $26,528k × 0.567 = $15,043k
```

**Sum of PVs:** $2,689k
**+ Terminal:** $15,043k
**= EV (Bull Case):** **$17,732k ≈ $17.7M**

---

## **Valuation Summary**

| Scenario | Enterprise Value | Per $1 ARR | Implied Multiple |
|---|---|---|---|
| **Conservative (20% CAGR)** | $1.2M | $2,400 | **2.4x ARR** |
| **Base Case (50% CAGR)** | $6.4M | $12,800 | **12.8x ARR** |
| **Bull Case (80% CAGR)** | $17.7M | $35,400 | **35.4x ARR** |

**SaaS Benchmarks (compare):**
- Growth <20%: 3-5x ARR
- Growth 20-50%: 8-12x ARR
- Growth 50%+: 12-20x ARR
- Exceptional (>80%): 20-35x ARR

---

## **Buyer Perspective**

Typical buyer uses:
1. **DCF** (your foundation) = **$6.4M** (base)
2. **Comps** (market multiples) = **$8.5M** (8x ARR × $1.06M ARR) — gives range
3. **Precedent** (past similar deals) = **$5.8M**
4. Weighted average: 40% DCF + 30% Comps + 30% Precedent = **$7.3M**

**Your ask:** DCF base case ($6.4M)
**Buyer offer:** Conservative case ($1.2M) + upside earnout
**Middle ground:** $4-5M + earnout

---

## **Earnout Terms (Tie to Base Case)**

```
Structure:
- Base Payment (at close):    $4.5M (cash)
- Earnout (Years 1-2):        Up to $2.0M

Earnout Trigger:
Year 1: If ARR > $2.5M (reasonable from $1.5M base)
        → Earn $500k

Year 2: If ARR > $4.0M
        → Earn $1.5M

Total upside: $4.5M + $2.0M = $6.5M (close to base case)
```

---

## **To Build in Excel:**

1. Column A: Years 0-5
2. Columns B-D: Revenue (Conservative / Base / Bull)
3. Columns E-G: EBITDA (same 3 scenarios)
4. Columns H-J: FCF (NOPAT + D&A - CapEx)
5. Columns K-M: Discount factors (1 / (1 + 0.12)^year)
6. Columns N-P: PV of FCF
7. Sum: Row for each scenario
8. Terminal value calc: Formula-based
9. Final EV: SUM(PVs) + PV(Terminal)

**Add sensitivity table:**
```
Vary WACC (9%-15%) vs Terminal Growth (1%-5%)
→ Shows range ($0.8M - $25M) to test robustness
```

---

## **What to Include in Dataroom:**

- `DCF_Model.xlsx` (Excel with 3 tabs: Conservative / Base / Bull)
- `Valuation_Summary.pdf` (this page + charts)
- `Assumptions_Documentation.md` (why you used 12% WACC, 3% terminal growth, etc.)
## Related
