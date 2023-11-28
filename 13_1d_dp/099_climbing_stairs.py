# [099_climbing_stairs] Fibonacci DP recurrence | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def climb_stairs(n: int) -> int:
    """Return distinct ways to climb n stairs taking 1 or 2 steps at a time."""
    if n <= 0:
        return 0
    if n <= 2:
        return n

    two_steps_back = 1
    one_step_back = 2

    for _ in range(3, n + 1):
        ways = one_step_back + two_steps_back
        two_steps_back = one_step_back
        one_step_back = ways

    return one_step_back


# --- tests ----------------------------------------------------------------

class TestClimbingStairs(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(climb_stairs(2), 2)
        self.assertEqual(climb_stairs(3), 3)

    def test_edges(self) -> None:
        self.assertEqual(climb_stairs(0), 0)
        self.assertEqual(climb_stairs(1), 1)
        self.assertEqual(climb_stairs(5), 8)
        self.assertEqual(climb_stairs(10), 89)


if __name__ == "__main__":
    unittest.main()
