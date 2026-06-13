---
type: skills-index
project: brantham
updated: 2026-05-20
---

# Brantham Skills Index

Cet index sert au routage des missions OpenCode/OpenRouter dans le vault Obsidian.

## Regle generale

1. Identifier la nature de la demande.
2. Lire la skill correspondante.
3. Lire le playbook correspondant dans `06_Playbooks/`.
4. Executer avec le modele economique si possible.
5. Escalader vers un sous-agent Pro uniquement pour les taches complexes.
6. Ecrire les livrables dans le vault.
7. Produire un JSON cowork si la mission a plusieurs etapes.

## Skills principales

| Demande | Skill | Agent | Modele par defaut | Escalade |
|---|---|---|---|---|
| Trouver des repreneurs | `buyer-hunt/SKILL.md` | `brantham-hunter` | Flash | Analyst Pro pour scoring final |
| OSINT / recherche web | `buyer-hunt/SKILL.md` ou playbook OSINT | `brantham-hunter` | Flash | QC Pro si source critique |
| Analyse data room | `data-room-analysis/SKILL.md` | `brantham-analyst` | Pro | QC Pro |
| Analyse financiere | `finance-analysis/SKILL.md` | `brantham-analyst` | Pro | QC Pro |
| Analyse juridique | `legal-analysis/SKILL.md` | `brantham-analyst` | Pro | validation avocat/humain |
| Emails / relances | `outreach-writer/SKILL.md` | `brantham-writer` | Flash | Writer/QC Pro si sensible |
| Website / scripts | `website-improver/SKILL.md` | `brantham-website` | Pro | QC Pro |
| Orchestration cowork | `cowork-runtime/SKILL.md` | `brantham-router` | Flash | agents specialises |

## Skills existantes a consulter si pertinent

- `quick-scan-diagnostic.md`
- `ethique-repreneur.md`
- `negociation-crise.md`
- `communication-parties-prenantes.md`

## Politique de cout

Utiliser Flash pour :

- extraire ;
- resumer ;
- classer ;
- convertir ;
- dedoublonner ;
- produire des brouillons ;
- creer des fiches simples.

Utiliser Pro pour :

- raisonner ;
- arbitrer ;
- scorer ;
- analyser finance/juridique/data room ;
- ecrire une synthese critique ;
- verifier un livrable important.

## Sortie cowork obligatoire

Pour toute mission multi-etapes, creer un JSON dans `brantham/cowork-outputs/` avec :

- agent ;
- run_id ;
- timestamp ;
- status ;
- summary ;
- data ;
- actions_taken ;
- pending_for_human ;
- triggered_next ;
- errors.
## Related
## Related
## Related
## Related
## Related
## Related
## Related
