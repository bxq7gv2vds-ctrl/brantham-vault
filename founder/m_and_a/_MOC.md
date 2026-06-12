# M&A — Master Index

## ⚡ QUICK START (pour aujourd'hui)
1. [Executive Summary 1-page](00_EXECUTIVE_SUMMARY.md) — Lire en 5 min
2. [Pre-M&A Self-Audit](self_audit_checklist.md) — Run checklist (15 min)
3. [BATNA Calculator](batna_calculator.md) — Définissez walk-away (10 min)
4. [Quickstart 90 jours](quickstart_90_days.md) — Lancez soft shop

## Outils Essentiels

### Nouveaux (Session 2026-06-12 — Volet Produit +13)
- [Executive Summary 1-page](00_EXECUTIVE_SUMMARY.md) — 5 Q critiques, order reading
- [Pre-M&A Self-Audit](self_audit_checklist.md) — Identify landmines before soft shop
- [BATNA Calculator](batna_calculator.md) — Walk-away price en 10 min
- [Email Templates](email_templates.md) — Outreach, LOI, closing logistics
- [Glossaire M&A 50 termes](glossaire_ma.md) — FR/EN, définitions concises
- [DCF Calculator (Python)](dcf_calculator.py) — Multi-scenario, outputs JSON
- [Deal Quick Scorecard](deal_quick_scorecard.md) — Score buyers en 5 min, prioritize
- [Buyer Outreach Playbook](buyer_outreach_playbook.md) — Cold to LOI en 90j (sequences, angles, rejections)
- [Integration 100-Day Brief](integration_100day_brief.md) — Post-close roadmap (team, produit, clients, opérations)
- [DD Customer Concentration Risk](dd_customer_concentration_risk.md) — Buyer's deep-dive (churn, stickiness, contracts)

### Nouveaux (Session 2026-06-12 — Volet Operationnel +13)
**Préparation (T-3m):**
- [Cost of Independence Calculator](calculator_cost_of_independence.py) — Comparez rester indépendant vs vendre (Python)
- [BATNA Card Template](template_batna_card.md) — 1-pager: quantifiez votre walk-away price
- [Narrative Building Guide](guide_narrative_building_saas.md) — Construire la story que les acheteurs veulent
- [Soft Shop Prep Checklist](checklist_soft_shop_prep.md) — 15 items avant le 1er contact

**Valuation (T-2m):**
- [Earnout Expected Value Script](script_earnout_expected_value.py) — Vraie valeur d'un earnout (Python)
- [SaaS Valuation Benchmarks 2026](benchmarks_saas_valuation_2026.md) — Multiples par ARR/croissance/catégorie
- [Anchoring & Pricing Guide](guide_anchoring_pricing_strategy.md) — L'art du "first number" en négociation

**Due Diligence (T+0 à T+8w):**
- [Financial DD Response Checklist](checklist_dd_financial_response.md) — 35 items: préparez vos finances
- [Reps & Warranties Guide](guide_reps_warranties_negotiation.md) — Négociez escrow sans tout sacrifier
- [Buyer Red Flags Matrix](matrix_buyer_red_flags.md) — Red flags par type (Strategic/PE/VC/Acqui-hire)

**Post-M&A (T+close):**
- [100-Day Integration Template](template_100day_integration_plan.md) — Jour 1 à jour 100: roadmap détaillé
- [Acqui-Hire Playbook](guide_acqui_hire_playbook.md) — Quand buyer veut l'équipe, pas le produit

### Fondations Existantes
- [Checklist Due Diligence Acheteur](checklist_due_diligence_acquereur.md) — 40-item scan avant acquisition
- [Red Flags M&A](red_flags_m_et_a.md) — 30+ signaux de risque majeur
- [Valuation DCF Template](valuation_dcf_template.md) — calcul enterprise value, scenarios
- [Deal Structures: Stock vs Asset](deal_structures_stock_vs_asset.md) — impacts fiscal/légal/risque
- [Playbook Négociation Vendeur](playbook_negociation_vendeur.md) — tactiques phase par phase
- [Buyer Profiles & Signaux](buyer_profiles_signals.md) — 5 archetypes d'acheteurs

## Architecture Générale

```
T-3m        Preparation
  ├─ BATNA definition
  ├─ Narrative building
  └─ Soft shop (2-3 buyers)

T-0         First contacts
  ├─ LOI negotiation (key terms)
  └─ Exclusivity period

T+0 to T+8w Due Diligence
  ├─ Data room management
  ├─ Tech/legal/financial audits
  └─ Price negotiation

T+8w        Closing
  ├─ Reps/warranties finalization
  ├─ Escrow structure
  └─ Closing conditions

T+0 (close)  Post-close
  ├─ Founder role definition
  ├─ Team retention
  └─ Earnout tracking
```

## Decision Trees

### Am I Ready to Sell?
```
✓ Product-market fit (50%+ YoY growth)
✓ Predictable revenue (recurring, low churn <7%/m)
✓ Team bench (not founder-dependent)
✓ Defensible moat (IP, network effects, or cost)
? Multiple options (strategic, PE, venture buyers)
→ If 4+ yeses = consider soft shop
```

### What Price Should I Ask?
```
Financial valuation:
  DCF (base case)           = $X
  Comps multiple (SaaS)     = Y× ARR
  
Negotiation strategy:
  Anchor at: max(DCF × 1.3, multiple × 1.2)
  Walk-away: min(DCF × 0.8, BATNA)
  Target zone: [BATNA, Anchor]
```

### Which Buyer Type is Best?
```
If want: control, long-term vision         → Venture buyer
If want: speed, highest price              → Strategic buyer
If want: synergies, operational leverage   → PE buyer
If want: passive return, no operational    → Financial buyer
If stuck: team hiring is only option       → Acqui-hire
```

## Metrics Tracked During Deal

| Phase | Metric | Target | Action if misses |
|-------|--------|--------|------------------|
| DD | Time to first question | <3d | slow buyer (renegotiate) |
| DD | Reps cap (% of price) | <1% | push back to 0.5% |
| DD | Earnout survival | <20% | reduce percentage |
| Closing | Holdback period | <18m | negotiate release schedule |

---

## Session Archives
- **2026-06-12**: Executive summary, self-audit checklist, BATNA calculator, email templates, glossaire 50 termes, DCF Python script

## Related Memories
- [[lat_arb_bot_m_and_a]] — if LAT-ARB Bot is acquirable target
- [[alliance_coiffure_valuation]] — if Alliance Coiffure M&A context
