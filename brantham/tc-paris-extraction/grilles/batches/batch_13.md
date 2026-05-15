---
type: batch-log
batch_id: 13
dossiers: [62]
created: 2026-05-15
extracted_by: claude-agent
tags: [tc-paris, extraction, INNATIS, vergers-anjou]
---

# Batch 13 — Dossier 62 SCEA DE LA CHAUSSEE (INNATIS Val de Loire)

## Resume execution

- **Dossier traite** : 62 — SCEA DE LA CHAUSSEE (RCS Angers 786 169 748, filiale INNATIS Pole Val de Loire, branche Angevine)
- **7 PDFs extraits** → 7 JSONs offres + 1 JSON dossier
- **Issue globale** : plan_cession_arrete (audience TAE Paris 30/04/2026)
- **Repreneur retenu (au niveau pole INNATIS)** : Les Vergers d'Anjou (cooperative) — 7,04 M€ + 200k€ accompagnement social, avec faculte substitution CELHER pour LPC et LVL POMANJOU
- **AUCUNE des 7 offres deposees dans le dossier 62 n'a ete retenue** (Vergers d'Anjou n'a pas depose d'offre specifique pour CHAUSSEE — sa stratégie passe par les actifs SCICA POMANJOU / LPC / LVL POMANJOU au niveau pole)

## Fichiers produits

| Fichier | Offrant | Prix | Emplois | Statut |
|---|---|---|---|---|
| 62-01.json | CASTEL/LEROY/VCAPITAL (amelioree 08/04) | 50 000€ (ventilation 1/24/1/24k) | 4/6 (66,7%) | non |
| 62-02.json | CELHER + AGRILAND NORD + PENCHENAT | 150 000€ + DPB 30k + avances 60k | 4/6 (66,7%) | non |
| 62-03.json | CELHER + AGRILAND NORD + PENCHENAT (DOUBLON 62-02) | 150 000€ | 4/6 | non |
| 62-04.json | CASTEL/LEROY/VCAPITAL (initiale 18/03) | 50 000€ (pas de ventilation) | 4/6 | non |
| 62-05.json | CASTEL/LEROY/VCAPITAL (DOUBLON 62-04) | 50 000€ | 4/6 | non |
| 62-06.json | CASTEL/LEROY/VCAPITAL (DOUBLON 62-04) | 50 000€ | 4/6 | non |
| 62-07.json | EARL CELLIER DU MESNIL | 50 000€ + DPB 30k + avances 55k | 4/6 | non |
| dossiers/62.json | Meta dossier | — | — | — |

## Doublons techniques detectes

- **62-03 = 62-02** : meme DocuSign ID `04750D32-5A75-4305-8552-1F52E6E3CFA0` (depot CELHER duplique au greffe)
- **62-05 = 62-06 = 62-04** : meme DocuSign ID `A33B3D05-BE34-48EB-A5AB-BFE1B121F625` (triple depot CASTEL/LEROY/VCAPITAL initial)

Donc reellement **3 offres distinctes** sur 7 fichiers.

## Application methode decortique-offres-gagnantes.md

Le decortique INNATIS/POMANJOU (Dossier 2) avait deja analyse CASTEL/LEROY/VCAPITAL comme perdant face a Vergers d'Anjou. Pour ce dossier 62 specifique :

- **CASTEL/LEROY/VCAPITAL** : marquage `non` (offre indivisible avec 10 autres entites, signaux faibles deja identifies : pas de ventilation prix dans l'initiale, modalites financement "a preciser ulterieurement", chateau de cartes)
- **CELHER+AGRILAND+PENCHENAT** : marquage `non` mais structure CELHER recuperee par Vergers d'Anjou comme substitut pour LPC et LVL POMANJOU (point intelligent dans le decortique — partenariat cooperative + producteurs locaux)
- **EARL CELLIER DU MESNIL** : marquage `non` — Laurent CELLIER travaille les terres CHAUSSEE depuis 30 ans (legitimite forte) + Mathias CELLIER primo-installation, mais pas de plan strategique au-dela continuite, prix trop bas (50k€ + DPB), discordance d'inventaire salaries (5 vs 6).

## Champs prioritaires remplis (tous JSONs)

- issue_dossier.cette_offre_retenue : oui (toutes `non`)
- motifs_rejet : explicites (renvoi decortique + Vergers d'Anjou retenu au pole)
- profil_repreneur.forme : holding_ad_hoc (CASTEL/LEROY/VCAPITAL), societe_existante_industriel (CELHER, EARL CELLIER)
- track_record_reprises : remplis (Maison Leroy / Paysans Resistants / AGRILAND coordination 7 regions / ETS CELLIER)
- pct_reprise : 66,7% pour les 3 offrants
- prix : 50k€ (CASTEL, CELLIER) / 150k€ (CELHER)
- charges_aug : 90k€ DPB+avances pour CELHER ; 85k€ DPB+avances pour CELLIER ; null pour CASTEL
- diagnostic_qualification : operationnel (CELHER, CELLIER) ; superficiel (CASTEL initial)
- plan_affaires_3ans_present : false partout
- aucune_cs : false partout (entre 1 et 8 conditions selon l'offre)
- agressivite_envers_dirigeants : aucune partout
- executive_summary_present : true (CASTEL, CELHER) ; false (CELLIER)
- personnalisation_visite_site : true pour CELHER + CELLIER (connaissance terrain) ; false pour CASTEL

## Anomalies / points d'attention

1. **Doublons techniques massifs** : 4 fichiers sur 7 sont des doublons. Sur les 570 offres totales du dataset, il faudrait revoir si cette pratique existe ailleurs pour eviter de gonfler artificiellement les stats.
2. **Vergers d'Anjou absent du dossier 62** : confirme l'architecture INNATIS — Vergers d'Anjou a pris les 3 entites cles (SCICA POMANJOU / LPC / LVL POMANJOU) et a delegue les 8 SCEA agricoles a CELHER par substitution. Les 7 offres CHAUSSEE n'ont jamais ete competitives face a la solution coop+CELHER en substitution.
3. **PENCHENAT primo-installation prioritaire SDREA rang 1** : signal interessant pour scoring agricole — la loi prevoit une priorite reglementaire SDREA pour les jeunes agriculteurs sur les cessions de SCEA (article L.642-1 alinea 3 in fine Code de commerce). Tribunal pourrait privilegier ce statut. A surveiller dans d'autres dossiers agricoles.
4. **Indivisibilite massive cote CASTEL/LEROY/VCAPITAL** : 11 offres liees pour cout global 6,49 M€ — pattern "chateau de cartes" deja identifie dans le decortique.

## Suggestions

- **Phase 2** : creer une variable derivee `is_duplicate_docusign` pour filtrer les doublons techniques lors de l'agregation
- **Phase 2** : creer un drapeau `procedure_groupe` pour les dossiers indivisibles (INNATIS Val de Loire = 11 SCEA + 3 holdings) — l'unite d'analyse pertinente est le pole, pas l'entite
- **Phase 2** : explorer la dimension "priorite reglementaire SDREA" pour les cessions agricoles
- **Compile-concepts** : potentiel d'un concept "cooperative-cooptee" — le tribunal a privilegie un acteur cooperatif local qui internalise les producteurs (Boujuau de CELHER + station Pomanjou voisine <5km) plutot qu'un consortium financier ad hoc

## Related

- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes|Decortique offres gagnantes]] — Dossier 2 INNATIS/POMANJOU
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal|Gagnants tribunal]] — point 6 Pole INNATIS
- [[brantham/tc-paris-extraction/grilles/dossiers/62|Fiche dossier 62]]
- [[brantham/tc-paris-extraction/grilles/_schema|Schema offre]]
- [[brantham/tc-paris-extraction/grilles/_workflow|Workflow extraction]]
