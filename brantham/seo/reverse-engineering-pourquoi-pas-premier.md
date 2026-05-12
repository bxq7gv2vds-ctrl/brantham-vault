---
title: SEO — Reverse engineering : pourquoi branthampartners.fr n'est pas premier
type: seo-analysis
project: brantham
date: 2026-05-12
tags: [seo, branthampartners, strategy, reverse-engineering]
---

# Pourquoi on n'est pas premier partout — et le plan pour y arriver

Analyse honnête. Le site est **techniquement très bien fait** (canonical, hreflang, robots meta, JSON-LD riche : Organization/ProfessionalService/FAQPage/HowTo/BreadcrumbList/LegalService, FAQ sitewide, contenu profond sur les pages piliers, mobile, HTTPS, sitemap propre). Le problème n'est presque pas on-page. Il est ailleurs.

## Reverse engineering — qui est premier et pourquoi

Sur les requêtes cibles ("rachat entreprise en difficulté", "modèle offre de reprise plan de cession", "liquidation judiciaire transport routier 2026"…), le top 5 est occupé par trois familles :

1. **Cabinets d'avocats & legaltech établis** : legalstart.fr, legalplace, swim.legal, legalrescue.fr, facchini-avocat.com, berton-associes.fr, novlaw.fr, lla-avocats.fr. Domaines de 5-15 ans, des centaines à des milliers de domaines référents, des milliers de pages.
2. **Institutionnel / officiel** : bpifrance-creation.fr, greffe-tae-paris.fr, **cnajmj.fr** (l'organe officiel des AJ/MJ), service-public.fr. Autorité maximale aux yeux de Google sur ce sujet juridique (YMYL — Your Money Your Life, Google exige du "trust" élevé).
3. **Annuaires & marketplaces** : doctrine.fr, actify.fr, repreneurs.com, dotmarket.eu, procedurecollective.fr. Énormes volumes de pages + maillage + listings réels d'entreprises.
4. **Presse** (sur les requêtes type "…2026") : trans.info, france3-regions, SGTCF, OTRE.

### Les 6 vraies raisons

1. **Le domaine a 2 mois.** branthampartners.fr a été enregistré ~mars 2026. Google applique une rampe de confiance ("sandbox" de fait) aux nouveaux domaines, surtout sur des sujets YMYL/juridiques. Un domaine de 2 mois ne peut pas battre legalstart (10 ans) ni cnajmj (officiel) sur des head terms commerciaux, peu importe la qualité on-page. **C'est ~70-80% de l'explication.** Délai réaliste pour percer le top 5 sur les gros termes : 6-18 mois de signaux d'autorité.

2. **Profil de backlinks ≈ zéro, zéro citation de marque.** Une recherche "branthampartners.fr" ne renvoie rien — Google ne connaît pas cette entité. Doctrine/legalstart ont des milliers de domaines référents. C'est le levier n°1 manquant, et il ne se code pas : il se construit (RP, partenariats AJ/MJ, articles invités, annuaires, contenu linkable).

3. **Mismatch d'intention SERP sur certains termes.** "liquidation judiciaire transport routier 2026" → Google veut de la **presse** (trans.info) ou un **annuaire** (Doctrine, Actify listant de vraies sociétés). Une page de conseil/service ne satisfait pas pleinement cette intention. → Soit on construit une vraie brique data/listing (le baromètre est un début), soit on vise les variantes à intention "conseil" ("comment racheter un transporteur en redressement", "racheter une société de transport en liquidation").

4. **Pages "villes" programmatiques perçues comme à faible valeur.** 28 pages `rachat-entreprise-[ville].html` construites sur le même gabarit avec le nom de ville permuté → le système "Helpful Content" de Google les escompte → bloquées pos 13-30. La page Amiens fait ~4 800 mots dont une grosse part de boilerplate ; Nice ~8 700 ; recouvrement de vocabulaire ~53% identique entre deux villes. → Soit on les rend **génuinement profondes et uniques** (vrai tribunal de commerce local + adresse + stats locales + cas réels + AJ/MJ locaux par leur nom), soit on **consolide** en ~10 pages régionales fortes.

5. **Aucun signal de fraîcheur.** Pas de blog daté avec publication régulière. Tout est figé au 28 mars 2026. Les sites actifs publient ; Google le voit.

6. **E-E-A-T mince.** Entité toute neuve, aucune validation externe, pas d'auteur reconnu dans le secteur. La page équipe existe (Paul, Soren, LinkedIn) mais ça ne pèse que si c'est relayé ailleurs (interviews, citations, articles signés sur d'autres sites, profils Doctrine/LinkedIn fournis).

## Ce qui est déjà bon — ne pas y toucher
Canonical absolus + hreflang + robots meta ; JSON-LD complet et propre ; FAQ schema sur 134 pages ; profondeur de contenu sur les piliers (souvent 15-25 min de lecture, ce qui est au niveau ou au-dessus des concurrents) ; mobile OK ; sitemap propre ; cache headers ; CSP. La 1ère vague de pages se positionne déjà sur **445 requêtes** — la fondation est saine. Le boulot maintenant : autorité + fraîcheur + maillage + capture de la longue traîne.

## Plan d'action

### Tier 1 — On-page : maximisation (codable, en cours)
- ✅ De-orphaning des 21 pages (fait, batch #1).
- ✅ www→non-www (fait, batch #1).
- ✅ Fraîcheur + bloc "mai 2026" sur la page transport-redressement, lastmod/priorité bumpés (batch #2).
- **Maillage contextuel** (pas juste le footer hub) : sur chaque pilier, 5-10 liens internes dans le corps vers les pages connexes du même silo. Construire 4-5 silos clairs (procédures / financement / juridique post-cession / sectoriel / villes).
- **AEO / AI Overviews** : en tête de chaque page money, un bloc "réponse directe" de 40-60 mots (définition + chiffre clé), structuré pour être cité par Google AI Overviews, Perplexity, ChatGPT (robots.txt les autorise déjà). Pour un domaine neuf, **être cité dans une AI Overview = visibilité même en position 8**. C'est le levier court terme le plus sous-exploité.
- **Pass titles/meta CTR** sur les pages pos 5-15 (notamment `financement-rachat-entreprise-difficulte.html` : pos 7,6 / CTR 0,39%).
- **Page phare** sur le head term ("Racheter une entreprise en liquidation judiciaire : le guide 2026") avec une profondeur imbattable + **modèle téléchargeable** (les concurrents proposent des "modèles gratuits" — l'intention est transactionnelle, fournir le doc).
- Sitemap : routine de `lastmod` réel à chaque modif (script).

### Tier 2 — Contenu & fraîcheur (à valider / scaffolder)
- **Blog `/insights/` daté, 2-4 posts/mois, en newsjacking.** Pour un domaine neuf c'est la voie la plus rapide vers des liens + du trafic : surfer l'actu (vague faillites transport 2026, Ziegler/Pedretti/Sogran, défaillances sectorielles, jurisprudence plans de cession). Chaque post = entité fraîche, longue traîne, et matière à relais LinkedIn.
- **Baromètre des défaillances = release mensuelle.** En faire un asset linkable récurrent (data + graphes), pitché aux journalistes éco. Un seul bon graphe repris = backlinks de presse.
- **Pages villes** : décision à prendre — consolider en ~10 régionales fortes, ou investir pour rendre chacune génuinement unique (tribunal, AJ/MJ locaux nommés, stats locales, cas anonymisés locaux).
- **Pages sectorielles** : le transport est le breakout — décliner la recette (BTP, agroalimentaire, restauration, tech) avec données sectorielles fraîches "2026".

### Tier 3 — Off-page : autorité (NON codable — c'est LE goulot)
- **Campagne de liens** : annuaires juridiques/M&A, partenariats AJ/MJ (échanges de liens naturels), articles invités sur sites M&A/restructuring, profils sur Doctrine / repreneurs.com / plateformes de reprise, communiqués de presse à partir des deals réels (le deal Magic Form = une histoire).
- **LinkedIn content engine** (déjà en place côté infra) → génère de la recherche de marque "brantham" → signal de confiance pour Google.
- **Google Business Profile** sur le 59 rue de Ponthieu 75008 si bureau physique (renforce le local).
- **Relations presse** : éco régionale (Les Échos régions, La Tribune, presse locale) sur les défaillances locales — Brantham comme expert cité.

## Mesure
KPI nord : position moyenne France (baseline 13,3 au 12/05). Sous-KPI : nb de requêtes en top 5, nb de pages indexées, nb de domaines référents (à suivre via un outil — Ahrefs/Semrush gratuit limité, ou GSC "Liens"). Point tous les 3 jours sur les exports GSC ([[brantham/seo/_MOC]]).

**Vérité à garder en tête** : on peut gagner 2-4 positions partout en 1-3 mois avec le maillage + la fraîcheur + l'AEO. Pour être *premier* sur les head terms, il faut 6-18 mois d'autorité (liens, marque, relais). Sur la longue traîne et les requêtes "2026"/sectorielles/locales peu concurrentielles, on peut viser le top 3 beaucoup plus vite — c'est là qu'on met l'énergie.

## Related
- [[brantham/seo/_MOC]]
- [[brantham/seo/reports/2026-05-12-point-01]]
- [[brantham/seo/reports/2026-05-12-actions-batch-01]]
- [[brantham/_MOC]]
- [[website/seo-strategy]]
