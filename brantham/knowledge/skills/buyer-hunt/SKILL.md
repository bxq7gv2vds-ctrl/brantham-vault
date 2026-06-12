---
type: skill
project: brantham
name: buyer-hunt
model_default: deepseek-v4-flash
model_escalation: deepseek-v4-pro
---

# Skill: Buyer Hunt

## Quand l'utiliser

Utiliser cette skill pour rechercher, qualifier, scorer et documenter des repreneurs potentiels.

## Inputs necessaires

- dossier deal ;
- secteur, code NAF, geographie ;
- CA cible, EBITDA si disponible ;
- contraintes de confidentialite ;
- types de repreneurs recherches.

## Etapes

1. Lire `06_Playbooks/Recherche_Repreneurs.md`.
2. Extraire les criteres du deal.
3. Segmenter : industriels, fonds, search funds, dirigeants.
4. Rechercher des candidats sources.
5. Normaliser les noms, SIREN, sites, contacts.
6. Creer fiches et longlist.
7. Scorer preliminairement A/B/C.
8. Escalader a `brantham-analyst` pour scoring final sensible.

## Sorties

- fiches dans `02_Repreneurs/` ;
- CSV dans `08_Exports/` ;
- notes sources dans `05_OSINT/Recherches_Web/` si utile ;
- output JSON cowork.

## Regles qualite

- Source obligatoire pour chaque fait externe.
- Emails devines marques comme non verifies.
- Pas de contact automatique.
- Faits et hypotheses separes.
## Related
## Related
## Related
## Related
## Related
