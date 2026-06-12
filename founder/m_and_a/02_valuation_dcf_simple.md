# Valuation DCF Rapide — SaaS

## **Inputs (remplir 5 chiffres)**

| Variable | Bear | Base | Bull | Unité |
|----------|------|------|------|-------|
| **ARR actuel** | 500k | 500k | 500k | € |
| **Taux croissance Y1-Y3** | 40% | 60% | 80% | % |
| **Taux croissance Y4-Y5** | 20% | 40% | 50% | % |
| **Taux croissance Y5+** | 5% | 15% | 20% | % |
| **EBITDA margin Y5** | 10% | 25% | 40% | % |
| **WACC (discount rate)** | 12% | 10% | 8% | % |
| **Terminal growth** | 2% | 3% | 4% | % |

---

## **Calcul (5 ans explicites)**

### Année 1-5 Revenue
```
Y1 Revenue = ARR × (1 + growth_Y1)
Y2 = Y1 × (1 + growth_Y2)
Y3 = Y2 × (1 + growth_Y3)
Y4 = Y3 × (1 + growth_Y4)
Y5 = Y4 × (1 + growth_Y5)
```

### Free Cash Flow
```
FCF = Revenue × EBITDA_margin_expected
```

### Present Value (discount)
```
PV_Y1 = FCF_Y1 / (1 + WACC)^1
PV_Y2 = FCF_Y2 / (1 + WACC)^2
... (until Y5)
```

### Terminal Value
```
Terminal Value = FCF_Y5 × (1 + terminal_growth) / (WACC - terminal_growth)
PV_Terminal = Terminal Value / (1 + WACC)^5
```

### Enterprise Value
```
EV = Sum(PV_Y1..Y5) + PV_Terminal
```

---

## **Scenario Builder (copy cette grille)**

### BEAR Case
- ARR 500k, +40% growth, 10% margin
- EV = ~**€2.5M** (5x ARR)

### BASE Case
- ARR 500k, +60% growth, 25% margin
- EV = ~**€3.8M** (7.6x ARR)

### BULL Case
- ARR 500k, +80% growth, 40% margin
- EV = ~**€5.2M** (10.4x ARR)

---

## **Red Flags dans la Valuation**

- ❌ "On te paie 10x ARR à zéro margin" → Growth != profitabilité
- ❌ "Terminal growth = 10%" → Impossible pour SaaS mature
- ❌ "WACC = 20%" → Tu es vu comme très risqué
- ❌ "Margin Y5 = 60%" → Trop optimiste sans proof
- ✅ Conservative est crédible → Buyer plus respecte ta DD

---

## **Multiple de Sortie par Stage (benchmark 2024)**

| Stage | Multiple ARR | Context |
|-------|-------------|---------|
| Seed → A | 3-4x | High risk |
| Series A → B | 4-6x | Proven PMF |
| Series B → C | 6-10x | Scale phase |
| Series C+ (exit) | 8-15x | Mature SaaS |
| Sub-€100k ARR | 2-3x | Micro SaaS |

**Pour Alliance Coiffure (estimation)** : ~500k ARR → fourchette **3-5x = €1.5-2.5M**

