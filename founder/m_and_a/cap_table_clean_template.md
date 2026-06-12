---
name: cap_table_clean_template
description: Cap table complète (actions, options, SAFEs)
metadata:
  type: template
---

# Cap Table — Clean & Current

| Shareholder | Type | Shares | % Ownership | Vesting | Notes |
|---|---|---|---|---|---|
| **Founder A** | Common | 5,000,000 | 50% | 100% (vested) | CEO |
| **Founder B** | Common | 3,000,000 | 30% | 100% (vested) | CTO |
| **Investor A (Seed Round)** | Preferred Series A | 1,500,000 | 15% | 100% (vested) | Board seat |
| **Employee 1 (Engineer)** | Option Pool | 150,000 | 1.5% | 50% vested (4-yr vest) | Strike price $0.10 |
| **Employee 2 (Designer)** | Option Pool | 100,000 | 1% | 33% vested (4-yr vest) | Strike price $0.10 |
| **SAFE Holder (Pre-seed)** | SAFE | — | On conversion | Converts at Series A price | $100k invested |
| **Convertible Note** | Debt (converting) | — | On maturity | 20% discount | Matures Q2 2026 |
| **TOTALS** | | 9,750,000 | 100%+ (dilution reserve) | | |

**Critical items:**
- [ ] All options accounted for (granted + unvested pool)
- [ ] SAFEs terms clear (what triggers conversion?)
- [ ] No unclaimed shares (dead person clause?)
- [ ] Vesting schedules confirmed with each holder

