---
type: pattern
project: brantham
date: 2026-03-12
category: scoring
tags: [scoring, qualification, m-and-a]
---

# Scoring Patterns

Patterns de decision pour la qualification des opportunites M&A distressed. Utilises par le Director et le systeme de scoring automatique.

## 5 Dimensions Cles

| # | Dimension | Poids | Ce qui compte |
|---|---|---|---|
| 1 | **Taille** | 30% | CA, effectif, total bilan. Sweet spot: 1-50M EUR CA, 10-200 salaries |
| 2 | **Secteur** | 25% | Attractivite sectorielle. Industrie/agro/tech > services generiques |
| 3 | **Procedure** | 20% | Type et stade. LJ > RJ > SV en urgence. RJ souvent meilleur deal. |
| 4 | **Actifs** | 15% | Qualite des actifs (immobilier, machines, stocks, PI, marques, clientele) |
| 5 | **Acheteurs** | 10% | Profondeur du marche acheteur pour ce type de cible |

## Seuils de Decision

| Score | Decision | Action |
|---|---|---|
| **75+** | URGENT | Pipeline complet immediat. Director alloue prioritairement. |
| **60-74** | GO | Lancement pipeline standard (Analyst → Writer + Hunter → Enricher) |
| **50-59** | WATCH | Surveillance. Pas de lancement auto. Reval si nouveaux elements. |
| **< 50** | ARCHIVE | Archivage. Pas d'action sauf changement de procedure. |

## Regles de Procedure

### Liquidation Judiciaire (LJ)
- **Urgence maximale**: deadlines courtes (souvent 2-4 semaines)
- Score procedure eleve (80-100)
- Privilegier rapidite d'execution sur profondeur d'analyse
- Actifs souvent a prix decote significative

### Redressement Judiciaire (RJ)
- **Meilleur ratio risque/opportunite**: entreprise encore en activite
- Periode d'observation 6-18 mois = plus de temps
- Score procedure moyen-haut (60-80)
- Plan de cession souvent plus structure

### Sauvegarde (SV)
- **Procedure proactive**: pas de cessation de paiement
- Score procedure moyen (40-60)
- Moins d'urgence, plus de negociation possible
- Souvent meilleure qualite des actifs

## Gestion du CA Manquant

Si le CA n'est pas disponible (frequent en procedure):

1. **Estimer depuis les actifs**: immobilier, machines, stocks → fourchette CA
2. **Estimer depuis le secteur**: multiples moyens du secteur NAF
3. **Estimer depuis l'effectif**: CA/salarie moyen du secteur
4. **Ne pas bloquer le scoring**: utiliser estimation mediane avec flag "estime"

## Precedents Historiques

Toujours verifier les precedents dans `backtest_scoring`:
- Entreprises similaires (meme NAF, meme taille, meme procedure)
- Taux de cession historique pour ce profil
- Prix de cession moyens observes
- Delai moyen entre ouverture et cession

## Anti-patterns

- Ne pas sursorer une entreprise uniquement a cause d'un gros CA (les dettes peuvent annuler la valeur)
- Ne pas ignorer les petites entreprises avec actifs strategiques (PI, marques, niches)
- Ne pas sous-estimer l'importance du mandataire (certains facilitent, d'autres bloquent)
- Ne pas lancer le pipeline si deadline < 5 jours (pas le temps de delivrer)
