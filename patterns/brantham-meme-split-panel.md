---
type: pattern
project: brantham
date: 2026-05-15
category: design-system
tags:
  - linkedin
  - meme
  - design-system
  - python
  - PIL
---

# Pattern — Meme split panel Brantham

> Pattern réutilisable pour générer des memes "split panel" dans la DA Brantham, dérivé du meme Anakin de la semaine 02.

## Quand l'utiliser

Tout post LinkedIn ou X où un retournement contre-intuitif s'exprime mieux en image qu'en texte. Format particulièrement efficace pour :
- Opposer deux narratifs (vautour : "espèce protégée" vs "stigmatisé")
- Mettre côte à côte deux mondes (cabinet classique vs builder solo)
- Illustrer un contraste de payoff (cas A vs cas B)

## Specs DA

| Élément | Valeur |
|---|---|
| Format | 1080×1080 carré (LinkedIn engagement max) |
| Fond | Cream `#EFEBE0` |
| Grille intérieure | 960×924, top 56px, marges latérales auto |
| Cellules | 2 × (475×924), gouttière cream 10px |
| Photos | Couleur conservée (pas N&B), fit-to-cover |
| Voile sombre | Gradient noir bas, ratio 0.42 hauteur, alpha max 170 |
| Texte | Impact uppercase, blanc, stroke noir 7px, glow noir blur 14px |
| Auto-fit | Taille calculée pour tenir dans 86% de la largeur cellule, common size min des deux côtés |
| Position texte | Bottom-center, 56px depuis le bas de la cellule |
| Logo Brantham | Navy `#0E1A2B`, 44px haut, centré bottom 26px |

## Code de référence

`vault/brantham/linkedin/week-02-2026-05-05/vautour-split/compose_v4.py`

Fonctions clés :
- `fit_cell(path, w, h)` : crop center pour ratio cible
- `add_bottom_vignette(img)` : voile sombre gradient bas
- `fit_size(text, target_w)` : auto-fit pour éviter débordement
- `draw_meme_text(canvas, text, ...)` : glow + stroke + fill multi-layer

## Recette pas à pas

1. Choisir deux photos (libres de droits Wikimedia/Unsplash)
2. Choisir le pair de mots-clés en opposition uppercase (court = mieux, max 14 chars chacun pour avoir une taille de police lisible)
3. Copier `compose_v4.py` dans le sous-dossier du post
4. Adapter les chemins photos + textes dans le bloc `__main__`
5. Lancer `python3 compose.py`
6. Vérifier le rendu en ouvrant le JPG

## Cas d'usage réalisé

[[brantham/linkedin/week-02-2026-05-05/post-06-distressed-moral-vautour]] — vautour fauve vs repreneur PME, "PROTÉGÉ / STIGMATISÉ"

## Variantes à explorer

- Meme Anakin 4 cases (template HTML existant : [[brantham/linkedin/week-02-2026-05-05/dsys-lp/meme-anakin-lp]])
- Split panel vertical (1080×1350) plutôt que carré, format portrait que LinkedIn pousse mieux
- Triptyque 1080×1080 avec 3 cellules verticales

## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[brantham/linkedin/INDEX]]
- [[brantham/linkedin/week-02-2026-05-05/post-06-distressed-moral-vautour]]
- [[brantham/linkedin/week-02-2026-05-05/dsys-lp/meme-anakin-lp]]
- [[brantham/sessions/2026-05-15-linkedin-post-vautour]]
