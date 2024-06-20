# [136_rotate_image] in-place clockwise matrix rotation | invariant: O(n^2) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def rotate(matrix: list[list[int]]) -> None:
    """Rotate an n x n matrix 90 degrees clockwise in place."""
    size = len(matrix)
    if size < 2:
        return

    for row in range(size):
        # invariant: swap only upper triangle so each pair flips once
        for col in range(row + 1, size):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row_values in matrix:
        row_values.reverse()


# --- tests ----------------------------------------------------------------

class TestRotateImage(unittest.TestCase):
    def test_examples(self) -> None:
        grid_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate(grid_3x3)
        self.assertEqual(grid_3x3, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

        grid_4x4 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        rotate(grid_4x4)
        self.assertEqual(
            grid_4x4,
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        )

    def test_edges(self) -> None:
        grid_1x1 = [[7]]
        rotate(grid_1x1)
        self.assertEqual(grid_1x1, [[7]])

        grid_empty: list[list[int]] = []
        rotate(grid_empty)
        self.assertEqual(grid_empty, [])


if __name__ == "__main__":
    unittest.main()
