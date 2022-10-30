# [031_find_minimum_in_rotated_sorted_array] rotated array pivot minimum | invariant: O(log n) time

import unittest


# --- public api -----------------------------------------------------------

def find_min(nums: list[int]) -> int:
    """Return the minimum element in a rotated strictly ascending array."""
    if not nums:
        raise ValueError("nums cannot be empty")

    lo = 0
    hi = len(nums) - 1

    # invariant: minimum stays inside [lo, hi]
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
            continue
        hi = mid

    return nums[lo]


# --- tests ----------------------------------------------------------------

class TestFindMin(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_min([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(find_min([11, 13, 15, 17]), 11)

    def test_edges(self) -> None:
        self.assertEqual(find_min([7]), 7)
        self.assertEqual(find_min([2, 1]), 1)
        with self.assertRaises(ValueError):
            find_min([])


if __name__ == "__main__":
    unittest.main()
