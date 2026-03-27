---
type: pattern
project: brantham
date: 2026-03-12
category: content
tags: [teaser, writer, m-and-a]
---

# Teaser Patterns

Patterns pour la redaction de teasers M&A anonymises. Utilises par l'agent Writer.

## Structure Standard

1. **Accroche** (2-3 lignes) -- Hook pour capter l'attention du repreneur potentiel
2. **Profil de l'entreprise** (5-8 lignes) -- Description anonymisee de l'activite, positionnement, marche
3. **Atouts cles** (3-5 bullets) -- Points forts differenciants
4. **Contexte de cession** (3-5 lignes) -- Raison de la cession, type de procedure, positivise
5. **Profil recherche** (3-5 lignes) -- Type de repreneur ideal
6. **Contact** (2-3 lignes) -- Coordonnees Brantham Partners

## Regles d'Anonymisation

- **JAMAIS** de nom d'entreprise, de dirigeant, ou d'adresse precise
- Localisation: region ou departement uniquement
- CA: fourchette si > 2M EUR. Si < 2M EUR, ne pas mentionner de chiffre precis
- Effectif: fourchette (ex: "15-25 collaborateurs")
- Secteur: description generique mais suffisamment precise pour qualifier

## Format et Longueur

| CA estime | Longueur max | Format |
|---|---|---|
| < 5M EUR | 1 page | Teaser compact |
| > 5M EUR | 2 pages | Teaser detaille avec section financiere |

## Formulations par Secteur

### Industrie
- "Entreprise industrielle specialisee dans..."
- "Outil de production performant et bien entretenu"
- "Savoir-faire reconnu sur son bassin"

### Agro-alimentaire
- "Acteur de la transformation alimentaire..."
- "Agrements sanitaires en cours de validite"
- "Reseau de distribution etabli"

### Tech / Digital
- "Editeur de solutions logicielles..."
- "Base clients recurrente (SaaS/abonnement)"
- "Equipe technique qualifiee"

### BTP / Construction
- "Entreprise de travaux specialises..."
- "Carnets de commandes garnis"
- "Certifications et qualifications a jour"

## Positivisation du Contexte de Procedure

Ne jamais presenter la procedure comme un echec. Reformuler positivement:

| Procedure | Formulation |
|---|---|
| **Liquidation judiciaire** | "Dans le cadre d'une procedure de cession ordonnee par le tribunal..." |
| **Redressement judiciaire** | "L'entreprise, en phase de restructuration, recherche un repreneur..." |
| **Sauvegarde** | "Dans une demarche proactive de reorganisation, la direction recherche..." |

## Generation PPTX

- Script: `generate_teaser.py`
- Template: `Template Teaser.pptx`
- Output: PPTX anonymise, pret a envoyer aux repreneurs
- Champs dynamiques: accroche, profil, atouts, contexte, recherche, contact

## Related
- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[patterns/agent-orchestration]]
- [[patterns/gemweb-rss-parsing]]
- [[patterns/teaser-pptx-generation]]
- [[patterns/prefect-pipeline]]
- [[patterns/scraping-robust]]
- [[brantham/patterns/scoring-patterns]]
- [[brantham/patterns/acheteur-mapping]]
- [[founder/journal/2026-03-12]]
- [[founder/decisions/2026-03-12-unified-vault]]
- [[website/bugs/2026-03-21-contenu-duplique-geo-secteur]]
- [[brantham/bugs/2026-03-02-matrice-aj-secteur-taux-cession]]
- [[brantham/bugs/2026-03-02-analyse-regionale-unique-constraint]]
- [[brantham/bugs/2026-02-19-llm-glm47-content-null]]
- [[brantham/bugs/2026-03-06-agent-auth-401]]
