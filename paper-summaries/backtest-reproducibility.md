# Backtest Reproducibility

## Question

When a validated quantitative backtest changes after data refreshes or retraining, how much of the change comes from the data, the model update, the evaluation window, or artifact drift?

## Current Draft

This is probably the cleanest paper direction right now. It uses a regime routed equity system as a case study in reproducibility.

The point is not that one version of a model is better. The point is that backtest numbers depend on artifacts, data vintages, retraining choices, cached decisions, and evaluation windows.

## Main Ideas

- a frozen artifact can still reproduce its original result;
- refreshed data can change realized performance even when decisions are held fixed;
- retraining can add a separate source of drift;
- evaluation-window changes can make comparisons misleading;
- model maintenance choices behave like hidden hyperparameters.

## TODO

Add reviewed charts to a future `charts/backtest-reproducibility/` folder.

Useful candidates:

- artifact lineage diagram;
- drift decomposition chart;
- evaluation-window timeline;
- retraining event timeline;
- bootstrap confidence interval chart;
- current-versus-frozen drawdown and rolling Sharpe charts, if sanitized and clearly labeled.

## Claims I Can Make 
## Sorta
- Reproducible quant research needs frozen artifacts, decision-series records, data-vintage notes, and hash manifests.
- Data refresh and retraining should be separated when explaining performance drift.
- A backtest can pass timing checks and still be hard to reproduce.

## Claims To Avoid

- live performance will match any backtest;
- a particular retraining policy is universally optimal;
- a high historical Sharpe proves future edge;
- private weekly parquet files, current targets, or full model summaries.
