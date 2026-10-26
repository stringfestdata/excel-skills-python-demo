---
name: expense-check-python
description: Check an Excel expense table for spending more than $500 over budget by executing the bundled Python script, then present the results in a worksheet. Use for the Stringfest expense-check exercise or an equivalent single-period expense table.
---

# Check expense overruns with a saved Python script

Use the active workbook's table `tblExpenses` on `Data`. Its columns are
`Expense`, `Budget`, `Actual`. These are nonnegative expense amounts in USD
for one reporting period. Exclude the table's totals row, if present.
Read the current table values, including blanks; do not use saved sample data.

## Execute the saved procedure

1. Locate and read `scripts/check_expenses.py` from this installed skill.
2. Confirm that this session has an authorized Python execution tool. If the
   script is inaccessible or Python cannot run, stop and explain which is
   unavailable. Do not substitute JavaScript, Excel formulas, a hand calculation,
   or newly generated calculation code and call it a Python run.
3. Export all current detail rows to a temporary CSV with the exact three headers.
   Preserve blanks as blanks and numbers as numbers, without currency signs or
   thousands separators. Keep the source table unchanged. The CSV is an internal
   handoff; do not ask the reader to export it manually.
4. Execute the bundled script unchanged with that CSV and `--threshold 500`.
   Resolve its actual path in the execution environment. For example:
   `python <skill-path>/scripts/check_expenses.py <temporary-csv-path> --threshold 500`
   If resource files must first be materialized in the Python runtime, copy their
   exact contents unchanged. Do not rewrite the function or its comparison.
5. On a nonzero exit, report the exact validation error and do not create or
   update a report. An existing report remains an old snapshot; identify it as
   stale when reporting the failed run. Do not fill missing data with zero.

## Present and verify the returned result

Only after successful execution, create `ExpenseCheck` with all returned rows
in source order. If that sheet already belongs to this exercise, update it;
if it holds unrelated content, ask for another destination name.

Use title `Expense check` and columns `Expense`, `Budget`, `Actual`,
`Over budget`, `Review?`. Write the script's returned numeric values as numbers,
with dollar formatting. Display `NeedsReview` as `Yes` or `No`. Do not recreate
the calculations in Excel formulas: this lesson demonstrates a Python-produced
snapshot. Explain that the report needs another skill run after data changes.

Above the table show `Flag amounts more than $500 over budget` and the returned
row count and review count. Below it show `Python output snapshot. Rerun after
changing Data.` Use Arial 11, a red (#CF3338) title, charcoal (#1F2120) column
headers with white text, and warm off-white (#EEECE1) alternating rows. Use
readable column widths (at least 24 for Expense, 18 for each amount, and 14 for
Review?) and row heights of 24 points. Account for table filter buttons when
fitting headers. Hide worksheet gridlines. Use neutral table styling so the
requested fills are preserved. Do not add a chart or infer reasons for spending.

Read back the written range and compare every amount and Yes/No label to the
script output. In chat report the executed script name, actual execution tool,
version and row count, and any failure to write or verify the worksheet. Never
claim execution based solely on reading a script or knowing the expected answer.
