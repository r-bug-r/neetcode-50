# [121_regular_expression_matching] NFA prefix DP with '.' and '*' | invariant: O(m * n) time and space

import unittest


# --- public api -----------------------------------------------------------

def is_match(s: str, p: str) -> bool:
    """Return True when entire string s matches regex pattern p supporting '.' and '*'."""
    rows = len(s)
    cols = len(p)
    dp = [[False] * (cols + 1) for _ in range(rows + 1)]
    dp[0][0] = True

    for col in range(2, cols + 1):
        if p[col - 1] == "*":
            dp[0][col] = dp[0][col - 2]

    for row in range(1, rows + 1):
        _fill_regex_row(s, p, dp, row, cols)

    return dp[rows][cols]


# --- helpers --------------------------------------------------------------

def _fill_regex_row(s: str, p: str, dp: list[list[bool]], row: int, cols: int) -> None:
    src_ch = s[row - 1]
    for col in range(1, cols + 1):
        pat_ch = p[col - 1]
        if pat_ch == "*":
            zero_repeat = dp[row][col - 2]
            one_or_more = _char_matches(src_ch, p[col - 2]) and dp[row - 1][col]
            dp[row][col] = zero_repeat or one_or_more
        else:
            dp[row][col] = _char_matches(src_ch, pat_ch) and dp[row - 1][col - 1]


def _char_matches(src_ch: str, pat_ch: str) -> bool:
    return pat_ch == "." or src_ch == pat_ch


# --- tests ----------------------------------------------------------------

class TestRegularExpressionMatching(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertFalse(is_match("aa", "a"))
        self.assertTrue(is_match("aa", "a*"))
        self.assertTrue(is_match("ab", ".*"))

    def test_edges(self) -> None:
        self.assertTrue(is_match("", ""))
        self.assertTrue(is_match("", "a*b*"))
        self.assertTrue(is_match("aab", "c*a*b"))
        self.assertFalse(is_match("mississippi", "mis*is*p*."))


if __name__ == "__main__":
    unittest.main()
