---
name: revenue-normalization-template-2
description: Spreadsheet template — EBITDA normalisé, add-backs courants, calcul pour 3 scenarii (conservative/base/aggressive)
metadata:
  type: reference
  project: M&A
  created: 2026-06-13
---

# Revenue Normalization Template

Utiliser pour calculer **Normalized EBITDA** = base pour multiples d'acquisition.

---

## Format Spreadsheet (à mettre dans Excel)

### Section 1: Revenue & Gross Profit (3 ans historique)

| Élément | 2023 | 2024 | 2025E |
|---------|------|------|-------|
| **Total Revenue** | $XXX | $XXX | $XXX |
| - COGS | (XXX) | (XXX) | (XXX) |
| **Gross Profit** | $XXX | $XXX | $XXX |
| **GP Margin %** | X% | X% | X% |

### Section 2: Operating Expenses

| Élément | 2023 | 2024 | 2025E | Notes |
|---------|------|------|-------|-------|
| Sales & Marketing | $XXX | $XXX | $XXX | Commission, ad spend, team |
| R&D | $XXX | $XXX | $XXX | Engineer salaries, infra |
| G&A | $XXX | $XXX | $XXX | Finance, admin, legal |
| **Total OpEx** | $XXX | $XXX | $XXX | |
| **EBITDA (reported)** | $XXX | $XXX | $XXX | = GP - OpEx |
| **EBITDA Margin %** | X% | X% | X% | |

### Section 3: Add-Backs (Non-Recurring, Non-Cash, Owner Perks)

| Add-Back | 2023 | 2024 | 2025E | Justification |
|----------|------|------|-------|---|
| **Stock-based compensation** | $X | $X | $X | Option grants to team |
| **Owner equity kicker** | $X | $X | $0 | (assume normalizé à 0) |
| **One-time costs** | $X | $X | $X | Acquisition, rebranding, restructure |
| **Non-recurring legal/tax** | $X | $X | $X | IP litigation, audit fees |
| **Excess owner benefits** | $X | $X | $0 | Car allowance, travel, personal |
| **Consulting fees (one-time)** | $X | $X | $X | Advisory, system implementation |
| **Total Add-Backs** | $X | $X | $X | |

### Section 4: Normalized EBITDA

| Élément | 2023 | 2024 | 2025E |
|---------|------|------|-------|
| **EBITDA (reported)** | $XXX | $XXX | $XXX |
| + **Add-Backs** | $XXX | $XXX | $XXX |
| = **Normalized EBITDA** | $XXX | $XXX | $XXX |
| **Norm. EBITDA Margin %** | X% | X% | X% |
| **3-yr Avg Norm. EBITDA** | — | — | **$XXX** |

---

## Calcul Valuation (3 Scénarios)

### Scenario Conservative (5.0–6.0× Norm. EBITDA)

```
Normalized EBITDA (2025E) × 5.5 = Enterprise Value
= $XXX × 5.5 = $M.X
```

**Rationale**: Market downturn, slowing growth, integration risk

### Scenario Base (7.0–8.0× Norm. EBITDA)

```
Normalized EBITDA (2025E) × 7.5 = Enterprise Value
= $XXX × 7.5 = $M.X
```

**Rationale**: Stable growth, strategic buyer, synergies

### Scenario Aggressive (9.0–10.0× Norm. EBITDA)

```
Normalized EBITDA (2025E) × 9.5 = Enterprise Value
= $XXX × 9.5 = $M.X
```

**Rationale**: High growth (>40% YoY), platform, defensible market

---

## Add-Backs Courants par Industrie

### SaaS / Tech
- [ ] R&D one-time costs (product pivot, platform rewrite)
- [ ] Sales commissions (if not recurring)
- [ ] Cloud infra optimization (post-acquisition economies of scale)
- [ ] Stock options (assume 5–8% of revenue, normalized)

### Marketplace / E-commerce
- [ ] Payment processing (acquirer has scale advantage)
- [ ] Advertising spend (one-time campaign)
- [ ] Fulfillment (buyer consolidates with own)

### Services / Agency
- [ ] Subcontractor costs (buyer hires directly)
- [ ] Principal's salary (assume $0 post-close if transitioning role)
- [ ] Client acquisition campaigns (non-recurring)

---

## Checklist: Quoi Inclure / Exclure

✅ **À inclure (add-backs valides)**
- Stock options (non-cash)
- One-time M&A costs (legal, advisory)
- Restructuring charges
- Litigation settlements (IP, employment)
- Owner perks not provided by buyer (car, travel)
- Platform-specific overheads buyer absorbs

❌ **À exclure (récurrent, cash)**
- Salaries équipe permanente
- Cloud hosting (buyer négocie même prix)
- Insurance, accounting (standard)
- Interest on debt (buyer refinance)

---

## Red Flags Que Buyer Contestera

1. **Add-backs > 30% du EBITDA** → Too aggressive, buyer pushes back
2. **Huge variance YoY** → Signals unsustainable business
3. **No growth in normalized revenue** → Buyer lowballs
4. **High customer concentration** → Adds risk, lowers multiple

---

## Données à Rassembler

- [ ] 3 years P&L (actuals)
- [ ] Equity compensation register (all options issued)
- [ ] AP/AR aging (timing of revenue recognition)
- [ ] Customer cohort analysis (MRR/ARR by cohort)
- [ ] Cloud hosting invoices (2 years)
- [ ] Any one-time invoices (legal, consulting, restructuring)

---

## Lié à:
- [[valuation_dcf_template]] — DCF alternative avec growth assumptions
- [[financial_normalization_template]] — Detail version avec scenarios
- [[rfi_buyer_template]] — Buyer questionnaire
