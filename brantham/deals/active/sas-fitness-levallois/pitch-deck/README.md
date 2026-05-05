---
name: Pitch deck SAS Fitness Levallois — README
description: Système de slides 16:9 pour la présentation du deal au repreneur — DA Brantham D3 (variant blanc + bleu profond)
type: deck-system
created: 2026-05-05
---

# Pitch repreneur — SAS Fitness Levallois

Deck 16:9 (1920×1080) construit sur le design system Brantham D3, variant **blanc + bleu profond** dérivé pour les présentations privées au repreneur (vs cream + bordeaux pour les contenus LinkedIn publics).

Sortie HTML/CSS rendue en PNG retina @2x via Playwright.

## Structure

```
pitch-deck/
├── _pitch-base.css      # tokens + composants partagés (single source of truth)
├── render.py            # rend tous les .html → .png
├── 01-cover.html        # slide 01 — couverture (canonique)
├── 04-trajectoire.html  # slide 04 — trajectoire financière 4 ans (sample)
└── _archive/            # itérations rejetées
```

## DA — variant blanc + bleu profond

| | |
|---|---|
| Fond | `#FAFAFA` (paper-pure) |
| Encre primaire | `#001F54` (bleu-deep) |
| Encre secondaire | `#14306E` (bleu-mid) — utilisée pour italique focus |
| Encre tertiaire | `#5A6FA0` (bleu-soft) — labels mono, watermark |
| Accent négatif | `#7A1D17` (bordeaux conservé pour signaux d'alerte) |
| Typo display | Source Serif 4 (titres + body) |
| Typo data/UI | DM Mono (références, kicker, footer credit) |

## Composants exposés par `_pitch-base.css`

Hérités du DS Brantham, restylés pour le variant bleu :
- `.head` — logo top-left (56px)
- `.foot` — signature + crédit, séparateur épais
- `.stamp` — section mark top-right (`§ ACTE · NN/13`)
- `.watermark` — texte vertical gauche
- `.kicker`, `.h1`, `.lede`, `.table`, `.list`, `.ledger`

Spécifiques pitch :
- `.compare-pair` — bloc 2 col avant/après ou repris/exclu
- `.alert` — encart "à savoir" / "lecture" (variant `.warn` rouge)
- `.cascade` — décomposition à barres horizontales (slide money cascade)
- `.anchor-num` — chiffre signature de section (slide point vital)
- `.scale-row` + `.scale-total` — liste numérotée 01/02/03 + montant + ligne total

## Workflow

```bash
cd /Users/paul/vault/brantham/deals/active/sas-fitness-levallois/pitch-deck
python3 render.py             # rend toutes les slides
python3 render.py 01-cover    # rend une slide spécifique
```

Le script utilise Playwright Chromium en device_scale_factor=2 pour produire des PNG retina (3840×2160).

## Mapping des 13 slides

| # | Slide | Composants | Statut |
|---|---|---|---|
| 01 | Cover | `cover-edition` + `cover-title` + `cover-deck` | ✓ rendu |
| 02 | Identité cible | `kicker` + `h1` + `lede` + `scale-row × 4` | ☐ à faire |
| 03 | Procédure | `kicker` + `h1` + `lede` + `scale-row × 4` | ☐ à faire |
| 04 | Trajectoire 4 ans | `kicker` + `h1` + `lede` + `table` 5 cols | ✓ rendu |
| 05 | Point vital — bail | `kicker` + `anchor-num` + `h1` + `alert.warn` | ☐ à faire |
| 06 | PO 6 mois | `kicker` + `h1` + `scale-row × 3` + `alert` | ☐ à faire |
| 07 | Money cascade | `kicker` + `h1` + `cascade × 5` | ☐ à faire |
| 08 | Levier — loyer | `kicker` + `h1` + `compare-pair` + `alert` | ☐ à faire |
| 09 | Trois scénarios | `kicker` + `h1` + `scale-row × 3` | ☐ à faire |
| 10 | Périmètre repris/exclu | `kicker` + `h1` + `compare-pair` | ☐ à faire |
| 11 | Ticket 115 K€ | `kicker` + `h1` + `scale-row × 4` + `scale-total` | ☐ à faire |
| 12 | Conditions go/no-go | `kicker` + `h1` + `scale-row × 3` (qualifier rouge) | ☐ à faire |
| 13 | Recommandation | `kicker` + `h1` (large) + `lede` + footer renforcé | ☐ à faire |

## Réutilisation pour un autre deal

1. `cp -r pitch-deck/ ../<autre-deal>/pitch-deck/`
2. Adapter le contenu HTML (titre, kicker, données)
3. Le path relatif vers le DS reste valide tant que la cible est sous `vault/brantham/deals/active/<deal>/`
4. `python3 render.py` regénère tous les PNG

Aucun token de couleur ou de typo à modifier — la DA est fixée dans `_pitch-base.css` au niveau du dossier `pitch-deck/`.

## Decisions de design

- **115 K€ retiré de la cover** — c'est l'aboutissement du raisonnement, pas un teaser ; il a sa slide dédiée n°11.
- **Tampon contextualisé** (`§ ACTE · NN/13`) plutôt que metadata admin — sert de chapter mark.
- **PNG plutôt que PPTX éditable** — la fidélité à la DA Source Serif 4 + Instrument Serif italique inline + watermark vertical rotaté n'est pas atteignable proprement dans python-pptx. Édition = HTML source, regénération = `render.py` 1 commande.

## Related

- [[brantham/deals/active/sas-fitness-levallois/_MOC]]
- [[brantham/linkedin/_design-system/README|Design System D3]]
- [[brantham/patterns/charte-graphique]]
- [[brantham/sessions/2026-05-05-sas-fitness-levallois-pitch-deck]]
