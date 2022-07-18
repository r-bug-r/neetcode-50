# [014_trapping_rain_water] trapped elevation water volume | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def trap_rain_water(heights: list[int]) -> int:
    """Return total units of rainwater trapped between elevation bars in heights."""
    # edge: fewer than three bars cannot form a basin
    if len(heights) < 3:
        return 0

    lo = 0
    hi = len(heights) - 1
    left_peak = heights[lo]
    right_peak = heights[hi]
    trapped = 0

    while lo < hi:
        # invariant: the smaller boundary peak caps water level at its moving pointer
        if left_peak <= right_peak:
            lo += 1
            left_peak = max(left_peak, heights[lo])
            trapped += left_peak - heights[lo]
            continue
        hi -= 1
        right_peak = max(right_peak, heights[hi])
        trapped += right_peak - heights[hi]

    return trapped


# --- tests ----------------------------------------------------------------

class TestTrappingRainWater(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(trap_rain_water([4, 2, 0, 3, 2, 5]), 9)

    def test_edges(self) -> None:
        self.assertEqual(trap_rain_water([]), 0)
        self.assertEqual(trap_rain_water([3, 1]), 0)
        self.assertEqual(trap_rain_water([1, 2, 3, 4]), 0)
        self.assertEqual(trap_rain_water([5, 0, 5]), 5)


if __name__ == "__main__":
    unittest.main()
