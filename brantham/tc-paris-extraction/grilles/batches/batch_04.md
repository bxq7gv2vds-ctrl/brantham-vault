---
type: batch_log
project: brantham
batch: 04
created: 2026-05-15
tags: [tc-paris, extraction, batch]
---

# Batch 04 — ILO (25) + YOGOSHA (56) + DES PLANCHES (NEW-52) + ARLO (NEW-59) + DIGITAL COLLEGE (NEW-61) + CPR (02) + CHEPOOKA (07) + PROGRESS SUP (13)

## Dossiers traités

| Dossier | Folder | Nb offres extraites | Confidence |
|---|---|---|---|
| 25 | SAS ILO (Groupe NEOCAMP) | 2 | high |
| 56 | SAS YOGOSHA | 2 | medium (Keyrus LOI) / high (Créative Invest) |
| NEW-PLANCHES | 52 - SARL DES PLANCHES | 2 | medium (PDFs scans OCR) |
| NEW-ARLO | 59 - SARL ARLO (La Bonne Place) | 2 | high (01) / medium (02 scan) |
| NEW-DIGITAL-COLLEGE | 61 - SAS DIGITAL COLLEGE | 2 | high |
| CPR | 02 - CLUB PALAIS ROYAL (EASYGYM) | 3 | high |
| 07 | SAS CHEPOOKA (Pavillon des Canaux) | 3 | high |
| 13 | SARL PROGRESS SUP (Progress Santé) | 3 | high (13-01) / medium (13-02, 13-03 doublons) |

**Total : 20 offres + 8 fiches dossier = 28 JSONs écrits.**

## Issues connues (gagnants-tribunal.md)

- **25 ILO (Groupe NEOCAMP)** : démantèlement accepté par tribunal. SEASONOVA gagnant Alpha Camping 15 sites (audience 02/04/2026) + MAEVA pour franchises Camping Paradis/Ushuaïa. SLBC PERON (25-01) et FEMINA STYL+MARENGO (25-02) écartés. ILO holding tracée comme partie du package.
- **NEW-61 DIGITAL COLLEGE** : en cours, audience probable mai-juin 2026. Deux offres asymétriques : IGS (École Conte uniquement, 10k) et Consortium UPSTAIRS+VOX POPULI (Digital College global, 5k - 10 CS - 1/56 emplois). Voir cas 3 gagnants-tribunal.
- **07 CHEPOOKA** : en cours, aucune source publique. 3 offres concurrentes très contrastées (154k OSD post-DLDO / 150k LEROY-DUMOUSSET / 30k MATHIEU).
- **13 PROGRESS SUP** : probablement en cours. Offre unique J.L 13 (BERREBI cousin dirigeant) - amélioration majeure 10k→100k / 3→44 emplois.

## Patterns détectés

1. **Pattern amélioration de prix CPR + 13** : même candidat dépose offre initiale plancher (50k CPR-03 / 10k 13-02-03) puis amélioration substantielle quelques semaines plus tard (105k CPR-01 / 100k 13-01). Stratégie connue d'optimisation pré-audience.
2. **Pattern art L.642-3 (lien familial)** : NEW-PLANCHES-02 (Kelly VANTHIER fille gérante) + 13-01 (Jean-Luc BERREBI cousin 2e degré). Nécessite autorisation Procureur - source de risque procédural majeur.
3. **Pattern dépôt hors délai** : 07-01 O'SULLIVANS (offre 23/01/2026 alors que DLDO 17/11/2025). Faiblesse procédurale majeure, accès data room sollicité a posteriori.
4. **Pattern asymétrie périmètre** : NEW-61 IGS offre 100% sur École Conte (filiale) plutôt que Digital College - "shopping" du périmètre rentable.
5. **Pattern offre indivisible multi-procédures** : 25-01 SLBC PERON (indivisible avec offres ALPHA CAMPING et 6 SCI) ; CPR-02 ALHIA GREEN (indivisible CGB+CPR) ; 13-01 J.L 13 (indivisible BAC COMMUNICATION). Risque que le tribunal rejette l'ensemble si un volet manque.

## Anomalies détectées

1. **CRD prêt Banque Populaire NEW-ARLO** : montant divergent entre offre 01 (116 490€) et offre 02 (121 051€). Probable mise à jour entre dates.
2. **Validité offre NEW-ARLO-01** : incohérence date - page 12 mentionne 10/10/2025 (date passée) vs page synthèse 18/05/2026.
3. **PDFs scans OCR NEW-PLANCHES** : données fines (RCS, capital, date ouverture, juge commissaire, DLDO) non lisibles. Confidence dégradée à "medium".
4. **Doublons 13-02 / 13-03** : contenu identique même date 19/11/2025 - second dépôt ou versions annexes différentes.
5. **NEW-DIGITAL-COLLEGE-01 IGS** : offre porte sur la filiale École Conte (SASU 100% à Nanterre RCS 399002807), pas sur Digital College en tant que tel. Incohérence de périmètre signalée dans signaux_faibles.
6. **56-01 KEYRUS** : LOI sans prix chiffré déposée à 7 jours de la DLDO. Intérêt déclaratif uniquement.

## Cas remarquable pour Phase 2

- **25 ILO** : démantèlement accepté tribunal en lots cohérents (Seasonova gestion directe + Maeva franchises). Confirmer pattern "découpage accepté" sur groupes multi-pôles cohérents.
- **NEW-61 Digital College** : test du tribunal face à offre périmètre maximaliste avec 10 CS et financement non bouclé (Consortium UPSTAIRS) vs offre cherry-picking restreinte (IGS École Conte). Précieux contre-exemple potentiel du pattern Minelli.
- **13 PROGRESS SUP** : pattern famille élargie (cousin 2e degré) + projet BP solide (CA an3 1,87M€, EBITDA an3 292k€) avec investissement e-learning IA. Bon proxy EdTech distressed.
- **07 CHEPOOKA** : tiers-lieu culturel + actif "convention domaine public" comme deal driver. Test du tribunal sur immatérialité + emplois.

## Suggestions Phase 2

- Coder explicitement le pattern "offre indivisible multi-procédures" : champ `indivisible_avec_autres_offres` et `risque_rejet_ensemble`.
- Recouper les améliorations de prix (deltas dans le temps) entre offre initiale et finale : signal de force/engagement candidat.
- Sur EdTech distressed (NEW-61 + 13) : tracer la valeur des marques + Qualiopi/RNCP comme actif déterminant.
- Pour les CHR (CPR, ARLO, CHEPOOKA, PLANCHES) : weighting fort sur `aucune_cs` + `pct_reprise` (patterns gagnants déjà identifiés bar-brasseries dans batch 22).

## Récap (<100 mots)

20 offres + 8 fiches dossier extraites batch 04 : ILO (2, Groupe NEOCAMP démantelé Seasonova+Maeva), YOGOSHA (2, Keyrus LOI vs Créative Invest 25k), DES PLANCHES (2, scans OCR - Mayeur vs Vanthier L.642-3), ARLO (2, Rivoli Capital 10k vs Aberrane 5k), DIGITAL COLLEGE (2, IGS École Conte vs Consortium UPSTAIRS 10 CS), CLUB PALAIS ROYAL (3, WS HOLDING amélioration 50→105k vs Alhia Green 70k), CHEPOOKA (3, O'Sullivans post-DLDO vs Negre Coste 150k vs Mathieu 30k), PROGRESS SUP (3, J.L 13 amélioration 10→100k cousin BERREBI). Patterns détectés : amélioration de prix, L.642-3, dépôt hors délai, cherry-picking périmètre, indivisibilité multi-procédures.

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_01]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_22]]
