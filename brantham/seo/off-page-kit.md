---
title: SEO — Kit d'exécution off-page (clé en main)
type: seo-playbook
project: brantham
date: 2026-05-12
status: à exécuter par Paul/Soren (comptes requis)
tags: [seo, branthampartners, backlinks, off-page, rp]
---

# Kit off-page clé en main — branthampartners.fr

Tout est rédigé. Ce qui reste = créer les comptes / cliquer "soumettre" / envoyer les mails (besoin des accès, je ne peux pas le faire à ta place). Cocher au fur et à mesure. NAP de référence à utiliser **partout, à l'identique** :

> **Brantham Partners** — SAS — SIREN 101 953 891 — 59 rue de Ponthieu, Bureau 326, 75008 Paris — 07 68 36 25 63 — paul.roulleau@branthampartners.fr — https://branthampartners.fr

Description courte (≤160 c.) : *Cabinet de conseil spécialisé dans le rachat d'entreprises en difficulté en France : sourcing, due diligence accélérée, exécution en audience.*

Description longue : *Brantham Partners accompagne repreneurs et investisseurs dans l'acquisition de sociétés en procédure collective — redressement judiciaire, liquidation judiciaire, sauvegarde, prépack cession — via des plans de cession validés par les tribunaux de commerce. Sourcing off-market, due diligence en 15 jours, structuration juridique, exécution à l'audience.*

---

## BLOC 1 — Citations / fiches (cette semaine — ~2 h, gratuit)

Liens faciles + cohérence NAP. À faire dans cet ordre :

- [ ] **Google Business Profile** — business.google.com → créer la fiche, catégorie principale *Conseiller en fusions et acquisitions* (ou *Cabinet de conseil*), adresse 59 rue de Ponthieu 75008, tél, site, horaires, description longue, 3-5 photos (logo, bureau, équipe). Valider par courrier/téléphone. → backlink + Maps + signal local fort.
- [ ] **Pappers.fr** — chercher SIREN 101 953 891 → la fiche existe déjà → "C'est mon entreprise / compléter" → ajouter le site web + logo + description.
- [ ] **Societe.com** — idem, revendiquer la fiche, ajouter site web.
- [ ] **Verif.com / Infonet / Manageo / Bilans-gratuits** — fiches auto-générées via SIREN, ajouter le site quand possible (souvent un simple lien suffit).
- [ ] **PagesJaunes.fr** — créer une fiche pro gratuite (catégorie conseil aux entreprises).
- [ ] **Crunchbase.com** — créer le profil entreprise (Add a company), lien site, courte description, fondateurs.
- [ ] **LinkedIn page entreprise** — vérifier qu'elle est complète à 100 % : logo bannière, site, description longue, secteur "Conseil et services aux entreprises", taille, siège Paris. (Le moteur de contenu LinkedIn tourne déjà côté infra → garder la cadence.)
- [ ] **Fusacq.com** — créer un profil "Conseil M&A / repreneur" (annuaire des intermédiaires de cession-reprise) → lien thématiquement très pertinent.
- [ ] **CessionPME.com** — profil conseil.
- [ ] **Bpifrance — Place de la reprise** (placedelareprise.bpifrance.fr) — profil accompagnateur si éligible.
- [ ] **Réseau Entreprendre / CRA (cra-asso.org)** — voir si une fiche partenaire/intervenant est possible.
- [ ] **Le Village de la Justice (village-justice.com)** — créer un profil rédacteur (Paul) → permet de publier des articles signés avec lien dofollow (cf. Bloc 3).
- [ ] **Doctrine.fr** — vérifier si les associés/le cabinet y ont une fiche pro ; sinon contacter Doctrine pour en créer une (ils référencent les pros du droit/restructuring).

**Mesure** : après ce bloc, GSC → "Liens" → tu devrais voir 8-15 domaines référents (vs <5 aujourd'hui).

---

## BLOC 2 — Contenu linkable (le moteur — récurrent)

### 2a. Baromètre des défaillances = release MENSUELLE
La page `barometre-defaillances.html` a déjà le schema `Dataset` — il faut juste la faire vivre.
- [ ] Chaque début de mois : mettre à jour avec les chiffres du mois écoulé (source : data pipeline `/Users/paul/Desktop/brantham-partners/`), `dateModified` + lastmod sitemap, ajouter 1-2 graphiques propres en PNG avec mention "Source : Brantham Partners — réutilisation libre avec lien".
- [ ] Générer un **mini-PDF "Baromètre [mois] 2026"** (1-2 pages, weasyprint depuis le template corporate) + un visuel carré pour LinkedIn.
- [ ] Pitcher (voir Bloc 3) à la liste journalistes. C'est CE type d'asset que la presse éco reprend → backlinks de presse.

### 2b. Modèles téléchargeables
Les concurrents rankent avec des "modèles gratuits". Mettre en téléchargement (PDF/DOCX, formulaire email facultatif) :
- [ ] Modèle d'offre de reprise en plan de cession (la page `modele-offre-reprise-plan-cession.html` existe → ajouter le doc téléchargeable réel).
- [ ] Modèle de business plan de reprise (`modele-business-plan-reprise.html`).
- [ ] Modèle de lettre d'intention (`modele-lettre-dintention-reprise.html`).
- [ ] Modèle de NDA (`nda-rachat-entreprise.html`).
→ pages "modèle gratuit" = aimants à liens (forums, blogs, écoles, LinkedIn).

### 2c. Études de cas anonymisées chiffrées
Déjà amorcé sur certaines pages. En faire 3-4 vraiment détaillées (timeline, valorisation, décote, leviers) → relayables par les sites M&A/repreneuriat.

---

## BLOC 3 — Newsjacking & RP (le plus rapide pour un domaine neuf — récurrent)

### 3a. Inscriptions
- [ ] **SourceOfSources** (sos.sourceofsources.com, ex-HARO) — s'inscrire comme source, mot-clés : "restructuring", "company acquisition", "bankruptcy", "distressed M&A", "reprise entreprise".
- [ ] Surveiller **#journorequest** sur LinkedIn/X + les groupes de journalistes éco.

### 3b. Liste de journalistes à constituer (20-30 contacts)
Cibles : Les Échos / Les Échos Entrepreneurs / Les Échos régions, La Tribune (+ éditions régionales), BFM Business, Challenges, Capital, Maddyness, L'Usine Nouvelle, + presse sectorielle (L'Officiel des Transporteurs, L'Antenne — transport ; Le Moniteur — BTP ; Néorestauration, L'Hôtellerie Restauration — CHR ; LSA — retail) + presse régionale (selon les défaillances locales). Tenir le fichier dans `vault/brantham/seo/journalistes.md`.

### 3c. Email de pitch baromètre (template)
> **Objet : [Région/Secteur] — les défaillances d'entreprises au [mois 2026], données exclusives**
>
> Bonjour [Prénom],
>
> Je vous transmets en exclusivité notre baromètre des défaillances pour [mois 2026] : [X] procédures collectives en France ([+/-Y %] sur un an), avec une concentration sur [secteur/région]. Le détail par secteur et par région : [lien].
>
> Quelques points qui peuvent intéresser vos lecteurs : [2-3 chiffres marquants + 1 phrase d'analyse].
>
> Je suis disponible pour un commentaire ou une interview — Brantham Partners accompagne au quotidien des repreneurs sur ces dossiers (reprise à la barre, plans de cession). Visuels libres de droit fournis avec mention de la source.
>
> Bien à vous,
> Paul Roulleau — Brantham Partners — 07 68 36 25 63 — branthampartners.fr

### 3d. Réponse type SourceOfSources / journorequest
> Bonjour, Paul Roulleau, fondateur de Brantham Partners (cabinet spécialisé dans le rachat d'entreprises en difficulté en France). Sur [sujet de la demande] : [réponse concise et factuelle, 3-5 phrases, 1 chiffre]. Je peux développer / fournir un cas concret anonymisé. Profil : branthampartners.fr/equipe.html. Dispo par tél : 07 68 36 25 63.

### 3e. Communiqué de presse — lancement du baromètre / positionnement cabinet
*(NB : ne PAS nommer de deal en cours dans un CP public — cf. règle vault. Quand un deal est closé et public, on peut faire un CP "deal" séparé, sans le nom de la cible si la confidentialité l'exige.)*

> **COMMUNIQUÉ DE PRESSE — Paris, le [date]**
>
> **Rachat d'entreprises en difficulté : Brantham Partners lance un baromètre mensuel des défaillances et accompagne les repreneurs sur les plans de cession**
>
> Avec [X] procédures collectives recensées en France au premier trimestre 2026 ([+Y %] sur un an), les opportunités de reprise d'entreprises en redressement ou liquidation judiciaire se multiplient — notamment dans le transport, le BTP et la restauration. Brantham Partners, cabinet de conseil basé à Paris, publie un baromètre mensuel des défaillances (par secteur et par région) et accompagne repreneurs et investisseurs dans l'acquisition de sociétés en procédure collective : sourcing off-market, due diligence accélérée en 15 jours, structuration de l'offre, exécution à l'audience du tribunal de commerce.
>
> « [Citation Paul : 2-3 phrases sur la tendance + la valeur d'un accompagnement structuré pour réussir une reprise à la barre]. »
>
> **À propos de Brantham Partners** — Cabinet de conseil spécialisé dans le rachat d'entreprises en difficulté en France (distressed M&A). Accompagnement de bout en bout des repreneurs : identification de cibles, due diligence, valorisation, structuration juridique, dépôt et défense de l'offre de reprise. Plus d'informations : branthampartners.fr
>
> **Contact presse** — Paul Roulleau — paul.roulleau@branthampartners.fr — 07 68 36 25 63

Diffusion : envoi direct aux journalistes de la liste + 1 fil de diffusion peu cher (Categorynet, 24presse, communiquedepresse.com) → quelques reprises = backlinks.

### 3f. Tribunes signées (lien d'autorité)
Proposer 1 tribune / 2 mois à : Le Village de la Justice, Maddyness, Les Échos "Idées", La Tribune "Opinions", L'Agefi. Sujets : "Pourquoi 2026 sera l'année des reprises à la barre", "Reprendre une entreprise en redressement : les 5 erreurs qui coulent une offre", "Plan de cession : ce que le repreneur doit comprendre du Code de commerce". Auteur identifié = Paul Roulleau, avec bio + lien.

Email de proposition (template) :
> **Objet : Proposition de tribune — « Pourquoi 2026 sera l'année des reprises à la barre »**
>
> Bonjour,
>
> Je suis Paul Roulleau, fondateur de Brantham Partners, cabinet spécialisé dans le rachat d'entreprises en difficulté en France. Au vu de la hausse des défaillances depuis début 2026 (transport, BTP, restauration en première ligne), je vous propose une tribune sur la reprise d'entreprises en procédure collective — sujet d'actualité, technique, mal compris des repreneurs.
>
> Angle : « Reprendre une entreprise en redressement judiciaire : les erreurs qui coulent une offre de reprise » (ou, selon votre ligne : « 2026, l'année des reprises à la barre : ce que dit le Code de commerce et ce que regardent les juges »). Format 4 000–6 000 signes, ton analytique et concret, exemples anonymisés. Je peux l'envoyer sous [délai].
>
> Seriez-vous intéressé(e) ?
>
> Paul Roulleau — Brantham Partners — 07 68 36 25 63 — paul.roulleau@branthampartners.fr — branthampartners.fr

---

## BLOC 4 — Partenariats & échanges naturels (récurrent)

- [ ] **Administrateurs & mandataires judiciaires** — relations avec les études (déjà dans le business : sourcing). Pages "partenaires" / mentions croisées quand naturel. Liste à tenir.
- [ ] **Avocats restructuring / droit des affaires** — co-publications, recommandations croisées.
- [ ] **Experts-comptables, CGP, banquiers d'affaires transmission** — réseau de prescripteurs → liens depuis leurs pages "ressources/partenaires".
- [ ] **Écoles & formations reprise** (CRA, CNAM, écoles de commerce) — intervenir + fournir ressources → liens.
- [ ] **Fédérations & associations** — OTRE, FNTR (transport), CAPEB/FFB (BTP), CCI, Réseau Entreprendre, CRA — adhésion / intervention / contribution → liens + visibilité.

---

## À NE PAS FAIRE
- Achat de liens en masse, PBN, annuaires spammy → pénalité quasi assurée sur un domaine neuf YMYL.
- Ancres exact-match répétées ("rachat entreprise en difficulté" en ancre 30×) → garder un ratio naturel (marque / URL nue / "ici"/"voir" / sémantique large).
- Échanges de liens industriels (link farms).
- Nommer publiquement un deal en cours.

## Mesure & cadence
- Tenir `vault/brantham/seo/journalistes.md` (contacts) + un log des liens obtenus.
- Suivre les **domaines référents** mensuellement (GSC "Liens" + Ahrefs Webmaster Tools gratuit).
- Cibles : 3 mois → ≥15 DR pertinents ; 6 mois → ≥30 dont ≥3 presse/autorité.
- Corréler avec la position moyenne France (baseline 13,3 — [[brantham/seo/_MOC]]).

## Related
- [[brantham/seo/_MOC]]
- [[brantham/seo/plan-link-building]]
- [[brantham/seo/reverse-engineering-pourquoi-pas-premier]]
- [[brantham-magic-form-levallois-first-deal]]
- [[brantham/_MOC]]
