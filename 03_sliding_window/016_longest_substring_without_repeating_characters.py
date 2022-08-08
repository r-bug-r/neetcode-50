# [016_longest_substring_without_repeating_characters] unique-char window | invariant: O(n) time, O(min(n, charset)) space

import unittest


# --- public api -----------------------------------------------------------

def length_of_longest_substring(text: str) -> int:
    """Return the length of the longest substring of text without repeated characters."""
    last_index_by_char: dict[str, int] = {}
    left = 0
    longest = 0

    for right, ch in enumerate(text):
        # invariant: text[left:right] contains no duplicate characters
        if ch in last_index_by_char and last_index_by_char[ch] >= left:
            left = last_index_by_char[ch] + 1
        last_index_by_char[ch] = right
        window_len = right - left + 1
        if window_len > longest:
            longest = window_len

    return longest


# --- tests ----------------------------------------------------------------

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    def test_edges(self) -> None:
        self.assertEqual(length_of_longest_substring(""), 0)
        self.assertEqual(length_of_longest_substring("a"), 1)
        self.assertEqual(length_of_longest_substring("abba"), 2)
        self.assertEqual(length_of_longest_substring("dvdf"), 3)


if __name__ == "__main__":
    unittest.main()
