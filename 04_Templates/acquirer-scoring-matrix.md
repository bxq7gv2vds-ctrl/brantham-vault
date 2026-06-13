---
name: acquirer-scoring-matrix
type: template
version: 1.0
date: 2026-06-12
---

# Matrice de Scoring Acquéreurs — Template

**Usage:** Évaluer et classer les acquéreurs potentiels par fit stratégique & capacité de closing.

---

## Score Global (0-100)

| Critère | Poids | Score (0-10) | Pondéré |
|---------|-------|--------------|---------|
| **Stratégie (fit produit + marché)** | 25% | _ | _ |
| **Capacité financière (cash/credit)** | 20% | _ | _ |
| **Track record M&A (closings passés)** | 20% | _ | _ |
| **Risque intégration technique** | 15% | _ | _ |
| **Risque légal/réglementaire** | 15% | _ | _ |
| **Risque culturel (CEO, governance)** | 5% | _ | _ |
| **SCORE TOTAL** | 100% | | **_/100** |

---

## Grille Détaillée — Stratégie (25%)

### Complémentarité produit
- [ ] **9-10:** Remplit un trou stratégique critique (data + produit crée un moat)
- [ ] **7-8:** Ajoute une feature attendue (no brainer pour users existants)
- [ ] **5-6:** Quelques synergies évidentes (cross-sell possible)
- [ ] **3-4:** Produit adjacent mais pas d'intégration naturelle
- [ ] **0-2:** Peu de fit (purement financier)

### Accès marché
- [ ] **9-10:** Ouvre 3+ nouveaux segments (SMB→Enterprise, EU, verticals fermés)
- [ ] **7-8:** 2 nouveaux segments majeurs ou distribution 10x existante
- [ ] **5-6:** 1 nouveau segment + growth 3x existant
- [ ] **3-4:** Cross-sell modéré (même base client)
- [ ] **0-2:** Pas de synergies commerciales

**Subtotal Stratégie:** `__/10`

---

## Grille Détaillée — Capacité Financière (20%)

### Liquidités + Capacité d'emprunt
- [ ] **9-10:** >5x enterprise value en cash liquid (M&A trophy) OU EBITDA >40% revenue (debt capacity infinie)
- [ ] **7-8:** 2-5x en cash OU EBITDA 25-40%
- [ ] **5-6:** 1-2x en cash OU EBITDA 15-25%
- [ ] **3-4:** <1x cash, EBITDA <15% (besoin financement tiers)
- [ ] **0-2:** Covenant risk élevé, refinancing en cours

### Intent signal (acquirer interest)
- [ ] **9-10:** CED engagé perso, budget approuvé, board mandate
- [ ] **7-8:** VP Business Dev a dit oui, process lancé
- [ ] **5-6:** Initial call okay, pas de mandate encore
- [ ] **3-4:** Inbound exploratory seulement
- [ ] **0-2:** Cold outreach / pas intéressé publiquement

**Subtotal Finance:** `__/10`

---

## Grille Détaillée — Track Record M&A (20%)

### Historique de closings
- [ ] **9-10:** 5+ deals >$10M en 3 ans, tous closed, intégration réussie
- [ ] **7-8:** 3+ deals, track record solide (0-1 fail)
- [ ] **5-6:** 2-3 deals avec 1 fail ou intégration lente
- [ ] **3-4:** 1-2 deals passés, pas clair
- [ ] **0-2:** Aucun M&A OU multiple fails publics

### Timing moyen (annonce → close)
- [ ] **9-10:** <4 mois (processus rapide & efficient)
- [ ] **7-8:** 4-6 mois (standard)
- [ ] **5-6:** 6-9 mois (slow but reliable)
- [ ] **3-4:** 9-15 mois (due diligence heavy)
- [ ] **0-2:** >15 mois OU jamais closed (abandon récurrent)

**Subtotal Track Record:** `__/10`

---

## Grille Détaillée — Risque Intégration Technique (15%, inverse)

### Compatibilité stack
- [ ] **9-10:** Même tech stack OU acquirer a pattern d'intégration agile (keep teams separate, API-first)
- [ ] **7-8:** Stack compatible (Python/JS, same cloud), minor retooling
- [ ] **5-6:** Different stack, refactor 3-6 mois plausible
- [ ] **3-4:** Major tech gap (monolith acquirer, microservices nous) + legacy debt chez eux
- [ ] **0-2:** Incompatibilité totale, full rewrite needed (death march 12+ mois)

### Plan d'intégration
- [ ] **9-10:** Acquirer a doc'd playbook (keep product separate, own eng team)
- [ ] **7-8:** Acquirer a géré integrations similaires avec succès
- [ ] **5-6:** Acquirer willing à discuter, no formal playbook yet
- [ ] **3-4:** Vague sur approach (probablement forced consolidation)
- [ ] **0-2:** "On fusionnera la tech" (red flag 🚩)

**Subtotal Tech:** `__/10`

---

## Grille Détaillée — Risque Légal/Réglementaire (15%, inverse)

### Compliance & enforcement
- [ ] **9-10:** Zero SEC/FTC flags, no active investigations, acquirer a legal bench
- [ ] **7-8:** Clean history, 1-2 resolved cases (immaterial)
- [ ] **5-6:** Minor FTC inquiry (resolved) OU one pending litigation
- [ ] **3-4:** Active investigation OU multiple pending cases
- [ ] **0-2:** Securities fraud OU willful GDPR violations (deal-killer)

### Regulatory overlap
- [ ] **9-10:** No overlap (different geographies/verticals)
- [ ] **7-8:** Minor overlap, no blocker
- [ ] **5-6:** Moderate (ex: GDPR in EU, FCA in UK)
- [ ] **3-4:** Significant (data privacy, healthcare, fintech)
- [ ] **0-2:** Likely merger review/antitrust challenge

**Subtotal Legal:** `__/10`

---

## Grille Détaillée — Risque Culturel (5%, inverse)

### Leadership stability
- [ ] **9-10:** Founder-led or veteran CEO (>5y tenure), board aligned
- [ ] **7-8:** Professional CEO with track record, stable board
- [ ] **5-6:** Recent CEO change (within 2y) OU known governance drama
- [ ] **3-4:** CEO succession risk imminent OR turnover spike
- [ ] **0-2:** C-suite revolving door, board conflict, known asshole founder

### Post-acquisition upside
- [ ] **9-10:** Founder staying, wants to build together (psychological buy-in)
- [ ] **7-8:** Key execs retained, financial incentives aligned
- [ ] **5-6:** Founder leaving but team staying, SOP earnout
- [ ] **3-4:** Team exodus risk (multiple key person quits announced)
- [ ] **0-2:** Acquirer known for "talent optimization" (euphemism for layoffs)

**Subtotal Culture:** `__/10`

---

## Hasil & Recommendation

**Score Total:** `__/100`

### Interpretation
- **90-100:** Green light — pursue aggressively (BATNA comparison needed)
- **75-89:** Good option — parallel track worth exploring
- **60-74:** Explore, but vet deeper (may have hidden issues)
- **45-59:** Secondary option — only if better not available
- **<45:** Yellow flag — proceed only if desperate (low enterprise value)

### Next Step
1. If **>80:** Schedule founder intro + LOI draft
2. If **60-80:** Request investor references + due diligence kick-off
3. If **<60:** Add to watch-list, revisit in Q2/Q3

---

## Exemple Rempli : "TechGiant Corp" (Acquirer potentiel)

| Critère | Score | Notes |
|---------|-------|-------|
| Stratégie | 8/10 | Comble gap product roadmap, 2 nouveaux segments |
| Finance | 9/10 | $2B cash, EBITDA 45%, board-approved mandate |
| Track Record | 7/10 | 4 deals en 2y, 1 fail, avg 5 mois close |
| Intégration Tech | 6/10 | Different stack (legacy Java vs our Go), refactor 6mo feasible |
| Légal | 9/10 | Clean history, no overlap réglementaire |
| Culture | 5/10 | Known for reorg post-deal, 30% attrition moyenne |
| **TOTAL** | **7.3 × 10 = 73/100** | Explore mais avec protections earnout |
## Related
## Related
## Related
## Related
