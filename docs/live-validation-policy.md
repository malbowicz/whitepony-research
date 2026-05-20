# Public Logging Policy

White Pony may publish delayed aggregate observations. The log should be boring on purpose: no current positions, no orders, no broker details.

## Allowed After Review

- delayed weekly return;
- delayed benchmark comparison, if the benchmark is defined;
- delayed drawdown state;
- delayed turnover bucket;
- short notes that do not reveal current exposure.
- whatever other data that might be leaking secret sause.

## Not Allowed

Do not publish:

- current holdings;
- current target weights;
- current or recent orders;
- broker account equity;
- broker account IDs;
- API keys or credential material;
- exact execution timestamps tied to live orders;
- private routing or position-generation code;
- logs that expose operational details.
- Any of the secret sause alphas especially. 

## Delay

Default public delay: at least 30 calendar days after the observation week.

Use a longer delay if a note could reveal current exposure or target changes.

## Wording

Use plain wording: "delayed aggregate note" or "delayed monitoring record." Do not imply market outperformance or future returns.

## Templates

- `live-log/weekly-log.md`
- `live-log/delayed-results.csv`
- `live-log/delayed-results.json`

TODO(public-review): Fill these only after applying the delay rule.
