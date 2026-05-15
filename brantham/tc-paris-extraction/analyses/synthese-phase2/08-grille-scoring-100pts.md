---
type: outil
project: brantham
phase: phase2
livrable: 08
created: 2026-05-15
tags: [tc-paris, scoring, grille, evaluation, offre, deal-execution]
---

# 08 — Grille de scoring d'une offre /100 pts (calibrée TC Paris)

**Outil principal** pour Brantham. Permet de noter une offre AVANT dépôt et de savoir où l'améliorer. Pondération calibrée sur les 47 retenues vs 107 rejetées du corpus, en privilégiant les variables dont Δ ≥ +15 pts entre les deux populations.

## 1. Architecture de la grille

| Bloc | Pts max | Justification de la pondération |
|---|---|---|
| **A. Prix et structure pricing** | 15 | Le prix médian ne discrimine pas — mais la **structure** oui (ventilation, modalités, transparence). Δ +5 à +15 pts entre retenues/rejetées sur sous-variables. |
| **B. Volet social** | 20 | Δ médian pct_reprise +33 pts. L'emploi est au cœur de L.642-5. |
| **C. Plan industriel / BP** | 15 | Diagnostic structurel/opérationnel Δ +34 pts, hypothèses prudentes Δ +28 pts. |
| **D. Financement** | 15 | Capacité financière forte documentée Δ +37 pts, attestation bancaire Δ +42 pts. |
| **E. Engagements et conditions suspensives** | 15 | « Aucune CS » Δ +32 pts, agressivité dirigeants kill-switch. |
| **F. Forme et présentation** | 10 | Clarté + sommaire + annexes Δ +20 à +42 pts cumulés. |
| **G. Signaux faibles et personnalisation** | 10 | Étude contrats Δ +50 pts, soutiens externes Δ +20 à +38 pts. |
| **TOTAL** | **100** | |

## 2. Bloc A — Prix et structure pricing (15 pts)

| Critère | Pts | Guide |
|---|---|---|
| A.1 Prix ≥ prix d'éviction estimé du dossier | 4 | Si pas d'info concurrent : utiliser règle 12% du CA cible plafond, 0,5-2× EBITDA si positif. Si symbolique 1-3€ : 0 pt sauf si reprise L.642-12 al.4 ≥ 100 k€ (alors 3 pts) |
| A.2 Ventilation incorporels / corporels / stocks chiffrée | 3 | Tout ventilé = 3. Manque un poste = 1. « Ultérieurement » = 0. |
| A.3 Modalité de paiement comptant à l'audience | 3 | Comptant = 3. Séquestre = 2. Mixte = 1. Échéancier = 0. |
| A.4 Charges augmentatives listées et transparentes | 3 | Toutes listées avec montants = 3. Mentionnées sans chiffrage = 1. Masquées = -3 (kill-switch). |
| A.5 Cohérence prix vs BP (DCF approximatif) | 2 | Cohérent = 2. NR = 1. Incohérent = 0. |

**Bornes** : 0 à 15 pts. Note minimale pour passer = 8/15.

## 3. Bloc B — Volet social (20 pts)

| Critère | Pts | Guide |
|---|---|---|
| B.1 Pct de reprise des effectifs | 8 | ≥90 % = 8 ; 70-89 % = 6 ; 50-69 % = 4 ; 30-49 % = 2 ; <30 % = 0 |
| B.2 Engagement non-licenciement chiffré (durée mois) | 4 | ≥24 mois = 4 ; 12-23 mois = 2 ; non précisé = 0 |
| B.3 L.1224-1 / maintien des conditions « oui total » | 4 | Oui total = 4 ; partiel = 2 ; non = 0 |
| B.4 Sanction prévue en cas de non-respect de l'engagement | 2 | Pénalité chiffrée = 2 ; mention sans chiffrage = 1 ; rien = 0 |
| B.5 Mention IRP/CSE et concertation prévue | 1 | Oui = 1 ; non = 0 |
| B.6 Plan d'accompagnement social pour non-repris | 1 | Indemnités/accompagnement chiffrés = 1 ; non = 0 |

**Bornes** : 0 à 20 pts. Note minimale pour passer = 12/20.

## 4. Bloc C — Plan industriel et BP (15 pts)

| Critère | Pts | Guide |
|---|---|---|
| C.1 Diagnostic du repreneur | 4 | Structurel = 4 ; Opérationnel = 3 ; Superficiel = 1 ; Absent = 0 |
| C.2 Vision stratégique formulée en 1 phrase claire | 2 | Oui avec chiffre/label = 2 ; oui générique = 1 ; non = 0 |
| C.3 Business plan 3 ans présent | 4 | BP détaillé avec hypothèses = 4 ; BP synthétique = 2 ; absent = 0 |
| C.4 Hypothèses qualifiées prudentes ou réalistes | 2 | Prudentes = 2 ; réalistes = 1,5 ; agressives = 0,5 ; absentes = 0 |
| C.5 Capex chiffré et calendarisé | 1 | Oui = 1 ; non = 0 |
| C.6 Synergies repreneur quantifiées | 1 | Oui chiffrées = 1 ; mentionnées sans chiffrage = 0,5 ; non = 0 |
| C.7 Maintien marques / savoir-faire / site | 1 | Oui total = 1 ; partiel = 0,5 ; non = 0 |

**Bornes** : 0 à 15 pts. Note minimale pour passer = 8/15.

## 5. Bloc D — Financement (15 pts)

| Critère | Pts | Guide |
|---|---|---|
| D.1 Capacité financière démontrée | 5 | Forte documentée = 5 ; Moyenne documentée = 3 ; Faible/intention = 0 |
| D.2 Attestation bancaire / RIB d'apport en annexe | 3 | oui_rib_attestation = 3 ; oui_simple_mention = 1 ; non = 0 |
| D.3 Dette bancaire engagement ferme | 3 | Engagement ferme = 3 ; lettre confort = 2 ; en cours = 0 |
| D.4 BFR redémarrage et trésorerie sécurité chiffrés | 2 | Les deux chiffrés = 2 ; un seul = 1 ; aucun = 0 |
| D.5 Comptes sociaux 3 ans du repreneur annexés | 2 | Oui = 2 ; partiel = 1 ; non = 0 |

**Bornes** : 0 à 15 pts. Note minimale pour passer = 9/15.

## 6. Bloc E — Engagements et conditions suspensives (15 pts)

| Critère | Pts | Guide |
|---|---|---|
| E.1 Nombre de conditions suspensives | 5 | Aucune = 5 ; 1 = 4 ; 2 = 3 ; 3 = 1 ; ≥4 = 0 |
| E.2 Agressivité CS envers dirigeants sortants | 4 | Aucune = 4 ; modérée = 1 ; forte (clause non-sollicitation) = -4 (kill-switch) |
| E.3 Incessibilité temporaire (mois) | 2 | ≥24 mois = 2 ; 12-23 = 1 ; non précisé = 0 |
| E.4 Non-démembrement engagé | 1 | Oui = 1 ; non = 0 |
| E.5 Déclaration L.642-3 signée | 2 | Oui = 2 ; non = 0 |
| E.6 Faculté de substitution précise et nominative | 1 | Oui nominative = 1 ; mention sans nom = 0,5 ; non = 0 |

**Bornes** : 0 à 15 pts (avec possibilité de -4 sur E.2). Note minimale pour passer = 10/15.

## 7. Bloc F — Forme et présentation (10 pts)

| Critère | Pts | Guide |
|---|---|---|
| F.1 Sommaire détaillé numéroté 10 sections | 2 | Oui = 2 ; lettre simple = 0 |
| F.2 Executive summary présent | 1 | Oui = 1 ; non = 0 |
| F.3 Ton mixte (juridique + commercial) | 1 | Mixte = 1 ; juridique strict = 0,5 ; commercial seul = 0 |
| F.4 Qualité rédactionnelle claire (relecture critique) | 2 | Claire = 2 ; dense = 1 ; confuse = 0 |
| F.5 Annexes obligatoires présentes (Kbis, CV, CNI, organigramme) | 2 | 4 annexes / 4 = 2 ; 3/4 = 1,5 ; 2/4 = 1 ; ≤1/4 = 0 |
| F.6 Annexes optionnelles (BP, comptes 3 ans, attest fisc-soc) | 1 | 3/3 = 1 ; 2/3 = 0,5 ; ≤1/3 = 0 |
| F.7 Nb de pages corps ≤15 + annexes lisibles | 1 | Oui = 1 ; corps >20 ou annexes confuses = 0 |

**Bornes** : 0 à 10 pts. Note minimale pour passer = 6/10.

## 8. Bloc G — Signaux faibles et personnalisation (10 pts)

| Critère | Pts | Guide |
|---|---|---|
| G.1 Étude des contrats clients/fournisseurs documentée | 3 | Paragraphe dédié avec noms contrats = 3 ; mention générale = 1 ; non = 0 |
| G.2 Visite de site mentionnée | 1 | Oui = 1 ; non = 0 |
| G.3 Rencontre des équipes mentionnée | 1 | Oui = 1 ; non = 0 |
| G.4 Soutien externe (banque historique, client clé ou collectivité) | 2 | 2+ lettres = 2 ; 1 lettre = 1 ; aucune = 0 |
| G.5 Différenciation explicite vs concurrents connus | 1 | Paragraphe dédié = 1 ; aucun = 0 |
| G.6 Volet narratif humain / engagement social qualitatif | 1 | Présent (au-delà du strictement juridique) = 1 ; non = 0 |
| G.7 Track record reprises antérieures du repreneur | 1 | ≥2 reprises = 1 ; 1 reprise = 0,5 ; 0 = 0 |

**Bornes** : 0 à 10 pts. Note minimale pour passer = 5/10.

## 9. Synthèse — seuils d'interprétation

| Score total | Diagnostic | Action |
|---|---|---|
| **90-100** | Offre « parfaite » (cas Vergers d'Anjou 13/13 Tier S+A) | Déposer en l'état |
| **75-89** | Offre forte (cas EURODIF / AA Investments HK ~80) | Déposer, prête à amélioration v2 si tribunal demande |
| **60-74** | Offre moyenne-haute | Renforcer 2-3 blocs faibles avant dépôt |
| **45-59** | Offre moyenne | Travail substantiel requis, risque rejet élevé |
| **30-44** | Offre faible | Refonte nécessaire ou retrait |
| **<30** | Offre non viable | Ne pas déposer |

**Seuil minimal de dépôt Brantham** : 70/100.

## 10. Kill-switches absolus (mise à zéro automatique)

Si une de ces erreurs est présente, **le score total est ramené à <30 et l'offre doit être réécrite** :

1. Périmètre marginal vs concurrent connu plus large (sauf si stratégie de positionnement défensive explicite)
2. Indivisibilité avec >5 entités (« château de cartes »)
3. Clause non-sollicitation imposée aux dirigeants sortants (« kill-switch COSA »)
4. Charges augmentatives masquées (>50 k€ non listés)
5. « Caractéristiques NewCo / BP / liste salariés communiquées ultérieurement »
6. PDF visant la mauvaise société-cible (erreur de classification)
7. Conflit d'intérêt non déclaré + L.642-3 non signée

## 11. Application — exemple de scoring (cas Magic Form Levallois)

À titre d'exemple, application de la grille à un cas en cours (premier deal Brantham, deadline 21/05/2026 12h) :

| Bloc | Critère | Note projetée | Commentaire |
|---|---|---|---|
| A. Prix | Prix ≥ éviction (CA 350-595k → cible 25-70k€) | ? | Dépend du benchmark concurrents (à demander à l'AJ) |
| A. Prix | Ventilation | 3/3 | À chiffrer dans la note |
| A. Prix | Comptant audience | 3/3 | À confirmer financement |
| B. Social | Pct reprise | Cible 100 % = 8/8 | Petit effectif, faisable |
| B. Social | Engagement 24 mois | 4/4 | À inclure |
| C. Plan | Diagnostic opérationnel | 3/4 | Vision salle sport quartier |
| D. Financement | Forte documentée | 5/5 | Si attestation bancaire sortie |
| E. CS | Aucune | 5/5 | Cible offre ferme |
| F. Forme | Sommaire 10 sections | 10/10 | Suivre template Brantham |
| G. Signaux | Étude contrats | 3/3 | Mentionner bail commercial + contrats fournisseurs |

**Note projetée** : 75-85/100 si exécution rigoureuse. **OK pour dépôt**.

## 12. Excel-friendly — feuille de scoring (à recopier)

Le fichier `/Users/paul/vault/brantham/tc-paris-extraction/analyses/synthese-phase2/grille_scoring_template.csv` (à créer) reprend les 32 critères de la grille pour scoring automatisé. Format suggéré :

```csv
Bloc,Critere,Pts_max,Note_attribuee,Justification
A,A.1 Prix éviction,4,,
A,A.2 Ventilation,3,,
A,A.3 Comptant audience,3,,
A,A.4 Charges augmentatives transparentes,3,,
A,A.5 Cohérence prix BP,2,,
B,B.1 Pct reprise effectifs,8,,
...
```

## 13. Calibration et limites

- Pondérations calibrées sur **154 offres décidées** (47 retenues + 107 rejetées) du TC Paris 2025-2026. Réplicabilité dans d'autres ressorts (Lille, Nanterre, Marseille) non testée.
- **n=47 retenues** dont environ 12 doublons techniques (le n unique est ~35).
- Les blocs B (social) et D (financement) sont les plus lourds (20+15 = 35 pts) car ce sont les deux dimensions où Δ retenues-rejetées est le plus stable.
- La pondération n'est pas issue d'une régression logistique multivariée — c'est une calibration **expert-driven informée par les stats**. Une régression avec n=154 serait fragile (overfit) ; on préfère la transparence du modèle additif.

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/01-stats-descriptives]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/02-anatomie-winners-vs-losers]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/07-signaux-credibilite-tribunal]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/09-bibliotheque-extraits]]
- [[brantham/tc-paris-extraction/analyses/playbook-redaction-offre]]
- [[brantham/deals/active/magic-form-levallois/_MOC]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/_index]]
