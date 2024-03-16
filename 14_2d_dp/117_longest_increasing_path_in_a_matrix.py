# [117_longest_increasing_path_in_a_matrix] Kahn DAG layer-peeling DP | invariant: O(R * C) time, no recursion limit

import unittest

DIRECTIONS: tuple[tuple[int, int], ...] = ((-1, 0), (1, 0), (0, -1), (0, 1))


# --- public api -----------------------------------------------------------

def longest_increasing_path(matrix: list[list[int]]) -> int:
    """Return length of the longest strictly increasing 4-directional path in matrix."""
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    indegree = _build_indegree_grid(matrix, rows, cols)
    layer = [(r, c) for r in range(rows) for c in range(cols) if indegree[r][c] == 0]
    path_len = 0

    # perf: iterative DAG peeling finds longest path in O(R * C) without stack overflow
    while layer:
        path_len += 1
        layer = _peel_layer(matrix, indegree, layer, rows, cols)

    return path_len


# --- helpers --------------------------------------------------------------

def _build_indegree_grid(matrix: list[list[int]], rows: int, cols: int) -> list[list[int]]:
    indegree = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            indegree[row][col] = _smaller_neighbor_count(matrix, row, col, rows, cols)
    return indegree


def _smaller_neighbor_count(
    matrix: list[list[int]],
    row: int,
    col: int,
    rows: int,
    cols: int,
) -> int:
    value = matrix[row][col]
    count = 0
    for dr, dc in DIRECTIONS:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < value:
            count += 1
    return count


def _peel_layer(
    matrix: list[list[int]],
    indegree: list[list[int]],
    layer: list[tuple[int, int]],
    rows: int,
    cols: int,
) -> list[tuple[int, int]]:
    next_layer: list[tuple[int, int]] = []
    for row, col in layer:
        _advance_uphill(matrix, indegree, row, col, rows, cols, next_layer)
    return next_layer


def _advance_uphill(
    matrix: list[list[int]],
    indegree: list[list[int]],
    row: int,
    col: int,
    rows: int,
    cols: int,
    next_layer: list[tuple[int, int]],
) -> None:
    value = matrix[row][col]
    for dr, dc in DIRECTIONS:
        nr, nc = row + dr, col + dc
        if not (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > value):
            continue
        indegree[nr][nc] -= 1
        if indegree[nr][nc] == 0:
            next_layer.append((nr, nc))


# --- tests ----------------------------------------------------------------

class TestLongestIncreasingPath(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(longest_increasing_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]), 4)
        self.assertEqual(longest_increasing_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]]), 4)
        self.assertEqual(longest_increasing_path([[1]]), 1)

    def test_edges(self) -> None:
        self.assertEqual(longest_increasing_path([]), 0)
        self.assertEqual(longest_increasing_path([[]]), 0)
        self.assertEqual(longest_increasing_path([[7, 7, 7], [7, 7, 7]]), 1)
        self.assertEqual(longest_increasing_path([[1, 2, 3], [6, 5, 4], [7, 8, 9]]), 9)


if __name__ == "__main__":
    unittest.main()
