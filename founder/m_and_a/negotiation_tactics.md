---
name: negotiation_tactics
description: Tactiques de négociation M&A par étape — positioning, leverage, scripts
metadata:
  type: reference
  format: playbook
  version: 1.0
---

# Negotiation Playbook — 5 étapes clés

---

## **ÉTAPE 1 : LOI — Positioning & leverage**

### Objective
Fixer prix et structure, garder optionné (pas binding sur toi, binding sur buyer).

### Tactiques vendeur

#### ✓ A : Créer urgence fausse
```
"Nous avons 2 autres acheteurs intéressés. 
Ton window est 10 jours si tu veux exclusivité."

Réalité: Peut être vrai ou bluff. 
Effet: Buyer presse, accepte moins bons terms
```

#### ✓ B : Anchorer prix haut
```
"Comparables: Notion sold @ 20x ARR, Figma @ 15x.
Nous: €1.5M ARR, €1M EBITDA → justifie 4-5x ARR."

Réalité: Comparables rarement pertinents (growth, market timing, exits vs acqui).
Effet: Buyer ancre perception haut
```

#### ✓ C : Garder options
```
LOI dit: 
- Price: €[X] (fixed)
- Earnout: €[Y] si retention ≥85% (optional pour buyer)
- Term: LOI binding sur confidentialité/exclusivité seulement

NOT binding: 
- À signer SPA (toi peux walk si DD change)
- À participer post-close (can negotiate rôle/earnout)
```

#### ✓ D : Insister data room = démarrage DD immédiat
```
"Data room opens demain, nous attendons buyer engagement."

Réalité: Si buyer lent à accéder data room = pas sérieux.
Effet: Filters out time-wasters, accelerates process.
```

### Buyer counter-tactics (et comment répondre)

| Buyer dit | Meaning | Réponse |
|-----------|---------|---------|
| "Prix dépend entièrement de DD" | Veut re-negotiate post-LOI | "Non, prix fixed dans LOI. Ajustements = NWC only." |
| "Earnout est trop bas pour nous" | Veut transférer risque à toi | "Earnout reflects toi risks. À toi de confiance." |
| "Nous voulons 90 jours exclusivité" | Veut bloquer concurrence | "45 jours. 90 si DD on-track." |
| "Founder must stay 5 years" | Indentured servitude | "3 ans max, avec rôle/compensation clair." |

---

## **ÉTAPE 2 : DATA ROOM — Due Diligence & information control**

### Objective
Give what's necessary, hide nothing material, control narrative around weaknesses.

### Tactiques

#### ✓ A : Pro-active disclose problèmes
```
"Vous verrez churn spike en Q2 2024. Reason: 
pricing change + competitor. 
We addressed via [product feature], churn back to 3% Q3."

Effet: Buyer less suspicious, no surprises.
Downside: Might negotiate lower price.
Upside: Closes faster (good faith), earnout more credible.
```

#### ✓ B : Provide interpretation, not raw data
```
❌ Send raw: "ARR_by_customer.csv" + silence

✓ Send: "ARR breakdown by segment, with context:
  Healthcare (€500k) = sticky, <3% churn
  SMB (€300k) = faster growth +25%, churn 8%
  Enterprise (€200k) = consolidated, few logos"

Effet: Narrative control, frame weakness as opportunity.
```

#### ✓ C : Limit access scope
```
"Data room access:
 ✓ Contracts, financials, customer list
 ✗ Full Git history (trade secrets)
 ✗ Employee emails
 ✗ Founder personal tax"

Réalité: Buyer can request, you can say no (within bounds).
```

#### ✓ D : Be responsive, win trust
```
Buyer asks: "Explain this expense spike in June"
Slow response: 10 days later = suspicious

Fast response: 24h later with data = trustworthy, shows goodwill.

Effect on price: +2-5% uplift from goodwill.
```

---

## **ÉTAPE 3 : TERM SHEET — Price & Earnout negotiation**

### Objective
Lock price before SPA, negotiate earnout structure to maximize payout probability.

### Tactiques

#### ✓ A : Start with highest credible ask
```
Initial ask:  4.5x ARR (€675k)
Buyer offers: 3.0x ARR (€450k)
Settle: 3.75x ARR (€562.5k) ← midpoint

vs.

Initial ask: 3.5x (€525k)
Buyer offers: 3.0x (€450k)
Settle: 3.25x (€487.5k) ← leaves money on table
```

**Rule:** Anchor 15-20% above target, negotiate down. Never start at target.

#### ✓ B : Decouple earnout from payout certainty
```
Buyer: "Earnout €100k if ARR grows 15%"
You: "Earnout €100k if ARR ≥ €[X] (today's growth baseline)
     Measured by [independent auditor]
     Payable in cash, not options"

Frame: Earnout = insurance you stay committed, not gamble on buyer.
```

#### ✓ C : Negotiate holding period separately from price
```
NOT: "€500k + 20% earnout vs. 30% earnout"

DO: "€500k cash at closing.
     + €50k earnout Y1 (retention ≥85%)
     + €50k earnout Y2 (churn <5%)"

Effect: Clearer, less aggregate risk, easier payout.
```

#### ✓ D : Use "walking point" to set credibility
```
"Our walk-away is 3.5x ARR or better terms elsewhere.
Anything below = we stay independent."

Credibility: Have real alternative (other buyer, or staying independent).
Effect: Buyer knows you're serious, pressure moves to them.
```

### Common objections & rebuttals

| Buyer says | Rebuttal |
|-----------|----------|
| "3x ARR is market for your growth profile" | "Comparable [Company X] sold 4.2x, growth similar" |
| "Earnout is standard" | "Yes, if conditions clear. Ours are—what's missing?" |
| "Founders should stay longer = higher price" | "Role post-close determines commitment, not artificial tenure" |
| "Due diligence will determine final price" | "Price fixed in term sheet. DD adjusts via NWC only." |

---

## **ÉTAPE 4 : SPA — Final legal **

### Objective
Lock down reps, warranties, indemnities to minimize holdback risk.

### Tactiques

#### ✓ A : Limit rep/warranty duration
```
Default (buyer): All reps survive 18-24 months

Better (vendeur): 
  - General reps: 12 months
  - IP reps: 18 months
  - Tax reps: 3-5 years (per law, can't negotiate below)
  
Effect: Reduces post-close claim risk.
```

#### ✓ B : Set minimum claim thresholds
```
Holdback escrow: €100k

Claim process:
  - Individual claim <€5k: Not covered (basket)
  - Aggregate claims >€20k (tipping basket): Holdback pays 50-100%
  
Effect: Buyer won't sue over small issues.
```

#### ✓ C : Carve out knowledge qualifiers
```
❌ "Founder reps that: No litigation exists"
   → Founder liable even for unknown suits

✓ "Founder reps to best of knowledge: 
    No material litigation exists of which Founder is aware"

Effect: Limits liability to what you actually know.
```

#### ✓ D : Dispute resolution clause
```
Disagreement on earnout triggers:
  1st: Good faith negotiation (30 days)
  2nd: Arbitration (if <€50k at stake)
  3rd: Litigation (if >€50k)

Effect: Escalates cost of suing you for minor issues.
```

---

## **ÉTAPE 5 : CLOSING — Final power plays**

### Objective
Get wire transfer before signing, protect against last-minute changes.

### Tactiques

#### ✓ A : Wire before signature
```
Process:
1. Wire arrives in escrow
2. Escrow holds until signature confirmation
3. Post-signature, escrow releases

NOT: Sign first, wire "tomorrow"
```

#### ✓ B : Independent escrow agent
```
Holdback escrow: Neutral 3rd party (not buyer's bank)
  → Buyer can't unilaterally claim against escrow
  → Need your consent to release claims
```

#### ✓ C : Minimum closing condition
```
"Closing contingent on:
 ✓ Key 5 customers haven't notified departure
 ✓ No material adverse change since LOI
 ✓ Team agrees to offer letters"

Effect: Walk if surprise issue emerges.
```

#### ✓ D : Final walkthrough
```
24h before closing:
- Verify wire amount matches term sheet
- Verify holdback percentage correct
- Verify earnout conditions written as agreed
- Final customer calls (random 2-3 to confirm retention)

Effect: Catch last-minute errors before signing.
```

---

## **NEGOTIATION MINDSET**

### What to DO

✓ **Anchor first** — set expectation high
✓ **Move slowly** — every concession costs (time = pressure)
✓ **Document agreements** — written, not handshake
✓ **Walk away credibly** — have alternative (stay independent)
✓ **Give reasons** — "That's industry standard because..." vs. arbitrary
✓ **Separate people from problem** — "The escrow clause protects both of us"

### What NOT to do

✗ **Split the difference** — anchors you down in next round
✗ **Accept first offer** — signals you'll take worse
✗ **Show desperation** — "We really need to sell" = lose 20%
✗ **Bluff** — if caught, lose all credibility
✗ **Forget buyer's constraints** — they have board, financing, timeline limits too
✗ **Get emotional** — business is business

---

## **Quick-ref negotiation scripts**

### Respond to "We need to reduce price by 10%"
```
"I understand you found something in DD. What is it specifically? 
If it impacts revenue or profitability, we adjust via NWC. 
If it's a risk you're uncomfortable with, earnout covers that.
But base price is fixed per term sheet."
```

### Respond to "We need founder to stay 4 years"
```
"3 years is what we agreed. Beyond that, I have other opportunities.
If you want longer commitment, we can discuss specific role/comp, 
but 4-5 years is not sustainable for me personally."
```

### Respond to "Earnout is too risky for us"
```
"Earnout reflects execution risk post-close—mostly in your hands.
If you're uncomfortable with earnout, we can increase base price by [X%], 
but that increases your financial risk. Let's structure around confidence."
```
## Related
## Related
## Related
## Related
