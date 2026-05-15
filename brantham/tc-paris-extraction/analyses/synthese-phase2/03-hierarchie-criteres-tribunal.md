---
type: analyse
project: brantham
phase: phase2
livrable: 03
created: 2026-05-15
tags: [tc-paris, motifs, l642-5, jurisprudence, criteres]
---

# 03 — Hiérarchie des critères mobilisés par le tribunal

Méthodologie : extraction des champs `motifs_tribunal_verbatim` et `motifs_rejet_verbatim` sur les 154 offres décidées, puis thématisation manuelle + verbatim direct. n=20 motifs « positifs » exploitables (côté winners) + n=96 motifs de rejet (côté losers). On distingue ce que la **loi L.642-5 impose** (prix, emploi, pérennité) de ce qui FAIT BASCULER en pratique.

## 1. La loi L.642-5 du Code de commerce

> « Le tribunal retient l'offre qui permet dans les meilleures conditions d'assurer le plus durablement l'emploi attaché à l'ensemble cédé, le paiement des créanciers, et qui présente les meilleures garanties d'exécution. »

Triade officielle : **emploi durable** + **paiement créanciers** + **garanties d'exécution**.

Dans la pratique observée à Paris (TAE Paris depuis sept. 2024), le motif officiel est rarement explicité dans la décision orale. On le reconstruit à partir de :
- communiqués de presse (cas EURODIF, INNATIS, Alpha Camping, Denteka)
- analyses tierces (`gagnants-tribunal.md`)
- contenu des offres améliorées (qui montre ce qu'a demandé le tribunal lors de l'audience).

## 2. Hiérarchie observée — thèmes positifs (winners)

Sur 20 motifs tribunal verbatim côté winners :

| Rang | Thème | n occurrences | % |
|---|---|---|---|
| 1 | **Pérennité / continuité de l'activité** | 9 | 45 % |
| 2 | **Expérience sectorielle du repreneur** | 3 | 15 % |
| 3 | Crédibilité financière | 1 | 5 % |

Le thème dominant n'est PAS le prix le plus haut, mais la pérennité — souvent formulée comme « projet coopératif local cohérent », « continuité filière », « expertise sectorielle », « ancrage territorial ».

## 3. Verbatims tribunal — winners (citation directe)

### Pérennité / projet cohérent

> « Projet coopératif local cohérent ; continuité filière fruits ; ancrage Val de Loire ; capacité financière démontrée 26M€ CP ; rapport qualité-prix supérieur (75k€ vs 40k€ consortium). »
> — Dossier 37-COOP (CAVL), retenue Vergers d'Anjou

> « Projet coopératif local cohérent ; capacité de stockage Les Vergers d'Anjou passe de 36 000 t à 49 000 t. »
> — Dossier 34-LPC (LPC), retenue Vergers d'Anjou

> « Projet coopératif local cohérent ; continuité sectorielle ; capacité de stockage Vergers d'Anjou passe de 36 000 t à 49 000 t ; voisinage immédiat <5km station Océane ; financement comptant garanti CRCAM + CIC ; 200k€ accompagnement social volontaire ; faculté de substitution CELHER pour SCEA agricoles cohérente. »
> — Dossier 36-LVL (LVL POMANJOU), retenue Vergers d'Anjou via CELHER

> « Continuité activité santé visuelle mobile, expertise sectorielle du repreneur, gouvernances Sym/LOM restent indépendantes. »
> — Dossier 20 (SYM TECH) — Sym repris par Les Opticiens Mobiles

### Expérience / track record sectoriel

> « Repreneur sectoriel stratégique avec continuité emploi. »
> — Dossier 28B-ALPHA (Seasonova retient 15 sites camping)

> « Monsieur et Madame BOUJUAU sont exploitants agricoles depuis 1998 et disposent donc d'une solide expérience en matière de conduite et de gestion d'une entreprise agricole. »
> — Dossier 57 (SCA DE LA PLESSE), retenue CELHER

### Démantèlement par lots cohérents

> « Démantèlement par lots cohérents par sous-activité accepté : Seasonova gestion directe + Maeva franchises Camping Paradis/Ushuaia/Mistercamp. »
> — Dossier 28B-ALPHA, audience 02/04/2026

### Périmètre maximum (cas EURODIF / Bouchara)

> « Plan de cession arrêté au profit d'AA Investments HK — périmètre maximum 25 baux / 185 emplois CDI + mécanisme stock du Havre co-construit avec la procédure. »
> — Dossier 50 (EURODIF SAS), retenue AA Investments HK

## 4. Hiérarchie observée — thèmes de rejet (losers)

96 motifs de rejet extraits. Classement thématique par fréquence :

| Rang | Thème de rejet | n occurrences (approx, comptage manuel + regex) | % |
|---|---|---|---|
| 1 | **Périmètre marginal vs offre concurrente plus large** | 17 | 18 % |
| 2 | **Indivisibilité / offre château de cartes** | 14 | 15 % |
| 3 | **Prix symbolique / dérisoire (1€, 2€, 3€)** | 14 | 15 % |
| 4 | **Doublon physique / duplicata** | 12 | 13 % |
| 5 | **Conditions suspensives lourdes (>5)** | 11 | 11 % |
| 6 | **Améliorée puis rejetée au profit d'autre** | 10 | 10 % |
| 7 | **PDF mal classé (hors périmètre)** | 9 | 9 % |
| 8 | **Lettre d'intention seule, pas offre ferme** | 6 | 6 % |
| 9 | **Conflit d'intérêt (ex-salarié, dirigeant historique)** | 5 | 5 % |
| 10 | **Cherry-picking d'actifs isolés** | 5 | 5 % |
| 11 | **Financement non documenté** | 4 | 4 % |
| 12 | **Charges augmentatives masquées** | 3 | 3 % |
| 13 | **Repreneur trop petit / capacité douteuse** | 3 | 3 % |
| 14 | **Erreurs apparentes (mauvais nom de ville, etc.)** | 2 | 2 % |
| 15 | **Vente d'actifs isolés (L.642-7-II) — pas plan cession** | 2 | 2 % |

Les motifs 1-3 cumulent 50 % des rejets explicites. C'est la **mécanique d'éviction par comparaison** : ton offre est plus marginale (moins d'emplois, moins de sites, moins de filière), donc tu sors.

## 5. Verbatims tribunal — rejets emblématiques

### Périmètre marginal

> « Périmètre limité à 11-13 magasins / 60 emplois vs AA Investments 25 magasins / 185 emplois (source presse + décortique). »
> — Dossier 50 (EURODIF), rejet offre concurrente

> « Offre limitée 1 site. Tribunal a privilégié offres consolidées (Seasonova multi-sites). »
> — Dossier 28B-ALPHA, rejet HUTTOPIA

> « Périmètre marginal : 2 magasins / 20 emplois vs AA Investments 25 mag / 185 emplois. »
> — Dossier 50 (EURODIF), rejet PP non documentée

### Indivisibilité « château de cartes »

> « Indivisibilité 11 offres Innatis (château de cartes) ; volet social très faible (1/2) ; conflit d'intérêts James LAUNAY ; prix dérisoire 40k€ pour coopérative avec CA 6,2M€. »
> — Dossier 37-COOP (CAVL), rejet consortium CASTEL+LEROY+VCAPITAL

> « Indivisibilité avec 10 autres offres (château de cartes) ; ventilation prix renvoyée à "ultérieurement" ; financement précisé "ultérieurement" ; conflit d'intérêts James LAUNAY ex-salarié LVL POMANJOU ; engagement social en pointillés. »
> — Dossier 36-LVL, rejet consortium

### Prix symbolique critiqué

> « Offre la plus basse 1 000 EUR. Société SHD recemment immatriculée (RCS Dijon 928117449). Erreur dans objet PDF : mention 'Narbonne' alors que bien est à Lamonzie-Montastruc (Dordogne). »
> — Dossier 27B-GD-LISSE

> « Prix dérisoire 40k€ pour coopérative avec CA 6,2M€. »
> — Dossier 37-COOP, rejet consortium

### Conditions suspensives jugées non fermes

> « Conditions suspensives nombreuses (DD, accords DSP, comité stratégique) — moins ferme face à Seasonova. »
> — Dossier 28B-ALPHA, rejet concurrent

### Conflit d'intérêts / dirigeant historique

> « Conflit d'intérêts James LAUNAY ex-salarié LVL POMANJOU »
> — Dossiers 36-LVL, 37-COOP, 60 — rejet récurrent du consortium CASTEL+LEROY+VCAPITAL

### Clause non-sollicitation imposée aux dirigeants

> « Demandes exorbitantes au tribunal : clause non-sollicitation clientèle 24 mois imposée aux 4 anciens dirigeants. Discrédite l'équipe sortante. »
> — Dossier 34 (COSA VOSTRA), rejet DATASOLUTION (50 k€)

### Charges augmentatives masquées

> « Charges augmentatives masquées (745k€ BFR/encours non facturés) non payées à la procédure. »
> — Dossier 34, rejet DATASOLUTION

### Repreneur sous-dimensionné

> « Repreneur trop petit (groupe PH7 4,5M€ CA, 35 collab) face à activité COSA VOSTRA (~7M€ CA). Prix faible 3k€. SAS à constituer cap 1000€. »
> — Dossier 34, rejet candidat alternatif

### Cherry-picking actifs

> « Cherry-picking e-commerce uniquement (hors bail, hors Tunisie, hors UK). 4 emplois CDI / 29. Actionnaire minoritaire 34% en position de conflit potentiel. »
> — Dossier 34

### LOI seule (pas d'offre ferme)

> « Simple LOI 1€ symbolique. Offre complète promise sous 1 semaine mais jamais formalisée. »
> — Dossier 34 (COSA VOSTRA), rejet candidat suisse

### Erreurs apparentes

> « Mention 'Narbonne' alors que bien est à Lamonzie-Montastruc (Dordogne). »
> — Dossier 27B-GD-LISSE

## 6. Trois familles de motifs — synthèse opérationnelle

### Famille A — Loi L.642-5 stricte (rare en verbatim direct)

Quand le tribunal cite directement la triade emploi/prix/garanties. Observé en clair sur 2-3 dossiers seulement (Denteka, Sym, EURODIF). Formulation typique :

> « Repreneur sectoriel stratégique avec continuité emploi. »

### Famille B — Pratique courante (« best of available »)

Le tribunal compare les offres reçues et retient la **meilleure parmi celles disponibles**. La justification est implicite mais reconstructible : « ton offre est moins large, moins ferme, moins prête que celle de X — donc rejetée ». 70 % des motifs de rejet relèvent de cette catégorie.

### Famille C — Disqualification technique

Doublons physiques, PDF mal classés, LOI sans offre ferme, erreurs grossières. Ces offres ne sont pas comparées sur le fond — elles sortent du jeu. 25-30 % des rejets explicites.

## 7. Recommandation pour Brantham — ce qu'il faut faire signer au tribunal

Une offre Brantham bien construite doit déclencher dans la décision écrite (ou les communiqués) au moins **un des trois marqueurs winning** :

1. « Projet [cohérent / industriel / coopératif / territorial] »
2. « Expérience sectorielle [démontrée / longue / pertinente] »
3. « Capacité financière [démontrée / garantie / ferme] »

Et **éviter absolument** les marqueurs perdants :

1. Périmètre plus petit que l'offre concurrente connue
2. Plus de 3 conditions suspensives
3. Indivisibilité avec d'autres offres
4. Prix symbolique non justifié par L.642-12 al.4
5. Tout ce qui suggère « impréparation » (ventilation prix « ultérieurement »)
6. Conflit d'intérêt même apparent
7. Clause hostile envers les anciens dirigeants

## 8. Limites de cette hiérarchie

- Seulement **20 motifs tribunal explicites** côté winners (les jugements de cession ne sont presque jamais motivés en clair sur l'attribution — le tribunal acte). Les motifs reconstitués viennent souvent de communiqués de presse / sources externes (`gagnants-tribunal.md` cite Les Echos, L'Officiel des Terrains de Camping, Réussir Fruits & Légumes).
- Les **96 motifs de rejet** sont eux aussi reconstruits à partir d'observations factuelles de l'offre (prix, périmètre, doublon) plutôt que d'attendus explicites. La pondération %fréquence est qualitative.
- Le corpus est **TAE Paris** uniquement (sept. 2024 — avr. 2026, période où le TAE expérimente sa nouvelle compétence sur procédures collectives). Non généralisable mécaniquement à d'autres ressorts.

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/02-anatomie-winners-vs-losers]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/06-pieges-recurrents-rejetees]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/08-grille-scoring-100pts]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/_index]]
