# [122_maximum_subarray] Kadane single-pass scan | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def max_subarray(nums: list[int]) -> int:
    """Return the largest sum of any contiguous non-empty subarray in nums."""
    if not nums:
        return 0

    best_sum = nums[0]
    curr_sum = nums[0]

    for num in nums[1:]:
        curr_sum = num if curr_sum < 0 else curr_sum + num
        if curr_sum > best_sum:
            best_sum = curr_sum

    return best_sum


# --- tests ----------------------------------------------------------------

class TestMaximumSubarray(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_subarray([1]), 1)
        self.assertEqual(max_subarray([5, 4, -1, 7, 8]), 23)

    def test_edges(self) -> None:
        self.assertEqual(max_subarray([]), 0)
        self.assertEqual(max_subarray([-5, -2, -9, -3]), -2)
        self.assertEqual(max_subarray([0, 0, 0]), 0)
        self.assertEqual(max_subarray([3, -2, 5, -1]), 6)


if __name__ == "__main__":
    unittest.main()
