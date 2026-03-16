---
type: session
project: website
date: 2026-03-15
topic: audit-maillage-interne
---

# Audit Maillage Interne — Brantham Partners

## Contexte
Audit complet du maillage interne des 20 pages HTML du site.

## Resultats — Matrice (liens hors nav/footer)

| Page | Sortants (body) | Entrants |
|------|----------------|----------|
| Equipe | 2 | 0 (ORPHELINE) |
| Article Blog | 3 | 2 |
| Sourcing Proprietaire | 3 | 14 |
| Pillar (Rachat) | 3 | 14 |
| Glossaire M&A | 2 | 14 |
| Barometre | 5 | 14 |
| Due Diligence | 6 | 14 |
| Execution Audience | 6 | 14 |
| Insights Index | 12 | 14 |
| Liquidation Judiciaire | 8 | 14 |
| Plan de Cession | 8 | 14 |
| Redressement Judiciaire | 10 | 14 |
| Reprise a la Barre | 10 | 14 |
| Valorisation | 10 | 14 |
| Accueil | 7 | 19 |

## Pages Orphelines / Sous-linkees

- **Equipe** : 0 entrant. Aucune page du site ne pointe vers /equipe.html.
- **Article Blog** : seulement 2 entrants (Accueil + Insights).
- **Sourcing Proprietaire** : seulement 3 liens sortants dans le body (pas de lien vers Barometre, Due Diligence, Execution Audience, Valorisation...).
- **Glossaire M&A** : seulement 2 liens sortants (Pillar + Insights). Enormement de termes definis mais zero lien vers les pages services correspondantes.
- **Pillar (Rachat)** : 3 liens body uniquement (Glossaire + Barometre x2). Manque liens vers les 4 services et les 3 guides.

## Accueil — Pages non linkees
L'accueil ne linke PAS vers :
- Glossaire M&A
- Barometre
- Valorisation
- Redressement Judiciaire
- Liquidation Judiciaire
- Plan de Cession
- Reprise a la Barre
- Equipe

## Top 5 Liens a Ajouter

1. **Toutes les pages → Equipe** : page orpheline complete, zero entrant.
2. **Glossaire M&A → pages services** (Sourcing, Due Diligence, Execution, Valorisation) : le glossaire definit ces concepts, il devrait renvoyer vers les services correspondants.
3. **Pillar (Rachat) → 4 services + 3 guides** : la pillar page est le hub strategique, elle doit linker vers tous les contenus du cluster.
4. **Accueil → Barometre + Glossaire + Valorisation** : 3 pages importantes absentes de la homepage.
5. **Sourcing Proprietaire → Due Diligence + Execution Audience** : la sequence logique (sourcing -> DD -> execution) doit etre materialise dans les liens.

## Audit Anchor Texts
- Pas de "cliquez ici" detecte — OK.
- Liens logo (href="/") avec ancre vide = normaux (image).
- Quelques ancres tres longues (blocs de texte HTML) dans les sections "En relation" — non problematique mais perfectible.
- Ancres contextuelles : bonnes pratiques respectees (ex: "due diligence acceleree", "liquidation judiciaire", "plan de cession").

## Liens Externes
- `https://app.brantham.fr` : CTA app (normal)
- `https://linkedin.com/in/paulroulleau` : profil LinkedIn equipe
- Google Fonts : resources techniques
- Pas de liens vers des sources d'autorite tierces (Infogreffe, BODACC, Legifrance, INSEE) dans le contenu.
