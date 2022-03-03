# [001_contains_duplicate] duplicate check in integer array | invariant: O(n) time, O(n) space

import unittest


# --- public api -----------------------------------------------------------

def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any integer appears at least twice in nums."""
    # edge: fewer than two elements cannot contain a duplicate
    if len(nums) < 2:
        return False

    seen_nums: set[int] = set()
    for num in nums:
        # perf: O(1) hash lookup exits on the first repeated value
        if num in seen_nums:
            return True
        seen_nums.add(num)

    return False


# --- tests ----------------------------------------------------------------

class TestContainsDuplicate(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))
        self.assertTrue(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_edges(self) -> None:
        self.assertFalse(contains_duplicate([]))
        self.assertFalse(contains_duplicate([42]))
        self.assertTrue(contains_duplicate([-1, -1]))


if __name__ == "__main__":
    unittest.main()
