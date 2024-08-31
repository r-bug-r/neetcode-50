# [141_powx_n] iterative binary exponentiation | invariant: O(log |n|) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def my_pow(x: float, n: int) -> float:
    """Compute x raised to integer power n using binary exponentiation."""
    if n == 0:
        return 1.0

    base = x
    exponent = n
    if exponent < 0:
        # edge: invert base once so negative powers reuse the positive loop
        base = 1.0 / base
        exponent = -exponent

    power = 1.0
    while exponent > 0:
        if exponent & 1:
            power *= base
        base *= base
        exponent >>= 1

    return power


# --- tests ----------------------------------------------------------------

class TestPowXN(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertAlmostEqual(my_pow(2.0, 10), 1024.0)
        self.assertAlmostEqual(my_pow(2.1, 3), 9.261)
        self.assertAlmostEqual(my_pow(2.0, -2), 0.25)

    def test_edges(self) -> None:
        self.assertEqual(my_pow(0.0, 0), 1.0)
        self.assertEqual(my_pow(0.0, 5), 0.0)
        self.assertEqual(my_pow(-2.0, 3), -8.0)
        self.assertAlmostEqual(my_pow(1.0, -(1 << 31)), 1.0)


if __name__ == "__main__":
    unittest.main()
