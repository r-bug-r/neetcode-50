# [147_reverse_bits] 32-bit unsigned bit reversal | invariant: O(1) time, O(1) space

import unittest

# --- constants ------------------------------------------------------------

MASK_32 = 0xFFFFFFFF
BIT_WIDTH = 32


# --- public api -----------------------------------------------------------

def reverse_bits(n: int) -> int:
    """Reverse the 32 bits of an unsigned integer."""
    bits = n & MASK_32
    reversed_bits = 0

    for _ in range(BIT_WIDTH):
        reversed_bits = (reversed_bits << 1) | (bits & 1)
        bits >>= 1

    return reversed_bits


# --- tests ----------------------------------------------------------------

class TestReverseBits(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(reverse_bits(43261596), 964176192)
        self.assertEqual(reverse_bits(4294967293), 3221225471)

    def test_edges(self) -> None:
        self.assertEqual(reverse_bits(0), 0)
        self.assertEqual(reverse_bits(0xFFFFFFFF), 0xFFFFFFFF)
        self.assertEqual(reverse_bits(1), 1 << 31)


if __name__ == "__main__":
    unittest.main()
