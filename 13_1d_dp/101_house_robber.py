# [101_house_robber] non-adjacent linear DP | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def rob(nums: list[int]) -> int:
    """Return maximum loot from non-adjacent houses along a linear street."""
    if not nums:
        return 0

    two_back = 0
    one_back = 0

    for stash in nums:
        best_here = max(one_back, two_back + stash)
        two_back = one_back
        one_back = best_here

    return one_back


# --- tests ----------------------------------------------------------------

class TestHouseRobber(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(rob([1, 2, 3, 1]), 4)
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)

    def test_edges(self) -> None:
        self.assertEqual(rob([]), 0)
        self.assertEqual(rob([9]), 9)
        self.assertEqual(rob([2, 1, 1, 2]), 4)
        self.assertEqual(rob([0, 0, 0]), 0)


if __name__ == "__main__":
    unittest.main()
