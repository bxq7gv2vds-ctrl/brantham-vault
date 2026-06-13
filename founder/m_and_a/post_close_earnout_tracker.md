---
name: post_close_earnout_tracker
description: Post-close KPI tracking + earnout payout calculator (Excel-ready)
type: tool
created: 2026-06-13
status: production
---

# POST-CLOSE EARNOUT TRACKER & KPI DASHBOARD

**Purpose:** Track earnout milestones weekly + calculate real-time payouts based on buyer's SPA clauses  
**Format:** Copy this structure into Excel/Google Sheets  
**Update frequency:** Weekly (Sunday evening)  

---

## A. EARNOUT STRUCTURE (Fill in from SPA)

```
|  Metric       | Target (Y1) | Target (Y2) | Target (Y3) | Max Payout |
|---|---|---|---|---|
| ARR Growth    | $2.5M       | $3.5M       | $4.5M       | $1.2M      |
| NDR (Net Dollar Retention) | 95% | 105% | 110% | $300K |
| Churn Rate    | <5%         | <4%         | <3%         | $200K      |
| **Earnout Subtotal** | | | | **$1.7M** |

**Notes:**
- Earnout paid 60 days post-year-end close (true-up period)
- Payouts quarterly vs annual? (confirm with CFO)
- Holdback % if targets missed: ___%
```

---

## B. WEEKLY KPI SNAPSHOT (Copy template below for each week)

### **WEEK XX (Date: YYYY-MM-DD)**

```
| KPI              | Weekly    | MTD        | Target (Pro-Rata) | Status   | Notes           |
|---|---|---|---|---|---|
| ARR              | $185K     | $740K      | $190K (4 weeks)   | 🟢 On   | +3% vs budget   |
| NDR %            | 98%       | 97.2%      | 98%               | 🟡 Flag | Churn uptick    |
| Churn Rate       | 3.2%      | 3.5%       | 3.0%              | 🔴 Miss | 1 customer lost |
| New ARR (Wins)   | $120K     | $480K      | $500K (est. Y1)   | 🟢 Pace | On track        |
| CAC Payback      | 8.5mo     | —          | <9mo (SPA req)    | 🟢 OK   | Improving       |

**Owner:** _______ (founder, CEO, CFO, buyer-side?)  
**Traffic light status:** 🟢 On track | 🟡 Monitor | 🔴 At risk
```

---

## C. EARNOUT PAYOUT CALCULATOR

**At Year-End Close**, calculate quarterly or annual earnout:

```python
# Formula (adjust to your SPA terms)

def calculate_earnout(arr_actual, ndr_actual, churn_actual, target_config):
    """
    SPA Example:
    - Hit 100% ARR target → 100% of ARR bucket ($1.2M)
    - Hit <50% ARR target → $0 of ARR bucket
    - Hit 100% NDR target → 100% of NDR bucket ($300K)
    - Churn gate: if >5%, cap total earnout at 50%
    """
    
    # ARR Component (0-100%)
    arr_pct = min(arr_actual / target_config['arr'], 1.0)  # Cap at 100%
    arr_payout = arr_pct * target_config['arr_bucket']
    
    # NDR Component (0-100%)
    ndr_pct = min(ndr_actual / target_config['ndr'], 1.0)
    ndr_payout = ndr_pct * target_config['ndr_bucket']
    
    # Churn Gate
    if churn_actual > target_config['churn_threshold']:
        total = (arr_payout + ndr_payout) * 0.5  # 50% cap
    else:
        total = arr_payout + ndr_payout
    
    return {
        'arr_payout': arr_payout,
        'ndr_payout': ndr_payout,
        'total_earnout': total,
        'percent_of_max': (total / target_config['max_payout']) * 100
    }

# Example: Y1 actual results
result = calculate_earnout(
    arr_actual=2.8M,      # 112% of target
    ndr_actual=102%,      # 102% of 100% target
    churn_actual=3.8%,    # Within gate
    target_config={
        'arr': 2.5M,
        'ndr': 100%,
        'churn_threshold': 5%,
        'arr_bucket': 1.2M,
        'ndr_bucket': 300K,
        'max_payout': 1.7M
    }
)
# → Earnout = $1.35M + $300K = $1.65M (97% of max)
```

---

## D. RED FLAGS IN EARNOUT TRACKING

Watch for these buyer tactics:

| Red Flag | How Buyer Can Manipulate | Your Response |
|---|---|---|
| **Definition creep** | "ARR doesn't include X customer" (moved to new category) | Demand written ARR definition (SPA Exhibit A) |
| **Cost allocation** | Attributing marketing costs to your team's ARR | Baseline cost structure lock (from close date) |
| **M&A post-close** | Buyer acquires competitor, dilutes your ARR growth | Standalone metric (your business only) |
| **Pricing changes** | Buyer changes pricing → ARR shifts, earnout tanks | Price consistency clause or revenue cap |
| **Team departures** | Key person leaves → earnout at risk | Founder/team retention bonus (separate from earnout) |
| **Integration friction** | Acquirer blocks your hires, product roadmap stalls | Defined operational budget + hiring plan |

---

## E. ESCALATION PROTOCOL

**If KPI deviates >15% from pro-rata target:**

1. **Week 1:** Flag to buyer (CFO or integration lead)
2. **Week 2:** Diagnose root cause (market? execution? buyer mistake?)
3. **Week 4:** If pattern continues, escalate to M&A counsel
4. **Month 2:** Prepare evidence for year-end true-up dispute

---

## F. EXCEL TEMPLATE STRUCTURE

```
Sheets:
  1. SPA_Terms (read-only) — copy from signed SPA
  2. Weekly_Tracker (rolling 52 weeks)
  3. Earnout_Calculator (formulas)
  4. Risk_Log (red flags encountered)
  5. Notes (conversations with buyer)
```

**Download:** Use this as template — insert your own SPA metrics

---

## CONTEXT

This tracker ensures you hit earnout targets AND catch buyer manipulation early. Update it every Sunday (takes 10 min per week). Share monthly review with your advisor/lawyer.

**Related:** `founder_transition_guide.md`, `template_earnout_calculator.md`, `integration_risk_matrix_2_0.md`
