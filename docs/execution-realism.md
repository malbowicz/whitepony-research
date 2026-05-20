# Execution Realism

Backtest performance is not the same as implementable performance.

Public materials should separate:

- research backtests;
- simulated or paper execution;
- delayed aggregate logs;
- operational trading systems.

## Frictions To Name

Public writeups can discuss:

- transaction costs;
- spread and slippage;
- turnover;
- rebalance delay;
- stale prices;
- partial fills;
- benchmark and timing mismatch;
- position-level versus allocation-level costs.

## Working Rule

Do not claim that a backtest is directly tradable. If execution assumptions matter, show them with simple stress charts:

- performance under extra lag;
- performance under higher cost assumptions;
- turnover versus return or Sharpe;
- drawdown under stress.

TODO(public-review): Add reviewed cost and lag charts after checking labels, captions, and metadata.
