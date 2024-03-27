# [119_edit_distance] Levenshtein rolling DP | invariant: O(m * n) time, O(min(m, n)) space

import unittest


# --- public api -----------------------------------------------------------

def min_distance(word1: str, word2: str) -> int:
    """Return minimum single-character edits to transform word1 into word2."""
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)

    # perf: keep shorter word as columns to minimize rolling DP width
    longer, shorter = (word1, word2) if len(word1) >= len(word2) else (word2, word1)
    prev_row = list(range(len(shorter) + 1))

    for row_idx, ch1 in enumerate(longer, start=1):
        prev_row = _step_edit_row(prev_row, ch1, shorter, row_idx)

    return prev_row[-1]


# --- helpers --------------------------------------------------------------

def _step_edit_row(prev_row: list[int], ch1: str, shorter: str, row_idx: int) -> list[int]:
    curr_row = [row_idx] + [0] * len(shorter)
    for col_idx, ch2 in enumerate(shorter, start=1):
        if ch1 == ch2:
            curr_row[col_idx] = prev_row[col_idx - 1]
        else:
            curr_row[col_idx] = 1 + min(prev_row[col_idx], curr_row[col_idx - 1], prev_row[col_idx - 1])
    return curr_row


# --- tests ----------------------------------------------------------------

class TestEditDistance(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(min_distance("horse", "ros"), 3)
        self.assertEqual(min_distance("intention", "execution"), 5)

    def test_edges(self) -> None:
        self.assertEqual(min_distance("", "abc"), 3)
        self.assertEqual(min_distance("abc", ""), 3)
        self.assertEqual(min_distance("same", "same"), 0)
        self.assertEqual(min_distance("a", "b"), 1)


if __name__ == "__main__":
    unittest.main()
