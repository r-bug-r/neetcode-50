# [010_valid_palindrome] alphanumeric palindrome check | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def is_palindrome(text: str) -> bool:
    """Return True if alphanumeric characters in text read the same forward and backward."""
    lo = 0
    hi = len(text) - 1

    while lo < hi:
        if not text[lo].isalnum():
            lo += 1
            continue
        if not text[hi].isalnum():
            hi -= 1
            continue
        if text[lo].lower() != text[hi].lower():
            return False
        lo += 1
        hi -= 1

    return True


# --- tests ----------------------------------------------------------------

class TestValidPalindrome(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertTrue(is_palindrome(" "))

    def test_edges(self) -> None:
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(".,!"))
        self.assertFalse(is_palindrome("0P"))
        self.assertTrue(is_palindrome("12321"))


if __name__ == "__main__":
    unittest.main()
