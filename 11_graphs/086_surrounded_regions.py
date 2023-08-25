# [086_surrounded_regions] border-escaped region capture | invariant: O(m*n) in-place flip

from __future__ import annotations

from collections import deque
from itertools import product
import unittest


# --- tables ---------------------------------------------------------------

ORTHO_DIRS: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


# --- public api -----------------------------------------------------------

def solve_surrounded_regions(board: list[list[str]]) -> None:
    """Capture all 'O' regions completely surrounded by 'X' in-place."""
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])
    # why: only 'O' cells connected to a border cannot be captured
    _mark_border_safe(board, rows, cols)

    for r_idx, c_idx in product(range(rows), range(cols)):
        cell = board[r_idx][c_idx]
        if cell == "O":
            board[r_idx][c_idx] = "X"
        elif cell == "S":
            board[r_idx][c_idx] = "O"


# --- helpers --------------------------------------------------------------

def _mark_border_safe(board: list[list[str]], rows: int, cols: int) -> None:
    queue: deque[tuple[int, int]] = deque()
    for r_idx in range(rows):
        _seed_if_open(board, r_idx, 0, queue)
        _seed_if_open(board, r_idx, cols - 1, queue)
    for c_idx in range(cols):
        _seed_if_open(board, 0, c_idx, queue)
        _seed_if_open(board, rows - 1, c_idx, queue)

    while queue:
        row, col = queue.popleft()
        _expand_safe_neighbors(board, row, col, queue)


def _seed_if_open(
    board: list[list[str]],
    row: int,
    col: int,
    queue: deque[tuple[int, int]],
) -> None:
    if board[row][col] == "O":
        board[row][col] = "S"
        queue.append((row, col))


def _expand_safe_neighbors(
    board: list[list[str]],
    row: int,
    col: int,
    queue: deque[tuple[int, int]],
) -> None:
    rows, cols = len(board), len(board[0])
    for dr, dc in ORTHO_DIRS:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            _seed_if_open(board, nr, nc, queue)


# --- tests ----------------------------------------------------------------

class TestSurroundedRegions(unittest.TestCase):
    def test_examples(self) -> None:
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        solve_surrounded_regions(board)
        self.assertEqual(
            board,
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        )

    def test_edges(self) -> None:
        single = [["O"]]
        solve_surrounded_regions(single)
        self.assertEqual(single, [["O"]])
        solve_surrounded_regions([])


if __name__ == "__main__":
    unittest.main()
