# [149_sum_of_two_integers] bitwise carry-add in 32-bit twos complement | invariant: O(1) time

import unittest

# --- constants ------------------------------------------------------------

MASK_32 = 0xFFFFFFFF
INT32_MAX = 0x7FFFFFFF


# --- public api -----------------------------------------------------------

def get_sum(a: int, b: int) -> int:
    """Add two 32-bit signed integers without using + or - operators."""
    # why: Python ints have arbitrary width so 32-bit masking prevents infinite carry loops
    total = a & MASK_32
    carry = b & MASK_32

    while carry:
        next_carry = ((total & carry) << 1) & MASK_32
        total ^= carry
        carry = next_carry

    return total if total <= INT32_MAX else ~(total ^ MASK_32)


# --- tests ----------------------------------------------------------------

class TestSumOfTwoIntegers(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(get_sum(1, 2), 3)
        self.assertEqual(get_sum(2, 3), 5)

    def test_edges(self) -> None:
        self.assertEqual(get_sum(-1, 1), 0)
        self.assertEqual(get_sum(-12, -8), -20)
        self.assertEqual(get_sum(0, -7), -7)
        self.assertEqual(get_sum(-1000, 1000), 0)


if __name__ == "__main__":
    unittest.main()
