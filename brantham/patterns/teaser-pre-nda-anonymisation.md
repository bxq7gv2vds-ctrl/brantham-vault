---
type: pattern
project: brantham
date: 2026-05-15
tags: [brantham, pattern, teaser, pre-nda, anonymisation, deal]
---

# Pattern, teaser pré-NDA et règles d'anonymisation

Convention de production des notes d'introduction destinées à un repreneur prospect non encore signataire d'un NDA. Issue de la session MONABEE du 15 mai 2026, après huit itérations user.

## Règle générale

Le teaser pré-NDA est un document court (4 à 8 pages PDF, A4) dont la fonction est de **séduire un prospect identifié sans permettre l'identification de la cible**. Toute information complémentaire est explicitement renvoyée à la signature d'un engagement de confidentialité bilatéral avec l'étude.

## Ce qui ne doit jamais apparaître dans un teaser pré-NDA

| Catégorie | Exemples interdits |
|---|---|
| Identité juridique | Dénomination sociale, SIREN, RCS, NAF, capital social, marque commerciale |
| Localisation | Adresse précise, code postal, commune exacte |
| Organes de la procédure | Nom des AJ et MJ, nom de l'étude, adresse de l'étude, référence dossier |
| Dates précises | Jugement RJ, BODACC, deadline offres, audience d'examen |
| Identifiants financiers | CA exact au centime, résultat net, effectif exact, capital exact |
| Sites secondaires | Adresses précises des dépôts ou antennes |
| Dirigeants | Noms du président, du DG, des actionnaires |
| Site web | Lien direct vers le site officiel |

## Ce qui doit apparaître dans un teaser pré-NDA

- Activité décrite par nature (pas par nom commercial)
- Géographie lissée à la région ou au bassin
- Ancienneté arrondie (plus de 13 ans, plus d'une décennie)
- CA arrondi au million sur 3 exercices
- Effectif arrondi à la dizaine
- Atouts stratégiques en tableau et sections développées
- Contexte sectoriel expliquant le retournement
- Leviers de redressement pour le repreneur
- Synergies par profil de repreneur
- Flexibilité du périmètre social (point clé du plan de cession)
- Périmètre cessible indicatif
- Process Brantham
- Contact Brantham (Paul Roulleau)

## Anatomie standardisée

Neuf sections, dans cet ordre :

1. **Avant-propos** : nature du document, ce qui est masqué, ce qui débloque post-NDA
2. **Opportunité** : 3 paragraphes d'accroche
3. **Profil cible** : tableau d'indicateurs + tableau CA arrondi
4. **Contexte sectoriel** : facteurs exogènes + spécificités cible (prudent) + signaux positifs de rebond
5. **Atouts stratégiques** : tableau synthèse + sections développées
6. **Leviers de redressement** : tableau orienté thèse de reprise
7. **Périmètre cessible indicatif** : tableau des catégories d'actifs et contrats
8. **Flexibilité du périmètre et retraitement de la structure de coûts** : retraitement de la masse salariale (point différenciant du plan de cession vs share deal) + synergies par profil de repreneur
9. **Procédure** : prose pré-NDA qui redirige tout détail vers post-NDA
10. **Process Brantham** : qualification, cadrage, dépôt, suivi
11. **Contact** : Paul Roulleau, email, téléphone

## Angle vendeur à préserver

1. **Retournement présenté comme conjoncturel et sectoriel**, jamais comme une faille intrinsèque du modèle de la cible.
2. **Signaux positifs de rebond adossés systématiquement** aux facteurs négatifs (jamais un tableau de difficultés sans pendant positif).
3. **Structure de coûts présentée comme "redimensionnable"** plutôt que "trop lourde". Le plan de cession est un atout, pas une contrainte.
4. **Base installée et techno propriétaire** sont les deux actifs immédiatement activables systématiquement mis en avant si la cible en dispose.
5. **Synergies par profil** : permet au prospect de se projeter immédiatement dans sa propre thèse.
6. **Pas de chiffres négatifs en relief** : pas de résultat net, pas de pertes cumulées, pas de mention explicite du déficit.

## Stack technique

- Source : un fichier `<DEAL>-teaser.html` dans `vault/brantham/deals/active/<deal>/`
- Template CSS : `vault/_system/templates/rapport-corporate.css` (Computer Modern, A4, marges 2.5 cm / 3 cm)
- Production PDF : `weasyprint <DEAL>-teaser.html <DEAL>-teaser.pdf`
- Taille cible : 4 à 8 pages, 30 à 50 Ko

## Référence

- Cas d'école : [[brantham/deals/active/monabee/_MOC]] (session 2026-05-15)
- Pattern source format teaser : [[teaser-patterns]] (format Open Bee France)
- Méthode OSINT d'identification : [[osint-deanon-cession-anonyme]]
- Onboarding repreneur : [[onboarding-distressed-ma]]

## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[brantham/deals/active/monabee/_MOC]]
- [[brantham/patterns/teaser-patterns]]
- [[brantham/patterns/onboarding-distressed-ma]]
- [[brantham/patterns/teaser-onepager-html-pdf]]
- [[brantham/sessions/2026-05-15-monabee-teaser-prenda]]
- [[_system/templates/rapport-corporate]]
