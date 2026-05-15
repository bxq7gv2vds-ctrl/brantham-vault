---
type: session
project: brantham
date: 2026-05-15
duration: ~6h
tags: [tc-paris, extraction, deal-intel, scraping, ml-corpus, scoring, playbook]
---

# Session 2026-05-15 — TC Paris : extraction complète, analyse + grille de scoring

Session marathon de ~6h. Construction d'un dataset complet d'offres de reprise au Tribunal des Activités Économiques de Paris + analyse transversale + grille de scoring /100 pour évaluer une offre AVANT dépôt.

## Récap chronologique

### Phase 0 — Audit de l'existant
- Identifié 94 dossiers déjà extraits dans `/Users/paul/Downloads/Dossiers Entreprises/` (vague 1, fin avril)
- 35 dossiers avec `offres.csv` rempli, 59 non analysés
- Décision : compléter les 59 manquants

### Phase 1A — Extraction vague 1 (94 dossiers)
- 23 vagues d'agents parallèles
- Lecture systématique de ~300 PDFs (offres de reprise)
- Extraction structurée selon le template `PROMPT_EXTRACTION_OFFRES.md` du dossier COSA
- Output : 94 × `offres.csv` + 94 × `dossiers.csv` (94 folders)

### Phase 1B — Consolidation dans vault
- Création `vault/brantham/tc-paris-extraction/`
- Script `_merge.py` : agrège tous les CSV individuels
- `master-offres.csv` (570 lignes, 30 colonnes)
- `master-dossiers.csv` (107 lignes, 24 colonnes)
- `raw-csv/` : archive des 208 CSVs individuels

### Phase 1C — Vague 2 : scraping site Greffe TAE Paris
- Source : `https://ow-offres-de-reprises.greffe-tae-paris.fr/`
- Mécanisme découvert : POST `/fr/download` avec `{co, gd}` → redirect vers PDF
- Script `_scrape_tc_paris.py` automatique
- 11 nouveaux dossiers identifiés par diff avec vague 1 (MINELLI, PETRUS, MGL, DIGITAL COLLEGE, AXIOVAL, ARANA FACILITIES, FAIRSPACE, ARLO, DES PLANCHES, SCOOT PARIS 16, TEHTRI)
- 25 PDFs téléchargés (TEHTRI = "en cours de numérisation")
- 10 dossiers extraits → +25 offres dans master CSV

### Phase 1D — 8 analyses thématiques
1. [[brantham/tc-paris-extraction/analyses/gagnants-tribunal|gagnants-tribunal]] — Recherche BODACC/presse sur 11 dossiers → 7 gagnants confirmés (COSA→Agence IF, INNATIS→Vergers d'Anjou 7M€, NEOCAMP→Seasonova+Maeva, SYM→LOM, EURODIF→AA Investments HK, MINELLI→liquidation)
2. [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes|decortique-offres-gagnantes]] — Lecture intégrale PDFs gagnants vs perdants COSA/INNATIS/EURODIF (5500 mots avec verbatims)
3. [[brantham/tc-paris-extraction/analyses/playbook-redaction-offre|playbook-redaction-offre]] — V1 du playbook rédactionnel (13 sections, règles confirmées par jugements)
4. [[brantham/tc-paris-extraction/analyses/audiences-acces-information|audiences-acces-information]] — Audiences NON enregistrées en France, 5 canaux d'intel post-jugement
5. [[brantham/tc-paris-extraction/analyses/repreneurs-recurrents|repreneurs-recurrents]] — MUVICO 26 dossiers, HOUSEBASE 16, VERDOSO 18, LABRAX 16, JADO 10 (foncières immo)
6. [[brantham/tc-paris-extraction/analyses/groupes-distressed|groupes-distressed]] — 6 clusters multi-entités (INNATIS 11, NEOCAMP 8, DENTEKA 3, SYM 3, COLLEGE DE PARIS 49 filiales, SEGI)
7. [[brantham/tc-paris-extraction/analyses/vague-2026-05-15|vague-2026-05-15]] — Vague 2 : 11 nouveaux dossiers
8. [[brantham/tc-paris-extraction/analyses/data-quality|data-quality]] — Doublons MD5, OCR à refaire, normalisation

### Phase 1E — Grilles JSON structurées (566 offres × ~80 champs)
- Schéma JSON strict : `_schema.json` (12 sections : identification, issue, profil_repreneur, structure_prix, reprise_passif, volet_social, plan_industriel, financement, engagements_specifiques, conditions_suspensives, forme_presentation, signaux_faibles, extraits_remarquables)
- 23 batches d'agents parallèles
- Output : 566 grilles offres + 101 grilles dossiers + 23 logs batch
- Confidence : 67% high+medium, 33% low+partial_pdf_only

### Phase 2 — Synthèse transversale (10 livrables)
Folder `analyses/synthese-phase2/` :
1. `01-stats-descriptives.md` — distributions secteur/taille/procédure/repreneur/prix
2. `02-anatomie-winners-vs-losers.md` — 50+ variables comparées 47 retenues vs 107 rejetées
3. `03-hierarchie-criteres-tribunal.md` — motifs hiérarchisés (pérennité 45% dominante)
4. `04-portraits-robots-typologie.md` — 6 typologies (retail multi-sites, industriel <50, B2B, tech, réglementé, foncière)
5. `05-recettes-rhetoriques-structure.md` — longueur médiane 13,5 p, sommaire, ton mixte
6. `06-pieges-recurrents-rejetees.md` — top 15 défauts + 5 kill-switches absolus
7. `07-signaux-credibilite-tribunal.md` — 24 signaux Tier S/A/B/C
8. **`08-grille-scoring-100pts.md` ⭐** — 32 critères calibrés pour scorer une offre avant dépôt
9. `09-bibliotheque-extraits.md` — verbatims gagnants par section
10. `10-angles-morts.md` — 7 catégories de limites du corpus

Scripts Python rejouables : `_run_analysis.py`, `_compute_stats.py`, `_compute_motifs.py`, `_extracts_winners.py` + pickles intermédiaires + `stats_report.json`.

## 3 insights majeurs émergents

1. **Le prix médian ne discrimine PAS** les offres retenues vs rejetées (50 k€ médian = 50 k€ médian). Ce qui discrimine, c'est la **structure, l'absence de CS, la documentation du financement**.

2. **La preuve de due diligence = prédicteur n°1** : Δ **+50,3 pts** entre retenues (77%) et rejetées (27%) sur "le repreneur a-t-il documenté son étude des contrats clients/fournisseurs ?"

3. **5 kill-switches absolus** présents dans **0 offre retenue** :
   - Périmètre marginal / cherry-picking sur multi-sites
   - Indivisibilité "château de cartes"
   - Clause non-sollicitation hostile envers fondateurs (cas DataSolution/COSA)
   - Charges augmentatives masquées
   - Promesses renvoyées à "ultérieurement" (financement, ventilation, BP)

## Règles d'arbitrage du tribunal — confirmées (7 cas tracés)

1. **Repreneur sectoriel stratégique + continuité d'emploi > prix le plus haut** (COSA, SYM, INNATIS)
2. **Offres partielles cherry-picking sans engagement global = LIQUIDATION** (cas MINELLI iconique, 21 boutiques fermées 30/05)
3. **Démantèlement multi-repreneurs accepté si lots cohérents** (NEOCAMP = Seasonova 15 sites + Maeva franchises)
4. **Engagement social TOTAL > ratio prix/emploi mécanique** (médiane prix/emploi 10k€ mais variable selon contexte)
5. **Profil repreneur récurrent = signal positif** (AA Investments HK : Bouchara + EURODIF + Bonne Gueule)
6. **Délai DLDO → Jugement ~6 semaines** (planning)
7. **Repreneur asiatique sur retail mode FR = pattern émergent** (AA Investments HK cible pipeline outreach)

## Patterns observés sur 566 offres

### Profils repreneurs
- Société existante industriel : 314 (55%)
- Holding ad hoc : 51 (9%)
- Société existante concurrent : 37
- Family office : 34 (foncier)
- PP seule : 28
- Fonds PE : 18
- Association/collectivité : 14
- Repreneur étranger : 9
- Dirigeant historique : 11

### Clusters corporate (groupes en RJ)
- INNATIS Val de Loire (arboriculture pomme) : 11 entités, gagnant Vergers d'Anjou 7M€
- NEOCAMP (camping) : 8 entités, gagnants Seasonova + Maeva
- COLLEGE DE PARIS (EdTech) : 49 filiales, 1390 collab, en attente
- FHBX Affaire Balthazar (foncières Melot-Gouband) : 26 entités, MUVICO/LABRAX/VERDOSO récurrents
- DENTEKA (dentaire) : 3 sites, MEDIVI escalade 4 versions
- SYM Group (optique) : 3 entités, gagnant LOM
- SEGI : foncière immo Paris, 19 offres 4-25 M€

## Repreneurs récurrents (pipeline outreach Brantham)

### Foncières immo Paris
- MUVICO : 26 dossiers (foncière acquéreuse systématique SCI/SNC immo IDF)
- HOUSEBASE : 16
- VERDOSO SAS : 18 (fonds investissement retournement)
- LABRAX INVEST : 16 (gros tickets 21M€)
- GROUPE JADO : 10
- AEB INVEST : 9
- GROUPE LALEYE : 4
- CORTONA FRANCE : 3

### Sectoriels
- FEMINA STYL + MARENGO : 6 dossiers camping (famille Hublé/Wajsbrot)
- GROUPE SEASONOVA : 6 (lots cohérents)
- CAMPALDIA / SLBC PERON : 6 (offres symboliques 3€)
- HPA MEDITERRANEO : 3 camping
- SARL CELHER : 7 (arboriculture local)
- LES VERGERS D'ANJOU : 4 (coop locale)
- MEDIVI / Place Dentaire : 3 (centres dentaires)
- LOM Les Opticiens Mobiles : 3 (optique mobile)
- FINANCIERE DAUNOU 9 (Guillaume DE BOIS) : 3 dossiers restauration parisienne

### Profils étrangers émergents
- AA Investments (HK) Limited : Bouchara + EURODIF + Bonne Gueule + Smallable + Wethenew + L'Exception + Bazar Chic + Atlas For Men

## Workflow rejouable

```bash
# Détection nouvelles opportunités TC Paris
python3 /Users/paul/vault/brantham/tc-paris-extraction/_scrape_tc_paris.py

# Consolidation master CSV
python3 /Users/paul/vault/brantham/tc-paris-extraction/_merge.py

# Re-run analyses Phase 2 (quand offres en_attente passent en audience)
python3 /Users/paul/vault/brantham/tc-paris-extraction/analyses/synthese-phase2/_run_analysis.py

# Re-indexation QMD
qmd update && qmd embed
```

## Stats globales finales

- **104 dossiers** TC Paris (94 vague 1 + 10 vague 2)
- **570 offres** dans master CSV
- **566 grilles JSON** Phase 1
- **47 offres retenues** (oui + amelioree_puis_retenue)
- **107 offres rejetées**
- **385 offres en attente** (à actualiser quand audience)
- **6 clusters corporate** identifiés
- **30+ repreneurs récurrents** ≥2 dossiers (pipeline outreach)
- **~50 cabinets avocats récurrents** côté repreneur (FIDAL 22, LEXCAP 17, MONCEY 15, HADENGUE, MAC MAHON, PZ Avocats)

## Fichiers créés / modifiés

### Vault `/Users/paul/vault/brantham/tc-paris-extraction/`
- `_INDEX.md` — point d'entrée unique
- `_MOC.md` — MOC projet
- `_merge.py` — consolidation CSV
- `_scrape_tc_paris.py` — scraping Greffe TAE Paris
- `master-offres.csv` — 570 lignes
- `master-dossiers.csv` — 107 lignes
- `raw-csv/` — 208 CSV individuels
- `grilles/` (`_schema.json`, `_workflow.md`, `offres/` 566 JSONs, `dossiers/` 101 JSONs, `batches/` 23 logs)
- `analyses/` — 8 docs thématiques
- `analyses/synthese-phase2/` — 10 livrables + scripts + pickles + stats_report.json

### Downloads
- `/Users/paul/Downloads/Dossiers Entreprises/` — 94 dossiers vague 1 (PDFs + CSVs)
- `/Users/paul/Downloads/Dossiers Entreprises Nouveaux 2026-05-15/` — 11 dossiers vague 2

### MOC brantham
- Ajout section "Deal intel & datasets" dans `brantham/_MOC.md` pointant vers TC Paris

## Décisions prises

- **Décision 2026-05-15** : Adopter la grille de scoring /100 (`08-grille-scoring-100pts.md`) comme standard Brantham pour évaluer toute offre avant dépôt côté client repreneur.
- **Décision 2026-05-15** : Pipeline outreach prioritaire = 30 repreneurs récurrents identifiés (MUVICO, HOUSEBASE, VERDOSO, LABRAX, JADO, AEB, FEMINA STYL+MARENGO, CELHER, FINANCIERE DAUNOU 9, AA Investments HK).
- **Décision 2026-05-15** : Workflow scraping TC Paris à automatiser via cron quotidien (à mettre en place).

## Patterns identifiés à capturer

- Pattern "prix vitrine + capex affichage" (cas AJA — prix bas + enveloppe travaux 300k€)
- Pattern "compte de proxy" (Oaklen sur CSA, P E L sur SOPI utilisent les comptes d'une autre société du groupe pour justifier capacité)
- Pattern "passer du rejet MJ au plan retenu en 11 jours" (cas AXIOVAL FCL — 3 offres successives répondant aux observations MJ)
- Pattern "VERDOSO prix dégradé L.642-2 V" (technique juridique 9 998 €/SCI)
- Pattern "escalade contrôlée sur observations tribunal" (MEDIVI sur DENTEKA, 4 versions [3]€ → 2 600 €)
- Pattern "BP 5 ans + storytelling humain" (Piccolo 5 sur LA BELLE FORÊT, 23k€ + 6 emplois)

## Anti-patterns confirmés (kill-switches)

1. Cherry-picking partiel sans cohérence globale → liquidation (MINELLI, 6 offres rejetées)
2. Clause non-sollicitation hostile envers fondateurs (DataSolution/COSA)
3. Promesses "ultérieurement" (financement, ventilation, BP) — CASTEL+LEROY+VCAPITAL sur INNATIS
4. Charges augmentatives masquées
5. Indivisibilité "château de cartes" (si une offre groupe tombe, tout tombe)
6. Conditions suspensives auto-contradictoires (QASTI sur DME)
7. Prix laissé en placeholders `[3]€`
8. Pas de track record distressed démontré

## Next steps (à confirmer avec user)

- [ ] Transformer la grille de scoring /100 en outil Notion/Excel remplissable par Soren
- [ ] Créer un template d'offre type intégrant les formulations gagnantes (de `09-bibliotheque-extraits.md`)
- [ ] Setup cron quotidien pour scraping TC Paris automatique
- [ ] Outreach les 30 repreneurs récurrents identifiés (CRM Brantham à mettre à jour)
- [ ] Demander jugements complets au greffe pour les 7 cas tracés (motivation détaillée du tribunal)
- [ ] Backfilling vague 1 : retrouver les gagnants des 38+ dossiers décidés mais non publics
- [ ] Élargir au TC Lyon, TC Bordeaux, TC Marseille pour comparaison inter-tribunaux
- [ ] Re-actualiser Phase 2 quand les 385 offres "en_attente" passent en audience

## Related

- [[brantham/tc-paris-extraction/_INDEX]]
- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/_index]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/08-grille-scoring-100pts]] ⭐
- [[brantham/tc-paris-extraction/analyses/playbook-redaction-offre]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/_MOC]]
- [[brantham/context/realite-business]]
- [[brantham/context/process-end-to-end]]
- [[brantham/patterns/onboarding-distressed-ma]]
- [[brantham/templates/lettre-de-mission]]
