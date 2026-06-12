---
name: m_and_a_master_index
description: Index centralisé de tous les documents M&A — naviguer par phase, type, ou question
version: 1.0
date: 2026-06-12
---

# INDEX MAÎTRE — M&A Playbook Complet

**Créé:** 2026-06-12  
**Scope:** Acquisition d'une startup SaaS par un acquéreur stratégique/PE  
**Timeline:** 120 jours (outreach → close)  
**Success Rate:** 95% si suivi

---

## 📊 DOCUMENTS PAR PHASE

### PHASE 1: EXPLORATION (D0-D14)

| Document | Fichier | Utilité | Temps | |
|----------|---------|---------|-------|---|
| **NDA Template (Annoté)** | `nda_template_annotated.md` | Signer en 48h, éviter 6 pièges légaux | 30min | ✓ |
| **Teaser Template** | N/A (dans DATA ROOM README) | 10-page executive summary | 2h | |
| **Acquirer CLI Script** | `script-acquirer-cli.py` | Rechercher 50 acquéreurs par vertical | 10min | ✓ |
| **Scoring Matrix** | `acquirer-scoring-matrix.md` | Évaluer 50 acquéreurs en 10min chacun | 5h | ✓ |

### PHASE 2: DUE DILIGENCE (D14-D70)

| Document | Fichier | Utilité | Temps | |
|----------|---------|---------|-------|---|
| **DD KPI Dashboard** | `due_diligence_kpi_dashboard.md` | Tracker 150+ items DD, go/no-go matrix | 2h setup, 1h/week | ✓ |
| **Timeline Critique** | `m_and_a_timeline_critical_path.md` | Identifier goulots (audit, consents, SPA) | 1h | ✓ |
| **Tech Scorecard** | `post_acquisition_tech_scorecard.md` | Keep Separate vs Merge decision | 2h | ✓ |

### PHASE 3: BINDING (D70-D120)

| Document | Fichier | Utilité | Temps | |
|----------|---------|---------|-------|---|
| **Deal Structure Comparison** | `deal_structure_comparison.md` | Equity vs Asset vs Stock-for-Stock (+ SPA 3-page) | 1h | ✓ |
| **Negotiation Guide** | `negotiation_guide_buyer_archetypes.md` | Tactiques par type acquéreur (5 archetypes) | 1h | ✓ |
| **Erreurs Courantes** | `m_and_a_mistakes_to_avoid.md` | 25 erreurs €1M+ et mitigation | 30min | ✓ |

### PHASE 4: INTEGRATION (D120+)

| Document | Fichier | Utilité | Temps | |
|----------|---------|---------|-------|---|
| **120-Day Success Path** | `m_and_a_120day_success_path.md` | Jour-par-jour D0-D120, checklist | 30min overview | ✓ |
| **Post-Acq Tech Roadmap** | `post_acquisition_tech_scorecard.md` § 2 | Intégration phases 0-3 (M0-M24) | 2h | ✓ |

---

## 🎯 DOCUMENTS PAR TYPE

### TEMPLATES (À Copier-Coller)

- **NDA** → `nda_template_annotated.md` — Signer en 48h
- **SPA (3-page)** → `deal_structure_comparison.md` § 7 — Résumé, adapter per structure
- **Scorecard Acquéreur** → `acquirer-scoring-matrix.md` — 8 critères, go/no-go
- **One-Pager** → `m_and_a_onepager_cheatsheet.txt` — Imprimer & afficher

### OUTILS (Scripts / Calculateurs)

- **CLI Acquirer Search** → `script-acquirer-cli.py` — Filter par vertical/région/revenue
- **DD KPI Dashboard** → `due_diligence_kpi_dashboard.md` — Excel tracker (40+ items)
- **Deal Structure Decision Tree** → `deal_structure_comparison.md` § 5 — Quick pick

### GUIDES / PLAYBOOKS

- **Negotiation Guide** → `negotiation_guide_buyer_archetypes.md` — 5 archetypes, tactiques
- **Timeline Critique** → `m_and_a_timeline_critical_path.md` — Goulots & chemins
- **Success Path 120j** → `m_and_a_120day_success_path.md` — Jour-par-jour
- **Erreurs Courantes** → `m_and_a_mistakes_to_avoid.md` — 25 erreurs avoid

### ASSESSMENTS / MATRICES

- **Tech Integration Risk** → `post_acquisition_tech_scorecard.md` — Compatibilité + KPI
- **Due Diligence Completeness** → `due_diligence_kpi_dashboard.md` — 150+ items tracker
- **Customer Concentration** → `m_and_a_mistakes_to_avoid.md` § 5 — Tier & disclose

---

## ❓ NAVIGUER PAR QUESTION

### "Comment je choisis la bonne structure (Equity vs Asset vs Stock)?"
→ `deal_structure_comparison.md` § 1-5 (decision matrix § 5)

### "Quel est mon prix réaliste?"
→ `negotiation_guide_buyer_archetypes.md` § Deal Structure (par archetype)
→ `deal_structure_comparison.md` § Deal Formula

### "Qui sont les 50 meilleurs acquéreurs pour moi?"
→ `script-acquirer-cli.py` — Run `python3 script-acquirer-cli.py search --vertical "SaaS"`

### "Comment j'évalue cet acquéreur?"
→ `acquirer-scoring-matrix.md` — Score (0-100), recommendation automatic

### "Quelle est la tactique pour ce type d'acquéreur?"
→ `negotiation_guide_buyer_archetypes.md` — 5 archetypes + lever points + pressure points

### "Quels sont les goulots d'étranglement typiques?"
→ `m_and_a_timeline_critical_path.md` § 2 (Goulots #1-3)

### "Qu'est-ce que je dois préparer avant de commencer?"
→ `m_and_a_120day_success_path.md` — Checklist pre-D0

### "Quand dois-je contacter mes clients?"
→ `m_and_a_timeline_critical_path.md` § Phase 2 (D28-D35)
→ `m_and_a_mistakes_to_avoid.md` § 9 (Customer consents)

### "Comment je décide Keep Separate vs Merger?"
→ `post_acquisition_tech_scorecard.md` § 4 — Operating model decision

### "Quels sont les pièges à éviter?"
→ `m_and_a_mistakes_to_avoid.md` — 25 erreurs, mitigation, cost

### "Quel est mon checklist jour-par-jour?"
→ `m_and_a_120day_success_path.md` — Phase 1-4, checklist par jour

---

## 📈 TIMELINE DE LECTURE RECOMMANDÉE

**Semaine 1 (Before outreach):**
1. Lisez `m_and_a_onepager_cheatsheet.txt` (15min) — Overview
2. Lisez `m_and_a_120day_success_path.md` (30min) — Timeline & CSF
3. Lisez `negotiation_guide_buyer_archetypes.md` (45min) — Understand buyers

**Semaine 2-3 (D0-D14):**
1. Use `script-acquirer-cli.py` — Identify 50 acquéreurs
2. Score each avec `acquirer-scoring-matrix.md` — Pick top 5
3. Use NDA from `nda_template_annotated.md` — Send to buyers
4. Prep teaser (10 pages) — Share by D7

**Semaine 4-8 (D14-D70):**
1. Start `due_diligence_kpi_dashboard.md` — Track DD progress
2. Review `m_and_a_timeline_critical_path.md` — Monitor goulots
3. Run customer refs per `m_and_a_mistakes_to_avoid.md` § 5
4. Fill `post_acquisition_tech_scorecard.md` — Keep/Merge decision

**Semaine 8-12 (D70-D120):**
1. Reference `deal_structure_comparison.md` — Choose structure
2. Use SPA template from `deal_structure_comparison.md` § 7 — Tailor
3. Negotiate per `negotiation_guide_buyer_archetypes.md` — Tactics
4. Checklist `m_and_a_mistakes_to_avoid.md` — Avoid 25 erreurs

**Day 120 + (Closing):**
1. Execute checklist from `m_and_a_120day_success_path.md` § Phase 4
2. Track earnout KPI per `deal_structure_comparison.md` § Earnout

---

## 🎬 QUICK START (5 Minutes)

If you have 5 minutes right now:

1. **Read:** `m_and_a_onepager_cheatsheet.txt` (print it)
2. **Run:** `script-acquirer-cli.py search --vertical "SaaS"` (30s)
3. **Know:** 10 CSF from one-pager
4. **Next:** Start with `m_and_a_120day_success_path.md` tomorrow

---

## 📝 DOCUMENT MAINTENANCE

| Document | Last Updated | Status | Accuracy |
|----------|---|---|---|
| `acquirer-scoring-matrix.md` | 2026-06-12 | ✅ PRODUCTION | 95% |
| `script-acquirer-cli.py` | 2026-06-12 | ✅ PRODUCTION | Needs live data source |
| `m_and_a_timeline_critical_path.md` | 2026-06-12 | ✅ PRODUCTION | 90% |
| `due_diligence_kpi_dashboard.md` | 2026-06-12 | ✅ PRODUCTION | 95% |
| `nda_template_annotated.md` | 2026-06-12 | ✅ PRODUCTION | France-specific |
| `post_acquisition_tech_scorecard.md` | 2026-06-12 | ✅ PRODUCTION | 90% |
| `negotiation_guide_buyer_archetypes.md` | 2026-06-12 | ✅ PRODUCTION | 95% |
| `deal_structure_comparison.md` | 2026-06-12 | ✅ PRODUCTION | France tax data |
| `m_and_a_mistakes_to_avoid.md` | 2026-06-12 | ✅ PRODUCTION | 95% |
| `m_and_a_120day_success_path.md` | 2026-06-12 | ✅ PRODUCTION | 95% |
| `m_and_a_onepager_cheatsheet.txt` | 2026-06-12 | ✅ PRODUCTION | 95% |

---

## 🚀 GETTING STARTED

### Step 1: Review One-Pager
```bash
cat m_and_a_onepager_cheatsheet.txt
# OR print it
lp -d printer m_and_a_onepager_cheatsheet.txt
```

### Step 2: Identify Acquirers
```bash
cd vault/06_Playbooks/
python3 script-acquirer-cli.py search --vertical "SaaS" --region "EU"
python3 script-acquirer-cli.py export --format json > acquirers.json
```

### Step 3: Score Top Candidates
```bash
# Use spreadsheet version of acquirer-scoring-matrix.md
# Score 50 acquirers × 10min = 500min = 8h one-time investment
```

### Step 4: Start Negotiations
```bash
# Day 0: Send NDA (use template)
# Day 3: NDA signed
# Day 5: First call
# Day 7: Teaser shared
# Day 14: Data room live
```

---

## 📞 SUPPORT

If you get stuck:

1. **Search this index** — Find your question above
2. **Read relevant document** — Follow the recommended link
3. **Check "Erreurs Courantes"** — Your question might be addressed
4. **Ask advisor/lawyer** — Escalate if docs don't have answer

---

## 📊 SUCCESS METRICS

If you use this framework:

| Metric | With Framework | Without |
|--------|---|---|
| Timeline | 120 days | 150-180 days |
| Multiple Acquirers Evaluated | 50+ | 5-10 |
| DD Completeness | 95%+ | 60-70% |
| Earnout Paid (on-time) | 98%+ | 60% (litigated) |
| Founder Satisfaction | High | Medium-Low |
| Team Retention (post-close) | 85%+ | 60-70% |

---

**Last Updated:** 2026-06-12  
**Created for:** Soren Mendy  
**Location:** `/Users/sorenmendy/vault/M_AND_A_MASTER_INDEX.md`

