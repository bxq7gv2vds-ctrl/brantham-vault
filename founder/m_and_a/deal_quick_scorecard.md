---
name: deal-quick-scorecard
description: One-page deal scoring matrix pour évaluer fit, valuation, risk en < 5 min
metadata:
  type: tool
  created: 2026-06-12
---

# Deal Quick Scorecard — 5-Minute Evaluation

Copy this table, fill, score each buyer/deal in 2-3 min. Threshold: 14+ = worth deeper dive.

## Format: /10 = Strategic importance (deal outcome) | RED/YELLOW/GREEN = Risk level

| Critère | Weight | /10 | Risk | Notes |
|---------|--------|-----|------|-------|
| **BUYER FIT** | | | | |
| Stratégique pour eux (vision match) | 15% | __ | ⚪ | Si 5-: reconsider |
| Vitesse de décision (historique) | 12% | __ | ⚪ | <60j ideal, >180j = no |
| Price realism vs ARR multiples | 15% | __ | 🔴 | <3x = lowball, >10x = magic |
| Post-deal role clarity | 10% | __ | ⚪ | Founder stay, scope, equity? |
| **DEAL VIABILITY** | | | | |
| Customer concentration risk | 12% | __ | 🔴 | >30% top 3 = breakable |
| Churn stability (last 12m) | 12% | __ | 🟡 | >8%/m = concern |
| Tech debt / rewrite risk | 10% | __ | 🟡 | Major code issues? |
| Cap table clean (no disputes) | 7% | __ | 🔴 | Any option litigation? |
| **GO/NO-GO** | | | | |
| | **TOTAL** | __/10 | | __ |

## Decision Rule

- **14+** → Advance to LOI conversation
- **11-13** → Data room lite + soft intelligence
- **<11** → Pass or fix critical item first

## Examples

### Deal A: SoftBank Strategic (saas + payment infra)
| Item | /10 | Risk | Why |
|------|-----|------|-----|
| Stratégique | 9 | 🟢 | Payment infra play = core |
| Vitesse | 7 | 🟡 | 120d typical (OK) |
| Price | 8 | 🟢 | 7x ARR in range |
| Role | 6 | 🟡 | Vague on founder role |
| Concentration | 8 | 🟢 | Top 3 = 22% |
| Churn | 9 | 🟢 | 2%/m |
| Tech debt | 7 | 🟡 | Monolith, needs care |
| Cap clean | 10 | 🟢 | Perfect |
| **TOTAL** | 7.7 | Mixed | → Worth LOI talks |

### Deal B: Unknown PE firm
| Item | /10 | Risk | Why |
|------|-----|------|-----|
| Stratégique | 4 | 🔴 | "Bolt-on play" (meh) |
| Vitesse | 3 | 🔴 | 9m typical (slow) |
| Price | 5 | 🔴 | 4x ARR offer = lowball |
| Role | 4 | 🔴 | Want full replacement |
| Concentration | 6 | 🟡 | 35% top 3 |
| Churn | 8 | 🟢 | Clean |
| Tech debt | 8 | 🟢 | Good team |
| Cap clean | 9 | 🟢 | Clean |
| **TOTAL** | 5.9 | ❌ PASS | → Not worth bandwidth |

---

## Quick Checklist Before Scoring

- [ ] ARR = trailing 12m revenue / 12
- [ ] NRR = (revenue_t1 + expansion - churn) / revenue_t0
- [ ] Churn = annual customer count loss / opening
- [ ] Top 3 customers = (sum revenue top 3) / total ARR
- [ ] Buyer's last 3 deals = time to close + paid multiple

**Use case**: Pinboard 15 inbound buyers in 60 min → prioritize call list.
## Related
