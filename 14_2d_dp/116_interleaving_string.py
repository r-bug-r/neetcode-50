# [116_interleaving_string] rolling 1D interleaving DP | invariant: O(m * n) time, O(min(m, n)) space

import unittest


# --- public api -----------------------------------------------------------

def is_interleave(s1: str, s2: str, s3: str) -> bool:
    """Return True when s3 is formed by an order-preserving interleaving of s1 and s2."""
    if len(s1) + len(s2) != len(s3):
        return False

    # perf: keep shorter string on the columns to minimize rolling DP width
    first, second = (s1, s2) if len(s1) >= len(s2) else (s2, s1)
    dp = [False] * (len(second) + 1)
    dp[0] = True

    for col in range(1, len(second) + 1):
        dp[col] = dp[col - 1] and second[col - 1] == s3[col - 1]

    for row, ch1 in enumerate(first, start=1):
        _step_interleave_row(dp, ch1, second, s3, row)

    return dp[-1]


# --- helpers --------------------------------------------------------------

def _step_interleave_row(dp: list[bool], ch1: str, second: str, s3: str, row: int) -> None:
    dp[0] = dp[0] and ch1 == s3[row - 1]
    for col, ch2 in enumerate(second, start=1):
        target_ch = s3[row + col - 1]
        from_first = dp[col] and ch1 == target_ch
        from_second = dp[col - 1] and ch2 == target_ch
        dp[col] = from_first or from_second


# --- tests ----------------------------------------------------------------

class TestInterleavingString(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(is_interleave("aabcc", "dbbca", "aadbbcbcac"))
        self.assertFalse(is_interleave("aabcc", "dbbca", "aadbbbaccc"))
        self.assertTrue(is_interleave("", "", ""))

    def test_edges(self) -> None:
        self.assertFalse(is_interleave("a", "b", "a"))
        self.assertTrue(is_interleave("", "abc", "abc"))
        self.assertTrue(is_interleave("abc", "", "abc"))
        self.assertFalse(is_interleave("db", "b", "cbb"))


if __name__ == "__main__":
    unittest.main()
