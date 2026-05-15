---
type: session
date: 2026-05-15
project: brantham
tags: [osint, skill, deanon, monabee, tech-valley, fhbx, meynet, deals]
---

# Session 2026-05-15 — OSINT Deanon : skill + cas MONABEE + TECH VALLEY

Session marathon construction d'un skill OSINT systématique pour
désanonymiser les annonces de cession judiciaire, suivi de deux cas réels
résolus : MONABEE (annonce Actify) et TECH VALLEY (annonce dataroom FHBX).

## 1. Cas n°1 — MONABEE (annonce Actify n°14566)

### Input
URL : `https://actify.fr/entreprises-liquidation-judiciaire/cession-dune-activite-de-panneaux-photovoltaiques/`

Annonce anonymisée : "Cession d'une activité de panneaux photovoltaïques",
deadline offres 19/06/2026, AJ Meynet, contacts MEYNET Robert Louis +
LEPRAT Camille, tranche CA >10M€, tranche effectif 11-50.

### Fausses pistes successives
1. **SOLAK ENERGIE** (Vaulx-en-Velin, SIREN 535 364 798) — matche AJ Meynet,
   activité photovoltaïque, RJ 25/02/2026. MAIS le teaser image révèle
   ensuite des sites Vaulx-Milieu (38) + Landivisiau (29) + 42 salariés,
   incompatibles avec SOLAK. **Éliminée.**
2. **EVERSUN** (Lyon, SIREN 922 192 729) — RJ photovoltaïque B2C
   11/12/2025. MAIS AJ = SELARL Anasta + MJ Martin (pas Meynet). **Éliminée.**
3. **SOLAIRE AVANTAGES, mylight150 France, APEM Énergie** — aucun ne matche.

### Identification finale
**MONABEE SAS** (SIREN 788 614 006)
- Siège : 4 chemin des Hirondelles, **69570 Dardilly** (Lyon métropole ouest)
- Création : 09/10/2012 (12 ans — invalide la tranche "2-5 ans" Actify)
- Capital : 33 571 €
- NAF : 4321A (installation électrique)
- Activité réelle : commercialisation/installation/SAV de générateurs solaires
  photovoltaïques + boîtiers de pilotage/délestage/stockage énergétique
  pour autoconsommation résidentielle
- Dirigeants : Vianney Fichet (Président depuis 25/08/2023), Clara Trevisiol
  (DG depuis 30/07/2022)
- CA 2023 (Société.com) : **12 061 000 €**
- CA décroissant teaser : 12,06 → 10,22 → 8,22 M€
- Effectif INSEE : 50-99 ; teaser : 42 (post-dégraissage)

### Procédure
- Tribunal : TAE de Lyon
- RJ ouvert : **09/04/2026**, cessation paiements 10/03/2026
- AJ : **SCP AJ Meynet & Associés** (Me Robert Louis Meynet / Me Typhaine
  Meynet / Me Arthur Boucaud) — 128 rue Pierre Corneille 69003 Lyon
- MJ : **SELARLU Martin** (Me Pierre Martin) — 20 bd Eugène Deruelle
  69003 Lyon
- Deadline offres : **19/06/2026 12h**
- Référence dossier interne Meynet : **n° 14566**
- Contacts : aurelie.plotton@etude-meynet.fr / camille.leprat@etude-meynet.fr

### Preuve d'identification
**CA 2022 teaser = 12 061 109 €** ↔ **CA 2023 Societe.com = 12 061 000 €**
(écart 109 € = même exercice avec décalage de publication). Empreinte unique.

### Pièges rencontrés
- "Adresse de contact" Actify = adresse étude AJ, **pas** siège débiteur
- Apostrophe typographique U+2019 dans URL image teaser (404 si non décodé
  en %E2%80%99)
- Camille Leprat = collaboratrice étude Meynet, **pas** MJ (Apollo.io renvoie
  faussement "ATMP du Rhône" — ATMP fait des tutelles, pas de procédures
  collectives)
- BODACC indique activité MONABEE = "commercialisation de boîtiers
  électroniques" (NAF 4321A) → filtrage par "photovoltaïque" rate la cible.
  Toujours scanner les "autres" candidats du même AJ.
- Champs Actify auto-saisis erronés : "ancienneté 2-5 ans" pour société de
  12 ans
- OCR teaser : "Vaulx-Meilieu" lu pour "Vaulx-Milieu"
- "Lyon (Siège)" sur teaser = Dardilly (banlieue ouest)

Voir [[brantham/deals/identified/2026-05-13-monabee]] (à créer).

## 2. Construction du skill `osint-deanon`

À partir des leçons MONABEE, construction d'un skill Claude Code complet :

```
~/.claude/skills/osint-deanon/
├── README.md           ← install + usage
├── SKILL.md            ← instructions Claude Code, méthode SCRAPE
├── playbook.md         ← 10 pièges documentés + études AJ usuelles
└── scripts/
    ├── fetch-teaser.sh           ← scrape page + teaser image (apostrophes Unicode décodées)
    ├── bodacc-aj-scan.sh         ← liste RJ d'un AJ sur une année
    ├── bodacc-verify.sh          ← historique BODACC d'un SIREN
    └── sirene-establishments.sh  ← fiche SIRENE + URLs établissements
```

### Méthode SCRAPE
1. **S**urface — scrape page anonymisée, meta + URLs images
2. **C**ross-check — identifier AJ ≠ adresse débiteur
3. **R**esolve AJ — annuaire CNAJMJ + collaborateurs étude
4. **A**cquire teaser — récupérer PNG/PDF, apostrophes Unicode décodées
5. **P**robe BODACC — API open data, filtre AJ + année + activité
6. **E**stablish proof — CA exact à l'euro près = empreinte unique

### Archives partagées
- `~/Desktop/osint-deanon.tar.gz` (12 KB)
- `~/Desktop/osint-deanon.zip` (16 KB)

Scope : cessions FR uniquement (BODACC + SIRENE + études AJ FR). Pas
international, pas personnes, pas infra. Pour ces usages → v2 à construire.

Pattern documenté : [[brantham/patterns/osint-deanon-cession-anonyme]].
Skill : `~/.claude/skills/osint-deanon/SKILL.md`.

## 3. Cas n°2 — TECH VALLEY (annonce FHBX dataroom n°13940)

### Input
URL : `https://dataroom.fhbx.eu/biens/bien/?numActif=12000008603`

Annonce anonymisée FHBX : ESN ingénierie informatique + conseil
digitalisation, 66100 Perpignan, deadline offres 05/06/2026, CA 30/06/2025
= 3 138 K€, RN −1 931 K€, 42 salariés, sous-traitance aéronautique/télécom/
finance.

### Pipeline OSINT
1. **Surface** : WebFetch dataroom FHBX → toutes les meta (référence 13940,
   contact Marine Camusat, AJ FHBX/Eric Samson Perpignan)
2. **Probe BODACC** : `bodacc-aj-scan.sh FHBX 2026` → 0 match informatique
   à Perpignan. Élargissement temporel : recherche RJ 66 2025.
3. **Trouvaille** : **TECH VALLEY** (SIREN 799 107 073), RJ ouverte
   29/01/2025 par TC Perpignan, activité = "Conseil et expertise informatique
   en SI, vente de prestations d'ingénierie, infogérance, formation, portage
   salarial". Match parfait.

### Identification finale — TECH VALLEY SARL
- SIREN : 799 107 073 — RCS Perpignan
- Siège : **3 Boulevard de Clairfont, 66350 Toulouges** (banlieue sud
  Perpignan — le teaser arrondit à "66100 Perpignan")
- Établissement secondaire : 1202 L'Occitane Technoparc, **31670 Labège**
  (Toulouse Sud), ouvert 18/06/2025 (pendant la période d'observation)
- Création : 19/12/2013 (12 ans)
- Capital : 300 000 €
- Forme : SARL
- NAF : 6202A — Conseil en systèmes et logiciels informatiques

### Direction
- **Sébastien GARCIA** (1991), gérant depuis 23/01/2025
- **Arnaud GAILLARD** (1989), gérant depuis 23/01/2025
- **Signal fort** : nominations simultanées 6 jours avant la cessation des
  paiements officielle (22/01/2025). Recapitalisation ratée ou prise de
  contrôle pré-RJ probable.

### Finances
- Exercice clôt **30 juin** (rare — ~5 % des PME FR)
- 30/06/2025 (teaser) : CA 3 138 K€ / RN −1 931 K€ (−61,5 % du CA)
- 2024 (Societe.com) : CA non publié (confidentialité activée) / RN −933 K€
- CA/tête : ~75 K€ → bas pour ESN aéro/finance (norme 100-130 K€) →
  taux inter-contrat élevé probable

### Procédure
- Tribunal : Tribunal de Commerce de Perpignan
- RJ ouvert : **29/01/2025**, cessation paiements 22/01/2025
- BODACC publication ouverture : 09/02/2025
- AJ : **SELARL FHBX** — **Me Eric SAMSON** (centreplus 9 rue Camille
  Desmoulins, 66026 Perpignan CEDEX)
- MJ : **SELARL MJSA** — **Me Aguilé SANTODOMINGO** (7 rue Léon Dieude,
  Résidence Saint Amand, 66000 Perpignan)
- Dépôt état des créances : 20/11/2025
- Deadline offres : **05/06/2026**
- Période d'observation : **>16 mois** (très long, max légal standard 12
  mois) → autorisation exceptionnelle ou relance d'appel à candidatures
  après échec d'une première phase
- Référence dataroom FHBX : **13940 / numActif 12000008603**
- Contact : Marine CAMUSAT — marine.camusat@fhbx.eu

### Repreneurs naturels à explorer
1. **Consolidateurs ESN distressed** : Ekino (Havas), Cap Vert Finance,
   Constellation, Niji
2. **ESN régionales Occitanie en consolidation** : SCC Occitanie, Coexel,
   Cyrès, Devotteam Sud
3. **Grandes ESN nearshore Sud France** : Sopra Steria (déjà Toulouse),
   Capgemini Régional, Atos/Eviden
4. **Concurrents locaux** : HCI Informatique (Perpignan), Agence 418
   (Perpignan), Koesio Méditerranée

### Honoraires Brantham
CA 3,1 M€ → grille **7 k€ acompte + 7 k€ succès = 14 k€ HT** (côté
repreneur), cf. [[founder/decisions/2026-04-24-pricing-7k-7k-petits-tickets]].

Voir [[brantham/deals/identified/2026-05-15-tech-valley]] (à créer).

## 4. Apprentissages méthodologiques

### Nouvelles plateformes ajoutées au scope
- **dataroom.fhbx.eu** (cabinet FHBX, AJ Sud France) — page React SPA, le
  WebFetch reste utilisable, pas de teaser image (texte structuré direct)

### Études AJ rencontrées
- SCP AJ Meynet & Associés (Lyon) — déjà connu
- SELARL FHBX (16 bureaux dont Perpignan) — Me Eric Samson Perpignan
- SELARL MJSA (Perpignan) — Me Aguilé Santodomingo
- SELARLU Martin (Lyon) — Me Pierre Martin

### Patterns d'enquête validés
1. **Le teaser image contient les preuves** (CA à l'euro près, loyers,
   sites précis, effectif réel)
2. **Le filtre activité BODACC manque souvent** car NAF déclaré générique
   (MONABEE = 4321A "installation électrique" pas "photovoltaïque")
3. **Le siège affiché peut être arrondi** (Lyon = Dardilly ; Perpignan =
   Toulouges)
4. **Période d'observation longue = signal repreneur faible** → opportunité
   pour Brantham comme intermédiaire
5. **Nominations dirigeants juste avant cessation paiements** = signal de
   restructuration ratée pré-RJ

## Decisions

- Skill `osint-deanon` installé localement + archivé pour partage
- Pattern `osint-deanon-cession-anonyme` documenté dans le vault Brantham
- Index MOC-patterns mis à jour
- Entry MEMORY.md ajoutée

## Bugs / Pièges nouveaux

Aucun bug logiciel — tous les pièges sont déjà documentés dans le playbook
du skill.

## Next steps

- [ ] Créer fiche deal `[[brantham/deals/identified/2026-05-13-monabee]]`
- [ ] Créer fiche deal `[[brantham/deals/identified/2026-05-15-tech-valley]]`
- [ ] Si confirmation user : note d'opportunité Brantham + outreach repreneurs
  pour MONABEE (deadline 19/06/2026) et TECH VALLEY (deadline 05/06/2026)
- [ ] Si scope élargi demandé : v2 du skill OSINT (UK/US/personnes/infra)

## Related

- [[brantham/_MOC]]
- [[brantham/patterns/osint-deanon-cession-anonyme]]
- [[_system/MOC-patterns]]
- [[_system/MOC-master]]
- [[founder/decisions/2026-04-24-pricing-7k-7k-petits-tickets]]
- [[brantham/context/realite-business]]
