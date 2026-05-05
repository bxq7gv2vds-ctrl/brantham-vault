---
name: Variant DA Brantham — blanc + bleu profond pour pitchs privés
description: Dérivation du DS Brantham D3 pour les présentations privées — palette bleu profond sur blanc, distinct du cream + bordeaux des contenus LinkedIn publics
type: decision
date: 2026-05-05
project: brantham
---

# Variant DA Brantham — blanc + bleu profond pour pitchs privés

## Décision

Les decks de présentation **privés** (pitch repreneur, dossier d'analyse client, mémoire interne) utilisent un variant dérivé du DS Brantham D3 :

- Fond `#FAFAFA` (paper-pure, plus froid que le cream `#EFEBE0` du variant LinkedIn)
- Encre primaire `#001F54` (bleu deep)
- Encre secondaire `#14306E` (bleu mid — italique focus)
- Encre tertiaire `#5A6FA0` (bleu soft — labels mono, watermark)
- Accent négatif `#7A1D17` (bordeaux conservé pour signaux d'alerte uniquement)
- Typo : Source Serif 4 + DM Mono (inchangé)

Distinct du variant **LinkedIn public** : cream `#EFEBE0` + ink `#0A0A0A` + bordeaux `#7A1D17`.

## Pourquoi deux variants

Les deux audiences sont différentes :

| Variant | Audience | Sensation visée |
|---|---|---|
| Cream + bordeaux | LinkedIn / contenus publics | Dossier d'investigation, NYT memo |
| Blanc + bleu profond | Pitchs privés repreneurs / clients | Memo Lazard, papier institutionnel privé |

Le bleu profond évoque l'institutionnel financier (banques, fonds, cabinets de conseil) — cohérent avec l'audience repreneur (souvent financiers ou industriels).

## Implémentation

Le variant est encapsulé dans un fichier CSS unique `_pitch-base.css` placé dans le dossier du deck. Il :
- Rebind les tokens du DS Brantham via `.post { --ink: var(--bleu-deep); ... }`
- Restyle les composants existants (`.kicker`, `.h1`, `.lede`, `.table`, `.list`, `.ledger`) en variant blanc + bleu
- Ajoute les composants pitch-spécifiques (`.compare-pair`, `.alert`, `.cascade`, `.anchor-num`, `.scale-row`)

Aucune modification du DS Brantham source — le variant est une **surcharge propre** côté deck.

## Réutilisation

Pour un nouveau deal en pitch privé :
```bash
cp -r vault/brantham/deals/active/sas-fitness-levallois/pitch-deck/ <nouveau-deal>/pitch-deck/
```
Le fichier `_pitch-base.css` est portable. Aucun token à modifier — il faut juste éditer les contenus HTML.

## Related

- [[_system/MOC-decisions]]
- [[brantham/_MOC]]
- [[brantham/sessions/2026-05-05-sas-fitness-levallois-pitch-deck]]
- [[brantham/linkedin/_design-system/README|Design System D3 — variant LinkedIn cream]]
- [[brantham/deals/active/sas-fitness-levallois/pitch-deck/README]]
- [[founder/decisions/2026-05-05-pitch-deck-html-png-vs-pptx]]
