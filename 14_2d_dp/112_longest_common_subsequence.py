# [112_longest_common_subsequence] rolling 1D LCS DP | invariant: O(m * n) time, O(min(m, n)) space

import unittest


# --- public api -----------------------------------------------------------

def longest_common_subsequence(text1: str, text2: str) -> int:
    """Return length of the longest common subsequence between text1 and text2."""
    if not text1 or not text2:
        return 0

    longer, shorter = (text1, text2) if len(text1) >= len(text2) else (text2, text1)
    prev_row = [0] * (len(shorter) + 1)

    for ch1 in longer:
        prev_row = _advance_lcs_row(prev_row, ch1, shorter)

    return prev_row[-1]


# --- helpers --------------------------------------------------------------

def _advance_lcs_row(prev_row: list[int], ch1: str, shorter: str) -> list[int]:
    curr_row = [0] * (len(shorter) + 1)
    for col, ch2 in enumerate(shorter, start=1):
        if ch1 == ch2:
            curr_row[col] = prev_row[col - 1] + 1
        else:
            curr_row[col] = max(prev_row[col], curr_row[col - 1])
    return curr_row


# --- tests ----------------------------------------------------------------

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(longest_common_subsequence("abcde", "ace"), 3)
        self.assertEqual(longest_common_subsequence("abc", "abc"), 3)
        self.assertEqual(longest_common_subsequence("abc", "def"), 0)

    def test_edges(self) -> None:
        self.assertEqual(longest_common_subsequence("", "abc"), 0)
        self.assertEqual(longest_common_subsequence("a", "a"), 1)
        self.assertEqual(longest_common_subsequence("bsbininm", "jmjkbkjkv"), 1)
        self.assertEqual(longest_common_subsequence("oxcpqrsvwf", "shmtulqrypy"), 2)


if __name__ == "__main__":
    unittest.main()
