---
type: session
project: website
date: 2026-03-28
tags: [seo, audit, geo, json-ld, footer, indexnow]
updated: 2026-03-28
---

# Session : Audit SEO complet — 95 pages

## Contexte

Audit page-par-page systématique de tout le site Brantham Partners (`/Users/paul/zura-inspired/`).
Workflow : audit → présentation fixes → "go" → apply → page suivante.

## Ce qui a été fait

### Fixes batch globaux (début de session, avant audit page-par-page)
- **geo.région → geo.region** : méta invalide (accent) corrigé sur ~80 pages
- **HowTo JSON-LD** : 33 blocs cassés (virgules manquantes entre steps + repr() Python single-quotes) → regex fix global
- **Footer "Reprise a la barre"** : 23 pages manquaient la version sans accent → batch fix
- **Soumission IndexNow** : 91 URLs → 200 OK (en début de session)

### Audit page-par-page (pages 7-26, guides principaux)
Pages auditées individuellement avec corrections :
- `multiples-ebitda-distressed.html` — desc, mtime, H2 typos, footer
- `trouver-entreprise-difficulte-racheter.html` — H2/FAQ typos, mtime
- `risques-rachat-entreprise-difficulte.html` — mtime
- `financement-rachat-entreprise-difficulte.html` — mtime, footer
- `prepack-cession.html` — mtime, FAQ 10 dupliquée remplacée ("Quelles entreprises sont éligibles ?")
- `procedure-collective.html` — geo, mtime, footer
- `plan-de-cession.html` — geo, mtime, footer
- `reprise-a-la-barre.html` — geo, mtime, footer
- `liquidation-judiciaire.html` — geo, mtime, footer
- `redressement-judiciaire.html` — geo, mtime, footer
- `glossaire-ma.html` — geo, placename Paris→France, footer
- `barometre-defaillances.html` — geo, placename, mtime ajouté (manquait), footer
- `insights.html` — geo, footer
- `sourcing-proprietaire.html` — geo, footer
- `execution-audience.html` — geo, mtime
- `valorisation-entreprise-difficulte.html` — geo, mtime
- `rachat-entreprise-difficulte.html` — geo, placename, mtime
- `due-diligence-acceleree.html` — geo
- `trouver-entreprise-difficulte-racheter.html` — geo, footer
- `multiples-ebitda-distressed.html` — geo
- `index.html` — geo, placename, footer

### Fixes batch finaux

**9 pages contenu** (calendrier, cout, difference, droits, garantie, modele, purge, role, equipe) :
- geo.position + ICBM ajoutés
- mtime 2026-03-27 → 2026-03-28
- placename Paris → France (cout + equipe)
- footer +4 liens Ressources (procedure-collective, financement, risques, prepack)

**5 pages légales** (cgu, mentions-legales, politique-confidentialite, politique-cookies, avertissement) :
- geo.region + geo.placename + geo.position + ICBM ajoutés (n'avaient aucun tag geo)

**20 city pages** :
- mtime + dateModified JSON-LD : 2026-03-27 → 2026-03-28

**42 sector pages** (liquidation + redressement × 21 secteurs) :
- geo.placename + geo.position + ICBM ajoutés (n'avaient que geo.region)
- mtime + dateModified JSON-LD : 2026-03-27 → 2026-03-28

### Selon count — réduction (pages critiques)
- `financement-rachat-entreprise-difficulte.html` : 12 → 4
- `prepack-cession.html` : 12 → 4
- `modele-offre-reprise-plan-cession.html` : 15 → 5

### IndexNow final
95 URLs soumises → **200 OK** (Bing + Yandex notifiés).
Google : soumettre sitemap manuellement via GSC.

## Résultat final

| Critère | Avant | Après |
|---|---|---|
| geo.position + ICBM | 0/95 | **95/95** |
| geo.placename "France" | partiel | **95/95** |
| modified_time + dateModified 2026-03-28 | ~30/95 | **95/95** |
| JSON-LD valide | 33 erreurs | **0 erreur** |
| Title ≤65c | quelques dépassements | **0 dépassement** |
| Footer +4 liens Ressources | partiel | **toutes pages** |
| Selon critique (>10) | 3 pages | **0 page** |
| Pages live | 70 | **95** |

**Commande vérification** : `python3 -c "import re,json,glob; pages=glob.glob('/Users/paul/zura-inspired/*.html'); [print(p) for p in pages if 'geo.position' not in open(p).read() or '2026-03-27' in open(p).read()]"`

## Related

- [[website/_MOC]]
- [[_system/MOC-master]]
