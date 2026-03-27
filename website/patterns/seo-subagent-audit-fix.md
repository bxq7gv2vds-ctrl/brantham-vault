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

## Related
- [[_system/MOC-patterns]]
- [[website/_MOC]]
- [[website/bugs/2026-03-15-audit-seo-technique]]
- [[website/sessions/2026-03-15]]
- [[website/sessions/2026-03-15-audit-maillage-interne]]
- [[brantham/strategy/2026-03-15-linkedin-personal-brand]]
- [[founder/sessions/2026-03-15-polytech-strategist]]
- [[website/bugs/2026-03-17-robots-txt-sitemap-wrong-domain]]
- [[website/bugs/2026-03-19-seo-procedures-legales-sitemap-fix]]
- [[website/bugs/2026-03-21-contenu-duplique-geo-secteur]]
- [[brantham/bugs/2026-03-06-agent-auth-401]]
