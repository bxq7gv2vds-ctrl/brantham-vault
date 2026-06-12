---
name: red_flags_vendeur
description: Red flags pour vendeur — comportements acheteur à surveiller, négociation piégée
metadata:
  type: reference
  format: warning_checklist
  version: 1.0
---

# Red Flags Vendeur — Signes d'alerte avant de signer

*Symétrique à "red flags acheteur" — cette fois, signes que L'ACHETEUR est dangereux ou pas sérieux.*

---

## **PRE-LOI : Drapeau rouge = risque acheteur pas légitime**

### 🚩 Processus & timing suspects

| Red Flag | Risque | Quoi faire |
|----------|--------|-----------|
| "Nous devons signer LOI en 48h sinon pas intéressés" | Pressure pour limiter due diligence | Walk ou exiger 10 jours |
| Pas de M&A experience (CEO fait 1ère acquisition) | Lenteur, erreurs légales, process chaotique | Demander avocat/broker assistant |
| "Nous ne faisons pas de DD avant LOI" | Red flag classique, tentent cacher manque de sérieux | Refuser, c'est non-standard |
| Refuse data room, demande "résumé Excel" | Contrôle illégitime, ou n'a pas $ | Decline, offrir data room |
| "Vous devez payer les frais d'avocat de notre camp" | Cost-shifting, bad faith | Non, chacun ses frais |

### 🚩 Signaux financiers douteux

| Red Flag | Risque | Quoi faire |
|----------|--------|-----------|
| "Valorisation dépend de due diligence" | Bait-and-switch post-LOI | Valorisation doit être fixe, ajustements seulement NWC |
| Pas de pre-approval de financement | Peut pas lever, faux processus | Exiger proof of funds (banquier letter) |
| "Nous finançons par crédit vendeur" (seller note >50%) | Caché endettement, risque acheteur default | Max 20-30% seller note |
| Earnout sans conditions claires | Acheteur peut arbitrairement réduire payout | Mettre dans LOI : metrique = ARR/retention/churn |
| Cible earnings déraisonnables ("€1M EBITDA" vs your €200k) | Setup pour fail earnout = payout réduit | Réaliste ou walk |

### 🚩 Comportement & signal culturel

| Red Flag | Risque | Quoi faire |
|----------|--------|-----------|
| CEO ne prend jamais vos calls, sous-délègue | Pas sérieux, ou sous-financé | Call leur boss, ou walk |
| Multiples exigences legales "standard" (impossible) | Lawyers agressifs = dur closing | Demander structure deal basique |
| Refuse d'identifier key person clés | Plan secret : licencier quelqu'un | Protéger rétention contractuellement |
| "Vos clients vont devoir renégocier contrats" | Switching risk, ou cost-justification fausse | Non, changement-contrôle ne doit pas forcer reneg |

---

## **POST-LOI : Drapeau rouge = problèmes avant closing**

### 🚩 Due diligence abusive

| Red Flag | Risque | Quoi faire |
|----------|--------|-----------|
| "Nous avons besoin de accès complet Git" | Peuvent voler code ou secrets | Donner read-only, à travers escrow |
| Demande accès "tous les emails" de la boîte | Fishing pour leverage, contenu privé | Limiter à contrats/finance/product |
| Remet document NDA post-accès data room | Veulent déniabilité après breach | Refuser |
| Retard majeur post-data room = stalling | Baissent leur prix en attente | Set deadline : "DD done par D30 ou walk" |
| Engage seconde opinion audit sans prévenir | Setup pour découvrir problème = baisser prix | Demander rapport avant réaction |

### 🚩 Négociation après LOI

| Red Flag | Risque | Quoi faire |
|----------|--------|-----------|
| "Nous voulons réduire prix de 20% après seeing books" | Pas d'accord sur base factuelle — lie | Refuser, invoquer LOI comme binding |
| Demande extended earnout (de 18m à 36m) | Étire payout, réduire trésorerie | Refuser, max 24 mois |
| "Founders doivent rester 3 ans" dans rôle subordonné | Indentured servitude, pas acquisition | Négocier : 12m + option de partir |
| Augmente indemnisation holdback de 10% → 25% | Dérive contractuelle | Resend LOI as limit |
| Ajoute conditions post-LOI (employee sign-offs, customer approvals) | Tuer deal via condition impossible | Demander legal guidance, invoquer MACA clause |

### 🚩 Customer/employee issues

| Red Flag | Risque | Quoi faire |
|----------|--------|-----------|
| "3 clients disent oui à transition seulement si..." | Changement-contrôle clauses mal readées | Audit clients avant LOI, pas après |
| CTO/key engineer "suddenly resigns" pendant DD | Buyer sabotage ou real retention risk | Protéger rétention dans deal, bonus post-close |
| Buyer demande licencier sales team post-close | Intègrent à leurs sales, perds people | Mettre retention bonus pool (holdback funded) |

---

## **CLOSING DAY RED FLAGS**

### 🚩 Dernière minute surprises

| Red Flag | Risque | Quoi faire |
|----------|--------|-----------|
| "Financement not quite ready, peut-on repousser closing?" | Pas de fonds, deal meurt | Refuser, exiger proof of funds 48h avant |
| "Avvocato says we need une clause supplémentaire" | Tirer dernière concession | Invoquer "deal is done" avec LOI/SPA |
| "NWC adjustment came in 30% negative" | Vous perdez cash à closing | Demander réconciliation avant signing |
| "Wire transfer tomorrow matin pas ce soir" | Timing risk, peut changer avis | Exiger wire avant signature (trustee) |

---

## **EARNOUT RED FLAGS — Avant de structurer**

### 🚩 Structure earnout piégée

```
❌ "Earnout si ARR > €[HIGH TARGET]"
   → Buyer peut réduire voluntairement = pas payout

✓ "Earnout si churn < [X]%, mesure indépendante"
   → Buyer can't easily manipulate

❌ "Earnout si customer satisfaction NPS > 50"
   → Buyer peut biaiser survey

✓ "Earnout si ≥85% retention de clients closing, audit Deloitte"
   → Objective, third-party verified
```

### 🚩 Earnout payout logistics piégées

| Red Flag | Risque | Quoi faire |
|----------|--------|-----------|
| Earnout payable "from EBITDA" pas cash | Si EBITDA low, pas payout | Exiger cash basis |
| Earnout payable à buyer's option "up to €X" | Discrétionnaire = 0 | Mettre minimum si conditions atteintes |
| Earnout "waived if founder leaves" | Te force à rester, ou perte | Inclure "if buyer causes departure" |

---

## **COMPORTEMENT BUYER = SIGNAL DEAL RISK**

### Bons signaux (acheteur SÉRIEUX)

✓ Répond emails dans 24h
✓ Transparent sur process & timeline
✓ Pre-approval financing AVANT LOI
✓ Avocat expérimenté, conseille deal structuring honnêtement
✓ Due diligence ciblée, pas fishing
✓ Respecte calendrier deadlines
✓ Explique stratégie acquisition clairement
✓ Parle rétention & culture

### Mauvais signaux (acheteur RISQUÉ)

✗ Lent, incohérent, pas de réponse
✗ Cache source financement
✗ Avocat agressif, demands déraisonnables
✗ Fishing massif ("send all emails")
✗ Repousse dates continuellement
✗ Vague sur stratégie, role post-close
✗ Essaie de baisser prix post-LOI
✗ Ne parle jamais culture/retention

---

## **WALK-AWAY TRIGGERS (Quand abandonner)**

**Arrête-toi si l'acheteur :**

1. Reneges sur prix/structure post-LOI sans cause objective
2. Refuse de clarifier earnout / payout conditions
3. Décourage employee retention (plan to "optimize")
4. Demande financement vendeur >30% EV
5. Change process fondamentalement (extended DD, new conditions)
6. Pas de financement confirmé 30j avant close
7. Demande royalties/non-compete déraisonnables
8. Essaie d'isoler toi du team durant DD
9. Refuse de reconnaître clients' change-of-control clauses
10. Comportement bad faith (lies, withholding, pressure)

---

## **CHECKLIST : "Should I sign with this buyer?"**

```
□ Financement: Pre-approval (banquier letter) en place?
□ Process: Timeline clair, <90 jours closing?
□ Team: Plan clair pour rétention key people?
□ Structure: Prix fixed (NWC-adjusted only), pas "depends on DD"?
□ Earnout: Conditions claires, objective, measurable?
□ Comportement: Responsive, honnête, respecte accord?
□ Équipe légale: Expérimentée M&A, pas agressif?
□ Culture: Alignment avec vision toi + respects team?
□ Stratégie: Articulent pourquoi ils t'achètent?
□ Terms: Nothing shocking dans LOI vs what's spoken?

Score: [__]/10
Minimum acceptable: 7/10
Si <7/10 → walk ou renegotiate avant LOI
```

---

## **Si tu repères red flag**

1. **Arrête tout** — ne donne pas plus data
2. **Documente** — sauvegarde emails, notes
3. **Appelle avocat** — interprete le drapeau légalement
4. **Donne ultimatum** — "Clarify ou we're walking"
5. **Walk** — mieux que mauvais deal

*Vendre n'est pas un besoin — c'est une option. Mauvais buyer = nightmare 3-5 ans.*
## Related
## Related
