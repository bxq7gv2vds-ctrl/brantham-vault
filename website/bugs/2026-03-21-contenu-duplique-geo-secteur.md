---
title: "Bug fix — Contenu duplique pages geo et secteur"
date: 2026-03-21
project: website
type: bug-fix
status: resolved
---

# Contenu duplique pages geo et secteur

## Probleme
- Pages secteur : 80% de contenu partage entre pages (memes paragraphes juridiques, memes bullets Brantham)
- Pages geo : 71% partage. Orleans/Angers et Dijon/Clermont quasi-identiques (memes stats)
- Root cause : shared.json n'avait que 3-4 variants par categorie pour 20 villes / 15 secteurs = collisions garanties (pigeonhole principle)

## Fix
1. shared.json : 65 → 166 variants, 12 nouvelles categories
2. cities.json : 3 champs uniques par ville + fix donnees dupliquees
3. sectors.json : 4 champs uniques par secteur
4. generate.py : utilisation de tous les nouveaux champs

## Resultat
- Contenu unique par page : 20% → 80%
- Zero paire de pages quasi-identiques
