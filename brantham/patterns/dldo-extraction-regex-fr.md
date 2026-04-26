---
projet: brantham
type: pattern
tags: [scraping, regex, dldo, fr]
date: 2026-04-26
---

# Pattern — Extraction DLDO multi-format français

## Problème
Les sites d'AJ français exposent la **Date Limite de Dépôt d'Offres** dans 8 formulations différentes et 2 formats de date (numérique + lettré). Un seul regex ne capture pas tout.

## Patterns lead clauses (8)
1. `date limite (de remise|dépôt) (des offres)? : DATE`
2. `remise des offres (le|au) DATE`
3. `dépôt des offres (le|au|avant le) DATE`
4. `date butoir DATE`
5. `DLDO (le|du|au)? DATE`  ← attention au "le" optionnel après DLDO
6. `offres attendues (au|le|avant le) DATE`
7. `avant le DATE`
8. `jusqu'au DATE`

## Formats de date acceptés
**Numérique** : `DD/MM/YYYY` ou `DD/MM/YY` (séparateurs `/`, `.`, `-`)
**Lettré FR** : `DD <mois> YYYY` ou `DD <mois> YY` (mois courts ou complets, accents tolérés)

```python
_FR_MONTHS = (
    r"(?:janv(?:ier|\.)?|f[ée]vr(?:ier|\.)?|mars|avr(?:il|\.)?|mai|juin|"
    r"juil(?:let|\.)?|ao[uû]t|sept(?:embre|\.)?|oct(?:obre|\.)?|"
    r"nov(?:embre|\.)?|d[ée]c(?:embre|\.)?)"
)
```

## Piège regex — alternation année
`(\d{2}|\d{4})` matche **toujours** `\d{2}` en premier (greedy gauche-droite). Pour préférer 4 digits, écrire `(\d{4}|\d{2})`. Sinon "2026" devient "20" → year=2020.

## Stratégie 3 niveaux (cheap → cher)
```python
def enrich_one(opp):
    # 1. URL elle-même (ex: BCM met DLDO dans le slug : /dldo-le-04-05-2026-a-14h00/)
    # 2. notes_scraper déjà en DB (ex: BCM, Reajir mettent DLDO dans le titre liste)
    # 3. Fetch page détail (requests + fallback LightPanda)
    for src in [url, notes]:
        iso, raw = extract_dldo(src)
        if iso: return ok
    text = fetch_text(url)
    return extract_dldo(text)
```

## Sanity check
- Refuse > 5 ans dans le passé (dates Y2K bugs)
- Refuse > 2 ans dans le futur (typos de l'AJ)
- **Garde les dates passées récentes** : sert au filtre TUI actif/expiré

## Coverage atteint sur 30 sites AJ français
- **91.3% (419/459 opps)**
- 100% : FHBX, Asteren, AJRS, Meynet, Abitbol, Ajilink Provence/Sud-Ouest/Grand Est, P2G, BMA, Trajectoire, Cardon, BCM, AJ Spé, AJ UP, CBF, AJ Partenaires
- Limites structurelles (sites qui ne publient simplement pas) : Ascagne, Maydaymag (presse)

## Code
`/Users/paul/Downloads/brantham-pipeline/cockpit/enrich_dldo.py`

## Origine
Session [[brantham/sessions/2026-04-26-cockpit-aj]] — Phase A du cockpit triage.

## Related
- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
- [[brantham/patterns/cockpit-tui-triage]]
- [[brantham/sessions/2026-04-26-cockpit-aj]]
