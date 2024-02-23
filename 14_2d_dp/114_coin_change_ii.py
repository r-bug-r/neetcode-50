# [114_coin_change_ii] unbounded knapsack combination DP | invariant: O(coins * amount) time

import unittest


# --- public api -----------------------------------------------------------

def change(amount: int, coins: list[int]) -> int:
    """Return number of coin combinations that sum to amount with unlimited coins."""
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    if not coins:
        return 0

    ways = [0] * (amount + 1)
    ways[0] = 1
    # invariant: outer loop over distinct coins counts unordered combinations once
    usable_coins = sorted(coin for coin in set(coins) if 0 < coin <= amount)

    for coin in usable_coins:
        _add_coin_combinations(ways, coin, amount)

    return ways[amount]


# --- helpers --------------------------------------------------------------

def _add_coin_combinations(ways: list[int], coin: int, amount: int) -> None:
    for total in range(coin, amount + 1):
        ways[total] += ways[total - coin]


# --- tests ----------------------------------------------------------------

class TestCoinChangeII(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(change(5, [1, 2, 5]), 4)
        self.assertEqual(change(3, [2]), 0)
        self.assertEqual(change(10, [10]), 1)

    def test_edges(self) -> None:
        self.assertEqual(change(0, []), 1)
        self.assertEqual(change(5, []), 0)
        self.assertEqual(change(-1, [1, 2]), 0)
        self.assertEqual(change(4, [1, 2, 3]), 4)


if __name__ == "__main__":
    unittest.main()
