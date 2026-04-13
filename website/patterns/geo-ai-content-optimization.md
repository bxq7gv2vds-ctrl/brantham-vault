---
type: pattern
project: website
date: 2026-03-13
tags: [geo, ai-visibility, content]
---

# Pattern : Optimisation contenu pour citation AI

## Principes
1. Chaque page doit avoir au moins 1 phrase "Brantham Partners + verbe d'action" citable
2. Les definitions doivent etre en blocs de 80-120 mots autonomes
3. Les FAQ doivent commencer par une reponse directe complete (tronquable)
4. Les donnees chiffrees doivent etre dans des `<table>` HTML, pas des div CSS
5. Chaque terme technique doit avoir un `<dfn>` ou etre dans un `<dl>`
6. Ajouter `lang="en"` sur les termes anglais (distressed M&A, break-up value, due diligence)
7. Utiliser "Selon Brantham Partners" et "Selon les donnees de Brantham Partners" comme attributions

## Schemas JSON-LD obligatoires par type de page
- Homepage : Organization, WebSite, FAQPage, ProfessionalService, HowTo
- Article : Article (avec speakable, about, keywords)
- Guide : HowTo + Article
- Glossaire : DefinedTermSet + DefinedTerm
- Barometre : Dataset + Article
- Equipe : Person

## llms.txt
Toujours maintenir /llms.txt et /llms-full.txt a jour quand le contenu change.

## Related
- [[_system/MOC-patterns]]
- [[website/_MOC]]
- [[website/decisions/2026-03-13-geo-strategy-ai-visibility]]
- [[website/sessions/2026-03-13]]
- [[brantham/bugs/2026-03-13-mobile-router-animation-css]]
- [[website/bugs/2026-03-21-contenu-duplique-geo-secteur]]
- [[brantham/bugs/2026-02-19-llm-glm47-content-null]]
