# [015_best_time_to_buy_and_sell_stock] single-trade max profit | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def max_profit(prices: list[int]) -> int:
    """Return maximum profit from one buy followed by one sell, or 0 if none exists."""
    # edge: fewer than two price points cannot form a buy-sell pair
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
            continue
        profit = price - min_price
        if profit > best_profit:
            best_profit = profit

    return best_profit


# --- tests ----------------------------------------------------------------

class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)

    def test_edges(self) -> None:
        self.assertEqual(max_profit([]), 0)
        self.assertEqual(max_profit([5]), 0)
        self.assertEqual(max_profit([2, 4, 1]), 2)
        self.assertEqual(max_profit([3, 3, 3]), 0)


if __name__ == "__main__":
    unittest.main()
