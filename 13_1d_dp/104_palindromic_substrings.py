# [104_palindromic_substrings] center expansion counter | invariant: O(n^2) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def count_substrings(s: str) -> int:
    """Return total number of palindromic substrings in s."""
    if not s:
        return 0

    total_palindromes = 0
    for center in range(len(s)):
        total_palindromes += _count_from_center(s, center, center)
        total_palindromes += _count_from_center(s, center, center + 1)

    return total_palindromes


# --- helpers --------------------------------------------------------------

def _count_from_center(s: str, left: int, right: int) -> int:
    limit = len(s)
    matches = 0
    while left >= 0 and right < limit and s[left] == s[right]:
        matches += 1
        left -= 1
        right += 1
    return matches


# --- tests ----------------------------------------------------------------

class TestPalindromicSubstrings(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(count_substrings("abc"), 3)
        self.assertEqual(count_substrings("aaa"), 6)

    def test_edges(self) -> None:
        self.assertEqual(count_substrings(""), 0)
        self.assertEqual(count_substrings("a"), 1)
        self.assertEqual(count_substrings("aba"), 4)
        self.assertEqual(count_substrings("abba"), 6)


if __name__ == "__main__":
    unittest.main()
