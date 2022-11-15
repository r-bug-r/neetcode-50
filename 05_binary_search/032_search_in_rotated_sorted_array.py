# [032_search_in_rotated_sorted_array] single-pass rotated binary search | invariant: O(log n) time

import unittest


# --- public api -----------------------------------------------------------

def search(nums: list[int], target: int) -> int:
    """Return index of target in a rotated unique sorted array, or -1 if absent."""
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if _in_left_branch(nums, lo, mid, hi, target):
            hi = mid - 1
            continue
        lo = mid + 1

    return -1


# --- helpers --------------------------------------------------------------

def _in_left_branch(nums: list[int], lo: int, mid: int, hi: int, target: int) -> bool:
    if nums[lo] <= nums[mid]:
        return nums[lo] <= target < nums[mid]
    return not (nums[mid] < target <= nums[hi])


# --- tests ----------------------------------------------------------------

class TestSearchRotated(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(search([1], 0), -1)

    def test_edges(self) -> None:
        self.assertEqual(search([], 1), -1)
        self.assertEqual(search([1], 1), 0)
        self.assertEqual(search([3, 1], 1), 1)


if __name__ == "__main__":
    unittest.main()
