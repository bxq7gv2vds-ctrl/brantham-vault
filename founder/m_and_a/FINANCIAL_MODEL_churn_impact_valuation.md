# Churn Impact on Valuation — Sensitivity Analysis

Buyer's #1 question: "What if your churn accelerates post-close?"

Use this sensitivity to show deal value under different churn scenarios.

## Your Current Metrics

| Metric | Value |
|--------|-------|
| Current ARR | $[X]k |
| Monthly Churn Rate | [Y]% |
| Annual Churn Rate | = (1 – (1 – Y%)^12) × 100 = [Z]% |
| Customer Concentration (top 5 as % of ARR) | [A]% |
| NRR (Net Revenue Retention) | [B]% |

---

## Valuation Bridge: Base Case vs. Churn Scenarios

| Scenario | Year 1 ARR | Year 2 ARR | Year 3 ARR | 3-Year Avg ARR | Multiple | Valuation | vs. Base |
|----------|-----------|-----------|-----------|---|---------|-----------|---------|
| **Base** (current churn) | $[X] | $[X] × (1 – Z%)^1 × NRR% = $[Y] | $[Y] × ... = $[Z] | $[Avg] | 4–6x | $[Val] | +0% |
| **+1% Churn** | $[X] | [Lower] | [Lower] | [Lower] | 4–6x | [Lower Val] | –[X]% |
| **+3% Churn** | $[X] | [Lower] | [Lower] | [Lower] | 3–5x | [Lower Val] | –[X]% |
| **+5% Churn** | $[X] | [Lower] | [Lower] | [Lower] | 2–4x | [Lower Val] | –[X]% |

---

## Churn Risk Scoring

Use this to predict buyer's churn concerns:

| Risk Factor | Score (1–5) | Impact on Valuation |
|-------------|------------|---|
| **Customer concentration (top 5 > 50%)** | [1–5] | –5–15% (earnout clawback) |
| **Churn trending up** (2024 vs 2025) | [1–5] | –10–25% |
| **Key customer at risk** (pending renewal) | [1–5] | –10–20% |
| **Product roadmap stalled** (customer feedback) | [1–5] | –5–10% |
| **Net revenue retention < 100%** | [1–5] | –10–30% |
| **Long sales cycle** (>6 months) | [1–5] | –5% (capital intensity) |

**Total Risk Score:** [Sum] / 30 → [%] likely valuation haircut

---

## Buyer's Earnout Tie to Churn (Common Structure)

Buyers protect themselves:

```
Earnout = [X% of purchase price]

Earned if Year 1 ARR ≥ [Y]k  
(If churn exceeds [Z]%, earnout reduces by [A]% per 1% excess churn)
```

**Example:**
- Base purchase: $10M
- Earnout: $3M (if Year 1 ARR ≥ $8M)
- If Year 1 ARR = $7.5M (due to 2% excess churn), earnout = $3M – (2% × $1M) = $2.98M

---

## How to De-Risk Churn in Buyer Conversation

1. **Show customer lifecycle** — How long does avg customer stay? Show cohort retention.
2. **Highlight expansion revenue** — NRR > 100% offsets churn risk.
3. **Prove customer success** — Case study from tier-1 customer; post-renewal expansion rate.
4. **Diversify customer base** — "Top 5 = 45% ARR" (not 60%); revenue spread = lower risk.
5. **Lock in multi-year contracts** — Offer discounts for 3-year prepay (before close) to reduce churn uncertainty.

---

## Earnout Measurement Framework (Buyer's Proposal)

Typical earnout tied to:

| Measurement | Formula | Period | Clawback Trigger |
|-------------|---------|--------|---|
| **ARR Retention** | (Year 1 ARR / Baseline ARR) × 100 | 12 months post-close | < 90% = –10% earnout |
| **Customer Retention** | (Customers at close – Churned) / Customers at close | 12 months | < 90% = –15% earnout |
| **Revenue Retention** | (Gross revenue retained / Starting revenue) × 100 | 12 months | < 85% = –20% earnout |

**Your play:** Push for annual measurement (not quarterly) to smooth seasonality.

---

## Pre-Close Prep Checklist

- [ ] Audit 24-month churn trend (show if improving, not worsening)
- [ ] Identify any customers at churn risk (notify buyer proactively = trust)
- [ ] Prepare customer retention playbook (what you'll do post-close to keep customers)
- [ ] Lock in any at-risk customer contracts before LOI signature
- [ ] Build ARR forecast model (buyer will create their own; yours should match)
