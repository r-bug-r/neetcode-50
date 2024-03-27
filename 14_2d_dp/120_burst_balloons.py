# [120_burst_balloons] interval DP over last burst | invariant: O(n^3) time, O(n^2) space

import unittest


# --- public api -----------------------------------------------------------

def max_coins(nums: list[int]) -> int:
    """Return maximum coins earned by bursting balloons in any order."""
    # perf: zero-value balloons yield 0 coins and contribute nothing as boundaries
    padded = [1, *(val for val in nums if val > 0), 1]
    count = len(padded)
    if count <= 2:
        return 0

    dp = [[0] * count for _ in range(count)]

    for span in range(2, count):
        _solve_span(padded, dp, count, span)

    return dp[0][count - 1]


# --- helpers --------------------------------------------------------------

def _solve_span(padded: list[int], dp: list[list[int]], count: int, span: int) -> None:
    for left in range(count - span):
        right = left + span
        dp[left][right] = _best_split_coins(padded, dp, left, right)


def _best_split_coins(padded: list[int], dp: list[list[int]], left: int, right: int) -> int:
    edge_product = padded[left] * padded[right]
    best = 0
    # invariant: split_idx is the final balloon burst inside open interval (left, right)
    for split_idx in range(left + 1, right):
        coins = dp[left][split_idx] + edge_product * padded[split_idx] + dp[split_idx][right]
        if coins > best:
            best = coins
    return best


# --- tests ----------------------------------------------------------------

class TestBurstBalloons(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(max_coins([3, 1, 5, 8]), 167)
        self.assertEqual(max_coins([1, 5]), 10)

    def test_edges(self) -> None:
        self.assertEqual(max_coins([]), 0)
        self.assertEqual(max_coins([0, 0]), 0)
        self.assertEqual(max_coins([7]), 7)
        self.assertEqual(max_coins([9, 76, 64, 21]), 116718)


if __name__ == "__main__":
    unittest.main()
