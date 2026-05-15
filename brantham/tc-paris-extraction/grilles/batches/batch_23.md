---
type: batch_log
project: brantham
batch: 23
created: 2026-05-15
tags: [tc-paris, extraction, batch, mega-dossiers]
---

# Batch 23 — MEGA DOSSIERS : SEGI (03) + COLLEGE DE PARIS (45)

## Dossiers traités

| Dossier | Folder | Nb offres extraites | Confidence |
|---|---|---|---|
| 03 | SEGI (foncière immo Paris 6e) | 19 | high (03-SEGI-02 Barings PDF lu) / medium (03-SEGI-04 à 19 via CSV verbatim très riche) / low (03-SEGI-11 et 03-SEGI-12 doublons) |
| 45 | COLLEGE DE PARIS (EdTech holding 32 établissements) | 26 | high (45-25 UPSTAIRS V3 PDF lu 15 pages) / medium (45-02/03/16/18/20/21/22/23/24/26 via CSV) / low (45-04/05/06/07/08/09/10/11/12/13/14/15/17/19 PDF non lus, doublons binaires ou fonctionnels) |

**Total : 45 offres + 2 fiches dossier = 47 JSONs écrits.**

## Issue : EN ATTENTE pour les 2 dossiers

Aucune source publique au 2026-05-15 sur jugements SEGI ou COLLEGE DE PARIS. SEGI DLDO 02/02/2026, audience probable Q2 2026. COLLEGE DLDO 10/04/2026, audience probable mai-juin 2026. À tracer post-audience via BODACC / Pappers / LinkedIn dirigeants (Galileo, Studialis, Novétude pour EdTech / Eternam, Emerige, Barings pour foncière).

## Clés SEGI (19 offres, 17 uniques après dédoublonnage)

**Fourchette prix** : 4,17 M€ (Huyghens partielle) à 25,2 M€ (Barings LOI). Cluster premium 20-22 M€ (Barings 25,2 / Trustone 25,05 / Eternam 22 / Herrmann 21 / PMV1 21 / Emerige 20,5 / BAM 20,5 / VPF 20,1 / JASP 20). Cluster milieu 15-19 M€ (PP Invest 19,1 / Zannier 15 / JCDecaux 15 / Mazouz 16). Outliers low 10 M€ (FP Real Estate Calmettes) + offres partielles (Schwarzenberg 4,42 / Huyghens 4,17).

**Pattern foncière haussmannienne** : Tribunal devra arbitrer entre :
1. **Prix le plus haut sans CS** : Eternam 22M€ offre ferme aucune CS + 15% versés (3,3M€) — capacité financière documentée FPCI 60M€ + lettre confort Arkéa. Le plus solide juridiquement.
2. **Prix le plus haut avec CS limitées** : Barings 25,2M€ LOI mais 3 CS (comité investissement + due diligence + accord termes promesse) — risque caducité après jugement.
3. **Build-up à long terme** : VPF/Lorenzetti+Mahout 20,1M€ avec reprise INTÉGRALE actifs + incorporels + 2 salariés engagement non-licenciement 24 mois — narratif foncière dédiée habitation.
4. **Famille fondatrice avec reprise sociale** : PP Invest 19,1M€ + 100% reprise 2 salariés + engagement 12 mois.
5. **Cherry-picking** : Huyghens 4,17M€ (4 lots — déjà propriétaire RDC) et Schwarzenberg 4,42M€ (3 lots) — pattern Minelli si tribunal refuse fragmentation.

**Doublons identifiés** : 03-SEGI-11 (Zannier) = 03-SEGI-07 ; 03-SEGI-12 (PMV1 Mac Mahon) = 03-SEGI-06. Phase 2 : dédoublonner.

**Incohérence** : 03-SEGI-19 (Mazouz) inclut lots 1+2 RDC déjà vendus à Huyghens 04/2023 pour 4M€. Erreur d'extraction CSV ou erreur dans l'offre originale — à vérifier.

## Clés COLLEGE DE PARIS (26 offres, complexité maximale)

**Structure unique** : holding 32 établissements, 76 campus, 1390 ETP, 10.339 étudiants — offres globales (45-01 et 45-25 UPSTAIRS, 45-23 REWORLD, 45-15 VERDOSO) vs offres partielles par filiale (COMUNDI, E2SE, ESCCOM, KEYCE, ISEV, NEXT STEP, VIA, ECEMA Valence, Ascencia, IFOCOP).

**Concurrence partielle** :
- **COMUNDI** : 4 offres concurrentes — CONSTELLATIS/GERESO 2,5M€ (plus élevé) vs DELLEN 800k vs GALILEO 100k partielle vs SAMARKAND 20k mais 44 emplois repris aucune CS. **Pattern EURODIF probable** : tribunal privilégie SAMARKAND si 44 ETP repris > prix CONSTELLATIS sans engagement social équivalent.
- **E2SE** : 3 offres — EDUINVEST 1M€ (plus élevé) vs EUREKA 500k 107 ETP vs ALTERNIS 500k. EUREKA gagnant probable (107 ETP + synergies Normandie + société à mission).
- **NEXT STEP** : PMP Consulting 200k€ (déjà actionnaire 50%) vs NEXT STEP HOLDCO 300k€ (salariés Man'Agir). Accord PMP/HOLDCO probable pour scission Man'Agir/3 sociétés Eva Moulin.
- **KEYCE** : Novétude Santé 100k€ — Charterhouse + Peugeot Invest, CA 156M€ — prix très bas pour CA 18M€ filiale = pattern opportuniste.

**Offres globales** :
- **45-25 UPSTAIRS V3 Finale** (lu) : Offre A 200k€/527 ETP Blocs 1+2 OU Offre B 150k€/1005 ETP Blocs 1+2+3. Plan industriel Eight Advisory documenté : 12 leviers L1-L12 +9.833 k€ EBITDA, retournement -3.078 k€ → +6.550 k€ an 1. BFR 6,5M€ documenté. **Capital UPSTAIRS 2100€ + CA 25k€ = problème pilotage holding 178M€ CA** — capacité financière 'intention_seule' = faiblesse majeure malgré qualité du plan. Pattern combine engagement social fort (1005 ETP 72%) + investisseur impact ESG + Bpifrance + 7 banques + Vox Populi pipeline QPV.
- **45-23 REWORLD MEDIA** : 2€ + 1 salarié + 7 CS — opportuniste extrême. Tribunal devrait refuser (pattern Minelli cherry-picking).
- **45-15 VERDOSO** : 11€ + 55 ETP + large périmètre. Fonds distressed — pas de plan industriel visible. Probablement refusé sauf si seule offre couvrant large périmètre.

**Tribunal arbitrera entre 2 scénarios** :
1. **Reprise globale UPSTAIRS** (45-25 Offre B) : maintien 1005 ETP / 10.339 étudiants / 18 RNCP — mais capacité financière UPSTAIRS sous-dimensionnée.
2. **Démantèlement par filiale** (pattern Neocamp/Innatis) : EUREKA E2SE + Novétude KEYCE + CONSTELLATIS/SAMARKAND COMUNDI + Réseau C&D IFOCOP + Hubert DUPUY ISEV + ROLLAND ESCCOM + PMP/HOLDCO NEXT STEP + OCEA ECEMA Valence. Périmètre résiduel CDP SAS et Bariacum → liquidation.

**Doublons identifiés** :
- DOUBLONS BINAIRES (fichiers identiques) : 45-04=45-05 (DELLEN), 45-06=45-07 (ALTERNIS)
- DOUBLONS FONCTIONNELS (même offre, formats différents) : 45-02 (112p annexes)=45-19 (13p texte) ROLLAND ; 45-03 (45p annexes)=45-16 (17p texte) EUREKA ; 45-01 (V1 80k€) précurseur de 45-25 (V3 Finale 150-200k€)

**PDF non lu en détail** : 45-17 (58 pages, repreneur non identifié).

## Anomalies détectées

1. **SEGI** : Lots 1+2 RDC déjà vendus à Huyghens (avril 2023, 4M€) — offre 03-SEGI-19 Mazouz les inclut dans le périmètre (contradictoire).
2. **SEGI** : 2 doublons (03-SEGI-11 et 12) liés à dépôt par 2 canaux (probablement avocats Mac Mahon vs DocuSign direct).
3. **COLLEGE** : 5 PDFs n'ont pas pu être ouverts en détail (45-04/05/06/07/17). Données extraites du CSV antérieur.
4. **COLLEGE** : PV de carence absent dans le CSV — l'AJ ASCAGNE doit en avoir un (référence dans 03-SEGI-01 mais pas explicite pour COLLEGE).
5. **COLLEGE** : OBSERVATION CLÉ — UPSTAIRS = société UPSTAIRS SOCIAL IMPACT SAS créée 17/10/2025 avec CAPITAL 2.100€ et exercice 1er partiel 09-12/2025 (CA 25k€, RN 19k€, trésorerie 25k€). PILOTER UNE HOLDING DE 178M€ CA AVEC CETTE STRUCTURE = signal massif d'asymétrie. Le tribunal va creuser.

## Suggestions Phase 2

1. **Pattern foncière distressed** : SEGI = exemple unique de 19 offres sur immeuble haussmannien 2.318 m² Paris 6e — fourchette x6 (4-25M€) signal incertitude majeure sur valorisation marché. Documenter dans `vault/brantham/patterns/cession-fonciere-distressed-paris.md`. Variables clés : présence locataires famille dirigeant (Pardo) + dette Banque Postale 28,8M€ + procédure parallèle Suisse + offres partielles vs globales.

2. **Pattern EdTech holding distressed** : COLLEGE DE PARIS = exemple unique de holding 32 établissements avec 26 offres concurrentes — démantèlement vs reprise globale. À documenter dans `vault/brantham/patterns/cession-edtech-holding-distressed.md`. Variables clés : multi-filiales en RJ propre (ESCCOM Nice 12/02, IRFA Lille 02/03), bail unique cause défaillance (Nanterre 1,2M€/an), goodwill anéanti Bariacum 63,2M€, privilège L.622-17 4,5M€ Barings, blocs de retournement par typologie filiale.

3. **Pattern UPSTAIRS** : société à mission + ESS + capital ridicule mais plan industriel Eight Advisory chiffré et plan financement 14-19M€ couverture. Tribunal devra arbitrer : qualité du plan vs capacité financière du véhicule. **Si retenue**, c'est un précédent majeur en M&A distressed FR pour PE/SPV avec investisseur impact.

4. **Pattern AA Investments / Galileo** : Galileo n'a déposé qu'une offre partielle COMUNDI 100k€ — alors qu'on attendait offre globale. À investiguer Phase 2 : Galileo a-t-il évité le dossier vs reprise partielle stratégique ? Hypothèse : capacité d'audit DD insuffisante sur 32 établissements en 4 semaines.

5. **Coder dans grille scoring Phase 2** :
   - `is_pattern_minelli_cherry_picking` : offre partielle <5% du périmètre + aucun ETP repris (3 cas SEGI : Schwarzenberg, Huyghens ; multiple COLLEGE : VERDOSO 11€, REWORLD 2€)
   - `is_pattern_eurodif_volet_social_premium` : ETP repris > moyenne offres concurrentes (UPSTAIRS 1005 vs autres ; SAMARKAND 44 vs autres COMUNDI)
   - `is_pattern_neocamp_demantelement` : offres groupées par cohérence sectorielle = COMUNDI/E2SE/KEYCE/IFOCOP cas d'école Phase 2

6. **Suivre BODACC** : audience COLLEGE probable mai-juin 2026. Cible Brantham pour intelligence pipeline EdTech : tracer le repreneur retenu + scénario démantèlement vs reprise globale.

## Récap (<150 mots)

47 JSONs écrits pour batch 23 mega-dossiers : SEGI 19 offres foncière haussmannienne Paris 6e (fourchette 4,17M€ partielle Huyghens à 25,2M€ LOI Barings, cluster premium 20-22M€ Eternam/Herrmann/PMV1/Emerige/BAM/VPF/JASP, 2 doublons SEGI-11=07 et SEGI-12=06) ; COLLEGE DE PARIS 26 offres EdTech holding 32 établissements 1390 ETP 178M€ CA (UPSTAIRS V3 Finale 150-200k€ 1005 ETP plan Eight Advisory mais capital véhicule 2100€ = asymétrie majeure, REWORLD 2€ opportuniste, VERDOSO 11€ symbolique, démantèlement par filiale : EUREKA E2SE 500k, NOVETUDE KEYCE 100k, SAMARKAND COMUNDI 20k 44 ETP aucune CS = pattern EURODIF, GERESO COMUNDI 2,5M€ prix le plus haut, Réseau C&D IFOCOP 1€ asso, 4 doublons binaires/fonctionnels). 2 fiches dossier. Issue : en_attente pour les 2 (audiences Q2 2026). Confidence : 1 PDF lu par dossier (Barings + UPSTAIRS V3), reste via CSV verbatim très riche.

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/repreneurs-recurrents]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/patterns/teaser-patterns]]
- [[_system/MOC-patterns]]
