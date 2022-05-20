# [008_valid_sudoku] 9x9 board constraint check | invariant: O(1) fixed 81-cell pass

from collections import defaultdict
from itertools import product
import unittest


# --- public api -----------------------------------------------------------

def is_valid_sudoku(board: list[list[str]]) -> bool:
    """Return True if filled cells in a 9x9 Sudoku board have no conflicts."""
    rows: dict[int, set[str]] = defaultdict(set)
    cols: dict[int, set[str]] = defaultdict(set)
    boxes: dict[tuple[int, int], set[str]] = defaultdict(set)

    for r_idx, c_idx in product(range(9), range(9)):
        digit = board[r_idx][c_idx]
        if digit == ".":
            continue

        box_key = (r_idx // 3, c_idx // 3)
        if digit in rows[r_idx] or digit in cols[c_idx] or digit in boxes[box_key]:
            return False

        rows[r_idx].add(digit)
        cols[c_idx].add(digit)
        boxes[box_key].add(digit)

    return True


# --- tests ----------------------------------------------------------------

class TestValidSudoku(unittest.TestCase):
    def test_valid_board(self) -> None:
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertTrue(is_valid_sudoku(board))

    def test_invalid_board(self) -> None:
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertFalse(is_valid_sudoku(board))


if __name__ == "__main__":
    unittest.main()
