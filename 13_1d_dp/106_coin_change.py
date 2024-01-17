# [106_coin_change] unbounded knapsack min-coins DP | invariant: O(coins * amount) time

import unittest


# --- public api -----------------------------------------------------------

def coin_change(coins: list[int], amount: int) -> int:
    """Return fewest coins needed to sum to amount, or -1 if impossible."""
    if amount == 0:
        return 0
    if amount < 0 or not coins:
        return -1

    sentinel = amount + 1
    min_coins = [sentinel] * (amount + 1)
    min_coins[0] = 0
    # perf: deduplicate and bound coins once before DP sweeps
    usable_coins = sorted(coin for coin in set(coins) if 0 < coin <= amount)

    for coin in usable_coins:
        _relax_coin_totals(min_coins, coin, amount)

    return -1 if min_coins[amount] == sentinel else min_coins[amount]


# --- helpers --------------------------------------------------------------

def _relax_coin_totals(min_coins: list[int], coin: int, amount: int) -> None:
    for total in range(coin, amount + 1):
        candidate = min_coins[total - coin] + 1
        if candidate < min_coins[total]:
            min_coins[total] = candidate


# --- tests ----------------------------------------------------------------

class TestCoinChange(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(coin_change([2], 3), -1)
        self.assertEqual(coin_change([1], 0), 0)

    def test_edges(self) -> None:
        self.assertEqual(coin_change([], 5), -1)
        self.assertEqual(coin_change([1], -1), -1)
        # edge: greedy choice 4+1+1=3 is worse than 3+3=2
        self.assertEqual(coin_change([1, 3, 4], 6), 2)
        self.assertEqual(coin_change([5, 5, 10], 15), 2)


if __name__ == "__main__":
    unittest.main()
