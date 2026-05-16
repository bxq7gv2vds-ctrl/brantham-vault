---
type: analyse
project: brantham
phase: phase2
livrable: 11
created: 2026-05-16
tags: [tc-paris, statistiques, chi-deux, mann-whitney, validation, machine-learning, angles-morts]
---

# 11 — Tests statistiques formels et analyses résiduelles

Ce livrable clôt la phase 2 en apportant la **rigueur statistique** qui manquait aux livrables 02 à 10 (différences de proportions présentées comme observations, jamais testées) et en traitant les **trois analyses jamais lancées** listées dans le livrable 10 section 9 : cabinet d'avocats, administrateur judiciaire, délai v1 vers v2.

Méthode : tous les calculs sont rejouables via le script `_compute_tests.py` (sorties brutes dans `_tests_output.json`). Corpus : 566 offres, dont **154 décidées** (47 retenues, 107 rejetées). Rappel structurant du livrable 10 : le n unique de repreneurs gagnants est plus proche de 15 que de 47 (doublons techniques et entités d'un même groupe). Tous les chiffres ci-dessous sont à lire avec ce facteur d'inflation en tête.

## 1. Tests statistiques formels sur les variables discriminantes

Pour chaque variable binaire du livrable 02, test du chi-deux (effectifs attendus tous supérieurs ou égaux à 5) ou test exact de Fisher (sinon), avec intervalle de confiance à 95 % sur la différence de proportions (approximation de Wald). Pour les variables numériques, test de Mann-Whitney U bilatéral avec taille d'effet rank-biserial. Tableau trié par p-value croissante.

### 1.1 Variables significatives à p < 0,05 (39 sur 53 testées)

| Variable | Δ | p-value | Test | IC 95 % du Δ (pts) |
|---|---|---|---|---|
| `apport_rib_attestation` | +42,7 pts | 5,4e-09 | Fisher | [29,8 ; 55,7] |
| `soutien_banques_historiques` | +37,6 pts | 1,6e-07 | Fisher | n.d. |
| `personnalisation_etude_contrats` | +50,3 pts | 2,1e-07 | chi2 | n.d. |
| `annexes_attest_bancaire` | +42,1 pts | 3,0e-07 | Fisher | n.d. |
| `declaration_L642_3_signee` | +46,7 pts | 3,4e-07 | chi2 | n.d. |
| `kbis_en_annexe` | +41,8 pts | 1,6e-06 | chi2 | n.d. |
| `aucune_cs` | +32,0 pts | 2,1e-06 | chi2 | n.d. |
| `nb_concurrents` (médiane) | -2 | 3,1e-06 | Mann-Whitney | rank-biserial négatif |
| `qualite_redac_claire` | +40,7 pts | 3,3e-06 | chi2 | n.d. |
| `annexes_kbis` | +42,0 pts | 4,5e-06 | chi2 | n.d. |
| `hypotheses_prudentes` | +28,2 pts | 7,0e-06 | Fisher | n.d. |
| `capacite_financiere_forte` | +37,5 pts | 2,4e-05 | chi2 | n.d. |
| `diagnostic_op_ou_struct` | +34,2 pts | 3,9e-05 | chi2 | n.d. |
| `nb_cs` (médiane) | -3 | 4,3e-05 | Mann-Whitney | rank-biserial négatif |
| `maintien_conditions_oui_total` | +36,6 pts | 5,1e-05 | chi2 | n.d. |
| `coherence_prix_bp_coherent` | +35,3 pts | 6,2e-05 | chi2 | n.d. |
| `elements_emotionnels_sociaux` | +34,7 pts | 7,9e-05 | chi2 | n.d. |
| `annexes_organigramme_cible` | +37,8 pts | 1,0e-04 | chi2 | n.d. |
| `soutien_clients_cles` | +22,4 pts | 1,0e-04 | Fisher | n.d. |
| `agressivite_cs_aucune` | +31,6 pts | 2,0e-04 | chi2 | n.d. |
| `bfr_redemarrage` (médiane) | -1,72 M€ | 2,0e-04 | Mann-Whitney | n.d. |
| `annexes_cni_dirigeants` | +23,6 pts | 3,0e-04 | Fisher | n.d. |
| `nb_salaries_repris` (médiane) | +4 | 4,0e-04 | Mann-Whitney | n.d. |
| `soutien_collectivite_locale` | +19,3 pts | 4,0e-04 | Fisher | n.d. |
| `ton_mixte` | +25,6 pts | 6,0e-04 | chi2 | n.d. |
| `dette_lettre_confort` | +21,9 pts | 7,0e-04 | Fisher | n.d. |
| `nb_erreurs` (médiane) | 0 | 4,0e-03 | Mann-Whitney | distribution décalée |
| `annexes_attest_fisc_sociale` | +18,4 pts | 4,0e-03 | Fisher | n.d. |
| `paiement_comptant_audience` | +24,5 pts | 4,7e-03 | chi2 | n.d. |
| `annexes_cv_dirigeants` | +22,1 pts | 6,8e-03 | chi2 | n.d. |
| `charges_augmentatives` (médiane) | -436 k€ | 1,2e-02 | Mann-Whitney | n.d. |
| `annexes_rib` | +13,3 pts | 1,3e-02 | Fisher | n.d. |
| `track_record_count` (médiane) | +1 | 1,4e-02 | Mann-Whitney | n.d. |
| `personnalisation_visite_site` | +18,9 pts | 1,6e-02 | chi2 | n.d. |
| `non_demembrement` | +15,1 pts | 1,7e-02 | chi2 | n.d. |
| `differenciation_concurrents_explicite` | +17,1 pts | 2,3e-02 | chi2 | n.d. |
| `pct_reprise` (médiane) | +34 pts | 2,9e-02 | Mann-Whitney | n.d. |
| `personnalisation_rencontre_equipes` | +14,4 pts | 3,8e-02 | chi2 | n.d. |
| `apport_fp` (médiane) | -395 k€ | 4,1e-02 | Mann-Whitney | n.d. |

### 1.2 Variables NON significatives (le Δ annoncé est du bruit ou trop fragile)

| Variable | Δ annoncé livrable 02 | p-value | Verdict |
|---|---|---|---|
| `annexes_comptes_sociaux_3ans` | +18,7 pts | 0,056 | Limite, non significatif |
| `annexes_business_plan` | +14,4 pts | 0,074 | Non significatif |
| `L642_12_al4` | -8,0 pts | 0,095 | Non significatif (l'effet « contre-intuitif » du livrable 02 n'est pas robuste) |
| `bp_3ans_present` | +11,9 pts | 0,111 | Non significatif |
| `exec_summary` | +13,0 pts | 0,113 | Non significatif (alors qu'il pèse dans la grille 08 bloc F) |
| `faculte_substitution_precise` | +12,2 pts | 0,140 | Non significatif (pèse dans la grille 08 bloc E.6) |
| `nb_pages_total` (médiane) | -17 | 0,148 | Non significatif (n=18/14 seulement, trop peu) |
| `exp_annees` (médiane) | +3 | 0,261 | Non significatif |
| `incorporels` (médiane) | +4 488 € | 0,284 | Non significatif (le « x5 » du livrable 02 n'est pas robuste) |
| `corporels` (médiane) | +7 500 € | 0,404 | Non significatif |
| `effectif` (médiane) | +1 | 0,567 | Non significatif |
| `ca_an1` (médiane) | +166 k€ | 0,853 | Non significatif |
| `prix_total` (médiane) | 0 | 0,942 | Non significatif (confirme : le prix ne discrimine pas) |
| `incessibilite_mois` (médiane) | 0 | 1,000 | Non significatif (n=10/5, ininterprétable) |

### 1.3 Lecture

- **Le squelette des 10 variables de la grille (livrable 08) tient.** Les 10 prédicteurs cités au livrable 02 section 4 sont tous significatifs à p < 0,001 : étude des contrats, L.642-3, Kbis et attestation bancaire, capacité financière forte, apport RIB, absence de CS, soutien banques, qualité claire, diagnostic opérationnel ou structurel. Ce sont des conclusions statistiquement validées, plus seulement des observations.
- **Six variables présentées comme discriminantes au livrable 02 ne le sont pas** : `incorporels` (le « x5 » disparaît), `corporels`, `bp_3ans_present`, `exec_summary`, `faculte_substitution_precise`, `L642_12_al4`. Deux d'entre elles (`exec_summary`, `faculte_substitution_precise`) sont pondérées dans la grille 08. Voir section 6 pour la conséquence sur la grille.
- **Le prix médian ne discrimine toujours pas** (p = 0,94). Ce qui est désormais confirmé : ni le prix, ni la ventilation incorporels/corporels ne séparent les winners des losers. Ce qui discrimine, c'est la **modalité** (comptant), la **structure de risque** (absence de CS, BFR redémarrage faible) et le **volet social** (`pct_reprise`).
- **Avertissement multiplicité.** 53 tests ont été menés. Avec une correction de Bonferroni stricte (seuil = 0,05/53 ≈ 9,4e-04), les variables des rangs 1 à 25 restent significatives, mais les 14 variables situées entre p = 9,4e-04 et p = 0,05 (de `nb_erreurs` à `apport_fp`) deviennent fragiles. La hiérarchie globale n'est pas modifiée : les prédicteurs de tête restent les mêmes.

## 2. Réplication sur sous-corpus fiable (high + medium confidence)

Re-calcul des 11 deltas de tête en excluant les offres `low` et `partial_pdf_only` (les 150 + 37 extractions douteuses). Sous-corpus fiable : **n = 138 décidées** (46 retenues, 92 rejetées). Les retenues perdent une seule unité (47 vers 46) : la cohorte gagnante était déjà à 83 % de confiance medium ou high, conformément au livrable 10 section 7.1.

| Variable | Δ full (n=154) | Δ fiable (n=138) | Écart | Tient ? |
|---|---|---|---|---|
| `personnalisation_etude_contrats` | +50,3 | +49,3 | -1,0 | OUI |
| `declaration_L642_3_signee` | +46,7 | +46,8 | +0,1 | OUI |
| `annexes_kbis` | +42,0 | +41,1 | -0,9 | OUI |
| `annexes_attest_bancaire` | +42,1 | +41,9 | -0,2 | OUI |
| `kbis_en_annexe` | +41,8 | +40,2 | -1,6 | OUI |
| `soutien_banques_historiques` | +37,6 | +37,5 | -0,1 | OUI |
| `aucune_cs` | +32,0 | +31,5 | -0,5 | OUI |
| `elements_emotionnels_sociaux` | +34,7 | +34,1 | -0,6 | OUI |
| `capacite_financiere_forte` | +37,5 | +36,0 | -1,5 | OUI |
| `qualite_redac_claire` | +40,7 | +37,0 | -3,7 | OUI |
| `apport_rib_attestation` | +42,7 | +42,3 | -0,4 | OUI |

**Verdict : les 11 deltas de tête sont robustes.** Aucun ne bouge de plus de 3,7 points quand on retire les 187 extractions douteuses, et tous restent significatifs à p < 0,05 sur le sous-corpus fiable. La crainte du livrable 02 section 6 (« les low confidence peuvent contenir des biais ») est levée pour les variables de tête : les patterns ne sont pas un artefact d'extraction. Cela ne dit rien des variables de seconde ligne (section 1.2), mais celles-ci ne sont de toute façon pas significatives.

## 3. Cabinet d'avocats du repreneur et succès

Champ `avocat_cabinet` (grilles) complété par `avocat_repreneur` (master CSV), après nettoyage du bruit d'extraction (dates, montants, mentions « non mentionné » qui polluaient le champ master). **67 offres décidées sur 154 ont un cabinet exploitable (44 %).** Taux de retenue de référence sur le corpus décidé : 30,5 %.

| Cabinet | n | Retenues | Taux retenue | p Fisher vs reste |
|---|---|---|---|---|
| FIDAL | 24 | 0 | 0,0 % | 0,0007 |
| LEXCAP | 18 | 15 | 83,3 % | 0,0000 |
| AGN Avocats | 3 | 3 | 100 % | n faible |
| Guarrel Avocat | 3 | 3 | 100 % | n faible |
| IKKI Partners | 3 | 0 | 0,0 % | n faible |
| Parthema Avocats | 3 | 0 | 0,0 % | n faible |
| PZ Avocats | 2 | 2 | 100 % | n faible |
| Autres (1 à 2 offres) | 11 | mixte | n.d. | n faible |

**Piège majeur : ces chiffres sont un artefact de confusion avec un méga-dossier, PAS un effet de compétence.** Vérification faite : les 18 offres LEXCAP et les 24 offres FIDAL portent **exclusivement** sur le bloc de méga-dossiers INNATIS / Vergers d'Anjou (dossiers 34-LPC, 35-SICA, 36-LVL, 37-COOP, 57 à 66). Sur ce bloc, deux repreneurs concurrents s'affrontaient : LEXCAP conseillait le repreneur retenu (pôle ligérien), FIDAL conseillait le repreneur évincé. Les deux cabinets n'apparaissent nulle part ailleurs dans le corpus. Le « LEXCAP 83 % » et le « FIDAL 0 % » ne mesurent donc qu'**une seule décision de tribunal sur un seul bloc de dossiers**, dupliquée par les ~40 entités du groupe. Le n effectif est de **1 dossier opposant 2 cabinets**, pas de 42 observations indépendantes.

**Conclusion analyse 3 : aucun signal exploitable.** Il n'existe pas dans le corpus de cabinet d'avocats sur-performant identifiable. Le champ est trop peu rempli (44 %) et, là où il l'est, dominé à 63 % par un méga-dossier unique. Cette hypothèse (livrable 10 section 9 point 1) ne peut pas être testée sans données neuves : il faudrait un corpus où chaque cabinet apparaît sur plusieurs dossiers indépendants.

## 4. Administrateur judiciaire et taux de retenue

Champ `aj` normalisé (regroupement des variantes orthographiques d'un même AJ). **153 offres décidées sur 154 ont un AJ renseigné.** Test exact de Fisher de chaque AJ contre le reste du corpus décidé.

| Administrateur judiciaire | n offres | Dossiers uniques | Retenues | Taux retenue | p Fisher |
|---|---|---|---|---|---|
| Marine PACE | 51 | 13 | 18 | 35,3 % | 0,49 |
| Flechard / Bouyer / Langet | 33 | n.d. | 5 | 15,2 % | 0,03 |
| Hélène Bourbouloux | 20 | n.d. | 1 | 5,0 % | 0,007 |
| Poli / Bauland | 15 | n.d. | 2 | 13,3 % | 0,13 |
| Sandra Beladjine | 14 | 3 | 9 | 64,3 % | 0,008 |
| Carole Martinez (et co-AJ) | 9 cumulé | n.d. | 2 | ~22 % | n faible |
| Carboni, Sanchez-Sepval, Hunsinger | 2 à 3 chacun | n.d. | variable | n faible |

**Lecture, avec la même prudence que la section 3.** Trois AJ ressortent statistiquement (p < 0,05) mais l'interprétation est piégée :

- **Hélène Bourbouloux à 5 % de retenue** : c'est l'AJ des méga-dossiers FHBX (26 SCI immobilières) et FHBX Balthazar, où une masse d'offres a été déposée puis rejetée ou laissée en attente. Le « 5 % » reflète la nature du dossier (immobilier SCI, faible taux d'attribution), pas une sévérité de l'AJ.
- **Sandra Beladjine à 64 % de retenue** : repose sur **3 dossiers uniques seulement** (dont le dossier 34 qui pèse 8 des 14 offres). Effet de méga-dossier identique à LEXCAP. Non interprétable comme un biais d'AJ.
- **Marine PACE** est le seul AJ avec une vraie diversité (51 offres réparties sur 13 dossiers uniques) : son taux de 35,3 % est statistiquement indistinguable du taux de référence (p = 0,49). C'est le résultat le plus fiable de la section, et il dit qu'il n'y a **pas de biais détectable**.

**Conclusion analyse 4 : pas de biais d'AJ exploitable.** Les écarts apparents sont entièrement explicables par la composition en méga-dossiers (un AJ = souvent un gros dossier). L'hypothèse du livrable 10 section 9 point 2 ne peut pas être tranchée : il faudrait un corpus où chaque AJ apparaît sur 10+ dossiers indépendants de tailles comparables.

## 5. Délai v1 vers v2 des offres améliorées puis retenues

Sur les **42 offres** marquées `amelioree_puis_retenue`, mesure du délai entre le premier et le dernier dépôt daté du même repreneur sur le même dossier (champ `date_offre` du master CSV). **23 paires v1 vers v2 datées exploitables** (les autres ont des dates v1 et v2 identiques ou manquantes dans le master).

| Statistique | Valeur |
|---|---|
| n paires datées | 23 (sur 42 offres améliorées) |
| Délai médian v1 vers v2 | **26 jours** |
| P25 / P75 | 21 jours / 38 jours |
| Min / Max | 11 jours / 93 jours |

**Lecture opérationnelle pour le calendrier Brantham.** Quand le tribunal ou l'AJ invite un repreneur à améliorer son offre, le repreneur dispose typiquement de **3 à 5,5 semaines** (intervalle interquartile 21 à 38 jours) pour produire une v2. La médiane de 26 jours est cohérente avec un calendrier d'audiences à intervalle mensuel. Conséquence pratique : un repreneur accompagné par Brantham doit pouvoir mobiliser en moins de 3 semaines une attestation bancaire actualisée, un BP révisé et une lettre de soutien, c'est-à-dire **anticiper ces pièces dès la v1**. Le délai minimum observé (11 jours) montre que certains dossiers se rejouent très vite : la réactivité documentaire est un avantage concurrentiel.

**Limite.** n=23 sur 42, et le master CSV ne distingue pas toujours proprement les dates v1 et v2. Le chiffre est un ordre de grandeur fiable, pas une mesure de précision. Le délai réel « invitation du tribunal vers dépôt v2 » serait plus court que le délai « dépôt v1 vers dépôt v2 » mesuré ici, puisque l'invitation arrive après la v1.

## 6. Contre-vérification de la grille /100 par apprentissage automatique

Objectif : vérifier que la grille expert (livrable 08) n'a pas raté un prédicteur évident. **Ce n'est PAS un remplacement de la grille.** Le rapport n/features est de 5 (154 observations, 30 features), insuffisant pour un modèle prédictif fiable : le risque d'overfit est documenté au livrable 10 section 8.1 et reste entier ici. L'exercice sert uniquement de garde-fou.

Deux modèles, validation croisée stratifiée 5 plis :

| Modèle | Accuracy CV | AUC CV |
|---|---|---|
| Baseline (classe majoritaire) | 0,695 | 0,500 |
| Arbre de décision (profondeur 3) | 0,740 (± 0,057) | 0,807 |
| Régression logistique L2 (C=0,5) | **0,812 (± 0,077)** | **0,888** |

### 6.1 Variables retenues spontanément par les modèles

**Arbre de décision, importance des variables (top 6) :** `declaration_L642_3_signee` (0,43), `nb_cs` (0,16), `personnalisation_etude_contrats` (0,14), `annexes_kbis` (0,11), `prix_total` (0,09), `qualite_claire` (0,08).

**Régression logistique, top 10 |coefficient| :** `qualite_claire` (+1,12), `personnalisation_visite_site` (-0,99), `capacite_fin_forte` (+0,78), `nb_concurrents` (-0,65), `pct_reprise` (+0,65), `soutien_banques_historiques` (+0,63), `kbis_en_annexe` (+0,58), `personnalisation_etude_contrats` (+0,58), `paiement_comptant` (-0,57), `declaration_L642_3_signee` (+0,53).

### 6.2 Recoupement avec la grille 08

**Variables ML de tête qui recoupent la grille 08 (10 sur 13) :** `annexes_kbis`, `capacite_fin_forte`, `declaration_L642_3_signee`, `kbis_en_annexe`, `nb_cs`, `paiement_comptant`, `pct_reprise`, `personnalisation_etude_contrats`, `qualite_claire`, `soutien_banques_historiques`. La grille expert capte bien le coeur du signal : les variables que les modèles jugent les plus prédictives sont presque toutes déjà pondérées.

**Variables ML de tête HORS grille 08 (3) :** `nb_concurrents`, `personnalisation_visite_site`, `prix_total`.

- `nb_concurrents` (coefficient -0,65) : le nombre de concurrents n'est pas une caractéristique de l'offre mais du dossier. Il est non actionnable par un repreneur, donc légitimement absent d'une grille de scoring d'offre. À noter pour le **scoring de dossier** en amont (un dossier à 3 concurrents est plus accessible qu'un dossier à 6).
- `personnalisation_visite_site` apparaît avec un coefficient **négatif** (-0,99) dans la régression, ce qui est contre-intuitif et probablement un artefact de colinéarité avec `personnalisation_etude_contrats` (les deux variables de personnalisation se chevauchent ; le modèle régularisé reporte le poids sur l'une et inverse l'autre). À ne pas sur-interpréter. La grille 08 a raison de pondérer la visite de site positivement (G.2, 1 point).
- `prix_total` ressort dans l'arbre (importance 0,09) alors que la section 1 montre qu'il n'est PAS significatif (p = 0,94). C'est un cas d'école d'**overfit** : l'arbre exploite une coupure de prix qui sépare le jeu d'entraînement par hasard. À ignorer.

### 6.3 Verdict sur la grille 08

**La grille expert n'a pas raté de prédicteur évident.** Aucune variable hors grille ne survit à l'examen : `nb_concurrents` n'est pas actionnable, `personnalisation_visite_site` est un artefact de colinéarité, `prix_total` est de l'overfit confirmé par le test formel de la section 1. La grille capte le signal.

**En revanche, deux variables pondérées dans la grille 08 sont fragilisées par la section 1** : `exec_summary` (bloc F.2) et `faculte_substitution_precise` (bloc E.6) ne sont pas significatives (p = 0,11 et p = 0,14). Recommandation : ces deux critères pèsent 1 point chacun et peuvent rester dans la grille comme bonnes pratiques de forme, mais leur pondération ne doit pas être augmentée et le livrable 08 gagnerait à signaler qu'elles relèvent du confort de lecture, pas du pouvoir discriminant prouvé. Le `bp_3ans_present` (bloc C.3, 4 points) est lui aussi non significatif en isolé (p = 0,11) : ce qui compte n'est pas la présence du BP mais la qualité de ses hypothèses (`hypotheses_prudentes`, p = 7e-06, très significatif). La pondération du bloc C devrait être déplacée du critère « BP présent » vers le critère « hypothèses qualifiées ».

L'accuracy CV de la régression (0,81) est cohérente avec la fiabilité de 75 à 80 % annoncée pour la grille au livrable 10 section 11. Mais avec un écart-type CV de 0,077 et un n de 154, cette accuracy est elle-même incertaine à plus ou moins 8 points. **Le modèle ML ne doit pas être déployé en production** : il sert uniquement à confirmer que la grille additive transparente est un bon choix.

## 7. Synthèse des six analyses

| # | Analyse | Résultat | Exploitable ? |
|---|---|---|---|
| 1 | Tests formels | 39/53 variables significatives ; 6 deltas du livrable 02 sont du bruit | OUI, conclusions désormais validées |
| 2 | Réplication sous-corpus fiable | Les 11 deltas de tête tiennent (écart < 3,7 pts) | OUI, robustesse confirmée |
| 3 | Cabinet d'avocats | Artefact de méga-dossier (LEXCAP/FIDAL = 1 seul bloc) | NON, demande données neuves |
| 4 | Administrateur judiciaire | Pas de biais détectable (PACE p=0,49) ; écarts = méga-dossiers | NON, demande données neuves |
| 5 | Délai v1 vers v2 | Médiane 26 jours, IQR 21 à 38 jours (n=23) | OUI, ordre de grandeur fiable |
| 6 | Contre-vérification grille | Grille validée ; 2 critères à dé-pondérer (exec_summary, faculté substitution) | OUI, ajustement mineur recommandé |

## 8. Recommandations d'ajustement

1. **Mettre à jour le livrable 02** : ajouter une colonne p-value au tableau de la section 1, et signaler explicitement les 6 variables non significatives (`incorporels`, `corporels`, `bp_3ans_present`, `exec_summary`, `faculte_substitution_precise`, `L642_12_al4`).
2. **Mettre à jour le livrable 08** : signaler que `exec_summary` (F.2) et `faculte_substitution_precise` (E.6) sont des critères de forme non prouvés discriminants ; déplacer le poids du bloc C de « BP présent » vers « hypothèses prudentes ».
3. **Créer un scoring de dossier distinct du scoring d'offre** : `nb_concurrents` est un fort prédicteur mais non actionnable au niveau de l'offre ; il appartient à un score amont de sélection des dossiers à travailler.
4. **Calendrier Brantham** : intégrer la fenêtre médiane de 26 jours (3 à 5,5 semaines) entre v1 et v2 dans les rétroplannings d'accompagnement repreneur.
5. **Ne pas relancer** les analyses cabinet et AJ sur ce corpus : elles sont structurellement non concluantes ici (voir section verdict).

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/_INDEX]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/02-anatomie-winners-vs-losers]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/03-hierarchie-criteres-tribunal]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/08-grille-scoring-100pts]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/10-angles-morts]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/_index]]

## Verdict : reste-t-il quelque chose à presser ?

Après ce passage, le corpus actuel (566 offres, 154 décidées) est **statistiquement épuisé**. Ce qui est désormais clos : la hiérarchie des prédicteurs est testée et validée (39 variables significatives, 6 deltas du livrable 02 démasqués comme bruit) ; la robustesse est confirmée par réplication sur le sous-corpus fiable ; la grille /100 est contre-vérifiée par deux modèles ML et tient, à deux dé-pondérations mineures près ; le délai v1 vers v2 est mesuré (médiane 26 jours). Il ne reste aucune analyse intra-corpus à forte valeur.

Trois questions resteront sans réponse tant qu'on n'injecte pas de **donnée externe** : (1) le **cabinet d'avocats** et (2) l'**administrateur judiciaire** ne sont pas testables ici, car le corpus est dominé par des méga-dossiers qui confondent l'identité du cabinet/AJ avec celle du dossier ; il faudrait un corpus multi-tribunaux où chaque acteur apparaît sur 10+ dossiers indépendants. (3) Aucun **suivi post-cession** n'est possible : le corpus capte la promesse, pas l'exécution. Les seules sources qui débloqueraient le corpus sont : les **385 audiences en attente** (printemps-automne 2026, qui feront passer le n décidé de 154 à 200-300), le **suivi à 12-24 mois** des 7 winners confirmés, et un corpus d'**autres tribunaux** (Lyon, Lille, Nanterre) pour tester la généralisation hors TAE Paris. Sans cela, on a tout sorti.
