---
title: Refonte CRM Brantham V3 — simplification radicale
date: 2026-05-19
tags: [crm, ops, decision]
---

# Refonte CRM Brantham V3

## Contexte
Le CRM précédent (`brantham CRM` shared, 22+ colonnes par onglet, ID `17A4wLby1U_DAZodtKJy1RlsPl4ubM1UG8NgSCA7rxFc`) était sur-ingéniéré : colonnes inutilisées, formules cassées (`#ERROR!`, `#VALUE!` partout), aucune adoption réelle. Soren a demandé de repartir de zéro et simplifier.

## Décision
Création de `Brantham CRM V3` (ID Drive: `1u9iSLIaWAZONf3YT5lqqkNDkL6_j5w_L`) — 3 onglets minimaux :

### Onglet 1 — Opportunités (5 colonnes)
| Société | Lien annonce | CA | Activité | DLDO |

### Onglet 2 — `1. Contacts` (6 colonnes)
| Nom | Prénom | Fonction | Société | Cible | Statut |
- Dropdown Statut : `Contacté` (gris) / `Réponse` (vert)

### Onglet 3 — `2. En cours` (auto-rempli)
| Nom | Prénom | Fonction | Société | Cible | Statut détaillé |
- A2 = `=IFERROR(FILTER('1. Contacts'!A2:E1000; '1. Contacts'!F2:F1000="Réponse");"")`
- Dropdown Statut détaillé : `En attente de réponse` (jaune) / `À traiter` (rouge)

## Pourquoi
- Adoption réelle > exhaustivité. Un CRM qui ne tient pas dans la tête n'est jamais rempli.
- Auto-transfert via FILTER : zéro double saisie pour la partie opérationnelle.
- Couleurs sur dropdown via Conditional Formatting → priorisation visuelle immédiate.

## Limites connues
- La col F de l'onglet 3 (Statut détaillé) est manuelle, alors que cols A-E sont auto-remplies par FILTER. Si Soren change le statut d'une ligne au milieu du tableau `1. Contacts` (passage Contacté → Réponse), l'ordre des lignes filtrées peut décaler le mapping de la col F.
- Mitigation : ajouter les nouvelles entrées en bas, ne pas modifier l'ordre des lignes existantes. Sur un faible volume (<100 lignes / mois), pas un problème.
- Si ça devient un problème : déplacer la col Statut détaillé dans l'onglet `1. Contacts` (col G) et faire de l'onglet `2. En cours` une vue pure read-only.

## Fichiers liés
- Drive: https://docs.google.com/spreadsheets/d/1u9iSLIaWAZONf3YT5lqqkNDkL6_j5w_L/edit
- Ancien CRM (à archiver) : https://docs.google.com/spreadsheets/d/17A4wLby1U_DAZodtKJy1RlsPl4ubM1UG8NgSCA7rxFc/edit
