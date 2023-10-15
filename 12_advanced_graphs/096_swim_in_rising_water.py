# [096_swim_in_rising_water] minimax Dijkstra over grid | invariant: O(N^2 log N) time

import heapq
import unittest

_CARDINAL_DIRS: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


# --- public api -----------------------------------------------------------

def swim_in_water(grid: list[list[int]]) -> int:
    """Return minimum water elevation t needed to swim from top-left to bottom-right."""
    size = len(grid)
    if size == 0 or len(grid[0]) == 0:
        return 0
    if size == 1:
        return grid[0][0]

    target = size - 1
    frontier: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]
    # invariant: seen prevents pushing the same cell twice because first visit via min-heap is optimal
    seen: set[tuple[int, int]] = {(0, 0)}

    while frontier:
        elevation, row, col = heapq.heappop(frontier)
        if row == target and col == target:
            return elevation
        _enqueue_neighbors(grid, size, elevation, row, col, seen, frontier)

    return -1


# --- helpers --------------------------------------------------------------

def _enqueue_neighbors(
    grid: list[list[int]],
    size: int,
    current_elevation: int,
    row: int,
    col: int,
    seen: set[tuple[int, int]],
    frontier: list[tuple[int, int, int]],
) -> None:
    for dr, dc in _CARDINAL_DIRS:
        next_row = row + dr
        next_col = col + dc
        if not (0 <= next_row < size and 0 <= next_col < size):
            continue
        coord = (next_row, next_col)
        if coord in seen:
            continue
        seen.add(coord)
        peak = max(current_elevation, grid[next_row][next_col])
        heapq.heappush(frontier, (peak, next_row, next_col))


# --- tests ----------------------------------------------------------------

class TestSwimInRisingWater(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(swim_in_water([[0, 2], [1, 3]]), 3)
        spiral = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        self.assertEqual(swim_in_water(spiral), 16)

    def test_edges(self) -> None:
        self.assertEqual(swim_in_water([]), 0)
        self.assertEqual(swim_in_water([[7]]), 7)
        self.assertEqual(swim_in_water([[3, 2], [0, 1]]), 3)


if __name__ == "__main__":
    unittest.main()
