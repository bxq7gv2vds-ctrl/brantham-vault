---
name: ma-decision-flowchart-typical
description: Flowchart des décisions M&A typiques pour processus d'acquisition
type: pattern
created: 2026-06-12
---

# Flowchart des Décisions M&A Typiques

## 🔄 Processus d'Acquisition Complet

```
START
│
├─► SCREENING INITIAL (Target Identification)
│   │
│   ├─► Market Analysis → Go/No Go
│   │   ├── If NO → END
│   │   └── If YES → Continue
│   │
│   └─► Initial Fit Assessment → Go/No Go
│       ├── If NO → END
│       └── If YES → Continue
│
├─► PRE-DUE DILIGENCE (Preliminary Assessment)
│   │
│   ├─► Financial Health Check → Pass/Fail
│   │   ├── If FAIL → END or Reweight
│   │   └── If PASS → Continue
│   │
│   ├─► Strategic Alignment Score >7/10 → Pass/Fail
│   │   ├── If FAIL → END
│   │   └── If PASS → Continue
│   │
│   └───► Technical Due Diligence Brief → Pass/Fail
│       ├── If FAIL → END
│       └── If PASS → Continue
│
└─► DETAILED DUE DILIGENCE (Comprehensive Review)
    │
    ├─► Financial Audit → Pass/Fail
    │   ├── If FAIL → Negotiation or END
    │   └── If PASS → Continue
    │
    ├─► Technical Deep Dive → Pass/Fail
    │   ├── If FAIL → Integration Planning or END
    │   └── If PASS → Continue
    │
    ├─► Legal & Regulatory Review → Pass/Fail
    │   ├── If FAIL → Risk Mitigation or END
    │   └── If PASS → Continue
    │
    └───► Team Assessment → Pass/Fail
        ├── If FAIL → Retention Planning or END
        └── If PASS → Continue
            │
            └─► NEGOTIATION & CLOSING
                │
                ├─► Term Sheet Negotiation → Accept/Reject
                │   ├── If REJECT → Reweight or END
                │   └── If ACCEPT → Continue
                │
                └─► Final Approval → Go/No Go
                    ├── If NO → END
                    └── If YES → EXECUTE DEAL
```

---

## 🎯 Décisions Clés avec Critères

### 1. Screening Initial
**Decision Gate** : Continuer ou abandonner

**Critères** :
- Market size >€100M
- Revenue growth >15% YoY
- Strategic fit score >6/10
- Management team qualified
- No regulatory showstoppers

**Action** :
- If YES → Proceed to pre-due diligence
- If NO → Document reasons and end process

### 2. Pre-Due Diligence
**Decision Gate** : Investir ou non

**Financial Criteria** :
- Revenue >€10M (or >€5M for high growth)
- EBITDA >€1M (or clear path)
- Debt/EBITDA <4x
- Cash runway >6 months

**Strategic Criteria** :
- Synergy potential >20%
- Market position Top 5
- Technology stack compatible
- Customer base complementary

**Action** :
- If >7/10 → Full due diligence
- If 5-7/10 → Limited scope review
- If <5/10 → End process

### 3. Due Diligence Phase
**Decision Gate** : Valuation adjustment or proceed

**Critical Findings** :
- Financial adjustments >10% → Renegotiate valuation
- Technical debt >30% → Integration cost adjustment
- Legal liabilities → Warranties and reps adjustment
- Team retention risk → Earn-out structure

**Action** :
- If major issues → Price adjustment or terms change
- If minor issues → Proceed with contingencies
- If no issues → Continue to negotiation

### 4. Negotiation Phase
**Decision Gate** : Accept or reject deal structure

**Price Negotiation** :
- Final range within ±15% of target
- Multiple valuation methods aligned
- Market comps support price

**Terms Structure** :
- Earn-out terms realistic
- Warranties adequate
- Closing conditions achievable
- Risk allocation fair

**Action** :
- If terms acceptable → Sign term sheet
- If terms unacceptable → Counter or walk away

### 5. Final Approval
**Decision Gate** : Execute deal or not

**Final Checks** :
- All due diligence findings addressed
- Integration plan detailed
- Financing secured
- Regulatory approvals in process
- Team retention plans in place

**Action** :
- If all checks pass → Execute closing
- If critical items missing → Delay or cancel

---

## 🚦 Decision Trees par Type de Cible

### High-Growth Startup
```
Initial Screening →
├─ Traction >100K ARR → Continue
├─ Growth >30% YoY → Continue  
├─ Team experience → Continue
├─ Market validation → Continue
└─ IP ownership → Continue
    │
    └─ Valuation Focus:
    ├── EV/Revenue multiple
    ├── Growth trajectory
    ├── Market share potential
    └─ Exit timeline
```

### Mature Company
```
Initial Screening →
├─ Profitable history → Continue
├─ Market position → Continue
├─ Customer base stable → Continue
├─ Operations efficient → Continue
└─ Cash flow positive → Continue
    │
    └─ Valuation Focus:
    ├── EV/EBITDA multiple
    ├── Cash flow analysis
    ├── Competitive advantage
    └─ Synergy realization
```

### Technology Platform
```
Initial Screening →
├─ Tech stack modern → Continue
├─ API ecosystem → Continue
├─ Scalability proven → Continue
├─ Security compliance → Continue
└─ Development velocity → Continue
    │
    └─ Valuation Focus:
    ├── User metrics
    ├── Platform value
    ├── Network effects
    └── Integration potential
```

---

## ⚠️ Risk Decision Points

### High-Risk Triggers
- **Financial** : EBITDA miss >15%
- **Technical** : Security incidents <3 months
- **Legal** : Pending litigation >€1M
- **Regulatory** : Compliance issues blocking
- **Team** : Key departure >30% leadership

### Risk Mitigation Decisions
1. **Price reduction** : 20-30% for high technical debt
2. **Earn-out structure** : 30-50% based on performance
3. **Warranty adjustments** : Extended coverage for liabilities
4. **Integration timeline** : Extended for complex migrations
5. **Contingency planning** : Backup integration strategy

---

## 📊 Success Metrics for Process

### Efficiency Metrics
- **Process time** : <6 months from initial contact
- **Success rate** : >25% of initial targets executed
- **Integration speed** : <90 days full integration
- **Cost efficiency** : <5% of deal value in fees

### Quality Metrics
- **Target accuracy** : >80% of top 3 targets qualified
- **Price accuracy** : ±10% of fair value
- **Integration success** : >90% of synergies realized
- **Team retention** : >90% key employees retained

---

## Related
[[_system/MOC-patterns]]
[[brantham/_MOC]]
[[ma-analysis-template]]