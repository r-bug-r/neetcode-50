# [042_find_the_duplicate_number] Floyd cycle entry finder | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def find_duplicate(nums: list[int]) -> int:
    """Return the repeated integer in a 1..n array of length n + 1 without modifying it."""
    if len(nums) < 2:
        raise ValueError("nums must contain at least two elements")

    # invariant: treating nums[i] as next pointer guarantees a cycle at the duplicate value
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    entry = nums[0]
    while entry != slow:
        entry = nums[entry]
        slow = nums[slow]

    return entry


# --- tests ----------------------------------------------------------------

class TestFindDuplicateNumber(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(find_duplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(find_duplicate([3, 1, 3, 4, 2]), 3)
        self.assertEqual(find_duplicate([3, 3, 3, 3, 3]), 3)

    def test_edges(self) -> None:
        self.assertEqual(find_duplicate([1, 1]), 1)
        self.assertEqual(find_duplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]), 9)
        with self.assertRaises(ValueError):
            find_duplicate([1])


if __name__ == "__main__":
    unittest.main()
