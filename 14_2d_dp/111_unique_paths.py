# [111_unique_paths] rolling grid DP | invariant: O(m * n) time, O(min(m, n)) space

import unittest


# --- public api -----------------------------------------------------------

def unique_paths(m: int, n: int) -> int:
    """Return distinct top-left to bottom-right grid paths moving only right or down."""
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

    # perf: fold over the smaller dimension to bound rolling row memory
    rows, cols = (m, n) if m >= n else (n, m)
    row_ways = [1] * cols

    for _ in range(1, rows):
        _accumulate_row(row_ways, cols)

    return row_ways[-1]


# --- helpers --------------------------------------------------------------

def _accumulate_row(row_ways: list[int], cols: int) -> None:
    for col in range(1, cols):
        row_ways[col] += row_ways[col - 1]


# --- tests ----------------------------------------------------------------

class TestUniquePaths(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(unique_paths(3, 7), 28)
        self.assertEqual(unique_paths(3, 2), 3)

    def test_edges(self) -> None:
        self.assertEqual(unique_paths(0, 5), 0)
        self.assertEqual(unique_paths(1, 1), 1)
        self.assertEqual(unique_paths(1, 8), 1)
        self.assertEqual(unique_paths(7, 3), 28)
        self.assertEqual(unique_paths(3, 3), 6)


if __name__ == "__main__":
    unittest.main()
