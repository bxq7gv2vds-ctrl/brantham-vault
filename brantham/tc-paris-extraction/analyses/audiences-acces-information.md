---
type: analysis
project: brantham
created: 2026-05-15
tags: [tc-paris, audiences, intelligence, sources-publiques]
---

# Audiences TC Paris — Que peut-on récupérer (et que peut-on PAS récupérer)

Question : "Les audiences sont-elles enregistrées par hasard ?"

## TL;DR
**Non, les audiences du Tribunal des Activités Économiques ne sont PAS enregistrées publiquement en France.** Mais on peut récupérer ~80% de l'information décisionnelle via 5 canaux complémentaires.

## 1. Audiences elles-mêmes — NON enregistrées

### Cadre légal
- Les audiences des **juridictions commerciales** (TC, TAE) sont **PUBLIQUES** mais **NON ENREGISTRÉES** par défaut (art. 22 NCPC).
- Seuls les jugements écrits font foi. Les débats oraux ne sont pas conservés.
- **Article 433-7 NCPC** : aucune captation audio/vidéo des audiences sans autorisation expresse du président (rarissime, jamais en commercial).
- Sanction pénale art. 38 ter de la loi du 29 juillet 1881 : 4 500 € d'amende pour captation non autorisée.

### Ce que ça change pour nous
On ne peut PAS écouter ce qu'a dit l'AJ, le repreneur ou le tribunal pendant l'audience. Notre intel se construit par d'autres canaux (voir §3).

### Workaround légal
- **Assister à l'audience en personne** : les audiences sont publiques, on peut s'asseoir au fond et prendre des notes manuscrites.
- **Calendrier** : `https://www.tribunal-de-commerce-paris.fr/agenda-audiences` (publication anticipée).
- **Stratégie Brantham** : envoyer un junior assister aux audiences sur les deals importants. Coût : 2-3h, valeur : énorme pour comprendre les arguments du tribunal.

## 2. Jugements écrits — Publics MAIS dispersés

### Publication formelle : BODACC
- Le **BODACC** publie les jugements arrêtant le plan de cession dans les **8 à 30 jours** après l'audience.
- URL : `https://www.bodacc.fr/annonce/liste?q={nom_societe}`
- API publique gratuite : `https://bodacc-datadila.opendatasoft.com/api/records/1.0/search/?dataset=annonces-commerciales`
- **Format de l'annonce** : précise le nom du repreneur retenu, le prix, et parfois les motifs.

### Exemple type d'annonce BODACC "Cession totale"
```
SOCIETE X (RCS 123 456 789)
Jugement du 15/04/2026 du Tribunal des activités économiques de Paris
Arrête le plan de cession au profit de :
  REPRENEUR Y (RCS 987 654 321)
  Prix de cession : 50 000 €
  Date d'effet : 30/04/2026
```

### Limites BODACC
- N'a souvent PAS les motifs détaillés (le tribunal motive en jugement écrit consultable au greffe sur demande)
- Le délai 8-30 jours fait qu'on apprend les jugements 1 mois après
- Le périmètre exact n'est pas toujours publié (renvoi au jugement complet)

### Récupération du jugement complet
- Demande écrite au greffe TAE Paris (`greffe@tribunal-de-commerce-paris.fr`)
- Coût : ~5-10€ par jugement
- Délai : 5-10j ouvrés
- **Valeur** : motivation complète du tribunal — gold pour comprendre les critères

## 3. Sources tierces — Construire l'intel post-audience

### Pappers — Suivi corporate du repreneur
- **Quand le repreneur est retenu**, il y a 3 signaux Pappers sous 30j :
  1. Constitution de la **NewCo** (si faculté de substitution) — RCS, capital, dirigeants
  2. **Changement dirigeant** de la société cible (parfois)
  3. **Apport en capital** ou augmentation chez le repreneur (financement de l'opération)
- Pappers MCP déjà configuré dans le vault — on peut monitorer 5+ entités/dossier.

### Presse spécialisée (par secteur)
| Secteur | Sources |
|---|---|
| **Retail / Mode** | LSA, Argus de l'Enseigne, Fashion Network, Le Journal du Textile |
| **Restauration / CHR** | L'Hôtellerie Restauration, B.R.A., Néorestauration |
| **Tech / EdTech / Digital** | Maddyness, Les Echos, FrenchWeb, Sifted |
| **Immobilier** | Business Immo, Les Echos Patrimoine, Pierre Papier, La Tribune |
| **Camping / HPA** | L'Officiel des Terrains de Camping |
| **Agroalimentaire** | LSA, Réussir, FLD |
| **M&A / Distressed** | DealMaker, Les Echos, La Lettre A, AGEFI |

### LinkedIn — Posts des dirigeants
- **Pattern** : les dirigeants des repreneurs annoncent leurs reprises sous 7-14 jours après le jugement (signal positif vis-à-vis investisseurs/équipes/clients).
- **Recherche** : `"plan de cession" OR "nous avons repris" + {nom_société}`
- **Valeur** : confirme l'identité du repreneur, donne souvent le prix et la stratégie d'intégration.

### Site web du repreneur
- Les groupes consolidateurs publient des **communiqués de presse** sur leur site (ex: SMCP, Place Dentaire/Viva Santé, IGS, Galileo).
- Section "Actualités" ou "Press releases".

### Communiqués boursiers (cotées)
- Pour les repreneurs cotés (PMV1/Cie Lebon, JCDecaux Holding, IF Group, etc.), Bourse direct / Actusnews / publications réglementées.

## 4. Construction d'un **monitoring TC Paris**

### Pipeline cible (à automatiser)
```
[CRON quotidien]
  1. Scraper la liste publique greffe-tae-paris (63 sociétés actuelles)
  2. Diff avec snapshot J-1 : 
     - NOUVEAUX → télécharger PDFs offres + extraire CSV
     - SUPPRIMÉS → potentiel jugement rendu, déclencher recherche
  3. Pour chaque dossier supprimé :
     a. Query BODACC API : "plan de cession" + nom société
     b. Search Pappers : changements actionnaires/dirigeants sur 60j
     c. Web search ciblée : presse sectorielle
     d. Notification Slack/email avec récap
  4. Auto-mise à jour vault/brantham/tc-paris-extraction/winners.csv
```

### Avantages
- Permet de mesurer la **win rate par profil de repreneur** (foncière, consolidateur, industriel...)
- Détecte les patterns gagnants en quasi-temps réel
- Source d'enrichissement continu du `playbook-redaction-offre`

## 5. Récupération HISTORIQUE des jugements (vague 1)

Sur les 94 dossiers vague 1, beaucoup sont **maintenant clos** (jugement rendu). Pour reconstituer l'intel :

### Workflow recommandé
```
Pour chaque dossier vague 1 NON présent dans la liste actuelle :
  1. BODACC query → URL annonce jugement
  2. Pappers → changements société cible + repreneurs candidats
  3. Web search → presse
  4. Cross-référencer avec nos offres CSV → identifier l'offre RETENUE
  5. Stocker dans winners.csv : {dossier, repreneur_retenu, prix_retenu, emplois_retenus, source}
```

Un agent de recherche est en cours sur 11 dossiers prioritaires (MINELLI, COSA, COLLEGE DE PARIS, SEGI, NEOCAMP, INNATIS, DENTEKA, SYM, EURODIF, PROGRESS SUP, CHEPOOKA). Résultats dans [[gagnants-tribunal]].

## 6. Ce qu'on NE PEUT PAS savoir (limites)

- **Le contenu oral des audiences** (questions des juges, défense des candidats)
- **Les notes internes** du Ministère public sur les déclarations L.642-3
- **Les motivations privées** des AJ/MJ entre eux
- **Les négociations préalables** entre les candidats et l'AJ (parfois certains candidats retirent leur offre 24h avant l'audience — Pappers ne le verra pas)
- **Les délibérés** du tribunal (huis clos)

Pour ces zones d'ombre, le seul moyen est :
- Assister à l'audience en personne (canal 1)
- Avoir un réseau d'avocats / AJ qui partagent (canal informel — c'est aussi un axe de développement Brantham)
- Demander le jugement complet au greffe (canal payant)

## 7. Roadmap Brantham — Intelligence TC Paris

### Phase 1 (immédiat, P0)
- [x] Scraping liste TC Paris ✓ (script `_scrape_tc_paris.py`)
- [x] Master CSV consolidé ✓
- [ ] Monitoring quotidien automatisé (cron + diff)
- [ ] Alerte sur nouveaux dossiers et dossiers supprimés
- [ ] Recherche BODACC automatisée pour identifier gagnants

### Phase 2 (P1, 1-3 mois)
- [ ] Pipeline d'enrichissement Pappers (suivi 30j post-jugement)
- [ ] Base de données "winners" enrichie (qui gagne, pourquoi, à quel prix)
- [ ] Système d'alerte par secteur (mode, CHR, tech, immo...)
- [ ] Backfilling vague 1 (45 dossiers décidés) via BODACC

### Phase 3 (P2, 3-6 mois)
- [ ] Stagiaire/junior pour assister aux audiences importantes
- [ ] Réseau informel avec 5-10 cabinets d'avocats AJ/MJ
- [ ] Demande systématique des jugements écrits sur les gros deals
- [ ] Modèle prédictif simple : étant donné les offres déposées, qui va gagner ?

## Related

- [[../_MOC|TC Paris MOC]]
- [[playbook-redaction-offre|Playbook rédaction]]
- [[gagnants-tribunal|Gagnants identifiés]] (en cours)
- [[../../context/process-end-to-end]]
- [[pappers_intelligence_hub|Pappers Intel]]
