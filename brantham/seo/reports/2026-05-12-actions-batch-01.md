---
title: SEO — Batch d'actions #1 (technique + maillage)
type: seo-changelog
project: brantham
date: 2026-05-12
tags: [seo, branthampartners, changelog]
---

# Batch d'actions #1 — 2026-05-12

Modifs faites sur `/Users/paul/zura-inspired/`. **Non déployées** — Paul déclenche le déploiement Vercel.

## Changements

### 1. Canonicalisation www → non-www (le fix "pages pas indexées")
`vercel.json` : ajout d'un bloc `redirects` → 301 de `www.branthampartners.fr/*` vers `https://branthampartners.fr/*`. Avant : `https://www.branthampartners.fr/equipe.html` répondait **200** = site dupliqué, signaux de ranking et budget de crawl divisés en deux. http→https était déjà en place (308 Vercel).

### 2. De-orphaning — 21 pages étaient orphelines
Diagnostic : 21 pages dans le sitemap mais **liées depuis aucune autre page** → Google les classe en "Detectée, actuellement non indexée". C'était la cause principale du "tous les liens ne sont pas indexés".

Pages concernées : 8 villes (Amiens, Brest, Caen, Limoges, Metz, Reims, Saint-Nazaire, Tours) + 13 pages thématiques (calculateur-cout-reprise, business-plan-reprise, lbo-distressed, nda-rachat-entreprise, peut-on-racheter-entreprise-avec-dettes, pse-plan-de-sauvegarde-emploi-cession, que-se-passe-t-il-quand-entreprise-liquidation, quel-prix-payer-entreprise-liquidation, sauvegarde-acceleree, sort-bail-commercial-liquidation, turn-around-management, tva-cession-fonds-de-commerce-liquidation, comment-fonctionne-audience-adjudication).

Fix : ajout d'une section "Présence nationale" (28 villes) + "Ressources" (13 pages) en bas de `rachat-entreprise-difficulte.html` (page pilier, 838 impr/90j). **Résultat : 0 page orpheline.** À renforcer ensuite avec des liens contextuels depuis les pages pertinentes.

### 3. Page cassée supprimée
`rachat-entreprise-0.html` : doublon corrompu (title = Saint-Nazaire, canonical = Metz, keywords = Metz). Supprimée + 301 vers `rachat-entreprise-metz.html` dans `vercel.json`.

### 4. Nettoyage
- `sections-proposals.html` : 301 vers `/` + retiré du `Disallow` robots.txt (sinon le 301 ne se propage pas).
- `sitemap.xml` : `lastmod` de `rachat-entreprise-difficulte.html` → 2026-05-12 (+ `article:modified_time` dans la page).

## Vérifications faites
- `vercel.json` JSON valide, `sitemap.xml` XML valide, page HTML parse.
- Re-scan orphelins : 0. Sitemap : aucune entrée fantôme, aucun fichier manquant.
- Liens villes ajoutés : tous les 28 fichiers `rachat-entreprise-<ville>.html` existent (Nîmes retiré, pas de page).

## À faire par Paul après déploiement
1. Déployer (Vercel).
2. GSC → vérifier que `www.branthampartners.fr/...` renvoie bien 301 (`curl -I https://www.branthampartners.fr/equipe.html`).
3. GSC → **Sitemaps** : re-soumettre `sitemap.xml`.
4. GSC → **Indexation des pages** : exporter le rapport et me l'envoyer — je verrai exactement quelles URLs sont "Crawlée non indexée" / "Détectée non indexée" et pourquoi.
5. GSC → Inspection d'URL sur 3-4 pages ex-orphelines (ex. `rachat-entreprise-metz.html`) → "Demander l'indexation".

## Reste à faire (prochains batchs)
- Liens contextuels (pas juste le hub) vers les ex-orphelines, depuis les pages thématiques pertinentes.
- Refonte profondeur des head terms à pos 20+ (`redressement-judiciaire.html`, `liquidation-judiciaire.html`, `procedure-collective.html`).
- Enrichir le cluster transport (breakout) : FAQ "2026", maillage transport-redressement ↔ transport-liquidation ↔ villes.
- Pass titles/meta sur les pages à CTR faible (`financement-rachat-entreprise-difficulte.html` notamment).
- JSON-LD `Organization` sur la home (SIREN, adresse).

## Related
- [[brantham/seo/_MOC]]
- [[brantham/seo/reports/2026-05-12-point-01]]
- [[brantham/_MOC]]
