# [146_counting_bits] linear DP bit-count recurrence | invariant: O(n) time, O(n) space

import unittest


# --- public api -----------------------------------------------------------

def count_bits(n: int) -> list[int]:
    """Return popcount for every integer from 0 through n inclusive."""
    if n < 0:
        return []

    counts = [0] * (n + 1)
    for num in range(1, n + 1):
        # invariant: dropping the least significant bit reduces to a solved subproblem
        counts[num] = counts[num >> 1] + (num & 1)

    return counts


# --- tests ----------------------------------------------------------------

class TestCountingBits(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(count_bits(2), [0, 1, 1])
        self.assertEqual(count_bits(5), [0, 1, 1, 2, 1, 2])

    def test_edges(self) -> None:
        self.assertEqual(count_bits(0), [0])
        self.assertEqual(count_bits(-1), [])
        self.assertEqual(count_bits(8), [0, 1, 1, 2, 1, 2, 2, 3, 1])


if __name__ == "__main__":
    unittest.main()
