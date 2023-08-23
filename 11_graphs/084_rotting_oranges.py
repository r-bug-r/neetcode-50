# [084_rotting_oranges] multi-source BFS decay timer | invariant: O(m*n) frontier waves

from __future__ import annotations

from collections import deque
from itertools import product
import unittest


# --- tables ---------------------------------------------------------------

ORTHO_DIRS: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


# --- public api -----------------------------------------------------------

def oranges_rotting(grid: list[list[int]]) -> int:
    """Return minimum minutes until no fresh orange remains, or -1 if unreachable."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    work = [row.copy() for row in grid]
    queue, fresh_count = _seed_frontier(work, rows, cols)

    minutes = 0
    while queue and fresh_count > 0:
        minutes += 1
        fresh_count -= _advance_minute(work, queue)

    return minutes if fresh_count == 0 else -1


# --- helpers --------------------------------------------------------------

def _seed_frontier(
    grid: list[list[int]],
    rows: int,
    cols: int,
) -> tuple[deque[tuple[int, int]], int]:
    queue: deque[tuple[int, int]] = deque()
    fresh_count = 0

    for r_idx, c_idx in product(range(rows), range(cols)):
        state = grid[r_idx][c_idx]
        if state == 2:
            queue.append((r_idx, c_idx))
        elif state == 1:
            fresh_count += 1

    return queue, fresh_count


def _advance_minute(grid: list[list[int]], queue: deque[tuple[int, int]]) -> int:
    newly_rotted = 0
    for _ in range(len(queue)):
        row, col = queue.popleft()
        newly_rotted += _rot_adjacent(grid, row, col, queue)
    return newly_rotted


def _rot_adjacent(
    grid: list[list[int]],
    row: int,
    col: int,
    queue: deque[tuple[int, int]],
) -> int:
    rows, cols = len(grid), len(grid[0])
    rotted = 0

    for dr, dc in ORTHO_DIRS:
        nr, nc = row + dr, col + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            continue
        if grid[nr][nc] != 1:
            continue
        grid[nr][nc] = 2
        queue.append((nr, nc))
        rotted += 1

    return rotted


# --- tests ----------------------------------------------------------------

class TestRottingOranges(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
        self.assertEqual(oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1)

    def test_edges(self) -> None:
        self.assertEqual(oranges_rotting([[0, 2]]), 0)
        self.assertEqual(oranges_rotting([]), 0)


if __name__ == "__main__":
    unittest.main()
