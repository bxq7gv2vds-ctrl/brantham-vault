# Intégration Kickbacks AI - Claude Code

## Vue d'ensemble

Extension VS Code permettant de générer des revenus passifs grâce aux publicités affichées pendant les temps d'attente de Claude Code.

### Caractéristiques principales
- 50% des revenus publicitaires
- Publicités subtiles pendant les temps d'attente IA
- Intégration transparente avec Claude Code

## Installation

### Script d'installation automatisée
- Location: `/Users/paul/.claude/projects/-Users-paul/install-kickbacks-ai.sh`
- Usage: `./install-kickbacks-ai.sh`
- Configure automatiquement VS Code et ajoute les paramètres nécessaires

### Configuration requise
- VS Code installé
- Claude Code extension installée
- Compte Stripe Connect pour les paiements

## Configuration VS Code

```json
{
    "kickbacks.enabled": true,
    "kickbacks.showAds": true,
    "kickbacks.adFrequency": "moderate",
    "kickbacks.aiWaitTime": 2.0,
    "kickbacks.adPlacement": "sidebar",
    "claude.code.enabled": true
}
```

## Emplacement des fichiers

- Script d'installation: `/Users/paul/.claude/projects/-Users-paul/install-kickbacks-ai.sh`
- Documentation: `/Users/paul/.claude/projects/-Users-paul/README-kickbacks-ai.md`
- Configuration settings.json: `$HOME/.config/Code/User/settings.json`

## Notes d'implémentation

- Extension installée via marketplace.visualstudio.com
- Fonctionne en arrière-plan pendant les attentes Claude Code
- Pas de modification nécessaire dans Claude Code lui-même
- Les publicités n'apparaissent que pendant les temps d'attente

## Liens

- [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Kickbacksai.kickbacks-ai)
- [Site officiel](https://kickbacks.ai)

## Related

- [[_system/MOC-integrations]] - Index des intégrations système
- [Claude Code](https://code.claude.com) - Documentation officielle Claude Code