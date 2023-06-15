# [070_find_median_from_data_stream] dual-heap running median | invariant: O(log n) add, O(1) median

import heapq
import unittest


# --- public api -----------------------------------------------------------

class MedianFinder:
    """Streaming median tracker backed by a balanced max-heap and min-heap."""

    def __init__(self) -> None:
        # invariant: len(_lower_max) == len(_upper_min) or len(_lower_max) == len(_upper_min) + 1
        self._lower_max: list[int] = []
        self._upper_min: list[int] = []

    def add_num(self, num: int) -> None:
        """Insert num into the stream and rebalance the two halves."""
        if not self._lower_max or num <= -self._lower_max[0]:
            heapq.heappush(self._lower_max, -num)
        else:
            heapq.heappush(self._upper_min, num)
        self._rebalance()

    def find_median(self) -> float:
        """Return the current median; raises ValueError if no numbers were added."""
        if not self._lower_max:
            raise ValueError("median of empty stream")
        if len(self._lower_max) > len(self._upper_min):
            return float(-self._lower_max[0])
        return (-self._lower_max[0] + self._upper_min[0]) / 2.0

    def _rebalance(self) -> None:
        if len(self._lower_max) > len(self._upper_min) + 1:
            heapq.heappush(self._upper_min, -heapq.heappop(self._lower_max))
        elif len(self._upper_min) > len(self._lower_max):
            heapq.heappush(self._lower_max, -heapq.heappop(self._upper_min))


# --- tests ----------------------------------------------------------------

class TestMedianFinder(unittest.TestCase):
    def test_examples(self) -> None:
        finder = MedianFinder()
        finder.add_num(1)
        finder.add_num(2)
        self.assertEqual(finder.find_median(), 1.5)
        finder.add_num(3)
        self.assertEqual(finder.find_median(), 2.0)

    def test_edges(self) -> None:
        finder = MedianFinder()
        with self.assertRaises(ValueError):
            finder.find_median()

        for num in (5, -2, -2, 10, 0):
            finder.add_num(num)
        self.assertEqual(finder.find_median(), 0.0)
        finder.add_num(1)
        self.assertEqual(finder.find_median(), 0.5)


if __name__ == "__main__":
    unittest.main()
