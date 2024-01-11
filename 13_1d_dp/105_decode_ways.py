# [105_decode_ways] rolling 2-char DP | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def num_decodings(s: str) -> int:
    """Return number of ways to decode a digit string where '1'..'26' map to A..Z."""
    if not s or s[0] == "0":
        return 0

    two_back = 1
    one_back = 1

    for idx in range(1, len(s)):
        ways = _ways_ending_at(s, idx, two_back, one_back)
        if ways == 0:
            return 0
        two_back = one_back
        one_back = ways

    return one_back


# --- helpers --------------------------------------------------------------

def _ways_ending_at(s: str, idx: int, two_back: int, one_back: int) -> int:
    ways = 0
    if s[idx] != "0":
        ways += one_back
    pair_value = int(s[idx - 1 : idx + 1])
    if 10 <= pair_value <= 26:
        ways += two_back
    return ways


# --- tests ----------------------------------------------------------------

class TestDecodeWays(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(num_decodings("12"), 2)
        self.assertEqual(num_decodings("226"), 3)
        self.assertEqual(num_decodings("06"), 0)

    def test_edges(self) -> None:
        self.assertEqual(num_decodings(""), 0)
        self.assertEqual(num_decodings("0"), 0)
        self.assertEqual(num_decodings("10"), 1)
        self.assertEqual(num_decodings("2101"), 1)
        self.assertEqual(num_decodings("100"), 0)
        self.assertEqual(num_decodings("27"), 1)


if __name__ == "__main__":
    unittest.main()
