---
type: protocol
project: brantham
updated: 2026-03-27
---

# OUTPUT PROTOCOL — Standard Cowork Brantham

**Règle absolue : chaque agent DOIT écrire son fichier output JSON à la fin de chaque run.**
Sans ce fichier, le run n'est pas considéré comme terminé.

## Dossier de sortie

```
/Users/paul/vault/brantham/cowork-outputs/
```

## Nom du fichier

```
[agent]-[YYYY-MM-DD]-[HHMM].json
```

Exemples :
- `sourcing-2026-03-27-0700.json`
- `deal-analysis-2026-03-27-0830.json`
- `buyer-hunt-2026-03-27-0900.json`

## Format JSON standard

```json
{
  "agent": "[nom-agent]",
  "run_id": "[agent]-[YYYY-MM-DD]-[HHMM]",
  "timestamp": "[ISO 8601]",
  "status": "success | partial | error",
  "duration_min": 0,
  "summary": "1 phrase — ce qui a été fait",

  "data": {
    // contenu spécifique à chaque agent (voir ci-dessous)
  },

  "actions_taken": [
    "action 1 réalisée",
    "action 2 réalisée"
  ],

  "pending_for_human": [
    {
      "who": "Paul | Soren",
      "action": "description précise",
      "urgency": "rouge | orange | vert",
      "deadline": "YYYY-MM-DD ou null"
    }
  ],

  "triggered_next": [
    "nom-agent-suivant (si applicable)"
  ],

  "errors": [
    {
      "type": "scrape_fail | api_error | file_missing | other",
      "description": "...",
      "impact": "bloquant | mineur"
    }
  ]
}
```

## Champ `data` par agent

### sourcing
```json
"data": {
  "sites_scraped": 0,
  "new_opportunities": 0,
  "go": [{"slug": "", "secteur": "", "ca": 0, "deadline": "", "score": 0}],
  "watch": [{"slug": "", "secteur": "", "ca": 0, "deadline": "", "score": 0}],
  "pass": 0,
  "urgent_alerts": [{"slug": "", "days_left": 0, "statut": ""}]
}
```

### pipeline-check
```json
"data": {
  "pipeline_health_score": 0,
  "deals_actifs": 0,
  "rouge": [{"slug": "", "days_left": 0, "problem": "", "action": ""}],
  "orange": [{"slug": "", "days_left": 0, "risk": ""}],
  "vert": [{"slug": ""}],
  "pending_human": [{"slug": "", "waiting_since": "", "action": ""}]
}
```

### deal-analysis
```json
"data": {
  "slug": "",
  "score": 0,
  "decision": "PRIORITE_ABSOLUE | PIPELINE_NORMAL | VEILLE | ARCHIVER",
  "ca_estime": 0,
  "procedure": "LJ | RJ | SV",
  "deadline": "",
  "days_left": 0,
  "key_assets": [""],
  "main_risks": [""],
  "missing_data": [""],
  "analyse_path": ""
}
```

### buyer-hunt
```json
"data": {
  "slug": "",
  "total_identified": 0,
  "total_qualified": 0,
  "top_buyers": [
    {
      "rang": 0,
      "siren": "",
      "nom": "",
      "ca": 0,
      "ca_multiple": 0,
      "contact_nom": "",
      "contact_email": "",
      "contact_linkedin": "",
      "priority_score": 0,
      "match_reason": ""
    }
  ],
  "acheteurs_path": ""
}
```

### morning-brief
```json
"data": {
  "date": "",
  "pipeline_summary": {
    "deals_actifs": 0,
    "teasers_prets": 0,
    "acheteurs_identifies": 0,
    "prets_outreach": 0
  },
  "alertes_rouges": 0,
  "new_detections_overnight": 0,
  "paul_actions": ["", "", ""],
  "soren_actions": ["", "", ""],
  "brief_path": ""
}
```

### contact-enricher
```json
"data": {
  "slug": "",
  "total_enriched": 0,
  "ready_for_outreach": 0,
  "enrichment_rate": "",
  "contacts": [
    {
      "rang": 0,
      "nom_entreprise": "",
      "contact_nom": "",
      "email": "",
      "email_confidence": "verifie | probable | incertain",
      "linkedin": "",
      "ready": true
    }
  ],
  "contacts_path": "",
  "outreach_brief_path": ""
}
```

## Commande bash de génération

À la toute fin de chaque run, écrire le fichier :

```bash
OUTPUT_DIR=/Users/paul/vault/brantham/cowork-outputs
AGENT=[nom-agent]
TIMESTAMP=$(date +%Y-%m-%d-%H%M)
OUTPUT_FILE=$OUTPUT_DIR/$AGENT-$TIMESTAMP.json

cat > $OUTPUT_FILE << 'OUTPUT_EOF'
{
  "agent": "[agent]",
  "run_id": "[agent]-[TIMESTAMP]",
  "timestamp": "[ISO_DATE]",
  "status": "success",
  "summary": "...",
  "data": { ... },
  "actions_taken": [...],
  "pending_for_human": [...],
  "triggered_next": [...],
  "errors": []
}
OUTPUT_EOF

echo "Output écrit : $OUTPUT_FILE"
```

## Related
- [[brantham/cowork-prompts/INDEX]]
