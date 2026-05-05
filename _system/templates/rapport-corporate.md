---
name: rapport-corporate
description: Convention de mise en forme pour tous les rapports Brantham Partners (audit deal, OSINT, valorisation, mémo financier)
type: pattern
created: 2026-05-05
---

# Convention rapport corporate Brantham

## Référence visuelle

`/Users/paul/Downloads/Dossier_Complet.pdf` --- mise en page LaTeX article, sobre, monochrome, serif Computer Modern. C'est la mise en forme cible pour **tous** les rapports Brantham (deal audits, mémos financiers, fiches OSINT, notes de cession).

## Template prêt à l'emploi

`vault/_system/templates/rapport-corporate.tex`

Compilation : `pdflatex rapport.tex` deux fois pour résoudre la table des matières.

## Règles de mise en forme

### Style général

- Police serif Latin Modern (Computer Modern), corps 11pt, A4, marges 2,5 cm.
- Texte justifié, interligne 1,5 (`\onehalfspacing`).
- Aucune couleur, aucun emoji, aucun encadré coloré. Monochrome strict.
- Pied de page : numéro de page centré.

### Hiérarchie des titres

| Niveau | Commande | Style |
|---|---|---|
| Page de garde | manuel, centrée verticalement | Titre `\Large\bfseries`, sous-titre `\normalsize` |
| Section grand titre | `\section{}` | `\Large\bfseries`, numéroté `1.` |
| Sous-section | `\subsection{}` | `\large\bfseries`, numéroté `1.1` |
| Sous-sous-section | `\subsubsection{}` | `\normalsize\bfseries` |
| Lead inline | `\textbf{Lead.}` en début de paragraphe | bold inline avec point |

### Conventions inline

- **Lead inline** pour entrer dans un paragraphe : `\textbf{Sa place.}`, `\textbf{Œuvre majeure.}`, `\textbf{Lecture.}`, `\textbf{Recommandation.}`. Toujours suivi d'un point puis du texte courant.
- *Italique* pour les noms d'œuvres, de marques média, de citations longues.
- Citations longues en environnement `quote` indenté.
- Listes à puces avec `\begin{itemize}[leftmargin=2em]`.
- Listes numérotées avec `\begin{enumerate}[leftmargin=2em]`.

### Tableaux

- Toujours `\toprule`, `\midrule`, `\bottomrule` (booktabs).
- Pas de bordures verticales.
- Aligner les chiffres à droite (`r`), le texte à gauche (`l`).
- Pour les tableaux longs : `longtable`. Pour les colonnes longues : `tabularx` ou `p{6cm}`.

### Page de garde

Minimaliste, centrée verticalement, contient uniquement :
1. Titre (Large bold)
2. Sous-titre (normalsize)
3. Contexte (« Brantham Partners --- Conseil M&A distressed »)
4. Date (AAAA-MM-JJ)
5. Mention de confidentialité (footnotesize italique)

### Avant-propos

Toujours présent, max 10 lignes. Doit contenir :
- Objet du rapport en une phrase
- Périmètre couvert
- Limites méthodologiques principales
- Liste numérotée « Utilisation recommandée »
- Liste à puces « Structure du rapport »

### Annexe sources

Toujours en fin de document. Numérotée. Chaque source : titre, URL, date de consultation.

Toujours ajouter une section finale **Limitations méthodologiques** : sources non consultées, bases payantes en panne, comptes non publiés au greffe, hypothèses non vérifiables.

## Workflow de production

1. Copier `vault/_system/templates/rapport-corporate.tex` dans `vault/brantham/deals/active/<slug>/rapport.tex` (ou `vault/brantham/reports/<slug>.tex`).
2. Remplir les champs `<<...>>`.
3. Compiler `pdflatex rapport.tex` deux fois.
4. Vérifier : sommaire à jour, page de garde propre, sources numérotées.
5. Commit dans le vault avec slug du dossier.

## Ce qu'on ne fait jamais

- Ajouter des couleurs, dégradés, encadrés colorés.
- Inclure des emojis ou icônes.
- Mélanger plusieurs polices.
- Mettre des en-têtes ou pieds de page chargés (logo, contact, etc.).
- Surcharger la page de garde.
- Écrire des paragraphes sans **lead inline** dans les sections analytiques.

## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[_system/templates/decision]]
- [[_system/templates/slides]]
