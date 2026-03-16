---
type: bug-fix
project: brantham
date: 2026-03-13
component: dashboard-frontend
severity: critical
tags:
  - css
  - mobile
  - routing
---

# Bug: Mobile Router Broken by CSS Animation Rule

## Symptom

On mobile (< 480px), navigating to any page via tab bar or hash shows the wrong page. Multiple pages render simultaneously. The "Accueil" button shows M&A or docs instead of overview.

## Root Cause

In `frontend/index.html`, the mobile media query applies animation to ALL `.page` elements:

```css
@media (max-width: 480px) {
  .page { animation: 0.2s ease mobFadeIn; }
}
```

The `mobFadeIn` animation overrides `display: none` from `.page { display: none; }`, making ALL pages visible simultaneously. The correct selector should be `.page.active`.

## Fix

```css
@media (max-width: 480px) {
  .page.active { animation: 0.2s ease mobFadeIn; }
}
```

## Related

- The `handleRoute` wrapper for EXTENDED_PAGES also has issues with routing delegation
- See audit report: `swarm/tracks/2026-03-13-001/reports/T01.md`
- Related: [[brantham/dashboard/_MOC]]
