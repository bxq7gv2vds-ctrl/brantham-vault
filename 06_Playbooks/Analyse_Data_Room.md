---
tags:
  - brantham/playbook
  - data-room
  - due-diligence
  - analyse
modeles_recommandes:
  extraction: DeepSeek V4 Flash
  analyse: DeepSeek V4 Pro
  agents_longs: Kimi / GLM / Qwen
---

# Analyse Data Room

## Objectif

Analyser une data room de cession ou reprise afin d'identifier les informations cles, les zones de risque, les incoherences documentaires et les questions de due diligence a poser.

## Inputs necessaires

- Index de data room ou liste des fichiers disponibles.
- Documents financiers, juridiques, commerciaux, sociaux, fiscaux et operationnels.
- Contexte de l'operation et hypothese de transaction.
- Questions deja posees ou points d'attention du client.
- Niveau de confidentialite et perimetre autorise d'analyse.

## Etapes de travail

1. Construire l'inventaire des documents par categorie.
2. Identifier les documents manquants ou incomplets.
3. Extraire les faits cles de chaque document.
4. Separer faits, hypotheses, calculs et interpretations.
5. Reperer les incoherences entre documents.
6. Classer les risques : financier, juridique, social, fiscal, operationnel, commercial.
7. Produire une liste de questions de due diligence.
8. Rediger une synthese executive et une matrice des risques.

## Format de sortie

- Synthese Markdown avec resume executif.
- Tableau des documents analyses : fichier, categorie, date, points cles, limites.
- Matrice des risques : risque, source, impact potentiel, niveau, action recommandee.
- Liste de questions ouvertes pour le vendeur, le dirigeant ou les conseils.

## Regles de qualite

- Ne jamais conclure au-dela des documents disponibles.
- Signaler toutes les incertitudes et limites d'analyse.
- Distinguer les donnees extraites des calculs produits par l'agent.
- Ne jamais modifier, renommer, supprimer ou deplacer les documents sources sans validation.
- Marquer les points critiques avec un niveau de confiance.

## Regles de citation des sources

- Citer le nom exact du fichier, la page ou section si disponible, et la date du document.
- Pour chaque chiffre, indiquer le document source et preciser s'il s'agit d'un chiffre publie, retraite ou calcule.
- En cas de contradiction, citer les deux sources contradictoires.

## Points necessitant validation humaine

- Toute conclusion pouvant affecter le prix, la structure de transaction ou la poursuite du dossier.
- Interpretation juridique, fiscale ou sociale.
- Priorisation finale des risques critiques.
- Communication d'un constat au vendeur, a l'acheteur ou a un conseil.

## Exemples de prompts utilisables

```text
Analyse cet index de data room. Classe les documents par categorie, identifie les manquants probables, puis propose une checklist de due diligence. Separe faits, hypotheses et questions.
```

```text
Lis ces documents financiers et cree une matrice des incoherences. Pour chaque point, indique le fichier source, la page si disponible, le risque et la question a poser.
```

```text
Prepare une synthese executive de la data room en distinguant les risques confirmes, les signaux faibles et les incertitudes.
```
