# M&A Deal Pipeline Scoring Model

## Deal Stage Progression Matrix

| Stage | Weight | Score 0-10 | Typical Timeline | Success Rate |
|-------|--------|------------|------------------|--------------|
| **Initial Contact** | 10% | Early signal quality | 1-2 weeks | 15% |
| **Preliminary Review** | 20% | Basic due diligence pass | 2-4 weeks | 35% |
| **LOI/NDA Stage** | 30% | Serious commitment | 4-8 weeks | 50% |
| **Full Due Diligence** | 25% | Comprehensive review | 8-12 weeks | 70% |
| **Closing** | 15% | Final execution | 2-4 weeks | 85% |

## Deal Score Calculation

### Lead Quality (30%)
- **Referral Source**: Management team (10) vs Cold contact (3) vs Network (7)
- **Deal Size**: >€50M (10), €10-50M (7), <€10M (4)
- **Sector Alignment**: Core focus (10), Adjacent (6), New (3)

### Financial Viability (25%)
- **Revenue Growth**: >20% (10), 10-20% (7), 0-10% (4), Negative (0)
- **EBITDA Margin**: >25% (10), 15-25% (7), 5-15% (4), <5% (0)
- **Debt/EBITDA**: <2x (10), 2-3x (7), 3-4x (4), >4x (0)

### Strategic Fit (20%)
- **Market Position**: Leader (10), Strong (7), Niche (4)
- **Technology**: Cutting-edge (10), Modern (7), Legacy (4)
- **Team Quality**: Exceptional (10), Strong (7), Adequate (4)

### Process Momentum (15%)
- **Decision Speed**: Fast (10), Medium (7), Slow (4)
- **Competition**: Limited (10), Moderate (7), Intense (4)
- **Seller Motivation**: Urgent (10), Standard (7), Reluctant (4)

### Execution Risk (10%)
- **Regulatory**: Low risk (10), Moderate (7), Complex (4), High (0)
- **Integration**: Simple (10), Moderate (7), Complex (4)
- **Financing**: Secure (10), In progress (7), Uncertain (4)

## Pipeline Health Indicators

### Green Zone (Healthy)
- 6+ active deals per quarter
- 20% conversion rate to LOI
- Avg. deal size >€25M
- <3 month average time-to-close

### Yellow Zone (Warning)
- 3-5 active deals per quarter
- 15-20% conversion rate
- Mix of deal sizes
- 3-4 month average time-to-close

### Red Zone (At Risk)
- <3 active deals per quarter
- <15% conversion rate
- Concentrated small deals
- >4 month average time-to-close

## Deal Momentum Score
```
Total Score = (Lead Quality × 0.3) + (Financial Viability × 0.25) + 
               (Strategic Fit × 0.2) + (Process Momentum × 0.15) + 
               (Execution Risk × 0.1)

Priority Levels:
- A Score: 80-100 → Immediate attention
- B Score: 60-79 → Regular monitoring  
- C Score: 40-59 → Slow track
- D Score: <40 → Consider dropping
```

## Related
[[_system/MOC-patterns]]
[[brantham/_MOC]]

---
*Ce modèle de scoring permet de prioriser les opportunités dans le deal pipeline et d'identifier les deals avec le meilleur potentiel de succès.*