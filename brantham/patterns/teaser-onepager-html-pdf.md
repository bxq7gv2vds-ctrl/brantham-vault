---
type: pattern
project: brantham
date: 2026-03-22
category: content
tags: [teaser, pdf, html, design, one-pager]
---

# Teaser One-Pager HTML/PDF

Pattern de generation de teasers M&A one-pager au format HTML + PDF. Design aligne sur l'identite visuelle du site branthampartners.fr.

## Architecture

Le systeme genere un HTML landscape A4 avec les donnees du deal, puis le convertit en PDF via Chrome headless. Le rendu est pixel-perfect.

### Fichiers

| Fichier | Role |
|---|---|
| `api/generate_teaser_onepager.py` | Script de generation (HTML + PDF) |
| `api/templates/teaser-onepager.html` | Template HTML avec `{{PLACEHOLDERS}}` |
| `api/templates/teaser-onepager-example.html` | Exemple rempli (deal Artemis) |

### Utilisation

```python
from generate_teaser_onepager import generate_onepager_teaser

data = {
    "titre": "...",
    "secteur_court": "...",
    "ref": "2207",
    "date": "19.02.2026",
    "ca": "< 1M€",
    "effectif": "10-15",
    "localisation": "Nord (59)",
    "delai": "8 jours",
    "delai_urgent": True,
    "score": 72,
    "opportunite_p1": "Texte avec **bold markdown**...",
    "opportunite_p2": "...",
    "contexte_p1": "...",
    "leviers": [{"titre": "...", "desc": "..."}],
    "profil_rows": [{"label": "Secteur", "value": "..."}],
    "benchmark_rows": [{"label": "Marge brute", "median": "65-70%", "cible": "~68%"}],
    "scoring_dims": [{"label": "Marche", "value": 85}],
    "actifs": ["Fonds de commerce", "Droit au bail"],
    "vigilances": [{"titre": "...", "desc": "..."}],
    "profil_repreneur": "Texte avec **bold**...",
    "deadline_date": "27 fevrier 2026 — 17h00",
    "contact_nom": "Me Laurent MIQUEL (BMA)",
    "contact_tel": "03.28.36.17.36",
}

generate_onepager_teaser(data, "output.pdf", format="pdf")
generate_onepager_teaser(data, "output.html", format="html")
```

## Design System

Identique au site web branthampartners.fr :

- **Fonts** : Instrument Serif (titres display), DM Sans (body), DM Mono (labels mono)
- **Couleurs** : Navy `#001F54` (accent unique), Ink `#0F0F0E`, T2 `#4A4A47`, T3 `#8A8A86`, Off `#F5F4F2`, Border `#E5E4E1`, Red `#C8251A` (deadline uniquement)
- **Layout** : Landscape A4 (297x210mm), 3 colonnes avec modules a headers gris

## Structure du one-pager

| Zone | Contenu |
|---|---|
| Header navy | Logo B + Brantham Partners + titre + Confidentiel + ref + date |
| KPI strip | 5 cellules : CA, Salaries, Localisation, Delai (rouge), Score/100 |
| Col 1 | L'opportunite (narratif), Contexte de cession, Leviers de creation de valeur |
| Col 2 | Profil de l'actif (table), Benchmark sectoriel (table), Scoring par dimension (barres) |
| Col 3 | Perimetre de cession (tags), Points de vigilance, Profil recherche + CTA deadline navy |
| Footer | Branding + mention confidentielle |

## Regles de design

1. **1 couleur d'accent** : navy. Gris pour les scores bas. Rouge uniquement pour le delai.
2. **2 tailles de texte** : 10.5px body + 7.5px mono labels. C'est tout.
3. **Module headers** : fond `--off` + label mono uppercase navy. Pas de badges colores.
4. **Bold** : utilise `**markdown**` dans les textes, converti en `<strong>` automatiquement.
5. **PDF** : genere via Chrome headless (`--print-to-pdf`), rendu identique au navigateur.

## Contenu d'un teaser distressed qui convertit

1. **Hook** — Pourquoi cette boite vaut le coup (pas "entreprise en difficulte" mais "opportunite strategique")
2. **Snapshot** — 5 chiffres cles en un coup d'oeil
3. **L'opportunite** — Positionnement, avantages concurrentiels, ce qui rend l'actif attractif
4. **Le marche** — Tendances sectorielles, benchmarks, montrer que le marche est porteur
5. **Le contexte** — Procedure positivee, prix decote comme argument, activite operationnelle
6. **Les actifs** — Tangibles et intangibles inclus dans la cession
7. **Les leviers** — Ce qu'un repreneur peut debloquer (nouveaux canaux, synergies)
8. **Les risques** — Transparent, credibilise. Aide l'acheteur a se qualifier
9. **Deadline + CTA** — Contact clair, date limite, reference

## Relation avec l'ancien systeme

L'ancien generateur PPTX (`generate_teaser.py`) utilise Cormorant Garamond + Work Sans + un template PPTX. Ce nouveau systeme le remplace pour les one-pagers avec un rendu superieur et aligne sur l'identite du site web.

## Related
- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[brantham/sessions/2026-03-22]]
- [[founder/sessions/2026-03-22-polytech-strategist]]
- [[founder/sessions/2026-03-22-polytech-calibration]]
- [[website/bugs/2026-03-21-contenu-duplique-geo-secteur]]
- [[brantham/bugs/2026-03-02-matrice-aj-secteur-taux-cession]]
- [[brantham/bugs/2026-03-02-analyse-regionale-unique-constraint]]
- [[brantham/bugs/2026-02-19-llm-glm47-content-null]]
- [[brantham/bugs/2026-03-05-asyncpg-another-operation]]
