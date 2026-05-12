---
title: SEO — Plan de consolidation des pages villes
type: seo-plan
project: brantham
date: 2026-05-12
status: à exécuter
tags: [seo, branthampartners, internal-architecture]
---

# Consolidation des 28 pages villes → 12 pages régionales

Décision (2026-05-12) : les 28 `rachat-entreprise-[ville].html` sont perçues comme du programmatique à faible valeur (bloquées pos 13-30, ~53% de vocabulaire identique entre deux villes). On consolide en **12 pages régionales fortes**, on 301 les 16 autres vers leur ancre régionale.

## Mapping (ancre conservée → villes redirigées vers elle)

| Région | Page ancre conservée | Pages 301 → vers l'ancre |
|---|---|---|
| Île-de-France | `rachat-entreprise-paris.html` | — |
| Auvergne-Rhône-Alpes | `rachat-entreprise-lyon.html` | saint-etienne, grenoble, clermont-ferrand |
| PACA | `rachat-entreprise-marseille.html` | nice, toulon |
| Occitanie | `rachat-entreprise-toulouse.html` | montpellier |
| Nouvelle-Aquitaine | `rachat-entreprise-bordeaux.html` | limoges |
| Hauts-de-France | `rachat-entreprise-lille.html` | amiens |
| Grand Est | `rachat-entreprise-strasbourg.html` | reims, metz |
| Pays de la Loire | `rachat-entreprise-nantes.html` | angers, saint-nazaire |
| Bretagne | `rachat-entreprise-rennes.html` | brest |
| Normandie | `rachat-entreprise-rouen.html` | le-havre, caen |
| Bourgogne-Franche-Comté | `rachat-entreprise-dijon.html` | — |
| Centre-Val de Loire | `rachat-entreprise-orleans.html` | tours |

→ 12 conservées, **16 redirigées** : saint-etienne, grenoble, clermont-ferrand, nice, toulon, montpellier, limoges, amiens, reims, metz, angers, saint-nazaire, brest, le-havre, caen, tours.

> Note : Nice et Montpellier ont du trafic réel ; on accepte la perte de ciblage exact-city au profit d'une page régionale plus autoritaire. L'ancre doit *mentionner ces villes partout* dans son corps (cf. étape 2).

## Étapes d'exécution (dans l'ordre — ne pas inverser)

1. **Réécrire les 12 ancres en pages régionales** : titre + H1 + meta orientés région ("Rachat d'entreprise en difficulté en Auvergne-Rhône-Alpes — Lyon, Saint-Étienne, Grenoble, Clermont-Ferrand"). Couvrir dans le corps : chaque ville de la région (tribunal de commerce local + adresse), stats régionales, secteurs dominants, AJ/MJ régionaux, fonds/aides régionaux, cas anonymisés. Recycler le contenu des pages qui vont être supprimées (fusionner le meilleur). Mettre à jour `dateModified` + lastmod sitemap + priorité 0.8.
2. **Vérifier** que chaque ancre mentionne bien explicitement les villes qui vont rediriger vers elle (sinon le 301 est traité comme soft-404 par Google).
3. **301** : ajouter dans `vercel.json` un `redirects` pour les 16 → leur ancre.
4. **Supprimer** les 16 fichiers `rachat-entreprise-<ville>.html`.
5. **Sitemap** : retirer les 16 entrées.
6. **Liens internes** : remplacer partout les liens vers les 16 supprimées par un lien vers l'ancre régionale (notamment la section "Présence nationale" de `rachat-entreprise-difficulte.html` et la section "par région" de `rachat-transport-logistique-redressement.html`). Re-scanner les orphelins après.
7. **GSC** : après déploiement, soumettre les 16 anciennes URLs à l'inspection (Google verra le 301), re-soumettre le sitemap.

## Vérifications de fin
- `python3` scan : 0 lien interne mort, 0 orphelin, sitemap sans entrée fantôme.
- `curl -I` sur 3-4 des 16 redirigées → 301 vers la bonne ancre.
- HTML des 12 ancres parse.

## Related
- [[brantham/seo/_MOC]]
- [[brantham/seo/reverse-engineering-pourquoi-pas-premier]]
- [[brantham/_MOC]]
