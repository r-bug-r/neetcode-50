# [140_plus_one] right-to-left carry propagation | invariant: O(n) time, non-mutating

import unittest


# --- public api -----------------------------------------------------------

def plus_one(digits: list[int]) -> list[int]:
    """Increment a non-negative integer represented as big-endian decimal digits."""
    incremented = digits.copy()

    for idx in range(len(incremented) - 1, -1, -1):
        if incremented[idx] < 9:
            incremented[idx] += 1
            return incremented
        incremented[idx] = 0

    # edge: all-nines input overflows to an extra leading 1
    return [1, *incremented]


# --- tests ----------------------------------------------------------------

class TestPlusOne(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(plus_one([1, 2, 3]), [1, 2, 4])
        self.assertEqual(plus_one([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(plus_one([9]), [1, 0])

    def test_edges(self) -> None:
        self.assertEqual(plus_one([0]), [1])
        self.assertEqual(plus_one([9, 9, 9]), [1, 0, 0, 0])
        original = [1, 9]
        self.assertEqual(plus_one(original), [2, 0])
        self.assertEqual(original, [1, 9])


if __name__ == "__main__":
    unittest.main()
