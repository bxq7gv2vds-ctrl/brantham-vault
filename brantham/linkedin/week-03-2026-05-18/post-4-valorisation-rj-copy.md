---
type: linkedin-post
project: brantham
date: 2026-05-18
status: ready-to-publish
registre: autorité technique / question intrigante
visuel: post-4-meme-anakin.png (alt : post-4-two-buttons.png)
sources:
  - vault/brantham/knowledge/legal/plans-de-cession
  - vault/brantham/knowledge/process/due-diligence-distressed
---

# Post 4 — Pourquoi l'offre la plus chère se fait recaler au tribunal

> Vulgarise une contre-intuition forte : en RJ le prix n'est pas un montant, c'est un signal envoyé au juge.
> Hook = question qui pique. Contenu dense, posture d'autorité.
> Chute = système de pricing Brantham basé sur la data agrégée de milliers de dossiers déposés.

## Copy LinkedIn

```
Pourquoi l'offre la plus chère se fait recaler au tribunal plus souvent qu'elle ne gagne ?

C'est le truc que les repreneurs refusent de croire.

Voici ce que personne ne leur explique sur la valorisation d'une entreprise en redressement judiciaire.

Une entreprise en redressement, on ne l'achète pas. On dépose une offre de reprise d'actifs devant un juge. Le passif reste au passé.

Donc le prix ne se négocie avec personne. Il se justifie.

Et un juge ne lit pas un prix comme un vendeur. Il lit un signal.

Une offre trop basse dit : « je sous-estime ce dossier. »
Une offre trop haute dit : « je vais m'asphyxier dans six mois et licencier tout le monde. »

Les deux se font rejeter.

Le bon prix en RJ n'est jamais le plus élevé.

C'est celui qui est calibré : assez sérieux pour rassurer le tribunal sur la reprise, assez prudent pour que l'entreprise tienne le jour 1.

Ça ne se devine pas. Ça se calcule.

Chez Brantham, on a construit un système de pricing qui s'appuie sur la data agrégée de nos analyses de l'ensemble des dossiers déposés. En croisant des milliers de cas réels, structures de prix, profils d'actifs et décisions rendues.

Résultat : on positionne une offre qui ressort comme la plus crédible aux yeux du tribunal de commerce. Pas la plus chère. La plus défendable.

Si vous préparez une reprise et que vous voulez sécuriser la valorisation de votre offre jusqu'au dépôt, on peut en parler.

—
Brantham Partners — M&A distressed
```

## Hook (1ère ligne, à AB-tester)

- H1 (retenu) : « Pourquoi l'offre la plus chère se fait recaler au tribunal plus souvent qu'elle ne gagne ? »
- H2 : « Pourquoi l'offre la plus chère se fait éliminer au tribunal de commerce ? »
- H3 : « Combien vaut une entreprise qui ne vaut presque plus rien ? C'est la question que tranche un tribunal. »

## Visuel — meme Anakin / Padmé (retenu)

Format meme Star Wars 4 cases « for the better, right ? ... right ? » (le silence d'Anakin).
Template visuel déjà éprouvé en semaine 02. Effet : on rit, puis on réalise le malaise.

- TL (Anakin) : « J'ai déposé l'offre la plus chère sur le dossier »
- TR (Padmé, souriante) : « Donc le tribunal va te choisir, non ? »
- BL (Anakin, silence) : « … »
- BR (Padmé, inquiète) : « Le tribunal va te choisir, non ? »

Template : `templates/post-4-meme-anakin-lp.html` (base `anakin.png`)
Rendu : `post-4-meme-anakin.png` + `-navy.png` (1080×1080, via `render.py`).

## Visuel — alt « two buttons »

Repli si on veut une version DA Brantham sans image externe.
Template : `templates/post-4-two-buttons-lp.html` → `post-4-two-buttons.png` + `-navy.png`.

## Pourquoi ce post

- Hook = question contre-intuitive : ouvre une boucle de curiosité que le lecteur veut refermer.
- Preuve d'expertise par la spécificité (signal au juge, asphyxie jour 1), pas par les adjectifs.
- Une seule grande idée portable : « un prix est un signal, pas un montant ».
- Chute crédibilisée par la data agrégée → positionne le système de pricing Brantham comme un actif.
- Meme = accroche visuelle légère qui contraste avec le sérieux du sujet, screenshot-able.

## Vérifs avant publi

- [ ] Produire le visuel meme (Drake) et vérifier la DA.
- [ ] Confirmer la formulation « milliers de dossiers » cohérente avec le volume réel analysé.

## Related

- [[brantham/linkedin/INDEX]]
- [[brantham/_MOC]]
- [[brantham/knowledge/legal/plans-de-cession]]
- [[brantham/knowledge/process/due-diligence-distressed]]
- [[brantham/linkedin/week-03-2026-05-18/post-2-pre-pack-cession-copy]]
