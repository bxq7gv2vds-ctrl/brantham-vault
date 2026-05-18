---
type: fiche-produit
deal: open-bee-france
date: 2026-05-18
analyste: Brantham Partners
cote: repreneur
statut: complement
sources: "brochure_corporate_open_bee_web.pdf · organigramme_general_vf_27_02_2026.pdf · dépôts APP/IDDN · lot-6-detail"
---

# FICHE PRODUIT — OPEN BEE SUITE

> **Note complémentaire repreneur.** L'analyse de la data room (lots 1 à 9) traite le logiciel
> sous l'angle juridique (titularité, verrou suisse). Cette fiche caractérise le **produit comme
> actif** : que fait-il, comment est-il construit, comment se vend-il, où se situe-t-il sur son
> marché. Un repreneur achète Open Bee d'abord pour ce produit — il doit savoir ce qu'il achète.
>
> ⚠️ Les chiffres « marketing » (utilisateurs, langues, R&D) viennent de la **brochure
> corporate** — document promotionnel **non audité**, à prendre comme ordre de grandeur, pas
> comme donnée vérifiée.

---

## 1. LE PRODUIT EN UNE PHRASE

Open Bee édite une **plateforme de GED / ECM** (gestion électronique de documents / gestion de
contenus d'entreprise) en mode **SaaS cloud**, hébergée dans un data center français, qui
dématérialise, classe, sécurise, fait circuler et archive les documents d'une organisation —
factures, bulletins de paie, contrats, formulaires — avec un volet **facture électronique**
(voir [[dataroom/12-facture-electronique]]).

Positionnement marché : **éditeur GED français de milieu de gamme**, vendu très majoritairement
via un **canal indirect de partenaires** (constructeurs d'imprimantes/copieurs et intégrateurs IT).

---

## 2. IDENTITÉ PRODUIT (chiffres brochure — non audités)

| Élément | Donnée brochure | Lecture repreneur |
|---|---|---|
| Nature | Éditeur français, siège opérationnel Annecy/Epagny | Cohérent avec le RCS |
| Ancienneté | « Spécialiste GED depuis 15+ ans » | Marque/produit datant de 2008-2009 — antériorité réelle |
| Base utilisateurs | « 250 000 utilisateurs dans le monde » | Chiffre marketing — **à recouper avec le parc de contrats actifs** (≠ 3000 clients) |
| Couverture | Solution disponible en **12 langues** ; représentations Europe/Asie/Afrique | La licence suisse limite pourtant l'exploitation à l'UE (cf. [[dataroom/lot-6-detail]]) — **contradiction export à instruire** |
| R&D | « 13 % du CA réinvesti en R&D » | Cohérent avec la production immobilisée capitalisée — voir réserves CAC ([[dataroom/lot-1-financier]]) |
| Effectif | « 100+ employés » | Pré-RJ ; effectif réel post-PSE ~46 (cf. [[dataroom/lot-8-social]]) |

---

## 3. FONCTIONNALITÉS — CE QUE FAIT LA SUITE

La brochure décrit **13 briques fonctionnelles**. Pour un repreneur, elles se regroupent en
4 familles :

**A. Capture & entrée documentaire**
- **Classement** — numérisation depuis scanner/multifonction, rangement en arborescence.
- **Smart Capture** — reconnaissance et extraction automatique des données (LAD/RAD) par un
  « moteur d'intelligence artificielle ». C'est le module à plus forte valeur technologique.
- **E-Form** — conception et diffusion de formulaires électroniques.

**B. Gestion & collaboration**
- **Gestion documentaire** — coffre central, droits d'accès paramétrables.
- **Recherche** — moteur de recherche plein texte.
- **Espaces de travail connectés** — espaces collaboratifs (co-édition, commentaires).
- **Circuits de validation** — workflows d'approbation linéaires ou conditionnels.
- **Mobilité** — application mobile.

**C. Conservation & valeur probante**
- **Cycle de vie** — gestion de la rétention (conservation / destruction / masquage à échéance).
- **Archivage à vocation probatoire** — coffre-fort électronique certifié **NF 203**
  (signature électronique, horodatage, scellement numérique).

**D. Intégration & sorties**
- **Intégration** — web services pour connecter la GED aux applications métiers (ERP, finances,
  RH, vente, logistique).
- **Analytics** — tableaux de bord d'usage.
- **Signature électronique** — simple ou avancée.
- Sorties : impression, intranet/extranet, email, espaces sécurisés, accès mobile, **Chorus Pro**
  (facturation du secteur public — antériorité e-facture, voir [[dataroom/12-facture-electronique]]).

**Cas d'usage commercialisés** : dématérialisation des factures fournisseurs, des factures
clients, des bulletins de paie et dossiers RH, des formulaires ; intranet ; partage sécurisé ;
archivage probatoire.

---

## 4. ARCHITECTURE — 4 LIGNES DE PRODUIT

L'organigramme R&D (27/02/2026) et les dépôts APP confirment une **suite modulaire à 4 composants** :

| Module | Rôle | Dev France | Dev Tunisie |
|---|---|---|---|
| **Capture** | LAD/RAD, extraction IA | Aurélien Duraz, F. Balzan, A. Avet | équipe lead/devs |
| **Portal** | portail web GED (cœur applicatif) | Yoann Lecointe | équipe lead/devs |
| **Mobile** | application mobile | Florian Eymard | équipe lead/devs |
| **.net** | brique/connecteurs .NET | Nicolas Romedenne (chef de projet/dev .net) | — |

- Produit déposé sous le nom **« OPEN BEE Suite logiciel »**, versions **6.13** (14/10/2022) et
  **6.14** (04/10/2023) — APP/IDDN au nom d'Open Bee France (cf. [[dataroom/lot-6-detail]]).
- **Architecte logiciel** : Ahmed Cherif Krid (Tunisie).
- Présence d'un module **.net** + **2 ingénieurs chercheurs IA développeurs C++** (Tunisie) →
  stack hétérogène (.NET/C# côté connecteurs, C++ côté moteur IA, web côté Portal).

🔴 **Point d'audit technique non tranché par la data room** : quelle part du code v6.x est une
**réécriture propre post-2008** (titularité Open Bee France) vs **dérivée des 7 logiciels MB2I de
2008** (revendicable par l'entité suisse) ? L'avenant 2018 chiffre ~50 % de la valeur logicielle
comme « développée par la SARL ». Une **expertise de code indépendante** est recommandée avant
l'offre — c'est ce qui détermine si l'actif « logiciel » est sécurisable. Voir
[[dataroom/00b-addendum-decouvertes]] §2.4.

---

## 5. CERTIFICATIONS & LABELS — UN ACTIF DE CRÉDIBILITÉ

| Label | Objet | Valeur pour le repreneur |
|---|---|---|
| **NF Logiciel NF 203** (AFNOR) | Coffre-fort numérique / archivage probatoire | Label rare, exigé sur les marchés réglementés — à vérifier toujours en vigueur |
| **Conformité RGPD** | Traitement des données | Affiché ; mais le registre RGPD interne nie des données personnelles sur le traitement « Gestion clients » — **affirmation fausse** (cf. [[dataroom/lot-6-detail]]) |
| **ISO 27001** | Sécurité de l'information | Porté par Vincent Boyer (organigramme) — vérifier le **statut de la certification** (en cours ? obtenue ? échéance ?) |
| Hébergement | Data center français, redondance, accès 24/7 | = contrat **Cloud Orange** — risque de coupure traité en [[dataroom/lot-5-contrats]] |
| **Agrément PA DGFIP** | Facture électronique | Voir note dédiée [[dataroom/12-facture-electronique]] |

Les labels (NF 203, ISO 27001, agrément PA) sont des **actifs immatériels réels** : longs à
obtenir, ils crédibilisent le produit sur les marchés exigeants. Mais chacun est **attaché à une
entité / à des conditions** — leur survie au plan de cession doit être vérifiée une à une.

---

## 6. MODÈLE DE DISTRIBUTION — LE CANAL EST LE VRAI ACTIF COMMERCIAL

Open Bee ne vend presque pas en direct. La structure commerciale (organigramme) est bâtie
**autour du canal indirect** :

- **BU partenaires premium & constructeurs** (J. Vaillant) — **Konica Minolta + Toshiba**. Les
  fabricants de copieurs/multifonctions revendent la GED Open Bee bundlée à leurs machines.
- **BU intégrateurs IT & éditeurs** (S. Vincent) — revendeurs et éditeurs tiers, dont la Suisse.
- **BU ETI & grands comptes** / **BU TPE-PME** — vente directe résiduelle.
- **IT partners success manager** dédié Konica Minolta / Toshiba.

→ **La balance comptable confirme la dépendance au canal** : compte « LIC CLOUD KM »
(Konica Minolta) = **1 268 K€**, soit ~1/5 du CA cloud ; le compte anonyme « LIC CLOUD AUTRE
PARTENAIRE » = **2 093 K€** (~1/3 du CA), non détaillé. Voir [[dataroom/lot-1-detail]].

🔴 **Conséquence repreneur** : le risque produit n° 1 n'est pas technique, c'est **la fuite des
partenaires distributeurs**. Konica Minolta et Toshiba sont des géants qui peuvent basculer leurs
clients vers une GED concurrente. Le RJ d'Open Bee est un signal qui les incite à se couvrir. Il
faut **sécuriser les contrats partenaires** (clauses de changement de contrôle, exclusivités,
poids réel) et identifier qui se cache derrière le compte « AUTRE PARTENAIRE » de 2 M€.

---

## 7. POSITIONNEMENT CONCURRENTIEL

Marché : **GED / ECM milieu de gamme en France** — marché mûr, fragmenté, en consolidation,
dopé par l'obligation de facture électronique.

| Concurrent | Profil | Remarque |
|---|---|---|
| **Sages Informatique (Zeendoc)** | GED PME française, leader du segment | **Adversaire dans un litige Open Bee** (contrefaçon de marque + Google Ads, cf. [[dataroom/lot-7-contentieux]]) — concurrent frontal direct |
| DocuWare, M-Files | GED/ECM internationales | Montée en gamme |
| Yooz, Esker, Tiime | Spécialistes dématérialisation facture / P2P | Concurrence sur le volet e-facture |
| Multigest, Zeendoc, DocuShare (Xerox) | GED diffusées par les constructeurs | Concurrents **sur le même canal** copieurs |

**Forces du produit** : suite fonctionnellement complète, certifications rares (NF 203), canal
constructeurs installé, brique IA (Smart Capture), agrément facture électronique.
**Faiblesses** : éditeur sous-capitalisé en RJ, pas de différenciation technologique affichée,
techno potentiellement vieillissante (socle 2008), dépendance R&D Tunisie, marque fragilisée
(litige Zeendoc + verrou suisse).

---

## 8. LECTURE REPRENEUR — SYNTHÈSE

**Ce que le repreneur achète réellement, côté produit :**
1. Une **suite GED/ECM complète et opérationnelle** servant ~3000 clients — pas un prototype.
2. Des **certifications** (NF 203, agrément PA) qui prennent des mois/années à obtenir.
3. Un **canal de distribution constructeurs** (Konica, Toshiba, Xerox) impossible à recréer de zéro.
4. Une **brique IA de capture** (Smart Capture) — la partie la plus moderne.

**Ce qui doit rester froid :**
- Le produit n'est **pas un actif technologique de rupture** — c'est une GED solide mais banalisée,
  sur un socle ancien. La valeur est dans la **base installée + le canal + les labels**, pas dans
  un avantage technique défendable.
- La **dépendance R&D Tunisie** est totale : sans cette équipe, pas de maintenance ni d'évolution
  (cf. [[dataroom/lot-6-detail]] §dépendance Tunisie).
- La **titularité du code** n'est pas purgée (verrou suisse) — l'actif logiciel n'est sécurisable
  qu'après accord avec EXO B Capital / expertise de code.

**À auditer avant l'offre (en plus des angles morts du [[dataroom/00-analyse-complete]] §11) :**
- Statut en vigueur des certifications NF 203 et ISO 27001 (échéances, périmètre, transférabilité).
- Roadmap produit et dette technique réelle du socle v6.x.
- Architecture d'hébergement et réversibilité (dépendance au Cloud Orange).
- Identité du partenaire « AUTRE PARTENAIRE » (2 M€) et solidité des contrats Konica/Toshiba.

---

## Related
- [[dataroom/_MOC]]
- [[dataroom/00-analyse-complete]]
- [[dataroom/00b-addendum-decouvertes]]
- [[dataroom/12-facture-electronique]]
- [[dataroom/10-strategie-reprise]]
- [[dataroom/lot-1-detail]]
- [[dataroom/lot-6-detail]]
- [[dataroom/lot-6-juridique]]
- [[dataroom/lot-7-contentieux]]
- [[dataroom/lot-8-social]]
- [[brantham/deals/active/open-bee-france/_MOC]]
