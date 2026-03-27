---
type: decision
project: cross-project
date: 2026-03-27
status: active
tags: [vault, obsidian, wikilinks, infrastructure]
alternatives_considered: [manual-linking-only, obsidian-plugin-auto-links]
linked_assumptions: []
review_at: 2026-04-27
---

# Vault Wikilinks Overhaul — 248 fichiers interconnectes

## Context
Audit du vault le 2026-03-27 : 70% des fichiers (192/274) n'avaient aucun wikilink. Le graph Obsidian etait une etoile (MOCs pointant vers des feuilles isolees) au lieu d'un web de connaissances interconnecte. Les bugs, sessions, patterns, decisions etaient bien documentes mais deconnectes les uns des autres.

## Alternatives
1. **Linking manuel uniquement** — Trop lent, oublis garantis. Rejete.
2. **Plugin Obsidian auto-links** — Existe mais ne comprend pas le contexte semantique (lie tout a tout). Rejete.
3. **Script batch + convention CLAUDE.md** — Script intelligent qui cross-link par date/type/projet + regles dans CLAUDE.md pour les futurs fichiers. Choisi.

## Decision
1. Batch-fix : script Python (`vault/_system/scripts/batch-wikilinks.py`) qui analyse chaque fichier et ajoute une section `## Related` avec des wikilinks contextuels
2. Templates : tous les 9 templates mis a jour avec section `## Related` pre-remplie
3. CLAUDE.md : nouvelle section "Wikilinks Obsidian — OBLIGATOIRE" avec regles par type de fichier
4. Convention : `vault/_system/wikilinks-convention.md` — guide de reference permanent
5. Memoire : feedback memory mise a jour pour toutes les sessions futures

## Consequences
- 248 fichiers mis a jour avec des wikilinks (de 30% a ~99% de couverture)
- Graph Obsidian passe d'etoile a web dense
- Process automatise : chaque nouveau fichier vault aura des wikilinks des la creation
- Script re-executable periodiquement pour rattrapage
- QMD re-indexe apres les modifications

## Review
- 30d: [pending] — verifier que les nouvelles sessions/bugs/patterns respectent la convention
- 60d: [pending] — relancer le script batch pour combler les trous eventuels
- 90d: [pending] — evaluer la densite du graph Obsidian

## Related
- [[_system/MOC-decisions]]
- [[_system/MOC-master]]
- [[_system/wikilinks-convention]]
- [[founder/decisions/2026-03-12-unified-vault]]
