# [085_pacific_atlantic_water_flow] dual-ocean reverse BFS | invariant: O(m*n) uphill reachability

from __future__ import annotations

from collections import deque
from itertools import product
import unittest


# --- tables ---------------------------------------------------------------

ORTHO_DIRS: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


# --- public api -----------------------------------------------------------

def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    """Return grid coordinates whose rainwater can reach both Pacific and Atlantic oceans."""
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific_seeds = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
    atlantic_seeds = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

    # perf: reverse uphill BFS from ocean borders avoids per-cell search
    pacific = _reachable_uphill(heights, pacific_seeds)
    atlantic = _reachable_uphill(heights, atlantic_seeds)

    return [
        [r_idx, c_idx]
        for r_idx, c_idx in product(range(rows), range(cols))
        if (r_idx, c_idx) in pacific and (r_idx, c_idx) in atlantic
    ]


# --- helpers --------------------------------------------------------------

def _reachable_uphill(
    heights: list[list[int]],
    seeds: list[tuple[int, int]],
) -> set[tuple[int, int]]:
    visited: set[tuple[int, int]] = set(seeds)
    queue: deque[tuple[int, int]] = deque(visited)

    while queue:
        row, col = queue.popleft()
        _enqueue_uphill(heights, row, col, visited, queue)

    return visited


def _enqueue_uphill(
    heights: list[list[int]],
    row: int,
    col: int,
    visited: set[tuple[int, int]],
    queue: deque[tuple[int, int]],
) -> None:
    rows, cols = len(heights), len(heights[0])
    curr_height = heights[row][col]

    for dr, dc in ORTHO_DIRS:
        nr, nc = row + dr, col + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            continue
        if (nr, nc) in visited or heights[nr][nc] < curr_height:
            continue
        visited.add((nr, nc))
        queue.append((nr, nc))


# --- tests ----------------------------------------------------------------

class TestPacificAtlantic(unittest.TestCase):
    def test_examples(self) -> None:
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertEqual(pacific_atlantic(heights), expected)

    def test_edges(self) -> None:
        self.assertEqual(pacific_atlantic([[1]]), [[0, 0]])
        self.assertEqual(pacific_atlantic([]), [])


if __name__ == "__main__":
    unittest.main()
