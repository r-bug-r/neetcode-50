# [102_house_robber_ii] dual-pass circular DP | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def rob(nums: list[int]) -> int:
    """Return maximum loot from non-adjacent houses arranged in a circle."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # why: first and last houses are adjacent, so solve both linear exclusions
    without_last = _rob_slice(nums, 0, len(nums) - 1)
    without_first = _rob_slice(nums, 1, len(nums))
    return max(without_last, without_first)


# --- helpers --------------------------------------------------------------

def _rob_slice(nums: list[int], start: int, stop: int) -> int:
    two_back = 0
    one_back = 0

    for idx in range(start, stop):
        best_here = max(one_back, two_back + nums[idx])
        two_back = one_back
        one_back = best_here

    return one_back


# --- tests ----------------------------------------------------------------

class TestHouseRobberII(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(rob([2, 3, 2]), 3)
        self.assertEqual(rob([1, 2, 3, 1]), 4)
        self.assertEqual(rob([1, 2, 3]), 3)

    def test_edges(self) -> None:
        self.assertEqual(rob([]), 0)
        self.assertEqual(rob([5]), 5)
        self.assertEqual(rob([4, 9]), 9)
        self.assertEqual(rob([200, 3, 140, 20, 10]), 340)


if __name__ == "__main__":
    unittest.main()
