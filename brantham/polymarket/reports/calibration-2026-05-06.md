# Calibration report — 2026-05-06

Scope: last 14 days

## Global metrics

- **n** : 212
- **brier** : 0.0699
- **log_loss** : 0.2748
- **ece** : 0.1076
- **wr_realized** : 0.7406
- **wr_expected** : 0.8482
- **pnl_realized_usdc** : -868.02

### Reliability diagram

| bucket      |   n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|----:|---------------:|--------------:|---------:|:---------|
| [0.20,0.30) |   1 |          0.249 |         0     |   -0.249 | low-n    |
| [0.40,0.50) |  48 |          0.424 |         0     |   -0.424 | yes      |
| [0.90,1.00) | 163 |          0.977 |         0.963 |   -0.014 | yes      |

## Per alpha_type

| alpha_type      |   n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| MODEL_VS_MARKET | 212 |     0.741 |    0.848 |  0.0699 |     0.2748 | 0.1076 |    -868.02 |

## Related

- [[brantham/infra/_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]