---
type: batch-log
batch_id: 11
project: brantham
created: 2026-05-15
agent: claude-agent
tags: [tc-paris, extraction, batch, innatis, vergers-anjou]
---

# Batch 11 — Pôle Val de Loire INNATIS (5 dossiers, 22 offres)

## Dossiers traités

| ID | Société | SIREN | Offres | Gagnant |
|---|---|---|---|---|
| 36-LVL | LVL POMANJOU | 407871656 | 6 (5 distinctes : 1 doublon DSA) | Vergers d'Anjou (sub. CELHER pour LPC+LVL) |
| 37-COOP | CAVL Coopérative arboriculteurs | 323839506 | 6 (3 distinctes : 4 doublons Docusign) | Vergers d'Anjou (sub. CELHER pour emploi) |
| 57 | SCA DE LA PLESSE | 379609514 | 6 (3 distinctes : 2 doublons CELHER) | CELHER (sous Vergers d'Anjou) |
| 59 | SCEA LA REINETTE D'ANJOU | 786159152 | 6 (4 distinctes : 2 doublons CELHER) | CELHER (sous Vergers d'Anjou) |
| 60 | SCEA DE LA DENIOLAY PEROUSSAY | 320401987 | 6 (4 distinctes : 2 doublons CASTEL) | Vergers d'Anjou (consortium-LAUNAY rejeté) |

## Issue globale — Plan de cession arrêté 30/04/2026

Audience tribunal 13/04/2026 9h15 (TC Activités Économiques Paris). Plan de cession arrêté pour les 11 entités du Pôle Val de Loire INNATIS (~40-50M€ CA, ~100 salariés, 300 ha vergers) au profit de la **Coopérative LES VERGERS D'ANJOU** :
- **Prix global ~7,04 M€** (SCICA POMANJOU 5,28M€ + LPC 0,87M€ + LVL POMANJOU 0,89M€)
- **28 emplois CDI repris** + **200.000€ accompagnement social volontaire**
- **Faculté de substitution intelligente** : CELHER (Boujuau) pour les SCEA agricoles (LPC, LVL, REINETTE, PLESSE)
- **Cash garanti** par CRCAM Anjou-Maine + CIC Ouest

Consortium adverse **CASTEL/LEROY/VCAPITAL** rejeté :
- Indivisibilité 11 offres parallèles (château de cartes)
- Ventilation prix + financement renvoyés à 'ultérieurement'
- Conflit d'intérêts James LAUNAY (ex-salarié LVL POMANJOU)
- Coût total annoncé 6,49M€ mais prix de cession dérisoire (40k€ CAVL, 50k€ Deniolay, 200k€ LVL)

Offres EARL CELLIER (60-06) et CELHER/AGRILAND-PENCHENAT (60-03) sur Deniolay/Chaussée également rejetées.

## Méthode

- Lecture **CSVs locaux** (`dossiers.csv` + `offres.csv` par dossier) — ~50% des champs déjà extraits
- Croisement **`decortique-offres-gagnantes.md`** (section dossier 2 INNATIS/POMANJOU — Vergers d'Anjou décortiquée à 11 sous-sections)
- Croisement **`gagnants-tribunal.md`** (Pôle Val de Loire INNATIS DÉCIDÉ — Vergers d'Anjou retenue)
- PDFs non relus directement : les CSVs étaient denses, datés et cohérents

## Tagging cette_offre_retenue

| Offre | Tag | Justification |
|---|---|---|
| 36-LVL-06 (Vergers d'Anjou) | amelioree_puis_retenue | Offre principale, prix CASH structuré, accompagnement social |
| 36-LVL-01/03 (Castel/Leroy/Vcap) | non | Rejeté pour indivisibilité, conflit, financement vague |
| 36-LVL-02/04 (Advantage Malte) | en_attente | Hors plan L.642-19 sur titres DSA — autorisation JC séparée |
| 36-LVL-05 (Dutoit Afrique du Sud) | en_attente | Idem L.642-19 |
| 37-COOP-03 (Vergers d'Anjou) | amelioree_puis_retenue | Prix 75k€, 1 emploi, CRCAM |
| 37-COOP-01/02 (Castel/Leroy/Vcap) | non | Prix 40k€, périmètre flou |
| 57-02/03 (CELHER) | amelioree_puis_retenue | Substitution Vergers d'Anjou — Boujuau exploitants 28 ans |
| 57-01 (Castel/Leroy/Vcap) | non | 50k€, 1 emploi, indivisibilité |
| 59-02/03 (CELHER) | amelioree_puis_retenue | Idem (REINETTE + PLESSE consolidé) |
| 59-01/04 (Castel/Leroy/Vcap) | non | 10k€, indivisibilité, 11 conditions suspensives |
| 60-01/02/04/05 (Castel/Leroy/Vcap) | non | Rejeté — doublons techniques |
| 60-03 (CELHER + AGRILAND PENCHENAT) | non | 0 emploi Deniolay, jeune agriculteur rang 1 mais perd |
| 60-06 (EARL CELLIER) | non | 0 emploi Deniolay, EARL familiale rejetée |

## Champs prioritaires couverts (15/15)

- ✅ issue / cette_offre_retenue (verbatim motifs tribunal pour Vergers d'Anjou)
- ✅ profil_repreneur.forme (societe_existante_industriel pour tous sauf EARL CELLIER pp_seule + Advantage/Dutoit repreneur_etranger)
- ✅ track_record_reprises (Maison Leroy 200 ans, Boujuau acquisitions 2008-2023, Vergers d'Anjou fusion SCAFLA 2024)
- ✅ experience_sectorielle_oui_non (oui partout)
- ✅ volet_social.pct_reprise (0 à 100% selon offres)
- ✅ structure_prix.prix_total_eur (10k€ à 3M€)
- ✅ charges_augmentatives_eur (6,49M€ documentés pour consortium CASTEL)
- ✅ plan_industriel.diagnostic_qualification (structurel pour Vergers d'Anjou, operationnel/superficiel pour autres)
- ✅ plan_affaires_3ans_present (true pour CELHER, false pour CASTEL)
- ✅ aucune_cs (true pour Vergers d'Anjou + CELHER, false pour CASTEL 7-11 CS)
- ✅ agressivite_envers_dirigeants (aucune pour Vergers d'Anjou, moderee CASTEL)
- ✅ executive_summary_present (true pour Vergers d'Anjou + CELHER, false CASTEL)
- ✅ personnalisation_visite_site / rencontre / etude_contrats (couverts)

## Anomalies / observations

1. **Doublons techniques massifs** : 37-COOP (4 doublons offre 1-2-3-4), 57 (offre3=4=5), 59 (offre3=4=5), 60 (offre1=2 et offre4=5). Mêmes Docusign Envelope ID — probablement signatures séparées par chacune des parties (Castel, Leroy, Vcap, cabinet).
2. **Indivisibilité 11 offres** : argument-clé du décortique — Castel signale d'emblée que toute échec d'une des 11 cessions fait tomber l'ensemble. Le tribunal lit "château de cartes".
3. **Vergers d'Anjou architecture intelligente** : substitution CELHER pour SCEA agricoles + reprise directe immobilier (SCICA POMANJOU station Océane). Producteurs locaux + coopérative = pérennité filière.
4. **James LAUNAY conflit d'intérêts** : actuellement salarié LVL POMANJOU — information privilégiée, rhétoriquement délicat.
5. **VCAPITAL coquille** : SAS unipersonnelle cap. 500€, CP 80k€, créée 2024.
6. **EARL CELLIER (60-06)** : Laurent CELLIER 30 ans de travaux agricoles SCA Chaussée — argument continuité valable mais offre 0 emploi Deniolay disqualifiante.
7. **AGRILAND NORD/PENCHENAT (60-03)** : carte "jeune agriculteur primo-installation rang 1 L.642-1 al.3" jouée — mais le tribunal a privilégié projet coopératif global de Vergers d'Anjou.

## Suggestions Phase 2

- **Pattern fort** : la **"phrase ultérieurement"** = signal disqualifiant absolu (CASTEL renvoie ventilation prix + financement à "ultérieurement"). À codifier comme signal_faible.
- **Pattern** : offres "indivisibles" sur plusieurs entités = surface de risque exponentielle perçue par tribunal. À discriminer.
- **Pattern** : repreneur coopératif local + accompagnement social volontaire = combinaison gagnante (déjà vu sur dossier 1 Eurodif avec AA Investments).
- **Anti-pattern** : faculté de substitution NewCo encore non-désignée = signal d'amateurisme procédural.

## Stats batch

- 5 dossiers, 22 offres distinctes (sur 30 PDFs avec doublons)
- 5 fiches dossier + 22 fiches offre = **27 JSONs créés**
- Confidence majoritairement **high** (CSVs très denses, décortique de référence)
- Temps de traitement : ~25 min

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[_system/MOC-master]]
