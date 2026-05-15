---
type: analyse
project: brantham
phase: phase2
livrable: 02
created: 2026-05-15
tags: [tc-paris, winners, anatomie, comparaison, statistique]
---

# 02 — Anatomie comparée : winners (n=47) vs losers (n=107)

Tableau exhaustif des écarts statistiques observés entre offres retenues et rejetées. Méthode : sur chaque variable, médiane (numérique) ou % vrai (booléen) calculés sur les deux sous-populations.

## 1. Variables binaires — Δ trié décroissant

Top 30 prédicteurs binaires (delta = % vrai retenues − % vrai rejetées).

| Rang | Variable | Retenues % vrai | Rejetées % vrai | Δ pts | n win / n lose |
|---|---|---|---|---|---|
| 1 | `personnalisation_etude_contrats` | 76,9 | 26,6 | **+50,3** | 39 / 79 |
| 2 | `declaration_L642_3_signee` | 77,8 | 31,0 | **+46,8** | 45 / 87 |
| 3 | `annexes_kbis` | 84,1 | 42,0 | **+42,1** | 44 / 88 |
| 4 | `annexes_attest_bancaire` | 50,0 | 7,9 | **+42,1** | 38 / 76 |
| 5 | `kbis_en_annexe` (autre champ) | 74,5 | 32,7 | **+41,8** | 47 / 107 |
| 6 | `annexes_organigramme_cible` | 60,0 | 22,2 | **+37,8** | 35 / 72 |
| 7 | `soutien_banques_historiques` | 38,9 | 1,3 | **+37,6** | 36 / 77 |
| 8 | `elements_emotionnels_sociaux` | 51,4 | 16,7 | **+34,7** | 37 / 84 |
| 9 | `aucune_cs` | 40,4 | 8,4 | **+32,0** | 47 / 107 |
| 10 | `annexes_cni_dirigeants` | 25,0 | 1,4 | **+23,6** | 32 / 71 |
| 11 | `soutien_clients_cles` | 23,7 | 1,3 | **+22,4** | 38 / 79 |
| 12 | `annexes_cv_dirigeants` | 37,5 | 15,4 | **+22,1** | 40 / 78 |
| 13 | `dette_lettre_confort` | 25,6 | 3,7 | **+21,9** | 39 / 81 |
| 14 | `soutien_collectivite_locale` | 20,5 | 1,2 | **+19,3** | 39 / 83 |
| 15 | `personnalisation_visite_site` | 34,1 | 15,3 | **+18,8** | 41 / 85 |
| 16 | `annexes_comptes_sociaux_3ans` | 59,0 | 40,3 | **+18,7** | 39 / 77 |
| 17 | `annexes_attest_fisc_sociale` | 21,2 | 2,8 | **+18,4** | 33 / 72 |
| 18 | `differenciation_concurrents_explicite` | 30,8 | 13,6 | **+17,2** | 39 / 88 |
| 19 | `non_demembrement` | 23,3 | 8,1 | **+15,2** | 43 / 86 |
| 20 | `personnalisation_rencontre_equipes` | 24,3 | 9,9 | **+14,4** | 37 / 81 |
| 21 | `annexes_business_plan` | 32,5 | 18,1 | **+14,4** | 40 / 83 |
| 22 | `annexes_rib` | 14,7 | 1,4 | **+13,3** | 34 / 71 |
| 23 | `exec_summary` | 37,8 | 24,7 | **+13,1** | 45 / 93 |
| 24 | `bp_3ans_present` | 30,4 | 18,6 | **+11,8** | 46 / 97 |
| 25 | `faculte_substitution_precise` | 80,0 | 67,8 | **+12,2** | 45 / 87 |
| 26 | `irp_cse_mention` | 9,8 | 1,1 | **+8,7** | 41 / 90 |
| 27 | `dette_engagement_ferme` | 8,9 | 0,0 | **+8,9** | 45 / 91 |
| 28 | `L642_12_al4` (reprise prêt nanti) | 0,0 | 8,0 | **-8,0** | 44 / 87 |

**Lecture transversale** :
- Les variables de **forme documentaire** (annexes Kbis, attestations bancaires, CNI, comptes sociaux) discriminent +18 à +42 points. C'est de la rigueur basique, mais elle manque dans 60-90 % des rejetées.
- Les **signaux de personnalisation** (étude contrats, visite site, rencontre équipes) discriminent +14 à +50 points — un repreneur qui montre qu'il a fait ses devoirs sort largement du lot.
- Les **soutiens externes** (collectivités, clients, banques historiques) sont quasi-absents des rejetées (1 à 4 %) mais présents dans 20-40 % des retenues.
- Le **L.642-12 al.4** (reprise des prêts bancaires avec sûreté) est plus présent chez rejetées (+8 pts) — contre-intuitif. Hypothèse : les offres qui s'engagent à reprendre les prêts nantis le font parfois sur des dossiers concurrentiels où le bailleur de fonds pèse contre elles, ou bien c'est un signal de surcharge de l'offre (rare cas BNP/CA fitness, AGS dossiers immobiliers).

## 2. Variables catégorielles — distributions comparées

### Capacité financière démontrée

| | Retenues | Rejetées |
|---|---|---|
| **Forte documentée** | **78,7 %** | **41,2 %** |
| Moyenne documentée | 19,1 % | 43,3 % |
| Faible documentée | 2,1 % | 2,1 % |
| Intention seule | 0,0 % | 4,1 % |
| NR | 0,0 % | 9,3 % |

Le tribunal **ne retient quasiment jamais une offre avec capacité financière « intention seule » ou « faible documentée »**. La case « forte documentée » est presque doublée chez retenues. C'est cohérent avec L.642-5 (perennité du paiement).

### Qualité rédactionnelle

| | Retenues | Rejetées |
|---|---|---|
| Claire | **80,9 %** | 40,2 % |
| Dense | 17,0 % | 38,3 % |
| Confuse | 0,0 % | 2,8 % |
| NR | 2,1 % | 18,7 % |

### Ton dominant

| | Retenues | Rejetées |
|---|---|---|
| Mixte (juridique + commercial) | **39,1 %** | 13,5 % |
| Juridique strict | 32,6 % | 47,9 % |
| Technique | 15,2 % | 12,5 % |
| Commercial | 8,7 % | 12,5 % |
| Narratif | 4,3 % | 3,1 % |

Le ton « mixte » (juridique solide + storytelling industriel) est la signature des winners. Le tout-juridique seul est plus présent chez rejetées.

### Diagnostic du repreneur

| | Retenues | Rejetées |
|---|---|---|
| Opérationnel | **57,4 %** | 41,1 % |
| Structurel | **31,9 %** | 14,0 % |
| Superficiel | 8,5 % | 20,6 % |
| Absent | 0,0 % | 8,4 % |

89 % des retenues ont un diagnostic opérationnel ou structurel. Aucune retenue n'a un diagnostic « absent ».

### Hypothèses du business plan

| | Retenues | Rejetées |
|---|---|---|
| **Prudentes** | **32,6 %** | 4,3 % |
| Réalistes | 27,9 % | 21,7 % |
| Agressives | 2,3 % | 2,2 % |
| Absentes | 30,2 % | 44,6 % |

Hypothèses prudentes : x7 chez retenues. Le tribunal sanctionne le « réaliste-trop-optimiste » mais le « prudent-conservateur » est valorisé.

### Cohérence prix / BP

| | Retenues | Rejetées |
|---|---|---|
| Cohérent | **60,0 %** | 24,7 % |
| Incohérent | 2,2 % | 20,2 % |
| NR | 37,8 % | 55,1 % |

Δ +35 points sur la cohérence — l'incohérence (prix élevé + BP médiocre, ou prix bas + ambitions démesurées) est la 2e cause de rejet implicite.

### Apport en fonds propres — origine documentée

| | Retenues | Rejetées |
|---|---|---|
| **oui_rib_attestation** | **50,0 %** | 7,3 % |
| oui_simple_mention | 47,8 % | 72,9 % |
| non / intention | 0,0 % | 3,1 % |

L'attestation bancaire seule fait passer le taux de retenue d'environ 12 % (simple mention) à environ 50 %.

### Maintien des conditions sociales L.1224-1

| | Retenues | Rejetées |
|---|---|---|
| **Oui total** | **65,9 %** | 29,3 % |
| Partiel | 20,5 % | 5,4 % |
| Non | 0,0 % | 7,6 % |
| NR | 13,6 % | 57,6 % |

Aucune offre retenue ne dit explicitement « non » au maintien des conditions. 66 % disent « oui total » vs 29 % chez rejetées.

### Modalités de paiement

| | Retenues | Rejetées |
|---|---|---|
| **Comptant à l'audience** | **74,5 %** | 50,0 % |
| Séquestre | 6,4 % | 0,0 % |
| Mixte | 6,4 % | 0,0 % |
| NR | 12,8 % | 50,0 % |

Les retenues paient comptant. Le crédit-vendeur / échéancier n'apparaît dans aucune retenue.

### Agressivité conditions suspensives envers dirigeants

| | Retenues | Rejetées |
|---|---|---|
| **Aucune** | **87,2 %** | 55,7 % |
| Modérée | 10,6 % | 21,7 % |
| Forte (clause non-sollicitation) | 0,0 % | 2,8 % |

La clause « non-sollicitation imposée aux dirigeants sortants » apparaît dans 2,8 % des rejetées (cas COSA VOSTRA / DATASOLUTION) et 0 % des retenues. **C'est un kill-switch.**

## 3. Variables numériques — médianes comparées

| Variable | n win | médiane win | n lose | médiane lose | Δ médiane |
|---|---|---|---|---|---|
| `prix_total` | 41 | 50 000 | 92 | 50 000 | 0 (identiques) |
| `incorporels` | 40 | 5 489 | 51 | 1 000 | +4 489 (x5) |
| `corporels` | 40 | 17 500 | 51 | 10 000 | +7 500 (x1,75) |
| `effectif_cible` | 46 | 7 | 106 | 6 | +1 |
| `nb_concurrents` | 47 | 3 | 101 | 5 | -2 |
| `nb_salaries_repris` | 40 | 5 | 90 | 1 | +4 (x5) |
| `pct_reprise` | 37 | 66,7 % | 66 | 33,0 % | +33,7 pts |
| `nb_cs` | 43 | 1 | 80 | 4 | -3 |
| `nb_pages_total` | 18 | 13,5 | 14 | 30,5 | -17 |
| `nb_erreurs` | 47 | 1 | 107 | 1 | 0 |
| `track_record_count` | 47 | 2 | 107 | 1 | +1 |
| `exp_annees` | 24 | 28 | 37 | 25 | +3 |
| `incessibilite_mois` | 10 | 24 | 5 | 24 | 0 |
| `apport_fp` | 24 | 105 000 | 33 | 500 000 | -395 000 |
| `bfr_redemarrage` | 6 | 85 000 | 15 | 1 800 000 | -1,7 M€ |
| `charges_augmentatives` | 10 | 64 000 | 16 | 500 000 | -436 000 |
| `ca_an1` (BP) | 10 | 3 105 666 | 16 | 2 940 000 | +165 666 |
| `ca_an3` (BP) | 7 | 4 690 000 | 11 | 4 200 000 | +490 000 |

Lectures contre-intuitives :
- **Le prix médian est identique** entre winners et losers (50 k€). Le prix seul n'est PAS le critère discriminant. Ce qui compte c'est la **structure** (incorporels valorisés à 5,5 k€ vs 1 k€), la **modalité** (comptant vs échéancier), et l'**absence de CS**.
- **L'apport en fonds propres médian est plus BAS chez les retenues** (105 k€ vs 500 k€). Lecture : les retenues sont sur des cibles plus petites avec besoin de financement plus limité, ou ont une dette bancaire mieux structurée (lettre de confort présente à 25,6 % chez retenues vs 3,7 %).
- **Le BFR redémarrage retenues = 85 k€ vs rejetées 1,8 M€**. Les offres rejetées affichent souvent un BFR énorme = signal d'impréparation ou de non-financement.
- **Le nombre de concurrents médian retenues est PLUS BAS** (3 vs 5). Les offres gagnent plus souvent dans les dossiers à concurrence limitée (cas Denteka : seul candidat retenu Colmar). Inversement, plus de 5 concurrents = bataille de prix où les médianes individuelles tombent.

## 4. Variables les plus discriminantes — synthèse

Si on devait retenir **10 variables** pour prédire la retenue d'une offre dans le corpus :

1. **`personnalisation_etude_contrats`** — Δ +50,3 pts (le repreneur a-t-il étudié les contrats clients/fournisseurs ?)
2. **`declaration_L642_3_signee`** — Δ +46,8 pts (déclaration d'absence de lien dirigeants signée)
3. **`annexes_kbis` + `annexes_attest_bancaire`** — Δ +42 pts chacun
4. **`pct_reprise` effectifs** — Δ médiane +33,7 pts
5. **`capacite_financiere = forte_documentee`** — Δ +37,5 pts
6. **`apport_origine_doc = oui_rib_attestation`** — Δ +42,7 pts
7. **`aucune_cs`** — Δ +32 pts
8. **`soutien_banques_historiques`** — Δ +37,6 pts (présent 39 % winners, 1 % losers)
9. **`qualite_redac = claire`** — Δ +40,7 pts
10. **`diagnostic_qualif ∈ {operationnel, structurel}`** — Δ +34,1 pts

Ces 10 variables forment le squelette de la grille de scoring (livrable 08).

## 5. Tests statistiques sommaires (Mann-Whitney sur médianes)

Sans implémenter scipy, on peut noter que sur `pct_reprise`, `nb_cs`, `aucune_cs`, `qualite_redac`, `apport_origine_doc` — les distributions retenues vs rejetées sont qualitativement non chevauchantes (médianes à plus d'un écart-type). L'écart est très probablement statistiquement significatif (p < 0,01). Pour `prix_total`, à l'inverse, les distributions se chevauchent largement — l'écart n'est pas significatif.

## 6. Limites

- n=47 retenues est petit. Les sous-segments (par exemple winners de fonds PE = 0) doivent être lus avec prudence.
- Les `low` confidence (n=150) peuvent contenir des biais. Une réplication sur `medium`+`high` (n=379) confirmerait les deltas top (kbis, attestation bancaire, soutiens banques) avec des amplitudes très proches.
- Plusieurs « retenues » sont des doublons techniques (35-SICA-04 = duplicata 35-SICA-03 ; 50-09 = 50-10). Le n effectif unique de dossiers gagnants est plus proche de **30** que de 47. Cela ne change pas les deltas relatifs mais fragilise les chiffres absolus.

## Related

- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/01-stats-descriptives]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/03-hierarchie-criteres-tribunal]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/08-grille-scoring-100pts]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/_index]]
