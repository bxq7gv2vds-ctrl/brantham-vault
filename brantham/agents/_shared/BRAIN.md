# BRAIN — Brantham Partners
_Memoire partagee entre tous les agents_
_Mis a jour : 2026-03-09_

---

## Sommaire

1. [Etat des agents](#etat-des-agents)
2. [Queue d'opportunites](#queue-dopportunites)
3. [Pipeline deals actifs](#pipeline-deals-actifs)
4. [Decisions en attente](#decisions-en-attente)
5. [Dernieres actions](#dernieres-actions)
6. [Scores qualite](#scores-qualite)
7. [Protocole de mise a jour](#protocole-de-mise-a-jour)

---

## Navigation vault

- [[AGENTS]] — Description de tous les agents
- [[OPPORTUNITIES]] — Liste des opportunites detectees par Scout
- [[PIPELINE]] — Pipeline complet des deals
- [[SOUL]] — Directives de personnalite et valeurs Brantham
- Agents : [[brantham/agents/analyst/README|Analyst]] | [[brantham/agents/scout/README|Scout]] | [[brantham/agents/director/README|Director]] | [[brantham/agents/writer/README|Writer]] | [[brantham/agents/hunter/README|Hunter]] | [[brantham/agents/enricher/README|Enricher]]
- Templates : [[deals/TEMPLATE|Deal]] | [[analyses/TEMPLATE|Analyse]]

---

## Pipeline deals actifs

| Deal | Etape courante | Agent en charge | Deadline |
|------|---------------|-----------------|----------|
| MLD (bma-multi-loisirs-distribution-mld) | HUNTER | — | 2026-03-17 |

---

## Etat des agents

| Agent    | Statut | Tache en cours | Depuis |
|----------|--------|----------------|--------|
| Director | idle   | —              | —      |
| Scout    | idle   | —              | —      |
| Analyst  | idle   | —              | —      |
| Writer   | idle   | —              | —      |
| Hunter   | idle   | —              | —      |
| Enricher | idle   | —              | —      |

---

## Queue d'opportunites

- [[deals/active/bma-multi-loisirs-distribution-mld|MLD]] → pret pour HUNTER — priorite haute

---

## Decisions en attente (→ Paul)

_(aucune)_

---

## Dernieres actions
- [2026-03-09] Director : structuration vault Obsidian — README + INDEX + templates par agent
- [2026-03-08] Migration memoire vers vault Obsidian
- [2026-02-19] Scout : veille BMA → 7 opportunites, 5 closees
- [2026-02-19] Analyst : analyses 5 deals
- [2026-02-19] Writer : teasers 4 deals

---

## Scores qualite (rempli par Director)

| Slug | Analyse/10 | Teaser/10 | Acheteurs/10 | Note Director |
|------|-----------|-----------|--------------|---------------|

---

## Protocole de mise a jour

Chaque agent DOIT mettre a jour ce fichier :

1. Au demarrage d'une tache : passer son statut a `actif`, noter la tache et l'heure
2. A chaque etape cle : ajouter une ligne dans "Dernieres actions"
3. A la fin : passer son statut a `idle`, noter le resultat

Format ligne :
```
- [YYYY-MM-DD HH:MM] [AGENT] : [action] → [resultat/statut]
```

Garder les 20 dernieres lignes max — archiver les plus anciennes.

## Related
- [[brantham/_MOC]]
