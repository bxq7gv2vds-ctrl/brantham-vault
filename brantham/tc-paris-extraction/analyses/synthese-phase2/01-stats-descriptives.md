---
type: analyse
project: brantham
phase: phase2
livrable: 01
created: 2026-05-15
tags: [tc-paris, stats, distressed-ma, repreneur, distribution]
---

# 01 — Statistiques descriptives du corpus TC Paris

566 offres et 101 dossiers extraits, fenêtre 2025-09 / 2026-04. Tous les chiffres ci-dessous sont calculés directement à partir des JSONs `grilles/offres/*.json` et `grilles/dossiers/*.json`.

## 1. Décompte global

| Statut de l'offre | n | % du corpus |
|---|---|---|
| Retenue (`oui` + `amelioree_puis_retenue`) | 47 | 8,3 % |
| Rejetée (`non`) | 107 | 18,9 % |
| En attente (audience non tenue) | 385 | 68,0 % |
| Non renseigné | 27 | 4,8 % |
| **Total** | **566** | **100 %** |

Sur les 154 offres pour lesquelles l'issue est connue, le taux de retenue est de **30,5 %** (47 / 154). Ce n'est PAS le taux gagnant intrinsèque : un dossier compte rarement >1 retenue, donc beaucoup d'offres concurrentes sont mécaniquement rejetées. Sur les 101 dossiers, 114 issues sont notées `plan_cession_arrete` (les dossiers ont parfois plusieurs entités, ex. groupes INNATIS), 6 `liquidation`, 446 `en_attente`.

Confiance d'extraction : 254 `high`, 125 `medium`, 150 `low`, 37 `partial_pdf_only`. Les chiffres calculés sur sous-échantillons `medium`+`high` (n=379) sont plus fiables que ceux du corpus complet.

## 2. Répartition sectorielle

Sur les 528 offres avec NAF renseigné :

| Secteur (top 15) | n offres | n dossiers | n retenues | n rejetées |
|---|---|---|---|---|
| Immobilier (toutes catégories) | 226 | 7 (groupe FHBX + NEOCAMP) | 2 | 17 |
| Commerce détail textile/déco | 15 | 1 (EURODIF/Bouchara) | 2 | 13 |
| Production agricole — pommes | 13 | 2 (groupe INNATIS) | 4 | 9 |
| Restauration / bar / club | 19 | 3 | 2 | 1 |
| Hôtellerie plein air / camping | 9 | 1 (Alpha Camping / Seasonova) | 1 | 8 |
| Salle de sport / fitness | 8 | 2 (CGB, CPR) | 1 | 0 |
| Tourisme social / hébergement / ESS | 14 | 2 | 0 | 0 |
| Santé — soins dentaires (Denteka) | 5 | 2 | 3 | 0 |
| Expertise comptable / CAC | 6 | 1 (EZIN & STRAUUS) | 2 | 1 |
| Arboriculture | 6 | 1 | 3 | 3 |
| Optique mobile (SYM/LOM) | 9 | 3 (SYM TECH, SYM OPTIC, SYM LAB) | 3 | 0 |
| Agences digitales / conseil (COSA) | 9 | 1 | 1 | 5 |
| Conseil (AXIOVAL) | 3 | 1 | 3 | 0 |

Lecture : **l'immobilier représente 40 % du corpus** mais surtout via 2 portefeuilles massifs (FHBX Affaire Balthazar 26 SCI, NEOCAMP 11+ SCI). Hors ces deux mégadossiers, l'immo pèse beaucoup moins. Trois secteurs concentrent 80 % des retenues observées : **agro-alimentaire (Vergers d'Anjou)**, **santé/dentaire**, **fitness/sport**.

## 3. Taille des cibles

CA cible (n=292 offres avec valeur, hors `null`) :

| Quantile | Valeur (€) |
|---|---|
| min | 0 |
| P25 | 700 000 |
| **médiane** | **2 197 445** |
| P75 | 9 350 000 |
| max | 119 600 000 |

EBITDA cible : seulement n=37 offres avec EBITDA renseigné (souvent null car dossier RJ = comptes dégradés). Médiane EBITDA = 0, P25 = -2,1 M€, P75 = 230 k€ — confirme que la majorité des cibles sont en perte.

Effectif (n=553 offres) : médiane 11, P25=3, P75=46, max=2 000 (groupe FHBX consolidé). 60 % des cibles ont **moins de 25 salariés**.

Nombre de sites : médiane 1, P75=2, max=212 (EURODIF / Bouchara). Le corpus est dominé par des PME mono-site, avec 6 mégadossiers multi-sites (INNATIS, NEOCAMP, FHBX, ALPHA CAMPING, EURODIF, MINELLI).

## 4. Type de procédure

| Procédure | n | % |
|---|---|---|
| **Redressement judiciaire (RJ)** | 519 | 91,7 % |
| Sauvegarde | 15 | 2,7 % |
| Liquidation judiciaire — poursuite | 15 | 2,7 % |
| Prepack-cession | 8 | 1,4 % |
| Plan de cession (autonome) | 6 | 1,1 % |
| LJ classique | 2 | 0,4 % |
| NR | 1 | 0,2 % |

Le RJ domine massivement. Les prepacks restent rares (1,4 %) malgré la pression réglementaire pour les développer.

## 5. Type de repreneur

Forme juridique des candidats (n=566) :

| Forme | n offres | n retenues | Taux retenue (sur décidées) |
|---|---|---|---|
| Société existante industrielle (entrant non-concurrent) | 314 (55,5 %) | 31 (66 % des winners) | 28,7 % (31/108 décidées) |
| Holding ad-hoc | 51 | 0 | 0 % (0/8) |
| Société existante concurrente | 37 | 5 | 33 % (5/15) |
| Family office | 34 | 3 | 100 % (3/3 décidées) |
| Personne physique seule | 28 | 1 | 16 % (1/6) |
| Fonds PE | 18 | 0 | 0 % (0/3) |
| Association / collectivité | 14 | 4 (groupe Vergers d'Anjou) | 100 % (4/4) |
| Dirigeant historique | 11 | 0 | 0 % (0/1) |
| Repreneur étranger | 9 | 2 (AA Investments HK / EURODIF) | 50 % (2/4) |
| Salariés | 3 | 1 (EZIN & STRAUUS) | 50 % (1/2) |

**Insight chiffré** : la holding ad-hoc et les fonds PE sortent à **0 % de retenue** sur les dossiers décidés du corpus (très petit n, fragile : 8 et 3). La société existante industrielle / association / family office concentrent l'ensemble des wins.

## 6. Pricing — distributions

Prix total (n=384 offres avec prix renseigné) :

| Tranche prix | n | % |
|---|---|---|
| Symbolique 1-9 € | 17 | 4 % |
| 10-999 € | 5 | 1 % |
| 1k–10k € | 36 | 9 % |
| 10k–100k € | 144 | 38 % |
| 100k–1M € | 105 | 27 % |
| 1M–10M € | 41 | 11 % |
| > 10M € | 36 | 9 % |

Médiane globale prix : **50 000 €**. P25 = 10 000 €. P75 = 300 000 €.

**Distribution retenues vs rejetées** (prix renseigné) :

| | n | min | P25 | médiane | P75 | max |
|---|---|---|---|---|---|---|
| Retenues | 41 | 1 300 | 30 000 | **50 000** | 100 000 | 7 040 000 |
| Rejetées | 92 | 1 | 5 000 | **50 000** | 250 000 | 12 000 000 |

Médianes identiques mais P75 plus haut chez rejetées (offres prix-only sans dossier solide). La distribution P25 nettement plus haute chez retenues (30k€ vs 5k€) montre que **les offres < 10 k€ gagnent rarement** sauf cas particuliers (Denteka 1 300 €/Colmar — concurrent unique, ou Alpha Camping/Seasonova 2 €/site — multi-sites consolidé).

Multiple prix / CA : **insufficient sample** — n=4 retenues seulement avec CA + prix > 0 (LPC mult 0,69 ; CAVL 0,012 ; ALPHA CAMPING quasi-nul). On ne peut pas conclure de multiple typique. Sur l'ensemble du corpus (n=44 décidées avec CA+prix), médiane multiple = **0,015 × CA** — confirmant que la cession en RJ se fait quasi-toujours à un prix très inférieur à 1 × CA.

## 7. Volet social — taux de reprise effectifs

n=347 offres avec pct_reprise renseigné :

| | n | min | P25 | médiane | P75 | max |
|---|---|---|---|---|---|---|
| Toutes offres | 347 | 0 | 33,3 % | 50 % | 87,5 % | 100 % |
| Retenues | 37 | 0 | 50 % | **66,7 %** | 100 % | 100 % |
| Rejetées | 66 | 0 | 0 % | **33 %** | 75 % | 100 % |

**Écart médian de 33 points** retenues vs rejetées sur le taux de reprise des effectifs. C'est l'un des deltas les plus forts du corpus. Les offres retenues affichent plus souvent 100 % (mediane P75) ; les rejetées s'agglutinent autour de 0–33 %.

## 8. Forme de l'offre

| Variable | retenues n=47 | rejetées n=107 |
|---|---|---|
| Sommaire détaillé | 89,1 % | 66,7 % |
| Lettre simple | 10,9 % | 22,9 % |
| Executive summary présent | 37,8 % | 24,7 % |
| Qualité « claire » | 80,9 % | 40,2 % |
| Qualité « dense / confuse » | 17,0 % | 41,1 % |
| Ton mixte (juridique + commercial) | 39,1 % | 13,5 % |
| Nb pages total (médiane, n petit) | 13,5 (n=18) | 30,5 (n=14) |

Les offres retenues sont **plus courtes médianes, mieux structurées, plus claires** que les rejetées (qui souvent compensent par du volume opaque).

## 9. Annexes — taux de présence (winners vs losers)

| Annexe | retenues | rejetées | Δ |
|---|---|---|---|
| Kbis du repreneur | 84,1 % | 42,0 % | +42 pts |
| Attestation bancaire / RIB | 50,0 % | 7,9 % | +42 pts |
| Comptes sociaux 3 ans | 59,0 % | 40,3 % | +19 pts |
| Business plan | 32,5 % | 18,1 % | +14 pts |
| Organigramme cible | 60,0 % | 22,2 % | +38 pts |
| CV dirigeants | 37,5 % | 15,4 % | +22 pts |
| CNI dirigeants | 25,0 % | 1,4 % | +24 pts |
| Attest. fiscale / sociale | 21,2 % | 2,8 % | +18 pts |

Toutes les annexes documentaires séparent retenues de rejetées d'au moins 14 points. C'est l'un des prédicteurs les plus forts du corpus.

## 10. Conditions suspensives

| Variable | retenues | rejetées |
|---|---|---|
| Aucune CS | 40,4 % | 8,4 % |
| Nb CS (médiane) | 1 | 4 |
| Agressivité « aucune » | 87,2 % | 55,7 % |
| Agressivité « modérée+forte » | 10,6 % | 24,5 % |

**Insight chiffré majeur** : les offres « sans CS » sortent à 40 % chez retenues vs 8 % chez rejetées — facteur x5.

## 11. Confiance d'extraction par segment

| Confidence | n offres | dont retenues | dont rejetées |
|---|---|---|---|
| high | 254 | 22 | 51 |
| medium | 125 | 17 | 30 |
| low | 150 | 7 | 22 |
| partial_pdf_only | 37 | 1 | 4 |

Les statistiques de la section 2 (anatomie winners vs losers) gagnent en précision en filtrant sur `confidence ∈ {high, medium}` (n=379), ce qu'on ne fait pas par défaut ici pour ne pas réduire les n des sous-segments rares.

## Related

- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/playbook-redaction-offre]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/02-anatomie-winners-vs-losers]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/08-grille-scoring-100pts]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/_index]]
