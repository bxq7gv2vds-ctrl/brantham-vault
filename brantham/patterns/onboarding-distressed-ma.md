---
type: pattern
project: brantham
created: 2026-04-24
tags: [pattern, onboarding, distressed, ma, lettre-mission, nda, data-room]
---

# Pattern — Onboarding distressed M&A (flow J+0 → dépôt offre)

## Origine du pattern

Pattern construit lors de l'onboarding du **premier deal Brantham Partners signé** (Magic Form Levallois, Arnaud GUILLEM, 2026-04-24). Inspiré du modèle SAPAUDIA Partners (LDM BAW/TNP Consultants 08/09/2025).

## Use case

Quand un repreneur donne son accord verbal pour qu'on l'accompagne sur un dossier de reprise d'entreprise en procédure collective (RJ/LJ/pré-pack cession), appliquer ce flow standardisé pour sécuriser le mandat, débloquer la data room, et démarrer la rédaction de l'offre avec un momentum maîtrisé par Brantham (pas par le repreneur).

## Timeline de référence

```
J+0 (call)                    Confirmation verbale repreneur
   ↓
J+1 matin                     Envoi PACK J+1 (email unique, 5 docs)
   ↓
J+1 soir                      Signature LDM + NDA + virement upfront #1
   ↓
J+2                           Courrier LRAR à l'AJ (extension NDA) + NDA Brantham
   ↓
J+3 à J+5                     Accès data room officialisé
   ↓
J+5 max                       Call de point deal (90 min, présentiel de préférence)
   ↓
S1 → S3                       Due diligence → modélisation → rédaction offre
   ↓
J-2 deadline AJ               Réunion de synthèse avec repreneur
   ↓
J-0 deadline AJ               Dépôt offre au greffe
```

## Pack J+1 — 5 documents à envoyer dans un seul email

1. **Lettre de mission Brantham** (DocuSign) — template : [[brantham/templates/lettre-de-mission]]
   - Structure 10 sections inspirée SAPAUDIA
   - NDA intégré comme clause de confidentialité mutuelle (durée 5 ans)
   - Devis intégré (section 8) — 7k/7k pour CA <1M€ (voir [[founder/decisions/2026-04-24-pricing-7k-7k-petits-tickets]])
   - Annexe RIB complète

2. **Note de cadrage du deal** (PDF lecture) — template : [[brantham/templates/note-cadrage-deal]]
   - 12 sections : résumé exécutif, procédure, cible, économique, thèse de reprise, risques, stratégie offre, couverture L.642-2, rétroplanning, gouvernance, fees, next steps 72h
   - **Basée 100 % sur sources publiques** (BODACC, Pappers, annonce AJ, presse, LinkedIn)
   - Mentions `[À CONFIRMER DR]` pour tout ce qui nécessite data room

3. **Courrier repreneur → AJ** (PDF à signer manuscritement) — template : [[brantham/templates/courrier-extension-nda-aj]]
   - Officialise le mandat Brantham
   - Sollicite l'extension du NDA initial (signé par repreneur) à l'équipe Brantham nommément désignée
   - Annexe un NDA Brantham pré-signé à contresigner par l'AJ
   - **LRAR obligatoire**

4. **Checklist KYC + questionnaire critères stratégiques** — liste des pièces à transmettre + questionnaire structuration acquisition / offre / deal-breakers

5. **RIB Brantham + proforma upfront #1** — pour virement

## Point juridique critique — flow data room

**Erreur fatale à éviter** : demander au repreneur de forwarder directement la data room à Brantham.

**Raison** : si le repreneur a déjà accédé à la DR, il a signé un **engagement de confidentialité individuel (intuitu personae)** avec l'AJ. Ce NDA interdit toute transmission à des tiers sans autorisation écrite de l'AJ.

**Conséquences de l'erreur** :
- Pour le repreneur : violation NDA AJ → exclusion du process de cession
- Pour Brantham : complicité de divulgation → réputation cassée auprès de l'AJ
- Pour l'offre : risque de nullité si le tribunal apprend que la DR a circulé hors cadre

**Flow correct** :
1. Courrier LRAR repreneur → AJ officialisant le mandat Brantham + sollicitant extension du NDA
2. Brantham signe son propre NDA (ou avenant) auprès de l'AJ
3. AJ donne accès officiel à Brantham (via plateforme dédiée ou autorisation écrite de transmission par le repreneur)
4. **Seulement à partir de là**, le repreneur peut forwarder la DR en toute légalité

## Posture au call — cadres à respecter

### Mindset
1. **Brantham dicte le tempo** — la deadline AJ ne se négocie pas, donc le planning autour non plus
2. **Jamais d'excuse, jamais de "si vous voulez"** — on énonce, on ne demande pas
3. **Chaque ask repreneur a une deadline ferme + une conséquence** (pas de deadline molle)

### Phrases d'autorité
- "Voici comment on procède" (jamais "je propose que")
- "La deadline c'est le [date], donc on n'a pas le choix sur le planning"
- "Ce qu'il me faut de votre côté, c'est..."
- "On bloque [date synthèse] maintenant dans nos deux agendas"

### 2 moments de closing obligatoires
1. **En fin de call** : récapituler les 3 engagements ("demain matin pack, demain soir signé, mercredi on se voit") — le repreneur doit confirmer à voix haute
2. **Avant de raccrocher** : envoi invitation calendrier pendant le call

## Entretien ancien dirigeant — cadre L.642-3

**Objectif** : comprendre l'historique, les causes réelles de la défaillance, les relations commerciales clés, les savoir-faire non formalisés.

**Cadre juridique strict** :
- L.642-3 interdit au dirigeant (de droit ou de fait) et ses parents au 2ᵉ degré (conjoint, enfants, parents, grands-parents, frères/sœurs) de reprendre — directement ou indirectement
- Interdiction étendue : 5 ans post-cession
- Sanction : nullité de l'acte — 3 ans de prescription

**Best practices** :
- Entretien purement informationnel (pas de promesse de réembauche famille, pas de contrat consulting déguisé)
- **Jamais seul** : toujours à 2 (Paul + Soren ou avec le repreneur)
- **Mail récap systématique** au repreneur uniquement (pas à l'AJ)
- **Mention spontanée à l'AJ** qu'un entretien informel a eu lieu — transparence

## Gouvernance mission

### Double revue obligatoire
Chaque livrable (memo DD, offre, BP) passe par : Analyst (Paul) → Director (Soren) → Repreneur. Aucun document ne sort sans double validation interne Brantham.

### Canaux
- **WhatsApp dédié** "Brantham × [Code deal]" — ouvert dès J+1 — réponse < 2h en horaires ouvrés
- **Point hebdo 30 min** — jour/heure fixes
- **Récap email vendredi** — archive formelle
- **Dashboard Notion** partagé — suivi temps réel

## Signaux "pro" à glisser pendant le call (différenciation vs amateur)

- Citer les articles (L.642-2, L.642-3, L.642-5, R.642-1) spontanément
- Nommer l'AJ et le MJ (Pappers/annonce)
- Mentionner les interdictions L.642-3 (parents au 2ᵉ degré, contrôleurs, 5 ans)
- Expliquer pourquoi le mieux-disant prix ne gagne pas toujours (motivation spéciale tribunal)
- Présenter un teaser anonymisé déjà produit si disponible
- **Règle d'or énoncée** : *"On ne vous fait pas déposer une offre qu'on ne déposerait pas nous-mêmes"*

## Templates associés

- [[brantham/templates/lettre-de-mission]]
- [[brantham/templates/note-cadrage-deal]]
- [[brantham/templates/courrier-extension-nda-aj]]

## Exemples d'application

- [[brantham/deals/active/magic-form-levallois/_MOC]] — premier deal Brantham, modèle pilote

## Related

- [[brantham/context/process-end-to-end]]
- [[brantham/context/realite-business]]
- [[brantham/knowledge/process/structuration-offres-reprise]]
- [[brantham/knowledge/process/audience-tribunal]]
- [[brantham/knowledge/procedures/redressement-judiciaire]]
- [[founder/decisions/2026-04-24-pricing-7k-7k-petits-tickets]]
- [[brantham/_MOC]]
