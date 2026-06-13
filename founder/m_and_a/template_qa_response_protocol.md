# Q&A Response Protocol — How to Answer Diligence Questions

## Cardinal Rules

1. **Never say "I don't know" without a follow-up.**
   - Bad: "I don't know our CAC payback."
   - Good: "We haven't formally measured it, but based on [proxy], it's roughly [estimate]."

2. **If you lie, the deal dies.**
   - Don't fudge numbers. Buyers will find the truth in diligence; nondisclosure kills deals.
   - Better: "We had a customer churn event in 2025-Q1 (impact: -$50k ARR); here's the analysis."

3. **Delay = No.**
   - If you don't respond in 48 hours, buyer assumes you're hiding something or don't care.
   - Create a shared Q&A doc; answer 5–10 questions daily.

4. **Answer the question they asked, not the question you wanted.**
   - Bad: "Our product is amazing!" (when they asked: "What's your churn rate?")
   - Good: "Our churn is 5% annually; here's why it's low [reasons]."

5. **Provide proof, not claims.**
   - Attach spreadsheets, customer letters, NPS reports, contracts.
   - "We have strong customer relationships" is meaningless; attach NPS survey data.

---

## Response Templates by Question Type

### Type 1: Financial Red Flag Questions

**Q: "Your revenue growth slowed in Q4 2025. Why?"**

**Bad response:**
- "Seasonal; it happens in every SaaS company."

**Good response:**
- "Q4 growth was $200k MRR (10% month-over-month), down from Q3's 15%. Root causes:
  - 3 customers churned due to [specific reason], impact: -$50k
  - Sales cycle for new deals extended (enterprise buying freezes), but pipeline is strong: $600k
  - Implementation team bottleneck delayed onboarding (we've hired 2 more engineers)
  - Projected Q1 recovery: $250k new MRR (signed LOIs attached)"

---

### Type 2: Customer Risk Questions

**Q: "Customer A is 25% of revenue. What's the churn risk?"**

**Bad response:**
- "They're a great customer; we have a strong relationship."

**Good response:**
- "Customer A (Acme Corp) is ARR $600k, 3-year contract through 2027-Q2. Churn risk assessment:
  - Strength: Deep API integration; 8+ stakeholders trained on platform; multi-year roadmap alignment
  - Risk: Single point-of-failure (CFO owns the decision); minimal alternative vendors they could use
  - Mitigation: We've locked a 3-year contract; embedded support engineer on their team; executive sponsor (our CEO) has quarterly calls
  - Post-acquisition: Recommend buyer assign a dedicated account executive pre-close"

---

### Type 3: Tech Debt / Risk Questions

**Q: "Your data model looks outdated. How will this scale?"**

**Bad response:**
- "It works fine; we've never had performance issues."

**Good response:**
- "Our data model was designed for <$1M ARR. Current architecture:
  - PostgreSQL with [schema], handles ~5M queries/day without issues
  - Known limitation: No multi-tenancy (all data in single schema); refactor needed to scale beyond $10M ARR
  - Timeline: 6-month engineering effort post-acquisition
  - Risk: If you acquire a second product with overlapping customers, integration will require simultaneous refactor
  - Recommendation: Budget $500k engineering + 3 months timeline for multi-tenancy build"

---

### Type 4: Compliance / Legal Red Flag Questions

**Q: "Are you GDPR compliant?"**

**Bad response:**
- "Yes, we're GDPR compliant."

**Good response:**
- "GDPR compliance status:
  - Data processing agreement (DPA) in place with all customers (copy attached)
  - Data residency: EU customers' data stored in Frankfurt, US customers in us-east-1
  - Right-to-deletion: Implemented; can delete customer data within 30 days of request
  - Audit: No formal GDPR audit conducted; recommend GDPR compliance audit post-close (~$50k, 6 weeks)
  - Known issue: Historical backup data (>7 years old) not yet deleted; will remediate by close"

---

### Type 5: "Gotcha" Questions

**Q: "We found a 1-star review on Capterra saying your product is buggy. How do you respond?"**

**Bad response:**
- "That review is wrong; our product is solid."

**Good response:**
- "That review (from Customer X, [date]) reflects a legitimate issue:
  - Their integration broke because they didn't follow the setup guide; our support could've been faster
  - We've since improved: Built setup wizard (reduces errors 95%), hired 2 more support engineers
  - Current NPS: 42 (up from 28 in 2025); customer satisfaction score: 4.6/5
  - Post-close opportunity: Expand support team; build community forum to reduce support burden
  - Same customer now has 4.5/5 rating and has renewed annually"

---

### Type 6: Competitive Questions

**Q: "Competitor Y launched a [feature] last month. How do you stay ahead?"**

**Bad response:**
- "We have a better product; we'll out-execute them."

**Good response:**
- "Competitive landscape:
  - Competitor Y's [feature] is comparable to our [feature], which we've had for [duration]
  - Where we differentiate:
    - Integration depth: Our API has 5x more endpoints; deeper customer stickiness
    - Pricing: We're 30% cheaper; better unit economics for SMBs
    - Community: 10k active users vs. their ~2k
  - Their advantage: Better brand; 2x our sales team
  - Strategic implication: We're niche leader, not category leader
  - Your opportunity: Post-acquisition, use your brand/sales to move upmarket"

---

## Non-Answer Patterns (Red Flags for Buyer)

| Non-Answer | What Buyer Hears | Your Risk |
|---|---|---|
| "I'll get back to you" (48+ hours) | "They're hiding something" | Damages credibility |
| "We don't track that metric" | "They're not a real business" | Valuation hit |
| "That's not really a problem" (dismissing Q) | "They're defensive; something's wrong" | Diligence derails |
| "I'd rather not share that info" | "They're definitely hiding it" | Deal dies |
| "Most companies do the same thing" (excusing issue) | "Standard practice ≠ acceptable" | Damages trust |

---

## Response Framework (Use This for Every Q&A)

```
[SITUATION]
- State the fact clearly and concisely
- Provide context (when, how big, why it matters)

[ANALYSIS]
- Root cause: What caused this?
- Impact: How bad was it? (numbers, not vibes)
- Action taken: What did you do about it?

[FORWARD LOOK]
- Improvement: What's better now?
- Timeline: When?
- Remaining risk: What could still go wrong?

[BUYER OPPORTUNITY]
- Post-acquisition action: What should buyer do?
- Budget / timeline: How much effort?
- Upside: How does this create value?
```

---

## Shared Q&A Doc Setup

**Create a Google Doc:**
- Title: "[Company Name] - Due Diligence Q&A"
- Share with: Buyer, buyer's counsel, buyer's accountant (read-only for them)
- Format:
  ```
  Q: [Question from buyer]
  Date received: [date]
  Due date: [date]
  Respondent: [name]
  Status: [ ] Answered  [ ] In progress  [ ] Pending data
  
  A: [Your response + attachments]
  Updated: [date]
  ```

**Daily standup:**
- 5 questions answered daily = Q&A complete in 3 weeks (typical)
- If Q&A drags > 6 weeks = buyer is slow-walking

---

## Emergency Protocols (When Buyer Finds Something Bad)

**Scenario: Buyer discovers $100k customer churn you didn't disclose**

**Your move:**
1. Acknowledge immediately: "Yes, we discovered this in Q4; here's the analysis" (attach doc)
2. Context: "This was isolated to [reason]; here's why it won't repeat"
3. Remediation: "We've [action]; 12 customers retained; only 1 did not renew"
4. Forward: "We expect 2–3% annual churn going forward; here's the data"

**Don't:**
- Deny it ("We didn't lose that customer")
- Minimize ("It was a small account" / "They were going to churn anyway")
- Blame buyer ("You should've asked earlier")

**Example honest response:**
- "We had a churn event in Q4 2025. We lost $150k ARR from 3 customers due to product-market fit issues with new segment. We've since re-focused on core SMB segment. New churn rate: 3% (was 8% in Q4). Confidence in retention: High."

---

## Best Practices Summary

| Do | Don't |
|---|---|
| Answer in 48 hours | Delay beyond 72 hours |
| Provide attachments/proof | Say it "sounds right" |
| Acknowledge problems upfront | Hide until buyer finds them |
| Offer post-close action plan | Minimize or dismiss concerns |
| Tie problems to opportunities | Make excuses |
| Use data & examples | Speak in generalities |
| Show confidence in the business | Panic or overapologize |
