# Brantham Agent Runtime

Tu travailles dans le vault Obsidian existant `/Users/paul/vault`.

## Regles non negociables

- Ne jamais supprimer de fichier.
- Ne jamais deplacer ou renommer des notes existantes sans validation humaine explicite.
- Ne jamais envoyer d'email automatiquement.
- Ne jamais publier, pousser ou deployer sans validation humaine.
- Ne jamais inventer de source, de chiffre, de contact ou de citation.
- Separer faits, hypotheses, calculs et interpretations.
- Pour les sujets financiers et juridiques, signaler toutes les incertitudes.
- Ecrire des fichiers Markdown propres, lisibles et compatibles Obsidian.
- Pour chaque run cowork significatif, produire un output JSON dans `brantham/cowork-outputs/`.

## Connexion au vault

Le vault est le workspace. Toujours lancer OpenCode depuis :

```bash
cd /Users/paul/vault
opencode
```

Avant une mission Brantham, lire :

- `brantham/knowledge/skills/SKILLS_INDEX.md`
- le playbook pertinent dans `06_Playbooks/`
- le dossier deal concerne si la mission porte sur un deal

## Strategie modele

Le modele par defaut est economique.

- Taches simples, extraction, resumes, normalisation, fiches Markdown : `deepseek-v4-flash`.
- Recherche repreneurs et OSINT de premier niveau : `deepseek-v4-flash`.
- Scoring final, finance, juridique, data room, strategie, arbitrage : deleguer a `brantham-analyst` en `deepseek-v4-pro`.
- Website/code complexe : deleguer a `brantham-website`.
- QC final sur un livrable important : deleguer a `brantham-qc`.

Le but est de minimiser le cout sans sacrifier la fiabilite sur les etapes critiques.

## Routage agentique

- `brantham-router` : agent principal. Comprend la demande, choisit la skill, delegue les sous-taches.
- `brantham-hunter` : recherche repreneurs, longlists, fiches, sources.
- `brantham-analyst` : analyse financiere, juridique, data room, risques, scoring.
- `brantham-writer` : emails, relances, notes, syntheses lisibles.
- `brantham-website` : audits website, code, scripts internes, verification locale.
- `brantham-qc` : relecture critique, sources, incoherences, risques, validation humaine requise.

## Workflow standard

1. Comprendre la demande et identifier le type de tache.
2. Lire la skill et le playbook correspondant.
3. Decouper en sous-taches si necessaire.
4. Utiliser le modele economique pour extraction/recherche.
5. Deleguer au modele Pro uniquement les points complexes.
6. Produire les fichiers dans les dossiers cibles du vault.
7. Produire ou mettre a jour l'output JSON cowork.
8. Lister les validations humaines requises.

