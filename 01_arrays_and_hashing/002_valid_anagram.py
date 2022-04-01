# [002_valid_anagram] frequency check for two strings | invariant: O(n) time, O(1) alphabet space

import unittest


# --- public api -----------------------------------------------------------

def is_anagram(s: str, t: str) -> bool:
    """Return True if t is an anagram of s."""
    if len(s) != len(t):
        return False

    char_balance: dict[str, int] = {}
    for ch_s, ch_t in zip(s, t):
        char_balance[ch_s] = char_balance.get(ch_s, 0) + 1
        char_balance[ch_t] = char_balance.get(ch_t, 0) - 1

    return all(count == 0 for count in char_balance.values())


# --- tests ----------------------------------------------------------------

class TestValidAnagram(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(is_anagram("anagram", "nagaram"))
        self.assertFalse(is_anagram("rat", "car"))

    def test_edges(self) -> None:
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("a", "ab"))


if __name__ == "__main__":
    unittest.main()
