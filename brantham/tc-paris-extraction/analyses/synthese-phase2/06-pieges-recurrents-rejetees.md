---
type: analyse
project: brantham
phase: phase2
livrable: 06
created: 2026-05-15
tags: [tc-paris, pieges, rejets, anti-patterns, kill-switch]
---

# 06 — Pièges récurrents : pourquoi 107 offres ont été rejetées

Analyse des **96 motifs de rejet renseignés** + cas iconique MINELLI (6 offres, 0 retenue → liquidation). Classement par récurrence et impact.

## 1. Top 15 défauts récurrents

| Rang | Défaut | n cas | Fond / Forme | Coût observé |
|---|---|---|---|---|
| 1 | Périmètre marginal vs concurrent plus large | 17 | Fond | Rejet quasi-automatique |
| 2 | Indivisibilité « château de cartes » | 14 | Fond | Rejet en groupe |
| 3 | Prix symbolique non justifié (1-3 €) | 14 | Fond | Rejet sauf cas L.642-12 al.4 |
| 4 | Doublon physique / duplicata | 12 | Forme | Comptée comme une seule offre |
| 5 | Conditions suspensives lourdes (>5) | 11 | Fond | Affaiblit la fermeté de l'offre |
| 6 | Améliorée puis rejetée au profit d'autre | 10 | Fond | L'amélioration ne suffit pas si périmètre marginal |
| 7 | PDF mal classé (hors périmètre) | 9 | Forme | Disqualification immédiate |
| 8 | Lettre d'intention seule, pas offre ferme | 6 | Forme | Hors-jeu |
| 9 | Conflit d'intérêt (ex-salarié, dirigeant historique) | 5 | Fond | Rejet sec |
| 10 | Cherry-picking d'actifs | 5 | Fond | Rejet si offre globale concurrente |
| 11 | Financement non documenté | 4 | Fond | Doute sur perennité |
| 12 | Charges augmentatives masquées | 3 | Fond | Tribunal recalcule et rejette |
| 13 | Repreneur sous-dimensionné | 3 | Fond | Pas la capacité |
| 14 | Erreurs apparentes (mauvais nom, dates) | 2 | Forme | Signal d'impréparation |
| 15 | Vente actifs isolés L.642-7-II vs plan cession | 2 | Fond | Procédure différente |

Cumul Fond : 88 cas (84 %). Cumul Forme : 23 cas (22 %). **Les défauts de fond dominent**, mais les défauts de forme suffisent à eux seuls pour disqualifier.

## 2. Défauts de fond — décortique

### 2.1 Périmètre marginal (n=17)

Le défaut #1. Le tribunal préfère systématiquement l'offre la plus large quand les autres dimensions (prix, emplois, financement) sont comparables.

Verbatim :
> « Périmètre 18 mag pour 80k EUR + CS multiples (accord bailleurs, audit marque) vs AA Investments sans CS, 25 mag, 185 emplois »
> — Dossier 50 (EURODIF)

> « Offre limitée 1 site. Tribunal a privilégié offres consolidées (Seasonova multi-sites). »
> — Dossier 28B-ALPHA

> « Périmètre marginal : 2 magasins / 20 emplois vs AA Investments 25 mag / 185 emplois »
> — Dossier 50

**Anti-pattern** : déposer une offre sur 1-3 magasins quand on sait qu'un concurrent dépose sur 20+.

**Remède Brantham** : avant de déposer, demander à l'AJ une indication des fourchettes connues (« sans révéler les autres, est-ce que mon périmètre est dans le bas / la moyenne / le haut ? »). Si bas → renoncer ou élargir.

### 2.2 Indivisibilité « château de cartes » (n=14)

Quand on dépose une offre couvrant plusieurs entités d'un groupe avec clause d'indivisibilité (« mes 11 offres doivent toutes être retenues ou aucune »), le tribunal préfère démanteler.

Verbatim :
> « Indivisibilité 11 offres Innatis (château de cartes) ; volet social très faible (1/2) ; conflit d'intérêts James LAUNAY ; prix dérisoire 40k€ pour coopérative avec CA 6,2M€. »
> — Dossier 37-COOP, rejet consortium CASTEL+LEROY+VCAPITAL

> « Indivisibilité avec 10 autres offres (château de cartes) ; ventilation prix renvoyée à 'ultérieurement' »
> — Dossier 36-LVL

> « Démantèlement accepté par tribunal en lots cohérents : Seasonova retient gestion directe Alpha (15 sites), Maeva les franchises. »
> — Dossier 31-OCCITANIE

**Anti-pattern** : offre indivisible sur >5 entités.

**Remède Brantham** : déposer des offres autonomes par entité, avec clause de « bonification de prix si l'ensemble est retenu » — ou faire confiance au démantèlement.

### 2.3 Prix symbolique non justifié (n=14)

1-3 € est acceptable QUAND le repreneur reprend des engagements bancaires lourds L.642-12 al.4 et donc « paye le prix » par la reprise du nantissement. Sinon, le tribunal le lit comme un manque de sérieux ou de capacité.

Verbatim :
> « Prix symbolique 3€ - offre indivisible avec autres NEOCAMP »
> — Dossier 26 (SCI C.H.A.)

> « Prix dérisoire 40 k€ pour coopérative avec CA 6,2M€. »
> — Dossier 37-COOP

**Cas où le prix symbolique fonctionne** : Seasonova / Alpha Camping 2 €/site (n=2 retenues). Justification : la reprise des emprunts bancaires (~270 k€ BNP+CA) + reprise 100 % du personnel + plan de redressement industriel chiffré + groupe sectoriel solide.

**Anti-pattern** : prix symbolique + offre seule (PP) + cherry-picking.

### 2.4 Conditions suspensives lourdes (n=11)

Médiane CS chez rejetées = 4 ; chez retenues = 1. Au-delà de 5 CS, l'offre est jugée non ferme.

Verbatim :
> « Conditions suspensives nombreuses (DD, accords DSP, comité stratégique) — moins ferme face à Seasonova. »
> — Dossier 28B-ALPHA

> « Conditions suspensives lourdes (11 items), prix 10k€ insignifiant pour les actifs visés. »
> — Dossier 59 (SCEA LA REINETTE D'ANJOU)

**Anti-pattern** : empiler les CS pour se protéger sans réaliser que chacune affaiblit la fermeté perçue.

**Remède Brantham** : maximum 2 CS, jamais sur le financement (sinon le tribunal lit « offre non finançée »).

### 2.5 Conflit d'intérêt (n=5)

L'ex-salarié, le dirigeant historique, le proche parent peuvent être disqualifiés s'ils ne signent pas la déclaration L.642-3 ou si le tribunal détecte un lien.

Verbatim :
> « Conflit d'intérêts James LAUNAY ex-salarié LVL POMANJOU »
> — Récurrent dossiers 36, 37, 59, 60

> « Actionnaire minoritaire 34 % en position de conflit potentiel. »
> — Dossier 34 (COSA VOSTRA)

**Cas exception** : PROGRESS SUP / Jean-Luc BERREBI (cousin 2e degré du dirigeant historique) gagne **parce qu'il déclare le lien explicitement** (« Le bénéficiaire effectif ultime est Monsieur Jean-Luc BERREBI, qui est par ailleurs le cousin au deuxième degré de Monsieur Didier SITBON ») et fournit la déclaration L.642-3.

**Remède Brantham** : si lien existe, **le déclarer en première page** + L.642-3 signée + démontrer l'indépendance économique.

### 2.6 Cherry-picking actifs (n=5)

Reprendre uniquement le e-commerce, ou uniquement le bail, ou uniquement la marque — sans le périmètre humain et industriel.

Verbatim :
> « Cherry-picking e-commerce uniquement (hors bail, hors Tunisie, hors UK). 4 emplois CDI / 29 »
> — Dossier 34 (COSA VOSTRA)

> « Offre partielle droit au bail isolé, 0 emploi - non intégrée au plan de cession AA Investments »
> — Dossier 50 (EURODIF)

> « Offre partielle marque BOUCHARA Collection seule. IDGIFT (filiale BEN'S) déjà licenciée exclusive depuis 16/05/2012. »
> — Dossier 50

**Anti-pattern** : actifs sans reprise humaine — disqualifiant en RJ (vs simple cession d'actifs hors procédure).

### 2.7 Financement non documenté (n=4)

Le repreneur annonce un montant sans prouver qu'il peut l'apporter.

Verbatim :
> « Offre PP non documentée financièrement (3M EUR crédit court terme demandés mais pas d'engagement bancaire), CS sur financement »
> — Dossier 50

> « Business plan en cours d'élaboration, liste salariés en cours, prévisionnel en cours = 3 occurrences 'ultérieurement / en cours' = signal d'impréparation vs AA Investments offre prête »
> — Dossier 50

**Anti-pattern** : « les caractéristiques NewCo seront communiquées ultérieurement », « le prévisionnel est en cours d'élaboration », « la liste des salariés repris sera précisée ».

**Remède Brantham** : tout fournir dans l'offre v1. Une amélioration v2 (« amelioree_puis_retenue ») n'est valable que pour ajuster prix ou périmètre — pas pour combler des trous.

### 2.8 Charges augmentatives masquées (n=3)

Verbatim :
> « Charges augmentatives masquées (745k€ BFR/encours non facturés) non payées à la procédure. Demandes exorbitantes au tribunal. »
> — Dossier 34 (COSA VOSTRA), rejet DATASOLUTION

**Anti-pattern** : annoncer un prix « bas » qui devient mécaniquement « élevé » une fois recalculé par l'AJ.

**Remède Brantham** : ventilation transparente, charges augmentatives listées séparément.

### 2.9 Repreneur sous-dimensionné (n=3)

Verbatim :
> « Repreneur trop petit (groupe PH7 4,5M€ CA, 35 collab) face à activité COSA VOSTRA (~7M€ CA). Prix faible 3k€. SAS à constituer cap 1000€. »
> — Dossier 34

**Anti-pattern** : ratio CA repreneur / CA cible < 0,5 + prix dérisoire + capital faible.

**Remède Brantham** : si repreneur sous-dimensionné, montrer une réserve de financement (lettre confort actionnaire, fonds garanti) ou une **substitution vers entité plus large**.

## 3. Défauts de forme — checklist anti-erreurs

### 3.1 Doublons physiques (n=12)

Verbatim :
> « DUPLICATA exact de 50-09 — même Docusign Envelope ID 55BB1506. À traiter comme une seule offre. »
> — Dossier 50

> « DUPLICATA exact de 35-SICA-03 (même 47 pages, même Docusign envelope C87386DC-A7F1-4900-AE69-3A96FD153DA2, même date 18/03/2026 11:33 CET) »
> — Dossier 35-SICA-04

Doublons fréquents = même PDF déposé 2 fois (parfois par erreur AJ, parfois par re-dépôt repreneur après remarque).

### 3.2 PDF mal classé (n=9)

Phénomène spécifique aux portefeuilles immobiliers (FHBX 26 SCI) : l'offre HOUSEBASE ciblant la SNC ADONIA est déposée dans 7 autres dossiers SCI. Chaque dépôt erroné est rejeté.

> « PDF mal classé — cette offre cible la SNC ADONIA (30 rue Étienne Dolet Cachan 94230, 501.600€), pas la présente entité. »

**Remède Brantham** : check binaire avant dépôt : « le n° RG et la raison sociale dans l'offre correspondent-ils au dossier cible ? ».

### 3.3 Erreurs apparentes (n=2 majeures)

Verbatim :
> « Erreur dans objet PDF : mention 'Narbonne' alors que bien est à Lamonzie-Montastruc (Dordogne). »
> — Dossier 27B-GD-LISSE

**Signal d'impréparation** = le tribunal anticipe d'autres défauts cachés. Une erreur visible suffit à descendre l'offre dans la pile.

## 4. Cas iconique — MINELLI (6 offres, 0 retenue → liquidation)

Source : `gagnants-tribunal.md`. Le dossier MINELLI est emblématique du **capot du marché** : aucune offre n'est jugée suffisante.

Caractéristiques du dossier :
- Maroquinerie de luxe, retail multi-sites.
- 6 offres déposées, toutes rejetées au motif de **périmètre trop étroit** vs maintien de la marque.
- Issue : **liquidation judiciaire** prononcée — la marque a fini par disparaître commercialement (ou être absorbée hors procédure).

Leçon pour Brantham :
- Quand un dossier est en LJ après échec du plan de cession, c'est souvent parce que **personne n'a proposé un périmètre cohérent**.
- Il y a une opportunité de positionner une offre Brantham « unique candidat large » dans les dossiers où les 6-10 premières offres sont marginales — mais il faut **financer 100 % du périmètre**.

## 5. Erreurs constatées dans les offres (champ `erreurs_apparentes`)

L'extraction a tracé un champ `erreurs_apparentes` (liste d'erreurs détectées). Médiane = 1 erreur par offre (retenues comme rejetées). Top erreurs observées dans les rejetées :

- Sections vides « seront communiquées ultérieurement » (très fréquent : COSA, EURODIF v1, CAVL v1, LVL v1)
- Noms de villes ou raisons sociales incorrects (Narbonne au lieu de Lamonzie)
- Capital social NewCo non précisé
- Date d'entrée en jouissance non datée
- Faculté de substitution mentionnée mais sans nominée
- Prix mentionné en chiffres ≠ prix mentionné en lettres
- Section dupliquée dans sommaire (cas 01-01)

## 6. Pattern « offre améliorée » — ne pas s'y tromper

42 offres sont notées `amelioree_puis_retenue`. Lecture : le repreneur a déposé v1, audience tenue, tribunal a invité à améliorer, v2 déposée et retenue.

**Mais** : 10 offres sont aussi notées `amelioree_puis_retenue` côté winners alors que c'est en réalité une autre offre du même dossier qui a gagné. Ex. CASTEL+LEROY+VCAPITAL a amélioré 34-LPC, mais c'est Vergers d'Anjou qui a gagné.

**L'amélioration ne sauve pas une offre fondamentalement périmètre-marginale.** Elle ne sauve pas non plus une offre indivisible. Elle sauve principalement :
- Une offre déjà bien construite mais avec **prix légèrement bas**
- Une offre v1 avec **CS levable**
- Une offre v1 avec un **détail oublié** (ex. ventilation incorporels)

## 7. Top 5 kill-switches absolus

Si une de ces erreurs est présente, l'offre est statistiquement quasi-condamnée :

1. **Périmètre marginal vs concurrent connu** (n=17 cas, 0 retenue avec ce défaut)
2. **Indivisibilité « château de cartes »** (n=14 cas, 0 retenue)
3. **Clause non-sollicitation hostile envers dirigeants sortants** (n=2-3 cas, 0 retenue)
4. **Charges augmentatives masquées** (n=3, 0 retenue)
5. **« Caractéristiques NewCo / BP / liste salariés communiquées ultérieurement »** (récurrent, 0 retenue)

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/02-anatomie-winners-vs-losers]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/03-hierarchie-criteres-tribunal]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/08-grille-scoring-100pts]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/_index]]
