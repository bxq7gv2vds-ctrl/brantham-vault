---
type: session
date: 2026-05-12
project: brantham
tags: [linkedin, content, casino, distressed, article]
---

# Session 2026-05-12 — LinkedIn : article Casino (format long-form) + cover

## Ce qui a été fait

- **Nouvel article long-form** : `vault/brantham/linkedin/week-02-2026-05-05/post-05-casino-article.md`, dérivé du thread `post-05-casino-thread.md`. D'abord structuré en 7 micro-sections, puis réécrit en **3 mouvements** (« Ce qui s'est passé » / « Pourquoi c'était possible » / « Le résultat, et ce que ça change ») en prose continue — le découpage en sous-titres courts rendait mal.
- **CTA de clôture ajouté** : paragraphe Brantham Partners sur l'accompagnement des repreneurs d'entreprises en difficulté, séparé par un trait. Devient une règle permanente (cf. memory `feedback_cta_accompagnement_repreneurs`).
- **Titre retenu** : « Le plus gros changement de contrôle d'un groupe français récent ne s'est pas joué en Bourse. Il s'est joué dans un tribunal de commerce. » (2 alternatives conservées dans le fichier).
- **Cover de l'article** : `post-05-casino-cover.{html,png}`. Plusieurs itérations sur retours Paul : version 1 « trop IA » → refonte sobre éditoriale ; logo Casino récupéré sur Wikimedia Commons (`casino-logo.svg`, enseigne « Casino supermarchés ») ; suppression bandeaux haut/bas ; logo Brantham retiré (Casino conservé) ; textes resserrés ; passage au ratio **1.91:1** (2560×1340 @2x) = format couverture d'article LinkedIn, plus de crop ; contenu centré (horizontal + vertical), texte aligné centre.
- **`render.py`** mis à jour : ajout de `post-05-casino-cover.html` (1280×670, body padding 0 pour atteindre le 1.91:1 plein cadre).
- **`INDEX.md`** : ajout d'une section « Pack Week 2 du 5 mai 2026 » + bloc détaillé Post 05 Casino (thread vs article, visuels, commande de régénération, vérifs avant publi).
- Nettoyage : suppression des fichiers temporaires `casino-try.bin` / `ct.bin`.

## Décisions

- **2 formats publiables pour le sujet Casino**, à ne pas publier le même jour : thread feed (`post-05-casino-thread.md`, meilleur reach immédiat) + article long-form (`post-05-casino-article.md`, meilleur archive/partage). Drafts 05A/05B/05C et le plan `post-05-casino-kretinsky.md` passent en archive.
- **Structure article = 3 mouvements**, pas de micro-sections. Option « zéro sous-titre / full essai » disponible si besoin.
- **CTA repreneurs systématique** en fin de tout contenu LinkedIn Brantham.

## Reste à faire

- Les 5 vérifications factuelles du frontmatter de `post-05-casino-article.md` avant publication (ordonnance n°2021-1193 du 15 sept. 2021 / date accord 27 juil. 2023 / répartition 53-46-1 / vote des classes 11 janv. 2024 / 25 % capital éco. & 63 % votes Naouri).
- Choisir la date de publication (ne pas chevaucher avec le thread).

## Related

- [[brantham/_MOC]]
- [[brantham/linkedin/INDEX]]
- [[brantham/linkedin/week-02-2026-05-05/post-05-casino-article]]
- [[brantham/linkedin/week-02-2026-05-05/post-05-casino-thread]]
- [[brantham/knowledge/market/cas-casino-groupe]]
- [[brantham/knowledge/procedures/sauvegarde-acceleree-sfa]]
- [[remember/2026-05-09]]
