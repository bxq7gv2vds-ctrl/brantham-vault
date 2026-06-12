# Buyer Scorecard — Matrice de Sélection

**Utilité** : évaluer et prioriser les acheteurs potentiels objectivement.

---

## Critères (10 dimensions)

| Critère | Weight | Scale | Notes |
|---------|--------|-------|-------|
| **Strategic Fit** | 20% | 1–5 | Does buyer solve customer problem? |
| **Financial Capacity** | 15% | 1–5 | Cash + ability to pay valuation |
| **Timeline** | 10% | 1–5 | Can close in 90–120 days? |
| **Tech Stack Alignment** | 10% | 1–5 | Integration effort (low = good) |
| **Cultural Fit** | 10% | 1–5 | Founders can work with buyer team |
| **Distribution Leverage** | 10% | 1–5 | Can buyer cross-sell to customers? |
| **Management Retention** | 10% | 1–5 | Will buyer keep team intact? |
| **Valuation Upside** | 10% | 1–5 | Likelihood of premium bid |
| **Regulatory Risk** | 5% | 1–5 | Antitrust, approval, timing |
| **Reference Score** | 5% | 1–5 | Prior acquisition track record |

**Score range** : 1=Very Poor, 2=Poor, 3=Neutral, 4=Strong, 5=Excellent

---

## Template (3 buyer examples)

```
╔════════════════════════════════════════════════════════════════════════╗
║                    BUYER A: BigCorp Corp (Public)                      ║
╠════════════════════════════════════════════════════════════════════════╣

Criterion              Weight  Score  Weighted  Notes
────────────────────────────────────────────────────────────────────────
Strategic Fit          20%     4      0.80      Complements product suite
Financial Capacity     15%     5      0.75      $2B cash, 20% acquired YoY
Timeline               10%     3      0.30      Board approval = 6 months (slow)
Tech Stack Align       10%     2      0.20      Different db, migrate cost $2M
Cultural Fit           10%     3      0.30      Bureaucratic, slow decisions
Distribution Leverage  10%     5      0.50      1M+ customer base overlap
Mgmt Retention         10%     2      0.20      Track record: 50% founder exodus
Valuation Upside       10%     4      0.40      Willing to pay 7–8x (good)
Regulatory Risk        5%      4      0.20      No antitrust concern
Reference Score        5%      3      0.15      Mixed integration history
────────────────────────────────────────────────────────────────────────
TOTAL SCORE                              3.80    "NEUTRAL-TO-STRONG"

RECOMMENDATION: Track, but not first choice (slow buyer, cultural risk)

────────────────────────────────────────────────────────────────────────

║                    BUYER B: ScaleUp Ventures (PE-backed)               ║
╠════════════════════════════════════════════════════════════════════════╣

Criterion              Weight  Score  Weighted  Notes
────────────────────────────────────────────────────────────────────────
Strategic Fit          20%     5      1.00      Product directly complements
Financial Capacity     15%     4      0.60      PE $300M fund, liquidity ready
Timeline               10%     5      0.50      PE-backed, 90-day close typical
Tech Stack Align       10%     4      0.40      Same cloud provider (easy)
Cultural Fit           10%     5      0.50      Founder-friendly, autonomy
Distribution Leverage  10%     4      0.40      350k customers, good overlap
Mgmt Retention         10%     4      0.40      Keep founders 2–3 years
Valuation Upside       10%     5      0.50      Will pay 8–10x (hungry)
Regulatory Risk        5%      5      0.25      Zero risk
Reference Score        5%      4      0.20      2 prior acqs, both successful
────────────────────────────────────────────────────────────────────────
TOTAL SCORE                              4.75    "STRONG"

RECOMMENDATION: PRIMARY TARGET. Contact immediately.

────────────────────────────────────────────────────────────────────────

║                    BUYER C: Industry Incumbent                          ║
╠════════════════════════════════════════════════════════════════════════╣

Criterion              Weight  Score  Weighted  Notes
────────────────────────────────────────────────────────────────────────
Strategic Fit          20%     3      0.60      Tangential product
Financial Capacity     15%     5      0.75      Fortune 500, unlimited cash
Timeline               10%     2      0.20      Corp approval = 12 months
Tech Stack Align       10%     1      0.10      Monolith legacy system (nightmare)
Cultural Fit           10%     1      0.10      Risk-averse, politics
Distribution Leverage  10%     3      0.30      Some customer overlap
Mgmt Retention         10%     1      0.10      Usually clean out founders
Valuation Upside       10%     2      0.20      Negotiation focused on price
Regulatory Risk        5%      2      0.10      Possible antitrust review
Reference Score        5%      2      0.10      1 acquisition (poor integration)
────────────────────────────────────────────────────────────────────────
TOTAL SCORE                              2.45    "POOR"

RECOMMENDATION: AVOID. Too slow, too risky culturally.
```

---

## Scoring Guidance

### Strategic Fit (20%)

**5** = Fills critical gap in buyer's product; customer asks for integration  
**4** = Clear synergy; solves known buyer problem  
**3** = Some relevance; buyer has related offering  
**2** = Tangential fit; buyer exploring but not urgent  
**1** = Wrong market; buyer doubtful fit  

### Financial Capacity (15%)

**5** = >$500M revenue, >10% operating margin, acquisition history  
**4** = $100–500M revenue, cash flow positive, some M&A  
**3** = $50–100M revenue, no PE backing, financing contingent  
**2** = $10–50M revenue, tight cash, no prior acquisitions  
**1** = <$10M revenue, bootstrapped, no acquisition capability  

### Timeline (10%)

**5** = Ready to close 60–90 days  
**4** = 90–120 day close realistic  
**3** = 120–180 day close (some approval delays)  
**2** = 6–9 months (requires board/financing)  
**1** = >12 months (strategic review ongoing)  

### Tech Stack (10%)

**5** = Compatible cloud, same DB, API-driven → 1 week integration  
**4** = Different but modern stacks → 3–4 week integration  
**3** = Some legacy but migrable → 2–3 month integration  
**2** = Mostly incompatible → 6+ month re-platform  
**1** = Legacy monolith, major re-architecture → 1 year+ migration  

### Cultural Fit (10%)

**5** = Founder-friendly, autonomy, fast decisions  
**4** = Professional but collaborative  
**3** = Some bureaucracy but functional  
**2** = Heavy process, slow decisions  
**1** = Political, founder hostile  

---

## Interpretation

| Score | Grade | Recommendation |
|-------|-------|-----------------|
| 4.5–5.0 | A | **PRIMARY** — contact immediately, exclusive talks |
| 3.9–4.4 | B+ | **STRONG** — contact in parallel, secondary option |
| 3.3–3.8 | B | **VIABLE** — keep warm, evaluate as backup |
| 2.7–3.2 | C | **WEAK** — contact if desperate, low priority |
| <2.7 | F | **AVOID** — time waste, cultural/strategic risk |

---

## Update & Reweight

**Re-score every 2 weeks** as you learn more:

- Buyer moves into/out of acquisition mode (score shifts ±1)
- New competing offer emerges (reweight timeline/valuation)
- Founders meet buyer team (cultural fit +/- 1–2 points)

---

## Export to Spreadsheet

```
Buyer Name | Strategic | Financial | Timeline | Tech | Culture | Distr | Mgmt | Valuation | Reg | Ref | TOTAL | Rank
──────────────────────────────────────────────────────────────────────────
BigCorp    | 4         | 5         | 3        | 2    | 3       | 5     | 2    | 4         | 4   | 3   | 3.80  | 2
ScaleUp    | 5         | 4         | 5        | 4    | 5       | 4     | 4    | 5         | 5   | 4   | 4.75  | 1
Incumbent  | 3         | 5         | 2        | 1    | 1       | 3     | 1    | 2         | 2   | 2   | 2.45  | 3
```

**Pro tip**: Sort by TOTAL score → focus on top 3–5 buyers. Contact all 5 simultaneously on day 1 (creates FOMO).
