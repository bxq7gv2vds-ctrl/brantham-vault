---
date: 2026-04-26
project: brantham
tags: [bug, textual, ui, fixed]
severity: high
---

# Bug : `@on(Button.Pressed)` sans selector ne fire pas dans TabbedContent

## Symptôme
Tous les boutons cliquables de l'action bar (Détail, Filtre AJ, Hunters, etc.) ne réagissent pas au clic souris ni à `btn.press()` programmatique. Seul le rendering visuel est OK.

User feedback : "il y a aucun bouton qui fonctionne"

## Cause racine
Le décorateur Textual `@on(Button.Pressed)` (sans CSS selector) attrape tous les `Button.Pressed` qui bubblent à l'App. Mais quand le widget Button est nested dans un `TabbedContent`, l'event est intercepté par les Tabs internes (qui contiennent eux-mêmes des Buttons pour switcher) et ne remonte jamais au handler app-level.

Sans selector, Textual considère que la stratégie de propagation est ambiguë et le handler n'est pas registered correctement.

## Fix
Ajouter un **CSS selector explicite** au décorateur pour cibler uniquement les boutons de la barre d'action :

```python
@on(Button.Pressed, "#action-bar Button")
def _on_action_button(self, event: Button.Pressed) -> None:
    cmd = getattr(event.button, "_cockpit_action", None)
    if cmd:
        event.stop()  # bloque la propagation pour éviter double-handling
        self.action_action_bar(cmd)
```

Le `event.stop()` est aussi important pour empêcher le Button de propager l'event à d'autres handlers.

## Vérification
Smoke test :
```python
btns[0].press()  # bouton "[ Détail ]"
# avant: top=Screen (rien)
# après: top=DetailModal ✓
```

## Leçon
- En Textual, **toujours qualifier `@on(Widget.Event)` avec un selector** dès qu'il y a plusieurs instances du même widget dans la hiérarchie
- `event.stop()` après dispatch pour éviter les doublons
- Tester l'action bar rapidement après chaque refacto UI

## Bonus pendant le fix
- Création de `Button` widgets réels (vs Static markup `[@click=...]`) → hover, focus, navigation Tab
- CSS dédiée pour les boutons : `min-width: 7`, `border: tall`, hover/focus colorés

## Where
- Fichier : `/Users/paul/Downloads/brantham-pipeline/cockpit/tui.py`
- Méthodes : `_render_action_bar`, `_on_action_button`, `action_action_bar`

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/_MOC]]
- [[_system/MOC-bugs]]
