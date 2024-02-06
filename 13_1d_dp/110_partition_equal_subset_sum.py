# [110_partition_equal_subset_sum] bitset subset sum DP | invariant: O(n * sum / w) time

import unittest


# --- public api -----------------------------------------------------------

def can_partition(nums: list[int]) -> bool:
    """Return True when nums can be partitioned into two subsets with equal sum."""
    if len(nums) < 2:
        return False
    if min(nums) < 0:
        raise ValueError("can_partition requires non-negative integers")

    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    target_bit = 1 << target
    # perf: bitset shift evaluates all reachable subset sums in C-level integer ops
    subset_mask = (target_bit << 1) - 1
    reachable = 1

    for num in nums:
        reachable = (reachable | (reachable << num)) & subset_mask
        if reachable & target_bit:
            return True

    return False


# --- tests ----------------------------------------------------------------

class TestPartitionEqualSubsetSum(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(can_partition([1, 5, 11, 5]))
        self.assertFalse(can_partition([1, 2, 3, 5]))

    def test_edges(self) -> None:
        self.assertFalse(can_partition([]))
        self.assertFalse(can_partition([2]))
        self.assertTrue(can_partition([0, 0]))
        self.assertTrue(can_partition([2, 2, 1, 1]))
        self.assertFalse(can_partition([1, 2, 5]))
        with self.assertRaises(ValueError):
            can_partition([1, -1])


if __name__ == "__main__":
    unittest.main()
