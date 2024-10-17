# [144_single_number] XOR cancellation of paired integers | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def single_number(nums: list[int]) -> int:
    """Return the sole integer appearing once when all others appear twice."""
    unpaired = 0
    for num in nums:
        # invariant: a ^ a == 0 leaves only the unique element after one sweep
        unpaired ^= num
    return unpaired


# --- tests ----------------------------------------------------------------

class TestSingleNumber(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(single_number([2, 2, 1]), 1)
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)
        self.assertEqual(single_number([1]), 1)

    def test_edges(self) -> None:
        self.assertEqual(single_number([-3, 7, -3]), 7)
        self.assertEqual(single_number([0, 5, 5]), 0)


if __name__ == "__main__":
    unittest.main()
