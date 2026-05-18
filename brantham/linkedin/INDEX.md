# LinkedIn Content — Brantham Partners

**Strategie v1 (mars 2026):** `vault/brantham/strategy/2026-03-15-linkedin-personal-brand.md`
**Strategie v2 (avril 2026, active):** [[linkedin-factory/framework/weekly-framework]] — framework inbound-native 7 jours, pivot vers conversion DMs qualifiés (objectif : submerger de demandes entrantes)

**Fabrique de contenu:** `vault/brantham/linkedin-factory/` (symlink vers `writing-vault/linkedin/`)
- [[linkedin-factory/framework/weekly-framework]] — plan 7 jours
- [[linkedin-factory/formats/all-templates]] — 8 templates (capacity update, deal showcase, framework, refusal, horror story, signal faible, case study, post-mortem)
- [[linkedin-factory/newsletter/weekly-barometre-template]] — Baromètre Brantham hebdo
- [[linkedin-factory/_MOC]] — MOC complet

**Archive v1 (ci-dessous):** les 8 posts produits en mars, gardés comme référence de ton initial. Remplacés par le framework v2 à partir d'avril.

---

## Pack visuel — Week 1 du 28 avril 2026 (v2 active)

Dossier : `vault/brantham/linkedin/week-01-2026-04-28/`

3 visuels carrés 1080×1080 en HTML/CSS, direction "feuille presse" éditoriale (FT / Le Monde diplomatique). Logo Brantham intégré, masthead presse, grain papier, Source Serif corps, Instrument Serif titres.

| Fichier | Date pub | Pilier |
|---|---|---|
| `post-01-top5-secteurs.png` | Lun 28 avr | Top 5 secteurs défaillances FR 2025 (sourcé INSEE) |
| `post-02-checklist-rj.png` | Mer 30 avr | 6 vérifications avant offre RJ |
| `post-03-vrai-prix.png` | Ven 2 mai | Le vrai prix d'une reprise (fond navy) |

Régénérer : `cd vault/brantham/linkedin/week-01-2026-04-28 && python3 render.py`. Voir `README.md` du dossier pour le template `_template.html` réutilisable.

---

## Pack — Week 2 du 5 mai 2026 (v2 active)

Dossier : `vault/brantham/linkedin/week-02-2026-05-05/`

| Post | Sujet | Format | Fichiers clés |
|---|---|---|---|
| 01 | 186 défaillances par jour | Visuel + texte | `post-01-186-par-jour.{html,png}` |
| 02 | LegalPlace × Legalstart (signal M&A) | Visuel (variantes A→I) + texte | `post-02-*.{html,png}` |
| 04 | Le directeur M&A qui ne connaît pas le distressed | Texte + meme Anakin | `post-04-directeur-ma-distressed.md`, `post-04-meme-anakin{,-navy}.png` |
| 05 | Casino × Kretinsky | Voir bloc ci-dessous | `post-05-*` |

### Post 05 — Casino × Kretinsky

Un même sujet décliné en deux formats publiables (ne pas publier les deux le même jour) :

| Fichier | Format | Statut |
|---|---|---|
| `post-05-casino-thread.md` | Thread feed : post hook + 7 commentaires en chaîne | ready-to-publish |
| `post-05-casino-article.md` | Article long-form (titre + chapô + 3 mouvements + CTA repreneurs) | ready-to-publish |
| `post-05-casino-kretinsky.md` | Plan d'origine (4 angles + vote) | archive |
| `post-05A/05B/05C-casino-*.md` | Drafts d'origine (récit / mécanisme / portée) avant fusion | archive |

Visuels (HTML/CSS → PNG via `render.py`, DA cream Brantham, Newsreader) :
- `post-05-casino-cover.png` — couverture de l'article, ratio 1.91:1, logo Casino + titre serif
- `post-05-pyramide.png` — pyramide de contrôle Naouri → Casino (1280×670)
- `post-05-resultat.png` — partage du capital 53 / 46 / 1 (1280×670)

Régénérer les visuels : `cd vault/brantham/linkedin/week-02-2026-05-05 && python3 render.py`.
Avant publi : faire les 5 vérifications factuelles listées dans le frontmatter de `post-05-casino-article.md`.

---

## Pack — Week 3 du 18 mai 2026 (v2 active)

Dossier : `vault/brantham/linkedin/week-03-2026-05-18/` — voir `README.md`.

| Post | Sujet | Format | Fichiers clés |
|---|---|---|---|
| 1 | Minelli — décryptage funnel | Visuel funnel + texte | `post-1-minelli-decryptage-copy.md`, `post-1-minelli-funnel{,-navy}.png` |
| 2 | Pre-pack cession | Visuel timeline + texte | `post-2-pre-pack-cession-copy.md`, `post-2-pre-pack-timeline{,-navy}.png` |
| 3 | Pyramide des créanciers | Visuel pyramide + texte | `post-3-pyramide-creanciers-copy.md`, `post-3-pyramide-creanciers{,-navy}.png` |
| 4 | Valorisation en RJ — pourquoi l'offre la plus chère perd | Meme « they don't know » + mini-guide 4 sections | `post-4-valorisation-rj-copy.md`, `post-4-meme-tdk.png` |

### Post 4 — Valorisation RJ

- Copy : `post-4-valorisation-rj-copy.md` (2 562 caractères, ready-to-publish), hook « question qui pique » + 4 sections (price d'offre vs valorisation, 4 repères de prix, critères L642-5, 3 erreurs).
- Visuel retenu : meme « they don't know » → `post-4-meme-tdk.png` (template `templates/post-4-meme-tdk-lp.html`, bases `tdk-base.png` / `tdk-lines.png`).
- Visuels alternatifs : `post-4-meme-anakin.png` (Star Wars), `post-4-two-buttons.png`.

---

## Semaine 1 — Archive v1 (mars 2026)

| # | Jour | Titre | Format | Fichiers |
|---|------|-------|--------|----------|
| 1 | Lun | 5 procedures pour sauver une PME | Carousel 8 slides | `carousels/post-01-slide-01.png` a `08.png` |
| 2 | Mar | La stigmatisation de la faillite | Texte + Image | `images/post-02-stigmatisation.png` |
| 3 | Jeu | PME industrielle : coulisses d'une reprise | Texte + Image | `images/post-03-coulisses.png` |
| 4 | Ven | Poll : frein a la reprise de PME | Poll (texte seul) | — |

## Semaine 2

| # | Jour | Titre | Format | Fichiers |
|---|------|-------|--------|----------|
| 5 | Lun | 5 signaux qu'une PME va en difficulte | Carousel 7 slides | `carousels/post-05-slide-01.png` a `07.png` |
| 6 | Mar | Defaillances T1 2026 : les chiffres | Texte + Infographie | A generer |
| 7 | Jeu | 12 repreneurs en 48h | Texte + Image | `images/post-03-coulisses.png` |
| 8 | Ven | Pourquoi j'ai cree Brantham Partners | Texte seul | — |

---

## Copies LinkedIn

Tous dans `posts/` :
- `post-01-copy.md` — Carousel procedures
- `post-02-copy.md` — Stigmatisation
- `post-03-copy.md` — Etude de cas coulisses
- `post-04-copy.md` — Poll
- `post-05-copy.md` — Carousel signaux faibles
- `post-06-copy.md` — Macro defaillances
- `post-07-copy.md` — Repreneurs en 48h
- `post-08-copy.md` — Post personnel

---

## Assets visuels

### Carousels (1080x1350px)
- `carousels/post-01-sauver-pme.html` + 8 PNG slides
- `carousels/post-05-signaux-faibles.html` + 7 PNG slides

### Images (1080x1080px)
- `images/post-02-stigmatisation.html` + PNG
- `images/post-03-coulisses.html` + PNG

## Related
- [[brantham/_MOC]]
