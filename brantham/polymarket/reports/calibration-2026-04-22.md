# Calibration report — 2026-04-22

Scope: last 14 days

## Global metrics

- **n** : 1768
- **brier** : 0.0793
- **log_loss** : 0.4784
- **ece** : 0.0401
- **wr_realized** : 0.8218
- **wr_expected** : 0.8403
- **pnl_realized_usdc** : 18893.52

### Reliability diagram

| bucket      |    n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|-----:|---------------:|--------------:|---------:|:---------|
| [0.00,0.10) |   17 |          0.082 |         0     |   -0.082 | yes      |
| [0.10,0.20) |  141 |          0.161 |         0.099 |   -0.062 | yes      |
| [0.20,0.30) |   22 |          0.243 |         0     |   -0.243 | yes      |
| [0.30,0.40) |   34 |          0.324 |         0.735 |    0.412 | yes      |
| [0.40,0.50) |   44 |          0.43  |         0.341 |   -0.089 | yes      |
| [0.50,0.60) |    1 |          0.572 |         0     |   -0.572 | low-n    |
| [0.60,0.70) |   11 |          0.692 |         0     |   -0.692 | yes      |
| [0.70,0.80) |   22 |          0.759 |         0.864 |    0.104 | yes      |
| [0.80,0.90) |  353 |          0.865 |         0.873 |    0.008 | yes      |
| [0.90,1.00) | 1123 |          0.976 |         0.955 |   -0.022 | yes      |

## Per alpha_type

| alpha_type      |    n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|-----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| CONFIRMED_NO    |  123 |     1     |    1     |  0      |     0      | 0      |     181.13 |
| CONFIRMED_YES   |   31 |     0     |    1     |  1      |    13.8155 | 1      |    -443.88 |
| MODEL_VS_MARKET | 1614 |     0.824 |    0.825 |  0.0677 |     0.2587 | 0.0331 |   19156.3  |

## ⚠️ Flagged (ECE > 0.12)

| alpha_type    |   n |   wr_real |   wr_exp |   ece |
|:--------------|----:|----------:|---------:|------:|
| CONFIRMED_YES |  31 |         0 |        1 |     1 |

Actionable: if ECE stays high across 7 days of sliding window and N > 30, reduce Kelly sizing for that pocket or disable via drift_monitor kill switch.

## Related

- [[_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]