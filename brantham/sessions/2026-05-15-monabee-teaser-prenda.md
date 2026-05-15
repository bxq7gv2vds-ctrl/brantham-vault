---
date: 2026-05-15
project: brantham
deal: monabee
type: session
tags: [brantham, deal, monabee, teaser, pre-nda, session]
---

# Session, montage du teaser pré-NDA MONABEE

Construction itérative d'un document de présentation pré-NDA pour la cible MONABEE (SIREN 788 614 006, plan de cession ouvert en avril 2026 par le TAE de Lyon, deadline offres 19 juin 2026 12h), destiné à un repreneur identifié non encore signataire d'un NDA. La conversation a couvert l'identification définitive de la cible, le premier draft de note d'opportunité, la conversion en PDF avec le template corporate Brantham, puis cinq passes d'enrichissement et de désanonymisation.

## Contexte de départ

Cible désanonymisée via méthode OSINT à partir de l'annonce Actify n° 14566 :
- Cross-check BODACC A202600743839 (parution 17/04/2026) + Pappers + SIRENE
- Match exhaustif sur 13 critères (activité, CA, effectif, AJ, géographie, contact)
- Identité confirmée : MONABEE SAS, siège 4 chemin des Hirondelles 69570 Dardilly
- AJ : SCP AJ Meynet & Associés (Me R. Meynet / Me T. Meynet / Me A. Boucaud), 128 rue Pierre Corneille 69003 Lyon
- MJ : SELARLU Martin (Me Pierre Martin), 20 bd Eugène Deruelle 69003 Lyon
- Contacts dossier : aurelie.plotton@etude-meynet.fr, camille.leprat@etude-meynet.fr

## Itérations de production

### Itération 1, note d'opportunité markdown

Première version `note-opportunite-repreneur.md` dans `vault/brantham/deals/active/monabee/`. Format note longue, résumé exécutif, fiche société, activité, marché, implantations, chiffres clés, procédure, sept angles d'intérêt, process Brantham. Comportait toutes les infos identifiantes (nom, SIREN, adresse, AJ nommés, deadline exacte).

Décision : créer en parallèle `_MOC.md` du deal et noter les repreneurs naturels à sourcer (Effy, mylight150, Cap Soleil, Otovo, Engie, EDF ENR, Hellio).

### Itération 2, alignement format Open Bee

User demande "doc comme Open Bee". Reformatage en `06-teaser-repreneur.md` calqué sur le format Open Bee France (tableau profil cible, atouts stratégiques en sept points, procédure, process Brantham, contact + mention NDA en pied).

### Itération 3, conversion PDF avec template corporate

User demande PDF. Création `MONABEE-teaser.html` utilisant `vault/_system/templates/rapport-corporate.css` (Computer Modern, A4, mise en page LaTeX-like). Génération via `weasyprint`. Document à six sections (Opportunité, Profil cible, Atouts stratégiques en sept sous-sections, Procédure, Process Brantham en quatre phases, Calendrier, Contact).

### Itération 4, anonymisation et reformatage profil cible

User : "ne donne pas le nom de l'AJ etc, on n'a pas signé encore", "pas trop de bullet points", profil cible mal mis. Trois changements :
- **Anonymisation** retirée : nom de société, SIREN, adresse, NAF, capital, noms des AJ et MJ, étude, référence dossier 14566, dates précises (BODACC, RJ, deadline). Localisation lissée à "région Auvergne-Rhône-Alpes" et "bassin lyonnais".
- **Profil cible** : grille KPI à 8 blocs avec bordure gauche (rendu jugé non satisfaisant).
- **Bullet points** : section Process Brantham passée en prose avec mots-clés en lead (Qualification, Cadrage, Dépôt, Suivi).

### Itération 5, retour à un tableau propre et retrait du calendrier

User : "j'aime pas la grille KPI". Retour à un tableau simple à 2 colonnes (style Open Bee). Suppression du calendrier détaillé qui donnait des ordres d'idée temporels susceptibles d'identifier la cible.

### Itération 6, repositionnement comme note d'introduction pré-NDA

User : "diffusion pré-NDA bien préciser que c'est un petit doc d'introduction de l'entreprise". Ajouts :
- Couverture sous-titre "Note d'introduction pré-NDA"
- Section "Avant-propos" en ouverture précisant : nature du document, ce qui est volontairement masqué (dénomination, organes, financier détaillé), ce qui se débloque post-NDA
- Mention de confidentialité en pied reformulée

User : "enlève la mention légale Brantham Partners SAS, SIREN 101 953 891". Retirée.

### Itération 7, enrichissement contexte sectoriel et leviers

User : "plus de tableaux, plus d'info sur les raisons probables du redressement". Trois ajouts majeurs :
- **Section 2 Contexte sectoriel** : 2.1 facteurs exogènes (7 lignes : taux d'intérêt, recalibrage aides, démarchage, surcapacité, défaillances en cascade, volatilité prix panneaux, cycle d'achat allongé), 2.2 facteurs spécifiques cible (paragraphe prudent), 2.3 signaux positifs de rebond (6 lignes : baisse taux, prix électricité, obligations tertiaire, stockage domestique, couplage VE+PAC, consolidation)
- **Section 3 Atouts stratégiques** : tableau synthèse 7 lignes en tête
- **Section 4 Leviers de redressement** : tableau 7 lignes (rationalisation commerciale, cross-sell base installée, pivot B2B, industrialisation pose, monétisation techno propriétaire, optimisation BFR, synergies industrielles)
- **Section 5 Périmètre cessible indicatif** : tableau 6 lignes (incorporels, corporels, contrats, implantations, certifications, backlog)

Angle vendeur : le retournement est présenté comme conjoncturel et sectoriel, pas comme une faille du modèle. Les signaux positifs suivent immédiatement les facteurs négatifs.

### Itération 8, synergies par profil et flexibilité du périmètre social

User : "mettre en avant les synergies et la reprise partielle du quota Salaires et charges sociales qui peut être retravaillé". Nouvelle **section 6, Flexibilité du périmètre et retraitement de la structure de coûts**.
- **6.1 Retraitement de la masse salariale** : tableau 7 lignes (salaires et charges sociales modulables, organigramme avec reprise sélective des fonctions opérationnelles, contrats fournisseurs, baux, stocks à juste valeur, **passif antérieur non repris**, cotisations sociales antérieures restant dans le passif cédant).
- **6.2 Synergies par profil de repreneur** : tableau 7 profils (installateur PV national, acteur stockage/VE, énergéticien intégré, industriel équipementier, constructeur, fonds/family office, acteur rénovation énergétique).

Conclusion 6.1 : "repartir avec une structure de coûts redimensionnée dès le jour un, alignée sur le volume d'activité cible des 18 à 24 premiers mois".

## État final du document

Fichier `vault/brantham/deals/active/monabee/MONABEE-teaser.pdf`, 49 Ko, 9 sections :

| Section | Contenu |
|---|---|
| Couverture | Note d'introduction pré-NDA, plan de cession ouvert |
| Avant-propos | Nature du document, ce qui est masqué, ce qui débloque post-NDA |
| Opportunité | 3 paragraphes d'accroche (marque connue, fenêtre courte) |
| 1. Profil cible | Tableau 8 indicateurs + tableau CA 3 exercices |
| 2. Contexte sectoriel | 2.1 facteurs exogènes, 2.2 spécifiques, 2.3 signaux positifs |
| 3. Atouts stratégiques | Tableau synthèse + 6 sections développées |
| 4. Leviers de redressement | Tableau 7 leviers |
| 5. Périmètre cessible | Tableau 6 catégories d'actifs et contrats |
| 6. Flexibilité périmètre | 6.1 retraitement masse salariale, 6.2 synergies par profil |
| 7. Procédure | Prose pré-NDA, redirige tout détail vers post-NDA |
| 8. Process Brantham | Qualification, cadrage, dépôt, suivi en prose |
| 9. Contact | Paul Roulleau, email, téléphone |

## Principes éditoriaux validés en cours de session

1. **Pré-NDA strict** : pas de dénomination, pas de SIREN, pas d'adresse, pas de NAF, pas de capital, pas de nom AJ/MJ, pas de référence dossier, pas de dates précises ouverture RJ ou deadline offres.
2. **Géo lissée** : "région Auvergne-Rhône-Alpes", "bassin lyonnais", "Nord-Isère", "Bretagne".
3. **CA arrondi au million** : "~ 12 M€" plutôt que "12 061 109 €".
4. **Effectif arrondi** : "environ 40" plutôt que "42 maintenus".
5. **Format à dominante tableau** plutôt que bullet points, sauf pour les paragraphes développés des atouts stratégiques.
6. **Angle vendeur préservé** : retournement présenté comme conjoncturel et sectoriel, signaux positifs systématiquement adossés aux facteurs négatifs, structure de coûts présentée comme "redimensionnable" plutôt que "trop lourde".
7. **Pas de calendrier détaillé** : aucun ordre d'idée temporel qui pourrait identifier la cible.
8. **Mention légale Brantham SAS retirée** du pied de page.

## Fichiers produits ou modifiés

| Fichier | Statut |
|---|---|
| `vault/brantham/deals/active/monabee/_MOC.md` | Créé |
| `vault/brantham/deals/active/monabee/note-opportunite-repreneur.md` | Créé (v0, conservé pour archive interne) |
| `vault/brantham/deals/active/monabee/06-teaser-repreneur.md` | Créé (markdown teaser format Open Bee) |
| `vault/brantham/deals/active/monabee/MONABEE-teaser.html` | Créé, 8 itérations |
| `vault/brantham/deals/active/monabee/MONABEE-teaser.pdf` | Généré, 49 Ko, 9 sections |

## Prochaines étapes proposées par Brantham

1. Identifier le repreneur prospect précis et calibrer la version finale du teaser pré-NDA (le doc actuel est générique, il peut être personnalisé selon le profil ciblé parmi les 7 profils du tableau 6.2).
2. Préparer un mail d'envoi court avec NDA en pièce jointe.
3. Sortir une fiche cible interne complète (non diffusée) à conserver côté Brantham pour cadrer la pré-due diligence.
4. Sortir la shortlist nominative des 6-8 repreneurs naturels avec contacts dirigeants (Effy, mylight150, Cap Soleil Énergie, Otovo, Engie filiale solaire, EDF ENR, Hellio, plus 2-3 intégrateurs régionaux).
5. Pré-cadrer la déclinaison post-NDA du document (mémorandum d'information complet, sur lequel s'appuyer pour l'accompagnement du repreneur jusqu'au dépôt d'offre).

## Décisions techniques

- Template corporate Brantham via `vault/_system/templates/rapport-corporate.css` validé pour ce type de teaser pré-NDA. Le même CSS sert pour les rapports longs (ex. ITFI 13 sections) et les notes courtes (MONABEE 9 sections).
- Workflow `weasyprint` confirmé comme production PDF standard, `pdflatex` absent du poste de travail.
- Convention d'anonymisation pré-NDA établie pour Brantham : pas d'identifiants, géo lissée à la région et au bassin, chiffres arrondis, organes de procédure cités comme "étude régionale de référence".

## Related

- [[brantham/deals/active/monabee/_MOC]]
- [[brantham/deals/active/monabee/06-teaser-repreneur]]
- [[brantham/deals/active/monabee/note-opportunite-repreneur]]
- [[brantham/_MOC]]
- [[_system/MOC-deals]]
- [[_system/MOC-patterns]]
- [[brantham/patterns/teaser-patterns]]
- [[brantham/patterns/onboarding-distressed-ma]]
- [[brantham/deals/active/open-bee-france/_MOC]]
- [[brantham/deals/active/itfi-groupe/_MOC]]
- [[_system/templates/rapport-corporate]]
