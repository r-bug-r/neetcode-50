# [083_walls_and_gates] multi-source gate distance fill | invariant: O(m*n) shortest-path BFS

from __future__ import annotations

from collections import deque
from itertools import product
import unittest


# --- tables ---------------------------------------------------------------

INF = 2147483647
ORTHO_DIRS: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


# --- public api -----------------------------------------------------------

def walls_and_gates(rooms: list[list[int]]) -> None:
    """Fill each empty room (INF) in-place with distance to its nearest gate (0)."""
    if not rooms or not rooms[0]:
        return

    rows, cols = len(rooms), len(rooms[0])
    # perf: multi-source BFS visits every reachable room exactly once in distance order
    queue: deque[tuple[int, int]] = deque(
        (r_idx, c_idx)
        for r_idx, c_idx in product(range(rows), range(cols))
        if rooms[r_idx][c_idx] == 0
    )

    while queue:
        row, col = queue.popleft()
        _relax_neighbors(rooms, row, col, queue)


# --- helpers --------------------------------------------------------------

def _relax_neighbors(
    rooms: list[list[int]],
    row: int,
    col: int,
    queue: deque[tuple[int, int]],
) -> None:
    rows, cols = len(rooms), len(rooms[0])
    next_dist = rooms[row][col] + 1

    for dr, dc in ORTHO_DIRS:
        nr, nc = row + dr, col + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            continue
        if rooms[nr][nc] != INF:
            continue
        rooms[nr][nc] = next_dist
        queue.append((nr, nc))


# --- tests ----------------------------------------------------------------

class TestWallsAndGates(unittest.TestCase):
    def test_examples(self) -> None:
        rooms = [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF],
        ]
        walls_and_gates(rooms)
        self.assertEqual(
            rooms,
            [
                [3, -1, 0, 1],
                [2, 2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4],
            ],
        )

    def test_edges(self) -> None:
        isolated = [[-1, INF], [-1, -1]]
        walls_and_gates(isolated)
        self.assertEqual(isolated, [[-1, INF], [-1, -1]])
        walls_and_gates([])


if __name__ == "__main__":
    unittest.main()
