# [139_happy_number] Floyd cycle detection on digit-square sum | invariant: O(1) space

import unittest


# --- public api -----------------------------------------------------------

def is_happy(n: int) -> bool:
    """Return True if repeatedly summing squared digits reaches 1."""
    if n <= 0:
        return False

    slow = n
    fast = _sum_square_digits(n)

    # perf: tortoise-and-hare avoids allocating a visited set
    while fast != 1 and slow != fast:
        slow = _sum_square_digits(slow)
        fast = _sum_square_digits(_sum_square_digits(fast))

    return fast == 1


# --- helpers --------------------------------------------------------------

def _sum_square_digits(number: int) -> int:
    total = 0
    while number > 0:
        number, digit = divmod(number, 10)
        total += digit * digit
    return total


# --- tests ----------------------------------------------------------------

class TestHappyNumber(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(is_happy(19))
        self.assertFalse(is_happy(2))

    def test_edges(self) -> None:
        self.assertTrue(is_happy(1))
        self.assertTrue(is_happy(7))
        self.assertFalse(is_happy(0))
        self.assertFalse(is_happy(4))


if __name__ == "__main__":
    unittest.main()
