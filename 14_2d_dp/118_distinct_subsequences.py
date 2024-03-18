# [118_distinct_subsequences] rolling 1D subsequence DP | invariant: O(m * n) time, O(n) space

import unittest


# --- public api -----------------------------------------------------------

def num_distinct(s: str, t: str) -> int:
    """Return number of distinct subsequences of s that equal t."""
    if not t:
        return 1
    if len(t) > len(s):
        return 0

    target_len = len(t)
    ways = [0] * (target_len + 1)
    ways[0] = 1

    for src_idx, src_ch in enumerate(s):
        max_prefix = min(target_len, src_idx + 1)
        _update_distinct_ways(ways, src_ch, t, max_prefix)

    return ways[target_len]


# --- helpers --------------------------------------------------------------

def _update_distinct_ways(ways: list[int], src_ch: str, t: str, max_prefix: int) -> None:
    # invariant: reverse sweep prevents reusing the same source character multiple times
    for t_idx in range(max_prefix, 0, -1):
        if src_ch == t[t_idx - 1]:
            ways[t_idx] += ways[t_idx - 1]


# --- tests ----------------------------------------------------------------

class TestDistinctSubsequences(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(num_distinct("rabbbit", "rabbit"), 3)
        self.assertEqual(num_distinct("babgbag", "bag"), 5)

    def test_edges(self) -> None:
        self.assertEqual(num_distinct("abc", ""), 1)
        self.assertEqual(num_distinct("", "a"), 0)
        self.assertEqual(num_distinct("ab", "abc"), 0)
        self.assertEqual(num_distinct("aaa", "aa"), 3)


if __name__ == "__main__":
    unittest.main()
