---
name: Session 2026-03-22 — Polytech Strategist Calibration
description: Full reverse-engineering of BeSoft demand model from 2 universes, model recalibration, Excalidraw brief creation
type: session
---

# Session 22 Mars 2026 — Polytech Strategist

## Ce qui a ete fait

### 1. Excalidraw brief pour video Loom
- `~/Desktop/brief-entreprise-T0.excalidraw` — 258 elements, hand-drawn style
- 7 slides horizontal: tresorerie, bilan, usine, equipe, couts, MP, saisonnalite
- Script voix off pour accompagner chaque slide

### 2. Reverse-engineering complet du modele BeSoft
- Lecture de TOUS les screenshots des 2 univers (36 screenshots Paul + 36 Leo)
- Extraction de chaque nombre: P&L, production, stocks, cash, competition report
- Analyse cross-universe: Paul (6 firms) vs Leo (5 firms)

### 3. Recalibration du modele de demande
Corrections appliquees dans `optimizer.py`:

| Parametre | Avant | Apres | Evidence |
|-----------|-------|-------|----------|
| Base demand | 3,200 | 3,300 | Paul desais=3,339, Leo=3,301 |
| Seller effect | 250 u/extra | 150 u/extra | Leo P2: +1 seller, demand dropped |
| Ads max | 300 u | 200 u | P2 residual: ~20u net, not 72 |
| Ad optimization | ROI at 6,100 | ROI at 5,100 | Coherent with new max=200 |

Precision: 2.2% → **1.5%** (pre-BOLT)

### 4. Decouvertes cles
- **BeSoft = MNL model**: marche total fixe, reparti par attractivite relative
- **competitor_prices EXCLUT own price**: valide par F3 exact match (0.0%)
- **3 marches separes**: local ATOM, local BOLT, export (ATOM+BOLT)
- **Export cannibalise le local** de 15-20% a partir de P4
- **BOLT cannibalise ATOM**: 5% → 45% du local en 4 periodes (identique 2 univers)
- **Storage costs**: formule exacte = 1000 + 1%(0-180K) + 2%(180K-540K) + 4%(>540K)
- **Commission**: exact P1-P2, diverge P3+ (probablement export/BOLT separes)

### 5. Push code
- 2 commits pushes sur `main`
- 272 tests green
- App recalibree et fonctionnelle sur localhost:3000/8000

## Fichiers crees dans le vault
- `vault/founder/data/besoft-demand-model-calibration.md` — UPDATED v2
- `vault/founder/data/besoft-complete-data-2-universes.md` — NEW
- `vault/founder/data/besoft-initial-state-T0.md` — NEW
- `vault/founder/data/besoft-10-golden-rules.md` — NEW
- `vault/_system/MOC-master.md` — UPDATED (ajout Polytech)

## Etat de l'app
- Backend: FastAPI localhost:8000, recalibre
- Frontend: Next.js localhost:3000, fonctionnel
- Monte Carlo: 95% prob profit, P5=341, P50=36,359 EUR
- 272 tests green
- Deploy: Vercel (frontend) + Vercel serverless (backend)

## Prochaines etapes
- Competition 23-25 Mars 2026
- Video Loom avec Excalidraw brief
- Utiliser l'app en temps reel pendant le jeu
- Recalibrer apres chaque round (saisir resultats + prix concurrents)

## Related
- [[_system/MOC-master]]
- [[brantham/patterns/teaser-onepager-html-pdf]]
- [[brantham/sessions/2026-03-22]]
- [[founder/sessions/2026-03-22-polytech-strategist]]
