# Audit SEO technique - branthampartners.fr
**Date** : 2026-03-18
**Probleme** : Le site n'apparait pas dans Google pour "rachat d'entreprise en difficulte" sans ajouter "brantham"
**Projet** : website

## Diagnostic principal : DOMAINE AGE DE 7 JOURS

**created: 2026-03-11T19:04:29** (WHOIS AFNIC)

Le domaine branthampartners.fr a ete enregistre le 11 mars 2026. Il a 7 jours.
Google n'a pas encore indexe le site. `site:branthampartners.fr` renvoie ZERO resultats.

C'est le probleme n.1 : pas d'indexation = pas de ranking possible.

## Verification d'indexation

| Test | Resultat |
|------|----------|
| `site:branthampartners.fr` | 0 resultats |
| `"branthampartners.fr"` (exact match) | 0 resultats |
| `brantham partners rachat` | 0 resultats (site absent) |
| robots.txt | OK - pas de blocage (`index, follow`) |
| meta robots | `index, follow, max-image-preview:large` - OK |
| sitemap.xml | Present, 17 URLs, content-type OK |
| canonical tags | Presents et corrects |
| HTTP status | 200 sur toutes les pages |

## Analyse on-page de /rachat-entreprise-difficulte.html

### Points positifs
- Title tag : "Rachat d'Entreprise en Difficulte : Guide 2026 | Brantham Partners" (59 chars, bon)
- Meta description : presente et pertinente (156 chars)
- H1 : "Rachat d'entreprise en difficulte en France : le guide complet"
- Hierarchie Hn : propre (1 H1, 9 H2, multiples H3)
- Contenu : ~4500 mots, couverture exhaustive
- Schema markup : Article + FAQPage (8 Q&A) + BreadcrumbList
- Canonical : correct
- Lang : fr
- Liens internes : 20+ liens vers pages du site
- Liens externes : sources autoritaires (Legifrance, INSEE, Bodacc, Banque de France)
- Mobile responsive
- HTTPS + HSTS

### Points a corriger (on-page)
- Alt text manquant sur les images
- Pas de hreflang (mineur, site monolingue)
- Inconsistance URL : sitemap a `.html` mais certains liens internes omettent l'extension (ex: `/barometre-defaillances` vs `/barometre-defaillances.html`)

## Architecture du site

17 pages dans le sitemap :
- 1 homepage
- 4 pages services (sourcing, DD, execution, valorisation)
- 7 guides (rachat, liquidation, plan-de-cession, reprise-a-la-barre, prepack, multiples-ebitda, cout-rachat)
- 2 pages data (barometre, article)
- 1 page glossaire
- 1 page insights (hub)
- 1 page redressement-judiciaire

Maillage interne : correct mais shallow (17 pages, toutes accessibles depuis nav/footer).

## Analyse concurrentielle SERP "rachat entreprise en difficulte"

Top 10 :
1. bpifrance-creation.fr (DA extreme, institution publique)
2. business-builder.cci.fr (CCI, institution)
3. sion-avocat.fr (cabinet avocat, autorite)
4. bpifrance-creation.fr (2e page)
5. transentreprise.com (marketplace)
6. lesclesdelabanque.com (Banque)
7. pacte-transmission-reprise.grandest.fr (institution regionale)
8. credipro.com (courtier financement)
9. cci.fr (CCI nationale)
10. baillet-dulieu-avocats.com (cabinet)

Constat : SERP dominee par des institutions (Bpifrance, CCI, Banque de France) et des cabinets d'avocats etablis avec forte autorite de domaine. Aucun site commercial jeune ne figure dans le top 10.

## Causes du non-ranking (par ordre d'impact)

### 1. DOMAINE NEUF - ZERO AUTORITE (CAUSE PRINCIPALE)
- 7 jours d'age
- 0 backlinks connus
- 0 pages indexees
- Google sandbox probable : les nouveaux domaines sont typiquement sandbox 2-8 semaines
- Meme avec un contenu parfait, Google ne rank pas un domaine de 7 jours face a Bpifrance

### 2. PAS ENCORE INDEXE
- Le crawl de Google prend du temps pour les nouveaux domaines
- Sitemap soumise via robots.txt mais pas confirmee via GSC
- Actions requises : soumettre sitemap dans Google Search Console, demander indexation URL par URL

### 3. ZERO BACKLINKS
- Pas de signal off-page
- Les concurrents top 10 ont des milliers de backlinks (Bpifrance, CCI)
- LinkedIn company page non trouvee pour Brantham Partners

### 4. SERP ULTRA-COMPETITIVE
- "rachat entreprise en difficulte" = SERP institutionnelle
- Keyword Difficulty probablement 60-80+
- Les pages qui rankent ont des DA de 70-90+

### 5. PROBLEMES TECHNIQUES MINEURS
- Inconsistance URLs (.html vs sans extension)
- Alt text images manquant
- Pas de page /blog ou /articles avec pagination pour le crawl budget

## Plan d'action recommande

### Immediat (cette semaine)
1. **Soumettre le site dans Google Search Console** et verifier l'indexation
2. **Soumettre le sitemap** dans GSC
3. **Demander l'indexation** des pages cles une par une via GSC
4. **Corriger les inconsistances d'URL** (.html partout)
5. **Ajouter les alt text** sur toutes les images

### Court terme (1-4 semaines)
6. **Creer une page LinkedIn Brantham Partners** et lier vers le site
7. **Soumettre le site aux annuaires M&A francais** (backlinks)
8. **Creer un profil Google Business** si applicable
9. **Publier sur des plateformes externes** (LinkedIn articles, Medium) avec lien retour

### Moyen terme (1-3 mois)
10. **Cibler des long-tail keywords** moins competitifs d'abord :
    - "prepack cession exemple"
    - "multiple ebitda entreprise difficulte"
    - "cout rachat entreprise liquidation judiciaire"
    - "due diligence acceleree procedure collective"
11. **Construire des backlinks** via guest posts, interviews, PR
12. **Ajouter du contenu frais** regulierement (blog/insights)
13. **Viser des featured snippets** via les FAQ schema deja en place

### Long terme (3-6 mois)
14. Monitorer les rankings et ajuster
15. Construire l'autorite de domaine progressivement
16. "rachat entreprise difficulte" sera accessible quand DA > 30-40

## Conclusion

Le site est techniquement bien construit. Le contenu est excellent (exhaustif, structure, schema markup). Le probleme est 100% lie a l'age du domaine (7 jours) et l'absence totale d'autorite. Google n'a meme pas encore indexe le site.

Priorite absolue : Google Search Console + backlinks + patience.
