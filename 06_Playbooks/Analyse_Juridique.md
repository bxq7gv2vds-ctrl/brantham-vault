---
tags:
  - brantham/playbook
  - juridique
  - due-diligence
  - risques
modeles_recommandes:
  extraction: DeepSeek V4 Flash
  analyse: DeepSeek V4 Pro
  agents_longs: Kimi / GLM / Qwen
---

# Analyse Juridique

## Objectif

Analyser des documents juridiques lies a une societe ou une transaction afin d'identifier les faits, obligations, risques, clauses sensibles et points a faire valider par un professionnel du droit.

## Inputs necessaires

- Statuts, Kbis, pactes, PV d'assemblee, contrats significatifs.
- Baux, contrats de travail, contentieux, garanties, assurances.
- Mandats, LOI, NDA, SPA, contrats de financement si disponibles.
- Contexte de l'operation et juridiction concernee.
- Questions specifiques a instruire.

## Etapes de travail

1. Classer les documents par nature et date.
2. Extraire les parties, dates, obligations, echeances et clauses importantes.
3. Identifier les clauses de changement de controle, exclusivite, non-concurrence, resiliation, garantie, penalites.
4. Reperer les documents manquants ou incoherents.
5. Separarer faits juridiques observes, hypotheses et interpretations.
6. Produire une matrice de risques et une liste de questions pour l'avocat ou le conseil.
7. Signaler explicitement les incertitudes.

## Format de sortie

- Note juridique Markdown.
- Tableau des documents : nom, date, parties, objet, points cles, risques, limites.
- Matrice des clauses sensibles.
- Liste des questions a valider par un humain qualifie.

## Regles de qualite

- Toujours signaler que l'analyse ne remplace pas un avis juridique.
- Toujours signaler les incertitudes, lacunes documentaires et interpretations.
- Ne jamais inventer de clause, obligation, partie ou date.
- Ne pas proposer d'action juridique definitive sans validation humaine.
- Conserver la distinction entre lecture documentaire et qualification juridique.

## Regles de citation des sources

- Citer le fichier, la page, l'article, la clause ou la section.
- Pour les documents officiels, citer la date de consultation et la source.
- En cas de conflit entre documents, citer les passages concernes de chaque source.
- Ne pas citer de longues clauses integralement sauf demande explicite et limitee.

## Points necessitant validation humaine

- Interpretation finale d'une clause.
- Evaluation d'un contentieux ou d'un risque indemnitaire.
- Redaction ou modification de documents juridiques engageants.
- Signature, envoi ou negociation d'un document.
- Toute conclusion pouvant influencer le prix, la garantie d'actif-passif ou les conditions suspensives.

## Exemples de prompts utilisables

```text
Analyse ces documents juridiques. Extrais les faits, clauses sensibles, incertitudes et questions a poser a l'avocat. Ne donne pas de conclusion definitive.
```

```text
Repere les clauses de changement de controle, resiliation, exclusivite, non-concurrence et penalites. Cite le fichier et la clause exacte si disponible.
```

```text
Prepare une matrice des risques juridiques pour ce dossier, avec niveau de confiance et validation humaine requise.
```
