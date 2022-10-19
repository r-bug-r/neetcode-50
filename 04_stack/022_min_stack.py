# [022_min_stack] stack with O(1) minimum lookup | invariant: O(1) time per operation

import unittest


# --- public api -----------------------------------------------------------

class MinStack:
    """LIFO integer stack supporting constant-time minimum queries."""

    def __init__(self) -> None:
        self._entries: list[int] = []
        # invariant: _prefix_mins[i] equals min(_entries[:i + 1])
        self._prefix_mins: list[int] = []

    def push(self, value: int) -> None:
        """Push value onto the stack and update the running minimum."""
        self._entries.append(value)
        next_min = value if not self._prefix_mins or value < self._prefix_mins[-1] else self._prefix_mins[-1]
        self._prefix_mins.append(next_min)

    def pop(self) -> None:
        """Remove the top element; raises IndexError if the stack is empty."""
        if not self._entries:
            raise IndexError("pop from empty MinStack")
        self._entries.pop()
        self._prefix_mins.pop()

    def top(self) -> int:
        """Return the top element; raises IndexError if the stack is empty."""
        if not self._entries:
            raise IndexError("top of empty MinStack")
        return self._entries[-1]

    def get_min(self) -> int:
        """Return the minimum element; raises IndexError if the stack is empty."""
        if not self._prefix_mins:
            raise IndexError("min of empty MinStack")
        return self._prefix_mins[-1]


# --- tests ----------------------------------------------------------------

class TestMinStack(unittest.TestCase):
    def test_examples(self) -> None:
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.get_min(), -3)
        stack.pop()
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.get_min(), -2)

    def test_edges(self) -> None:
        stack = MinStack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.top()
        with self.assertRaises(IndexError):
            stack.get_min()

        stack.push(2)
        stack.push(2)
        self.assertEqual(stack.get_min(), 2)
        stack.pop()
        self.assertEqual(stack.get_min(), 2)


if __name__ == "__main__":
    unittest.main()
