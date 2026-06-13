---
name: template-qanda-40-questions
description: Template Q&A document (40 questions fréquentes) pour due diligence M&A
metadata:
  type: reference
  created: 2026-06-13
---

# M&A DUE DILIGENCE Q&A
**40 Questions Fréquentes + Réponses Templat**

**Version**: Seller-prepared (proactive = faster diligence)  
**For**: Data room or email distribution to buyer & advisors

---

## SECTION 1: COMPANY & HISTORY (5 Q)

**Q1: What is [Company]'s legal entity structure?**

```
[Company] is a [C corporation / S corporation / Limited Company] 
incorporated on [DATE] in [JURISDICTION]. 
Registered office: [ADDRESS]. 
Employees: [#] full-time, [#] contractors.
```

**Q2: What is the cap table (share ownership)?**

| Shareholder | Shares | % Owned | Price per Share | Notes |
|-------------|--------|---------|-----------------|-------|
| [Founder A] | [#] | [X]% | [Valuation at grant] | Common, fully vested |
| [Founder B] | [#] | [X]% | [Valuation at grant] | Common, [X]% vested |
| [Investor 1] | [#] | [X]% | $[Price] | Series A, [participation rights] |
| **Total**   | | 100% | | |

**Q3: What is your funding history?**

| Round | Date | Amount | Lead Investor | Use of Funds |
|-------|------|--------|---------------|--------------|
| Pre-seed | [DATE] | $[X] | [Founder] | Product dev |
| Seed | [DATE] | $[X] | [Investor] | Sales + hiring |
| Series A | [DATE] | $[X] | [VC Firm] | Platform expansion |

**Q4: What is your current burn rate and runway?**

- **Monthly cash burn**: $[X]K (operations + payroll)
- **Current cash on hand**: $[X]M
- **Runway**: [X] months (at current burn)
- **Path to profitability**: [Q1/Q2 20XX] (projecting positive EBITDA)

**Q5: Are there any pending equity grants or unvested stock options?**

```
Yes. [X] options outstanding, all granted to employees/advisors.
- [#] options at $[strike], vesting [4-year cliff with 1-year cliff]
- [#] options at $[strike], vesting [3-year]
- [#] RSUs to [Founder], vesting [24 months post-Series A]

Total dilution: [X]% (on fully-diluted basis).
All vesting agreements are standard; no unusual acceleration clauses.
```

---

## SECTION 2: PRODUCT & TECHNOLOGY (8 Q)

**Q6: What does your product do? (One-line summary)**

```
[Company] is a [category] that [solves X pain point] for [customer segment] 
by [unique approach]. Deployed as [SaaS / on-premise / hybrid]. 
Core differentiator: [1 technology edge].
```

**Q7: What is your product roadmap for the next 12 months?**

| Quarter | Milestone | Impact |
|---------|-----------|--------|
| Q3 2026 | [Feature A] | +[10]% revenue expansion |
| Q4 2026 | [Feature B] + [Integration C] | +[15]% customer retention |
| Q1 2027 | [Vertical expansion] | $[X]M new ARR opportunity |
| Q2 2027 | [AI/ML capability] | [Competitive differentiation] |

**Q8: Do you own all IP (patents, code, trademarks)?**

```
Yes. All code is original, written by [Company] employees.
All IP is owned by [Company], not licensed from third parties.

Exceptions:
- [# open-source libraries] (MIT/Apache 2.0 licenses - fully compliant)
- [# third-party APIs] (Stripe, Twilio, AWS - standard SaaS stack)

Trademarks: [Company name] trademarked in [US, EU, UK] (™ registrations attached).
Domains: [main domain] + [X backup domains] all owned by [Company].

No pending litigation around IP.
```

**Q9: What is your tech stack?**

```
Backend:    [Node.js / Python / Go] + [PostgreSQL / MongoDB]
Frontend:   [React / Vue.js] + [Tailwind CSS]
Infrastructure: [AWS / GCP / Azure] + [Docker / Kubernetes]
Deployment: [CI/CD platform, e.g., GitHub Actions / CircleCI]
Monitoring: [Datadog / New Relic / CloudWatch]

All infrastructure is owned by [Company]; no dependence on single vendor.
```

**Q10: What is your technical debt, and what is the plan to address it?**

```
Areas of known technical debt:
1. [Legacy payment processing module] — refactor in Q4 2026 (est. 2 weeks)
2. [Monolithic API] — planning microservices split in 2027 (not urgent)
3. [Manual data migration process] — automating in Q3 (1 week eng effort)

None of these are blocking acquisitions or customer adoption.
Estimated total refactor cost: [X]K engineer-hours over [X] months.
```

**Q11: What are your security practices?**

```
- [SOC 2 Type II certified] / [ISO 27001 certified] / [In progress]
- Data encryption: TLS in-transit, AES-256 at rest
- Access control: [OAuth 2.0 / SSO / SAML]
- Penetration testing: [Annual by firm X] / [Quarterly internal]
- Incident response: [Plan documented, on file]
- GDPR / CCPA compliance: [Reviewed by counsel, compliant as of DATE]

No major security incidents to date.
Responsible disclosure policy: [Link to policy].
```

**Q12: What is your technology scalability? Can you handle 10x growth?**

```
Yes. Current architecture scales to [X] concurrent users / [X] transactions/sec.
For 10x growth, we'd need to:
- Upgrade database (2 weeks, no downtime via migration)
- Expand [compute resources / caching layer] (1 week setup)
- Estimated incremental cost: $[X]K/year at 10x scale

We've stress-tested to [Y] concurrent users; no issues projected.
```

**Q13: Are there any third-party dependencies that are critical to the product?**

```
Primary dependencies:
- [Stripe] for payment processing — industry standard, easily replaceable
- [Twilio] for SMS notifications — standard integration, can pivot to Nexmo/Plivo
- [AWS] for cloud compute — multi-region capable; can migrate to GCP/Azure

No single point of failure; all integrations are replaceable.
```

---

## SECTION 3: CUSTOMERS & REVENUE (8 Q)

**Q14: Who are your top customers? (By ARR)**

| Customer | ARR | Product Use Case | Churn Risk |
|----------|-----|------------------|------------|
| [Cust A] | $[X]K | [Description] | Low |
| [Cust B] | $[X]K | [Description] | Low |
| [Cust C] | $[X]K | [Description] | Medium (1 contract left) |
| [Cust D] | $[X]K | [Description] | Low |
| **Top 10 total** | **[X]% of ARR** | | |

**Q15: What is your customer concentration risk?**

```
Top 1 customer: [X]% of ARR
Top 5 customers: [X]% of ARR
Top 10 customers: [X]% of ARR

No customer is >15% of revenue; healthy diversification.
Lowest ARR customer: $[X]/year; highest: $[X]K/year.
```

**Q16: What is your churn rate (monthly/annual)?**

```
Monthly churn: [X]% (gross), [Y]% (net retention after upsells)
Annual churn: [Z]%

Churn drivers:
- [Reason 1]: [X]% (e.g., customer went out of business)
- [Reason 2]: [Y]% (e.g., replaced with competitor)
- [Reason 3]: [Z]% (e.g., product no longer needed)

Mitigation: [Initiatives to reduce churn].
```

**Q17: What is your NPS (Net Promoter Score) and customer satisfaction?**

```
NPS: [X] (as of [DATE])
Detractors ([0-6]): [X]% | Passives ([7-8]): [X]% | Promoters ([9-10]): [X]%

Customer satisfaction survey: [X]/10 average
CSAT trends: [Graph showing improvement / stability].
```

**Q18: What is your CAC and payback period?**

```
CAC (Customer Acquisition Cost): $[X] (total sales + marketing / new customers)
CAC Payback: [X] months
LTV (Lifetime Value): $[X]
LTV:CAC Ratio: [X]:1 (healthy = >3:1)

[Sales channel breakdown]:
- Self-serve / freemium: $[X] CAC, [X]-month payback
- SMB sales: $[X] CAC, [X]-month payback  
- Enterprise sales: $[X] CAC, [X]-month payback
```

**Q19: What is your pricing model?**

```
Model: [Per-seat / Usage-based / Hybrid]

Pricing:
- Starter: $[X]/month, [X] seats, [Y] features
- Professional: $[X]/month, [X] seats, [Y] features
- Enterprise: Custom (typically $[X]K–$[X]K/year)

Average selling price (ASP): $[X]/customer/month
Pricing elasticity: [Modest / high] (we've tested [X]% increase; demand effect [Y]%)

No discounting to named accounts (policy: list price only).
```

**Q20: What is your pipeline and sales cycle?**

```
Current pipeline: $[X]M (forecasted to close in next [X] months)
Average sales cycle: [X] weeks (SMB: [X] weeks, Enterprise: [X] weeks)

[Forecasted revenue next 12 months]:
- Q3 2026: $[X]M ARR
- Q4 2026: $[X]M ARR
- Q1 2027: $[X]M ARR
- Q2 2027: $[X]M ARR

Conservative case (50% pipeline close rate): $[X]M by EOY.
Aggressive case (70% close rate): $[X]M by EOY.
```

**Q21: Are there any multi-year contracts or unusual terms?**

```
Contract length: Majority [1-year] / [2-year] / [multi-year]

[X] customers on [3-year contracts] with annual price escalation clause (typically [3–5]%).
[Y] customers on [month-to-month]; most convert to annual via upsell.

All customer contracts are in the data room (folder: /Contracts/Customer Agreements/).
```

---

## SECTION 4: FINANCIAL PERFORMANCE (6 Q)

**Q22: What is your revenue (ARR / MRR)?**

```
Current ARR (as of [DATE]): $[X]M
Current MRR: $[X]K
Growth trajectory: [X]% YoY, [Y]% MoM

Historical revenue:
- [DATE–12 months ago]: $[X]M ARR
- [DATE–24 months ago]: $[X]M ARR
- YoY growth rate: [Z]%
```

**Q23: What are your unit economics (gross margin, COGS)?**

```
Gross margin: [X]% (revenue minus COGS)

COGS breakdown:
- Cloud infrastructure (AWS): [X]% of revenue
- Payment processing fees: [X]% of revenue
- Third-party APIs: [X]% of revenue
- Support & hosting: [X]% of revenue

Total COGS: [X]% of revenue
Gross margin: [100 – X]% = [Y]% (very healthy for SaaS; benchmark: 70–80%)
```

**Q24: What is your path to profitability?**

```
Current EBITDA: [Positive / Breakeven / Loss of $X]
Operating expenses: $[X]K/month

Assuming current revenue growth ([X]% MoM):
- Q4 2026: [Projected EBITDA: $[+/−X]K]
- Q1 2027: [Projected EBITDA: $[+/−X]K]
- Q2 2027: [Projected EBITDA: $[+/−X]K, breakeven expected]

We're already [self-sustaining / on path to profitability], reducing acquisition risk.
```

**Q25: What are your top 3 operating expenses?**

| Expense | Monthly | % of Revenue | Notes |
|---------|---------|--------------|-------|
| **Payroll** | $[X]K | [X]% | [# FTE breakdown] |
| **Cloud/Infrastructure** | $[X]K | [X]% | [Scales with usage] |
| **Sales & Marketing** | $[X]K | [X]% | Mostly contractor/ads, can be adjusted |

**Opportunity to optimize**: S&M spend (currently [X]% of revenue; benchmark: [Y]%). Possible to reduce to [Z]% with operational efficiency or channel shift.

**Q26: What is your cash balance and burn rate?**

```
Cash on hand (as of [DATE]): $[X]M
Monthly cash burn: $[X]K (or: Monthly positive cash flow of $[X]K)
Runway: [X] months at current burn (or: Cash-flow positive)

Expected burn trajectory:
- If hiring [# FTE] in sales: burn increases to $[X]K/month (runway: [X] months)
- If no new hiring: runway extends to [X] months (breakeven in [Q# YYYY])
```

---

## SECTION 5: TEAM & TALENT (4 Q)

**Q27: Who are the key team members?**

| Name | Role | Background | Retention |
|------|------|-----------|-----------|
| [Founder 1] | CEO | [Prior: Exits / Experience] | Committed through [closing + X years] |
| [Founder 2] | CTO | [Prior: Big Tech / Startup] | Open to post-close role discussion |
| [VP Sales] | [Role] | [Background] | [Timeline] |
| [VP Eng] | [Role] | [Background] | [Timeline] |

**Q28: What is your employment agreements and retention structure?**

```
All employees have:
- Offer letters with standard at-will employment
- Non-compete / non-solicitation agreements (standard [12-month] term)
- IP assignment agreements (standard)
- No unusual acceleration or severance arrangements (except as noted below)

Exceptions:
- [Founder 1]: [X]% equity acceleration upon [change of control / acquisition]
- [Key employee]: [X]% acceleration upon [3-year anniversary]

Note: All acceleration clauses are standard and disclosed in LOI.
```

**Q29: What is your organization structure?**

```
[Org chart diagram or text description]

Headcount:
- Engineering: [X] (product [#], infra [#], QA [#])
- Product: [X]
- Sales: [X]
- Customer Success: [X]
- Operations: [X]
- Total: [X] FTE, [Y] contractors

No redundant roles; lean team.
```

**Q30: Are there any key person risks?**

```
[Founder / Key person] is critical to [product direction / customer relationships / technical architecture].

Mitigation:
- We're [building deep team / documenting processes / creating knowledge base]
- [Key person] is committed to [X-year employment agreement] post-close
- [Backup plan]: [Alternative resource / team member who can transition role]

Risk level: [Low / Medium / Mitigated]
```

---

## SECTION 6: LEGAL & COMPLIANCE (5 Q)

**Q31: Are there any pending or threatened lawsuits?**

```
No pending litigation, claims, or threats as of [DATE].

Historical disputes:
- [Example]: [Customer dispute re: refund, settled for $[X]]
- [Example]: [Contractual disagreement with vendor, resolved]

All matters resolved; no contingent liabilities.
```

**Q32: What is your data privacy and regulatory compliance status?**

```
GDPR: [Fully compliant / Data Processing Agreement in place]
CCPA: [Compliant]
SOC 2 Type II: [Certified as of DATE] / [Audit in progress, expected DATE]
HIPAA: [Not applicable / Compliant]
Other: [List any industry-specific compliance, e.g., PCI-DSS, FedRAMP]

DPA (Data Processing Agreement): [On file; customers sign as part of sales process]
Privacy policy: [Link / attached]
No data breaches to date.
```

**Q33: Do you have any material contracts or commitments?**

```
Material commitments:
- [Lease agreement]: [Office, $X/month, expires DATE]
- [Cloud contract]: [AWS, $X/month, expires DATE, can terminate with notice]
- [Partner agreement]: [Strategic partnership, no exclusivity, renewable annually]

All contracts are on file in data room (folder: /Legal/Agreements/).
No unusual or burdensome obligations.
```

**Q34: Are there any employment disputes or workers' compensation claims?**

```
No active disputes, claims, or investigations.
Workers' compensation: [# claims in past 3 years] (all within industry norms).
No wrongful termination suits or discrimination complaints.
```

**Q35: What is your IP ownership and licensing status?**

```
All core IP (patents, copyrights, trademarks) owned by [Company].

Patents:
- [Patent name] (US [number], filed [DATE], issued [DATE])
- [Patent name] (US pending, filed [DATE])
- [# additional provisional patents] in development

Trademarks: [Company name] (US, EU, UK); all defensive. No third-party disputes.

Third-party IP:
- [# open-source components] (all Apache 2.0 / MIT; reviewed for compliance)
- No GPL or copyleft licenses that would infect our product

Licenses from third parties:
- [Tool / API], licensed under [terms], $[X]/month (non-exclusive)

No IP litigation or disputes with third parties.
```

---

## SECTION 7: RISKS & MITIGATIONS (3 Q)

**Q36: What are the top 3 business risks?**

| Risk | Severity | Mitigation |
|------|----------|-----------|
| [Competitive threat / new entrant] | [High] | [Differentiation / speed to market / customer stickiness] |
| [Customer concentration on top 3] | [Medium] | [Diversification roadmap / vertical expansion] |
| [Key person dependency] | [Medium] | [Hiring / documentation / team building] |

**Q37: What could cause revenue to decline?**

```
Scenarios:
1. [Market downturn affecting customer segment] → Risk: [Medium] 
   Mitigation: [Diversify customer base / expand to adjacent markets]

2. [Competitive product launch] → Risk: [Low] 
   Mitigation: [Our tech moat / customer switching costs / feature roadmap]

3. [Key customer churn] → Risk: [Low if <10% revenue exposure]
   Mitigation: [Diversification / expansion to other verticals]

Worst-case scenario: $[X]M revenue loss (if top 3 customers churn).
Probability: [Low] (all customers expanding usage).
```

**Q38: Are there any environmental, social, or governance (ESG) issues?**

```
Environmental: [Not applicable / Minimal carbon footprint (cloud-native)]
Social: [Equal opportunity employer / Diverse team / Fair wages]
Governance: [Compliant with local regulations / Audit-ready financial controls]

No ESG-related disputes or controversies.
```

---

## SECTION 8: TRANSACTION-SPECIFIC (2 Q)

**Q39: What seller representations are you comfortable making?**

```
We're prepared to make standard representations regarding:
- Organization and good standing
- Authority to enter transaction
- No conflicting agreements
- Accurate financial statements
- No undisclosed liabilities
- IP ownership and non-infringement
- Compliance with laws and regulations

Standard indemnification: [15–20]% of purchase price for [12–18 months]
Fraud/IP: [Uncapped] for [36 months]

We request [materiality baskets of $[50K–100K]] to avoid micro-claims.
```

**Q40: What is the expected timeline from LOI to close?**

```
Proposed timeline:
- LOI signed: [DATE]
- SPA drafted and reviewed: [45 days]
- Diligence completed: [30 days in parallel]
- Regulatory approvals (if any): [X days]
- Financing confirmation: [10 days]
- Closing: [45–60 days from LOI]

Hard close deadline: [DATE] (mutual termination if not closed by then).

We're prepared to move quickly; no significant obstacles anticipated.
```

---

## APPENDICES (Reference Only)

- **A**: Historical financial statements (12 months)
- **B**: Customer contracts (redacted or in separate secure folder)
- **C**: IP assignments and patent documentation
- **D**: Employee agreements and offer letters
- **E**: Board meeting minutes and cap table updates
- **F**: Insurance policies (D&O, liability, etc.)
- **G**: Compliance certifications (SOC 2, GDPR, etc.)

---

## UPDATES & AMENDMENTS

| Date | Update | Owner |
|------|--------|-------|
| [DATE] | Initial Q&A, 40 questions | [Founder] |
| [DATE] | Added customer references | [VP Sales] |
| [DATE] | Updated financials (Q3 close) | [Finance] |

**Last updated**: [DATE]  
**Owner**: [Founder / Finance Lead]
## Related
