---
name: valuation_calculator_dcf_multiples
description: Practical valuation calc tool using DCF method + comparable multiples (Excel-ready)
version: 1.0
date: 2026-06-12
---

# VALUATION CALCULATOR — DCF + COMPARABLES

**Input your numbers below. Copy to Excel for dynamic calculation.**

---

## PART A: YOUR INPUTS

### Current Metrics (Last 12 Months)

```
Annual Recurring Revenue (ARR):           $[____]M
Monthly Recurring Revenue (MRR):          $[____]k
Gross Margin %:                           [____]%
EBITDA Margin % (or net margin):          [____]%

Growth Rate (YoY %):                      [____]%
Net Retention Rate %:                     [____]%
  (formula: (Beginning ARR - Churn + Expansion) / Beginning ARR)

Customer Count:                           [____]
Customer Concentration (Top 1 as % of revenue): [____]%
```

---

## PART B: DCF VALUATION

### Step 1: Project Revenue (5-Year)

| Year | Base ARR | Growth % | Projected ARR | Notes |
|------|----------|----------|---------------|-------|
| Y0 (Today) | $[ARR]M | — | $[ARR]M | Actual |
| Y1 | $[ARR]M | [60]% | $[X]M | Conservative growth |
| Y2 | — | [40]% | $[X]M | Deceleration |
| Y3 | — | [25]% | $[X]M | Continued slowdown |
| Y4 | — | [15]% | $[X]M | Mature growth |
| Y5 | — | [10]% | $[X]M | Terminal growth |

**Your inputs:** Replace [60]%, [40]%, [25]%, [15]%, [10]% with realistic growth rates.  
**Conservative approach:** Use 60% of historical growth rate for projection.

### Step 2: Project Free Cash Flow

| Year | Projected ARR | EBITDA Margin | EBITDA | Tax Rate (20%) | FCF |
|------|---------------|---------------|--------|---|---|
| Y1 | $[X]M | [Y]% | $[Z]M | (20%) | $[FCF]M |
| Y2 | $[X]M | [Y]% | $[Z]M | (20%) | $[FCF]M |
| Y3 | $[X]M | [Y]% | $[Z]M | (20%) | $[FCF]M |
| Y4 | $[X]M | [Y]% | $[Z]M | (20%) | $[FCF]M |
| Y5 | $[X]M | [Y]% | $[Z]M | (20%) | $[FCF]M |

**Assumption:** EBITDA margin improves [Y]% per year (as you scale). Conservative: keep flat.

### Step 3: Calculate Terminal Value

```
Terminal Growth Rate (perpetuity):        [3]%
WACC (Discount Rate):                     [12]%
  (Typical for SaaS: 10-15%. Use 12% if uncertain.)

Terminal Value = (Y5 FCF × (1 + Terminal Growth)) / (WACC - Terminal Growth)
               = ($[FCF] × 1.03) / (0.12 - 0.03)
               = $[X]M
```

### Step 4: Discount to Present Value

```
Year 1 FCF × (1 / (1 + WACC)^1) = $[PV1]M
Year 2 FCF × (1 / (1 + WACC)^2) = $[PV2]M
Year 3 FCF × (1 / (1 + WACC)^3) = $[PV3]M
Year 4 FCF × (1 / (1 + WACC)^4) = $[PV4]M
Year 5 FCF × (1 / (1 + WACC)^5) = $[PV5]M

Terminal Value (discounted) × (1 / (1 + WACC)^5) = $[PVTV]M

ENTERPRISE VALUE (DCF) = $[PV1] + $[PV2] + $[PV3] + $[PV4] + $[PV5] + $[PVTV]
                       = $[X]M
```

---

## PART C: COMPARABLE MULTIPLES VALUATION

### Revenue Multiple Approach

**Step 1: Identify comparable acquisitions**

| Company | Year | Buyer | Purchase Price | ARR at Close | Multiple (Price/ARR) |
|---------|------|-------|-----------------|--------------|----------------------|
| [Co A] | 2025 | [Acquirer] | $[X]M | $[Y]M | [X/Y]x |
| [Co B] | 2025 | [Acquirer] | $[X]M | $[Y]M | [X/Y]x |
| [Co C] | 2024 | [Acquirer] | $[X]M | $[Y]M | [X/Y]x |
| [Co D] | 2024 | [Acquirer] | $[X]M | $[Y]M | [X/Y]x |
| Your Company | — | — | ? | $[Y]M | ? |

**Industry Benchmarks (if you don't have comps):**

| Category | Multiple | Notes |
|----------|----------|-------|
| Horizontal SaaS (SMB) | 6-12x ARR | Lower growth, mature |
| Vertical SaaS (Enterprise) | 10-20x ARR | Higher sticky, growth |
| Consolidator target | 8-15x ARR | Add-on play |
| Strategic acquisition | 12-25x ARR | Synergy upside |

**Step 2: Apply your multiple**

```
Median Comparable Multiple:        [X]x ARR
Your Current ARR:                  $[Y]M

Valuation = $[Y]M × [X]x = $[Z]M (Revenue multiple approach)
```

### EBITDA Multiple Approach (if profitable)

```
EBITDA Multiple (SaaS):            [8-15]x (typical)
Your Current EBITDA:               $[X]M (= ARR × EBITDA margin)

Valuation = $[X]M × [Y]x = $[Z]M (EBITDA multiple approach)
```

---

## PART D: SUMMARY & VALUATION RANGE

| Method | Valuation | Weight | Weighted Value |
|--------|-----------|--------|-----------------|
| DCF (5-year) | $[X]M | 40% | $[X]M |
| Revenue Multiple (Comparables) | $[X]M | 35% | $[X]M |
| EBITDA Multiple (if profitable) | $[X]M | 25% | $[X]M |

```
FAIR VALUE RANGE:

Conservative (pessimistic):  $[X]M  (10th percentile)
Mid-range (likely):          $[X]M  (median)
Optimistic (upside):         $[X]M  (90th percentile)

ASKING PRICE (recommended):  $[X]M  (upper quartile, leaves room for negotiation)
```

---

## ⚠️ SENSITIVITY ANALYSIS

**What if growth rate decelerates faster?**

| Scenario | Y1-Y5 Growth | Terminal Value | Enterprise Value | Valuation Change |
|----------|---|---|---|---|
| Base Case | 60%→10% | $[X]M | $[Y]M | — |
| Downside | 40%→5% | $[X]M | $[Y]M | -20% |
| Upside | 80%→15% | $[X]M | $[Y]M | +30% |

**What if WACC is 10% vs 12% vs 15%?**

| WACC | DCF Enterprise Value | Impact |
|------|---|---|
| 10% (lower risk) | $[X]M | +15% |
| 12% (base) | $[X]M | — |
| 15% (higher risk) | $[X]M | -15% |

---

## ✅ QUICK SANITY CHECKS

Use these to validate your valuation:

1. **Magic Number (efficiency metric)**
   ```
   Magic Number = Revenue Growth (annual) / Sales & Marketing Spend (annual)
   
   Your number: [____]
   Benchmark (SaaS): 0.75+
   
   If yours is [below], you're overspending on growth. Explains lower valuation.
   If yours is [above], you're efficient. Justifies higher multiple.
   ```

2. **Payback Period**
   ```
   Payback Period = (Avg. CAC) / (Monthly ARPU × Gross Margin)
   
   Your payback: [____] months
   Benchmark: <12 months for strong SaaS
   
   Longer payback → higher risk → lower multiple.
   ```

3. **Rule of 40**
   ```
   Growth Rate (%) + EBITDA Margin (%) = Rule of 40 Score
   
   Your score: [____]%
   
   >40 = Strong valuation case
   <40 = Needs growth or profitability improvement
   ```

4. **Burn Multiple (if not profitable)**
   ```
   Burn Multiple = Valuation / Monthly Burn Rate
   
   Your burn multiple: [____]x
   Benchmark: <10x (means 10 months of runway at this valuation)
   
   Higher = better (indicates path to profitability is clear).
   ```

---

## 📊 VALUATION BY BUYER TYPE

| Buyer Type | Typical Multiple | Adjustment Factors |
|---------|---|---|
| **Strategic (vertical integration)** | 15-25x | +Synergy multiple, +customer overlap, +tech fit |
| **PE (growth play)** | 8-15x | -Risk premium, +team retention bonus |
| **Consolidator (add-on)** | 10-16x | -Due diligence risk, +immediate synergies |
| **Acqui-hire** | 4-10x | -Company value secondary, +team premium |
| **Crossover (investor)** | 12-20x | +Warm relationship, -dilution concerns |

**Adjust your valuation up/down 20-30% based on buyer type.**

---

## 🎯 NEGOTIATION STRATEGY

```
Your Asking Price:     $[X]M  (upper quartile, defensible)
Their Opening Offer:   $[Y]M  (likely 20-30% lower)
Your Walk-Away Price:  $[Z]M  (your BATNA, never go below)

Negotiation Zone:      $[Y]M — $[X]M
Expected Close:        ~$[mid-range]M
```

**Never disclose:**
- Walk-away price
- Your cost basis / cap table dilution
- Personal financial motivation

**Always disclose:**
- Your growth assumptions (with data)
- Customer concentration (with mitigation)
- Anything material that diligence will find

---

## ✏️ EXCEL TEMPLATE

| Cell | Formula | Example |
|------|---------|---------|
| B5 | ARR | $2.5M |
| C5 | MRR | =B5/12 | $208k |
| B6 | Gross Margin | 75% |
| B7 | EBITDA Margin | 15% |
| B15 (Y1 ARR) | =B5 * (1 + Growth%) | =2.5 * 1.60 | $4.0M |
| B20 (Y1 FCF) | =B15 * B7 * 0.8 (tax) | =4.0 * 0.15 * 0.8 | $0.48M |
| B45 (DCF Sum) | =SUM(PV1:PV5) + PVTV | — | $[X]M |
| B50 (Multiple) | Comps research | 10x | $25M |
| B55 (Fair Value) | =(B45*0.4 + B50*0.35 + B60*0.25) | — | $[X]M |

---

**Created:** 2026-06-12  
**For:** Soren Mendy (M&A valuation)  
**Time to complete:** 15-30 min (fill in your numbers)  
**Files:** Copy to Excel for dynamic calculations

