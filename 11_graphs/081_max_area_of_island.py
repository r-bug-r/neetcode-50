# [081_max_area_of_island] largest connected land area | invariant: O(m*n) BFS without mutation

from __future__ import annotations

from collections import deque
from itertools import product
import unittest


# --- tables ---------------------------------------------------------------

ORTHO_DIRS: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


# --- public api -----------------------------------------------------------

def max_area_of_island(grid: list[list[int]]) -> int:
    """Return the maximum area among orthogonally connected 1-cell islands."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()
    best_area = 0

    for r_idx, c_idx in product(range(rows), range(cols)):
        if grid[r_idx][c_idx] != 1 or (r_idx, c_idx) in visited:
            continue
        best_area = max(best_area, _measure_island(grid, r_idx, c_idx, visited))

    return best_area


# --- helpers --------------------------------------------------------------

def _measure_island(
    grid: list[list[int]],
    start_r: int,
    start_c: int,
    visited: set[tuple[int, int]],
) -> int:
    queue: deque[tuple[int, int]] = deque([(start_r, start_c)])
    visited.add((start_r, start_c))
    area = 0

    while queue:
        row, col = queue.popleft()
        area += 1
        _enqueue_land_neighbors(grid, row, col, visited, queue)

    return area


def _enqueue_land_neighbors(
    grid: list[list[int]],
    row: int,
    col: int,
    visited: set[tuple[int, int]],
    queue: deque[tuple[int, int]],
) -> None:
    rows, cols = len(grid), len(grid[0])
    for dr, dc in ORTHO_DIRS:
        nr, nc = row + dr, col + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            continue
        if grid[nr][nc] != 1 or (nr, nc) in visited:
            continue
        visited.add((nr, nc))
        queue.append((nr, nc))


# --- tests ----------------------------------------------------------------

class TestMaxAreaOfIsland(unittest.TestCase):
    def test_examples(self) -> None:
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        self.assertEqual(max_area_of_island(grid), 6)

    def test_edges(self) -> None:
        self.assertEqual(max_area_of_island([[0, 0, 0, 0, 0, 0, 0, 0]]), 0)
        self.assertEqual(max_area_of_island([]), 0)


if __name__ == "__main__":
    unittest.main()
