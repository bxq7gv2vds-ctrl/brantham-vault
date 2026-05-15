---
type: session
project: brantham
date: 2026-05-15
duration: 2h
tags:
  - linkedin
  - contenu
  - meme
  - vautour
  - design-system
---

# Session 2026-05-15 — Post LinkedIn vautour + meme

## Contexte

Réflexion sur un post LinkedIn Brantham en s'inspirant du vault Brantham et du writing-vault. Angle retenu : pourquoi le M&A distressed est moral, avec hook étude vautours Inde et meme visuel split panel.

## Décisions

1. **Angle retenu** : pilier 7 (opinions contrarian) du plan LinkedIn, sourcé sur [[writing-vault/drafts/banger-seeds/05-pourquoi-distressed-est-moral]]
2. **Hook final** : étude Frank & Sudarshan AER 2024 sur la disparition des vautours en Inde et la mortalité humaine consécutive
3. **Chiffres FR** : passage de chiffres devinés vers les chiffres Altares 2025 réels sourcés via [[brantham/knowledge/market/stats-defaillances-2025]] et [[brantham/mastery/data-marche/stats-2025]]
   - 69 957 défaillances en 2025 (record absolu)
   - 47 078 LJ directes (67%)
   - 21 336 RJ (30%)
   - 1 543 sauvegardes (2%)
   - 267 200 emplois menacés
   - ~6 000 plans de cession (30% des RJ)
4. **CTA corrigé** : audience cible = entreprises stratégiques qui font de la croissance externe en distressed, pas dirigeants de PME en difficulté ni particuliers repreneurs. Cohérent avec positionnement Brantham côté acquéreur.
5. **DA visuelle** : matcher strictement le format meme Anakin de la semaine 02 (cream `#EFEBE0`, photos couleur conservées, texte Impact uppercase blanc + stroke noir + glow, logo Brantham navy centré bas). Voir [[brantham/linkedin/week-02-2026-05-05/dsys-lp/meme-anakin-lp]].

## Livrables

### Post markdown
- [[brantham/linkedin/week-02-2026-05-05/post-06-distressed-moral-vautour]]

### Visuel meme split panel
3 variantes finales générées avec auto-fit pour que le texte tienne sans déborder :
- `vautour-split/vautour-split-v5a.jpg` : ESPÈCE PROTÉGÉE / STIGMATISÉ (le plus rigoureux factuellement)
- `vautour-split/vautour-split-v5b.jpg` : PROTÉGÉ / STIGMATISÉ (recommandé — opposition lexicale pure, texte le plus gros)
- `vautour-split/vautour-split-v5c.jpg` : INDISPENSABLE / MÉPRISÉ (le plus émotionnel)

### Photos sourcées
- Vautour : Wikimedia Commons, *Gyps fulvus in flight, Spain* (CC BY-SA, à créditer l'auteur exact en commentaire LinkedIn)
- Repreneur : Unsplash, photo libre d'usage commercial

### Script de composition
`vautour-split/compose_v4.py` — réutilisable pour d'autres splits panel avec auto-fit du texte

## Itérations visuelles

- v1 : N&B + Newsreader italic + labels en bas + bande caption (trop éditorial, pas assez meme)
- v2 : couleurs + Impact uppercase + texte bottom-center (manque de punch, trop petit)
- v3 : ajout caption "Même métier. Jugement opposé." (chevauchement avec logo, bug)
- v4 : texte plus gros + stroke + glow + voile sombre dégradé + gouttière (déborde des cellules)
- v5 : ajout auto-fit qui dimensionne le texte pour tenir pile dans chaque cellule (final retenu)

## Patterns capturés

- **Meme split panel Brantham** : 1080x1080, cream `#EFEBE0`, gouttière 10px entre les 2 cellules, photos couleur conservées, voile sombre dégradé en bas pour faire ressortir le texte, Impact uppercase blanc + stroke noir 7px + glow Gaussien 14px, logo Brantham navy 44px centré bottom 26px. Voir le script `vautour-split/compose_v4.py`.
- **Auto-fit texte meme** : pour éviter le débordement, calculer la taille de police max pour que chaque texte tienne dans 86% de la largeur de cellule, et prendre le min des deux côtés pour homogénéité visuelle.

## Idées pour les prochains posts

Voir [[brantham/linkedin/week-02-2026-05-05/idees-prochains-posts]] (angles refusés et angles à explorer).

## Related

- [[brantham/_MOC]]
- [[brantham/linkedin/INDEX]]
- [[brantham/linkedin/week-02-2026-05-05/post-06-distressed-moral-vautour]]
- [[brantham/linkedin/week-02-2026-05-05/idees-prochains-posts]]
- [[brantham/strategy/2026-03-15-linkedin-personal-brand]]
- [[brantham/knowledge/market/stats-defaillances-2025]]
- [[brantham/mastery/data-marche/stats-2025]]
- [[writing-vault/drafts/banger-seeds/05-pourquoi-distressed-est-moral]]
- [[writing-vault/drafts/banger-seeds/06-distressed-comme-jeu]]
- [[writing-vault/drafts/banger-seeds/08-context-farmer-paul-signature]]
- [[writing-vault/drafts/banger-seeds/09-metier-100-paris]]
- [[brantham/linkedin/week-02-2026-05-05/dsys-lp/meme-anakin-lp]]
