# [027_largest_rectangle_in_histogram] monotonic bar stack area scan | invariant: O(n) time, O(n) space

import unittest


# --- public api -----------------------------------------------------------

def largest_rectangle_area(heights: list[int]) -> int:
    """Return the largest rectangular area formed by contiguous histogram bars."""
    if not heights:
        return 0

    max_area = 0
    # invariant: bar_stack holds (start_idx, height) pairs with increasing heights
    bar_stack: list[tuple[int, int]] = []

    for idx, height in enumerate(heights):
        start_idx = idx
        while bar_stack and bar_stack[-1][1] > height:
            prev_start, prev_height = bar_stack.pop()
            max_area = max(max_area, prev_height * (idx - prev_start))
            start_idx = prev_start
        bar_stack.append((start_idx, height))

    total_bars = len(heights)
    for start_idx, height in bar_stack:
        max_area = max(max_area, height * (total_bars - start_idx))

    return max_area


# --- tests ----------------------------------------------------------------

class TestLargestRectangleArea(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(largest_rectangle_area([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(largest_rectangle_area([2, 4]), 4)

    def test_edges(self) -> None:
        self.assertEqual(largest_rectangle_area([]), 0)
        self.assertEqual(largest_rectangle_area([5]), 5)
        self.assertEqual(largest_rectangle_area([0, 0, 0]), 0)
        self.assertEqual(largest_rectangle_area([3, 3, 3, 3]), 12)


if __name__ == "__main__":
    unittest.main()
