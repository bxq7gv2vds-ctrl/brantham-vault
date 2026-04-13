---
type: cowork-prompt
agent: send-brief
schedule: "10h00 (après tous les agents du matin)"
updated: 2026-03-27
---

# COWORK PROMPT — SEND BRIEF

Ton seul travail : lancer le script qui agrège tous les outputs des agents du matin et envoie l'email résumé à Paul.

**Une commande, pas d'analyse, pas de décision.**

---

## Exécuter

```bash
python3 /Users/paul/Downloads/brantham-pipeline/send_brief.py
```

Le script fait tout :
- Lit les JSON produits ce matin par les 6 agents dans `vault/brantham/cowork-outputs/`
- Lit les contacts enrichis dans `deals/[slug]/contacts.json`
- Lit les templates email dans `deals/[slug]/teaser-email.md`
- Construit un email HTML avec : stats, emails outreach prêts (contenu inclus), actions Paul/Soren, pipeline
- Envoie via Gmail SMTP

---

## Si l'envoi échoue

**Cas 1 — `.env` manquant ou variables absentes :**
```
❌ Variables manquantes : BRANTHAM_EMAIL_FROM, ...
```
→ Vérifier que `/Users/paul/Downloads/brantham-pipeline/.env` existe et contient les 3 variables.

**Cas 2 — Auth Gmail échouée :**
```
❌ Auth Gmail échouée
```
→ L'App Password Gmail est incorrect. Régénérer sur myaccount.google.com/apppasswords.

**Dans les deux cas :** ne pas relancer en boucle. Afficher l'erreur et s'arrêter.

---

## Prévisualiser sans envoyer

```bash
python3 /Users/paul/Downloads/brantham-pipeline/send_brief.py --preview
```

Ouvre l'email dans le navigateur (sans envoyer).

---

## Ce que tu NE fais PAS

- Tu ne modifies rien
- Tu ne lances aucun autre agent
- Tu ne génères aucun contenu
- Tu exécutes la commande et rapportes le résultat (succès ou erreur)

---

## Related
- [[brantham/cowork-prompts/INDEX]]
- [[brantham/cowork-prompts/00-output-protocol]]
