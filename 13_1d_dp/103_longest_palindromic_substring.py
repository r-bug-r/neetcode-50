# [103_longest_palindromic_substring] center expansion | invariant: O(n^2) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def longest_palindrome(s: str) -> str:
    """Return the longest palindromic substring in s."""
    if len(s) < 2:
        return s

    best_start = 0
    best_length = 1

    for center in range(len(s)):
        odd_start, odd_len = _expand_palindrome(s, center, center)
        even_start, even_len = _expand_palindrome(s, center, center + 1)
        cand_start, cand_len = (
            (odd_start, odd_len) if odd_len >= even_len else (even_start, even_len)
        )
        if cand_len > best_length:
            best_start = cand_start
            best_length = cand_len

    return s[best_start : best_start + best_length]


# --- helpers --------------------------------------------------------------

def _expand_palindrome(s: str, left: int, right: int) -> tuple[int, int]:
    limit = len(s)
    while left >= 0 and right < limit and s[left] == s[right]:
        left -= 1
        right += 1
    start = left + 1
    return start, right - start


# --- tests ----------------------------------------------------------------

class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertIn(longest_palindrome("babad"), {"bab", "aba"})
        self.assertEqual(longest_palindrome("cbbd"), "bb")

    def test_edges(self) -> None:
        self.assertEqual(longest_palindrome(""), "")
        self.assertEqual(longest_palindrome("a"), "a")
        self.assertIn(longest_palindrome("ac"), {"a", "c"})
        self.assertEqual(longest_palindrome("racecar"), "racecar")
        self.assertEqual(longest_palindrome("aacabdkacaa"), "aca")


if __name__ == "__main__":
    unittest.main()
