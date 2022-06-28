# [012_three_sum] unique zero-sum triplets | invariant: O(n^2) time, O(1) aux space

import unittest


# --- public api -----------------------------------------------------------

def three_sum(nums: list[int]) -> list[list[int]]:
    """Return all unique triplets in nums whose elements sum to zero."""
    if len(nums) < 3:
        return []

    sorted_nums = sorted(nums)
    triplets: list[list[int]] = []

    for anchor_idx, anchor in enumerate(sorted_nums[:-2]):
        # perf: sorted positive anchor cannot sum to zero with larger elements
        if anchor > 0:
            break
        if anchor_idx > 0 and anchor == sorted_nums[anchor_idx - 1]:
            continue
        _collect_zero_pairs(sorted_nums, anchor_idx, triplets)

    return triplets


# --- helpers --------------------------------------------------------------

def _collect_zero_pairs(
    sorted_nums: list[int],
    anchor_idx: int,
    triplets: list[list[int]],
) -> None:
    anchor = sorted_nums[anchor_idx]
    lo = anchor_idx + 1
    hi = len(sorted_nums) - 1

    while lo < hi:
        triplet_sum = anchor + sorted_nums[lo] + sorted_nums[hi]
        if triplet_sum < 0:
            lo += 1
            continue
        if triplet_sum > 0:
            hi -= 1
            continue

        triplets.append([anchor, sorted_nums[lo], sorted_nums[hi]])
        lo += 1
        hi -= 1
        # invariant: skip duplicate left values so each triplet is emitted once
        while lo < hi and sorted_nums[lo] == sorted_nums[lo - 1]:
            lo += 1


# --- tests ----------------------------------------------------------------

class TestThreeSum(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(three_sum([0, 1, 1]), [])
        self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])

    def test_edges(self) -> None:
        self.assertEqual(three_sum([]), [])
        self.assertEqual(three_sum([0, 0]), [])
        self.assertEqual(three_sum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(three_sum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])


if __name__ == "__main__":
    unittest.main()
