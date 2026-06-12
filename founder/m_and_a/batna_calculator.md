---
name: batna-calculator
description: Worksheet 10 min — calculer votre walk-away price (BATNA) en 5 scénarios
---

# BATNA Calculator — What's Your Minimum Price?

**Utilité** : définir votre walk-away price AVANT de parler à des buyers (sinon vous paniqueriez).

Remplissez les chiffres ci-dessous. Votre BATNA = la plus haute valeur parmi les 3 options.

---

## SCENARIO A : Raise Next Round

**Question:** "Si pas d'acquisition, je lève Series X."

### Fill in:
```
Current valuation (post-money): $______M
Equity dilution from next round: _____%  (typical: 20-30% dilution)
→ Post-dilution ownership:      _____%
→ Your stake value:             $______M
```

### Example:
```
Current post: $50M
Dilution:     25%
You own:      40%
Your stake:   50 × 0.40 = $20M (without sale)

Next round at 25% dilution:
  Ownership after: 40% × 0.75 = 30%
  Your stake:      30% × valuation_in_3_years
  
  Assume 3-year growth at 30%/year:
    Valuation:     $50M × 1.30^3 = $109M
    Your stake:    30% × $109M = $32.7M
```

**Your BATNA from this path: $________M**

---

## SCENARIO B : Stay Independent (No Raise, No Sale)

**Question:** "What if I just keep building without outside capital?"

### Fill in:
```
Current ARR:                     $______M
Expected growth rate (next 3y):  _____%/year (be conservative)
Target EBITDA margin (year 3):   _____%

Valuation at year 3:
  ARR at year 3:        $______M × (1 + ____%)^3 = $______M
  SaaS multiple applied:  ____x (typical: 5-15x for healthy SaaS)
  → Valuation:          $______M

Less your operating costs (50% of proceeds):
  → NET to you:         $______M
```

### Example:
```
Current ARR:        $2M
Growth:             40%/year
Year 3 ARR:         $2M × 1.40^3 = $5.5M

Multiple:           8x (healthy, independent SaaS)
Valuation:          $5.5M × 8 = $44M

Assuming you own:   60%
Your share:         $44M × 0.60 = $26.4M
```

**Your BATNA from this path: $________M**

---

## SCENARIO C : IPO Path (Long, risky, high upside)

**Question:** "Could I go public instead?"

### Fill in:
```
IPO timeline:                        18-24 months
Dilution for IPO prep (series C, D): _____%
Your ownership at IPO:               _____%

Assume IPO at 12x forward ARR:
  Forward ARR (IPO year):           $______M
  Valuation:                        $______M × 12
  → Enterprise value:               $______M
  Your stake:                       $______M
```

### Realistic Checks:
- 🚨 IPO costs $3-5M legal + admin. Doable only if >$10M ARR.
- 🚨 Lock-up period = 180 days (6 months) before you can sell.
- 🚨 Public company = boring, compliance-heavy (vs. M&A exit = done).

**Your BATNA from this path: $________M** (if applicable)

---

## SCENARIO D : Sell to Strategic Buyer (M&A)

**Question:** "What's a fair price if acquired?"

### Fill in:
```
Current ARR:                $______M
Fair multiple for vertical: ____x (ask your advisor)

Base valuation:             $______M × ____x = $______M
Synergy premium (typical):  +20% = $_____M
→ Fair enterprise value:    $______M
```

### Add: Earnout potential
```
Earnout percentage:         ____% (typical: 10-30%)
Earnout amount:             $______M
Probability of earning it:  ____% (be realistic: 50-70%)

Expected value:             $______M × ____% = $______M
```

### Example:
```
ARR:            $2M
Multiple:       8x (SaaS benchmark)
Fair value:     $16M

+ Earnout (25% of price):
  Earnout amount:   $4M
  Probability:      60%
  Expected value:   $4M × 60% = $2.4M

Total expected:     $16M + $2.4M = $18.4M
```

**Your BATNA from this path: $________M**

---

## DECISION MATRIX

| Path | Timeline | Certainty | Net to You | Notes |
|------|----------|-----------|-----------|-------|
| **Raise Next Round** | 2-3 years | 70% | $____M | Dilution, but more control |
| **Stay Independent** | 3+ years | 60% | $____M | Slowest, but keep 100% upside |
| **IPO** | 18-24m | 40% | $____M | Risky, only if >$10M ARR |
| **M&A Now** | 3-6m | 85% | $____M | Fastest, most certain |

---

## YOUR BATNA

**Maximum of the above paths:**

```
BATNA = max($____M, $____M, $____M, $____M)
      = $________M
```

This is your **walk-away price**. 

- If buyer offers < BATNA, you walk.
- If buyer offers ≥ BATNA, you consider it seriously.
- Your anchor price for negotiation = BATNA × 1.3

---

## Quick Rules

| Metric | Rule |
|--------|------|
| **Your ask** | BATNA × 1.3 (opens negotiations) |
| **Walk-away** | BATNA × 0.95 (your minimum) |
| **Deal sweetspot** | BATNA to BATNA × 1.5 |
| **Too low to consider** | < BATNA |

---

## Reality Checks

- **If all paths <$10M**: Consider if exit even makes sense (maybe stay indie)
- **If M&A >> other paths**: Take it. M&A is fastest, most certain.
- **If earnout would be >40%**: Walk. Earnout is risky; you don't control metric.
- **If fundraise < 3 years away**: M&A might be better (avoid dilution from Series X).

---

## Example Output

```
Raise Series C at $150M post:   $25M
Stay independent (3y):          $28M
IPO (18-24m):                   $35M (but risky)
M&A now at 7x ARR:              $30M

→ BATNA = $30M (M&A path)
→ Ask = $30M × 1.3 = $39M
→ Walk-away = $28M (Series C path)
→ Target zone = $28M–$40M
```

If a buyer offers $32M (+ 20% earnout = $38.4M expected):
- Above BATNA ($30M) ✓
- Below your ask ($39M) ✓
- **This is worth negotiating.**

---

**Last updated**: 2026-06-12
