---
name: earnout-kpi-dashboard
description: Post-close metrics tracker — revenue, retention, churn; ties to founder payout schedule
type: tool
---

# Earnout KPI Dashboard — Post-Close Tracking

**Utilisation** : Google Sheets / Airtable template. Weekly refresh. Determines founder payout.

**Why** : 60% of earnouts dispute happens because metrics aren't tracked weekly. This prevents that.

---

## Template Setup (Copy to Sheets)

### Part A: Target Metrics (1-pager)

| Metric | Target (Y1) | Target (Y2) | Payout if Hit | Notes |
|--------|-------------|-------------|---------------|-------|
| **ARR** | $[X] | $[X+growth] | 40% of earnout | Minimum retention baseline |
| **Net Retention Rate** | 95% | 95%+ | 30% of earnout | Avoid churn cliff |
| **Customer Count** | [#] | [#] | 20% of earnout | Volume metric |
| **Churn Rate (annual)** | <5% | <5% | 10% of earnout | Stability check |
| **EBITDA Margin** | [%] | [%] | Bonus 10% | Operational health |
| **TOTAL EARNOUT** | — | — | **$[X]M over 2y** | — |

---

### Part B: Weekly Tracking Sheet

**Format** : Auto-update from accounting system (Stripe, Quickbooks, HubSpot, etc.)

```
Week  | Date      | ARR     | Δ from Target | NRR  | Churn% | Customer# | Status
------|-----------|---------|---------------|------|--------|-----------|--------
1     | 2026-07-01| $100K   | +$2K          | 96%  | 3%     | 25        | ✓ On track
2     | 2026-07-08| $102K   | +4K           | 96%  | 2%     | 26        | ✓ On track
3     | 2026-07-15| $98K    | 0K (-$2K)     | 94%  | 5%     | 25        | ⚠ Watch NRR
4     | 2026-07-22| $101K   | +1K           | 95%  | 4%     | 26        | ✓ Recovered
```

---

### Part C: Monthly Recap & Projection

| Metric | Jan Actual | Jan Target | Variance | Q1 Projection | Full Year Projection | On Track? |
|--------|-----------|-----------|----------|---------------|---------------------|-----------|
| ARR | $[X] | $[X] | — | — | — | ✓ / ⚠ / ✗ |
| NRR | 96% | 95% | +1% | — | — | ✓ / ⚠ / ✗ |
| Churn | 2% | 5% | Better | — | — | ✓ / ⚠ / ✗ |
| EBITDA% | 35% | 30% | +5% | — | — | ✓ / ⚠ / ✗ |

**Commentary** : What drove variance? (New customers / churn event / price increase / cost cuts?)

---

### Part D: Earnout Payout Schedule

```
Year 1 (2026):
├─ Q1 (Mar 31):  $50K payment if ARR ≥ $[X] && NRR ≥ 95%
├─ Q2 (Jun 30):  $50K payment if ARR ≥ $[X] && NRR ≥ 95%
├─ Q3 (Sep 30):  $50K payment if ARR ≥ $[X] && NRR ≥ 95%
└─ Q4 (Dec 31):  $100K payment if full-year targets met

Year 2 (2027):
└─ Dec 31:       $[X] payment based on cumulative 2-year KPIs
```

**Trigger logic** :
- If any metric misses: payment held, founder has 30 days to remediate
- If metric recovers next quarter: back-payment issued
- If metric fails 2 quarters in a row: earnout for that metric is forfeited

---

## Real Example Setup

**Scenario** : $500K ARR SaaS, buyer pays $1.5M cash + $500K earnout (2 years).

### Metrics
- **ARR growth** : $500K → $600K (20% YoY) → 40% of $500K earnout
- **NRR** : Stay ≥95% → 30% of earnout
- **Customer retention** : Keep 90% of existing customers → 20% of earnout
- **Bonus** : Hit 40% EBITDA margin → 10% bonus earnout

### Payout Schedule
```
Q1 2026: $50K if ARR ≥ $525K, NRR ≥ 95%
Q2 2026: $50K if ARR ≥ $545K, NRR ≥ 95%
Q3 2026: $50K if ARR ≥ $565K, NRR ≥ 95%
Q4 2026: $100K if full-year ARR ≥ $600K, avg NRR ≥ 95%

Full Year 2: $250K if 2-year cumulative ARR ≥ $1.2M, retention ≥ 90%
Bonus: +$50K if avg EBITDA margin ≥ 40%
```

---

## How to Use Weekly

**Every Friday 5pm:**
1. Pull ARR from Stripe (or accounting system)
2. Calculate NRR (New - Churn / Beginning balance)
3. Count churned customers this week
4. Update tracker
5. If variance > ±$10K, investigate root cause
6. Share with buyer / acquirer (transparency builds trust)

**Monthly (First Friday of month):**
1. Recalculate projections
2. If off-track, decide: Are we fixing metrics or renegotiating?
3. Document decisions in separate "Notes" sheet

---

## Dispute Prevention

**Common disputes** :
- "We thought NRR was 96%, but you say 92%"
  → **Solution** : Audit trail (Stripe + invoice data + manual reconciliation, all stored in Sheets)

- "Churned customer shouldn't count because they're temporarily paused"
  → **Solution** : Define **churn** upfront (30/60/90-day pause = churn?)

- "We hit $600K ARR but you won't pay earnout"
  → **Solution** : SPA specifies: "_ARR = sum of all active recurring contracts as of measurement date, excluding trials/demos_"

**Best practice** :
- Pull raw data from systems (Stripe, Quickbooks) → automated imports → less manual error
- Buyer AND seller both have access to dashboard → real-time alignment
- Monthly "earnout sync" call (15 min) → agree on actuals, discuss projections

---

## Template: Google Sheets / Airtable

**Google Sheets version** : Duplicate this template
```
Sheet 1: Targets (reference)
Sheet 2: Weekly tracker (auto-pull from API if possible)
Sheet 3: Monthly recap (formulas to summarize Sheet 2)
Sheet 4: Payout schedule (if/then logic for earnout trigger)
Sheet 5: Notes (qualitative explanations)
```

**Airtable version** : Use same structure, use lookups for auto-calculations.

---

## What to Negotiate into SPA

```
"Earnout payments are triggered when:
(a) ARR ≥ [threshold] as of measurement date (based on Stripe & reconciliation)
(b) NRR ≥ [threshold] (calculated as: (Beginning ARR - Churn + New) / Beginning ARR)
(c) No customer >30% of ARR has churned

Measurement dates: Last day of each quarter.
Disputes resolved: Buyer provides calculation → Founder audits within 15 days → 
Independent accountant breaks tie if >$10K variance.

Founder has 30-day remediation window: if metric dips below threshold in Month 1, 
can be recovered in Month 2 → back-payment issued if recovered.
```

---

## Next Step
Copy this template, populate with your actual targets, share with buyer before LOI → build trust.
