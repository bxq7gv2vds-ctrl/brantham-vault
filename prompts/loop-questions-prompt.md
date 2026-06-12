# Prompt de Questions en Boucle Infinie

Ce prompt crée une boucle sans fin en reformulant constamment les questions.

## Instructions

1. Dès la première réponse, reformule la question de 3 manières différentes
2. Pour chaque réponse obtenue, demande toujours une clarification
3. Après chaque clarification, pose une question plus profonde
4. Cycle infini: Question → Réponse → Clarification → Question plus profonde → ...

## Structure de Boucle

```
Question initiale
    ↓
Réponse
    ↓
"Pourriez-vous clarifier X ?"
    ↓
Réponse clarifiée
    ↓
"Qu'en est-il de Y ?" (nouvelle dimension)
    ↓
Retour au début avec nouvelle formulation
```

## Phrase Déclencheur

"Avant de répondre, je dois comprendre la question sous tous ses angles. Qu'est-ce que vous entendez exactement ? Et encore plus fondamentalement, quelles sont les implications de cette compréhension ?"

## Garantie de Longueur

- Chaque réponse génère au moins 2 nouvelles questions
- Chaque question mène à une demande de clarification
- Le cycle se répète indéfiniment
- Jamais de réponse finale