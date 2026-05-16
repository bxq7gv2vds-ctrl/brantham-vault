---
type: session
project: brantham
date: 2026-05-16
tags: [tc-paris, redaction-offre, kit, tests-statistiques, deal-execution]
---

# Session 2026-05-16 — TC Paris : kit de rédaction d'offre + pressage statistique final

Suite de la session [[brantham/sessions/2026-05-15-tc-paris-extraction-complete]]. Deux livrables : un kit de rédaction d'offre modulaire pour les clients-repreneurs, et un pressage statistique qui épuise le corpus.

## Récap

### 1. Revue de la couche rédactionnelle
Audit des 4 documents rédactionnels existants : [[brantham/tc-paris-extraction/analyses/playbook-redaction-offre]] (process), [[brantham/tc-paris-extraction/analyses/synthese-phase2/05-recettes-rhetoriques-structure]] (forme), [[brantham/tc-paris-extraction/analyses/synthese-phase2/09-bibliotheque-extraits]] (verbatims), [[brantham/tc-paris-extraction/analyses/synthese-phase2/08-grille-scoring-100pts]] (contrôle). Constat : solide sur le fond mais statique, et pas d'outil exécutable pour rédiger une offre.

### 2. Création du kit de rédaction d'offre
Nouveau fichier [[brantham/templates/kit-redaction-offre-reprise]]. Choix validé avec le user : pas un template à trous figé, mais un kit modulaire. Chaque offre étant différente (périmètre, secteur, concurrence), le kit donne pour chaque section des variantes selon la typologie de deal + des décisions à arbitrer + les pièges. Structure : étape 0 de qualification (6 typologies), 10 sections détaillées, auto-scoring /100, kill-switches, boucle d'amélioration.

### 3. Pressage statistique final (livrable 11)
But : garantir qu'on ne peut plus rien tirer du corpus sans donnée neuve. Agent général lancé sur les pickles + JSON. Nouveau livrable [[brantham/tc-paris-extraction/analyses/synthese-phase2/11-tests-statistiques-et-analyses-residuelles]] + script rejouable `_compute_tests.py`.

## Résultats du pressage

- **Tests formels** : 39/53 variables significatives à p<0,05. Les 10 prédicteurs clés validés à p<0,001. Prix non discriminant reconfirmé (p=0,94).
- **6 faux deltas démasqués** : `incorporels` (le "x5" disparaît), `corporels`, `bp_3ans_present`, `exec_summary`, `faculte_substitution_precise`, `L642_12_al4`. À ne plus citer comme arguments.
- **Robustesse confirmée** : en retirant les 150 extractions douteuses, les patterns de tête tiennent (écart max 3,7 pts).
- **Délai v1→v2 des offres améliorées** : médiane 26 jours, IQR 21-38 (n=23/42). Donnée calendaire neuve pour le planning Brantham.
- **Grille /100 contre-vérifiée par ML** : régression logistique L2, accuracy CV 0,81 / AUC 0,89. La grille expert ne rate aucun prédicteur.
- **Cabinet d'avocats et AJ non testables** : le corpus est dominé par des méga-dossiers qui confondent l'identité de l'acteur avec celle du dossier (LEXCAP/FIDAL = un seul bloc INNATIS). Limite structurelle, pas un manque d'effort.

## Verdict

Le corpus actuel (566 offres, 154 décidées) est **statistiquement épuisé**. Aucune analyse intra-corpus à forte valeur ne reste. Trois questions exigent de la donnée externe : lien cabinet-avocat / AJ ↔ succès (corpus multi-tribunaux nécessaire), suivi post-cession (le corpus capte la promesse, pas l'exécution), et les 385 offres en attente (audiences 2026).

## Décisions prises

- Adoption du kit de rédaction modulaire comme outil standard Brantham pour rédiger les offres côté client-repreneur.
- Le corpus TC Paris est clos en analyse ; prochaine réouverture conditionnée à de la donnée neuve (audiences 2026, suivi post-cession, autres tribunaux).

## En attente de décision user

- Appliquer 2 dé-pondérations à la grille `08-grille-scoring-100pts.md` : retirer le poids d'`exec_summary` (F.2) et de `faculte_substitution` (E.6), basculer le poids du bloc C de "BP présent" vers "hypothèses prudentes". Recommandé par le livrable 11, non appliqué.

## Next steps (hérités de la session précédente, toujours ouverts)

- Transformer la grille /100 en outil Notion/Excel remplissable par Soren
- Setup cron quotidien pour le scraping TC Paris
- Outreach des 30 repreneurs récurrents
- Re-actualiser quand les 385 offres en attente passent en audience

## Related

- [[brantham/_MOC]]
- [[brantham/sessions/2026-05-15-tc-paris-extraction-complete]]
- [[brantham/tc-paris-extraction/_INDEX]]
- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/templates/kit-redaction-offre-reprise]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/11-tests-statistiques-et-analyses-residuelles]]
- [[brantham/tc-paris-extraction/analyses/synthese-phase2/08-grille-scoring-100pts]]
- [[brantham/tc-paris-extraction/analyses/playbook-redaction-offre]]
