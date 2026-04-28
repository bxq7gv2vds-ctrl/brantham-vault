# Brantham — LinkedIn Design System

Système de templates HTML/CSS pour visuels LinkedIn. Une seule DA, tous les formats.

## DA — Mono dossier brutaliste (D3)

- **Fond** : cream `#EFEBE0` (light) · navy `#000F2A` (dark)
- **Encre** : `#0A0A0A`
- **Accents** : bordeaux `#7A1D17` · navy `#001F54` · or `#C8B97A`
- **Typo display** : Source Serif 4 (titres + body lede)
- **Typo data/UI** : DM Mono (références, meta-bar, tampons, footer)
- **Signatures** : watermark vertical gauche · tampon rotaté haut droite · références FR-0X

## Structure

```
_design-system/
├── base/
│   ├── tokens.css      # variables couleur + typo + reset
│   └── base.css        # composants (head, foot, watermark, stamps, table, ledger, list, quote)
├── templates-1080x1080/    # carré standard LinkedIn
├── templates-1080x1350/    # vertical (engagement max)
├── templates-1200x628/     # paysage (header article / lien)
├── templates-1920x1080/    # slides PDF carrousel 16:9
├── logo.png
├── render.py           # render PNG retina @2x via Playwright
└── README.md
```

Chaque dossier `templates-XxY/` contient :
- `_format.css` — surcharge des variables `--t-*` selon dimensions
- des `.html` autoporteurs prêts à dupliquer

## Templates par format

| Format     | Templates disponibles                                                  |
|------------|------------------------------------------------------------------------|
| 1080×1080  | data-table, data-ledger, data-checklist, headline-only, quote-card, cover-slide |
| 1080×1350  | (idem 1080×1080 — copie auto-adaptée)                                  |
| 1200×628   | cover-banner, stat-banner, headline-banner, quote-banner               |
| 1920×1080  | slide-cover, slide-content, slide-quote, slide-end                     |

## Workflow type — créer un nouveau visuel

1. Choisir format + template :
   ```
   cp templates-1080x1080/data-table.html ../mes-posts/2026-05-mon-post.html
   ```
2. Éditer le HTML : titre, kicker, contenu de la table/ledger/list.
3. Render :
   ```bash
   cd _design-system
   python3 render.py 1080x1080
   ```
   Produit `mon-post.png` retina 2160×2160.

## Variant dark (navy)

Ajouter la classe `dark` à `.post` :
```html
<div class="post dark">...</div>
```
Tous les tokens `--ink`, `--ink-soft`, `--ink-mute`, `--rule` se rebindent automatiquement. Le logo s'inverse via `filter: brightness(0) invert(1)`. Aucun override par élément à écrire.

## Composants disponibles

### Head (logo + meta-bar)
```html
<header class="head">
  <div class="brand"><img src="../logo.png" alt="Brantham"></div>
</header>

<div class="meta-bar" style="--meta-cols:4;">
  <div>Volume <b>67 830</b></div>
  <div>Variation <b>+16 %</b></div>
  <div>Période <b>2025</b></div>
  <div>Source <b>INSEE · BdF</b></div>
</div>
```
La variable `--meta-cols` règle le nombre de colonnes (3, 4, 5).

### Watermark vertical (signature dossier)
```html
<div class="watermark">Brantham Partners · Confidentiel · n°XX/2026</div>
```

### Tampons
```html
<div class="stamp">Type<b>N°XX·2026</b><span class="x">04 · Avril</span></div>
<div class="stamp2">Étude · Avril 2026</div>
```

### Body — kicker + h1 + lede
```html
<div class="body">
  <div class="kicker">Section · Sous-section</div>
  <h1 class="h1">Titre <span class="it">avec italique</span> de focus.</h1>
  <p class="lede">Paragraphe d'introduction. <b>Chiffre clé</b> en gras.</p>
</div>
```

### Table (5 cols)
```html
<div class="table">
  <div class="row h"><div>Réf.</div><div>Secteur</div><div>Part</div><div>Dossiers</div><div>vs n-1</div></div>
  <div class="row"><div class="num">FR-01</div><div class="name">...</div><div class="pct">21 %</div><div class="count">14 264</div><div class="delta">+14 %</div></div>
  <div class="row flag">...</div>  <!-- ligne mise en avant (bordeaux) -->
</div>
```

### Ledger (calcul / coût)
```html
<div class="ledger">
  <div class="li"><div class="op">+</div><div class="lbl">Poste<span class="note">détail</span></div><div class="val">100 — 200 k€</div></div>
  ...
  <div class="total"><div class="op">=</div><div class="lbl">Total</div><div class="val">485 — 810 k€</div></div>
</div>
```

### List (checklist)
```html
<div class="list">
  <div class="item">
    <div class="num">FR-01</div>
    <div class="label">Titre du point</div>
    <div class="desc">Description courte.</div>
  </div>
</div>
```

### Quote (verbatim)
```html
<p class="quote">Citation en italique avec guillemets bordeaux.</p>
<div class="quote-attr"><b>D. M.</b> · Fonction · Contexte</div>
```

### Footer
```html
<footer class="foot">
  <div class="sig"><div class="n">Paul Roulleau</div><div class="f">Brantham Partners — M&A distressed</div></div>
  <div class="credit"><div><b>Source</b> · INSEE · BdF</div><div><b>Voir</b> · branthampartners.fr</div></div>
</footer>
```

## Variables surchargeables (par template)

Toutes les variables `--t-*` (taille typographique, padding) sont définies dans `_format.css`. Pour un visuel one-shot, les surcharger dans le `<style>` du HTML :
```css
.post { --t-h1: 72px; --t-pad-body: 160px; }
```

## Render

```bash
python3 render.py                # tous formats
python3 render.py 1080x1080      # un seul format
```
Génère un `.png` à côté de chaque `.html`. Retina 2x (file × 2 px). Skipe les `_format.css` automatiquement.

## Règles cardinales (à ne pas casser)

- **1 fond** par variant (cream OU navy, jamais entre-deux)
- **2 typos max** : Source Serif 4 + DM Mono
- **3 niveaux** typographiques : kicker · h1 · lede
- **1 accent** : bordeaux en light, or en dark
- **Watermark + tampon = signature** — toujours présents (c'est ce qui rend la DA non-réplicable)
- **Pas d'italique gratuit** : seulement sur mots de focus dans le titre
- **Pas de gradient, pas de grain, pas d'ombre**
- **Pas d'emoji**

## Liens vault

- Décisions DA : `vault/founder/decisions/2026-04-27-da-linkedin-mono-dossier-brutaliste.md` (à créer)
- Pattern : `vault/brantham/patterns/linkedin-design-system.md` (à créer)
