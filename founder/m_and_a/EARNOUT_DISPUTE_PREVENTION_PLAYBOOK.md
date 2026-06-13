# Earnout Dispute Prevention Playbook

**Critical:** 40% of acquisitions end in earnout disputes. This playbook prevents yours.

---

## **Pre-Close: Lock Mechanics (Most Important)**

### **Define Measurement Clearly**

| Element | Example (BAD) | Example (GOOD) |
|---------|---|---|
| **What counts** | "Revenue growth" | "Annual recurring revenue (ARR) as calculated per [Accounting Methodology], excluding [specific exclusions]" |
| **How to measure** | "As reported by buyer" | "From audited financial statements + monthly reconciliation, signed by buyer's CFO + seller within 15 days of month-end" |
| **Timing** | "Year 1" | "Period: Jan 1, 2026 – Dec 31, 2026; Measurement date: Jan 31, 2027; Due date for earnout payment: Feb 28, 2027" |
| **Dispute resolution** | "Negotiate if disagree" | "If disagree, independent audit by [Big 4 firm]; loser pays audit cost; decision is binding" |

### **Build Transparency Into the Deal**

Lock in your earnout agreement:

```
EARNOUT MEASUREMENT

1. Annual revenue target: $[X] ARR (as of Dec 31, 2026)
2. Earn-out payment if target hit:
   - ≥ $[X]: Full $[Y]M earned
   - ≥ $[X-2M]: $[Y]M × 50% earned
   - < $[X-2M]: $0

3. Monthly reporting: Buyer sends you:
   - MRR + ARR (monthly, within 15 days of month-end)
   - Customer list (any churn? who left?)
   - Revenue reconciliation (P&L tie-out)
   
4. Annual audit: Independent CPA audits final measurement
   - Both parties can propose questions
   - CPA's report is binding
   - Cost split 50/50 unless dispute < 5% (winner pays all)

5. Payment: Due 45 days after final audit report
```

---

## **Post-Close: Weekly Hygiene**

### **Establish a Reporting Rhythm**

| Frequency | What | Who | Due Date |
|-----------|------|-----|----------|
| **Weekly** | MRR, new logos, churn (high level) | Buyer's CFO → You | Monday AM |
| **Monthly** | Detailed P&L + customer list reconciliation | Buyer's CFO/Controller → You | 15th of month |
| **Quarterly** | Board review + forecast update | You + Buyer's CEO | 30 days after quarter-end |
| **Annual** | Full audit + earnout measurement | Independent CPA | Jan 31 post-year |

### **Create a Shared Dashboard**

If possible, ask buyer for access to:
- Salesforce (to see new deals, churn)
- QuickBooks / accounting system (to see MRR + ARR)
- Customer success metrics (NPS, adoption, etc.)

**Why?** No surprises at year-end. If you see slipping in April, you can react in time.

---

## **Red Flags During Year 1 (Watch for These)**

| Flag | What It Means | Action |
|------|---|---|
| **Buyer missing monthly reporting deadline** | They're hiding something, or forgot about earnout | Escalate: "We haven't received April numbers. [Buyer CFO], can you send by Friday?" |
| **Revenue number doesn't reconcile to P&L** | Accounting mismatch (timing, accruals) | Ask: "April MRR is $[X]k, but P&L shows $[Y]k. What's the difference?" Get written explanation |
| **Churn jumps suddenly** | Usually buyer's management issue (changed pricing, sunsetted feature, terrible sales process) | Call [Buyer CEO]: "We're seeing unexpected churn in [Customer segment]. What changed?" |
| **Buyer disputes revenue recognition** | They might want to change how revenue is counted to lower earnout payout | Demand: "We agreed on [accounting method] at close. We're not changing that." |
| **Key customer leaves unexpectedly** | Might be buyer's fault (product issue, sales issue) | Investigate: Is buyer still supporting them? Did buyer change terms? |
| **Buyer merges your company into larger division** | Accounting gets murky (intercompany transactions, consolidated reporting) | Get written confirmation: "ARR will be reported separately, not consolidated." |

---

## **If Buyer Disputes Earnout (What to Do)**

### **Scenario 1: Buyer says "ARR is $[Lower], not $[Higher]"**

**Your response:**
1. **Ask for reconciliation** — "Show me the detail. Which invoices don't count? Why?"
2. **Reference the PA** — "Our PA says revenue is [definition]. This doesn't match that."
3. **Get written explanation** — Don't accept verbal excuses.
4. **If misalignment:** Ask for independent audit (per PA terms) — Costs $15–30k, split 50/50.

**Reality:**
- 80% of disputes are honest accounting misalignments (accruals vs. cash, refunds, etc.)
- 20% are buyer trying to cheat (don't pay earnout)
- Audit usually costs less than the disputed amount; forces resolution.

### **Scenario 2: Buyer changed the business (lost customers, sunsetted products)**

**Your legal argument:**
- Buyer has obligation to not *materially impair* earnout opportunity
- If buyer deliberately causes churn, you have breach claim
- Example: "Buyer shut down [Feature] that [Customer] relied on, causing them to churn. That's buyer's breach."

**Your action:**
1. **Document the cause** — Email trail showing buyer made decision
2. **Calculate impact** — "[Customer] churned because of [Buyer's decision]. That's $[X] ARR lost."
3. **Demand make-whole** — "[Buyer] owes earnout adjustment for damages caused by their decision."
4. **Escalate to buyer's CEO** — Go above CFO/M&A person; they'll force settlement

### **Scenario 3: Buyer disputes the audit**

**If buyer rejects independent audit findings:**

1. **Get audit in writing** — Binding language in PA should say CPA's findings are final
2. **Threaten arbitration** — "PA says [Arbitrator] has authority. You can dispute the audit, but we'll arbitrate."
3. **Prepare for litigation** — You likely need to sue; be prepared for legal costs

---

## **How to Win an Earnout Dispute (If It Gets There)**

### **Evidence You Need**

- [ ] **Written communications** (email, Slack) showing buyer had certain responsibilities (CSM, feature development, etc.)
- [ ] **Monthly reporting** (all 12 months of MRR, ARR, customer list) — Shows buyer reported numbers in real-time; can't change them later
- [ ] **Customer evidence** (why they churned, email trails with buyer's team, etc.)
- [ ] **Accounting reconciliation** (showing your numbers match P&L consistently)
- [ ] **Independent audit** (CPA's analysis, supporting the $[X] earnout calculation)

### **Strongest Argument**

"Buyer reported [X]k ARR monthly (which I accepted at the time). Now buyer says actual was $[Lower]k. This is inconsistent. By buyer's own monthly reports, earnout should be $[Y]."

Monthly reporting is your insurance policy. Use it.

---

## **Legal Language to Add to PA Now**

Add to earnout section:

```
"Buyer shall provide monthly reporting of ARR within 15 days 
of month-end. Monthly reports are deemed accepted unless 
disputed in writing within 30 days. Annual earnout shall be 
calculated based on audited year-end AR, with monthly reports 
used as reference for reconciliation.

If buyer's year-end earnings report differs from monthly reports 
by >5%, independent audit by [Big 4 firm] shall be conducted 
at buyer's cost. CPA's findings are binding."
```

This prevents buyer from saying "actually, January was $10k lower" after you've accepted their January report.

---

## **Reality Check**

**Most earnout disputes settle 50/50** because:
1. Litigation costs $[X]k+ in legal fees
2. Both sides want to avoid dragging it out
3. Earnout amount is usually < what it costs to litigate

**Best case:** You prevent disputes via transparency. Monthly reporting = mutual confidence.

**Worst case:** You have 12 months of documented numbers to support your claim. Buyer can't change the narrative.

---

## **Checklist for Year 1**

- [ ] Weekly dashboard review (comparing to forecast)
- [ ] Monthly written report from buyer (request by 15th of following month)
- [ ] Quarterly check-in call (just you + buyer CFO, review numbers)
- [ ] Identify risks in Q1/Q2 (if churn accelerating, flag it early)
- [ ] Resolve accounting differences month-by-month (don't let disputes pile up)
- [ ] Keep independent audit firm on speed-dial (in case you need them)
- [ ] Celebrate when you hit earnout (you've earned it)
