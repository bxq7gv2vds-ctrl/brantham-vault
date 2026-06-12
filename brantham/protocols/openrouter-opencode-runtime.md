---
type: protocol
project: brantham
updated: 2026-05-20
---

# OpenRouter + OpenCode Runtime

## Objectif

Executer des workflows internes Brantham dans le vault Obsidian avec delegation entre agents, selection automatique du modele le moins cher possible et escalade controlee vers un modele plus puissant.

## Lancement

```bash
cd /Users/paul/vault
opencode
```

Verifier les modeles disponibles avec :

```bash
opencode models
```

Si les noms OpenRouter changent, corriger `opencode.jsonc`.

## Politique modele

### Flash par defaut

Utiliser `openrouter/deepseek/deepseek-v4-flash` pour :

- extraction ;
- resume ;
- classification ;
- nettoyage ;
- brouillons ;
- fiches Markdown ;
- CSV/JSON ;
- recherche initiale.

### Pro sur escalation

Utiliser `openrouter/deepseek/deepseek-v4-pro` pour :

- analyse financiere ;
- analyse juridique ;
- data room ;
- scoring final ;
- decision go/no-go ;
- QC critique ;
- code complexe.

## Delegation

Le `brantham-router` ne doit pas tout faire lui-meme. Il delegue :

- `brantham-hunter` pour repreneurs/OSINT ;
- `brantham-analyst` pour analyse complexe ;
- `brantham-writer` pour emails et notes ;
- `brantham-website` pour website/code ;
- `brantham-qc` pour controle qualite.

## Computer use local

Actions autorisees avec prudence :

- lire et ecrire dans le vault ;
- lancer scripts locaux apres validation ;
- faire recherches web apres validation ;
- produire CSV/JSON/Markdown ;
- utiliser navigateur/Playwright si configure et valide.

Actions interdites sans validation explicite :

- supprimer ;
- deplacer ;
- renommer massivement ;
- envoyer email ;
- publier/deployer ;
- modifier un repo externe au vault ;
- utiliser des donnees confidentielles hors perimetre.

## Pattern de demande utilisateur

```text
Utilise le workflow Brantham.
Objectif: [mission].
Dossier: [chemin].
Modele: economique par defaut, Pro seulement si necessaire.
Livrables: [fiches/CSV/emails/synthese].
Contraintes: ne rien envoyer, ne rien supprimer, sources obligatoires.
```
## Related
## Related
## Related
