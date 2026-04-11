---
type: pattern
project: brantham
date: 2026-04-11
category: design
tags: [design-system, brand, charte-graphique, presentations, corporate]
---

# Charte Graphique — Brantham Partners

Direction artistique unifiee pour tous les supports : pitch deck, teaser one-pager, data room, lettres, rapports.

Reference absolue. Aucun support ne doit devier de ces specs.

---

## 1. Palette de couleurs

### Couleurs primaires

| Token | Hex | Usage |
|---|---|---|
| `navy-deep` | `#001438` | Fonds sombres (couvertures, slides cles, headers) |
| `navy` | `#001F54` | Accent fort, pastilles, cartes sur fond sombre, barres |
| `navy-card` | `#001A3D` | Fond cartes sur slide sombre (subtil, profondeur sans contraste dur) |
| `cream` | `#FAFAF8` | Fonds clairs (contenu, slides intermediaires) |
| `white` | `#FFFFFF` | Fond cartes sur slide clair, texte sur fond sombre |

### Couleurs de texte

| Token | Hex | Usage |
|---|---|---|
| `ink` | `#0F0F0E` | Titres sur fond clair |
| `t2` | `#4A4A47` | Corps de texte sur fond clair |
| `t3` | `#6A6A66` | Texte secondaire universel (clair et sombre) |
| `t4` | `#767672` | Labels discrets, numeros de page/slide, metadata |

### Couleurs fonctionnelles

| Token | Hex | Usage |
|---|---|---|
| `accent` | `#5B9BD5` | Eyebrows, metriques, liens, lignes decoratives |
| `stone` | `#E5E4E0` | Borders cartes fond clair, separateurs legers |
| `line-dark` | `#0A1E3D` | Lignes de separation sur fond sombre |
| `off` | `#F5F4F2` | Fond module headers (one-pager uniquement) |
| `red` | `#C8251A` | Deadlines uniquement. Aucun autre usage. |

### Interdits absolus

- Violet / purple — interdit partout
- Orange, vert vif, jaune — interdit
- Gradients multicolores — interdit
- Ombres portees visibles, glow, reflets — interdit
- Opacites faibles (<30%) comme couleur principale — interdit

---

## 2. Typographie

### Famille de polices

| Role | Police | Poids | Fallback |
|---|---|---|---|
| Titres display (print) | Georgia | Regular | Times New Roman, serif |
| Titres display (web/one-pager) | Instrument Serif | Regular | Georgia, serif |
| Corps de texte | DM Sans | 300-600 | Inter, Helvetica, sans-serif |
| Donnees, metriques, code | DM Mono | 400-500 | JetBrains Mono, monospace |

**Regle** : Georgia pour les decks (PPTX/PDF), Instrument Serif pour le web et les one-pagers HTML. Meme intention esthetique, adaptation au medium.

### Echelle typographique

| Role | Police | Weight | Taille | Couleur | Notes |
|---|---|---|---|---|---|
| Titre principal | Georgia | Regular | 44-54pt | white / ink | Selon le fond |
| Titre secondaire | Georgia | Regular | 32-36pt | white / ink | — |
| Sous-titre | DM Sans | Light 300 | 15-18pt | t3 | — |
| Corps | DM Sans | Regular 400 | 11-13pt | t2 / t3 | — |
| Corps emphase | DM Sans | Semi-bold 600 | 11-13pt | ink / white | — |
| Chiffre hero | DM Mono | Medium 500 | 36-48pt | white / navy | Point focal |
| Chiffre secondaire | DM Mono | Medium 500 | 24-28pt | navy / white | Cartes, KPIs |
| Metrique / KPI | DM Mono | Regular 400 | 10-11pt | accent | Toujours en accent |
| Eyebrow | DM Mono | Medium 500 | 9pt | accent | MAJUSCULES, letter-spacing 200 |
| Label discret | DM Sans | Regular 400 | 9pt | t4 | — |
| Numero de slide/page | DM Mono | Regular 400 | 9pt | t4 | — |

### Regles typographiques

1. **3 niveaux de hierarchie maximum** par slide/page : eyebrow, titre, contenu.
2. **Aucun texte en dessous de 8pt.** Jamais.
3. **Les chiffres sont toujours plus gros** que le texte adjacent. Toujours.
4. **Max 40 mots** de texte continu par bloc. Au-dela, couper.
5. **Pas de bullet points** (ronds noirs). Utiliser 01, 02, 03... ou rien.
6. **Pas d'italique** sauf citations. Pas de souligne. Pas de ALL CAPS sur le corps.
7. **Eyebrows** : toujours MAJUSCULES, toujours accent, toujours DM Mono Medium 9pt.

---

## 3. Grille et espacement

### Format

- **Slides/decks** : 16:9 (33.867 cm x 19.05 cm)
- **One-pagers** : A4 landscape (297 x 210 mm)
- **Lettres/rapports** : A4 portrait (210 x 297 mm)

### Marges — Slides

| Cote | Valeur |
|---|---|
| Gauche | 1.5 pouces (3.81 cm) |
| Droite | 1.2 pouces (3.05 cm) |
| Haut | 1 pouce (2.54 cm) |
| Bas | 1 pouce (2.54 cm) |

**Regle critique** : marge gauche constante. Tous les titres, eyebrows et contenus demarrent au meme x = 1.5". Alignement vertical parfait entre les slides.

### Marges — Documents A4

| Cote | Valeur |
|---|---|
| Gauche | 2.5 cm |
| Droite | 2.5 cm |
| Haut | 3 cm |
| Bas | 2.5 cm |

### Espacements internes

| Element | Espacement |
|---|---|
| Eyebrow → titre | 12pt |
| Titre → sous-titre | 8pt |
| Sous-titre → contenu | 48pt minimum |
| Gouttiere entre colonnes | 0.4 pouces minimum |
| Padding interne des cartes | 28pt (4 cotes) |
| Coins arrondis cartes | 8-12pt (si le medium le permet) |
| Gap entre cartes grille | 0.25-0.3 pouces |

### Regles de composition

1. **Un seul point focal par slide.** L'oeil sait immediatement ou regarder.
2. **40%+ d'espace vide** sur chaque slide. Espace negatif = luxe.
3. **Alignement obsessionnel.** Chaque element sur la grille. Zero decalage.
4. **Alternance sombre/clair** recommandee : couverture sombre, contenu clair, conclusion sombre.
5. **Lignes decoratives** : fines (0.5-1pt), accent ou line-dark, max 2 par slide.
6. **Contenu a gauche** par defaut. Centre uniquement pour le slide de contact.
7. **Moitie droite vide sur les couvertures.** Espace negatif pur = premium.

---

## 4. Composants visuels

### Cartes (fond clair)

```
Background: white #FFFFFF
Border: 1pt stone #E5E4E0
Corners: 8-12pt radius
Padding: 28pt
Shadow: aucune
```

### Cartes (fond sombre)

```
Background: navy-card #001A3D
Border: aucune
Corners: 8-12pt radius
Padding: 24pt
Shadow: aucune
```

### Barre de KPIs

- Ligne horizontale fine 1pt au-dessus (line-dark ou stone selon le fond)
- N cellules reparties uniformement sur la largeur
- Valeur : DM Mono Medium 26pt, white/navy
- Label : DM Sans Regular 8pt, t4, MAJUSCULES, letter-spacing 120
- Label 6pt sous la valeur

### Eyebrow avec ligne

- Ligne horizontale 32px, 1pt, accent, a gauche du texte (meme baseline)
- Texte DM Mono Medium 9pt accent MAJUSCULES letter-spacing 200
- Espacement ligne-texte : 8px

### Pastilles de flux (pipeline)

- Rectangles navy #001F54 arrondis, taille identique (~1.4" x 0.3")
- Texte : DM Mono Medium 7pt white centre
- Gap entre pastilles : 0.15"
- Chevron `>` entre chaque : DM Mono 10pt t4

### Separateurs

- Fond clair : 1pt stone #E5E4E0
- Fond sombre : 0.5-1pt line-dark #0A1E3D
- Max 2 par slide/page

### Tableaux

- Header : DM Mono Medium 9pt accent MAJUSCULES
- Cellules : DM Sans Regular 11pt t2
- Lignes horizontales uniquement (pas de bordures verticales)
- Fond header : off #F5F4F2 (clair) ou navy-card (sombre)
- Lignes separatrices : stone ou line-dark selon le fond

---

## 5. En-tete et pied de page

### Header (one-pager / data room)

```
Background: navy-deep #001438
Height: 60-70px
Left: Logo "B" + "Brantham Partners" (DM Sans Semi-bold 14pt white)
Center: Titre du document (DM Sans Light 12pt white)
Right: "CONFIDENTIEL" (DM Mono 8pt t3) + reference + date
```

### Footer

```
Left: "Brantham Partners — Confidentiel" (DM Sans 7pt t4)
Right: Page N/N (DM Mono 8pt t4)
Separator: ligne fine stone au-dessus
```

### Numero de slide/page

- Position : haut droit
- Style : DM Mono 9pt t4
- Format : `02`, `03`, `04`... (zero-padded)
- Absent sur la couverture

---

## 6. Applications par type de support

### Pitch deck corporate

- Format : PPTX 16:9
- Fonts titres : Georgia
- Fonds : alternance navy-deep / cream
- 5-8 slides max
- Usage : presentation repreneur, investisseur, AJ

### Teaser one-pager

- Format : HTML → PDF (A4 landscape)
- Fonts titres : Instrument Serif
- Layout : 3 colonnes, KPI strip, modules avec headers off
- Donnees anonymisees, publiques uniquement
- Usage : premier contact buyer, envoi email

### Presentation data room

- Format : PPTX 16:9 ou HTML → PDF
- Fonts titres : Georgia
- Fonds : alternance navy-deep / cream
- Marque "CONFIDENTIEL" sur chaque slide
- Donnees reelles, chiffrees, detaillees
- 15-25 slides
- Usage : presentation post-data-room au buyer

### Lettre / rapport

- Format : A4 portrait, PDF
- En-tete navy avec logo
- Fonts titres : Georgia 18-24pt
- Corps : DM Sans 11pt
- Usage : lettre de mission, CGV, NDA, rapport de due diligence

### Email / document court

- Pas de logo inline (sauf signature)
- Police : DM Sans 13px
- Accent navy pour liens
- Usage : outreach, follow-up, envoi teaser

---

## 7. Logo

### Logo principal

- Monogramme : lettre `B` seule
- Lockup : `B` + `Brantham Partners`
- Couleur : white sur fond sombre, navy-deep sur fond clair
- Pas de tagline dans le logo

### Regles d'usage

- Espace de protection : hauteur du B sur les 4 cotes
- Taille minimum : 24px de hauteur
- Pas de deformation, pas de rotation, pas d'ombre
- Sur fond image : interdit (pas de fond image de toute facon)

---

## 8. Interdits — Resume

| Interdit | Raison |
|---|---|
| Emojis | Pas corporate |
| Violet/purple | Direction artistique |
| Icones / pictogrammes / clipart | Bruit visuel |
| Stock photos / images | Pas notre style |
| Gradients multicolores | Cheap |
| Ombres portees / glow / reflets | Cheap |
| Bullet points (ronds noirs) | Numeros ou rien |
| Texte < 8pt | Illisible |
| Plus de 40 mots continu | Couper |
| Texte centre (sauf slide contact) | Aligner a gauche |
| Borders visibles sur fond sombre | Profondeur par la couleur |
| Plus de 3 niveaux hierarchiques | Simplifier |
| Italic (sauf citations) | — |
| Souligne | — |
| ALL CAPS sur le corps | Eyebrows uniquement |

---

## 9. Checklist qualite — Avant validation

- [ ] Palette respectee (aucune couleur hors charte)
- [ ] Typographie respectee (polices, poids, tailles)
- [ ] Marges gauches identiques sur tous les slides
- [ ] Eyebrows au meme y entre les slides
- [ ] Titres au meme y entre les slides
- [ ] 40%+ d'espace vide par slide
- [ ] Zero emoji, zero icone, zero image
- [ ] Chiffres plus gros que le texte adjacent
- [ ] Lisible a 3 metres (titres 36pt+, chiffres 24pt+)
- [ ] Max 40 mots par bloc de texte
- [ ] Alternance sombre/clair coherente
- [ ] Mention "CONFIDENTIEL" si applicable
- [ ] Le deck degage "Lazard" pas "startup week-end"

---

## 10. Tokens CSS (reference technique)

Pour les supports HTML/web :

```css
:root {
  /* Backgrounds */
  --navy-deep: #001438;
  --navy: #001F54;
  --navy-card: #001A3D;
  --cream: #FAFAF8;
  --white: #FFFFFF;
  --off: #F5F4F2;

  /* Text */
  --ink: #0F0F0E;
  --t2: #4A4A47;
  --t3: #6A6A66;
  --t4: #767672;

  /* Functional */
  --accent: #5B9BD5;
  --stone: #E5E4E0;
  --line-dark: #0A1E3D;
  --red: #C8251A;

  /* Typography */
  --font-display: 'Instrument Serif', Georgia, 'Times New Roman', serif;
  --font-display-print: Georgia, 'Times New Roman', serif;
  --font-body: 'DM Sans', Inter, Helvetica, sans-serif;
  --font-mono: 'DM Mono', 'JetBrains Mono', monospace;

  /* Spacing */
  --margin-left: 3.81cm;
  --margin-right: 3.05cm;
  --margin-top: 2.54cm;
  --margin-bottom: 2.54cm;
  --card-padding: 28pt;
  --card-radius: 10pt;
  --gutter: 0.4in;
}
```

## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[brantham/patterns/teaser-onepager-html-pdf]]
- [[brantham/patterns/teaser-patterns]]
