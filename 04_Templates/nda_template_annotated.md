---
name: nda_template_annotated
type: template
version: 1.0
date: 2026-06-12
---

# NDA Template — Annoté avec Pièges Courants

**Usage:** Signer en 48h, pas 2 semaines. Version légale France-friendly.

---

## ACCORD DE CONFIDENTIALITÉ (NDA)

**Entre:** [SELLER COMPANY] ("Divulgatrice") et [ACQUIRER COMPANY] ("Destinataire")

**Date:** [DD/MM/YYYY]

---

### 1. DÉFINITION — CONFIDENTIAL INFORMATION

**Texte Standard:**
> « Toute information divulguée par la Divulgatrice au Destinataire, incluant (sans limitation) les données financières, les secrets commerciaux, les plans produits, les listes clients, les architectures techniques, et tout document marqué "CONFIDENTIEL" ou verbalement identifié comme confidentiel. »

🚨 **PIÈGE #1 — Champ Trop Large**
- **Mauvais:** "Toutes les discussions, idées, conseils, feedbacks"
- **Bon:** "Informations spécifiques identifiées comme confidentielles, documentées"
- **Pourquoi?** Si trop large, tout est secret (même la taille de l'équipe). Acquirer refuse de signer.

---

### 2. EXCLUSIONS — INFORMATION NON-CONFIDENTIELLE

**Texte Standard:**
> « N'est pas Confidentielle l'information qui : (a) est publiquement disponible sans violation de cet accord; (b) était connue du Destinataire avant divulgation, documentée par écrit; (c) est reçue légalement d'un tiers sans obligation de confidentialité; (d) est développée indépendamment par le Destinataire sans accès à l'Information Confidentielle; (e) est requise à être divulguée par la loi. »

🚨 **PIÈGE #2 — Exclusion "Required by Law" Mal Rédigée**
- **Mauvais:** "Si divulgation légalement requise, pas d'avis préalable"
- **Bon:** "Divulgation requise légalement = avis préalable raisonnable pour permettre injunction"
- **Pourquoi?** Acquirer veut vraiment parler à ses avocats avant de discuter en due diligence avec ses investisseurs.

✅ **BONNE VERSION:**
```
(e) Si divulgation légalement requise par autorité compétente ou 
    ordre de tribunal : le Destinataire avisera la Divulgatrice 
    dans le délai le plus court possible (sans révéler que notification 
    va être donnée) afin de permettre à la Divulgatrice de chercher 
    une ordonnance de protection.
```

---

### 3. OBLIGATIONS DU DESTINATAIRE

**Texte Standard:**
> « Le Destinataire s'engage à : (i) traiter l'Information Confidentielle avec le même soin qu'il traite ses propres informations confidentielles (au minimum "reasonable care"); (ii) limiter l'accès à ses employés, consultants, et avocats ayant besoin de le savoir; (iii) ne pas utiliser l'Information pour autre chose qu'évaluer une transaction potentielle. »

🚨 **PIÈGE #3 — "Reasonable Care" Trop Flou**
- **Mauvais:** "Reasonable care" (interprétation variable selon juge)
- **Bon:** "Industrie-standard measures, au minimum X sécurité"
- **Pourquoi?** Breached = tu dois prouver Destinataire était négligent. Difficile.

✅ **BONNE VERSION:**
```
(ii) Protéger par mesures d'industrie-standard incluant :
  - Accès limité à "need-to-know" (max 10 personnes côté Destinataire)
  - Stockage sécurisé (encrypted at rest, VDR avec access logs)
  - NDA signé par tous les accesseurs
  - Pas de screenshot, vidéo, ou copie locale de data room
```

---

### 4. TERM & TERMINATION

**Texte Standard:**
> « Cet accord durera [X] ans à partir de sa date d'signature, sauf si terminé plus tôt si transaction n'avance pas. Obligations de confidentialité survivront [Y] ans après termination. »

🚨 **PIÈGE #4 — Durée de Confidentialité Trop Courte**
- **Mauvais:** "Confidentialité dure 2 ans après close" (acquirer apprend secrets après)
- **Bon:** "Confidentialité dure [3-5 ans] post-close; secrets commerciaux = in perpetuity"
- **Pourquoi?** Si acquirer viole 2 ans post-close, tu as peu de recours.

✅ **BONNE VERSION:**
```
Obligations de confidentialité :
  - Documents financiers : 3 ans post-close
  - Architecture technique / secrets : 5 ans post-close
  - Trade secrets (formulas, customer lists) : in perpetuity
  - Droit applicable : loi française (French IP law protects 
    trade secrets indefinitely si meilleur intérêt de divulgatrice)
```

---

### 5. RETURN / DESTRUCTION OF CONFIDENTIAL INFORMATION

**Texte Standard:**
> « À demande de la Divulgatrice, le Destinataire retournera ou détruira (certifié par écrit) toute Information Confidentielle dans [30] jours. »

🚨 **PIÈGE #5 — Destruction Sans Vérification**
- **Mauvais:** "Destinataire certifie seul qu'il a détruit, no audit"
- **Bon:** "Destruction certifiée + droit d'audit raisonnable si breach soupçonné"
- **Pourquoi?** Copy could still exist on backup/laptop. Audit protège divulgatrice.

✅ **BONNE VERSION:**
```
Retour/Destruction :
  - Toute information retournée ou détruite dans 30 jours
  - Destruction certifiée par écrit (signed destruction certificate)
  - Exceptions pour : (a) archivage légal (1 copy, VDR); 
    (b) legal hold (court order); (c) copies créées par système 
    de backup automatique (destroyed upon normal backup cycle)
  - Droit d'audit : si breach soupçonné, Divulgatrice peut 
    auditer Destinataire (raisonnable, <30j notice)
```

---

### 6. NO LICENSE / NO OBLIGATION

**Texte Standard:**
> « Rien dans cet accord ne confère de licence à l'Information ou ne crée d'obligation de la Divulgatrice de poursuivre une transaction. »

✅ **Standard — Rarement un Problème**
- Protect toi : NDA ≠ intent to sell
- Protect buyer : Access to data ≠ obligation to buy

**Mais ajoute:**
```
Clarification : 
  - La Divulgatrice peut discuter cette opportunité 
    avec d'autres acquéreurs potentiels
  - Aucune exclusivité n'est conférée par cet accord
  - Ni party n'a obligation de poursuivre transaction 
    ou de révéler raison de non-poursuite
```

---

### 7. NO REPRESENTATIONS / "AS IS"

**Texte Standard:**
> « L'Information est fournie "AS IS" sans représentations ou garanties. La Divulgatrice ne garantit pas l'exactitude ou la complétude. »

🚨 **PIÈGE #6 — Déni de Responsabilité Trop Large (Te Protège à Excess)**
- **Mauvais:** "Toute info fournie sans garantie aucune; pas notre faute si inexacte"
- **Bon:** "Fournie en bonne foi; si false/misleading = breach possible mais pas garantie formelle"
- **Pourquoi?** Acquirer demandera reps & warranties dans SPA anyway. Trop d'immunity ici = red flag.

✅ **BONNE VERSION:**
```
Représentations limitées :
  - Information fournie de bonne foi, basée sur records actuels
  - Pas de garantie explicite de complétude/exactitude (données 
    exploratoires à valider en DD)
  - Divulgatrice engage que : (a) a le droit de divulguer; 
    (b) divulgation ne viole pas droit de tiers; (c) n'a pas 
    connaissance de discrepancies matérielles

Note : Reps complètes = dans Purchase Agreement (SPA), pas ici
```

---

### 8. REMEDIES

**Texte Standard:**
> « Chaque party reconnaît que breach causerait dommage irréparable. Donc, injonction est disponible en plus de dommages-intérêts. »

✅ **Standard — Gardé Généralement Pareil**
- Mais clarifiez : injunction est via tribunal français (compétent pour IP/confidentialité)

---

### 9. GOVERNING LAW & JURISDICTION

**Texte Standard:**
> « Cet accord est régi par la loi de [FRANCE / STATE]. »

✅ **FORT RECOMMANDÉ — LOI FRANÇAISE**

**Pourquoi?**
- French IP law (Code de la Propriété Intellectuelle) protège secrets commerciaux "in perpetuity" si "raison valable de maintenir le secret"
- French courts prennent confidentialité sérieusement
- Droit français = meilleure protection que US common law (qui demande à prouver "competitive advantage" pour protéger indéfiniment)

✅ **BONNE VERSION:**
```
9. DROIT APPLICABLE
Cet accord est régi par la loi de la République Française.

Juridiction exclusive :
  - Tribunal de commerce compétent selon siège de Défendeur
  - Ou, si injonction urgente : référé (emergency injunction via 
    judge) auprès du tribunal de Grande Instance compétent

Arbitrage OPTIONNEL (si préféré) :
  - Alternative : arbitrage ICC (International Chamber of Commerce), 
    1 arbitre, règles ICC, siège arbitrage = Paris, droit français

Note : Injunction souhaitable plutôt qu'arbitrage (= plus rapide 
si breach flagrant, ex: info divulguée à concurrent)
```

---

### 10. MUTUAL VS. ONE-WAY NDA

**Situation 1: Seller → Buyer (One-Way, Typical)**
```
Seller confie données. Buyer sign NDA avant accès data room.
Buyer ne divulgue rien de soi → pas d'obligation mutuelle.

Template ci-dessus = ONE-WAY, correct.
```

**Situation 2: Exploratory Mutual (Rare, Both Share)**
```
Buyer aussi partage (sa stratégie d'intégration, son tech stack).
= MUTUAL NDA = symétrique (même obligations des deux côtés).

Template modifié :
- Changer "Divulgatrice / Destinataire" → "Party A / Party B"
- Obligations = mêmes deux sens
```

---

## SPEED CHECKLIST — Comment Signer en 48h

1. **D0 (Vendredi matin):** Envoie NDA annoté au buyer (pas ta draft, plutôt version neutre)
2. **D0 (Lundi matin):** Follow-up — "As discussed, attached NDA. Can we sign by Wed?"
3. **D1 (Lundi):** Buyer lawyer répond avec 3-5 asks → toi tu réponds "Accepted" ou "Counter"
4. **D1 (Lundi soir):** Signature électronique (DocuSign / Yousign France)

**Red Flags à Rejeter d'Emblée (cost you 2 weeks sinon):**
- "5-year mutual NDA" (trop lourd si one-way)
- "Liquidated damages $1M per breach" (court = better remedy)
- "Non-solicitation of employees 2 years post-close" (belongs in employment agreements, not NDA)

---

## TEMPLATE TEXT — Ready to Use

```markdown
---
CONFIDENTIALITY AGREEMENT

THIS CONFIDENTIALITY AGREEMENT (the "Agreement"), executed as of [DATE]
(the "Effective Date"), between [SELLER], a [SASU/SARL/SAS] located at 
[ADDRESS] ("Disclosing Party" or "Seller"), and [BUYER], a [CORPORATION] 
located at [ADDRESS] ("Receiving Party" or "Buyer").

WHEREAS, the Parties contemplate a potential transaction involving the 
business of Seller, and in connection therewith, Seller may disclose 
certain confidential information to Buyer.

NOW, THEREFORE, in consideration of mutual covenants:

1. CONFIDENTIAL INFORMATION

"Confidential Information" means information disclosed by Seller to Buyer, 
in any form, that Seller identifies as confidential or that reasonably 
should be understood to be confidential, including but not limited to:

(a) Financial information (revenue, expenses, cash flow, cap table)
(b) Customer information (names, contracts, pricing, feedback)
(c) Technical information (architecture, code, infrastructure)
(d) Business plans, roadmaps, and strategic initiatives
(e) Pricing information and cost data

Confidential Information does NOT include information that:
(i) Is or becomes publicly available through no breach of this Agreement
(ii) Was rightfully known to Buyer prior to disclosure, documented in writing
(iii) Is lawfully received by Buyer from a third party without 
     confidentiality obligations
(iv) Is independently developed by Buyer without access to Confidential Information
(v) Is required to be disclosed by law (with prior notice to Seller per Section 3)

2. OBLIGATIONS OF BUYER

Buyer shall:
(a) Use Confidential Information solely to evaluate a potential transaction
(b) Limit disclosure to employees, consultants, and attorneys on a 
    need-to-know basis, each bound by written confidentiality obligations
(c) Protect Confidential Information using industry-standard security 
    measures, at minimum encryption at rest, access controls, and audit logs
(d) Not reproduce, retain, or transmit Confidential Information beyond 
    as necessary for evaluation
(e) Upon request, return or certify destruction of all Confidential 
    Information within 30 days

3. REQUIRED DISCLOSURE BY LAW

If Buyer is required by law, court order, or regulatory authority to 
disclose Confidential Information, Buyer shall:
(a) Promptly notify Seller in writing (unless prohibited by law)
(b) Cooperate with Seller's efforts to obtain protective order
(c) Disclose only the minimum information legally required

4. TERM AND SURVIVAL

This Agreement shall continue for [X years] from the Effective Date, 
unless earlier terminated by written notice. Buyer's obligations regarding 
Confidential Information shall survive termination for:
(a) Financial and business information: 3 years post-termination
(b) Technical information and trade secrets: 5 years post-termination
(c) Trade secrets (customer lists, formulas): indefinitely under French law

5. NO LICENSE OR OBLIGATION

(a) No license, rights, or obligation to proceed with transaction is granted
(b) Seller may discuss opportunity with other potential acquirers
(c) Either party may terminate discussions without liability

6. REMEDIES

The Parties acknowledge that breach would cause irreparable harm. 
Accordingly, Seller shall be entitled to seek injunctive relief and specific 
performance, in addition to all other remedies available at law or in equity.

7. GOVERNING LAW

This Agreement is governed by and construed in accordance with the laws of 
France, without regard to conflicts of law. The parties irrevocably submit 
to the jurisdiction of the competent courts of France.

8. ENTIRE AGREEMENT

This Agreement constitutes the entire agreement between the parties regarding 
confidentiality and supersedes all prior and contemporaneous agreements.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the 
Effective Date.

[SELLER NAME]
By: ____________________
Name: __________________
Title: __________________
Date: __________________

[BUYER NAME]
By: ____________________
Name: __________________
Title: __________________
Date: __________________
```

---

## POST-SIGNATURE CHECKLIST

- [ ] NDA uploaded to data room (or referenced in access email)
- [ ] Signed copy stored in deal folder `/vault/01_Deals/[BUYER-NAME]/nda-signed.pdf`
- [ ] Buyer added to data room with access log
- [ ] Seller legal team notified (backup copy)
- [ ] LOI kick-off call scheduled for D+3 to D+5

