# [148_missing_number] index-value XOR reduction | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def missing_number(nums: list[int]) -> int:
    """Return the missing integer from the range [0, len(nums)]."""
    missing = len(nums)
    for idx, num in enumerate(nums):
        missing ^= idx ^ num
    return missing


# --- tests ----------------------------------------------------------------

class TestMissingNumber(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(missing_number([3, 0, 1]), 2)
        self.assertEqual(missing_number([0, 1]), 2)
        self.assertEqual(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_edges(self) -> None:
        self.assertEqual(missing_number([]), 0)
        self.assertEqual(missing_number([0]), 1)
        self.assertEqual(missing_number([1]), 0)


if __name__ == "__main__":
    unittest.main()
