---
tags:
  - brantham/playbook
  - website
  - seo
  - contenu
  - code
modeles_recommandes:
  extraction: DeepSeek V4 Flash
  analyse: DeepSeek V4 Pro
  code_agents_longs: Kimi / GLM / Qwen
---

# Website

## Objectif

Ameliorer le website Brantham par des audits, contenus, optimisations SEO/GEO, corrections UX, idees de pages et scripts internes, en gardant une trace claire dans Obsidian.

## Inputs necessaires

- URL ou chemin local du site.
- Objectif : conversion, SEO, GEO/LLM visibility, credibilite, vitesse, design, contenu.
- Pages prioritaires et audience cible.
- Contraintes de marque, ton, offres et preuves disponibles.
- Donnees disponibles : analytics, Search Console, logs, captures, contenus existants.

## Etapes de travail

1. Clarifier l'objectif d'amelioration.
2. Inventorier les pages, composants ou contenus concernes.
3. Auditer le contenu, la structure, le SEO technique et l'experience utilisateur.
4. Separarer observations, hypotheses, recommandations et changements proposes.
5. Prioriser les actions par impact, effort et risque.
6. Rediger les contenus ou specifications necessaires.
7. Pour le code, travailler dans le repo concerne et verifier localement quand c'est possible.
8. Documenter les changements dans une note Obsidian.

## Format de sortie

- Audit Markdown avec priorites P0/P1/P2.
- Backlog d'actions : action, page, impact, effort, risque, validation requise.
- Drafts de contenus ou briefs de composants.
- Notes de verification : commandes lancees, resultats, limites.

## Regles de qualite

- Ne pas modifier massivement le site sans confirmation.
- Ne pas inventer de preuve client, chiffre, reference ou temoignage.
- Distinguer les recommandations basees sur donnees des hypotheses UX/SEO.
- Tester les changements quand un environnement local existe.
- Preserver le style de marque et les conventions du repo.

## Regles de citation des sources

- Citer les pages auditees avec URL ou chemin local.
- Pour les benchmarks, citer les sources et dates de consultation.
- Pour les recommandations SEO, indiquer si elles viennent d'un audit local, d'une source externe ou d'une hypothese.
- Ne pas reprendre de contenu concurrent sans transformation originale.

## Points necessitant validation humaine

- Positionnement, promesses commerciales et claims de marque.
- Publication en production.
- Changement de structure d'offre, prix, preuves ou references.
- Suppression de pages ou redirections.
- Modification importante de tracking ou formulaires.

## Exemples de prompts utilisables

```text
Audite cette page du website Brantham. Separe observations, hypotheses et recommandations. Priorise les actions P0/P1/P2.
```

```text
Propose une nouvelle page service pour cette offre. N'invente aucune preuve client. Donne le plan, les sections, les messages cles et les validations humaines requises.
```

```text
Analyse ce repo website, identifie les conventions, puis propose une petite amelioration UX implementable et testable localement.
```
