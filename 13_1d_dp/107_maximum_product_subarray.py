# [107_maximum_product_subarray] min-max product DP | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def max_product(nums: list[int]) -> int:
    """Return maximum product of any contiguous non-empty subarray."""
    if not nums:
        return 0

    best_product = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]

    for factor in nums[1:]:
        # invariant: curr_min tracks most negative product for sign flips on negative factors
        candidates = (factor, curr_max * factor, curr_min * factor)
        curr_max = max(candidates)
        curr_min = min(candidates)
        if curr_max > best_product:
            best_product = curr_max

    return best_product


# --- tests ----------------------------------------------------------------

class TestMaximumProductSubarray(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(max_product([2, 3, -2, 4]), 6)
        self.assertEqual(max_product([-2, 0, -1]), 0)

    def test_edges(self) -> None:
        self.assertEqual(max_product([]), 0)
        self.assertEqual(max_product([-3]), -3)
        self.assertEqual(max_product([-2, 3, -4]), 24)
        self.assertEqual(max_product([0, 2]), 2)
        self.assertEqual(max_product([-2, 0, -3, -4]), 12)


if __name__ == "__main__":
    unittest.main()
