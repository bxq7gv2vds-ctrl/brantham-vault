# Session Auto-Enrichment — 2026-04-04

**Heure** : 04h34 CEST
**Budget LLM** : ~$0.48 / $0.50

---

## Resultats

| Metrique | Valeur |
|----------|--------|
| Scraper AJ lance | Oui (31 sites / 40, 458 opportunites) |
| Opportunites qualifiees identifiees | 321 (CA>500k ou score>60) |
| Nouvelles opportunites non traitees | 321 |
| Top 10 selectionnees | 10 |
| Dossiers deals crees | 10 |
| Enrichissements Pappers reussis | 5 / 10 |
| Enrichissements Pappers skipped (anon) | 5 / 10 |
| Erreurs | 0 |
| Repreneurs identifies | 5 par deal via API Entreprises |

---

## Top 10 deals traites

1. **ajire-ecole-de-conduite-prezeau** — ECOLE CONDUITE PREZEAU | SIREN 339957037 | Dept 85
2. **trajectoire-cyfac-meral** — CYFAC & MERAL Cycles | Fabrication cycles haut-de-gamme
3. **ajilink-sudouest-sas-mgmv** — SAS MGMV (FRENCH DISORDER) | SIREN 989826672 | Gironde
4. **ajilink-sudouest-h-a-location** — H&A LOCATION (barriques viti) | Gironde | deadline 24/04
5. **ajup-sas-abeil** — SAS ABEIL Literie | SIREN 533134698 | Cantal
6. **aj-specialises-2133** — Entreprise sante DOM/TOM | CA 5.76M€ | 37 salaries (anon)
7. **aj-specialises-2092** — Infrastructures portuaires | CA 5.3M€ | 16 salaries (anon)
8. **aj-specialises-2230** — Charcuterie industrielle Var | CA 3.6M€ | 30 salaries (anon)
9. **aj-specialises-2144** — Reseau pharmaceutique | CA 2.36M€ | 37 salaries (anon)
10. **aj-specialises-2091** — Mobilier Agencement CHR | ~3M€ | referencements (anon)

---

## Infrastructure

- API FastAPI (port 8000) : hors service au moment du run
- Repreneurs identifies via API Entreprises (fallback gouvernement)
- Pappers : 5 lookups reussis (non-anon), 5 skips (opportunites anonymes AJ Specialises)

---

## Actions suivantes

- Completer avec datarooms AJ
- Relancer API FastAPI pour matching 4D
- CYFAC et H&A Location : rechercher SIRENs manuellement

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
- Deep enrichment termine a 04:39
---
