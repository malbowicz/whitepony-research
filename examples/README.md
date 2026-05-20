# Examples

These examples use synthetic data only. They demonstrate research ideas, not the private White Pony production system.

Run them with standard Python3:

```bash
python3 examples/toy-backtest-example.py
python3 examples/portfolio-weighting-example.py
python3 examples/cost-lag-stress-example.py
```

The examples avoid external dependencies so they can be inspected pretty easily.

## Files 

- `toy-backtest-example.py`: simple weekly return simulation with basic metrics.
- `portfolio-weighting-example.py`: capped inverse-volatility weighting on synthetic sleeve data.
- `cost-lag-stress-example.py`: very simplified cost and lag stress on synthetic signal returns.

These are educational sketches. They are not trading systems and do not contain private formulas. But they are close to the broad ideas used. 
