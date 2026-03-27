---
type: knowledge
project: brantham
category: sectors
topic: tech et startups en M&A distressed
level: avance
created: 2026-03-27
updated: 2026-03-27
sources:
  - https://www.ey.com/fr_fr/newsroom/2026/02/bilan-defaillances-dentreprises-en-france-en-2025
  - https://www.scalex-invest.com/blog/navigating-post-series-a-bankruptcies-in-the-french-tech-ecosystem
  - https://www.scalex-invest.com/blog/understanding-post-series-a-bankruptcies-in-the-french-tech-ecosystem-insights-from-scalex-invest
  - https://www.exponens-croissance.com/french-tech-2026-le-passage-de-leuphorie-a-la-maturite-exigeante/
  - https://www.frenchweb.fr/startups-ce-que-dit-vraiment-le-rapport-de-la-banque-de-france/457175
  - https://www.optionfinance.fr/actualites/hausse-des-defaillances-chez-les-start-up-de-la-french-tech.html
  - https://www.lemondeinformatique.fr/actualites/lire-plus-de-defaillances-en-2024-pour-les-start-ups-it-francaises-96302.html
  - https://www.frenchweb.fr/startups-francaises-les-acquisitions-discretes-mais-strategiques-de-mai-2025/455020
  - https://www.le-ticket.fr/le-guide-2025-des-bspce-en-startup-les-12-questions-pour-tout-comprendre-et-ne-pas-se-faire-enfumer/147052/
  - https://actify.fr/secteurs/annonces-secteur-startup-tech/
---

# Tech et Startups -- Playbook Sectoriel M&A Distressed

> Fiche operationnelle Brantham Partners. Derniere MAJ : 27 mars 2026.

---

## 1. Panorama sectoriel

### Chiffres cles defaillances

| Indicateur | Valeur 2025 | Source |
|---|---|---|
| Defaillances info/communication | **~2 500** | Altares |
| Part des defaillances totales | **~4%** | Altares |
| vs moyenne 2010-2019 | **+40%** | EY |
| Startups post-Series A en difficulte | **82** (12 mois glissants fin Q1 2025) | ScaleX Invest |
| Taux de LJ directe startups | **70%** | Banque de France |
| Multiple median valuation tech EU | **4,73x revenues** (-18% sur 1 an) | Caption Market |

### Profil type de la startup en difficulte

| Caracteristique | Detail |
|---|---|
| Levee de fonds | Series A-B (5-30M EUR) |
| Burn rate | 200-500K EUR/mois |
| Runway | < 6 mois |
| Derniere levee | > 18 mois |
| Modele | B2B SaaS ou deep-tech |
| Cause de defaillance | Pas de product-market fit, ou burn > revenues |

### Sous-segments

| Segment | Risque | Tendance |
|---|---|---|
| SaaS B2B | Modere | Correction, mais modele recurring viable |
| Deep-tech / hard-tech | Eleve | Burn rate insoutenable (Ynsect, Carmat) |
| Fintech | Modere | Consolidation, rachat par banques |
| Healthtech/medtech | Eleve | Cycle reglementaire long, cash burn |
| Agritech | Eleve | Gap industrialisation trop cher |
| E-commerce / marketplace | Eleve | Marges comprimees, concurrence |
| Cybersecurite | Faible | Marche porteur, acqui-hires frequents |
| IA/ML | Faible a modere | Hype mais monetisation incertaine |

---

## 2. Specificites sectorielles

### Valorisation de la PI (Propriete Intellectuelle)

La PI est souvent le **principal actif** d'une startup tech en difficulte. Elle comprend :

| Type PI | Exemples | Valorisation distressed |
|---|---|---|
| **Brevets** | Algorithmes, procedes techniques | 10-30% de la valeur going concern. Royalties capitalisees (3-5 ans) |
| **Code source** | Logiciel, plateforme SaaS | Cout de reproduction - dette technique. Si code propre : 30-50% du cout de dev |
| **Marque** | Nom, domaine, notoriete | 0 si startup inconnue. Valeur du domaine + base users si notoriete |
| **Donnees** | Base clients, datasets, modeles entraines | Valeur RGPD-compliant uniquement. Donnees proprietaires = actif strategique |
| **Savoir-faire** | Documentation, process, equipe | Non transferable sans les personnes cles |
| **Licences** | Licences logicielles, API, partenariats | Verifier la cessibilite des licences |

**Point cle** : en LJ, les actifs PI sont vendus aux encheres ou de gre a gre par le liquidateur. Les prix sont souvent 5-15% de la valorisation du dernier tour de table. C'est le terrain de jeu des acqui-hires.

### ARR vs Burn Rate

| Metrique | Seuil sain | Red flag distressed |
|---|---|---|
| **ARR growth** | > 50% YoY | < 20% ou stagnant |
| **Net Revenue Retention** | > 110% | < 90% (churn net) |
| **Burn multiple** | < 2x (burn/ARR growth) | > 4x |
| **Runway** | > 12 mois | < 6 mois |
| **CAC payback** | < 18 mois | > 24 mois |
| **LTV/CAC** | > 3x | < 1,5x |
| **Gross margin** | > 70% (SaaS) | < 50% |

**Analyse Brantham** : une startup avec un ARR de 1-5M EUR, un burn de 300K/mois et 3 mois de runway = cible typique. Si le produit a du PMF (NRR > 100%, clients qui renouvellent), le fonds de commerce tech a de la valeur.

### Dette technique

La dette technique est le **passif cache** des startups :

- Code non documente, architecture monolithique, pas de tests
- Dependance a des frameworks obsoletes ou a un dev unique
- Infrastructure sur-dimensionnee (cloud burn = 20-40% du burn total)
- Securite negligee (pas d'audit, pas de pentests)

**Due diligence technique** : faire auditer le code par un CTO externe (2-5 jours). Evaluer le cout de remise a niveau (refactoring, migration, securisation).

### BSPCE (Bons de Souscription de Parts de Createur d'Entreprise)

| Aspect | Detail |
|---|---|
| Nature | Options d'achat d'actions reservees aux salaries de startups |
| En procedure collective | Les BSPCE deviennent **sans valeur** si l'entreprise est liquidee (actions = 0) |
| Impact repreneur | Le repreneur **n'herite pas** des BSPCE. Il peut emettre de nouvelles stock-options. |
| Statistique | **75% des BSPCE ne sont jamais exerces** (depart, echec, conditions non remplies) |
| Acqui-hire | Les salaries qui avaient des BSPCE perdent tout. Le repreneur peut proposer de nouvelles conditions. |

### Acqui-hire : racheter l'equipe

L'acqui-hire est la forme de M&A la plus frequente pour les startups en difficulte :

| Element | Detail |
|---|---|
| **Principe** | Racheter l'entreprise (ou ses actifs) principalement pour **recruter l'equipe** |
| **Prix** | Souvent < 1M EUR. Parfois gratuit (reprise des salaires uniquement) |
| **Structure** | Rachat du fonds de commerce (PI + contrats de travail) ou rachat de la societe a l'euro symbolique |
| **Risque** | Les salaries cles partent apres la reprise. Prevoir des clauses de retention (bonus, earn-out, nouvelles BSPCE) |
| **Volume** | 20 startups acquises en procedure d'insolvabilite en 2024 parmi celles ayant leve > 5M EUR |
| **Tendance** | Les operations discrètes M&A mid-market tech augmentent en 2025 (source FrenchWeb) |

---

## 3. Risques cles

### Risques eliminatoires

| Red flag | Impact | Verification |
|---|---|---|
| **Pas de PI propre** (tout en open source) | Rien a acheter | Audit PI |
| **Dependance a 1-2 developpeurs** | Risque de perte totale post-reprise | Entretiens equipe |
| **Infrastructure non transferable** | Lock-in fournisseur (AWS credits, Google partnership) | Audit infra |
| **Litiges PI** (brevet contrefait, licence violee) | Passif potentiel | Freedom-to-operate analysis |
| **Donnees clients non RGPD-compliant** | Amendes CNIL, invendable | Audit RGPD |

### Risques a maitriser

- **Churn clients** : en procedure collective, les clients SaaS migrent vite. Agir en < 30 jours.
- **Cloud costs** : AWS/GCP/Azure = 30-50K EUR/mois pour une startup en croissance. Optimisable a -50%.
- **Contrats SaaS entrants** : verifier les licences logicielles utilisees (open source, SAAS vendors, API). Sont-elles cessibles ?
- **Equipe** : le CTO et les lead devs sont les actifs cles. S'ils partent = code orphelin.
- **Valorisation anterieure** : ne JAMAIS se baser sur la valorisation du dernier tour de table. C'est la valeur en going concern avec expectation de croissance. En distressed, diviser par 5-20x.

---

## 4. Valorisation

### Methodes privilegiees tech distressed

| Methode | Application | Reference |
|---|---|---|
| **Multiple ARR** | SaaS avec revenus recurrents | 1-3x ARR (distressed) vs 5-15x (going concern) |
| **Cout de reproduction** | Code + PI | Cout de re-developpement - dette technique |
| **Valeur base clients** | Clients actifs payants | ARPU x nombre clients x duree de vie estimee x discount |
| **Acqui-hire** | Equipe principalement | 50-200K EUR/ingenieur (cout de recrutement evite) |
| **Liquidation** | Aucun actif tangible | Materiel IT (faible) + PI aux encheres |

### Grille de valorisation rapide

| Actif | Startup pre-revenue | Startup 1-5M ARR | Startup 5M+ ARR |
|---|---|---|---|
| PI/code | 50-200K EUR | 200-500K EUR | 500K-2M EUR |
| Base clients | 0 | 0,5-1x ARR | 1-3x ARR |
| Equipe (acqui-hire) | 100-500K EUR | 200K-1M EUR | 500K-2M EUR |
| Marque/domaine | 0-10K EUR | 10-50K EUR | 50-200K EUR |
| **Total distressed** | **150K-700K EUR** | **500K-2,5M EUR** | **2-7M EUR** |

### Comparaison going concern vs distressed

| Metrique | Going concern | Distressed | Ratio |
|---|---|---|---|
| Valorisation derniere levee | 20M EUR | -- | -- |
| Valorisation distressed estimee | -- | 1-3M EUR | **5-20x discount** |
| Multiple ARR applique | 8-12x | 1-3x | /4 a /6 |

---

## 5. Exemples emblematiques France

| Entreprise | Annee | Secteur | Procedure | Issue | Enseignement |
|---|---|---|---|---|---|
| **Ynsect** | 2025 | Agritech | RJ puis LJ | Liquidation | 1,5 Md EUR de valorisation en 2022, burn insoutenable |
| **Carmat** | 2026 | Medtech | LJ | Liquidation | Coeur artificiel, R&D sans marche suffisant |
| **Lynx** | 2026 | VR/XR | LJ | Liquidation | Realite mixte, marche trop etroit |
| **Sigfox** | 2022 | IoT | RJ | Reprise UnaBiz | Licorne devaluee, PI = actif principal |
| **Devialet** | 2024 | Audio tech | RJ | Restructuration | Produit premium, pivot B2B necessaire |
| **Swile** (restructuration) | 2024 | Fintech | Restructuration | Pivot | Pas de procedure collective mais 30% licenciements |

### Patterns observes

1. **LJ directe = norme** : 70% des startups en difficulte vont directement en LJ. Pas de temps pour un RJ.
2. **Valorisation en chute libre** : la valorisation distressed est 5-20x inferieure au dernier tour.
3. **Acqui-hires discrets** : beaucoup de rachats se font sans publicite, en negociation directe avec le liquidateur.
4. **Deep-tech = plus risque** : les startups hardware/biotech/cleantech brulent plus de cash et ont moins d'actifs cessibles que les SaaS.
5. **Mid-market M&A tech emerge** : les acquisitions de startups B2B SaaS par des PME/ETI se multiplient (source FrenchWeb 2025).

---

## 6. Checklist repreneur Brantham

### Phase 1 : Quick Scan (48h)

- [ ] Identifier le modele economique (SaaS, marketplace, deep-tech, services)
- [ ] Obtenir les metriques : ARR, MRR, churn, burn rate, runway restant
- [ ] Lister la PI : brevets, code source (Github/Gitlab), marques deposees, noms de domaine
- [ ] Effectif : CTO, lead devs, profils cles. Sont-ils encore la ?
- [ ] Base clients : nombre, ARPU, taux de retention, contrats en cours
- [ ] Stack technique : langages, cloud provider, infrastructure, dette technique estimee

### Phase 2 : Due Diligence (7-14 jours)

- [ ] **PI** : titularite des brevets (INPI, OEB), assignments des developpeurs (cession PI dans le contrat de travail), licences open source utilisees, litiges
- [ ] **Code** : audit technique par un CTO externe (2-5 jours). Qualite, tests, documentation, dette technique, securite
- [ ] **Clients** : contacter les top 5 clients. Sont-ils satisfaits ? Resteront-ils apres la reprise ?
- [ ] **Infra** : couts cloud, credits cloud restants (AWS Activate etc.), transferabilite
- [ ] **Social** : contrats des salaries cles, BSPCE/BSA en cours (sans valeur si LJ), clauses de non-concurrence
- [ ] **RGPD** : conformite des donnees clients/utilisateurs, DPO designe, registre des traitements
- [ ] **Contrats SaaS** : licences logicielles entrantes, API, conditions de cessibilite
- [ ] **Table de capitalisation** : actionnaires, dettes convertibles, preferred shares, liquidation preference
- [ ] **Contentieux** : litiges en cours (PI, clients, salaries, investisseurs)

### Phase 3 : Structuration offre

- [ ] **Structure** : achat d'actifs (fonds de commerce tech) preferable au rachat de la societe (eviter passif cache)
- [ ] Perimetre : PI + contrats clients + contrats travail cles + donnees
- [ ] Prix : multiple ARR distressed + valeur PI + acqui-hire value
- [ ] Plan de retention equipe : bonus, nouvelles BSPCE/AGA, conditions competitives
- [ ] Plan de migration : infrastructure, contrats clients, communication
- [ ] Tresorerie J+1 : salaires, cloud costs, licences logicielles
- [ ] Communication : rassurer les clients (email, call), les equipes, les partenaires tech

### Points d'attention specifiques tech

- **Vitesse** : les deals tech se font en 2-4 semaines. Les clients partent vite, les developpeurs aussi.
- **Liquidation preference** : les investisseurs (preferred shares) ont priorite sur les fondateurs (common shares). En LJ, cela ne s'applique plus (tout est purge).
- **Open source** : verifier les licences (GPL = contamination, Apache/MIT = safe). Un produit base sur du GPL peut avoir des obligations de publication du code source.
- **Domain name** : le nom de domaine peut valoir plus que le code si la marque est connue.
- **Donnees** : les datasets proprietaires (entraines sur des donnees exclusives) sont un actif majeur en IA. Verifier la legalite de la collecte.

---

*Fiche compilee a partir de sources publiques (ScaleX Invest, BdF, FrenchWeb, Actify, Caption Market) et experience terrain. Usage interne Brantham Partners.*
