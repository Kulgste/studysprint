"""Tests for the StudySprint average quiz score report."""

import unittest

from features import reports


class TestAverageScore(unittest.TestCase):
    def test_empty_history_returns_zero(self):
        self.assertEqual(reports.average_score({"history": []}), 0.0)

    def test_single_score_returns_itself(self):
        self.assertEqual(reports.average_score({"history": [8]}), 8.0)

    def test_multiple_scores_return_average(self):
        self.assertEqual(reports.average_score({"history": [5, 6, 4]}), 5.0)

    def test_average_rounds_to_one_decimal(self):
        self.assertEqual(reports.average_score({"history": [1, 2, 2]}), 1.7)


if __name__ == "__main__":
    unittest.main()
