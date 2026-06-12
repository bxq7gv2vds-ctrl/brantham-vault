# SaaS Valuation Quick Guide

**Utilité** : déterminer fourchette de prix réaliste selon ARR + croissance.

---

## 1. Valuation par Multiple d'ARR

### Benchmark (2025–2026)

| Growth Rate | Multiple | Example |
|-------------|----------|---------|
| **Hyper-growth** (>100% YoY) | 8–12x ARR | $10M ARR = $80–120M valuation |
| **Fast growth** (50–100% YoY) | 5–8x ARR | $10M ARR = $50–80M valuation |
| **Solid growth** (25–50% YoY) | 3–5x ARR | $10M ARR = $30–50M valuation |
| **Mature** (<25% YoY) | 1.5–3x ARR | $10M ARR = $15–30M valuation |

**Note** : These are **acquisition multiples** (buyer premium). IPO multiples typically 2–3x higher.

---

## 2. Quick Calculator

```
INPUTS:
────────
ARR (Annual Recurring Revenue)        : $[X]M
YoY Growth Rate                       : [Y]%
Churn Rate (monthly)                  : [Z]%
Magic Number (Rule of 40)             : [Growth + Margin]
────────────────────────────────────────────

STEP 1: Determine growth tier
IF growth > 100%      → Use 8–12x multiplier
IF growth 50–100%     → Use 5–8x multiplier
IF growth 25–50%      → Use 3–5x multiplier
IF growth < 25%       → Use 1.5–3x multiplier

STEP 2: Adjust for quality
Quality factor ↑ if:
  ✓ Churn <5% (sticky customer base)
  ✓ NRR >110% (expansion revenue)
  ✓ Enterprise customers (>$100k ACV)
  ✓ PLG / high-touch hybrid
Quality factor ↓ if:
  ✗ Churn >10% (red flag)
  ✗ NRR <100% (shrinking base)
  ✗ SMB only (price compression)
  ✗ Founder-dependent sales

STEP 3: Calculate base valuation

Base = ARR × Multiple

STEP 4: Apply quality adjustment

Adjusted = Base × (0.8 to 1.3)
  • 1.3 = best-in-class metrics
  • 1.0 = market average
  • 0.8 = below-market quality

Example:
────────
ARR: $5M, growth 75%, churn 7%, NRR 95%

Step 1: 75% growth → 5–8x multiple
Step 2: Quality: churn 7% (OK), NRR 95% (slight drag) → 0.95 adjustment
Step 3: Base = $5M × 6.5 = $32.5M
Step 4: Final = $32.5M × 0.95 = $30.9M

RANGE: $25M–$35M (depending on buyer appetite, strategic value)
```

---

## 3. Alternative Valuation Methods (Sanity Check)

### Rule of 40

```
Score = Growth % + Net Margin %

IF Score < 40    → Below-market valuation (2–3x ARR)
IF Score 40–60   → Market valuation (3–6x ARR)
IF Score > 60    → Premium valuation (6–10x ARR)

Example:
Growth: 75%, Net Margin: 10% → Score = 85 (premium)
→ Valuation: 6–10x ARR is justified
```

### Comparable Transactions

| Company | ARR | Exit | Multiple |
|---------|-----|------|----------|
| Clearbit (HubSpot, 2021) | $2M | $10M | 5x |
| Notion (funding, 2023) | ~$50M | $10B | 200x (but late-stage) |
| Stripe (2023 funding) | ~$300M | $95B | 316x |
| SolarWinds (IPO, 2015) | $400M | $20B | 50x |

**Insight** : Acquisition multiples (3–8x) << IPO multiples (30–100x+).

### DCF (Simplified)

```
ASSUMPTIONS:
- Base ARR: $5M
- Growth next 5 years: 40%, 30%, 25%, 20%, 15%
- Terminal margin: 30%
- Discount rate: 15%

CALCULATE:
Year 1: $5M × 1.40 = $7M
Year 2: $7M × 1.30 = $9.1M
Year 3: $9.1M × 1.25 = $11.4M
Year 4: $11.4M × 1.20 = $13.7M
Year 5: $13.7M × 1.15 = $15.8M

Terminal Value (Year 6+): $15.8M × 30% margin / 15% discount = $31.6M
Discount terminal value to present: $31.6M / (1.15^5) = $15.7M

NPV (sum of discounted cash flows):
  Year 1: $7M / 1.15 = $6.1M
  Year 2: $9.1M / 1.15² = $6.9M
  Year 3: $11.4M / 1.15³ = $7.5M
  Year 4: $13.7M / 1.15⁴ = $7.8M
  Year 5: $15.8M / 1.15⁵ = $7.9M
  Terminal: $15.7M (already discounted)

TOTAL DCF VALUATION ≈ $40M
```

---

## 4. Valuation Sensitivity

```
                ARR    Growth   Quality   Low      Mid      High
────────────────────────────────────────────────────────────────────
CASE 1: Hot    $10M   80%      Premium   $65M     $85M     $110M
CASE 2: Good   $5M    50%      Average   $15M     $25M     $35M
CASE 3: OK     $3M    30%      Average   $5M      $10M     $15M
CASE 4: Cold   $2M    15%      Below     $2M      $4M      $6M
```

---

## 5. Valuation Drivers (Ranked)

| Rank | Driver | Impact |
|------|--------|--------|
| 1 | **Growth rate** | 50% of value → 75% growth = 2–3x premium |
| 2 | **Churn rate** | 30% of value → 5% churn vs 15% = 30% discount |
| 3 | **NRR** | 15% of value → NRR 120% = expansion revenue boost |
| 4 | **Customer concentration** | 10% of value → top customer >30% ARR = 20% haircut |
| 5 | **CAC payback** | 5% of value → 12-month payback = premium |

---

## 6. Red Flags (Lower Valuation)

🚩 Churn >15% monthly → -30% valuation  
🚩 NRR <90% → -20% valuation  
🚩 Top 3 customers >50% ARR → -25% valuation  
🚩 Negative growth → 1–2x ARR only  
🚩 Founder-dependent sales → -15% valuation  

---

## 7. Strategic Buyer Premium

Buyers paying 1.5–3x market multiples if:

✓ **Vertical synergies** : buyer has same customer, can cross-sell → +50%  
✓ **Cost synergies** : G&A elimination (duplicate CFO, legal) → +30%  
✓ **Tech acceleration** : buyer saves 12 months R&D → +40%  
✓ **Market consolidation** : buyer has no solution in this segment → +60%  

---

## 8. Negotiation Strategy

| Situation | Your Opening | Buyer Counter | Likely Settle |
|-----------|--------------|---------------|---------------|
| Competitive (2+ buyers) | Top of range | 20% discount | High end of range |
| Hot deal | 10x ARR | 5x ARR | 7–8x ARR |
| Mature SaaS | 4x ARR | 2.5x ARR | 3–3.5x ARR |
| Talent only | "Not for sale" | "Will overpay" | 1–2x ARR |

**Pro tip** : Let buyer anchor first. Then counter at +50% of market median. Settle in middle.

---

## 9. Excel Template (3-line formula)

```
=Valuation
=ARR × Lookup(Growth%; "Low/Mid/High") × Adjustment(Churn; NRR)

Example:
=$A1 × 6 × (1 - $A2 × 0.05) × (1 + MAX($A3 - 1.0, 0) × 2)
  ↑     ↑   ↑                 ↑
  ARR  6x  churn drag        NRR bonus
```

---

## 10. BATNA Reality Check

**You'll likely get:**
- If growth >75% + clean metrics = 6–8x ARR
- If growth 50% + OK churn = 3–5x ARR
- If mature/slow = 1.5–3x ARR
- **Earnout component** = 10–30% of deal (back-loaded)

**You won't get:**
- 10x+ unless hyper-growth ($50M+ ARR trajectory) OR strategic buyer paying for synergies
- 0.5x ARR (unless zombie, about to die)
- All cash (expect 70% cash, 30% earnout/stock/notes)
