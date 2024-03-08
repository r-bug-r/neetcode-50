# [115_target_sum] subset-sum reduction DP | invariant: O(n * target_sum) time, O(target_sum) space

import unittest


# --- public api -----------------------------------------------------------

def find_target_sum_ways(nums: list[int], target: int) -> int:
    """Return number of +/- sign assignments over nums that evaluate to target."""
    if not nums:
        return 1 if target == 0 else 0

    total = sum(abs(num) for num in nums)
    if abs(target) > total or (total + target) % 2 != 0:
        return 0

    # why: P - N = target and P + N = total implies 2*P = total + target
    positive_sum = (total + target) // 2
    ways = [0] * (positive_sum + 1)
    ways[0] = 1

    for num in nums:
        magnitude = abs(num)
        if magnitude <= positive_sum:
            _accumulate_subset_ways(ways, magnitude, positive_sum)

    return ways[positive_sum]


# --- helpers --------------------------------------------------------------

def _accumulate_subset_ways(ways: list[int], weight: int, positive_sum: int) -> None:
    # invariant: reverse sweep preserves 0/1 usage and doubles counts when weight is 0
    for total in range(positive_sum, weight - 1, -1):
        ways[total] += ways[total - weight]


# --- tests ----------------------------------------------------------------

class TestTargetSum(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(find_target_sum_ways([1, 1, 1, 1, 1], 3), 5)
        self.assertEqual(find_target_sum_ways([1], 1), 1)

    def test_edges(self) -> None:
        self.assertEqual(find_target_sum_ways([], 0), 1)
        self.assertEqual(find_target_sum_ways([], 1), 0)
        self.assertEqual(find_target_sum_ways([0, 0, 0, 0, 1], 1), 16)
        self.assertEqual(find_target_sum_ways([1, 2, 1], 10), 0)
        self.assertEqual(find_target_sum_ways([1, 2, 1], 1), 0)


if __name__ == "__main__":
    unittest.main()
