# Give an Excel custom skill a Python script

**[Download the exercise (ZIP)](https://github.com/stringfestdata/excel-skills-python-demo/archive/refs/heads/main.zip)**

Use a prepared Copilot skill to check six fictional expenses, change one dollar,
and run the same Python script again. You do not need to write Python.

## What's included

- **python-skills-practice.xlsx** — the starting workbook.
- **expense-check-python/** — the complete skill folder, containing `SKILL.md`
  and `scripts/check_expenses.py`.
- **practice-prompts.txt** — the prompts to copy into Copilot.
- **README.md** — these instructions.

## Try it

1. Extract the ZIP and open `python-skills-practice.xlsx`.
2. In Copilot settings, open **Manage skills** (or **Manage plugins & skills**),
   then **Custom skills**. Open the OneDrive skills folder; create it if needed.
3. Copy the entire `expense-check-python` folder into it. Inside the copied
   folder, `SKILL.md` should sit beside `scripts`. Let OneDrive sync, refresh
   the skill list, and enable the skill if needed.
4. Send **PASS 1** from `practice-prompts.txt` in the practice workbook.
5. Check the new **ExpenseCheck** sheet: Food ($600 over budget) and Repairs
   ($900 over) should say **Yes**. Supplies is exactly $500 over, so it is **No**.
6. Change **Data!C7** from `1500` to `1501`, then send **PASS 2**.
   Supplies should now say **Yes**, bringing the count from two to three.

**ExpenseCheck is a snapshot.** Rerun the skill after changing Data.

You need Copilot workbook editing, Custom skills, and a Python execution tool
available in that Copilot session. The skill stops if Python cannot run.
This workflow does not require a GitHub account or a local Python installation,
and it is separate from Python in Excel's `=PY()` worksheet feature.

## Optional: try a missing amount

Clear **Data!B10** (Repairs budget), then send **OPTIONAL CHECK** from the prompts
file. The script should stop and identify the missing budget. Any existing
ExpenseCheck sheet is now an older snapshot. Restore B10 to `1000` and C7 to
`1500`, then send PASS 1 to return to the starting example.

The rule is **Actual minus Budget > 500**. All data and the threshold are
fictional teaching examples.

For the earlier JSON lesson, see the
[separate article and exercise](https://stringfestanalytics.com/json-copilot-excel-skills-output-structure/).
