---
name: Framework d'analyse de cibles M&A
description: Framework systématique pour l'analyse et la qualification des opportunités M&A distressed
metadata:
  type: template
---

# Framework d'Analyse de Cibles M&A Distressed

## 📐 Phase 0: Sourcing & Qualification Rapide (Scorecard)

### Quick Scan - First Filter (0-15 min par deal)

| Critère | Score | Poids | Pondéré | Commentaires |
|---------|-------|-------|---------|--------------|
| **Statut procédure** | | 0.3 | | 0=LJ, 1=RJ, 2=SAUVEGARDE, 3=CONTINUE, 5=EN LIQUIDATION |
| **CA récent** | | 0.2 | | 0=<500k€, 1=500k-2M€, 2=2-10M€, 3=10-50M€, 4=>50M€ |
| **Viabilité business** | | 0.25 | | 0=non viable, 1=marge limitée, 2=correcte, 3=bonne |
| **Actifs identifiables** | | 0.15 | | 0=aucun, 1=faible, 2=moyenne, 3=forte |
| **Potentiel repreneur** | | 0.1 | | 0=aucun, 1=peu, 2=moyen, 3=fort |
| **TOTAL** | **/5** | **1** | **/5** | **GO/NO-GO: >3.5** |

**Trigger automatisé**: Si score < 3.5 → archiver ou passer à "low priority".

---

## 🔍 Phase 1: Due Diligence Approfondie

### 1.1 Vérification Juridique Obligatoire
```yaml
Statut légal: 
  - SARL/SAS/EURL/[autre]
  - Date immatriculation: YYYY-MM-DD
  - Capital actuel: €
  - Capital variable: [oui/non]
  
Procédure collective:
  - Type: [Liquidation/Redressement/Sauvegarde]
  - Date ouverture: YYYY-MM-DD
  - Tribunal: [Nom]
  - Administrateur: [Nom + contact]
  - Phase: [Observation/Conciliation/Redressement/Liquidation]
  
Créances prioritaires:
  - Fournisseurs: €
  - Fisc: €
  - Sécurité sociale: €
  - Salariés: €
```

### 1.2 Analyse Financière Structurée
```excel
Bilan (dernier exercice):
  - Actif total: €
  - Dettes totales: €
  - Capitaux propres: €
  - Trésorerie: €

Compte de résultat:
  - CA: €
  - EBE: €
  - Résultat net: €
  - Marge brute: %

EBITDA normalisé:
  - EBITDA reporté: €
  - Retraitements: €
  - EBITDA normalisé: €
  - Multiple sectoriel: x
  - EV théorique: €
```

### 1.3 Analyse Opérationnelle
```yaml
Personnel:
  - Effectif: []
  - Clés compétences: []
  - Taux turn-over: %
  
Clients:
  - Top 3 clients: % CA total
  - Concentration risque: [élevée/moyenne/faible]
  - Contrats en cours: []
  
Fournisseurs:
  - Top 3 fournisseurs: % achats totaux
  - Dépendance critique: [oui/non]
  
Actifs:
  - Immobilisations: €
  - Stocks: € ( jours CA)
  - Valeur marché estimée: €
```

---

## 📊 Phase 2: Qualification Scoring (Scorecard Détaillé)

### 2.1 Score Viabilité Business (sur 10)

| Indicateur | Score | Notes |
|------------|-------|-------|
| **Rentabilité sectorielle** | | 1-3 selon secteur |
| **Marge EBITDA normalisée** | | <0=1, 0-5%=3, 5-10%=6, >10%=10 |
| **Cash burn rate** | | >6 mois=1, 3-6=5, <3=10 |
| **Positionnement marché** | | 1=faible, 5=moyen, 10=fort |
| **Potentiel croissance** | | 1=aucun, 5=moyen, 10=fort |
| **TOTAL** | **/50** | **VIABLE: >30** |

### 2.2 Score Risques Structurels (sur 10)

| Risque | Score | Impact |
|--------|-------|--------|
| **Dépendance dirigeant** | | Forte: -3, Moyenne: -1, Faible: 0 |
| **Concentration client** | | >70%: -3, 40-70%: -2, <40%: 0 |
| **Dette cachée** | | Découverte: -5, Vérifiée: 0 |
| **Actifs surévalués** | | >30%: -3, 10-30%: -1, <10%: 0 |
| **Contentieux non déclaré** | | Majeur: -5, Mineur: -2, Aucun: 0 |
| **TOTAL** | **/25** | **RISQUE TOLÉRABLE: >15** |

### 2.3 Score Potentiel Repreneur (sur 15)

| Type repreneur | Score | Probabilité |
|----------------|-------|-------------|
| **Stratégique (même secteur)** | | 12-15 (synergies fortes) |
| **Financier (LBO)** | | 8-12 (ROI focus) |
| **International** | | 10-13 (croissance marché) |
| **Concurrent direct** | | 9-11 (consolidation) |
| **Opportuniste** | | 5-8 (prix bas) |
| **TOTAL** | **/15** | **POTENTIEL: >10** |

---

## 💡 Phase 3: Valorisation & Pricing

### 3.1 Multiples Application
```python
# Calcul multiple ajusté
multiple_sectoriel = get_multiple_sectoriel(sector)
decote_distressed = 0.4  # 40% base
decotes_structurelles = 0.0  # à calculer selon risques

multiple_ajuste = multiple_sectoriel * (1 - decote_distressed) * (1 - decotes_structurelles)

valorisation_ebitda = ebitda_normalise * multiple_ajuste

# Triangulation méthodes
multiples_range = valorisation_ebitda
patrimoniale_range = actif_net_reel
dcf_range = dcf_plan_repreneur

prix_offre_min = min(multiples_range, patrimoniale_range) * 0.9
prix_offre_max = max(multiples_range, dcf_range) * 0.8
```

### 3.2 Fourchette de Pricing
```yaml
Pricing strategy:
  - Baseline: € (méthode multiples)
  - Floor price: € (patrimoniale)
  - Ceiling price: € (DCF optimiste)
  - Target range: €€
  
Courtage considerations:
  - Commission standard: 5-8% du prix
  - Success fee: €€
  - Payment terms: [30% upfront, 70% closing]
  
Tribunal expectations:
  - Minimum acceptable: €
  - Expected range: €€
  - Maximum realistic: €€
```

---

## 🎯 Phase 4: Action Plan & Next Steps

### 4.1 Deal Pipeline Status
```yaml
Current stage: [analyse/teaser/acheteurs/contacts/approach/close]
Timeline:
  - Target date: YYYY-MM-DD
  - Critical path: []
  - Dependencies: []
  
Resources needed:
  - Analyst: [nom]
  - Writer: [nom]
  - Hunter: [nom]
  - Legal: [nom]
```

### 4.2 Action Items
```markdown
### Immediate (0-7 jours)
- [ ] Obtenir documents comptables complets
- [ ] Vérifier créances avec fournisseurs
- [ ] Valuer actifs clés
- [ ] Identifier 5 acheteurs potentiels

### Short-term (1-4 semaines)
- [ ] Rédiger teaser cible
- [ ] Approcher acheteurs qualifiés
- [ ] Préparer due diligence
- [ ] Négocier exclusivité

### Medium-term (1-3 mois)
- [ ] MOU signature
- [ ] Due diligence détaillée
- [ ] Due diligence légale
- [ ] Final pricing et terms
```

### 4.3 Risk Mitigation Plan
```yaml
Top 3 risks:
  1. [Risk description] → Mitigation: [action]
  2. [Risk description] → Mitigation: [action] 
  3. [Risk description] → Mitigation: [action]
  
Contingencies:
  - Plan B: [alternative strategy]
  - Exit strategy: [conditions]
  - Timeline buffer: [days]
```

---

## 📈 Phase 5: Monitoring & Tracking

### 5.1 Deal Score Summary
| Métrique | Valeur | Target | Status |
|----------|--------|--------|--------|
| **Qualification Score** | /50 | >40 | 🟢/🟡/🔴 |
| **Viabilité Business** | /10 | >6 | 🟢/🟡/🔴 |
| **Risque Structurel** | /10 | <4 | 🟢/🟡/🔴 |
| **Potentiel Repreneur** | /15 | >10 | 🟢/🟡/🔴 |
| **Pricing Range** | €€ | Acceptable | 🟢/🟡/🔴 |

### 5.2 Dashboard Indicators
```yaml
Health metrics:
  - Due diligence completeness: %
  - Acheteurs contacted: 
  - Responses positive: 
  - Competition level: [low/medium/high]
  
Timeline tracking:
  - Days in pipeline: 
  - Estimated close: 
  - Critical path items: []
```

## Related
- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
- [[brantham/mastery/finance/_MOC]]
- [[brantham/templates/dd-checklist]]

*Framework généré le 2026-06-12*