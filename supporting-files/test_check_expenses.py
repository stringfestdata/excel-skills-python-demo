"""Developer checks; readers do not need to run these to follow the post."""
from copy import deepcopy
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("expense_script", ROOT / "expense-check-python/scripts/check_expenses.py")
script = module_from_spec(spec)
spec.loader.exec_module(script)


class ExpenseChecks(unittest.TestCase):
    def row(self, budget=1000, actual=1500):
        return {"Expense": "Supplies", "Budget": budget, "Actual": actual}

    def test_strict_boundary(self):
        for actual, flag in [(1499.99, False), (1500, False), (1500.01, True), (1501, True)]:
            with self.subTest(actual=actual):
                self.assertEqual(script.check_expenses([self.row(actual=actual)])["results"][0]["NeedsReview"], flag)

    def test_real_zero_and_underspend(self):
        self.assertFalse(script.check_expenses([self.row(0, 0)])["results"][0]["NeedsReview"])
        self.assertEqual(script.check_expenses([self.row(1500, 1200)])["results"][0]["OverBudget"], -300)

    def test_invalid_numbers(self):
        for value in [None, "", " ", "unknown", True, "NaN", "Infinity", -1, "1.001"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                script.check_expenses([self.row(budget=value)])

    def test_duplicate_empty_and_extra_fields(self):
        with self.assertRaises(ValueError):
            script.check_expenses([self.row(), self.row()])
        with self.assertRaises(ValueError):
            script.check_expenses([])
        with self.assertRaises(ValueError):
            script.check_expenses([{**self.row(), "Extra": 1}])

    def test_input_unchanged(self):
        rows = [self.row()]
        original = deepcopy(rows)
        script.check_expenses(rows)
        self.assertEqual(rows, original)


if __name__ == "__main__":
    unittest.main()
