---
type: batch-log
batch_id: 08
dossiers_traites: 5
offres_extraites: 27
date: 2026-05-15
agent: claude-agent-batch08
tags: [tc-paris, batch, extraction]
---

# Batch 08 — Dossiers 30-LORMED / 33-JEFFREY / 34-LPC / 37-VOLTAIRE / 38-URIOS

## Fichiers JSON créés

### Dossiers (5)
- `dossiers/30-LORMED.json` — LORMED (groupe NEOCAMP, camping Soleil d'Oc Narbonne)
- `dossiers/33-JEFFREY.json` — JEFFREY CAGNES PARIS (4 pâtisseries Paris/Levallois)
- `dossiers/34-LPC.json` — LPC (filière pommes Val de Loire INNATIS)
- `dossiers/37-VOLTAIRE.json` — VOLTAIRE (vélos électriques premium 4 boutiques)
- `dossiers/38-URIOS.json` — URIOS (information financière + recouvrement + logiciels, filiale DIOT-SIACI, prépack L611-7)

### Offres (27)
- LORMED : 30-LORMED-01 (HPA Mediterraneo, 300K€) / 02 (HOMAIR-ECG, 1,2M€ + 1,7M€ charges aug) / 03 (Seasonova lettre d'intention) / 04 (CAMPALDIA-PERON 3€ symbolique) / 05 (FEMINA STYL+MARENGO 1M€)
- JEFFREY : 33-JEFFREY-01 (PARIS-BREST 60K€) / 02 (JUCHHEIM Japon 700K€) / 03 (JOSETTE 75K€) / 04 (Cagnes+Schneider 30K€) / 05a (FAUCHON Montorgueil 17K€) / 05b (Maison Arnaud Larher Moines 10K€)
- LPC : 34-LPC-01 (CASTEL+LEROY+VCAPITAL amélioré 50K€) / 02 (LES VERGERS D'ANJOU 3M€) / 03 (GSF ligne agrumes 20K€) / 04 (doublon GSF) / 05 (CASTEL+LEROY initial 50K€)
- VOLTAIRE : 37-VOLTAIRE-01 (UTO/LION 50K€) / 02 (RE-CYCLES 10K€+compensation) / 03 (Amsterdam Air/Notus 27K€) / 04 (doublon 03) / 05 (triple doublon)
- URIOS : 38-URIOS-01 (YRCAM 600K€) / 02 (Reydellet+Loiseau 1€) / 03 (EPHRUSSI ex-dirigeants 150K€) / 04 (BLANDIN Pôle Logiciel 5K€) / 05 (GROUPE CFO 100K€)

## Anomalies détectées

1. **Doublons techniques** : 3 cas avérés
   - 34-LPC-03 et 34-LPC-04 — même Docusign envelope `79E2E104-8C9D-4609-8F02-D4928BF11AEE`, taille fichier identique 2672771 bytes
   - 37-VOLTAIRE-03/04/05 — TRIPLE doublon Docusign envelope `14E85F2C-F893-429F-AD8F-FF32A5A0ED53`
   → Probable double/triple dépôt au greffe par erreur ou copie de sauvegarde
2. **Offres collatérales / groupes liés** :
   - LORMED indivisible avec SCI C.H.A. / ALPHA CAMPING OCCITANIE / ESCAPADE / GRANDE LISSE / ILO (pôle foncier NEOCAMP)
   - LPC indivisible avec 10 autres structures pôle Val de Loire INNATIS
   - URIOS-03 EPHRUSSI complémentaire URIOS-04 BLANDIN (pôles Études+Recouvrement vs Logiciel)
3. **Compensation autoréférente** : 37-VOLTAIRE-02 RE-CYCLES achète VOLTAIRE pour 10K€ + compensation créance impayée 298K€ + stocks impayés 453K€ — conflit d'intérêt latent.
4. **Reprise par anciens dirigeants** : 38-URIOS-03 EPHRUSSI = ex-Président Monteiro + ex-DG Lobey-Monteiro (avaient cédé en 2022 à DIOT-SIACI). Sensibilité tribunal.
5. **Reprise par directeur de pôle** : 38-URIOS-04 BLANDIN = actuel Directeur Pôle Logiciel.
6. **Erreur typo** : 30-LORMED-05 indique "28 janvier 2025" au lieu de "28 janvier 2026" dans synthèse.
7. **Décomposition prix incohérente** : 34-LPC-01 page synthèse p3 = 50000€ vs détail p29 affiche total 45000€.
8. **CAMPALDIA prix 3€ symbolique** sur LORMED — sans charges augmentatives chiffrées. Position de négociation, pas offre crédible.
9. **Tableau effectifs incohérent JEFFREY-04** : 41 postes total mais 31 repris, ratios cherry-pick (6 vendeurs sur 9, 1 resp boutique sur 3).

## Issues confirmées (gagnants-tribunal.md)

- **34-LPC Innatis** : Les Vergers d'Anjou retenu (audience 30/04/2026, prix global pôle ligérien 7M€). Consortium CASTEL+LEROY+VCAPITAL écarté. Marque `34-LPC-02 cette_offre_retenue: "amelioree_puis_retenue"` et `34-LPC-01/05 cette_offre_retenue: "non"`.
- **30-LORMED Neocamp** : Seasonova retenu pour 15 sites Alpha Camping (audience 02/04/2026), Maeva pour franchises. FEMINA STYL+MARENGO/HOMAIR-ECG/CAMPALDIA écartés. Périmètre précis LORMED (foncier filiale ILO) non clairement détaillé dans communiqués — marqué `issue_globale_dossier: "plan_cession_arrete"` mais `cette_offre_retenue: "en_attente"` sauf Seasonova `amelioree_puis_retenue`.
- **33-JEFFREY** : pas dans gagnants. `en_attente`. DLDO 31/03/2026 — décision probable mi-mai 2026.
- **37-VOLTAIRE** : pas dans gagnants. `en_attente`. Pas de DLDO renseigné.
- **38-URIOS** : pas dans gagnants. `en_attente`. Prépack — décision rapide attendue.

## Champs où l'info manquait systématiquement

- `cible_siren` : présent dans 4 dossiers sur 5 (manque sur 33-JEFFREY confirmé via Pappers public)
- `date_audience_cession` : connue uniquement pour 34-LPC (30/04/2026)
- `juge_commissaire` : connu uniquement pour 30-LORMED (Franck MEYNAUD) et 34-LPC (WEHBI Joseph)
- `caution_dirigeant_*` : jamais mentionné
- `engagement_maintien_emplois_duree_mois` : jamais explicité
- `cautionnement_personnel` : presque toujours NR
- `nb_pages_total` : info non disponible sans ouvrir PDFs systématiquement (estimés sur la base de fichiers ouverts ou notes CSV)

## Patterns observés

1. **Prix symbolique avec charges augmentatives massives** : pattern récurrent sur deals industriels (HOMAIR 1,2M€ + 1,7M€ charges aug ; CAMPALDIA 3€ ; FEMINA STYL "à parfaire"). Tribunal regarde valeur économique globale.
2. **Offres complémentaires structurantes** : URIOS-03+04 (EPHRUSSI + BLANDIN se partagent Études/Recouvrement et Logiciel sans concurrence). Pattern intéressant pour deals multi-pôles.
3. **Anciens dirigeants en repreneurs** : Cagnes (33-04) + Monteiro/Lobey (URIOS-03) + Reydellet (URIOS-02) — récurrent dans dossiers tertiaire/services.
4. **Coopératives industrielles vs holdings privées** : LPC Vergers d'Anjou (coop 73 adhérents, 50M€ CA, 26M€ FP, soutien Crédit Agricole) bat consortium privé. Pattern "coopérative locale > fonds privé" pour filière agricole.
5. **Doublons Docusign multiples** : 3 offres / 27 = 11% de bruit technique dans le dataset. À filtrer en Phase 2.

## Suggestions amélioration schema

1. **Ajouter `offre_indivisible_avec`** : array d'`offre_id` liées (cas LORMED→SCI CHA / LPC→Innatis). Renforce le champ `groupe_dossiers_lies` du dossier mais côté offre.
2. **Ajouter `offre_complementaire_avec`** : pour URIOS-03/URIOS-04 qui se partagent les pôles sans concurrence.
3. **Ajouter `signaux_faibles.conflit_interet_dirigeant_creancier`** : booléen pour cas RE-CYCLES qui rachète VOLTAIRE (son débiteur).
4. **Ajouter `signaux_faibles.ex_dirigeant_societe_cible`** : booléen pour Monteiro/Lobey/Cagnes/Reydellet/Blandin.
5. **`structure_prix.prix_total_ECONOMIQUE_eur`** : déjà suggéré batch 01 — confirmé indispensable (cas HOMAIR 1,2M€ → 2,9M€ avec charges aug).
6. **`forme_presentation.doublon_technique_strict`** : booléen pour 3 cas batch 08.

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_01]]
