---
name: checklist-ip-audit
description: IP ownership verification before sale — patents, domains, contractors, open-source
metadata:
  type: checklist
  session: 2026-06-13-cycle1
---

# IP Audit Checklist — Pre-Sale Verification

**Do this 4-6 weeks before first buyer meeting. One surprise = $1-5M discount.**

## MUST-DO (Dealbreaker if Missing)

- [ ] **Patents:** All US + key intl inventors = your company (not founder). Get engineer confirmations.
- [ ] **Trademarks:** Company owns all (TM, UK, EU, Canada if applicable). Check USPTO + intl registry.
- [ ] **Domains:** Company owns all (DNS registrar shows company as admin, not founder personal email).
- [ ] **Source Code:** 100% assignment docs from all employees/contractors hiring on. Spot-check 3 contracts.
- [ ] **Open-Source Audit:** Run [FOSSA](https://fossa.com) or [Black Duck](https://www.blackducksoftware.com/) — zero GPL/AGPL in production.

## SHOULD-DO (Improves Valuation)

- [ ] **Trade Secrets:** NDA + non-compete docs signed by all employees (annual refresh).
- [ ] **Database Rights:** If EU customer, document data ownership + processing agreements.
- [ ] **Third-Party IP:** Document all Stripe/Twilio/AWS API usage (no custom fork/mod).
- [ ] **Logos / Brand:** Confirm designer did work-for-hire, transferred copyright to you.
- [ ] **Customer IP:** Any customer-provided content (integrations, workflows) clearly licensed to company.

## NICE-TO-DO (Shows Professionalism)

- [ ] **Copyright Registration:** US Copyright Office registration for main product (proof of ownership date).
- [ ] **License Audit:** All dependencies properly licensed (permissive vs restrictive).
- [ ] **Prior Art Search:** Document prior art if product = improvement on existing (reduces patent challenge risk).

## IF YOU FIND ISSUES

**Co-ownership with founder:**
- Get assignment letter from founder (with or without cash) before sale.
- Or: Indemnify buyer (reduce escrow).

**Missing contractor docs:**
- Email contractor asking for retroactive IP assignment (most comply).
- If refused: Estimate $50K legal cost to litigate; reduce deal value by this amount.

**GPL/AGPL in code:**
- Remove or relicense (if AGPL: impossible; if GPL: possible but risky).
- Or: Disclose to buyer + accept $500K+ discount.

**Third-party dependencies (Stripe, Twilio, etc.):**
- Verify terms allow change of ownership. Most do; some require customer approval.
- Document this with buyer pre-LOI.

## DOCUMENT TEMPLATE

Create a simple IP manifest (send to buyer during DD):

```
IP OWNERSHIP REGISTER

PATENTS
- [Patent Name] (US 10,123,456) → Company owns 100%, filed [date]

TRADEMARKS
- [TM Name] (US Reg. 5,123,456, Class XX) → Company owns 100%

DOMAINS
- company.com → Registered [date], transferred to company [date]

KEY EMPLOYEE IP ASSIGNMENTS
- [Employee Name] (CTO) → IP Assignment signed [date], all prior work covered
- [Employee Name] (Engineer) → IP Assignment signed [date]

OPEN SOURCE
- FOSSA audit completed [date], zero GPL/AGPL production dependencies

THIRD PARTY
- Stripe API integration → Standard terms, no custom fork
- Twilio API → Standard terms, change of ownership permitted
```

## NEXT STEPS

- [ ] Schedule 4-hour session to audit all IP docs
- [ ] Fix any missing contractor assignments (2-week buffer)
- [ ] Run open-source audit + remediate (4-week buffer if needed)
- [ ] Before first buyer call, share IP manifest with your lawyer
- [ ] Move to Tâche #6 (NDA Templates)

