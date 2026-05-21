---
type: decision
date: 2026-05-19
project: brantham
tags: [toolchain, pdf, teaser, pandoc, latex]
related:
  - "[[2026-05-18-infra-strasbourg]]"
  - "[[2026-05-18-infra-strasbourg-presentation-pre-nda]]"
---

# Toolchain PDF teasers Brantham — pandoc + tectonic

## Décision

Pour générer les **notes pré-NDA** au format identique au teaser Open-Bee (typo Computer Modern, tableaux booktabs, maketitle LaTeX), la chaîne retenue est :

```
markdown (YAML metadata) → pandoc → tectonic → PDF
```

## Pourquoi pas BasicTeX

BasicTeX (`brew install --cask basictex`) requiert un mot de passe **sudo** pour finaliser l'installation du paquet `.pkg`, ce qui bloque toute exécution non-interactive (Claude Code en mode autonome notamment).

## Pourquoi tectonic

- `brew install tectonic` — installation **sans sudo**
- Télécharge automatiquement les paquets LaTeX à la volée
- Maintenu (Rust), rendu compatible avec les templates pandoc standards
- ~16 Mo seulement (vs ~100 Mo BasicTeX)

## Setup YAML minimal pour les teasers

```yaml
---
title: Opportunité de reprise
subtitle: |
  Note d'introduction pré-NDA \
  [Description anonymisée de la cible] \
  [Statut procédure]
author: Brantham Partners, Conseil M&A distressed
date: YYYY-MM-DD
lang: fr-FR
documentclass: article
geometry:
  - a4paper
  - margin=25mm
fontsize: 11pt
linestretch: 1.15
colorlinks: true
linkcolor: black
urlcolor: black
header-includes:
  - \usepackage{titling}
  - \pretitle{\begin{center}\Large\bfseries}
  - \posttitle{\end{center}}
  - \preauthor{\begin{center}\normalsize}
  - \postauthor{\end{center}}
  - \predate{\begin{center}\normalsize}
  - \postdate{\par\vspace{1em}\textit{Document de présentation, diffusion strictement pré-NDA}\end{center}}
  - \setlength{\parskip}{0.5em}
  - \setlength{\parindent}{0pt}
---
```

## Commande

```bash
pandoc teaser.md --pdf-engine=tectonic -o teaser.pdf
```

## ⚠️ Piège — option clash babel

**Ne PAS** ajouter `\usepackage[french]{babel}` dans `header-includes`. Le template pandoc charge déjà babel via la metadata `lang:`. Doublon → `LaTeX Error: Option clash for package babel`.

Idem pour `booktabs`, `longtable`, `array` — pandoc les charge automatiquement quand il y a des tableaux markdown.

## Premier déploiement réussi

- Teaser INFRA Strasbourg (2026-05-19), 46 Ko, 7 pages
- Visuellement identique au teaser Open-Bee
## Related

- [[_system/MOC-decisions]]
- [[brantham/_MOC]]