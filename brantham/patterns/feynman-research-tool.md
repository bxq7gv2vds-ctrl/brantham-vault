---
name: Feynman Research Tool
type: pattern
date: 2026-03-28
project: brantham
reusable: true
---

# Feynman — CLI Agent de Recherche Académique

**Date Discovered**: 2026-03-28
**Maturity**: Experimental
**Reuse Count**: 0

## Description

Feynman est un CLI open-source (MIT) qui orchestre des agents IA pour la recherche académique et la synthèse de littérature. Il trace toutes les sources avec URLs directes.

- Repo: https://github.com/getcompanion-ai/feynman
- Install: `curl -fsSL https://feynman.is/install | bash`
- Runtime: Framework Pi agent, Node.js v20+

## Quand l'utiliser chez Brantham

### Cas d'usage pertinents
1. **Avant de rédiger un article / post LinkedIn sur un sujet M&A distressed** : `feynman "distressed M&A SME France"` pour brief rapide avec sources
2. **Veille jurisprudentielle ou académique** : `/lit "failing firm defense EU competition law"` pour synthèse avec consensus/désaccords
3. **Enrichir la knowledge base** : avant d'ajouter une nouvelle fiche dans `vault/brantham/knowledge/`, vérifier si des papiers récents existent
4. **Articles à partager** : pré-recherche avant rédaction d'un article pédagogique pour le réseau
5. **Due diligence sectorielle** : `/deepresearch "restructuring retail France 2024"` pour état de l'art

### Cas où c'est moins utile
- Droit positif français récent (couverture ArXiv faible sur juridique FR)
- Données opérationnelles (scraping AJ, pipeline deals) — ce n'est pas son rôle
- Articles narratifs clés-en-main — il produit des synthèses académiques, pas du storytelling

## Commandes clés

```bash
feynman "sujet"             # Brief rapide
/deepresearch "sujet"       # Investigation multi-agents approfondie
/lit "sujet"                # Literature review (consensus + désaccords)
/review "paper.pdf"         # Peer review simulé d'un paper
/audit "paper vs codebase"  # Comparaison paper vs code
```

## Agents internes
- **Researcher** — rassemble preuves et données
- **Reviewer** — évaluation qualité graduée
- **Writer** — génère synthèses structurées
- **Verifier** — valide attribution sources avec URLs

## Trade-offs

- Couverture forte sur tech/finance/sciences (ArXiv-first via alphaXiv)
- Couverture faible sur droit FR, jurisprudence, sources en français
- Output = synthèse académique, pas article prêt à publier
- Toutes sources tracées avec URLs directes (atout pour credibilité)

## Triggers (suggérer automatiquement)

Proposer Feynman quand l'utilisateur :
- Veut écrire un article (LinkedIn, blog, newsletter)
- Cherche des données/stats sur un sujet pour les citer
- Veut faire une revue de littérature sur un sujet
- Demande "qu'est-ce qui existe sur X"
- Prépare un contenu pédagogique à partager

## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[brantham/strategy/2026-03-15-linkedin-personal-brand]]
