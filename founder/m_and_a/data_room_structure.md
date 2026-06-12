---
name: data_room_structure
description: Structure data room M&A complète pour SaaS — dossiers, fichiers minimaux, timeline
metadata:
  type: reference
  format: process_template
  version: 1.0
---

# Data Room — Structure SaaS Complète

**Platform recommandée :** Intralinks, Dealroom, Box, Google Drive (pas OneDrive)
**Timeline :** Setup ~3 jours, populate ~5 jours, live ~60 jours

---

## **STRUCTURE DOSSIERS (VDD)**

```
01_EXECUTIVE_SUMMARY
├─ Executive summary (2p)
├─ One-pager (pricing, terms)
├─ Company presentation (10-15 slides)
└─ 3-year plan & projections

02_FINANCIAL
├─ P&L (12 derniers mois, monthly + annuel)
├─ Balance sheet (derniers 3 ans)
├─ Cash flow forecast (12-24 mois)
├─ ARR breakdown (top 20 clients)
├─ Churn analysis (monthly, by cohort)
├─ CAC & LTV calculations
├─ Bank statements (last 12 months)
└─ Tax filings (3 derniers years)

03_LEGAL_CORPORATE
├─ Articles of incorporation / SARL statuts
├─ Shareholders register & cap table
├─ Board minutes (last 12 months)
├─ Option pool & vesting agreements
├─ Non-compete & IP assignment agreements
├─ Conflict of interest disclosures
└─ Insurance policies (D&O, general liability)

04_INTELLECTUAL_PROPERTY
├─ Patent filings & registrations (all jurisdictions)
├─ Trademark registrations
├─ Copyright registrations
├─ Software source code (GitHub access ou zip)
├─ List of 3rd-party libraries (dependencies)
├─ Licenses used (open-source, proprietary)
├─ IP indemnification history
└─ Trade secret documentation (if any)

05_CONTRACTS_COMMERCIAL
├─ Customer contracts (template + top 20)
├─ Partner agreements
├─ Reseller agreements (if applicable)
├─ Supplier contracts (critical only)
├─ Employment agreements (C-suite + key hires)
├─ Consulting/advisor agreements
├─ Service level agreements (SLAs)
└─ Master service agreements (MSA templates)

06_CUSTOMERS_SALES
├─ Customer list (name, ARR, contract term, renewal date)
├─ Monthly cohort churn analysis
├─ Sales pipeline (forecast accuracy track record)
├─ Customer concentration (top 20 = [%] ARR)
├─ NPS survey results (last 2 cycles)
├─ Customer testimonials/case studies
├─ Account expansion initiatives
└─ Top 5 customer contact info (for buyer calls)

07_PRODUCT_TECHNOLOGY
├─ Product roadmap (12-24 months)
├─ Engineering team size & seniority
├─ Tech stack diagram
├─ Infrastructure costs (monthly breakdown)
├─ System architecture & scalability plan
├─ Security certifications (ISO 27001, SOC 2)
├─ Disaster recovery & backup plan
├─ Downtime history & incidents (last 24 months)
└─ API documentation & integrations

08_MARKETING_GROWTH
├─ CAC calculation & payback
├─ Marketing spend breakdown (channels)
├─ Brand assets (logos, guidelines)
├─ Website analytics (Google Analytics)
├─ Social media metrics
├─ Organic vs paid breakdown
├─ Retention curves & cohort data
└─ Growth initiatives (last 12 months results)

09_COMPLIANCE_RISKS
├─ Data protection & GDPR compliance
├─ Privacy policy & T&C audit
├─ Security incidents history (if any)
├─ Litigation history (if any)
├─ Regulatory requirements by market
├─ Insurance coverage detail
├─ Data breach response plan
└─ Vendor risk assessments

10_PEOPLE_ORGANIZATION
├─ Org chart
├─ Team headcount & budget
├─ Key person life insurance policies
├─ Compensation philosophy
├─ Hiring plan (next 12 months)
├─ Engineering turnover history
├─ Top 10 bios
└─ References (former employees, if ok)

11_OPERATIONAL
├─ Business plan execution (roadmap vs actuals)
├─ Quarterly board decks (last 4 quarters)
├─ Monthly metrics dashboards
├─ Standard operating procedures (key processes)
├─ Vendor contracts (hosting, tools, etc.)
└─ Facility agreements (if any)

12_MISCELLANEOUS
├─ Loan agreements (if any debt)
├─ Subscription services audit
├─ Related-party transactions
├─ Founder background & credentials
└─ Awards & recognitions
```

---

## **CRITICAL FILES (Minimum Viable Data Room)**

Pour démarrer VDD sans tout avoir :

### ✓ MUST-HAVE (Jour 1)

1. **Executive summary** (1–2 pages)
2. **Financial model** — P&L 12 mois (monthly) + 3-year projection
3. **Customer list** — ARR, churn, retention
4. **Cap table** — qui possède combien (%)
5. **Key contracts** — customer top 5, employment key hires
6. **IP assignment** — preuve que tu possédes le code
7. **Org chart** + bios founders/CTO
8. **Pitch deck** (15–20 slides)

### ◐ SHOULD-HAVE (Jour 2–3)

9. Board minutes (last 2 quarters)
10. Customer references (3–5 willing to talk)
11. Security & compliance certs
12. Tech stack & architecture overview
13. Vendor list & renewal dates
14. Tax filings (dernière année complète)
15. Employment agreements (all team)

### ◆ NICE-TO-HAVE (Jour 4+)

16. Patent filings
17. Detailed roadmap
18. Cohort analysis spreadsheet
19. Incident reports (security, uptime)
20. Former employees references

---

## **FORMAT STANDARDS**

- **Format :** PDF ou Excel (pas Word, pas PPT)
- **Naming :** `[DOSSIER]_[sujet]_[date].pdf` ex: `02_FINANCIAL_P&L_2025-06-12.pdf`
- **Redaction :** Masquer les noms clients confidentiels (keep ARR)
- **Confidentiality :** Chaque document : "CONFIDENTIAL - FOR AUTHORIZED RECIPIENTS ONLY"
- **Access control :** Password-protected dossier, unique login par buyer
- **Audit trail :** Tracer qui voit quoi & quand
- **Updates :** Ajouter nouvelles données daily (pas une seule upload)

---

## **TIMELINE STANDARD**

```
D0 :  Data room opens
      ├─ Buyer: First week = skim executive summary
      ├─ Buyer: 2nd week = deep dive financials + customers
      └─ Buyer: Weeks 3-4 = technical & legal due diligence

D7 :  Data room fully populated (if not earlier)

D21 : Buyer finishes initial review, sends data requests
      ├─ Interpret requests (often vague)
      └─ Upload follow-ups within 48h

D35 : Buyer full draft reports, negotiation points identified

D60 : Data room access expires OR deal closes
```

---

## **COMMON BUYER REQUESTS (& How to respond)**

| Request | What they want | How to respond |
|---------|---|---|
| "Explain negative growth last Q" | Temporary dip or structural decline? | Detailed breakdown: seasonality vs. churn |
| "Why did customer X leave?" | Is it churn or market indication? | Honest post-mortem + plan to prevent similar |
| "Breakdown ARR by customer segment" | Concentration risk? | Table: segment, #clients, ARR, churn |
| "Technology debt or modernization needed?" | Integration cost? | Roadmap prioritization + tech lead interview |
| "Key person dependencies?" | Can business run without founder? | Succession plan + team depth evidence |
| "Explain this expense spike" | Burn spike or one-time? | Annotate with reason (hiring, marketing, etc) |
| "Customer NPS & satisfaction" | Product-market fit signal? | NPS trend + qualitative feedback |

---

## **RED FLAGS TO AVOID CREATING**

❌ **Missing documents** → Looks like you're hiding something
❌ **Inconsistent numbers** → P&L vs bank statements mismatch
❌ **Outdated financials** → Should be current month actuals
❌ **Customer concentration hidden** → Transparency is trust
❌ **IP ownership unclear** → Legally risky for buyer
❌ **Unresolved litigation mentioned** → Detail it fully
❌ **Founder in 5 customer relationships only** → Key person risk

**Best practice :** Over-disclose early. Trust builds faster than suspicion erodes.

---

## **CHECKLIST BEFORE OPENING DATA ROOM**

- [ ] All numbers cross-checked (P&L vs bank vs tax)
- [ ] Top 20 customers manually verified (ARR, churn, NPS)
- [ ] IP ownership documented & proven
- [ ] Org chart + bios current & accurate
- [ ] Litigation/disputes listed (even old resolved ones)
- [ ] Vendor contracts in folder
- [ ] Security certs valid & current
- [ ] Redaction plan for sensitive items
- [ ] Key person interviews pre-recorded (optional but good)
- [ ] Lawyer reviewed all legal docs

---

## **Pro Tips**

1. **Use Intralinks or Box**, not Google Drive (buyer expects institutional setup)
2. **Add Q&A function** — buyer leaves questions, you answer within 24h
3. **Version control** — if you update P&L, mark as "V2" + date
4. **Video intro** — CEO 5-min video ("Here's who we are, what we've built")
5. **Update daily** — shows momentum & engagement
6. **Be responsive** — buyer asks something? Answer in <24h = trust signal
## Related
