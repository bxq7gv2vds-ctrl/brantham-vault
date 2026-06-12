# Deal Structures — Stock vs Asset Sale

**Utilité** : choisir la structure optimale pour acheteur et vendeur (impacts fiscaux, légaux, risque).

## Stock Sale (Acquisition de 100% des parts)

**Buyer acquiert:**
- Tous les assets (IP, customer contracts, data)
- Tous les liabilities (debt, contingent liabilities, indemnity risk)
- Continuité légale (pas de rupture de contrats nécessaire)

**Avantages Seller:**
- Simplicité administrative (une transaction)
- Généralement traité en capital gains (taxes favorables)
- Pas de recertification client (contracts restent valides)
- Plus rapide (pas de consent client massif)

**Désavantages Seller:**
- Liable pour liabilities cachées (même après closing)
- Reps & warranties = exposé 12–24 mois post-deal
- Escrow/holdback = trésorerie bloquée

**Avantages Buyer:**
- Assets intangibles → goodwill traité favorablement (Section 338)
- Continuité immédiate

**Désavantages Buyer:**
- Hérite ALL liabilities (connus + cachés)
- Plus cher en inspection (due diligence complète requise)

---

## Asset Sale (Acquisition des assets spécifiques)

**Buyer acquiert:**
- Assets ciblés: IP, contracts sélectionnés, clients choisis
- PAS de liabilities (sauf si explicitement assumées)

**Avantages Buyer:**
- Cherry-pick: sélectionne clients rentables, laisse les perdants
- Limited liability exposure
- Tax-efficient step-up (reset asset basis)

**Désavantages Buyer:**
- Recertification client massive (contracts doivent être reassigned)
- Perdre actifs importants: relationships, team knowledge
- Plus long (3–6 mois supplémentaires pour consent)

**Avantages Seller:**
- Liabilities restent dans la coquille (corp entity)
- Moins d'escrow (buyer = moins peur)

**Désavantages Seller:**
- Impôt double: corp tax sur asset sale + shareholder tax au distribution
- Abandon de contrats peut déclencher clause "change of control" (clients qui partent)
- Timing du shutdown de la coquille (dissolution taxes)

---

## Hybrid Structures

### Stock Sale + Escrow + Indemnity Insurance
```
Buyer pays: 70% upfront (stock transfer)
           20% escrowed (1 year hold)
           10% earn-out (performance 2 ans)

Seller risk: capped à escrow (max loss = 20%)
Buyer risk: mitigated par insurance ($X couverture)
```

### Reverse Triangular Merger
```
Parent Buyer creates subsidiary.
Subsidiary merges INTO target company.
Target shareholders get consideration.
Result: target becomes buyer subsidiary (continuity + liabilities).

Tax: Section 368(a)(2)(E) qualified reorganization
     (sellers = deferred tax, not immediate)
```

### Earnout Structure
```
Base price: $10M (cash + stock)
Earnout: +$2M si $5M revenue Y1 & 80% retention Y2

Avantages Seller: share upside, downside capped
Avantages Buyer: pay for performance, tax deferral

Piège: seller alignment (peut sabotter pour $2M extra)
       metric gaming (revenue recognition, early bookings)
```

---

## Tax Optimization (US / EU Context)

| Structure | Seller Tax | Buyer Tax | Speed | Complexity |
|-----------|-----------|-----------|-------|------------|
| Stock sale | Capital gain (~20%) | Goodwill step-up (depreciate over 15y) | Fast (6–8w) | Moderate |
| Asset sale | Double tax (~34% combined) | Step-up basis | Slow (16–20w) | High |
| 338(h)(10) election | Capital gain, ~20% | Asset step-up immediate | Medium (10–12w) | Very high |
| Merger (qualified) | Deferred (stock-for-stock) | Deferred | Medium (12–16w) | Very high |

---

**Decision Rule:**
- **Seller perspective** : Stock sale 95% du temps (sauf si liabilities énormes).
- **Buyer perspective** : Asset sale si seller liabilities > 10% deal price, sinon stock merger.
- **Earn-out** : utilisé si valuation gap >20% (diffère le prix, aligne risque).

