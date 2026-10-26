"""Check expense overruns using Python's standard library.

Usage: python check_expenses.py current-expenses.csv --threshold 500
Reads a CSV and prints JSON. Does not edit files or Excel, or use the network.
"""
import argparse
import csv
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path

VERSION = "1.0"
HEADERS = ["Expense", "Budget", "Actual"]


def money(value, label):
    """Require an amount, preserving the difference between blank and zero."""
    if value is None or isinstance(value, bool) or str(value).strip() == "":
        raise ValueError(f"{label} is missing or is not a number")
    try:
        amount = Decimal(str(value).strip())
    except InvalidOperation as exc:
        raise ValueError(f"{label} must be numeric") from exc
    if not amount.is_finite() or amount < 0:
        raise ValueError(f"{label} must be a finite, nonnegative amount")
    if amount != amount.quantize(Decimal("0.01")):
        raise ValueError(f"{label} must have at most two decimal places")
    return amount


def check_expenses(rows, threshold=500):
    threshold = money(threshold, "Threshold")
    if not rows:
        raise ValueError("No expense rows were supplied")
    results, seen = [], set()
    for row_number, row in enumerate(rows, 1):
        if set(row) != set(HEADERS):
            raise ValueError(f"Data row {row_number}: use only Expense, Budget, Actual")
        expense = str(row["Expense"] or "").strip()
        if not expense:
            raise ValueError(f"Data row {row_number}: Expense is missing")
        if expense.casefold() in seen:
            raise ValueError(f"Duplicate expense: {expense}")
        if expense.casefold() in {"total", "grand total", "subtotal"}:
            raise ValueError("Supply detail rows only, without a totals row")
        seen.add(expense.casefold())
        budget = money(row["Budget"], f"{expense}: Budget")
        actual = money(row["Actual"], f"{expense}: Actual")
        over_budget = actual - budget
        needs_review = over_budget > threshold
        results.append({
            "Expense": expense, "Budget": budget, "Actual": actual,
            "OverBudget": over_budget, "NeedsReview": needs_review,
        })
    return {
        "script_version": VERSION,
        "rows_checked": len(results),
        "threshold": threshold,
        "flagged_count": sum(row["NeedsReview"] for row in results),
        "results": results,
    }


def json_number(value):
    if isinstance(value, Decimal):
        return int(value) if value == value.to_integral_value() else float(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--threshold", default="500")
    args = parser.parse_args()
    try:
        with args.csv_path.open(newline="", encoding="utf-8-sig") as source:
            reader = csv.DictReader(source)
            if reader.fieldnames != HEADERS:
                raise ValueError("CSV headers must be Expense,Budget,Actual in that order")
            result = check_expenses(list(reader), args.threshold)
        print(json.dumps(result, default=json_number, indent=2, allow_nan=False))
    except (ValueError, OSError, InvalidOperation) as exc:
        parser.exit(2, f"Expense check stopped: {exc}\n")


if __name__ == "__main__":
    main()
