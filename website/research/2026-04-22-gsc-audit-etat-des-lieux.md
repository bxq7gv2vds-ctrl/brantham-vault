---
type: research
project: website
date: 2026-04-22
tags: [seo, gsc, indexation, strategie, backlinks]
---

# GSC Audit — État des lieux ranking au 22/04/2026

## Contexte
Audit demandé par Paul : "je ne nous vois pas encore premier partout". Cross-check entre vault (score GEO 84/100) et réalité Google Search Console.

## Chiffres clés (fenêtre 15/03→20/04, 36 jours)
- Clics : **194**
- Impressions : **8 908**
- CTR moyen : **2,2 %** (sous-performant vs pos 10,9, cible 3-5%)
- Position moyenne : **10,9** (page 1/2)
- Pages indexées : **92**
- Pages non indexées : **61**
- Sitemap GSC : 125 URLs soumises | sitemap.xml local : 134 URLs | site physique : 146 pages HTML
- Compte GSC : `paul.roulleau@branthampartners.fr`

## Répartition indexation

| Raison | Pages | Diagnostic |
|---|---|---|
| Dans l'index | 92 | OK |
| **Détectée, non indexée** | **38** | **Crawl budget insuffisant — autorité faible** |
| Canonique correcte (duplicate) | 16 | Variantes www/non-www, normal |
| Exclue par noindex | 4 | Pages légales (mentions, cookies, confidentialité) — volontaire |
| Redirection | 2 | Normal |
| Explorée, non indexée | 1 | Jugement Google sur valeur |

### 38 pages "Détectées, non indexées" — liste
- insights.html
- 27 sectorielles : agroalim-redr, auto-liq/redr, btp-liq/redr, commerce-liq, conseil-liq/redr, edition-liq/redr, energie-liq/redr, immobilier-liq/redr, imprimerie-liq/redr ×2, industrie-manuf-liq/redr, interim-liq/redr, metallurgie-liq/redr, nettoyage-liq, sante-liq, securite-liq/redr, services-liq/redr
- sauvegarde-acceleree, sauvegarde-judiciaire
- sort-bail-commercial-liquidation, transfert-contrats-travail-plan-cession
- turn-around-management, tva-cession-fonds-de-commerce-liquidation
- rachat-entreprise-metz

**Cause racine** : templates quasi-identiques entre pages secteur → Google détecte thin/duplicate content, ne dépense pas de crawl budget sur un site à faible autorité.

## Top queries (clics > 0)
| Query | Clics | Impr | Pos |
|---|---|---|---|
| modèle offre de reprise liquidation judiciaire | 2 | 14 | 6,7 |
| depot de bilan transport routier 2026 | 2 | 11 | 6,8 |
| liquidation judiciaire transport routier 2026 | 1 | 44 | 6,1 |
| liquidation judiciaire dans le transport | 1 | 41 | 10,5 |
| annonces légales bodacc | 1 | 1 | **1,0** |

Pattern : **transport routier = niche dominée**, queries sectorielles bien positionnées.

## Top impressions à zéro clic (opportunités)
| Query | Impr | Pos | Note |
|---|---|---|---|
| cession entreprise rennes | 73 | 22,7 | Page géo faible |
| redressement judiciaire | 69 | 47,3 | Volume énorme, pos page 5 |
| plan redressement nice | 49 | 18,1 | Géo |
| liste entreprise en liquidation judiciaire gratuit bodacc | 44 | 11,9 | Quasi page 1 |
| liquidation judiciaire | 34 | 79,3 | Volume massif, pos page 8 |
| score3 liquidation | 31 | **7,7** | Quick win |
| reprise entreprise toulouse | 30 | 31,4 | Géo |
| redressement judiciaire transport routier | 28 | 9,9 | Quick win |

## Top pages performance
| Page | Clics | Impr | Pos | CTR |
|---|---|---|---|---|
| `/` (homepage) | 36 | 102 | 2,4 | **35,3 %** |
| droits-salaries-plan-cession | 17 | 433 | 6,1 | 3,9 % |
| rachat-transport-logistique-redressement | 16 | **761** | 9,6 | 2,1 % |
| cout-rachat-entreprise-liquidation | 16 | 418 | 6,4 | 3,8 % |
| modele-offre-reprise-plan-cession | 13 | 261 | 6,3 | 5 % |
| prepack-cession | 8 | 281 | 7,9 | 2,8 % |
| rachat-entreprise-difficulte (pillar) | 7 | 441 | 7,6 | 1,6 % |
| calendrier-procedure-collective | 7 | 138 | 6,3 | 5,1 % |
| barometre-defaillances | 6 | 318 | 5,4 | 1,9 % |

## Pages indexées bien classées mais 0 clic (meta/title à refaire)
| Page | Pos | Impr |
|---|---|---|
| modele-lettre-dintention-reprise | **4,2** | 86 |
| aides-reprise-entreprise-difficulte | 6,4 | 181 |
| garantie-actif-passif-entreprise-difficulte | 6,2 | 87 |
| rachat-tech-digital-redressement | 6,3 | 102 |
| rachat-transport-logistique-liquidation | 6,6 | 85 |
| plan-de-retournement-entreprise | 8,3 | 100 |
| checklist-due-diligence-distressed | 8,3 | 71 |
| rachat-entreprise-lille | 7,7 | 89 |
| glossaire-ma | 13,8 | 82 |

## Les 3 vrais blocages identifiés

1. **Crawl budget bloqué** (38 pages non indexées) — manque d'autorité + thin content sectoriel
2. **CTR sous-performant** (2,2 % vs 4-5 % attendu à pos 10) — titres/meta faibles
3. **Autorité quasi-nulle** — zéro backlink → impossibilité de ranker sur queries génériques à volume

## Stratégie ajustée — 90 jours

### P0 — Débloquer indexation (7 jours)
- Enrichir 27 pages sectorielles avec contenu unique (stats BODACC secteur, cas anonymisés, benchmarks EBITDA). 3000+ mots, plus de templates.
- Maillage interne depuis top page transport vers 10 autres sectorielles
- Request indexing manuel GSC, 10 pages/jour sur 4 jours

### P1 — Reprendre clics dormants (14 jours)
- Réécrire title + meta de 20 pages classées <10 sans clics
- Format : question + chiffre + bénéfice
- Objectif : CTR moyen → 4 %

### P2 — Construire autorité (60 jours)
Zéro raccourci :
- Wikipedia "Reprise d'entreprise en difficulté (France)"
- Guest post Village de la Justice
- LinkedIn Brantham + 3 posts/semaine (réutiliser writing-vault concepts)
- Crunchbase, Societe.com, Pages Jaunes, CRA, Fusacq, BPI Bourse Transmission
- Pitch presse (Les Echos, La Tribune, JDN) avec angle données BODACC exclusives
- **Cible : 10 backlinks DA>30**

### P3 — Consolidation contenu (30 jours)
42 sectorielles + 30 géo = trop de templates minces. Fusionner :
- Pages combinées RJ/LJ par secteur (20 au lieu de 42)
- Contenu unique par secteur (pas de copie)

## Quick wins ce soir
1. Request indexing des 38 pages (manuel GSC)
2. Rewrite title/meta des 10 pages "0 clic à pos<8"
3. Publier post LinkedIn avec lien barometre
4. Soumettre sitemap actualisé (134 URLs réelles)

## Verdict
L'écart vault (GEO 84/100) vs GSC (pos 10,9) s'explique par **un seul facteur** : manque d'autorité. Le site est techniquement prêt à >95 %. Les 3-4 prochains mois doivent être **backlinks + LinkedIn + PR**, pas du code.

## Related
- [[website/_MOC]]
- [[_system/MOC-master]]
- [[website/research/2026-03-18-indexation-ranking-audit]]
- [[website/sessions/2026-03-28-audit-seo-complet]]
- [[website/strategies/2026-03-18-fast-ranking-strategy]]
