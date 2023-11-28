# [100_min_cost_climbing_stairs] rolling 2-step DP | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def min_cost_climbing_stairs(cost: list[int]) -> int:
    """Return minimum cost to reach the top floor past the end of cost."""
    step_count = len(cost)
    if step_count < 2:
        return 0

    two_back = 0
    one_back = 0

    for idx in range(2, step_count + 1):
        # invariant: one_back holds min cost to reach step idx - 1
        cheapest = min(one_back + cost[idx - 1], two_back + cost[idx - 2])
        two_back = one_back
        one_back = cheapest

    return one_back


# --- tests ----------------------------------------------------------------

class TestMinCostClimbingStairs(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(min_cost_climbing_stairs([10, 15, 20]), 15)
        self.assertEqual(
            min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
            6,
        )

    def test_edges(self) -> None:
        self.assertEqual(min_cost_climbing_stairs([]), 0)
        self.assertEqual(min_cost_climbing_stairs([5]), 0)
        self.assertEqual(min_cost_climbing_stairs([10, 15]), 10)
        self.assertEqual(min_cost_climbing_stairs([0, 0, 0, 0]), 0)


if __name__ == "__main__":
    unittest.main()
