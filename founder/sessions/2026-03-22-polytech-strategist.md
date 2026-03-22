---
date: 2026-03-22
project: polytech-strategist
duration: ~6h
---

# Session: Polytech Strategist — Calibration BeSoft + Redesign BP + Decision Engine

## Ce qui a ete fait

### 1. Calibration du modele de demande sur donnees historiques BeSoft

**Source:** 2 univers complets (R1-R6), 11 firmes, 12 periodes.

**Donnees extraites:**
- Univers 1 (6 firmes): `/Users/paul/Desktop/Besoft/` — screenshots + PDFs
- Univers Leo (5 firmes): `/Users/paul/Desktop/Besoft Leo/` — screenshots
- Donnees structurees: `vault/founder/data/besoft-historical-r1-r6.md`
- Calibration: `vault/founder/data/besoft-demand-model-calibration.md`

**Parametres calibres:**
- Base demand: 2800 → **3200** (valide P1 F3: prediction 3827 vs reel 3826)
- Elasticite prix: 50 → **85 units/EUR** (source: P1 F3 vs F4/F5, 349/4.11=84.9)
- Effet pub: 60 → **300 units max** (hyperbolic diminishing returns)
- Effet vendeur: 200 → **250 units/vendeur supplementaire**
- Reference prix: 176 → **172.80** (T0 reel)
- Clamp: [1500,4000] → **[1500,4500]** (P2 F1 a vendu 4064)

**Validation croisee:**
- Univers 1 P1 F3: erreur 0.03%
- Univers 1 P2 F1: erreur 1.3%
- Univers Leo P1 (5 firmes, tous a 172.50): erreur **0.7%**
- Base demand/firme identique quel que soit le nombre de firmes (ratio 0.989)

### 2. Audit complet et fix du moteur

**3 bugs critiques fixes dans le Monte Carlo:**
- Base competiteurs: 2800 → 3200 (surestimait market share de 14%)
- Coefficients prix: 15 et 50 → 85 (seul 85 calibre)
- Clamp MC: [500,5000] → [1500,4500]

**2 améliorations importantes:**
- Storage costs ajoutes: 2.50 EUR/unite stock PF
- Docstring building depreciation corrigee (432K/160=2700)

**Verification cout COGS P1:** prediction 476,418 vs reel 476,616 = 0.04% erreur.

### 3. Optimiseur de decisions recalibre

**Bugs critiques de l'optimiseur corrigés:**
- Prix: maximisait profit court terme (177 EUR quand concurrents a 170!). Fixe: cap strategique a market_avg + 2 EUR max.
- Publicite: recommandait minimum 3600 EUR. Fixe: calcul ROI optimal → **6100 EUR** (+1945 net).
- Travel: 5040 → **6000 EUR/vendeur** (historique gagnants: 5500-6700).
- MLT T1: 381K → **120K** cap (historique: 60K CT suffisait).

**Monte Carlo integre dans les decisions:**
- 1000 sims MC apres chaque calcul de decision
- Si P5 < -10K, prix flagge HIGH RISK automatiquement
- P5/P50/P95 + probabilite de profit retournes

### 4. Decouverte: parametres decisionnels BeSoft

**Salaire vendeur, commission, quota, travel sont des DECISIONS, pas des constantes!**
- Seller salary: le joueur choisit (pas d'augmentation auto)
- Commission rate: modifiable (4.32 → 4.50 dans les donnees)
- Quota/vendeur: modifiable (750 → 950 en P6)
- Travel/vendeur: modifiable (4824 → 6700)

### 5. Ajout de tous les champs BeSoft au formulaire

34 champs de decision ajoutes:
- Marketing national: 9 champs (BOLT, salaire, commission, quota)
- Export: 8 champs complets
- Production: BOLT + ATOM
- Previsions BeSoft: 4 champs auto-calcules par l'optimiseur
- DB Neon Postgres migree avec nouveau schema

### 6. Redesign frontend — Design system Brantham Partners

**3 iterations de design:**
1. Terminal vert Matrix → rejete (trop de vert)
2. Monochrome noir/gris → rejete (encore du blanc dans les composants)
3. **Design BP exact** → accepte:
   - DM Mono partout
   - Palette: #0c0c0c bg, #141414 cards, #e0e0e0 accent
   - Border radius 0px global
   - Sidebar: "POLYTECH / strategist", nav items `> page`
   - Eyebrow `> SECTION` pattern
   - KPI grids gap:1px, stat-cards BP

### 7. Nouvelles visualisations 3D

8 visualisations sur la page Modelisation:
1. Surface de Profit 3D (prix x vendeurs → profit)
2. Surface de Demande 3D (prix x pub → demande)
3. Monte Carlo 3D scatter (10,000 simulations)
4. Score Competitif (radar)
5. Projection multi-trimestre (line chart)
6. **Break-even Surface 3D** (prix x production → zone profitable) — NEW
7. **Tornado d'impact** (barres horizontales, impact de chaque parametre) — NEW (remplace heatmap)
8. **Risk Cone** (fan chart P5-P95 sur 6 trimestres) — NEW

### 8. Strategic Brief PDF

Document genere: `/Users/paul/Desktop/POLYTECH_STRATEGIST_BRIEF.pdf`
- Style Jane Street, noir/blanc, DM Sans/Mono
- 8 sections: exec summary, calibration, historique, 10 regles, decisions T1, MC, strategie
- Aussi en HTML: `frontend/public/strategic-brief.html`

### 9. Fix deploiement Vercel

- Railway trial expire → migration backend sur Vercel serverless
- SQLite in-memory avec StaticPool pour Vercel (auto-seed a chaque cold start)
- DB Neon Postgres connectee (migration schema decisions 34 colonnes)
- Fonction definitions avant auto-seed (bug order)
- Traceback endpoint pour debug

## Decisions T1 recommandees par le modele

| Decision | Valeur |
|----------|--------|
| Prix ATOM | 175 EUR (cap market_avg+2) |
| Vendeurs | 3 |
| Salaire vendeur | 10,800 EUR |
| Quota | 750 unites |
| Commission | 4.32 EUR/unite |
| Travel/vendeur | 6,000 EUR |
| Publicite | 6,100 EUR |
| Production ATOM | 3,000 (max capacite) |
| MP | 6,000 x 4 livraisons (12.8% remise) |
| Emprunt MLT | 120,000 EUR |
| MC Prob Profit | 95% |
| MC P5 (worst) | +231 EUR |
| MC P50 (median) | +36,939 EUR |

## URLs
- Frontend: https://frontend-liart-omega-78.vercel.app
- Backend API: https://polytech-strategist.vercel.app
- GitHub: https://github.com/bxq7gv2vds-ctrl/polytech-strategist
- Brief PDF: `/Users/paul/Desktop/POLYTECH_STRATEGIST_BRIEF.pdf`

## Stack
- Frontend: Next.js 16, Tailwind, Plotly.js, Recharts
- Backend: FastAPI, SQLAlchemy, numpy, Neon Postgres
- Deploy: Vercel (both frontend + backend serverless)
- Tests: 272 pass

## Fichiers cles modifies
- `backend/engine/optimizer.py` — demand model + price strategy + MC validation
- `backend/engine/analysis.py` — Monte Carlo aligned (base 3200, elasticity 85)
- `backend/engine/costs.py` — storage costs, docstring fix
- `backend/engine/parameters.py` — seller salary increment
- `backend/database.py` — Vercel serverless SQLite StaticPool
- `backend/models.py` — 34 decision fields
- `backend/routes/decisions.py` — MC traceback, all new fields
- `frontend/src/app/globals.css` — BP design system
- `frontend/src/components/sidebar.tsx` — BP sidebar
- `frontend/src/components/modelisation/` — 3 new 3D viz
- `frontend/public/strategic-brief.html` — Jane Street brief

## Competition
- Date: 23-25 Mars 2026 (DEMAIN)
- Lieu: EDHEC BBA2 Lille
- Simulation: Polytech 3.0
- Objectif: **Premier de l'univers ET tous univers reunis**
