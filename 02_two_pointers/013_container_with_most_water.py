# [013_container_with_most_water] max rectangle area between lines | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def max_water_area(heights: list[int]) -> int:
    """Return the maximum water area formed by any two vertical lines in heights."""
    lo = 0
    hi = len(heights) - 1
    best_area = 0

    while lo < hi:
        width = hi - lo
        # why: moving the taller wall can only shrink width without raising height
        if heights[lo] < heights[hi]:
            best_area = max(best_area, width * heights[lo])
            lo += 1
            continue
        best_area = max(best_area, width * heights[hi])
        hi -= 1

    return best_area


# --- tests ----------------------------------------------------------------

class TestContainerWithMostWater(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(max_water_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(max_water_area([1, 1]), 1)

    def test_edges(self) -> None:
        self.assertEqual(max_water_area([]), 0)
        self.assertEqual(max_water_area([5]), 0)
        self.assertEqual(max_water_area([0, 0, 0]), 0)
        self.assertEqual(max_water_area([4, 3, 2, 1, 4]), 16)


if __name__ == "__main__":
    unittest.main()
