# [080_number_of_islands] grid connected components | invariant: O(m*n) BFS without input mutation

from __future__ import annotations

from collections import deque
from itertools import product
import unittest


# --- tables ---------------------------------------------------------------

ORTHO_DIRS: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


# --- public api -----------------------------------------------------------

def num_islands(grid: list[list[str]]) -> int:
    """Count orthogonally connected '1' islands in a 2D binary grid."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()
    islands = 0

    for r_idx, c_idx in product(range(rows), range(cols)):
        if grid[r_idx][c_idx] != "1" or (r_idx, c_idx) in visited:
            continue
        islands += 1
        _explore_island(grid, r_idx, c_idx, visited)

    return islands


# --- helpers --------------------------------------------------------------

def _explore_island(
    grid: list[list[str]],
    start_r: int,
    start_c: int,
    visited: set[tuple[int, int]],
) -> None:
    queue: deque[tuple[int, int]] = deque([(start_r, start_c)])
    visited.add((start_r, start_c))

    while queue:
        row, col = queue.popleft()
        _enqueue_land_neighbors(grid, row, col, visited, queue)


def _enqueue_land_neighbors(
    grid: list[list[str]],
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
        if grid[nr][nc] != "1" or (nr, nc) in visited:
            continue
        visited.add((nr, nc))
        queue.append((nr, nc))


# --- tests ----------------------------------------------------------------

class TestNumberOfIslands(unittest.TestCase):
    def test_examples(self) -> None:
        grid_one = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(num_islands(grid_one), 1)

        grid_three = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(num_islands(grid_three), 3)

    def test_edges(self) -> None:
        self.assertEqual(num_islands([]), 0)
        self.assertEqual(num_islands([["0", "0"]]), 0)


if __name__ == "__main__":
    unittest.main()
