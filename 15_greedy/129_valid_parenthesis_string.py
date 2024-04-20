# [129_valid_parenthesis_string] open-count interval tracking | invariant: O(n) time, O(1) space

import unittest

OPEN_DELTAS: dict[str, tuple[int, int]] = {
    "(": (1, 1),
    ")": (-1, -1),
    "*": (-1, 1),
}


# --- public api -----------------------------------------------------------

def check_valid_string(s: str) -> bool:
    """Return True when wildcard '*' as '(', ')' or empty can balance string s."""
    min_open = 0
    max_open = 0

    for ch in s:
        deltas = OPEN_DELTAS.get(ch)
        if deltas is None:
            return False
        min_open += deltas[0]
        max_open += deltas[1]
        if max_open < 0:
            return False
        # edge: discard negative min_open branches because '*' could act as empty or '('
        if min_open < 0:
            min_open = 0

    return min_open == 0


# --- tests ----------------------------------------------------------------

class TestValidParenthesisString(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(check_valid_string("()"))
        self.assertTrue(check_valid_string("(*)"))
        self.assertTrue(check_valid_string("(*))"))

    def test_edges(self) -> None:
        self.assertTrue(check_valid_string(""))
        self.assertTrue(check_valid_string("*"))
        self.assertFalse(check_valid_string("((("))
        self.assertFalse(check_valid_string(")*("))
        self.assertFalse(check_valid_string("((*)(*))((*"))


if __name__ == "__main__":
    unittest.main()
