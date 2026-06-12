---
type: template
category: deal-evaluation
created: 2026-06-12
updated: 2026-06-12
---

# Template de Scoring de Deals M&A Distressed

*Template pour évaluation standardisée des opportunités d'acquisition*

## Instructions d'utilisation

Copier ce template pour chaque nouveau deal et compléter les sections. Le score final est pondéré et donne un indice de priorité (0-100).

```yaml
# Configuration du deal
deal_slug: "[slug-du-deal]"
entreprise: "[Nom entreprise]"
secteur: "[Secteur d'activité]"
source: "[Source d'annonce]"
date_evaluation: "YYYY-MM-DD"
evaluator: "[Nom de l'évaluateur]"
```

## Section 1: Qualification Juridique & Procédurale (Poids: 30%)

### 1.1 Statut Procédural
- [ ] **Liquidation Judiciaire** (+10) | **Redressement Judiciaire** (+8) | **Sauvegarde** (+6) | **Autre** (-5)
- [ ] **Tribunal compétent** : [ ] District [ ] Commerce [ ] Spécialisé (+2)
- [ ] **Délai restant** : [ ] >30j (+5) | [ ] 15-30j (+3) | [ ] <15j (-3)
- [ ] **Passif connu** : [ ] Oui (+3) | [ ] Partiel (+1) | [ ] Non (-5)

**Sous-total 1.1**: /20

### 1.2 Risques Juridiques
- [ ] **Contentieux majeur** : [ ] Aucun (+5) | [ mineur (+2) | [ ] Majeur (-5)
- [ ] **Procédures antérieures** : [ ] Aucune (+3) | [ ] 1-2 (+1) | [ ] >2 (-3)
- [ ] **Actions en responsabilité** : [ ] Aucune (+3) | [ ] En cours (-3) | [ ] Gagnées (-5)
- [ ] **Compatibilité repreneur** : [ ] Forte (+5) | [ ] Moyenne (+2) | [ ] Faible (-3)

**Sous-total 1.2**: /15

### 1.3 Cadre Temporel
- [ ] **Calendrier réaliste** : [ ] Oui (+5) | [ ] Conditionnel (+2) | [ ] Non (-3)
- [ ] **Flexibilité AJ** : [ ] Élevée (+3) | [ ] Moyenne (+1) | [ ] Faible (-2)
- [ ] **Période observation** : [ ] Stable (+2) | [ ] Fragile (-1) | [ ] Critique (-5)

**Sous-total 1.3**: /10

**Score Section 1**: /45 × 0.30 = **/13.5**

---

## Section 2: Viabilité Économique (Poids: 25%)

### 2.1 Chiffres Clés
- **CA Annuel** : [ ] € M
- **EBE** : [ ] € M
- **Marge EBE** : [ ] %
- **Taux de croissance CA** (3ans) : [ ] %
- **Endettement net/EBE** : [ ] x

**Scoring 2.1**:
- CA >10M€ (+5) | 5-10M€ (+3) | 2-5M€ (+1) | <2M€ (-2)
- EBE >15% (+5) | 10-15% (+3) | 5-10% (+1) | <5% (-3)
- Croissance >5% (+3) | Stable (+1) | Déclin (-2)
- Endettement <2x (+3) | 2-4x (+1) | >4x (-3)

**Sous-total 2.1**: /20

### 2.2 Rentabilité & Trésorerie
- [ ] **EBE positif** : [ ] Oui (+5) | [ ] Nul (+1) | [ ] Négatif (-3)
- [ ] **Cash flow opérationnel** : [ ] Positif (+3) | [ ] Nul (+1) | [ ] Négatif (-2)
- [ ] **Besoin de financement BFRE** : [ ] Géré (+2) | [ ] Modéré (+1) | [ ] Non géré (-3)
- [ ] **Trésorerie actuelle** : [ ] >3mois (+3) | [ ] 1-3mois (+1) | [ ] <1mois (-3)

**Sous-total 2.2**: /15

### 2.3 Position de Marché
- [ ] **Part de marché** : [ ] Leader (+5) | [ ] Positionnée (+3) | [ ] Fragile (+1) | [ ] Nulle (-2)
- [ ] **Portefeuille clients** : [ ] Diversifié (+5) | [ ] Concentré (+2) | [ ] Client unique (-5)
- [ ] **Contrats long terme** : [ ] >70% (+5) | [ ] 50-70% (+3) | [ ] <50% (+1)
- [ ] **Réseau fournisseurs** : [ ] Stabilisé (+3) | [ ] Renégocié (+1) | [ ] Rompu (-3)

**Sous-total 2.3**: /20

**Score Section 2**: /55 × 0.25 = **/13.75**

---

## Section 3: Potentiel de Transformation (Poids: 20%)

### 3.1 Synergies & Potentiel
- [ ] **Synergies évidentes** : [ ] Fortes (+5) | [ ] Modérées (+3) | [ ] Faibles (+1) | [ ] Aucunes (-2)
- [ ] **Potentiel de croissance** : [ ] Élevé (+5) | [ ] Moyen (+3) | [ ] Faible (+1)
- [ ] **Optimisation coûts** : [ ] >20% (+5) | [ ] 10-20% (+3) | [ ] <10% (+1)
- [ ] **Nouveaux marchés** : [ ] Accessibles (+3) | [ ] Potentiels (+1) | [ ] Difficiles (-2)

**Sous-total 3.1**: /20

### 3.2 Actifs Stratégiques
- [ ] **Propriété intellectuelle** : [ ] Forte (+5) | [ ] Modérée (+3) | [ ] Faible (+1) | [ ] Nulle (-2)
- [ ] **Marque & Reputation** : [ ] Forte (+5) | [ ] Établie (+3) | [ ] Limitée (+1)
- [ ] **Compétences clés** : [ ] Conservées (+5) | [ ] Replicables (+3) | [ ] Périssables (-2)
- [ ] **Infrastructure** : [ ] Adéquate (+3) | [ ] À améliorer (+1) | [ ] Inadéquate (-3)

**Sous-total 3.2**: /20

### 3.3 Risques de Transformation
- [ ] **Complexité intégration** : [ ] Faible (+5) | [ ] Modérée (+2) | [ ] Élevée (-2)
- [ ] **Dépendances clés** : [ ] Maîtrisées (+3) | [ ] Gérées (+1) | [ ] Critiques (-3)
- [ ] **Risques réglementaires** : [ ] Faibles (+3) | [ ] Modérés (+1) | [ ] Élevés (-3)
- [ ] **Obsolescence technologique** : [ ] Nulle (+3) | [ ] Mineure (+1) | [ ] Majeure (-3)

**Sous-total 3.3**: /20

**Score Section 3**: /60 × 0.20 = **/12**

---

## Section 4: Équipe & Opérationnel (Poids: 15%)

### 4.1 Équipe Direction
- [ ] **Dirigeant actuel compétent** : [ ] Oui (+3) | [ ] Partiellement (+1) | [ ] Non (-2)
- [ ] **Équipe clé présente** : [ ] Complete (+5) | [ ] Majorité (+3) | [ ] Fragile (+1) | [ ] Absente (-5)
- [ ] **Rotation de personnel** : [ ] Stable (+3) | [ ] Modérée (+1) | [ ] Élevée (-3)
- [ ] **Compétences techniques** : [ ] Fortes (+5) | [ ] Moyennes (+3) | [ ] Faibles (+1)

**Sous-total 4.1**: /20

### 4.2 Opérations & Processus
- [ ] **Processus documentés** : [ ] Oui (+3) | [ ] Partiellement (+1) | [ ] Non (-2)
- [ ] **Systèmes informatiques** : [ ] Fonctionnels (+5) | [ ] Partiels (+2) | [ obsolètes (-3)
- [ ] **Supply chain** : [ ] Stable (+5) | [ ] Gérée (+2) | [ ] Fragile (-2)
- [ ] **Qualité & certifications** : [ ] Certifiées (+5) | [ ] En cours (+2) | [ ] Absentes (-1)

**Sous-total 4.2**: /20

### 4.3 Facteurs Humains
- [ ] **Morale employés** : [ ] Positive (+3) | [ ] Neutre (+1) | [ ] Négative (-3)
- [ ] **Syndicats** : [ ] Absents (+3) | [ ] Apaisés (+1) | [ ] Conflictuels (-3)
- [ ] **CSE** : [ ] Collaboratif (+3) | [ ] Neutre (+1) | [ ] Hostile (-3)
- [ ] **Transfert de personnel** : [ ] Facile (+5) | [ ] Possible (+2) | [ ] Difficile (-3)

**Sous-total 4.3**: /20

**Score Section 4**: /60 × 0.15 = **/9**

---

## Section 5: Stratégique & Marché (Poids: 10%)

### 5.1 Alignement Stratégique
- [ ] **Stratégie repreneur cohérente** : [ ] Forte (+5) | [ ] Modérée (+3) | [ ] Faible (+1) | [ ] Inexistante (-2)
- [ ] **Segment cible viable** : [ ] Leader (+5) | [ ] Actif (+3) | [ ] Nouveau (+1) | [ ] Déclinant (-2)
- [ ] **Avantage concurrentiel** : [ ] Durable (+5) | [ **Temporaire (+3) | [ **None (-2)
- [ ] **Croissance organique** : [ ] Potentielle (+5) | [ ] Possible (+3) | [ ] Limitée (+1)

**Sous-total 5.1**: /20

### 5.2 Contexte Marché
- [ ] **Croissance secteur** : [ ] >10% (+5) | [ ] 5-10% (+3) | [ ] <5% (+1) | [ ] Déclin (-2)
- [ ] **Concentration marché** : [ ] Faible (+5) | [ ] Modérée (+3) | [ ] Élevée (+1) | [ ] Monopole (-2)
- [ ] **Innovation secteur** : [ ] Forte (+5) | [ ] Modérée (+3) | [ ] Faible (+1)
- [ ] **Réglementation** : [ ] Stable (+3) | [ ] Évolutive (+1) | [ **Volatil (-3)

**Sous-total 5.2**: /20

**Score Section 5**: /40 × 0.10 = **/4**

---

## Synthèse du Scoring

| Section | Score Pondéré | Score Brut | Poids |
|---------|---------------|------------|-------|
| 1. Juridique & Procédural | /13.5 | /45 | 30% |
| 2. Économique | /13.75 | /55 | 25% |
| 3. Transformation | /12.0 | /60 | 20% |
| 4. Équipe & Opérationnel | /9.0 | /60 | 15% |
| 5. Stratégique & Marché | /4.0 | /40 | 10% |
| **TOTAL** | **/52.25** | **/260** | **100%** |

### Interprétation du Score Final

- **90-100**: Deal exceptionnel - À suivre immédiatement
- **75-89**: Deal fort - Priorité haute
- **60-74**: Deal moyen - À qualifier plus avant
- **45-59**: Deal marginal - Risques importants
- **<45**: Deal à rejeter - Trop de risques

### Recommandation Finale

**Score obtenu**: [ ] /52.25

**Recommandation**:
- [ ] **GREEN LIGHT** (Score >70) - Proceed immediately
- [ ] **YELLOW LIGHT** (Score 50-70) - Proceed with conditions
- [ ] **RED LIGHT** (Score <50) - Reject or major restructuring

**Conditions si YELLOW LIGHT**:
1. 
2. 
3. 

**Risques principaux identifiés**:
1. 
2. 
3. 

**Next Steps**:
1. 
2. 
3. 

---

## Notes Complémentaires

_(Observations spécifiques, données contextuelles, exceptions au modèle)_

## Related
- [[brantham/deals/template]]
- [[brantham/analysis/pipeline-friction-points]]
- [[brantham/knowledge/process/end-to-end]]