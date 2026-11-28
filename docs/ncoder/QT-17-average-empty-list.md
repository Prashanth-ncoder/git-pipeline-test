# QT-17: average([]) raises ZeroDivisionError

Checked against `calc.py` on `origin/qa/nonsf-review-1`.

- `average([])` computes `sum([]) / len([])`, which is `0 / 0`.
- Result: `ZeroDivisionError: division by zero`. The function does not return a value and does not handle the empty case.
- The current code and test file contain no test for an empty list.
- The behaviour is recorded as it is. QT-14 proposes returning `0` instead; this analysis does not implement that change.
