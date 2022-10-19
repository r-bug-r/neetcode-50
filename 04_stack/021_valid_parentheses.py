# [021_valid_parentheses] bracket nesting validation | invariant: O(n) time, O(n) space

import unittest


# --- tables ---------------------------------------------------------------

BRACKET_PAIRS: dict[str, str] = {
    ")": "(",
    "]": "[",
    "}": "{",
}


# --- public api -----------------------------------------------------------

def is_valid(brackets: str) -> bool:
    """Return True if every opening bracket in brackets closes in valid order."""
    # edge: odd-length strings cannot pair every bracket
    if len(brackets) % 2 == 1:
        return False

    open_brackets: list[str] = []
    for ch in brackets:
        if ch not in BRACKET_PAIRS:
            open_brackets.append(ch)
            continue
        if not open_brackets or open_brackets.pop() != BRACKET_PAIRS[ch]:
            return False

    return not open_brackets


# --- tests ----------------------------------------------------------------

class TestValidParentheses(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(is_valid("()"))
        self.assertTrue(is_valid("()[]{}"))
        self.assertFalse(is_valid("(]"))
        self.assertTrue(is_valid("([])"))

    def test_edges(self) -> None:
        self.assertTrue(is_valid(""))
        self.assertFalse(is_valid("("))
        self.assertFalse(is_valid("]"))
        self.assertFalse(is_valid("([)]"))


if __name__ == "__main__":
    unittest.main()
