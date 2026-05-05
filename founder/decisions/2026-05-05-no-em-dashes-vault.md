---
name: Interdiction des tirets cadratins dans les vaults
type: decision
date: 2026-05-05
status: approved
tags: [writing, style, vault]
---

# Interdiction des tirets cadratins dans les vaults Obsidian

**Date** : 2026-05-05
**Status** : Approved
**Decision Maker** : Paul
**Trigger** : Première publication writing-vault, [[../../../writing-vault/published/2026-05-05-le-gout-dernier-territoire]]

## Contexte

Lors de la rédaction du premier essai publié du writing-vault, Claude a utilisé 14 tirets cadratins (—) comme séparateurs stylistiques. Paul a demandé leur interdiction sur tout le vault.

Le tiret cadratin est devenu une signature stylistique IA très visible (overuse par GPT-4 et Claude). L'utiliser dans un texte revendiqué comme la voix de Paul casse l'authenticité.

## Options considérées

1. **Garder les cadratins, les utiliser avec modération** : risque de fuite stylistique IA, demande un contrôle manuel à chaque draft.
2. **Interdire les cadratins (—) et demi-cadratins (–) sur tous les textes des vaults** : règle binaire, applicable automatiquement, force des phrases plus tranchantes.
3. **Interdire seulement dans le writing-vault (textes publiés)** : moins strict mais introduit une asymétrie entre vaults.

## Décision

**Choisi** : Option 2 — interdiction sur tous les vaults Obsidian (`/Users/paul/writing-vault/` et `/Users/paul/vault/`).

**Reasoning** :
- Élimine la signature IA partout où Paul peut publier
- Force des phrases plus courtes ou des restructurations qui rendent le texte plus tranchant
- Règle simple à appliquer automatiquement
- Les traits d'union français (`non-goût`, `peut-être`, `dix-neuvième`) sont conservés car obligatoires en orthographe

## Application

- Remplacements possibles : point, virgule, deux points, parenthèses, ou restructuration de la phrase
- Listes markdown (`- item`) inchangées (le tiret de liste est un caractère ASCII, pas un cadratin)
- Sauvegardé dans la mémoire globale : `~/.claude/projects/-Users-paul/memory/feedback_no_em_dashes_vault.md`

## Related

- [[../../../writing-vault/sessions/2026-05-05-publication-gout-dernier-territoire]]
- [[../../../writing-vault/published/2026-05-05-le-gout-dernier-territoire]]
- [[../../_system/MOC-decisions]]
