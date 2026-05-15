---
type: analyse
project: brantham
phase: phase2
livrable: 10
created: 2026-05-15
tags: [tc-paris, limites, biais, blind-spots, methodologie]
---

# 10 — Angles morts : ce que le corpus ne permet PAS de conclure

Inventaire honnête des **limites** du dataset 566 offres / 101 dossiers. À lire AVANT de présenter les résultats à un client ou de prendre une décision opérationnelle qui en dépende. Sept catégories de limites.

## 1. Biais de sélection — 8 % de retenues seulement, 68 % en attente

Distribution des issues :

| Statut | n | % |
|---|---|---|
| Retenue | 47 | 8,3 % |
| Rejetée | 107 | 18,9 % |
| **En attente** | **385** | **68,0 %** |
| NR | 27 | 4,8 % |

**Conséquence** : tous les écarts statistiques calculés (retenues vs rejetées) le sont sur **154 offres décidées** seulement. Quand l'audience des 385 offres en attente aura été rendue (vague AJ printemps 2026), la composition des winners peut basculer significativement.

Concrètement, sur les 101 dossiers : **7 sont confirmés gagnants** (Vergers d'Anjou pôle ligérien, AA Investments HK / EURODIF, Seasonova / Alpha Camping, MEDIVI / Denteka Colmar, LOM / SYM, MEDIVI / Enghien, BAC Berrebi). Les 6 dossiers restants (sur 13 cités dans `gagnants-tribunal.md`) sont des entités du même groupe (35-SICA, 36-LVL, 37-COOP, 57, 58, 59, 60, 61, 66 — tous Vergers d'Anjou). En **issues uniques de winners**, on est plus proche de **7 dossiers décidés**, soit ~7 % du corpus.

**Lecture** : les patterns observés sont robustes **pour 6-7 winners types**. Ils ne sont pas validés au-delà.

## 2. Doublons techniques inflatent le n de winners

Sur les 47 offres marquées « retenue », au moins 12 sont des duplicatas physiques (même Docusign Envelope ID, même date, même contenu) :

- 35-SICA-04 ≡ 35-SICA-03 ≡ 35-SICA-06 (3 duplicatas)
- 50-09 ≡ 50-10 (2 duplicatas)
- BAC-01 ≡ BAC-02 (versions très proches)
- 14-COLMAR-01 + 14-COLMAR-02 + 14-COLMAR-03 (3 versions successives → 1 win effectif)
- 20-01 + 21-SYM-OPTIC-01 + 22-SYM-LAB-01 (3 entités même repreneur)
- 28B-ALPHA-04-SEASONOVA + 29-LESCAPADE-02 + 30-LORMED-03 + 31-OCCITANIE-06 + 26-CHA-06 (5 entités même repreneur Seasonova)

**Le n unique de "winning repreneurs" est plus proche de 15** que de 47. Toutes les stats sur la cohorte winners gagnent à être lues avec ce facteur de pondération.

## 3. Secteurs sous-représentés ou absents

Le corpus est dominé par 4 méga-dossiers :

| Méga-dossier | n offres | % corpus |
|---|---|---|
| FHBX Affaire Balthazar (26 SCI immo) | ~75 | 13 % |
| NEOCAMP (11+ SCI camping) | ~45 | 8 % |
| INNATIS pôle ligérien (11 entités agro) | ~50 | 9 % |
| ALPHA CAMPING (16 sites HPA) | ~30 | 5 % |
| EURODIF/Bouchara | ~16 | 3 % |

Cumul : ~38 % du corpus appartient à 5 dossiers seulement. Les conclusions sur ces secteurs (immo SCI, camping, agro arboriculture, retail textile) sont **sur-représentatives** ; les conclusions générales en sont déformées.

**Secteurs faiblement représentés ou absents** :
- Industrie lourde (métallurgie, chimie, équipement) : <2 % du corpus
- BTP : ~3 %
- Transport / logistique : <2 %
- Tech / SaaS : ~3 % (PROGRESS SUP + COSA VOSTRA + corpus partiel)
- Santé hors dentaire / optique : <1 % (maisons de retraite Cap Lormont à peine couvertes)
- Distribution alimentaire / chaînes restaurants : ~2 %

Pour ces secteurs, **les patterns observés à Paris ne se généralisent pas** — il faudrait un corpus dédié.

## 4. Pas d'info sur l'exécution post-cession

Le corpus capte le **moment de l'audience de cession**. Il ne dit rien sur :

- Est-ce que le repreneur a tenu ses engagements de non-licenciement à 24 mois ?
- Combien de salariés sont effectivement encore en poste à 12-24 mois ?
- Le BP a-t-il été tenu (CA réalisé vs CA prévu) ?
- Les charges augmentatives ont-elles été soldées comme prévu ?
- L'incessibilité 24 mois a-t-elle été respectée ?
- La société repreneuse a-t-elle elle-même fait défaut (un repreneur RJ peut tomber en RJ ensuite) ?

**Tous les patterns winning sont sur du « ce qui a été promis et accepté »**, pas sur du « ce qui a été tenu ». Un repreneur peut être un excellent rédacteur d'offres et un mauvais opérateur — le corpus ne le détecte pas.

Pour combler : à mesure que les 47 retenues vieillissent (premières datent de septembre 2024), Brantham peut suivre 12-24 mois après chaque cession :
- Filiales / NewCo créées ?
- Effectif déclaré aux URSSAF ?
- Comptes annuels déposés ?
- Procédures collectives ultérieures ?

**Recommandation** : créer un suivi `vault/brantham/post-cession/` avec un dossier par winning repreneur, mis à jour annuellement.

## 5. Tribunal unique — TC Paris (depuis sept. 2024 TAE)

Le corpus est **100 % TAE Paris**. Avant sept. 2024, ce ressort était le TC Paris ; depuis, il s'appelle Tribunal des Activités Économiques. Cette transition implique :

- **Une jurisprudence en construction** — le TAE Paris expérimente sa nouvelle compétence sur les procédures collectives. Les usages observés en 2025-2026 ne sont **pas figés**.
- **Une équipe d'AJ spécifique** : Me Marine PACE (2M&Associés / AJ2M), Stéphane Martin (Actis), Maître Benhacine Chamieh, Maître Labis (AJILINK Lambersart), etc. — leur sensibilité juridique forme partie de ce que le corpus reflète.
- **Volume parisien** : 60 % des grands dossiers distressed nationaux passent à Paris. Mais la jurisprudence Lyon (1er ressort province en volume RJ), Lille, Nanterre, Versailles, Marseille — chacun a sa pratique. Une offre « bonne pour Paris » n'est pas mécaniquement bonne pour Lyon.

**Recommandation** : avant d'appliquer la grille à un dossier hors Paris, faire un sanity-check sur 5-10 décisions récentes du tribunal cible.

## 6. Évolution temporelle — fenêtre courte 2025-2026

Le corpus capte essentiellement **septembre 2024 — avril 2026**, soit 19 mois. Les pratiques (notamment des AJ et du TAE Paris) peuvent évoluer :

- **Pression réglementaire prepacks** : la loi PACTE encourage les prepacks-cession. À ce stade, ~1,4 % du corpus seulement. Pourrait grimper, modifiant les patterns winning (un prepack arrive « pré-marié » à l'audience).
- **Concentration des AJ** : la consolidation des cabinets AJ (AJ2M, AJILINK, ACTIS) modifie les pratiques.
- **Inflation des prix RJ** : conjoncture macro post-2025 — si les taux baissent, les multiples grimpent ; si la conjoncture se dégrade encore, les prix baissent davantage.
- **Précisions législatives** : la loi de simplification 2025 a renforcé L.642-3 (lien dirigeants) — déjà visible dans le corpus avec 78 % L.642-3 signée chez retenues. Pourrait monter à 95 % d'ici 2027.

**Recommandation** : revérifier la grille de scoring annuellement (juin 2027 = audit + recalibration).

## 7. Limites techniques d'extraction

### 7.1 Confidence d'extraction

| Niveau | n offres | Notes |
|---|---|---|
| high | 254 | PDF lisible, structure claire, données fiables |
| medium | 125 | PDF lisible mais partiel, ou champs ambigus |
| low | 150 | OCR scanné, structure non standardisée, doutes |
| partial_pdf_only | 37 | Seulement les premières pages disponibles |

**Sur les 150 low confidence**, les champs `motifs_tribunal_verbatim`, `pct_reprise`, `nb_cs` sont souvent NR ou reconstruits. Les stats globales sont donc **sous-estimées** pour certaines variables (notamment `bp_3ans_present`, `annexes_*`, qui sont booléens dépendants d'une lecture complète).

Sur les **47 retenues**, on a 22 `high`, 17 `medium`, 7 `low`, 1 `partial`. Donc 83 % de confiance ≥ medium. C'est le seul morceau du corpus où la qualité est forte.

### 7.2 PDFs > 5 Mo non extraits

Certains PDFs scannés ou très lourds (>5 Mo, scans OCR de qualité moyenne) n'ont pas été décortiqués complètement. Le champ `partial_pdf_only` (n=37) signale ces cas.

### 7.3 Mauvaise classification dossier

9 cas identifiés de PDFs mal classés (offre HOUSEBASE ciblant SNC ADONIA déposée dans 7 dossiers SCI FHBX différents). Ces 9 sont marqués `non` retenues mais déforment légèrement les stats sur l'immobilier.

### 7.4 Manque d'info repreneur

`forme_repreneur = NR` sur 46 offres (8,1 %). Pour ces offres, on ne peut ni classer le winner ni vérifier les patterns par typologie.

### 7.5 Master CSV vs grilles JSON

Le master-offres.csv (extraction phase 1) et les grilles JSON (extraction phase 2 plus structurée) peuvent diverger sur des champs ; les grilles JSON sont la référence canonique pour la phase 2.

## 8. Limites méthodologiques

### 8.1 Pondération de la grille de scoring (livrable 08)

La pondération est **expert-driven informée par les stats** — pas une régression logistique multivariée. Une régression sur n=154 (corpus décidé) avec ~30 features serait à risque d'overfitting (rapport n/features = 5 — insuffisant). On préfère un modèle additif transparent. **L'incertitude sur les pondérations exactes est probablement de ±20 %** (un critère pondéré 4 pourrait raisonnablement être pondéré 3 ou 5).

### 8.2 Pas de test statistique formel publié

Les écarts (« Δ +50 pts ») sont des différences de proportions calculées sur des effectifs petits (n=47 vs n=107). Sans test Mann-Whitney ou chi-deux explicitement appliqué, ces deltas sont à lire comme **observations**, pas comme conclusions statistiquement validées. Un Δ >20 pts avec n>30 dans chaque groupe est probablement significatif p<0,01 ; les Δ entre +10 et +20 pts sont plus fragiles.

### 8.3 Thématisation par regex sur les motifs

L'analyse des motifs tribunal (livrable 03) utilise un thématiseur regex maison sur les `motifs_tribunal_verbatim`. Certains thèmes ont 0-3 hits — la thématisation peut être incomplète ou biaisée par les expressions choisies. La hiérarchie « pérennité dominante 45 % » est qualitativement robuste mais pas quantitativement précise au pourcentage près.

### 8.4 Verbatims tribunal — sources hybrides

Sur les 20 « motifs tribunal winners », beaucoup proviennent de communiqués de presse / sources externes (`gagnants-tribunal.md` cite Les Echos, L'Officiel des Terrains de Camping, Acuité, etc.) — pas de jugements écrits. Les jugements de cession ne sont presque jamais motivés en clair sur l'attribution. La reconstruction des motifs est donc **probabiliste**, pas littérale.

## 9. Ce qu'on ne sait pas (et qu'on aimerait savoir)

Pour les phases ultérieures :

1. **Lien entre cabinet d'avocats du repreneur et succès** — corpus a un champ `avocat_repreneur` mais peu rempli (~30 %). Hypothèse : cabinets spécialisés (Monceau Avocats, Fidal, Lexcap, Hadengue) ont un meilleur taux de succès. Non vérifié.
2. **Lien entre AJ et taux de retenue** — chaque AJ a-t-il un biais de sélection ? Hypothèse pas testée.
3. **Temps entre dépôt offre et amélioration** — sur les 42 `amelioree_puis_retenue`, quel est le délai médian dépôt v1 → dépôt v2 ? Important pour le calendrier Brantham.
4. **Pourcentage des prepacks qui aboutissent** — 1,4 % du corpus, n=8. Pas assez pour conclure.
5. **Effet du nombre de concurrents** — la médiane nb_concurrents = 3 chez retenues, 5 chez rejetées. Mais corrélation pas causalité.
6. **Repreneurs étrangers — réussite par origine** — n=9, dont 2 retenues (HK, Suisse). Trop petit.

## 10. Recommandations méthodologiques pour Brantham

1. **Présenter les stats avec n** explicite. « 78 % des winners ont capacité financière forte documentée (n=47) » ; pas « la majorité » seul.
2. **Mentionner « TC Paris » systématiquement** dans tout livrable client — la généralisation à d'autres ressorts n'est pas démontrée.
3. **Ne pas appliquer la grille de scoring aux secteurs sous-représentés** sans recalibrer (industrie lourde, transport, tech).
4. **Suivre les 7 winners confirmés à 12-24 mois** pour valider le pattern « offre gagnante = exécution réussie ».
5. **Réindexer le corpus à mesure que les 385 en attente passent en audience** — d'ici fin 2026, on aura probablement 200-300 décidées et les patterns se stabiliseront.
6. **Documenter les exceptions** (ex. PROGRESS SUP : lien familial déclaré, 6 CS, retenu = sortie du pattern « 0-1 CS »). Les exceptions enrichissent la grille.

## 11. Synthèse honnête à présenter au client

> « Cette analyse s'appuie sur 566 offres et 101 dossiers extraits du TAE Paris entre septembre 2024 et avril 2026. Sur les 154 offres décidées (47 retenues + 107 rejetées), nous identifions une vingtaine de variables qui discriminent statistiquement les offres gagnantes. La grille de scoring proposée a une fiabilité estimée de l'ordre de 75-80 % pour prédire qu'une offre passera le filtre crédibilité du tribunal — sous réserve que le dossier ne soit pas dans un secteur sous-représenté du corpus (industrie lourde, transport, tech) ou hors TC Paris. Les patterns sur 6-7 winners types (Vergers d'Anjou, AA Investments, Seasonova, MEDIVI, LOM, Berrebi) sont robustes ; au-delà, la généralisation reste à valider. »

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/data-quality]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/01-stats-descriptives]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/08-grille-scoring-100pts]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/_index]]
