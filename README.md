# Give an Excel custom skill a Python script

**[Download the complete exercise (ZIP)](https://github.com/stringfestdata/excel-skills-python-demo/archive/refs/heads/main.zip)**

Check six fictional restaurant expenses with one saved rule: flag spending
**more than $500 over budget**. Run the prepared skill, change one workbook
value, and run the same script again. No Python writing is required.

This standalone repository contains the resources for George Mount's Python
script and Excel skill walkthrough. For the earlier JSON exercise, see
[the separate JSON tutorial repository](https://github.com/stringfestdata/excel-skills-json-demo)
and [the published article](https://stringfestanalytics.com/json-copilot-excel-skills-output-structure/).

## Start here

1. Extract the ZIP. Open `python-skills-practice.xlsx`.
2. Open Copilot settings, then **Manage skills** (or **Manage plugins & skills**),
   then **Custom skills**. Open the skills folder in OneDrive; create it if needed.
3. Copy the entire `expense-check-python` folder into that OneDrive folder.
   Let it sync, then refresh the skill list. Enable it if needed.
4. Send **PASS 1** from `practice-prompts.txt` in the practice workbook.
5. Look for six rows and two **Yes** labels: Food ($600 over) and Repairs ($900 over).
   Supplies is exactly $500 over, so it should say **No**.
6. Change **Data!C7** from `1500` to `1501`. Send **PASS 2**.
   Supplies should now say **Yes**, bringing the count to three.

You need an Excel account with Copilot workbook editing and Custom skills,
plus a Python execution tool available to that Copilot session. A `scripts`
folder cannot supply a missing runtime. If execution is unavailable, the
skill stops and says so. The demonstrated path does not require Git,
a GitHub account, or installing Python on your computer.

## What the files do

| File | Purpose |
|---|---|
| `python-skills-practice.xlsx` | Your starting workbook; only the Data sheet. |
| `expense-check-python/SKILL.md` | Tells Copilot to read current data, execute the script and present the result. |
| `expense-check-python/scripts/check_expenses.py` | The saved validation and calculation procedure. |
| `practice-prompts.txt` | Copy-ready requests for the two passes and an optional missing-value check. |
| `START-HERE.txt` | Plain-text setup and checks. |
| `live-example/` | Completed workbooks, real Excel captures and notes from the live test. |
| `supporting-files/` | Optional sample CSV and developer tests. Not needed for the Excel walkthrough. |

**ExpenseCheck is a snapshot.** Change Data, then rerun the skill to update it.
This exercise does not insert `=PY()` formulas or install a VBA macro or Office
Script. The saved Python code calculates results; Copilot's workbook tools write
the worksheet.

## Optional: see validation stop a bad input

Clear **Data!B10**, the Repairs budget, and send the optional prompt.
The script should reject the missing amount. It must not quietly treat blank as
zero or refresh ExpenseCheck with made-up input. The old sheet is now stale.
Restore B10 to `1000` and C7 to `1500`, then send PASS 1 again.

## For people who want to inspect the code

The heart of the rule is:

```python
over_budget = actual - budget
needs_review = over_budget > threshold
```

The surrounding code checks the required headers, nonblank unique expense names,
and finite nonnegative amounts with at most two decimal places. It uses Python's
standard library, prints JSON, and does not edit files, call APIs or use the network.

If you independently have Python installed, you can run these commands from this
extracted folder. They are optional developer checks, not the reader setup:

```text
python expense-check-python/scripts/check_expenses.py supporting-files/sample-expenses.csv --threshold 500
python supporting-files/test_check_expenses.py
```

A maintained script gives the agent a procedure to reuse. It does not guarantee
the right data was supplied, that a host can execute it, or that every workbook
edit succeeds. Check the output. An existing skill may already bundle scripts;
custom code is useful when you need to own and test a particular rule.

All data and the $500 rule are fictional teaching examples.
