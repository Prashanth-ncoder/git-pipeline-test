# QT-15: tests in test_calc.py

Source: `test_calc.py` on `origin/qa/nonsf-review-1`.

| Test | Assertion | Result |
|------|-----------|--------|
| `test_average` | `average([2, 4]) == 3` | passes |
| `test_discount` | `discount(100, 10) == 90` | passes |

Two tests in total. Neither covers an empty list for `average()` or a non-positive or over-100 percent for `discount()`.

No files are changed by this analysis: the repository change is limited to the `docs/ncoder/` notes.
