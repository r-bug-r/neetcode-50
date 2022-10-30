# [030_koko_eating_bananas] parametric binary search on eating speed | invariant: O(n log max_pile) time

import unittest


# --- public api -----------------------------------------------------------

def min_eating_speed(piles: list[int], hours_limit: int) -> int:
    """Return the minimum integer bananas-per-hour speed to finish within hours_limit."""
    if not piles:
        return 0

    lo = 1
    hi = max(piles)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if _hours_needed(piles, mid) <= hours_limit:
            hi = mid
            continue
        lo = mid + 1

    return lo


# --- helpers --------------------------------------------------------------

def _hours_needed(piles: list[int], speed: int) -> int:
    return sum((pile + speed - 1) // speed for pile in piles)


# --- tests ----------------------------------------------------------------

class TestMinEatingSpeed(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 6), 23)

    def test_edges(self) -> None:
        self.assertEqual(min_eating_speed([], 5), 0)
        self.assertEqual(min_eating_speed([1], 1), 1)
        self.assertEqual(min_eating_speed([100], 100), 1)


if __name__ == "__main__":
    unittest.main()
