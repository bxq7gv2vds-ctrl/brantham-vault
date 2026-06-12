---
name: m_and_a_timeline_critical_path
type: template
version: 1.0
date: 2026-06-12
---

# Timeline M&A — Chemin Critique & Jalons

**Usage:** Planifier deal M&A de 3-9 mois. Identifier dépendances + chemins critiques. Éviter delays causés par "on attendait X pour faire Y".

---

## Timeline Standard : Annonce → Close (140-180 jours)

### PHASE 1 : EXPLORATION & TEASER (Jours 0-14)

| Jalon | Jour | Chemin | Owner | Dépendance | Slack |
|-------|------|--------|-------|-----------|-------|
| **Initial Contact** | D0 | Outbound (LI), Inbound (warm intro) | Founder | None | 0j |
| **Confidentiality Agreement Signed** | D3 | NDA (template from vault) | Legal | Contact | 2j |
| **First Substantive Call** | D5 | 60min call (CEO/VP Biz Dev) | Founder | NDA signed | 1j |
| **Teaser Shared** | D7 | 10-page teaser (product, market, traction) | FP&A | Substantive call | 2j |
| **Acquirer Interest Confirmed** | D12 | "Yes, we want to explore" + budget signal | Founder | Teaser positive feedback | 3j |
| **Mutual LOI Kick-off** | D14 | "Okay, let's talk structure" + data room access | Legal | Interest confirmed | 2j |

**Critical Path Slack:** 5-7 days total (if teaser flops → pivot to next acquirer by D21)

---

### PHASE 2 : DUE DILIGENCE (Jours 14-70)

| Jalon | Jour | Chemin | Owner | Dépendance | Duration |
|-------|------|--------|-------|-----------|----------|
| **Data Room Live** | D14 | VDR + 200+ docs (see checklist) | FP&A + Ops | Legal sign-off | 2j prep |
| **Tech Due Diligence Starts** | D18 | Acquirer CTO/team + our eng | CTO | Data room live | 3j setup |
| **Tech DD Review Meeting** | D25 | Acquirer Q&A + findings | CTO | Tech DD running | 1j |
| **Financial Due Diligence Starts** | D18 | Acquirer finance + our CFO/accountant | CFO | Data room live | 3j setup |
| **Audit & Tax DD** | D22 | Third-party auditors (acquirer's firm) | CFO + Lawyer | Financial DD | 4-6w |
| **Legal DD** | D20 | Contracts, IP, litigation, employment | Lawyer | Data room live | 3-4w |
| **Customer References** | D28 | Acquirer calls 5-10 top customers | BD | Tech + fin DD 30% done | 2w |
| **Employee & Cultural Assessment** | D30 | Acquirer HR + leadership interviews | HR | Interest solid | 1w |
| **Offer Guidance Provided** | D45 | "We're thinking $X range" + term sheet sketch | CFO | Tech/Fin/Legal mostly done | 2j |
| **Draft LOI Received** | D50 | Non-binding term sheet + structure | Lawyer | Offer guidance given | 3j review |
| **LOI Signed** | D60 | Mutual commitment (non-binding in France, binding post-signature = heads of terms) | Lawyer + CEO | Draft LOI approved | 5j negotiate |

**Critical Path Slack:** 10-15 days (if auditors slow → use external audit from last year)

---

### PHASE 3 : BINDING AGREEMENT (Jours 60-120)

| Jalon | Jour | Chemin | Owner | Dépendance | Duration |
|-------|------|--------|-------|-----------|----------|
| **SPA (Share Purchase Agreement) Drafted** | D65 | Full purchase agreement (60-80 pages) | Lawyer (M&A counsel) | LOI signed | 5-10j |
| **Reps & Warranties Insurance** | D70 | Quote R&W policy (2-3% of EV, 18-24mo tail) | Insurance broker | SPA 1st draft | 3-5j |
| **Closing Conditions Finalized** | D85 | Regulatory clearances, third-party consents, no material adverse change | Lawyer | SPA review rounds | 10-15j |
| **SPA Signed** | D95 | Binding agreement executed | CEO + Lawyer | Reps negotiated, R&W terms settled | 10j final round |
| **Closing Conditions Satisfied** | D115 | All conditions met (regulators, consents, no MAC) | Lawyer + Ops | SPA signed | 15-20j |
| **Closing (Wire + Equity Transfer)** | D120 | Cash wire, cap table transfer, keys handover | CFO + Legal | Conditions satisfied | 1j |

**Critical Path Slack:** 5-10 days (if regulator drags → escalate to CEO level at D100)

---

### PHASE 4 : INTEGRATION (Jours 120-180+)

| Jalon | Jour | Chemin | Owner | Dépendance | Duration |
|-------|------|--------|-------|-----------|----------|
| **Day 1 Integration Plan Executed** | D121 | Announce to team, acquirer's integration playbook begins | CEO + CTO | Closing done | 1j |
| **Earnout Period Begins** | D121 | 12-24 month earnout (if applicable) payout schedule | CFO | SPA signed | varies |
| **First Product Integration Milestone** | D150 | APIs live / data migration / user transition 50% complete | CTO | Tech integration roadmap | 30j |
| **Final Earnout Payout Window** | D360+ | Payout based on holdback terms (revenue targets, retention, etc) | CFO | 12mo performance metrics | 120j+ |

---

## Chemins Critiques : Où les Deals Traînent

### ⚠️ Goulot #1 : Audit (Jours 22-45)
**Cause:** Acquirer's Big 4 firm backlog. External auditors = 4-6 semaines.

**Mitigation:**
- **D10:** Proactively engage acquirer's audit firm (give them data early)
- **D15:** Use audited financials from dernière année si possible (avoid full reaudit)
- **D22:** Provide audit-ready pack (reconciliations, schedules) → saves 2 weeks

### ⚠️ Goulot #2 : Regulatory / Third-Party Consents (Jours 70-100)
**Cause:** Customer contracts avec change-of-control clauses, supplier agreements, licences.

**Mitigation:**
- **D20:** Audit all contracts for consent requirements (done in legal DD)
- **D60:** Pre-notify key customers (before LOI signed) that deal is coming
- **D75:** Submit regulatory filings (CNIL, if France; antitrust if big)
- **D90:** Chase down final consents (use acquirer's legal team for leverage)

### ⚠️ Goulot #3 : SPA Negotiation (Jours 65-95)
**Cause:** Reps & warranties, indemnification, escrow, earnout structure.

**Mitigation:**
- **D50:** Use template SPA (from vault) as baseline → cut negotiation time by 50%
- **D60:** Agree on R&W insurance cap early (avoid "we want $10M escrow" vs "we'll pay R&W premium")
- **D75:** Lock down earnout KPIs (don't fight over 2% variance in calculations at D100)

---

## Dépendances Critiques : À Ne Pas Oublier

```
D0:  Initial Contact
      ↓ (D3) 
D5:  Substantive Call + NDA signed
      ↓ (D5)
D7:  Teaser Shared
      ├─→ D12: Interest Confirmed
      │         ↓ (D2)
      │    D14: Data Room Live [critical]
      │         ├─→ D18: Tech DD Starts ─→ D25: Tech DD Review ─→ D45: Tech Sign-off [CRITICAL PATH]
      │         ├─→ D18: Financial DD Starts ─→ D22: Audit Starts ─→ D45: Audit Complete [CRITICAL PATH]
      │         └─→ D20: Legal DD ─→ D50: Legal Sign-off
      │
      └─→ D60: LOI Signed
           ├─→ D65: SPA Draft (depends on tech + fin DD done)
           ├─→ D70: R&W Insurance Quote
           ├─→ D85: Closing Conditions (regulatory, consents) [CRITICAL PATH]
           └─→ D95: SPA Signed
                ├─→ D115: Conditions Satisfied [CRITICAL PATH]
                └─→ D120: CLOSING ✅
```

---

## Checklist par Phase : Éviter les Surprises

### Phase 1 (Jours 0-14): Exploration
- [ ] NDA signed by day 3
- [ ] Founder + CTO have 1:1 calls (chemistry check)
- [ ] Teaser includes: team, traction (revenue/users), product roadmap, customer logos
- [ ] Acquirer's interest signal is explicit ("we want to move forward")

### Phase 2 (Jours 14-70): Due Diligence
- [ ] Data room has ≥ 200 docs (financials, tech, legal, ops)
- [ ] Tech DD scheduled within 3 days of data room go-live
- [ ] Audit firm engaged by day 20 (not day 30)
- [ ] Customer reference calls scheduled by day 28
- [ ] Offer guidance received by day 45 (else deal is slow)

### Phase 3 (Jours 60-120): Binding
- [ ] SPA 1st draft within 5 days of LOI (not 15 days)
- [ ] R&W insurance terms settled by day 75 (not day 100)
- [ ] All regulatory/consent requirements identified by day 60
- [ ] No surprises at closing table (all conditions known by D100)

### Phase 4 (Jours 120+): Integration
- [ ] Integration playbook documented pre-closing
- [ ] Key person retention agreements signed
- [ ] Earnout KPIs locked by SPA signature (no ambiguity later)

---

## Modèle de Durée : Estimateur Rapide

| Scenario | Total Duration | Reason |
|----------|---|---------|
| **Smooth deal** (strategic buyer, clean financials, no regulatory) | 120-140 jours | Fast-track audit + simple SPA |
| **Standard deal** (mid-size acquirer, normal DD scope) | 160-180 jours | Full audit cycle, 1-2 consent rounds |
| **Complex deal** (cross-border, regulated industry, big targets) | 240-300+ jours | Antitrust review, regulatory filings |
| **Rough deal** (multiple acquirers, negotiation cycles) | 200-240 jours | Competing bids slow process |

**Rule of Thumb:** Add 30 days to initial estimate. Subtract 20 days if audit is done pre-LOI.
## Related
## Related
## Related
