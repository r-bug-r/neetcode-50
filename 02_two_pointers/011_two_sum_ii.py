# [011_two_sum_ii] 1-indexed pair sum in sorted array | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """Return 1-indexed positions of two numbers in sorted numbers summing to target."""
    lo = 0
    hi = len(numbers) - 1

    while lo < hi:
        pair_sum = numbers[lo] + numbers[hi]
        if pair_sum == target:
            return [lo + 1, hi + 1]
        if pair_sum < target:
            lo += 1
            continue
        hi -= 1

    raise ValueError("no two sum solution exists")


# --- tests ----------------------------------------------------------------

class TestTwoSumSorted(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(two_sum_sorted([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(two_sum_sorted([2, 3, 4], 6), [1, 3])
        self.assertEqual(two_sum_sorted([-1, 0], -1), [1, 2])

    def test_edges(self) -> None:
        self.assertEqual(two_sum_sorted([-5, -2, 0, 3, 8], 1), [2, 4])
        self.assertEqual(two_sum_sorted([1, 1], 2), [1, 2])
        with self.assertRaises(ValueError):
            two_sum_sorted([1, 2, 3], 10)


if __name__ == "__main__":
    unittest.main()
