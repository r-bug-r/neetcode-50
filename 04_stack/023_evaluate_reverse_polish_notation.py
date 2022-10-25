# [023_evaluate_reverse_polish_notation] postfix expression evaluator | invariant: O(n) time, O(n) space

from collections.abc import Callable
import operator
import unittest


# --- tables ---------------------------------------------------------------

def _trunc_div(lhs: int, rhs: int) -> int:
    # why: Python // floors toward -inf; RPN division truncates toward zero
    quotient = abs(lhs) // abs(rhs)
    return -quotient if (lhs < 0) ^ (rhs < 0) else quotient


OPERATORS: dict[str, Callable[[int, int], int]] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": _trunc_div,
}


# --- public api -----------------------------------------------------------

def eval_rpn(tokens: list[str]) -> int:
    """Evaluate a valid Reverse Polish Notation token sequence."""
    if not tokens:
        raise ValueError("tokens cannot be empty")

    operands: list[int] = []
    for token in tokens:
        op = OPERATORS.get(token)
        if op is None:
            operands.append(int(token))
            continue
        rhs = operands.pop()
        lhs = operands.pop()
        operands.append(op(lhs, rhs))

    return operands[0]


# --- tests ----------------------------------------------------------------

class TestEvalRpn(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(
            eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
            22,
        )

    def test_edges(self) -> None:
        self.assertEqual(eval_rpn(["42"]), 42)
        self.assertEqual(eval_rpn(["-7", "2", "/"]), -3)
        with self.assertRaises(ValueError):
            eval_rpn([])


if __name__ == "__main__":
    unittest.main()
