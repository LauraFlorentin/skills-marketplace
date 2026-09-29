# Real Estate Calculation Tests

These tests use synthetic inputs, not market evidence or investment recommendations.
They protect calculation mechanics such as NOI, debt service, DSCR, cash-on-cash
return, exit proceeds, and basic input validation.

Run them from the repository root:

```bash
python3 -m unittest discover -s real-estate-investment/tests -p 'test_*.py'
```

Update a fixture only when the documented model contract changes. Add a focused
regression case for every calculation defect before changing the formula.
