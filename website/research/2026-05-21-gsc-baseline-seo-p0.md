---
type: research
project: website
date: 2026-05-21
tags: [seo, gsc, baseline, p0-fixes]
---

# GSC Baseline — P0 SEO fixes (2026-05-21)

## Statut collecte API

**Bloqué** : le fichier service account GSC est absent.

- Path configuré : `autopilot/.secrets/gsc-service-account.json`
- Variable : `GOOGLE_SERVICE_ACCOUNT_FILE` dans `autopilot/.env`
- Action requise : restaurer le JSON depuis Google Cloud Console (Search Console API + Indexing API) et l'ajouter au path ci-dessus

Commande une fois le fichier restauré :

```bash
cd /Users/paul/zura-inspired/autopilot
uv run python -c "
from collectors import gsc
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
key = os.environ['GOOGLE_SERVICE_ACCOUNT_FILE']
out = Path('.snapshots')
gsc.collect_daily(key, 'sc-domain:branthampartners.fr', out, days_back=28)
"
```

## Dernière baseline disponible (22/04/2026)

Source : [[website/research/2026-04-22-gsc-audit-etat-des-lieux]]

| Métrique | Valeur |
|---|---|
| Clics (36 j) | 194 |
| Impressions | 8 908 |
| CTR | 2,2 % |
| Position moyenne | 10,9 |
| Pages indexées | 92 |
| Non indexées | 61 |

### Top queries (clics > 0)

| Query | Clics | Impr | Pos |
|---|---|---|---|
| modèle offre reprise liquidation judiciaire | 2 | 14 | 6,7 |
| depot bilan transport routier 2026 | 2 | 11 | 6,8 |
| liquidation judiciaire transport routier 2026 | 1 | 44 | 6,1 |

### Quick wins identifiés (0 clic, fort volume)

| Query | Impr | Pos |
|---|---|---|
| cession entreprise rennes | 73 | 22,7 |
| score3 liquidation | 31 | 7,7 |
| liste entreprise liquidation judiciaire gratuit bodacc | 44 | 11,9 |

## P0 corrigés aujourd'hui (local, deploy pending)

1. `cession-entreprise-rennes.html` supprimée → 301 vers `rachat-entreprise-rennes.html`
2. `article.html` renommé → `defaillances-entreprises-2025.html` + 301
3. Domaine harmonisé `brantham.fr` → `branthampartners.fr` (pages légales)
4. `og-image.png` + `apple-touch-icon.png` : déjà en prod (HTTP 200)
5. Autopilot : skip `cession-entreprise-{ville}` si `rachat-entreprise-{ville}` existe
6. Autopilot content_gen : plus de référence à `/styles.css` inexistant

## Post-deploy checklist GSC

1. Deploy Vercel prod
2. Search Console → Sitemaps → resubmit `sitemap.xml`
3. URL Inspection : `defaillances-entreprises-2025.html`, `rachat-entreprise-rennes.html`
4. Valider 301 sur `/article.html` et `/cession-entreprise-rennes.html`
5. Relancer collecte API GSC (commande ci-dessus)

## Related

- [[website/_MOC]]
- [[website/research/2026-04-22-gsc-audit-etat-des-lieux]]
- [[website/bugs/2026-05-21-p0-seo-fixes]]
- [[_system/MOC-bugs]]
