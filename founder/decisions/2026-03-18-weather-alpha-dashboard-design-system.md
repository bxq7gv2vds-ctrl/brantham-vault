---
type: decision
project: weather-alpha
date: 2026-03-18
status: implemented
---

# Decision: Design System Weather Alpha Dashboard

## Contexte
Le dashboard Weather Alpha (Next.js 15, Tailwind 4) avait 64 composants, 8 pages, mais un design basique. L'expansion du tradeable universe (15 stations, 4 variables, 4 horizons) necessitait une refonte visuelle.

## Decision
Implementer un design system complet avec :
- Inter font via next/font/google
- Palette sans violet (teal #14b8a6 a la place)
- 4 animations CSS (fadeIn, slideUp, countUp, shimmer)
- Panel variants (default, glass, elevated)
- Badge pulse pour indicateurs LIVE
- TabBar avec sliding underline
- Sidebar SVG icons + tooltips + auto-collapse <1440px

## Alternatives considerees
- Shadcn/UI : trop lourd, pas adapte au theme trading terminal
- Framer Motion : overhead JS, CSS animations suffisantes
- Radix primitives : unnecessary complexity pour ce cas

## Resultat
- 12 pages, zero erreur TS
- 2 nouvelles pages (Universe, Performance)
- Sidebar restructuree (TRADE/INTEL/ANALYSIS)
- Zero violet dans le codebase
