---
name: Session 2026-05-05 — Pitch deck SAS Fitness Levallois
description: Construction du système de slides 16:9 pour la présentation au repreneur — DA Brantham D3 dérivée en variant blanc + bleu profond
type: session
date: 2026-05-05
project: brantham
deal: sas-fitness-levallois
---

# Session 2026-05-05 — Pitch deck SAS Fitness Levallois

## Objectif

Produire un deck de présentation pour le repreneur de la salle de sport en RJ, livré avant la décision interne du 14/05/2026 (DLDO 21/05/2026 12h).

## Itérations rejetées (archivées)

Avant d'arriver au système final, plusieurs pistes ont été explorées et rejetées par le founder :

1. **Deal X-Ray** — dashboard A3 one-pager. Verdict : "pas dingue ni révolutionnaire".
2. **Bloodline** — animation particulaire HTML montrant les flux d'argent. Verdict : trop gadget, illisible.
3. **Money Cascade standalone** — visualisation verticale des flux. Verdict : "vraiment de la merde", la décomposition doit être UNE slide dans un deck, pas un outil isolé.
4. **PPTX généré via python-pptx** — tentative de produire un fichier PowerPoint éditable. Rejeté pour deux raisons : (a) DA inventée à partir des screenshots LinkedIn, ne correspondait pas au vrai design system D3 du vault, (b) python-pptx ne peut pas reproduire fidèlement le watermark vertical, le tampon rotaté, les italiques inline Source Serif 4.

Tous archivés dans `_archive/` plutôt que supprimés (traçabilité).

## Découverte clé

Le founder pointe vers `vault/brantham/linkedin/_design-system/` — un design system Brantham D3 documenté avec règles cardinales : palette stricte (cream `#EFEBE0` ou navy `#000F2A`), Source Serif 4 + DM Mono uniquement, watermark vertical + tampon obligatoires. C'est la **single source of truth** pour la DA.

Avoir reconstitué la DA depuis les screenshots était une erreur — il fallait lire `tokens.css` et `base.css` directement.

## Pivot DA — variant blanc + bleu profond

Le founder demande un variant : fond blanc, encre bleu profond. Trois prototypes rendus (cream original, navy avec accents or, blanc avec bleu profond). Le variant blanc validé.

Tokens dérivés :
- Paper `#FAFAFA`
- Bleu deep `#001F54` (ink + accent)
- Bleu mid `#14306E` (italique focus)
- Bleu soft `#5A6FA0` (labels mono, watermark)
- Bordeaux `#7A1D17` conservé pour signaux d'alerte uniquement

## Itérations cover

| Version | Changement | Statut |
|---|---|---|
| v1 | Layout 2 col avec rail vertical `Chapitre I / § / Cession L. 642-1` | rejeté — § inutile, rail redondant avec watermark |
| v2 | Rail supprimé, watermark seul comme ancrage gauche, titre 124 px | base validée |
| v3 | Tampon admin remplacé par signature manuscrite italique `P. Roulleau` rotaté −3° | conservé en alternative |
| **v4** | **Stat 115 K€ retiré (spoile la punchline) · tampon = section mark `§ COUVERTURE 00/13` · titre 104 px** | **canonique → renommé `01-cover.html`** |

## Système final — `_pitch-base.css`

Single source of truth pour le deck. Importée par chaque slide HTML après les fichiers du DS Brantham.

Composants exposés :
- Restyle des composants DS (`.head`, `.foot`, `.stamp`, `.watermark`, `.kicker`, `.h1`, `.lede`, `.table`, `.list`, `.ledger`) en variant blanc + bleu
- Composants pitch-spécifiques : `.compare-pair`, `.alert`, `.cascade`, `.anchor-num`, `.scale-row` + `.scale-total`

Chaque slide = 4 imports CSS + composition de composants. Aucune duplication.

## Preuve de scalabilité

Slide 04 — Trajectoire 4 ans rendue en utilisant le `.table` 5-col du DS Brantham (le composant le plus dense). Démontre que le système supporte les vues data-heavy avec la même grammaire que la cover. Layout 2 col texte / table comme `slide-content` du DS, mais palette et chrome unifiés via `_pitch-base.css`.

## Décisions

- [[founder/decisions/2026-05-05-pitch-deck-html-png-vs-pptx|HTML/CSS rendu en PNG plutôt que PPTX éditable]]
- [[founder/decisions/2026-05-05-pitch-da-blanc-bleu-profond|Variant blanc + bleu profond pour pitchs privés]]

## Livrables

- `pitch-deck/_pitch-base.css` — système CSS partagé (single source of truth)
- `pitch-deck/render.py` — pipeline Playwright HTML → PNG retina @2x
- `pitch-deck/01-cover.html` + `.png` — slide canonique
- `pitch-deck/04-trajectoire.html` + `.png` — slide preuve de scalabilité
- `pitch-deck/README.md` — documentation système + mapping des 13 slides
- `_MOC.md` — map of content du deal

## Reste à faire

11 slides à décliner sur le système :
- 02 Identité, 03 Procédure → `scale-row` × 4
- 05 Point vital → `anchor-num` + `alert.warn`
- 06 PO 6 mois → `scale-row` × 3 + `alert`
- 07 Money cascade → `cascade` × 5
- 08 Levier loyer → `compare-pair` + `alert`
- 09 Scénarios → `scale-row` × 3
- 10 Périmètre → `compare-pair`
- 11 Ticket 115 K€ → `scale-row` × 4 + `scale-total`
- 12 Conditions → `scale-row` × 3 (qualifier rouge)
- 13 Recommandation → closer

Toute la grammaire est posée — il ne reste que la composition.

## Related

- [[brantham/_MOC]]
- [[brantham/deals/active/sas-fitness-levallois/_MOC]]
- [[brantham/linkedin/_design-system/README|Design System D3]]
- [[brantham/patterns/charte-graphique]]
- [[founder/decisions/2026-05-05-pitch-deck-html-png-vs-pptx]]
- [[founder/decisions/2026-05-05-pitch-da-blanc-bleu-profond]]
