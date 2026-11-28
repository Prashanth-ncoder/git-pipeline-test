# QT-16: average() and discount() in calc.py

Source: `calc.py` as it exists on `origin/qa/nonsf-review-1`. The story branch (`story/QT-13-...`) does not contain `calc.py`, so these results were checked against that copy.

## average(values)

- Returns `sum(values) / len(values)`: the arithmetic mean of a list of numbers.
- `average([2, 4])` returns `3.0` (Python 3 true division, so the result is a float).
- `average([])` raises `ZeroDivisionError` (see QT-17).
- `average(['a'])` raises `TypeError` because `sum` cannot add a string to an int. Non-numeric items are out of scope for QT-13.

## discount(price, percent)

- Returns `price - price * percent / 100`: the price after a percent discount.
- `discount(100, 10)` returns `90.0`.
- No range check is applied. `discount(100, 150)` returns `-50.0` and `discount(100, -10)` returns `110.0`. Whether these inputs are valid is an open question (see the design document).

## Verification

Both assertions in `test_calc.py` (`average([2, 4]) == 3`, `discount(100, 10) == 90`) were run against this copy and pass.
