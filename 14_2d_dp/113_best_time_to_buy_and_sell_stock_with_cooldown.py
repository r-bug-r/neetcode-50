# [113_best_time_to_buy_and_sell_stock_with_cooldown] 3-state trading DP | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def max_profit(prices: list[int]) -> int:
    """Return maximum stock profit with a mandatory one-day cooldown after each sale."""
    if len(prices) < 2:
        return 0

    held = -prices[0]
    sold = 0
    rest = 0

    for price in prices[1:]:
        prev_sold = sold
        sold = held + price
        # invariant: buying requires entering from rest so cooldown day is respected
        held = max(held, rest - price)
        rest = max(rest, prev_sold)

    return max(sold, rest)


# --- tests ----------------------------------------------------------------

class TestStockWithCooldown(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(max_profit([1, 2, 3, 0, 2]), 3)
        self.assertEqual(max_profit([1]), 0)

    def test_edges(self) -> None:
        self.assertEqual(max_profit([]), 0)
        self.assertEqual(max_profit([5, 4, 3, 2, 1]), 0)
        self.assertEqual(max_profit([1, 4, 2, 7]), 6)
        self.assertEqual(max_profit([2, 1, 4, 5, 2, 9, 7]), 10)


if __name__ == "__main__":
    unittest.main()
