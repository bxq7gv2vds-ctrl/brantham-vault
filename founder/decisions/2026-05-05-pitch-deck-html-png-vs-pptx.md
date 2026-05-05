---
name: Pitch deck — HTML/CSS rendu en PNG plutôt que PPTX éditable
description: Choix d'architecture pour les decks de présentation au repreneur — fidélité DA prime sur l'éditabilité PowerPoint
type: decision
date: 2026-05-05
project: brantham
---

# Pitch deck — HTML/CSS rendu en PNG plutôt que PPTX éditable

## Décision

Les decks de présentation au repreneur sont produits en **HTML/CSS rendus en PNG retina @2x via Playwright Chromium**, intégrés ensuite dans une présentation où chaque slide est une image. Pas de fichier PPTX natif éditable.

## Alternative écartée

`python-pptx` pour générer un fichier `.pptx` natif où chaque texte / forme reste éditable dans PowerPoint, Keynote ou Google Slides.

## Pourquoi

La DA Brantham D3 (mono dossier brutaliste) repose sur des éléments que `python-pptx` ne reproduit pas proprement :
- **Watermark vertical rotaté 90°** avec filet 1px en bordure gauche
- **Tampon avec rotation négative** (−1.5° à −3° pour la signature manuscrite)
- **Italique Source Serif 4 inline** dans un titre serif principal — sélection de mot par mot
- **Filet horizontal** sous-titre + tirets typographiques précis
- **Marges et grille pixel-parfaites** héritées de `tokens.css`

Tentative initiale en `python-pptx` (fichier `_archive/pitch-repreneur.pptx`) a produit un rendu visuellement dégradé que le founder a explicitement rejeté ("c'est terrible").

## Trade-off accepté

| | HTML → PNG | python-pptx |
|---|---|---|
| Fidélité DA | 100 % | ~60 % |
| Éditable au texte près dans PPT | ✗ | ✓ |
| Édition par modification HTML + regénération | ✓ (1 commande) | ✗ |
| Réutilisable pour autres deals | ✓ (copier le dossier) | ✓ |
| Cohérent avec le système design existant | ✓ (mêmes fichiers source) | ✗ (réinvention) |

Le founder préfère la fidélité DA — le repreneur reçoit un PDF / des images, pas un fichier qu'il va modifier. L'édition se fait côté Brantham via le HTML source.

## Conséquence

Tous les futurs decks Brantham (pitch repreneur, dossier d'analyse, présentations clients) suivent ce pattern :
- HTML/CSS dans `<deal>/pitch-deck/` (ou équivalent)
- Imports : `tokens.css` + `base.css` + `_format.css` + un `_<contexte>-base.css` pour rebind tokens
- `render.py` Playwright pour PNG retina

## Related

- [[_system/MOC-decisions]]
- [[brantham/_MOC]]
- [[brantham/sessions/2026-05-05-sas-fitness-levallois-pitch-deck]]
- [[brantham/linkedin/_design-system/README|Design System D3]]
- [[brantham/patterns/charte-graphique]]
