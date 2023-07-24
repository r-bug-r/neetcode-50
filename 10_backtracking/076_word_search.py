# [076_word_search] 2D grid word DFS | invariant: in-place marker restored on backtrack

from __future__ import annotations

from collections import Counter
from itertools import product
import unittest


# --- tables ---------------------------------------------------------------

ORTHO_DIRS: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


# --- public api -----------------------------------------------------------

def exist(board: list[list[str]], word: str) -> bool:
    """Return True if word can be formed by orthogonally adjacent unvisited cells."""
    if not word:
        return True
    if not board or not board[0]:
        return False

    board_counts = Counter(ch for row in board for ch in row)
    if not _has_required_counts(board_counts, word):
        return False

    # perf: start from the rarer endpoint to minimize DFS branching factor
    search_word = word[::-1] if board_counts[word[0]] > board_counts[word[-1]] else word
    rows, cols = len(board), len(board[0])
    for r_idx, c_idx in product(range(rows), range(cols)):
        if _match_from(board, r_idx, c_idx, search_word, 0):
            return True
    return False


# --- helpers --------------------------------------------------------------

def _has_required_counts(board_counts: Counter[str], word: str) -> bool:
    word_counts = Counter(word)
    return all(board_counts[ch] >= needed for ch, needed in word_counts.items())


def _match_from(
    board: list[list[str]],
    row: int,
    col: int,
    word: str,
    char_idx: int,
) -> bool:
    if char_idx == len(word):
        return True
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False
    if board[row][col] != word[char_idx]:
        return False

    saved = board[row][col]
    board[row][col] = "#"
    matched = any(
        _match_from(board, row + dr, col + dc, word, char_idx + 1)
        for dr, dc in ORTHO_DIRS
    )
    board[row][col] = saved
    return matched


# --- tests ----------------------------------------------------------------

class TestWordSearch(unittest.TestCase):
    def test_examples(self) -> None:
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        self.assertTrue(exist(board, "ABCCED"))
        self.assertTrue(exist(board, "SEE"))
        self.assertFalse(exist(board, "ABCB"))

    def test_edges(self) -> None:
        self.assertTrue(exist([["a"]], "a"))
        self.assertFalse(exist([], "a"))
        self.assertTrue(exist([["a"]], ""))


if __name__ == "__main__":
    unittest.main()
