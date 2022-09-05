# [018_permutation_in_string] fixed-width anagram window | invariant: O(n) time, O(1) space

import unittest

_ASCII_A = ord("a")
_ALPHABET_SIZE = 26


# --- public api -----------------------------------------------------------

def check_inclusion(pattern: str, text: str) -> bool:
    """Return True if any permutation of lowercase pattern appears as a substring of text."""
    if not pattern:
        return True
    if len(pattern) > len(text):
        return False

    pattern_counts = [0] * _ALPHABET_SIZE
    window_counts = [0] * _ALPHABET_SIZE
    span = len(pattern)

    for idx in range(span):
        pattern_counts[ord(pattern[idx]) - _ASCII_A] += 1
        window_counts[ord(text[idx]) - _ASCII_A] += 1

    # perf: track matching slots incrementally instead of comparing 26 counts per step
    matches = sum(1 for slot in range(_ALPHABET_SIZE) if pattern_counts[slot] == window_counts[slot])
    if matches == _ALPHABET_SIZE:
        return True

    for right in range(span, len(text)):
        in_slot = ord(text[right]) - _ASCII_A
        out_slot = ord(text[right - span]) - _ASCII_A
        matches = _shift_slot(window_counts, pattern_counts, in_slot, 1, matches)
        matches = _shift_slot(window_counts, pattern_counts, out_slot, -1, matches)
        if matches == _ALPHABET_SIZE:
            return True

    return False


# --- helpers --------------------------------------------------------------

def _shift_slot(
    window_counts: list[int],
    pattern_counts: list[int],
    slot: int,
    delta: int,
    matches: int,
) -> int:
    if window_counts[slot] == pattern_counts[slot]:
        matches -= 1
    window_counts[slot] += delta
    if window_counts[slot] == pattern_counts[slot]:
        matches += 1
    return matches


# --- tests ----------------------------------------------------------------

class TestPermutationInString(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(check_inclusion("ab", "eidbaooo"))
        self.assertFalse(check_inclusion("ab", "eidboaoo"))

    def test_edges(self) -> None:
        self.assertTrue(check_inclusion("", "abc"))
        self.assertFalse(check_inclusion("abcd", "abc"))
        self.assertTrue(check_inclusion("adc", "dcda"))
        self.assertTrue(check_inclusion("a", "a"))
        self.assertFalse(check_inclusion("a", "b"))


if __name__ == "__main__":
    unittest.main()
