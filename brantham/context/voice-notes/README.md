---
type: readme
project: brantham
---

# Voice Notes — Brantham

## Comment Paul m'envoie un vocal

**Trois modes possibles :**

### Mode 1 — Fichier audio local
Paul dépose le fichier dans `~/Desktop/brantham-voice/` (ou n'importe quel chemin) et me dit :
> "voice note brantham : ~/Desktop/brantham-voice/2026-05-06-pricing.m4a"

Je transcris (mlx-whisper local) → traite.

### Mode 2 — Transcript collé directement
Paul colle le texte du vocal (depuis dictée iOS, WhatsApp, autre app) et me dit :
> "voice note brantham : [texte]"

Je traite direct, pas de transcription nécessaire.

### Mode 3 — Vocal court tapé
Paul tape directement ce qu'il veut me dire en mode décousu / oral. Je traite comme un vocal.

## Ce que je fais à chaque vocal

1. **Transcript brut** sauvegardé : `vault/brantham/context/voice-notes/YYYY-MM-DD-HHMM-slug.md`
2. **Insights extraits** : injectés dans `business-profile/_PROFILE.md` à la bonne section
3. **Capture auto** :
   - Décision détectée → `vault/founder/decisions/YYYY-MM-DD-titre.md`
   - Assumption → `vault/founder/assumptions/titre.md`
   - Customer / repreneur retour → `vault/founder/customers/YYYY-MM-DD-nom.md`
   - Pattern réutilisable → `vault/brantham/patterns/nom.md`
4. **Mise à jour index** : `business-profile/voice-notes-index.md`
5. **Annonce** ce que j'ai capturé en 2-3 lignes max

## Format transcript

```markdown
---
type: voice-note
project: brantham
date: YYYY-MM-DD
slug: topic-slug
duration: ~Xmin (estimé)
mode: audio|text-pasted|typed
---

# Voice note — [titre]

## Transcript
[texte brut, idéalement nettoyé des hesitations mais conservé fidèle]

## Insights extraits
- [insight 1] → updated `_PROFILE.md` section X
- [insight 2] → captured as `decisions/...`
- [insight 3] → ouverture question Y

## Related
- [[brantham/context/business-profile/_PROFILE]]
- [autres backlinks selon contenu]
```

## Sujets prioritaires pour Paul à raconter
1. Pourquoi Magic Form a signé sans data room (replicable ?)
2. Profil idéal repreneur grade A vs B vs C — vraies différences en call
3. Comment on traite un AJ pour qu'il devienne ami (pas client)
4. Vraies objections entendues en outreach (pas hypothèses)
5. Soren — statut activation, blocages, plan d'attaque
6. Vision 2026 fin d'année — combien de deals, quel revenu, quelle équipe
7. Relation pricing / qualification — quand passer un deal en 15k+15k vs 7k+7k
8. Concurrents directs — qui prend les deals qu'on rate
9. Erreurs / leçons des calls passés (pas seulement le raté d'aujourd'hui)
10. Politique data room — ce qu'on fait pour débloquer l'AJ
