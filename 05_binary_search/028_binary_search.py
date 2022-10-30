# [028_binary_search] classic sorted-array index lookup | invariant: O(log n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def search(nums: list[int], target: int) -> int:
    """Return the index of target in sorted nums, or -1 if absent."""
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
            continue
        hi = mid - 1

    return -1


# --- tests ----------------------------------------------------------------

class TestBinarySearch(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_edges(self) -> None:
        self.assertEqual(search([], 5), -1)
        self.assertEqual(search([5], 5), 0)
        self.assertEqual(search([5], -5), -1)


if __name__ == "__main__":
    unittest.main()
