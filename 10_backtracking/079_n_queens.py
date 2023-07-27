# [079_n_queens] N-queens placement | invariant: O(1) column and diagonal conflict sets

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def solve_n_queens(board_size: int) -> list[list[str]]:
    """Return all distinct N-queens board layouts for an N x N grid."""
    if board_size <= 0:
        return []
    boards: list[list[str]] = []
    _place_row(0, board_size, set(), set(), set(), [], boards)
    return boards


# --- helpers --------------------------------------------------------------

def _place_row(
    row: int,
    board_size: int,
    used_cols: set[int],
    pos_diags: set[int],
    neg_diags: set[int],
    queen_cols: list[int],
    boards: list[list[str]],
) -> None:
    if row == board_size:
        boards.append(_render_board(queen_cols, board_size))
        return

    for col in range(board_size):
        if col in used_cols or (row + col) in pos_diags or (row - col) in neg_diags:
            continue
        used_cols.add(col)
        pos_diags.add(row + col)
        neg_diags.add(row - col)
        queen_cols.append(col)

        _place_row(row + 1, board_size, used_cols, pos_diags, neg_diags, queen_cols, boards)

        queen_cols.pop()
        neg_diags.remove(row - col)
        pos_diags.remove(row + col)
        used_cols.remove(col)


def _render_board(queen_cols: list[int], board_size: int) -> list[str]:
    return [
        "." * col + "Q" + "." * (board_size - col - 1)
        for col in queen_cols
    ]


# --- tests ----------------------------------------------------------------

class TestNQueens(unittest.TestCase):
    def test_examples(self) -> None:
        expected = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ]
        self.assertEqual(sorted(solve_n_queens(4)), sorted(expected))
        self.assertEqual(solve_n_queens(1), [["Q"]])

    def test_edges(self) -> None:
        self.assertEqual(solve_n_queens(2), [])
        self.assertEqual(solve_n_queens(3), [])


if __name__ == "__main__":
    unittest.main()
