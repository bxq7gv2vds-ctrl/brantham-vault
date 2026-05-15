---
type: session
project: brantham
date: 2026-05-15
tags: [cockpit-web, opportunites, scraping, aj, ux, data-quality]
---

# Session 2026-05-15 — Cockpit opportunites, coverage AJ et detail fiche

## Contexte

Paul veut recentrer le cockpit sur le besoin operationnel critique : **voir toutes les opportunites du marche, en cours, avec un maximum d'informations fiables et verifiables**.

La priorite n'est plus la gestion des mandats, de la finance, ni le sourcing repreneurs dans l'interface principale. Le cockpit doit d'abord devenir une page simple, lisible, qui donne envie de travailler, permettant :

- de voir toutes les opportunites actives ;
- de cliquer une opportunite pour consulter son detail ;
- de surligner les opportunites interessantes ;
- de relancer le scraping ;
- de voir toutes les AJ repertoriees avec leurs liens ;
- de verifier si une source AJ ou Mayday manque ;
- de consulter les donnees scrapees de facon structuree.

Phrase directrice utilisateur : "le plus important c'est d'avoir tous les deals du marche sur notre cockpit avec le max d'info possible".

## Infrastructure comprise pendant la session

Le cockpit Brantham a trois couches :

1. **Cockpit TUI** dans `/Users/paul/brantham-pipeline/cockpit/`
   - Textual/Python.
   - Fonctionnel pour triage, mais plafond UX atteint.
   - Continue d'exister pour operations rapides terminal.

2. **Cockpit Web** dans `/Users/paul/cockpit-web/`
   - Next.js 15/16 + Supabase Postgres.
   - Cible principale pour Paul + Soren.
   - Doit devenir une interface simple et fiable pour les opportunites.

3. **Pipeline scraping/enrichissement** dans `/Users/paul/brantham-pipeline/`
   - Scrapers AJ, Mayday, enrichissement detail opportunites, hunters.
   - Alimente la DB Supabase commune.

Ancien dashboard React `/Users/paul/internal-tool/` et vieux pipeline multi-agents OpenClaw compris comme ancienne generation, non prioritaire pour ce chantier.

## Decisions produit prises

- Le premier ecran doit etre une **page opportunites active-only**, pas un cockpit large avec finance/mandats/repreneurs.
- Les opportunites archivees, poubelle et expirees ne doivent pas polluer la vue principale.
- La recherche repreneur n'est pas prioritaire dans cette page.
- La qualite du scraping et la couverture marche passent avant les features commerciales.
- Les AJ doivent etre visibles, nommees, avec liens directs de verification.
- Mayday doit etre traite comme source/relai important meme si ses annonces sont normalisees vers les AJ reelles.
- Le detail d'opportunite doit etre sobre, dense, verifiable, pas un rendu "full IA".

## Travail realise dans le cockpit web

Fichier principal : `/Users/paul/cockpit-web/components/SimpleOpportunitiesPage.tsx`.

La page racine `/Users/paul/cockpit-web/app/page.tsx` rend maintenant une interface simple `SimpleOpportunitiesPage`.

### Vue opportunites

La page charge :

- `/api/opps?status=all&life=actives&limit=5000`
- `/api/aj-sources`

La liste filtre les statuts `archive` et `poubelle`, puis trie par deadline croissante.

Affichage principal :

- header "Opportunites en cours" ;
- metriques : en cours, surlignees, J-7 ;
- carte "Scraping AJ" avec bouton `Relancer tout le scraping` ;
- liste dense des opportunites ;
- panneau detail sticky a droite ;
- panneau "Sources AJ suivies" en bas.

### Surlignage

Le bouton `Surligner` bascule `user_status` entre :

- `shortlist`
- `nouveau`

via `POST /api/opps/[id]` avec `action: "set_status"`.

Les opportunites surlignees ont un fond jaune pale et un bord gauche visible.

### Sources AJ

Fichiers :

- `/Users/paul/cockpit-web/app/api/aj-sources/route.ts`
- `/Users/paul/cockpit-web/lib/ajSources.ts`

Ameliorations integrees :

- affichage des sources AJ repertoriees ;
- liens directs vers les AJ ;
- statut source : ok, failed, empty, relay ;
- Mayday pris en compte comme relai ;
- `AJ Associes` et `STAR Administrateurs Judiciaires` ajoutes comme `mayday_relay` ;
- ajout automatique des sources detectees dans les opportunites actives mais absentes du registre statique.

Point Mayday clarifie : le dernier run pouvait indiquer `Maydaymag = empty`, mais un test direct a montre que Mayday contenait des opportunites actives. Elles etaient normalisees sous les AJ reelles, par exemple AJ UP, Meynet, AJ Associes, 2M&Associes, Maitre Sophie TCHERNIAVSKY, Maitre Laurent MIQUEL.

## Detail opportunite

Dernier chantier realise : amelioration du panneau detail d'une opportunite.

Le panneau detail affiche maintenant :

- badge AJ source ;
- bouton `Surligner` ;
- nom de l'entreprise ;
- resume verifiable ;
- section `Donnees cles` ;
- section `Contact & AJ` ;
- section `Liens de verification` ;
- bouton `Copier resume` ;
- section `Donnees extraites du scrape` ;
- texte source complet repliable.

### Donnees structurees affichees

Le detail tente d'extraire et d'afficher :

- deadline offre ;
- procedure ;
- localisation ;
- secteur / activite ;
- chiffre d'affaires ;
- effectif ;
- SIREN / SIRET ;
- prix / loyer / fonds ;
- AJ source ;
- mandataire / AJ ;
- tribunal ;
- audience / jugement ;
- contact ;
- emails ;
- telephones ;
- adresse ;
- dossier / reference.

Les champs absents sont affiches explicitement comme `Non trouve`, pour rendre les trous de donnees visibles.

### Parsing local ajoute

Fonctions ajoutees/ameliorees dans `SimpleOpportunitiesPage.tsx` :

- `parseExtractedInfo`
- `uniqueMatches`
- `hasValue`
- `renderValue`
- `flattenValues`
- `buildOpportunitySummary`
- `cleanResidual`

Le parsing reste conservateur : il structure ce que le scraper a deja mis dans `notes_scraper`, sans inventer de donnees.

## Verification technique

Build cockpit web :

```bash
cd /Users/paul/cockpit-web
npm run build
```

Resultat : OK.

Serveur local relance :

```bash
cd /Users/paul/cockpit-web
npm run dev -- -H 127.0.0.1 -p 3000
```

URL :

```text
http://127.0.0.1:3000
```

Au moment de la session, le serveur Next repondait et les routes suivantes avaient retourne 200 :

- `/`
- `/api/aj-sources`
- `/api/opps?status=all&life=actives&limit=5000`

## Limites restantes

Le chantier n'est pas termine. Points critiques encore ouverts :

- La couverture marche n'est pas encore prouvee a 100%.
- Il faut auditer source par source les AJ suivies vs les AJ du marche.
- Il faut verifier que Mayday est scrape de facon fiable, pas seulement indirectement via normalisation AJ.
- Le detail depend encore beaucoup de `notes_scraper`, donc la qualite amont du scraping detail page reste decisive.
- Les champs structured DB comme SIREN, NAF, dirigeant, contact, CA fiable, effectif fiable ne sont pas encore toujours remplis.
- Repreneurs/hunters restent hors priorite immediate dans cette page.
- L'UX globale est amelioree mais doit encore etre testee par Paul en usage reel.

## Prochaine roadmap immediate

Priorite 1 : **coverage marche observable**

- Lister toutes les sources AJ ciblees.
- Pour chaque source : URL, scraper actif, dernier statut, nb trouve, erreur, dernier run.
- Ajouter un indicateur "source non couverte / source couverte / source en erreur / relai Mayday".
- Comparer manuellement les sources majeures avec le cockpit.

Priorite 2 : **scraping detail opportunite**

- Ouvrir la page source de chaque opportunite active.
- Extraire proprement les champs metier dans une structure stable.
- Ne pas se contenter d'un blob texte.
- Stocker les champs utiles en DB plutot que seulement dans `notes_scraper`.

Priorite 3 : **fiche opportunite complete**

- Ajouter confiance par champ : `scrape`, `deduit`, `manquant`.
- Afficher source exacte de chaque donnee quand possible.
- Ajouter bouton "ouvrir source AJ" et "ouvrir dataroom" toujours visibles.
- Ajouter une alerte si une opportunite manque de deadline, source, procedure, localisation ou detail.

Priorite 4 : **qualite operationnelle**

- Ajouter tests/API smoke pour `/api/opps`, `/api/aj-sources`, `/api/scrape`.
- Ajouter monitoring scrape quotidien.
- Faire remonter les 8 sites AJ historiquement casses.
- Creer un rapport quotidien simple : nouvelles opps, sources cassees, sources vides, Mayday detecte.

## Fichiers touches pendant la conversation

Dans `/Users/paul/cockpit-web/` :

- `components/SimpleOpportunitiesPage.tsx`
- `app/page.tsx`
- `app/api/aj-sources/route.ts`
- `lib/ajSources.ts`

Autres fichiers deja modifies avant cette sauvegarde dans le repo selon `git status` :

- `app/globals.css`
- `app/layout.tsx`
- `package-lock.json`
- `package.json`
- `proxy.ts`
- dossier `app/api/`
- dossier `components/`
- dossier `lib/`
- `STATE.md`

Ne pas revert ces changements sans verification, car ils correspondent au chantier en cours ou a des modifications preexistantes.

## Intentions utilisateur a garder en tete

- "On ne peut pas se permettre de ne pas voir les differentes opportunites."
- "Deja contente toi de bien scraper les informations."
- "Je veux juste une page avec toutes les opportunites super simple a comprendre."
- "Je dois voir que celles en cours et je dois pouvoir cliquer dessus pour y voir plus de detail."
- "Je veux des boutons pour relancer tout le scraping."
- "Je veux aussi voir visiblement toutes les AJ repertoriees, avoir les liens de toutes les AJ."
- "Je veux le nom de l'AJ."
- "Il faut que je puisse surligner des opportunites."
- "Dans les informations extraites les datas doivent etre bien structurees."
- "Je ne suis pas sur que tu couvres toutes les opportunites."
- "Maydaymag il doit y avoir des opportunites normalement."

## Related

- [[brantham/_MOC]]
- [[brantham/architecture]]
- [[brantham/cockpit/roadmap-2026-05-05]]
- [[brantham/sessions/2026-05-05-audit-cockpit-roadmap]]
- [[brantham/sessions/2026-05-12-cockpit-coverage-monitoring]]
- [[brantham/sessions/2026-05-12-scraping-detail-pages]]
- [[brantham/sessions/2026-05-12-cockpit-web-hunt-ux]]
- [[brantham/patterns/mayday-mag-detail-parsing]]
- [[brantham/patterns/cockpit-tui-triage]]
- [[_system/MOC-master]]
