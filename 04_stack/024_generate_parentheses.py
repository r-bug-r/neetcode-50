# [024_generate_parentheses] well-formed bracket enumeration | invariant: valid prefix counts

import unittest


# --- public api -----------------------------------------------------------

def generate_parentheses(pair_count: int) -> list[str]:
    """Return all valid combinations of pair_count balanced parenthesis pairs."""
    if pair_count <= 0:
        return []

    combinations: list[str] = []
    _backtrack([], 0, 0, pair_count, combinations)
    return combinations


# --- helpers --------------------------------------------------------------

def _backtrack(
    chars: list[str],
    open_count: int,
    close_count: int,
    pair_count: int,
    combinations: list[str],
) -> None:
    if len(chars) == 2 * pair_count:
        # perf: single join on complete leaf avoids repeated string allocations
        combinations.append("".join(chars))
        return

    if open_count < pair_count:
        chars.append("(")
        _backtrack(chars, open_count + 1, close_count, pair_count, combinations)
        chars.pop()

    if close_count < open_count:
        chars.append(")")
        _backtrack(chars, open_count, close_count + 1, pair_count, combinations)
        chars.pop()


# --- tests ----------------------------------------------------------------

class TestGenerateParentheses(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            sorted(generate_parentheses(3)),
            sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]),
        )
        self.assertEqual(generate_parentheses(1), ["()"])

    def test_edges(self) -> None:
        self.assertEqual(generate_parentheses(0), [])
        self.assertEqual(generate_parentheses(2), ["(())", "()()"])


if __name__ == "__main__":
    unittest.main()
