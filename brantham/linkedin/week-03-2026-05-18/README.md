---
type: linkedin-week-pack
project: brantham
date: 2026-05-18
status: draft
---

# Pack LinkedIn — Semaine du 18 mai 2026

Suite directe au [post vautour](../week-02-2026-05-05/post-06-distressed-moral-vautour.md) (semaine 2).
Trois angles complémentaires pour varier les registres : **meme / coulisses / data**.

> Soren à choisir parmi A / B / C — chaque post est ready-to-publish.

## Posts

| Code | Registre | Format | Copy | Visuel HTML | Visuel PNG |
|---|---|---|---|---|---|
| **A** | Meme dark-humor | Image meme 4 cases + texte court | [post-A](post-A-meme-urssaf-copy.md) | [templates/post-A-meme-urssaf-lp.html](templates/post-A-meme-urssaf-lp.html) | `post-A-meme-urssaf.png` |
| **B** | Build-in-public coulisses | Image timeline + texte long | [post-B](post-B-mardi-cabinet-macbook-copy.md) | [templates/post-B-journee-mardi-lp.html](templates/post-B-journee-mardi-lp.html) | `post-B-journee-mardi.png` |
| **C** | Data-shock sec | Image stat-hero + texte court | [post-C](post-C-stat-shock-67pct-copy.md) | [templates/post-C-stat-67pct-lp.html](templates/post-C-stat-67pct-lp.html) | `post-C-stat-67pct.png` |
| **4** | Meme + mini-guide | Meme « they don't know » + post détaillé 4 sections | [post-4](post-4-valorisation-rj-copy.md) | [templates/post-4-meme-tdk-lp.html](templates/post-4-meme-tdk-lp.html) | `post-4-meme-tdk.png` |

## Workflow

1. **Choisir 1 angle** (A, B ou C) — ou les 3 si on étale sur la semaine.
2. **Render** : `cd vault/brantham/linkedin/week-03-2026-05-18 && python3 render.py`
   - Génère les `.png` (cream) + `-navy.png` (dark).
3. **Vérif visuelle** : ouvrir le PNG, contrôler typo / overflow.
4. **Publier** : copier le copy du `.md`, joindre le PNG, post sur LinkedIn.

## Architecture éditoriale (si on publie les 3)

- **Lun 18 mai** — Post A (meme URSSAF) → exploite la traction du vautour, viral.
- **Mer 20 mai** — Post B (mardi cabinet) → humanise, génère DM.
- **Ven 22 mai** — Post C (67% LJ directe) → boucle la séquence, pose le différenciateur Brantham.

## DA & cohérence

- Tous les visuels suivent le design system Brantham (`_design-system/base/`).
- Cream `#EFEBE0`, ink `#0A0A0A`, accent bordeaux `#7A1D17`.
- Typo : Source Serif 4 (titres / corps), DM Mono (méta / chiffres).
- Logo intégré dans `head.brand` ou en pied (meme).

## Related

- [[INDEX]]
- [[post-4-valorisation-rj-copy]]
- [[../week-02-2026-05-05/idees-prochains-posts]]
- [[../week-02-2026-05-05/post-06-distressed-moral-vautour]]
- [[../_design-system/README]]
