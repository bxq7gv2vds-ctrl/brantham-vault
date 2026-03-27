---
type: agent-config
updated: 2026-03-26
---

# Blacklist — Mots et patterns AI interdits

## Mots anglais (detection immediate)
delve, tapestry, moreover, furthermore, landscape, crucial, foster, leverage, utilize, comprehensive, intriguing, pivotal, nuanced, multifaceted, streamline, synergy, paradigm, embark, innovative, groundbreaking, cutting-edge, transformative, harness, robust, overarching, encompass, spearhead, resonate, underscore, noteworthy, testament, realm, beacon, holistic, unprecedented, game-changer, elevate, empower, unlock, supercharge, unleash, deep-dive, ecosystem, seamless, scalable, disruptive, actionable, insightful, thought-provoking, compelling

## Mots francais (detection immediate)
il est important de noter, dans un monde en constante evolution, plongeons dans le sujet, voici ce que j'en pense, un veritable game-changer, force est de constater, il convient de souligner, en definitive, par consequent, neanmoins, toutefois (en debut de phrase), en somme, indeniablement

## Patterns structurels
- Listes numerotees trop propres (1. 2. 3. 4. 5.)
- Paragraphes de longueur identique
- Conclusions qui rephrasent l'intro
- Transitions trop lisses entre idees
- "It's worth noting that..."
- "In today's rapidly evolving..."
- "Let's dive in" / "Let's break it down"
- "Here's the thing:"
- "This is huge."
- "I've been thinking about X and here are my thoughts"
- Tout ce qui sonne comme un communique de presse

## Signes structurels
- Toutes les phrases font 10-15 mots (pas de variation)
- Chaque paragraphe = exactement 3 phrases
- Enumeration parfaitement parallele (toujours la meme construction)
- Absence totale de fragments, d'hesitations, d'imperfections

## Related
- [[_system/MOC-master]]
