# [003_two_sum] index pair summing to target | invariant: O(n) time, O(n) space

import unittest


# --- public api -----------------------------------------------------------

def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers in nums that add up to target."""
    index_by_val: dict[int, int] = {}
    for idx, num in enumerate(nums):
        complement = target - num
        # perf: O(1) complement lookup avoids quadratic pair scan
        if complement in index_by_val:
            return [index_by_val[complement], idx]
        index_by_val[num] = idx

    raise ValueError("no two sum solution exists")


# --- tests ----------------------------------------------------------------

class TestTwoSum(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_negative_numbers(self) -> None:
        self.assertEqual(two_sum([-3, 4, 3, 90], 0), [0, 2])


if __name__ == "__main__":
    unittest.main()
