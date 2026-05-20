---
tags:
  - brantham/playbook
  - repreneurs
  - osint
  - sourcing
modeles_recommandes:
  extraction: DeepSeek V4 Flash
  analyse: DeepSeek V4 Pro
  agents_longs: Kimi / GLM / Qwen
---

# Recherche Repreneurs

## Objectif

Identifier, qualifier et prioriser des repreneurs potentiels pour un dossier de cession ou reprise, puis produire des fiches Markdown, une longlist exploitable et des angles d'approche.

## Inputs necessaires

- Nom de la cible, secteur, localisation, taille, chiffre d'affaires, EBITDA si disponible.
- Type d'operation recherchee : reprise totale, majoritaire, minoritaire, adossement, carve-out, distressed.
- Contraintes du mandat : confidentialite, zones geographiques, profils exclus, concurrents sensibles.
- Criteres prioritaires : capacite financiere, fit industriel, experience sectorielle, rapidite d'execution, reputation.
- Sources autorisees : web, bases internes, Pappers, Societe.com, LinkedIn, presse, bases sectorielles, CRM.

## Etapes de travail

1. Reformuler le besoin et lister les criteres de recherche.
2. Segmenter les repreneurs : industriels, fonds, search funds, dirigeants/personnes physiques.
3. Construire les requetes OSINT par segment, secteur, geographie et mots-cles.
4. Collecter uniquement des informations sourcables.
5. Dedoublonner les candidats et normaliser les noms d'entites.
6. Creer une fiche courte par repreneur prioritaire.
7. Scorer les repreneurs en A/B/C avec justification explicite.
8. Produire une longlist CSV et une shortlist commentee.
9. Proposer les angles d'approche et drafts d'emails sans envoi automatique.

## Format de sortie

- Note de synthese Markdown.
- Fiches repreneurs dans `02_Repreneurs/`.
- Longlist CSV dans `08_Exports/`.
- Tableau de scoring : nom, segment, pays, secteur, taille estimee, rationale, score, sources, prochaines actions.
- Angles d'approche par segment.

## Regles de qualite

- Ne jamais inventer de source, de chiffre, de contact ou de relation capitalistique.
- Separer clairement faits, hypotheses, calculs et interpretations.
- Indiquer le niveau de confiance pour chaque candidat.
- Preferer moins de candidats mais mieux qualifies si les sources sont faibles.
- Marquer comme "a verifier" toute information non confirmee par une source primaire ou fiable.

## Regles de citation des sources

- Chaque fait externe doit avoir une source ou etre marque "non source".
- Citer le titre de la page, l'URL, la date de consultation et la date de publication si disponible.
- Conserver les extraits courts et utiles, sans copier de longs passages.
- Privilegier les sources primaires : site de l'entreprise, registre, communiques, documents officiels.

## Points necessitant validation humaine

- Inclusion d'un concurrent direct ou d'un acteur sensible.
- Qualification finale A/B/C des candidats importants.
- Utilisation de donnees confidentielles du mandat.
- Envoi d'emails ou prise de contact.
- Interpretation d'un signal faible non confirme.

## Exemples de prompts utilisables

```text
Trouve 50 repreneurs potentiels pour le dossier suivant. Separe industriels, fonds, search funds et dirigeants. Pour chaque candidat, donne les faits sources, les hypotheses, le score A/B/C et l'angle d'approche. N'invente aucune source.
```

```text
A partir de cette longlist, dedoublonne les candidats, signale les informations non sourcees, puis propose une shortlist de 15 repreneurs avec justification.
```

```text
Cree une fiche Obsidian pour chaque repreneur prioritaire avec profil, rationale, signaux, risques, sources, score et prochaines actions.
```
