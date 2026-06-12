# M&A Valuation Multiples Model

## Comprehensive Valuation Framework

### Multiples Matrix by Sector

#### Technology & Software Sector
| Multiple | Range | Application | Key Drivers |
|----------|-------|-------------|-------------|
| **EV/Revenue** | 4-8x | Early stage | Growth rate, customer base |
| **EV/EBITDA** | 18-30x | Mature SaaS | Profitability, retention |
| **EV/EBIT** | 15-25x | Pre-profit | Revenue quality |
| **EV/Gross Profit** | 3-6x | Service businesses | Margin efficiency |
| **Revenue/Employee** | 200k-500k | Talent efficiency | Productivity |

#### Healthcare Sector
| Multiple | Range | Application | Key Drivers |
|----------|-------|-------------|-------------|
| **EV/EBITDA** | 12-20x | Services | Regulatory compliance, growth |
| **Revenue/Bed** | 1M-3M | Hospitals | Utilization rates, location |
| **EV/Prescription** | 50k-200k | Pharma | Pipeline strength, patents |
| **EV/Patient** | 5k-20k | Services | Patient volume, retention |
| **P/CF** | 15-25x | Public comps | Cash flow generation |

#### Industrial & Manufacturing
| Multiple | Range | Application | Key Drivers |
|----------|-------|-------------|-------------|
| **EV/EBITDA** | 8-14x | Mature operations | Asset efficiency, margins |
| **EV/Revenue** | 0.8-1.5x | Commodity-driven | Capacity utilization, cycles |
| **EV/EBIT** | 6-12x | Cyclical businesses | Earnings quality |
| **P/Book Value** | 1.5-3x | Asset-heavy | Asset quality, ROIC |
| **EV/EBITDA Capex** | 6-12x | Capital-intensive | Capex efficiency |

#### Consumer Sector
| Multiple | Range | Application | Key Drivers |
|----------|-------|-------------|-------------|
| **EV/EBITDA** | 10-18x | Brands | Brand strength, loyalty |
| **EV/Sales** | 1-3x | Retail | Same-store growth, margins |
| **EV/EBIT** | 8-15x | Diversified | Revenue mix, geographic |
| **Revenue/Store** | 2M-10M | Retail | Location, productivity |
| **EV/EBITDA Capex** | 8-15x | Consumer goods | Capex intensity |

### Valuation Methodology

#### Step 1: Select Comparable Companies
- **Market Cap**: Similar size (>€100M, €10-100M, <€10M)
- **Geographic**: Same region/market
- **Growth Stage**: Similar growth trajectory
- **Profitability**: Comparable margins
- **Capital Structure**: Similar leverage levels

#### Step 2: Calculate Key Multiples
```python
# Key Multiple Calculations
Enterprise_Value = Market_Cap + Debt - Cash
EV_Revenue_Multiple = Enterprise_Value / Revenue
EV_EBITDA_Multiple = Enterprise_Value / EBITDA
P_BV_Multiple = Market_Cap / Book_Value
Revenue_Employee_Multiple = Revenue / Employees

# Normalization Adjustments
Adjusted_EV = EV + Non_recurring_items - Excess_cash
Adjusted_EBITDA = EBITDA + Non_recurring_revenue
```

#### Step 3: Apply Industry-Specific Adjustments
- **Size Premium**: Smaller companies typically trade at discount
- **Growth Premium**: High growth commands premium multiple
- **Quality Premium**: Strong margins, customer concentration low
- **Risk Premium**: Higher risk = lower multiple

### Sector-Specific Valuation Considerations

#### Technology Sector Adjustments
- **SaaS Companies**: 
  - Rule of 40: Revenue growth + EBITDA margin >40%
  - Dollar-based retention >120%
  - CAC payback <18 months
- **Software Companies**: 
  - Maintenance revenue >20% of total
  - Product revenue growth >15%
  - Gross margins >70%

#### Healthcare Adjustments
- **Regulatory Risk**: FDA/EMA approval status
- **Patent Protection**: Years remaining, strength
- **Reimbursement Risk: Payment model stability
- **Clinical Data:** Trial success rates

#### Industrial Adjustments
- **Capacity Utilization:** >80% optimal
- **Asset Age:** <10 years ideal
- **Supply Chain:** Geographic diversity
- **Labor Relations:** Union presence

### Premium/Discount Application

#### Premiums (Add 20-50%)
- Market leadership (>25% share)
- Proprietary technology/IP
- Strategic fit (Brantham synergy)
- Strong management team

#### Discounts (Apply 20-50%)
- Concentrated customer base (>30% from top 3)
- Dependence on single product
- High regulatory risk
- Poor management track record

### Valuation Output Ranges

#### Strategic Value Range
- **Strategic Buyer**: 1.5x-2.0x Market Value
- **Financial Buyer**: 1.0x-1.5x Market Value
- **Market Price**: 1.0x Base Multiple

### Valuation Timeline & Validation

#### 3-Month Valuation Process
1. **Month 1**: Comps selection, multiple calculation
2. **Month 2**: Industry adjustments, premium/discount application
3. **Month 3**: Validation, sensitivity analysis

### Sensitivity Analysis Matrix

| Base Multiple | -10% Scenario | Base Case | +10% Scenario |
|---------------|---------------|-----------|----------------|
| **Low Growth** | 6.0x | 6.7x | 7.3x |
| **Base Case** | 7.2x | 8.0x | 8.8x |
| **High Growth** | 8.4x | 9.3x | 10.2x |

## Related
[[_system/MOC-patterns]]
[[brantham/_MOC]]

---
*Ce modèle de valuation permet de déterminer les multiples appropriés pour les cibles M&A en fonction du secteur et des caractéristiques spécifiques de l'entreprise.*