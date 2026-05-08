---
type: protocol
project: brantham
status: active
date: 2026-05-08
tags: [mastery, programme, 1h30, intensif]
---

# Programme intensif — 1h30/jour pendant 30 jours

> Pour aller du "j'ai lu les fiches" au "je sors les chiffres et les articles sans hésiter dans un call". Discipline daily.

## Le format 6×15 min

```
🕐 0-15 min : DRILL JURIDIQUE (fiche du jour, Couches 0-5)
🕐 15-30 min : CAS PRATIQUE FINANCIER (analyse chiffrée)
🕐 30-45 min : RESTITUTION ORALE (à voix haute, chrono)
🕐 45-60 min : QUESTION PIÈGE (réponse complète + recherche)
🕐 60-75 min : LECTURE BIBLIOGRAPHIQUE (Le Corre / Vallansan)
🕐 75-90 min : CROSS-LINK + LOG (anti-oubli + journal)
```

## Phase par phase (détail)

### Phase 1 — Drill juridique (15 min)
- Ouvre la fiche du jour selon [[brantham/mastery/curriculum]]
- Lecture active : surligne 3 chiffres / articles / distinctions clés
- Ferme la fiche, écris de mémoire les 3 points
- Vérifie

**Output attendu** : 3 points écrits sans regarder, validés.

### Phase 2 — Cas pratique financier (15 min)
Selon le jour :
- **J1-J7** (Couche 0) : prendre un bilan PME via Pappers, repérer les 5 lectures critiques
- **J8-J12** (Couche 1) : analyser une offre de cession publiée (Camaieu, Go Sport, etc.)
- **J13-J17** (Couche 2) : suivre un dossier en cours via la presse spécialisée (Les Echos, BJE)
- **J18-J21** (Couche 3) : examiner un PSE en RJ
- **J22-J25** (Couche 4) : faire un retraitement EBITDA sur cas Magic Form ou ITFI
- **J26-J28** (Couche 5) : étudier une purge de sûretés réelle

**Sources data** :
- Pappers MCP (bilans publics)
- BODACC pour annonces récentes
- Cas pratiques cités dans Le Corre Dalloz
- Notre vault `vault/brantham/deals/active/` (Magic Form, ITFI)

**Output attendu** : memo 5 lignes "ce que j'ai vu sur ce dossier".

### Phase 3 — Restitution orale (15 min)
- Imagine que tu as un repreneur en face
- Réponds à 3 questions à voix haute, chronométrées :
  1. "C'est quoi un [sujet du jour] ?" — 60 sec
  2. "Quelle est la subtilité importante ?" — 90 sec
  3. "Donne-moi un exemple concret" — 90 sec
- Refais 2 fois jusqu'à fluidité

**Test du miroir** : si hésitation > 2 sec au milieu d'une phrase, recommence.

### Phase 4 — Question piège (15 min)
- Va au bas de la fiche du jour
- Réponds à la question piège, à voix haute, sans regarder
- Si tu doutes : rouvre la fiche, lis la réponse modèle, refais
- Repère le **vocabulaire pro** que tu as raté
- Ajoute 1-2 termes à ton lexique perso

**Output attendu** : tu sors la réponse en 75 sec, fluide.

### Phase 5 — Lecture bibliographique (15 min)
**Sans les livres physiques** (en attendant l'achat) :
- Lis 1 chapitre de [[brantham/knowledge/legal/plans-de-cession]] ou autre source vault correspondant au jour
- Note 3 phrases / formules d'auteurs (à citer plus tard)

**Avec les livres** (après achat Tier S) :
- 15 min lecture **Le Corre Mémento** ou **Antonini-Cochin** (Couche 0-1)
- Surligne 3 idées force
- Note un "snippet citable" pour parler comme un pro

### Phase 6 — Cross-link + log (15 min)
**Cross-link (10 min)** :
- Ouvre une fiche d'un sujet déjà drillé (J-1, J-3, J-7)
- Restitue oralement en 60 sec sans regarder
- Note ce qui a coincé
- Re-révise le passage faible

**Log (5 min)** :
- Écris 1 ligne dans `vault/brantham/mastery/log-mastery.md`
- Format : `J<n> (date) : <sujet> — fiche OK/NOK, oral <durée>, cas pratique <résumé>, citation <auteur>. Difficulté: <ce qui a coincé>`

## Programme ajusté par couche

### Couches 0-1 (J1-J12) — Fondations + Plan de cession
**Focus** : maîtrise du Code de commerce L631-L642, acteurs, calendrier
**Cas pratique** : analyser bilans Pappers + offres publiques cession
**Lecture** : Antonini-Cochin (vue d'ensemble) puis Le Corre Mémento (procédures)

### Couches 2-3 (J13-J21) — Process + Social
**Focus** : process AJ/MJ/tribunal + L1224-1 + AGS + PSE
**Cas pratique** : suivre un dossier réel via BJE / Les Echos
**Lecture** : Le Corre Droit social procédures collectives

### Couches 4-5 (J22-J28) — Finance + Sûretés
**Focus** : multiples, retraitements, BFR, purge sûretés, fiscalité
**Cas pratique** : retraitement EBITDA sur Magic Form, ITFI, ou Pappers
**Lecture** : Cabrillac/Pétel Sûretés + chapitres finance Le Corre

### Couche 6 (J29-J30) — Cas pratiques
**Focus** : intégration de tout via cas emblématiques
**Cas pratique** : Camaieu, Orpea, Casino — refaire le scoring
**Lecture** : revue rapide de toutes les fiches

## Le drill du week-end (3h, optionnel mais recommandé)

**Samedi matin** : revue complète de la semaine
- Refaire les 6 fiches de la semaine sans regarder (test 90 min)
- Identifier les 3 plus grandes faiblesses
- Drill ciblé sur ces 3 points (60 min)
- Cas pratique transverse (30 min)

**Dimanche** : repos OU mock call de 30 min
- Tu joues toi, je joue le repreneur (grade A, B ou C)
- Je te pose des questions piège
- On débrief ensemble dans la session suivante

## Outils

- [[brantham/mastery/_MOC]] — programme complet
- [[brantham/mastery/curriculum]] — fiche du jour
- [[brantham/mastery/fiches/_index]] — toutes les fiches
- [[brantham/mastery/finance/_MOC]] — module finance
- [[brantham/mastery/lexique-pro]] — vocabulaire
- [[brantham/mastery/data-marche/stats-2025]] — chiffres marché
- [[brantham/mastery/log-mastery]] — journal quotidien
- [[brantham/mastery/quiz/_index]] — quiz hebdo
- [[brantham/mastery/bibliographie]] — livres à acheter

## Métriques de progression

| Indicateur | Cible J7 | Cible J14 | Cible J21 | Cible J30 |
|------------|----------|-----------|-----------|-----------|
| Quiz Couche 0 | 18/20 | — | — | — |
| Quiz Couche 1 | — | 18/20 | — | — |
| Quiz Couche 2 | — | — | 18/20 | — |
| Test final | — | — | — | 9/10 |
| Fluidité orale (60-90 sec/sujet) | 50 % | 70 % | 85 % | 95 % |
| Sortir 5 articles Code commerce sans regarder | 3 | 8 | 15 | 25 |
| Citer 1 auteur de référence sur un sujet | 1 | 3 | 5 | 8 |

## Si tu sautes un jour
- Tu **rattrapes le lendemain en doublant** (3h au lieu de 1h30)
- Pas plus de 2 jours sautés sinon décrochage cumulatif
- Si décrochage > 3 jours → repars de la dernière fiche solide

## Variante intensive 2h/jour (si possible week-ends)
**Bonus 30 min** :
- Lecture BJE / Revue procédures collectives (10 min)
- Suivi jurisprudence Cass. com. récente (10 min)
- Vocabulaire pro : 5 termes nouveaux à utiliser (10 min)

## Règle d'or

**Tu n'as pas appris tant que tu ne peux pas l'expliquer à un repreneur sans hésiter ET sans regarder tes notes.**

Le test ultime : un repreneur grade A te pose 3 questions surprise sur le sujet. Tu réponds en 60-90 sec, avec article du Code, jurisprudence, exemple, et tu **sonnes comme un pro qui a vu 30 dossiers**. Pas comme un étudiant qui récite.

## Related
- [[brantham/mastery/_MOC]]
- [[brantham/mastery/curriculum]]
- [[brantham/mastery/drill-quotidien]]
- [[brantham/mastery/log-mastery]]
