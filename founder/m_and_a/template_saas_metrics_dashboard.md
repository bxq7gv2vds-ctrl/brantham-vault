---
name: saas_metrics_dashboard_specs
description: Dashboard buyer-ready — ARR, churn, CAC, LTV, payback period (data room format)
metadata:
  type: reference
  created: 2026-06-13
  effort: 8min
---

# SaaS Metrics Dashboard — Buyer-Ready Format

**Objectif :** Format standardisé que tout PE/acquéreur attend de voir (data room, VDD call).

---

## Tier 1: Core Metrics (Every SaaS Buyer Wants These)

### 1. Revenue Metrics

| Metric | Definition | M-3 | M-2 | M-1 | Trend | Notes |
|--------|-----------|-----|-----|-----|-------|-------|
| **MRR (Monthly Recurring Revenue)** | Subscription revenue only (excl. one-time) | $[X] | $[Y] | $[Z] | +[X]% | SaaS metric; ex-professional svcs |
| **ARR (Annualized RR)** | MRR × 12 | $[X]k | $[Y]k | $[Z]k | +[X]% | What buyer valuates on |
| **Gross Revenue Retention (GRR)** | (MRR_month / MRR_prev_month) less churn | [X]% | [Y]% | [Z]% | [Trend] | No expansion; just churn-only |
| **Net Revenue Retention (NRR)** | GRR + expansion ÷ base | [X]% | [Y]% | [Z]% | [Trend] | Magic #: ≥100% = buyer premium |
| **Monthly Churn Rate** | (Churned customers / month) ÷ (start customers) × 100 | [X]% | [Y]% | [Z]% | [Trend] | <3% = healthy; <2% = strong |

**Calculation example (MRR):**
```
Churn: 2 customers × $500/mo = -$1k
Expansion: 1 customer upsell $300 = +$300
NRR = (Base - Churn + Expansion) ÷ Base
    = ($100k - $1k + $0.3k) ÷ $100k
    = 99.3% (below 100% = net negative)
```

---

### 2. Unit Economics

| Metric | Value | Source | Notes |
|--------|-------|--------|-------|
| **CAC (Customer Acquisition Cost)** | $[X] | Sales & marketing ÷ new customers | Don't include pre-sales effort unless % of payroll |
| **CAC Payback (months)** | [X] months | Gross Margin ÷ CAC | < 12 months = healthy; < 6 = strong |
| **LTV (Lifetime Value)** | $[X] | 1 ÷ churn rate × gross margin per customer | LTV:CAC ratio ≥ 3:1 = viable |
| **LTV:CAC Ratio** | [X]:1 | LTV ÷ CAC | Target: ≥ 3:1 (PE expects 4:1+) |
| **Gross Margin %** | [X]% | (Revenue - COGS) ÷ Revenue | SaaS: 70-90% healthy; <60% = red flag |
| **Magic Number (Sales Leverage)** | [X] | (ARR growth ÷ sales & marketing spend) | ≥0.75 = strong GTM efficiency |

**Calculation example (LTV:CAC):**
```
Churn = 2.5%/mo = 30%/yr
LTV = 1 ÷ 0.30 = 3.3 years × $3k gross margin = $10k
CAC = $2k
Ratio = 10:2 = 5:1 (STRONG)
```

---

### 3. Customer Metrics

| Metric | Current | Trend | Benchmark | Notes |
|--------|---------|-------|-----------|-------|
| **Total Customers** | [X] | +[X]%/yr | Category-specific | All paying customers |
| **Avg Contract Value (ACV)** | $[X]/yr | [Trend] | Mid-market = $10-50k | Affects payback calculation |
| **Customer Concentration (Top 5)** | [X]% of ARR | [Trend] | Healthy = <30% | >50% = risky for acquirer |
| **Expansion Rate (%/mo)** | [X]% | [Trend] | 2-5%/mo = strong | Upsells + cross-sells ÷ base |
| **New Logo Growth** | [X]/mo | +[X]%/yr | 10-20/mo (depends) | New customer acquisitions |

---

## Tier 2: Context Metrics (Buyer Will Ask for These)

| Metric | Value | Caveat |
|--------|-------|--------|
| **Salesforce Renewal Rate** | [X]% | Contracts up for renewal in next 12mo that renew |
| **Win Rate** | [X]% | Deals closed ÷ qualified pipeline |
| **Sales Cycle (days)** | [X] | Deal close date - first contact date |
| **Rule of 40 Score** | [X] | ARR growth % + gross margin % (target: ≥ 40) |
| **Net Burn (if pre-revenue)** | $[X]/mo | Monthly cash burn rate |
| **Runway** | [X] months | Cash ÷ net burn (if unprofitable) |

---

## Dashboard: Monthly P&L Snapshot

```
═════════════════════════════════════════════════════════
MONTH: [YYYY-MM]  |  TTM (Trailing 12 Months): [X] months

REVENUE
  MRR:                          $[X]k
  Less: Refunds / Credits       $(X)k
  Net MRR:                      $[X]k
  ARR (annualized):             $[X]k

CHURN & EXPANSION
  Customers Lost This Month:    [X] (GRR: [X]%)
  Expansion (Upsells):          $[X]k (NRR: [X]%)
  
UNIT ECONOMICS
  Gross Profit (Revenue - COGS): $[X]k ([X]%)
  CAC This Month:               $[X] ([X] new customers)
  CAC Payback Period:           [X] months
  LTV:CAC Ratio:                [X]:1

CUSTOMER HEALTH
  Total Active Customers:       [X]
  New Customers:                [X]
  Churn Rate (monthly):         [X]%
  Top 5 Customers % ARR:        [X]%

EFFICIENCY
  S&M Spend / ARR:              [X]% (benchmark: 30-50%)
  Magic Number:                 [X]x
  Rule of 40:                   [X] (ARR growth % + GM%)

═════════════════════════════════════════════════════════
```

---

## What NOT to Include (Buyer Red Flags)

❌ **Non-recurring revenue in "ARR"** → Breaks valuation math
❌ **Deferred revenue as "revenue"** → Inflates top line
❌ **Customer acquisition via founder network only** → Not scalable
❌ **Gross margin without COGS detail** → Likely unsustainably high
❌ **Missing churn data** → Hides customer satisfaction issues
❌ **Blended CAC (paid + organic)** → Can't assess paid GTM efficiency
❌ **"Adjusted" metrics (GAAP exceptions)** → Buyer will recalculate anyway

---

## Pre-Diligence Checklist (Data Room Format)

- [ ] **Revenue Ledger** — 24 months of monthly MRR (reconcile to accounting)
- [ ] **Customer List** (anonymized if needed) — Name, ARR, contract end date, churn risk (Y/N)
- [ ] **Customer Cohort Analysis** — Customers by vintage (2022 cohort, 2023 cohort, etc.)
- [ ] **Churn Analysis** — Last 24 months (month/reason/ARR lost per reason)
- [ ] **Sales Funnel** — Current pipeline (stage, deal size, close probability)
- [ ] **GTM Spend Breakdown** — Sales (salaries), marketing (budget), pre-sales (salaries)
- [ ] **Unit Economics Calc** — Show formula, not just numbers
- [ ] **Accounting Reconciliation** — Revenue metric (MRR) reconciles to P&L within 5%

---

## Buyer Questions You WILL Get

**Q: Why is NRR only 98%?**
A: [Root cause]. Mitigation plan: [what you're doing to fix].

**Q: How much revenue comes from top 3 customers?**
A: [X]% — diversifying via [product/GTM changes].

**Q: Why is CAC so high?**
A: Because ACV is [X], not [Y] — payback is [Z] months, which is [sustainable/not].

**Q: What's your churn trend?**
A: Declining — from [X]% (M-12) to [Y]% (M-3).

---

## Export Format (for VDD Data Room)

**File:** `Metrics_Dashboard_[YYYY-MM].xlsx`

```
Sheet 1: "Revenue" — 36 months of MRR, ARR, GRR, NRR
Sheet 2: "Churn" — Monthly cohort churn rates (visualized)
Sheet 3: "Unit Econ" — CAC, LTV, payback, Rule of 40 (with formulas visible)
Sheet 4: "Customers" — Full list (redacted or anonymized as needed)
Sheet 5: "Assumptions" — All metric definitions + data sources
```

---

**Impact:** Answers 80% of buyer questions in first 24 hours.
