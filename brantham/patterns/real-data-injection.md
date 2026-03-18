# Pattern: Real Data Injection into Agent Population

## Context
MiroFish world simulator needs real agents (buyers, mandataires, tribunaux) from Brantham PostgreSQL alongside synthetic agents.

## Solution

### Architecture
- `backend/ma/data/loader.py` — 5 loaders (procedures, buyers, mandataires, tribunaux, calibration)
- `backend/ma/agents/population.py` — `generate_population()` checks `data_mode` and injects real agents
- Real agents reduce synthetic count per type: `max(0, config.n_type - n_real_type)`

### Buyer Classification (no price data available)
Most repreneurs have NULL `prix_min/prix_max`. Classification by:
1. `nb_acquisitions >= 3` -> SERIAL_ACQUIRER
2. Name contains GROUPE/HOLDING/CAPITAL/INVEST -> FONDS_PE
3. Name starts with M./Madame/Monsieur -> REPRENEUR_INDUSTRIEL
4. Default -> REPRENEUR_INDUSTRIEL

Result: 130 repreneurs, 10 fonds PE, 3 serial acquirers from 143 real buyers.

### Calibration
`calibrate_distributions()` returns real NAF/region weights from 84K+ procedures.
Applied via `_apply_calibrated_weights()` before synthetic agent generation.
- 30 NAF codes (top: 43=15.9%, 56=13.5%, 47=11.6%)
- 18 regions (IDF=24.3%, ARA=10.1%)

### Mandataire Reputation
`taux_cession * 5.0 + 0.3` -> maps [0, 0.14] to [0.3, 1.0]

### Tribunal Geo
Department-to-region mapping dict for `geo_pref` assignment.

## Performance
- 7459 agents (1152 real) + 80 rounds = 5.3s
- 6884 agents (synthetic) + 50 rounds = 2.85s
- Zero regression from real data injection

## Date
2026-03-17
