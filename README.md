# White Pony Research

White Pony is my applied mathematics and quantitative finance research portfolio. The project studies how systematic strategies are designed, tested, combined, and monitored after the initial backtest.

This is the public version of the work. It is intentionally incomplete: the private production repo contains code, formulas, configs, broker tooling, targets, and logs that are not appropriate to publish.

## What This Repo Is

This repo is meant to be readable by admissions readers, professors, research mentors, and quant internship recruiters. It contains:

- short summaries of current paper ideas;
- plain-English methodology notes;
- synthetic examples that illustrate backtest concepts;
- placeholders for reviewed charts and PDFs;
- a template for delayed, aggregate public logging.

It is not a full trading-system release.

## Current Research Threads

The public summaries are organized around three working paper directions:

- Portfolio construction: combining signal sleeves while checking concentration, correlation, turnover, and drawdown.
- Alpha mutation: treating signal variants as a way to find failure modes, not just better-looking backtests.
- Backtest reproducibility: showing how data refreshes, retraining, cached artifacts, and evaluation windows can change reported results.

These are drafts. The final papers and chart sets still need manual review before publication.

## Repository Map

- `paper-summaries/`: short public summaries of the three paper directions.
- `docs/`: methodology, risk notes, limitations, glossary, and public logging policy.
- `examples/`: small Python examples using synthetic data only.
- `papers/`: TODO folder for reviewed public PDFs.
- `charts/`: TODO folder for reviewed public charts.
- `live-log/`: TODO templates for delayed aggregate observations.
- `architecture/`: high-level system diagram notes without private implementation details.

## Educational Examples

The examples use synthetic data and standard Python. They are included to make the research ideas inspectable without exposing private logic.

For example:

```bash
python3 examples/toy-backtest-example.py
```

## Publication Boundary

The public repo does not include private formulas, model parameters, ranking rules, broker integrations, account information, current holdings, target files, order logs, or production execution code.

When results are added, they should be presented as historical research or delayed monitoring, not as proof of future performance.

## Status

This is an early public draft. The most useful next edits are:

- add reviewed PDFs to `papers/`;
- add reviewed charts with captions to `charts/`;
- replace TODOs with actual paper-specific notes;
- add a short personal note on what I learned from each research thread.

## Disclaimer

Research and education only. Not financial advice or a recommendation to trade. Historical, simulated, paper, or delayed results do not guarantee future performance.
