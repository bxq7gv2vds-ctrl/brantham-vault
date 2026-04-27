---
name: Visuels LinkedIn — Week 1 (2026-04-28)
description: 3 visuels HTML/CSS prêts à publier pour le lancement S1 Paul, direction "feuille presse" éditoriale (FT / Le Monde diplomatique)
type: assets-pack
project: brantham
date: 2026-04-27
status: ready-to-ship
---

# Visuels LinkedIn — Week 1 du 28 avril 2026

Pack de 3 visuels carrés 1080×1080 (rendus 2160×2160 retina) pour les posts S1 du draft `writing-vault/linkedin/drafts/week-01-2026-04-28.md`.

## Direction artistique

Style "feuille presse" inspiré FT Weekend, Le Monde diplomatique, Bloomberg Businessweek. Anti-IA explicite : pas de pastilles SaaS, pas de gradients, pas de cartes-rectangles. Masthead avec logo Brantham + double règle, dateline Paris, grain papier subtil, tableaux à filets fins.

- Police corps : Source Serif 4
- Police titres : Instrument Serif (italique pour mots-clés)
- Police data : DM Mono
- Palette papier : `#F1ECE0` cream chaud
- Brand : navy `#001F54`, accent or `#C8B97A` (post sombre)

## Fichiers

| Fichier | Format | Date pub | Pilier |
|---|---|---|---|
| `post-01-top5-secteurs.html` / `.png` | Cream | Lundi 28 avril 8h | Data sourcée INSEE |
| `post-02-checklist-rj.html` / `.png` | Cream | Mercredi 30 avril 8h15 | Méthode interne |
| `post-03-vrai-prix.html` / `.png` | Navy | Vendredi 2 mai 8h | Le vrai prix |

## Régénérer les PNG

Si tu modifies un HTML, relance :

```bash
cd /Users/paul/vault/brantham/linkedin/week-01-2026-04-28
python3 render.py
```

Output : 2160×2160 retina (LinkedIn carré).

## Shipper un nouveau post

Partir de `_template.html` :

```bash
cp _template.html post-XX-titre.html
# éditer le contenu
# ajouter le fichier dans render.py → liste FILES
python3 render.py
```

## Logo

`logo.png` = wordmark officiel Brantham Partners (étoile + texte navy, 2504×330, fond transparent). Source : `/Users/paul/Desktop/brantham-partners/api/templates/brantham_logo.png`.

Sur fond sombre (`<div class="post px dark">`), le logo est inversé en blanc automatiquement via `filter: brightness(0) invert(1)` dans `_shared.css`.

## Related

- [[../linkedin-factory/drafts/week-01-2026-04-28]]
- [[../patterns/charte-graphique]]
- [[../patterns/teaser-onepager-html-pdf]]
- [[../_MOC]]
- [[../linkedin/INDEX]]
