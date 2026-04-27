---
type: session
project: website
date: 2026-04-27
tags: [orthographe, typographie, SEO, deploy]
---

# Audit cohérence/orthographe site + corrections + deploy prod

## Contexte
Audit complet du site `branthampartners.fr` (141 pages HTML statiques) pour cohérence éditoriale et orthographe française. Suivi par corrections automatiques en masse et déploiement prod Vercel.

## Audit (lecture seule)
Rapport généré : `/Users/paul/zura-inspired/audits/audit-coherence-orthographe-2026-04-27.md`

Top 5 problèmes identifiés :
1. IDs HTML sans accents (faux problème — voir conclusions)
2. "tribunal de commerce" en minuscule (627 vs 3 correct)
3. Mots français sans accents (creancier, periode, redaction, etc.)
4. 8 924 espaces simples au lieu d'insécables avant `:` `;` `?` `!`
5. Acronyme "AJ" non défini à première mention

## Corrections appliquées

### Phase A — Orthographe (script `/tmp/fix_accents.py` + `fix_accents2.py`)
- **80+ mots français** accentués automatiquement : rédaction, périmètre, représentation, créancier, acquéreur, présentation, crédibilité, opérations, débarrassés, équipements, état, accélérée, préparation, réglementaire, développement, déroulement, dépendance, etc.
- **Volume** : 356 lignes / 70 fichiers
- **Garde-fous** : verbes ambigus (propose/proposé, décide/décidé, intègre conjugué, identifie/identifié, etc.) volontairement exclus pour éviter faux positifs
- **Bug détecté en cours** : 1er run avait "propose" → "proposé" qui cassait le verbe au présent → rollback complet + raffinement de la liste

### Phase B — Casse (`/tmp/fix_tribunal.py`)
- "tribunal de commerce" → "**Tribunal de commerce**" (T majuscule, c minuscule = norme typo FR officielle, pas la double-majuscule "Tribunal de Commerce" anglo-saxonne suggérée par l'audit)
- 595 lignes / 97 fichiers, 900 occurrences
- 32 résiduels intentionnels = `<meta name="keywords">` (convention SEO en minuscule)

### Phase C — IDs HTML (analyse seule)
- **Aucune action** : les IDs ASCII (`id="creancier-chirographaire"`) sont une best practice web. Tous les `<a href="#xxx">` correspondent exactement aux `<id="xxx">`. Aucune ancre cassée.
- L'audit avait diagnostiqué un faux problème ici.

### Phase D — Acronyme AJ (annulée après casse)
- Script naïf `/tmp/fix_aj.py` qui ajoutait "Administrateur judiciaire (AJ)" à la 1ère occurrence d'"AJ"
- **Casse détectée** sur `rachat-entreprise-marseille.html:688` — "AJ Partenaires Marseille" (raison sociale d'un cabinet) transformée en "Administrateur judiciaire (AJ) Partenaires Marseille"
- Aussi : `business-plan-reprise-entreprise-difficulte.html:689` — "certains AJ" (pluriel) cassé
- **Rollback complet** : `replace('Administrateur judiciaire (AJ)', 'AJ', 1)` sur les 5 fichiers touchés
- Conclusion : la définition d'acronyme nécessite un jugement humain, pas automatisable safely

### Phase E — Espaces insécables (`/tmp/fix_nbsp.py`)
- `&nbsp;` ajouté avant `:` `;` `?` `!` dans le texte HTML
- 5 933 segments / 141 fichiers
- 4 152 avant `:`, 1 692 avant `?`
- Scripts/styles/JSON-LD préservés via state machine ligne par ligne
- Regex finale : `re.sub(r' ([:;!?])(?=\s|<|$|\))', r'&nbsp;\1', text)` appliquée uniquement aux text nodes entre balises

### Bonus
- Faute pré-existante corrigée : `rachat-entreprise-le-havre.html:696` "intere" → "intègre"

## Backup
`/tmp/zura-html-backup-2026-04-27.tar.gz` (2,7 Mo) — état pré-corrections

## Deploy
```bash
cd /Users/paul/zura-inspired && vercel deploy --prod --yes
```
- Production : `https://branthampartners.fr` (alias)
- Inspect : https://vercel.com/paulroulleau-7473s-projects/zura-inspired/FuW4FDr92UQcYUN6PuqihnrfSa3K
- 11.1 MB upload, 19s build
- Vérifié post-deploy : "Tribunal de commerce" et "&nbsp;:" présents en prod

## Leçons
1. **Ne jamais faire de replace global sans masking d'attributs/URLs** — sinon les `href`, `id`, `name`, `content` sont touchés.
2. **Verbes français en -e/-er/-ir sont presque tous ambigus** entre présent indicatif (sans accent) et participe passé (avec accent). Toute liste de remplacements automatiques doit les exclure.
3. **L'acronyme→définition n'est pas automatisable** : "AJ" peut être un acronyme, une raison sociale, un nom propre. Toujours laisser au jugement humain.
4. **L'audit LLM peut diagnostiquer des faux problèmes** : ici les IDs ASCII présentés comme "ancres cassées" alors qu'ils sont conformes aux best practices et fonctionnent.
5. **Norme typo FR pour les institutions** : "Tribunal de commerce" (T maj seulement), pas "Tribunal de Commerce" (anglo-saxon).

## Restant manuel (skip volontaire)
- Définition acronyme AJ par page (éditorial)
- Renommage `role-administrateur-judiciaire-acquereur.html` → version accentuée (casse les liens externes, faible ROI SEO)

## Related
- [[website/_MOC]]
- [[_system/MOC-bugs]]
- [[_system/MOC-patterns]]
- [[patterns/html-mass-corrections-safe-replacement|HTML mass corrections — safe replacement pattern]]
- [[brantham/_MOC]]
