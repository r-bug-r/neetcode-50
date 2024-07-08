# [137_spiral_matrix] boundary-shrinking spiral traversal | invariant: O(m*n) time, O(1) extra

import unittest


# --- public api -----------------------------------------------------------

def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return all elements of matrix in clockwise spiral order."""
    if not matrix or not matrix[0]:
        return []

    traversal: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            traversal.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            traversal.append(matrix[row][right])
        right -= 1

        # edge: single-row or single-column remnants have already been read above
        if top > bottom or left > right:
            break

        for col in range(right, left - 1, -1):
            traversal.append(matrix[bottom][col])
        bottom -= 1

        for row in range(bottom, top - 1, -1):
            traversal.append(matrix[row][left])
        left += 1

    return traversal


# --- tests ----------------------------------------------------------------

class TestSpiralMatrix(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        )
        self.assertEqual(
            spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        )

    def test_edges(self) -> None:
        self.assertEqual(spiral_order([]), [])
        self.assertEqual(spiral_order([[1, 2, 3]]), [1, 2, 3])
        self.assertEqual(spiral_order([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(spiral_order([[42]]), [42])


if __name__ == "__main__":
    unittest.main()
