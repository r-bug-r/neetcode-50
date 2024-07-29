# [138_set_matrix_zeroes] in-place first-row/col zero markers | invariant: O(m*n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def set_zeroes(matrix: list[list[int]]) -> None:
    """Zero out every row and column containing a 0 in place."""
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    # invariant: capture header-line zeros before using row 0 / col 0 as scratch markers
    first_row_zero = any(matrix[0][col] == 0 for col in range(cols))
    first_col_zero = any(matrix[row][0] == 0 for row in range(rows))

    for row in range(1, rows):
        _record_row_zeros(matrix, row, cols)

    for row in range(1, rows):
        _apply_row_zeros(matrix, row, cols)

    if first_row_zero:
        for col in range(cols):
            matrix[0][col] = 0

    if first_col_zero:
        for row in range(rows):
            matrix[row][0] = 0


# --- helpers --------------------------------------------------------------

def _record_row_zeros(matrix: list[list[int]], row: int, cols: int) -> None:
    for col in range(1, cols):
        if matrix[row][col] == 0:
            matrix[row][0] = 0
            matrix[0][col] = 0


def _apply_row_zeros(matrix: list[list[int]], row: int, cols: int) -> None:
    for col in range(1, cols):
        if matrix[row][0] == 0 or matrix[0][col] == 0:
            matrix[row][col] = 0


# --- tests ----------------------------------------------------------------

class TestSetMatrixZeroes(unittest.TestCase):
    def test_examples(self) -> None:
        grid_a = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        set_zeroes(grid_a)
        self.assertEqual(grid_a, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

        grid_b = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        set_zeroes(grid_b)
        self.assertEqual(grid_b, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    def test_edges(self) -> None:
        grid_row = [[1, 0, 3]]
        set_zeroes(grid_row)
        self.assertEqual(grid_row, [[0, 0, 0]])

        grid_col = [[1], [0], [3]]
        set_zeroes(grid_col)
        self.assertEqual(grid_col, [[0], [0], [0]])

        grid_none = [[1, 2], [3, 4]]
        set_zeroes(grid_none)
        self.assertEqual(grid_none, [[1, 2], [3, 4]])


if __name__ == "__main__":
    unittest.main()
