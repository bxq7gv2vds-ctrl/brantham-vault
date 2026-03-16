---
date: 2026-03-15
project: website
type: pattern
---

# Pattern : Audit SEO par subagents paralleles

## Workflow

1. Lancer 4 agents audit en parallele (technique, linking, contenu, performance)
2. Consolider les findings avec priorites (critique/important/mineur)
3. Lire les fichiers de reference (page correcte) pour extraire le pattern cible
4. Lancer N agents fix en parallele, chacun avec le contexte du pattern cible
5. Verifier : curl 200, grep mentions, grep liens morts

## Resultats 2026-03-15

- 40+ issues identifiees en ~2min
- 5 agents fix en parallele, tout corrige en ~5min
- Zero erreur post-fix

## Notes

- Donner a chaque agent fix le HTML de reference (page correcte) pour harmoniser
- Verifier les canonical URLs vs sitemap apres fix
- Les agents fix doivent recevoir les liens internes existants pour eviter les liens morts
