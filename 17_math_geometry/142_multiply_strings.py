# [142_multiply_strings] grade-school big-integer multiplication | invariant: O(m*n) time

import unittest


# --- public api -----------------------------------------------------------

def multiply(num1: str, num2: str) -> str:
    """Multiply two non-negative decimal integer strings without big-int casting."""
    if num1 == "0" or num2 == "0":
        return "0"

    products = [0] * (len(num1) + len(num2))

    for idx_a in range(len(num1) - 1, -1, -1):
        digit_a = ord(num1[idx_a]) - 48
        _accumulate_row(products, idx_a, digit_a, num2)

    first_nonzero = 0
    while first_nonzero < len(products) and products[first_nonzero] == 0:
        first_nonzero += 1

    return "".join(chr(48 + digit) for digit in products[first_nonzero:])


# --- helpers --------------------------------------------------------------

def _accumulate_row(products: list[int], idx_a: int, digit_a: int, num2: str) -> None:
    for idx_b in range(len(num2) - 1, -1, -1):
        digit_b = ord(num2[idx_b]) - 48
        low_slot = idx_a + idx_b + 1
        high_slot = idx_a + idx_b
        carry, remainder = divmod(products[low_slot] + digit_a * digit_b, 10)
        products[low_slot] = remainder
        products[high_slot] += carry


# --- tests ----------------------------------------------------------------

class TestMultiplyStrings(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(multiply("2", "3"), "6")
        self.assertEqual(multiply("123", "456"), "56088")

    def test_edges(self) -> None:
        self.assertEqual(multiply("0", "99999"), "0")
        self.assertEqual(multiply("999", "999"), "998001")
        self.assertEqual(multiply("1", "12345678901234567890"), "12345678901234567890")


if __name__ == "__main__":
    unittest.main()
