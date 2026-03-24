---
name: Session Competition Polytech 23 Mars 2026
description: T1 test round results, model recalibration, T1 real decision prep
type: session
---

# Session 23 Mars 2026 — Competition Polytech 3.0

## Contexte
- Competition EDHEC BBA2 Lille, 23-25 Mars 2026
- Simulation #4164, Univers 4, Firme 2
- 5 firmes dans l'univers
- T1 test (compte pour du beurre) joue aujourd'hui
- T1 real demain matin

## Resultats T1 Test — PREMIER

| Firme | CA | Prix ATOM | NI | Cash |
|-------|-----|----------|-----|------|
| F1 | 584,642 | 170.40 | 28,968 | -79,576 |
| **F2 (nous)** | **613,368** | **168.00** | **35,021** | **35,940** |
| F3 | 598,091 | 169.00 | 21,303 | -76,740 |
| F4 | 639,705 | 165.00 | 27,442 | -78,559 |
| F5 | 579,812 | 172.00 | 23,069 | -91,085 |

Marche total: 17,869 u | Vendeurs moyen: 2.20 | Pub moyenne: 4,800
Taux interet annuel prochaine periode: 5.00%

### Notre P&L T1 Test
- Ventes: 613,368 (3,651 u @ 168)
- COGS: 489,582
- Marge brute: 123,786
- Frais vente: 47,392 (salaires 21,600 + comm 9,292 + travel 12,000 + pub 4,500)
- Frais generaux: 27,000 (salaires 25,654 + charges 1,346 + storage 0)
- EBIT: 49,394
- Frais financiers: 2,700 (hypotheque seule, MLT commence T2)
- IS: 11,674
- NI: 35,021

### Notre Tresorerie T1 Test
- Encaissements: 603,840 (creances 483,840 + MLT 120,000)
- Decaissements: 635,566
- Cash fin: 35,940 (POSITIF — seuls en positif)

### Rapport Production T1 Test
- MP: 6,200 init + 8,000 achats (32.96/u) = 14,200 | consomme 6,000 | fin 8,200
- PF: 2,898 init + 3,000 prod (132.32/u) = 5,898 dispo | vendu 3,651 | fin 2,247
- CMP PF: 134.10

## Recalibration Modele

### Demande — Modele valide (+0.4% erreur)
Avec les prix concurrents reels (avg 169.10 excluant nous):
- Predit: 3,665 u
- Reel: 3,651 u
- Erreur: +0.4%

Base recalibree: 3,340/firme desaisonnalise (vs 3,300 avant, from 17,869/5/1.07 = 3,340)

### Corrections identifiees
1. **Storage costs = 0 en T1** (et probablement T2). BeSoft ne charge pas de storage au debut.
2. **Impot paye meme periode** (pas reporte). IS = 25% de EBT dans le meme trimestre.
3. **Interets MLT commencent T2** (pas T1). Frais financiers T1 = hypotheque seule (2,700).
4. **Taux de base = 5% annuel = 1.25%/trimestre**. MLT = 2.25%/trim, CT = 4.25%/trim, Decouvert = 5%/trim.
5. **MP commande = par livraison**. 8,000 × 4 = 8,000 recues/trim pendant 4 trims consecutifs.

### Evolution marche (donnees historiques P1-P6)
| Period | Marche/firme (Paul) | Marche/firme (Leo) | Croissance |
|--------|--------------------|--------------------|-----------|
| P1 | 3,572 | 3,532 | base |
| P2 | 3,716 | 3,548 | +2% |
| P3 | 3,168 | 3,095 | -14% (transition BOLT) |
| P4 | 2,692 | 2,679 | -14% (Q4 + transition) |
| P5 | 3,813 | 3,782 | +41% (export explose) |
| P6 | 4,431 | 3,944 | +10% |

### Rupture de stock sans machine supplementaire
Simulation avec cap 3,000 (T1-T4) puis 2,880 (T5+):
- T1-T4: OK
- T5: RUPTURE (-882 u Paul, juste en Leo)
- T6: RUPTURE dans les 2 univers

### Decision machine: acheter 1 machine F en T3
- T3 = 10 trims restants > 6 breakeven
- Cap passe de 3,000 a 3,900
- Cash sera solide apres T1-T2 receivables
- MP: ajuster commande a 8,000/livraison quand machine achetee
- Evite rupture T5-T6

## Decision T1 Real (demain matin)

| Champ | Valeur |
|-------|--------|
| Effort BOLT | 0.00 |
| Prix ATOM | 168 |
| Prix BOLT | 0 |
| Vendeurs | 2 |
| Salaire vendeur | 10,800 |
| Quota | 750 |
| Commission | 4.32 |
| Travel/vendeur | 6,000 |
| Publicite | 4,500 |
| Production ATOM | 3,000 |
| Production BOLT | 0 |
| Machines F actives | 4 |
| Equipes | 1 |
| Taux utilisation | 1.00 |
| Commande MP | 6,000 |
| Nb livraisons | 4 |
| Machines achetees | 0 |
| Machines vendues | 0 |
| Emprunt CT | 0 |
| Emprunt MLT | 120,000 |
| Prevision CA | 621,264 |
| Prevision Resultat | 35,512 |
| Prevision encaissements | 603,840 |
| Prevision decaissements | 635,933 |

### Projections T1 Real
- Demande: 3,698 u (si concurrents avg ~169)
- Vendu: 3,698 u
- NI: 35,512
- Cash fin: 35,573

## Plan strategique T1-T7

| Trim | Prix | Vendeurs | Pub | Prod | MP | Machine | MLT |
|------|------|---------|-----|------|----|---------|-----|
| T1 | 168 | 2 | 4,500 | 3,000 | 6,000×4 | 0 | 120K |
| T2 | 167 | 2 | 4,500 | 3,000 | (contrat) | 0 | 0 |
| T3 | 166 | 3 | 4,500 | 3,900 | 8,000×4* | +1 | 0 |
| T4 | 163 | 3 | 4,500 | 3,900 | (contrat) | 0 | 0 |
| T5 | 164 | 3 | 4,500 | 3,780 | 8,000×4 | 0 | 0 |
| T6 | 164 | 3 | 4,500 | 3,780 | (contrat) | 0 | 0 |
| T7 | 163 | 3 | 4,500 | 3,780 | (contrat) | 0 | 0 |

*T3: nouveau contrat MP 8,000×4 pour couvrir la machine supplementaire (prod 3,900 × 2 = 7,800 MP)

## Avantages competitifs confirmes
1. **Cash positif**: seule firme sans decouvert. Les autres payent 5%/trim d'interets.
2. **MLT intelligent**: 120K a 2.25%/trim vs decouvert a 5%/trim pour les concurrents.
3. **Remise MP maximale**: 12.8% (32.96/u) via contrat 4 livraisons.
4. **Prix agressif calibre**: 168 = sweet spot memory effect + NI.
5. **Pub optimisee**: 4,500 (ROI max) vs industrie a 4,800.

## Webapp ameliorations session 23-24 mars

### Simulateur restructure
- Formulaire: 20 champs dans l'ordre exact BeSoft (BOLT, salaire, quota, commission, taux MO, machines vendues, emprunt CT)
- Prix decimaux (step 0.10, champ editable a cote du slider)
- Override ventes manuelles (0 = auto modele, >0 = force)
- Encaissements/Decaissements dans le panneau resultats

### Projections stocks
- Tableau T1-T7: production, vendu, stock PF fin, stock MP fin par trimestre
- Barres visuelles avec alertes RUPTURE
- Chart capacite vs ventes (barres avec marqueurs capacite)

### Trajectoires multi-periodes
- NI cumule T1-T7 avec 3 scenarios concurrents (optimiste/baseline/pessimiste)
- Price sweep: impact du prix T1 sur le NI cumule a T7 (162-176 EUR)
- Band d'incertitude + prix optimal baseline et robuste

### 4 bugs corriges dans le simulateur
1. CMP PF: hardcode 133.33 → dynamique (134.18, reel 134.10)
2. Tech director: en double (prod + admin) → retire des frais generaux (27,000 exact)
3. Interets MLT: factures en T1 → mis a 0 (BeSoft commence T2)
4. CMP MP T0: 37.80 → 35.65 (reel)
- Resultat: simulateur NI = 34,789 vs live 35,021 (**0.7% erreur**)

### Modele demand_model.py (backend)
- BOLT cannibalization timeline T1-T12
- Export volume estimation T4+
- Storage costs tiered formula exacte BeSoft (<3% erreur)
- Seller salary inflation +500/trim
- Production split ATOM/BOLT
- Export pricing local + 3 EUR
- Competitor price convergence
- Transition correction factors T3-T6 (MAE 2.7%)
