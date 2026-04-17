## Comparaison baseline → filter

| Mode | N | WR | P&L | Sharpe | Max DD |
|---|---|---|---|---|---|
| Baseline (passthrough) | 1599 | 81.9% | $-619.99 | -9.23 | -56.6% |
| Filter + Kelly | 1540 | 97.1% | $1,049.50 | 12.30 | 0.0% |

**Δ**: $+1,669.49 (+269.3%)

## Sum-to-1 arbitrage (7 derniers jours de price_bars)

- Opportunities détectées: 21,390
- Groups uniques: 377
- Profit moyen: 22.22%
- Profit max: 232.00%
- PnL espéré total (notional $50/arb): $237,600.33

---
# Alpha Engine — Filter + Kelly (bankroll $1,000)
_Generated 2026-04-17 12:25 UTC_

## Configuration
```json
{'bankroll': 1000.0, 'slippage': {'depth_usdc': 250.0, 'slope': 0.008, 'fixed_bps': 5.0, 'reject_rate': 0.02}, 'apply_slippage': True, 'daily_loss_cap_pct': 1.0}
```

## Résumé

| Métrique | Valeur |
|---|---|
| N trades | 1,540 |
| Win rate | 97.1% |
| P&L total |  $  1,049.50 |
| Avg win |  $      1.43 |
| Avg loss | -$     45.10 |
| Profit factor | 1.97 |
| Sharpe (ann.) | 12.30 |
| Sortino (ann.) | 0.00 |
| Calmar | 0.00 |
| Max drawdown | 0.0% |
| Max DD duration | 0j |
| VaR 95% (journalier) |  $      0.27 |
| CVaR 95% |  $      0.26 |
| Kelly optimal | 12.83 |
| Skew | 1.21 |
| Kurtosis | -0.44 |

## Equity curve

```
▁▁▇▇▇█
Start:  $  1,412.26 → End:  $  2,049.50
```

## PnL journalier

- Moyenne:  $    174.92
- Median:  $      9.10
- Meilleur jour:  $    618.47
- Pire jour:  $      0.26
- % jours positifs: 100.0%

## Monte Carlo (horizon 365j, 1000 simulations)

| Percentile | PnL annuel projeté |
|---|---|
| p05 |  $ 56,292.49 |
| p25 |  $ 60,478.28 |
| p50 |  $ 63,672.94 |
| p75 |  $ 66,975.24 |
| p95 |  $ 71,369.56 |
| Espérance |  $ 63,811.47 |
| P(loss) | 0.0% |

## Attribution par pocket

| pocket                    |    n |   total_pnl |   avg_pnl |   wr_pct |
|:--------------------------|-----:|------------:|----------:|---------:|
| COLDMATH_NO_EXTREME_TIGHT | 1154 |     744.219 |     0.645 |   99.827 |
| PROB_NO_SAFE              |   47 |     181.393 |     3.859 |   65.957 |
| COLDMATH_NO_LONG_TTR      |  155 |      74.223 |     0.479 |   87.097 |
| COLDMATH_NO_EXTREME_WIDE  |   85 |      27.217 |     0.32  |   98.824 |
| EXACT_BIN_YES_CERT        |   18 |      19.386 |     1.077 |  100     |
| COLDMATH_YES_CERT         |    6 |       7.238 |     1.206 |  100     |
| SPEEDA_YES_CONFIRMED      |    1 |       5.73  |     5.73  |  100     |
| COLDMATH_NO_MID           |   74 |      -9.906 |    -0.134 |   93.243 |

## Attribution par ville (top 10)

| city      |   n |   total_pnl |   avg_pnl |   wr_pct |
|:----------|----:|------------:|----------:|---------:|
| singapore |  46 |     118.086 |     2.567 |   97.826 |
| seattle   |  52 |      79.677 |     1.532 |   98.077 |
| miami     |  44 |      75.845 |     1.724 |   97.727 |
| london    |  45 |      64.337 |     1.43  |   95.556 |
| milan     |  26 |      63.573 |     2.445 |   96.154 |
| warsaw    |  40 |      57.378 |     1.434 |  100     |
| munich    |  39 |      56.834 |     1.457 |   94.872 |
| wuhan     |  36 |      56.177 |     1.56  |  100     |
| madrid    |  36 |      55.119 |     1.531 |   97.222 |
| jakarta   |  22 |      51.683 |     2.349 |  100     |

## Attribution par signal

| signal_type   |    n |   total_pnl |   avg_pnl |   wr_pct |
|:--------------|-----:|------------:|----------:|---------:|
| COLDMATH_NO   | 1468 |     835.752 |     0.569 |   98.093 |
| PROB_NO       |   47 |     181.393 |     3.859 |   65.957 |
| EXACT_BIN_YES |   18 |      19.386 |     1.077 |  100     |
| COLDMATH_YES  |    6 |       7.238 |     1.206 |  100     |
| SPEEDA_YES    |    1 |       5.73  |     5.73  |  100     |

## Walk-forward (OOS)

|    | test_start   | test_end   |   n_trades |   pnl |   wr_pct |   sharpe |   max_dd |
|---:|:-------------|:-----------|-----------:|------:|---------:|---------:|---------:|
|  0 | 2026-04-10   | 2026-04-11 |          1 |  0.3  |      100 |        0 |        0 |
|  1 | 2026-04-11   | 2026-04-12 |          0 |  0    |        0 |        0 |        0 |
|  2 | 2026-04-13   | 2026-04-14 |          6 |  4.05 |      100 |        0 |        0 |
|  3 | 2026-04-14   | 2026-04-15 |          9 | 14.16 |      100 |        0 |        0 |

### Pooled OOS metrics
- N trades: 16
- P&L total:  $     18.51
- Sharpe: 16.43
- Max DD: 0.0%
