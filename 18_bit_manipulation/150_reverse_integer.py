# [150_reverse_integer] 32-bit signed digit reversal with overflow guard | invariant: O(log n)

import unittest

# --- constants ------------------------------------------------------------

INT32_MAX = (1 << 31) - 1
ABS_INT32_MIN = 1 << 31


# --- public api -----------------------------------------------------------

def reverse(x: int) -> int:
    """Reverse decimal digits of signed 32-bit integer x, or return 0 on overflow."""
    if x == 0:
        return 0

    sign = -1 if x < 0 else 1
    remaining = -x if x < 0 else x
    limit_div10, limit_mod10 = divmod(INT32_MAX if sign > 0 else ABS_INT32_MIN, 10)
    reversed_abs = 0

    while remaining:
        remaining, digit = divmod(remaining, 10)
        # edge: check 32-bit bound before multiplying by 10 to mirror fixed-width arithmetic
        if reversed_abs > limit_div10 or (reversed_abs == limit_div10 and digit > limit_mod10):
            return 0
        reversed_abs = reversed_abs * 10 + digit

    return sign * reversed_abs


# --- tests ----------------------------------------------------------------

class TestReverseInteger(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(reverse(123), 321)
        self.assertEqual(reverse(-123), -321)
        self.assertEqual(reverse(120), 21)

    def test_edges(self) -> None:
        self.assertEqual(reverse(0), 0)
        self.assertEqual(reverse(1534236469), 0)
        self.assertEqual(reverse(-2147483648), 0)
        self.assertEqual(reverse(-2147483412), -2143847412)


if __name__ == "__main__":
    unittest.main()
