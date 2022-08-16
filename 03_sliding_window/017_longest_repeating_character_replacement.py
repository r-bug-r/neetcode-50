# [017_longest_repeating_character_replacement] k-replacement window | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def character_replacement(text: str, max_replacements: int) -> int:
    """Return max substring length achievable with at most max_replacements edits."""
    char_counts: dict[str, int] = {}
    left = 0
    peak_freq = 0
    longest = 0

    for right, ch in enumerate(text):
        char_counts[ch] = char_counts.get(ch, 0) + 1
        peak_freq = max(peak_freq, char_counts[ch])

        # invariant: window size never shrinks, so peak_freq only needs upward updates
        if (right - left + 1) - peak_freq > max_replacements:
            left_ch = text[left]
            char_counts[left_ch] -= 1
            left += 1

        longest = max(longest, right - left + 1)

    return longest


# --- tests ----------------------------------------------------------------

class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(character_replacement("ABAB", 2), 4)
        self.assertEqual(character_replacement("AABABBA", 1), 4)

    def test_edges(self) -> None:
        self.assertEqual(character_replacement("", 2), 0)
        self.assertEqual(character_replacement("A", 0), 1)
        self.assertEqual(character_replacement("ABCDE", 0), 1)
        self.assertEqual(character_replacement("BAAAB", 2), 5)


if __name__ == "__main__":
    unittest.main()
