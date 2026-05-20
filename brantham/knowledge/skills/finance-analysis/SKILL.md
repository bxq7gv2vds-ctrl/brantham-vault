---
type: skill
project: brantham
name: finance-analysis
model_default: deepseek-v4-pro
---

# Skill: Finance Analysis

## Quand l'utiliser

Utiliser cette skill pour analyser comptes, KPI, rentabilite, BFR, dette nette, EBITDA et capacite financiere.

## Inputs necessaires

- comptes annuels ;
- balances ou situations intermediaires ;
- budget/previsionnel ;
- dette, tresorerie, BFR ;
- retraitements proposes.

## Etapes

1. Lire `06_Playbooks/Analyse_Financiere.md`.
2. Extraire les KPI.
3. Verifier les coherences documentaires.
4. Calculer ratios et formules.
5. Distinguer faits, calculs, hypotheses, interpretations.
6. Lister incertitudes et questions.

## Sorties

- note financiere Markdown ;
- tableau KPI ;
- liste d'incertitudes ;
- questions dirigeant/expert-comptable ;
- output JSON cowork.

## Regles qualite

- Toujours signaler les incertitudes.
- Chaque chiffre doit avoir une source ou etre marque a verifier.
- Ne pas donner de conclusion financiere definitive sans validation humaine.

