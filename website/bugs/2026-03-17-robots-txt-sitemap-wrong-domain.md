---
type: bug-fix
project: website
date: 2026-03-17
status: fixed
severity: critical
---

# Bug: robots.txt sitemap pointe vers mauvais domaine

## Probleme
Le fichier `robots.txt` deploye sur branthampartners.fr contenait :
```
Sitemap: https://brantham.fr/sitemap.xml
```
Au lieu de :
```
Sitemap: https://branthampartners.fr/sitemap.xml
```

## Impact
- Google ne pouvait pas trouver le sitemap via robots.txt
- Bloquait potentiellement l'indexation du site
- Le site n'apparaissait dans aucun resultat Google (`site:branthampartners.fr` = 0)

## Cause
Le fichier source est `/Users/paul/zura-inspired/robots.txt` (site statique deploye).
Le `robots.ts` dans le projet Next.js (`/Users/paul/brantham-partners/website-landing/`) avait la bonne URL mais n'est pas le fichier deploye.

## Fix
Corrige `brantham.fr` → `branthampartners.fr` dans `/Users/paul/zura-inspired/robots.txt` ligne 33.

## A deployer
Le fix doit etre deploye sur le site live pour prendre effet.
