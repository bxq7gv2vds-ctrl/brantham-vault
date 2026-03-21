---
name: BeSoft Demand Model Calibration
description: Reverse-engineered demand model parameters from BeSoft historical data R1-R6, used to calibrate polytech-strategist engine
type: reference
---

# BeSoft Demand Model — Reverse-Engineering Results

## Model Architecture (likely MNL / market-share)

BeSoft uses a **market-share allocation model**:
1. Compute total market demand (base * seasonal * market factors)
2. Allocate shares via attractiveness scores (price, ads, sellers)
3. Each firm gets: total_demand × share_i

## Calibrated Parameters

### Base Demand
- **3,200 units/firm** (deseasoned, at avg market price)
- Validated: P1 F3 prediction=3,827 vs actual=3,826 (delta=1)
- Source: T0 was ~2,800/firm but described as "very quiet" quarter

### Price Elasticity
- **85 units per EUR** deviation from competitor average
- Source: P1 F3 (165.89, 3826) vs F4/F5 (170.00, 3477) = 349/4.11 = 84.9
- This is a **market share** effect, not total market expansion
- Works both ways: 1 EUR above avg → -85 units, 1 EUR below → +85 units

### Advertising Effect (hyperbolic diminishing returns)
- Formula: `300 * (1 - 3600 / advertising)`
- At 3,600 (minimum): 0 extra units
- At 5,000 (standard): +84 units
- At 7,500: +156 units
- At 10,000: +192 units
- At 15,000: +228 units
- Max theoretical: ~300 units (never reached)

### Seller Effect
- +250 units per seller above baseline of 2
- Commission: 750 units quota/seller, 4.32 EUR/unit above quota (verified)

### Market Memory
- 15% weight on (previous_sales - base_demand)
- Inertia: good period → slightly better next period

### Seasonal Indices (confirmed)
- Q1: 107, Q2: 108, Q3: 101, Q4: 84 (repeats)

## Validation Results

| Period | Firm | Predicted | Actual | Delta | Error % |
|--------|------|-----------|--------|-------|---------|
| P1 | F3 | 3,827 | 3,826 | +1 | 0.03% |
| P1 | F1 | 3,428 | 3,514 | -86 | 2.4% |
| P1 | F4 | 3,408 | 3,477 | -69 | 2.0% |
| P2 | F1 | 4,012 | 4,064 | -52 | 1.3% |

Residual errors (2-3%) likely from unknown inter-firm advertising/travel differences.

## Key Strategic Insights

1. **Price is king**: 85 units/EUR is massive. Undercutting by 5 EUR = +425 units.
2. **Advertising has diminishing returns**: going from 5K to 10K adds only 108 more units.
3. **3rd seller**: adds ~250 units but costs 10,800 salary + reduces commission threshold. Worth it only if margin > 43 EUR/unit (10,800/250).
4. **BOLT cannibalization**: from P3 onward, ATOM demand drops as BOLT grows (45% of market by P6). Temporal diffusion model, not price-driven.
5. **T0 is "quiet"**: actual first-period demand will be significantly higher than T0 reference.

## Files Updated
- `backend/engine/optimizer.py` — `estimate_demand()` recalibrated
- `backend/tests/test_analysis.py` — clamp range updated to [1500, 4500]
- `backend/tests/test_engine.py` — building depreciation corrected
