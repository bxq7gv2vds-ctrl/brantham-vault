---
type: protocol
project: brantham
status: active
date: 2026-05-06
tags: [protocol, vocaux, business-profile, claude-instructions]
---

# Protocole — Vocaux continus business profile

> Comment Paul m'envoie ses vocaux pour enrichir ma compréhension Brantham, et ce que je dois faire à chaque fois.

## Quand le déclencher
Paul écrit l'un de :
- "voice note brantham" / "vocal brantham" / "vocal pour brantham"
- "j'enregistre" + contenu décousu sur la boîte
- Dépose un fichier audio dans `~/Desktop/brantham-voice/`
- Colle un transcript

## What I do (ordre strict)

### 1. Transcript
- Si audio fourni : transcrire (mlx-whisper si installé, sinon proposer install ou demander à Paul de coller le texte).
- Si texte déjà transcrit : nettoyer hésitations légères, garder fidèle.
- Sauvegarder dans `vault/brantham/context/voice-notes/YYYY-MM-DD-HHMM-slug.md` avec frontmatter `type: voice-note`.

### 2. Extraction d'insights
Identifier dans le transcript :
- **Faits nouveaux** sur le business (équipe, pricing, deals, AJ, repreneurs, process).
- **Décisions** prises ou à prendre.
- **Assumptions** à valider.
- **Customers/repreneurs** mentionnés avec retours.
- **Patterns** réutilisables.
- **Tensions/contradictions** avec ce qu'on avait avant.
- **Questions ouvertes** pour vocaux futurs.

### 3. Mise à jour _PROFILE.md
Injecter chaque insight dans la bonne section de `vault/brantham/context/business-profile/_PROFILE.md`. Si conflit avec contenu antérieur : remplacer (le plus récent fait foi) ET noter la mise à jour avec date.

### 4. Capture auto vault (selon CLAUDE.md)
- Décision → `vault/founder/decisions/YYYY-MM-DD-titre.md`
- Assumption → `vault/founder/assumptions/titre.md`
- Customer → `vault/founder/customers/YYYY-MM-DD-nom.md`
- Pattern → `vault/brantham/patterns/nom.md`
- Bug-fix process → `vault/brantham/bugs/YYYY-MM-DD-titre.md`

### 5. Mise à jour index
Ajouter ligne dans `vault/brantham/context/business-profile/voice-notes-index.md`.

### 6. Wikilinks Obsidian (obligatoire)
Chaque fichier créé doit avoir `## Related` avec :
- `[[brantham/context/business-profile/_PROFILE]]`
- `[[brantham/_MOC]]`
- Cross-links pertinents (deals, décisions, etc.)

### 7. Annonce courte à Paul
2-3 lignes max :
- "Vault: voice-note — [titre], X insights intégrés au profil."
- Lister les captures (décisions/assumptions/etc).
- 1 question de relance si gap clair (sans forcer).

## Sujets prioritaires à pousser
Si Paul demande "sur quoi je devrais te parler", proposer dans cet ordre :
1. Pourquoi Arnaud Guillem (Magic Form) a signé sans data room.
2. Profil grade A vs B vs C — différences réelles en call.
3. Relations AJ — politique long terme, qui on cultive.
4. Soren — statut, blocages, plan activation commerciale.
5. Vraies objections entendues en outreach.
6. Concurrents directs — qui prend les deals qu'on rate.
7. Erreurs/leçons des calls passés.
8. Vision fin 2026 (deals, revenu, équipe).

## Locations clés
- Living profile : `vault/brantham/context/business-profile/_PROFILE.md`
- Voice notes : `vault/brantham/context/voice-notes/`
- Index : `vault/brantham/context/business-profile/voice-notes-index.md`
- Drop folder audio : `~/Desktop/brantham-voice/`
- README protocole : `vault/brantham/context/voice-notes/README.md`

## Subtilité importante
**Ne JAMAIS résumer en surface**. Paul a explicitement dit qu'il veut que je capte les **subtilités** de la boîte — donc à chaque vocal, je dois aller chercher : tensions, contradictions, signaux faibles, non-dit. Pas seulement les faits.

Le `_PROFILE.md` doit refléter une compréhension qui **s'approfondit**, pas un résumé qui s'allonge.

## Related
- [[brantham/_MOC]]
- [[brantham/context/business-profile/_PROFILE]]
- [[brantham/context/voice-notes/README]]
- [[brantham/playbooks/call-introduction-repreneur]]
