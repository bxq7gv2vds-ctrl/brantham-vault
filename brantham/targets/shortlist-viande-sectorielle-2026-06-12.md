---
type: shortlist
project: brantham
date: 2026-06-12
target: Gesler Abattoirs
sector: viande-bovine-aura
---

# Shortlist Repreneurs Sectorielle - Filère Viande Ain/AURA

Cible: ETS Gesler (abattoir bovin Ain) | DLDO: 06/07/2026 | Priorité: A

## Méthodologie de sélection

Critères:
- **Fit géographique**: < 200km Ain/Rhône-Alpes/Bourgogne
- **Capacité financière**: CA > 10M€ ou fonds propres > 5M€  
- **Adéquation métier**: Abattage/découpe bovine intégrée
- **Culture reprise**: Historique de deals distressed
- **Disponibilité**: Acteurs actifs sur acquisition récente

## Tier 1 - Repreneurs Stratégiques (Contact Immédiat)

| Repreneur | Fit | Points Forts | Risques | Angle d'approche | Statut Contact |
|-----------|-----|--------------|---------|-----------------|----------------|
| **T'Rhea / Viandes de Bresse** | ★★★★★ | Intégration verticale, ancrage territorial, marque forte | Prix élevé potentiel | "Consolider leadership AURA" | À contacter |
| **Bovi-Coop** | ★★★★★ | Coopérative locale, 2200 adhérents, logique territoriale | Processus coopératif long | "Sécuriser outil pour éleveurs" | À contacter |
| **Société Bellegardienne d'Abattage** | ★★★★☆ | Voisin direct, logique de mutualisation | Taille limitée | "Densification bassin Ain" | À contacter |
| **Tradival / Sicarev** | ★★★★☆ | Groupe coopératif fort, présence régionale | Centralisation Roanne | "Extension territoire Ain/Jura" | À contacter |
| **Puigrenier** | ★★★★☆ | Spécialiste bovin, qualité reconnue | Éloignement géographique | "Extension est France" | À qualifier |

## Tier 2 - Repreneurs Industriels (Qualification Prioritaire)

| Repreneur | Fit | Points Forts | Risques | Angle d'approche | Statut Contact |
|-----------|-----|--------------|---------|-----------------|----------------|
| **Centre Viandes Beauvallet** | ★★★★☆ | Présence Amberieu (Ain), groupe LJC | Focus plutôt découpe | "Renforcer sourcing local" | À qualifier |
| **Agrial / Sibert La Bresse** | ★★★☆☆ | Présence Ain, filière complète | Moins abattage pur | "Complément charcuterie" | À qualifier |
| **Terrena / Elivia** | ★★★☆☆ | Grand acteur national, capacité financière | Moins local | "Point d'ancrage AURA" | À qualifier |
| **SVA Jean Roze / Agromousquetaires** | ★★★☆☆ | Intégration retail, forte capacité | Éloignement Intermarché | "Accès sourcing local" | À qualifier |
| **Cooperl Arc Atlantique** | ★★☆☆☆ | Industriel complet, distressed expert | Focus porc, fit bovin faible | "Option multi-espèces" | Watchlist |

## Tier 3 - Distributeurs & Retailers (Approche Asset Focused)

| Repreneur | Fit | Points Forts | Risques | Angle d'approche | Statut Contact |
|-----------|-----|--------------|---------|-----------------|----------------|
| **Boucheries André** | ★★★☆☆ | Réseau lyonnais 45M€, circuit court | Pas repreneur naturel | "Actifs commerciaux & sourcing" | Approche contrats |
| **Grand Frais / Prosol** | ★★★☆☆ | Ecosystem premium, distribution | Pas industriel | "Accès filière premium" | Partenariat possible |
| **Despi Le Boucher** | ★★☆☆☆ | National, premium positioning | Coûteux | "Contrat d'approvisionnement" | Asset only |
| **Maison Lascours** | ★★☆☆☆ | Marque forte, premium | Éloigné, petit | "Marque & savoir-faire" | Marque uniquement |

## Tier 4 - Options Locales / Spécialisées

| Repreneur | Fit | Points Forts | Risques | Angle d'approche | Statut Contact |
|-----------|-----|--------------|---------|-----------------|----------------|
| **Kamakle (Foissiat)** | ★★☆☆☆ | Local, DGAL découpe | Taille incertaine | "Partenariat local" | À qualifier |
| **Label Découpe (Saint-Didier)** | ★★☆☆☆ | Proche, spécialisé | Capacité inconnue | "Reprise partielle" | À qualifier |
| **ORSAC - CAT Dienet** | ★☆☆☆☆ | Social, territorial | Pas repreneur industriel | "Option sociale" | Institutionnel |

## Stratégie d'Approche

### Phase 1: Tier 1 (Semaine 1)
1. **T'Rhea** via Olivier Aubert - proposition d'intégration stratégique
2. **Bovi-Coop** via Régis Favier - logique coopérative territoriale
3. **SBA** via Guillaume Megevand - mutualisation outil voisin

### Phase 2: Tier 2 (Semaine 2)
- Focus groupes avec capacité d'exécution industrielle
- Vérifier disponibilité deals récents

### Phase 3: Asset Focused (Semaine 3)
- Approche distributeurs pour contrats/clients plutôt qu'actif total

## Scorecard Custom Viande

```python
def score_viande_repreneur(acquirer):
    score = 0
    # Adéquation géographique (max 5)
    if distance < 50: score += 5
    elif distance < 200: score += 3
    
    # Capacité financière (max 3)
    if ca > 50M: score += 3
    elif ca > 10M: score += 2
    
    # Fit métier (max 5)
    if 'abattage' in activities: score += 3
    if 'decoupe' in activities: score += 2
    
    # Expérience distressed (max 2)
    if distressed_deals > 2: score += 2
    
    return score
```

## Timing & Budget

- **Prospection**: 3 semaines
- **DD**: 2 semaines par target
- **Offres**: 1ère offre J+21
- **Budget estimation**: 15-20K€ (frais juridiques + DD)

## Related

- [[brantham/deals/active/gesler/repreneurs-2026-06-03]]
- [[brantham/frameworks/qualification-distressed-2026-06-12]]
- [[brantham/knowledge/sectors/agriculture-agroalimentaire]]