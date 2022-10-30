# [029_search_a_2d_matrix] flattened 2D sorted matrix search | invariant: O(log(m * n)) time

import unittest


# --- public api -----------------------------------------------------------

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Return True if target exists in a row-wise and cross-row sorted matrix."""
    if not matrix or not matrix[0]:
        return False

    col_count = len(matrix[0])
    lo = 0
    hi = len(matrix) * col_count - 1

    # perf: map 1D cursor to (row, col) for a single O(log(m * n)) search
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        cell = matrix[mid // col_count][mid % col_count]
        if cell == target:
            return True
        if cell < target:
            lo = mid + 1
            continue
        hi = mid - 1

    return False


# --- tests ----------------------------------------------------------------

class TestSearchMatrix(unittest.TestCase):
    def test_examples(self) -> None:
        grid = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(search_matrix(grid, 3))
        self.assertFalse(search_matrix(grid, 13))

    def test_edges(self) -> None:
        self.assertFalse(search_matrix([], 1))
        self.assertFalse(search_matrix([[]], 1))
        self.assertTrue(search_matrix([[1]], 1))
        self.assertFalse(search_matrix([[1]], 2))


if __name__ == "__main__":
    unittest.main()
