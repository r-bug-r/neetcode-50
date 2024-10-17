# [145_number_of_1_bits] Brian Kernighan popcount | invariant: O(popcount) time, O(1) space

import unittest

# --- constants ------------------------------------------------------------

MASK_32 = 0xFFFFFFFF


# --- public api -----------------------------------------------------------

def hamming_weight(n: int) -> int:
    """Return count of set bits in the 32-bit unsigned representation of n."""
    bits = n & MASK_32
    set_bits = 0

    while bits:
        # perf: n & (n - 1) clears the lowest set bit per iteration
        bits &= bits - 1
        set_bits += 1

    return set_bits


# --- tests ----------------------------------------------------------------

class TestNumberOf1Bits(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(hamming_weight(11), 3)
        self.assertEqual(hamming_weight(128), 1)
        self.assertEqual(hamming_weight(2147483645), 30)

    def test_edges(self) -> None:
        self.assertEqual(hamming_weight(0), 0)
        self.assertEqual(hamming_weight(0xFFFFFFFF), 32)
        self.assertEqual(hamming_weight(1), 1)


if __name__ == "__main__":
    unittest.main()
