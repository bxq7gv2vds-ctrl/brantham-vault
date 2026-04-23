---
type: moc
project: brantham
updated: 2026-04-23
---

# Brantham Deals — Map of Content

Tous les deals du pipeline. Auto-alimenté par l'orchestrateur autopilot.

## Statuts pipeline

```
detecte → notifie → valide_pour_buyer_hunt → analysed → acheteurs_identifies → contacts_enrichis → drafts_prets → outreach_envoye → mandat_signe → ferme
                                                                                                                          ↓
                                                                                                                       passe (archived)
```

## Structure

```
deals/
├── _MOC.md                    (ce fichier)
├── TEMPLATE.md                (template par deal — legacy)
├── active/                    (deals en cours)
│   └── <slug>/
│       ├── raw.json           (données brutes scraping AJ + BODACC)
│       ├── analyse.md         (analyse financière + juridique)
│       ├── teaser.md          (teaser anonyme)
│       ├── acheteurs.json     (30-50 repreneurs identifies)
│       ├── contacts.json      (top 30 dirigeants enrichis)
│       ├── outreach-emails.json     (data structuree pour drafts)
│       ├── outreach-linkedin.md     (DMs LinkedIn copy-paste)
│       └── outreach-drafts-<slug>.md (recap final emails)
└── archived/
    └── <slug>/
```

## Deals actifs

Auto-listé par `python3 /Users/paul/Library/Brantham/scripts/autopilot_orchestrator.py status`.

## Pipeline volumetric goals

- 100 emails outreach / jour
- 30-40 DMs LinkedIn / jour
- Toutes les opportunites des 31 sites AJ traitees daily

## Related

- [[brantham/_MOC]]
- [[brantham/cowork-prompts/INDEX]]
- [[brantham/context/process-end-to-end]]
