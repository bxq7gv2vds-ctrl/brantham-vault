---
tags:
  - brantham/playbook
  - finance
  - analyse-financiere
  - due-diligence
modeles_recommandes:
  extraction: DeepSeek V4 Flash
  analyse: DeepSeek V4 Pro
  agents_longs: Kimi / GLM / Qwen
---

# Analyse Financiere

## Objectif

Produire une analyse financiere fiable d'une societe ou d'un dossier, en identifiant performance, rentabilite, structure de bilan, cash-flow, normalisations possibles et risques.

## Inputs necessaires

- Comptes annuels, balances, liasses fiscales, grand livre si disponible.
- P&L mensuel, budget, previsionnel, carnet de commandes.
- Dette, tresorerie, BFR, engagements hors bilan.
- Details des retraitements demandes ou deja proposes.
- Hypothese d'operation : valorisation, reprise, financement, retournement.

## Etapes de travail

1. Inventorier les documents financiers disponibles et leur periode.
2. Extraire les principaux chiffres : CA, marge brute, EBITDA, EBIT, resultat net, dette nette, BFR.
3. Verifier la coherence entre documents.
4. Calculer les ratios utiles et documenter les formules.
5. Identifier les tendances, ruptures et elements non recurrents.
6. Distinguer les retraitements justifies des hypotheses non validees.
7. Produire une synthese des risques financiers et questions ouvertes.
8. Preparer, si demande, une grille de scoring financier.

## Format de sortie

- Note financiere Markdown.
- Tableau des KPI par exercice et periode intermediaire.
- Section "Faits", "Calculs", "Hypotheses", "Interpretations".
- Liste des incertitudes et documents manquants.
- Questions de clarification pour le dirigeant, l'expert-comptable ou le conseil.

## Regles de qualite

- Toujours signaler les incertitudes.
- Ne jamais presenter une hypothese comme un fait.
- Indiquer les formules de calcul pour EBITDA retraite, dette nette, BFR et ratios.
- Ne pas donner de conseil financier definitif sans revue humaine.
- Controler les ordres de grandeur et signaler les anomalies.

## Regles de citation des sources

- Chaque chiffre doit pointer vers un document, une page, un onglet ou une cellule si disponible.
- Les calculs doivent mentionner les inputs utilises.
- Les retraitements doivent indiquer leur source et leur justification.
- Les donnees non sourcees doivent etre marquees "a verifier".

## Points necessitant validation humaine

- Retraitements d'EBITDA.
- Hypotheses de valorisation.
- Evaluation de la solvabilite ou de la capacite d'endettement.
- Conclusions adressees a un client, investisseur, banque ou conseil.
- Utilisation de documents incomplets ou non audites.

## Exemples de prompts utilisables

```text
Analyse ces comptes annuels. Extrais les KPI, calcule les ratios principaux, separe faits, calculs, hypotheses et interpretations, puis liste les incertitudes.
```

```text
Compare ces trois exercices et identifie les ruptures de tendance, les anomalies et les questions a poser au dirigeant.
```

```text
Construis une grille de scoring financier A/B/C pour ce repreneur ou cette cible, avec justification sourcee et limites d'analyse.
```
