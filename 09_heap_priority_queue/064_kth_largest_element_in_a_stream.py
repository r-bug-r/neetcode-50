# [064_kth_largest_element_in_a_stream] bounded min-heap stream tracker | invariant: heap size <= k

import heapq
import unittest


# --- public api -----------------------------------------------------------

class KthLargest:
    """Maintains the kth largest integer across an append-only stream."""

    def __init__(self, k: int, nums: list[int]) -> None:
        if k <= 0:
            raise ValueError("k must be positive")
        self._k = k
        # invariant: min_heap stores up to k largest values seen so far
        self._min_heap: list[int] = []
        for score in nums:
            self.add(score)

    def add(self, score: int) -> int:
        """Insert score into the stream and return the current kth largest value."""
        if len(self._min_heap) < self._k:
            heapq.heappush(self._min_heap, score)
        elif score > self._min_heap[0]:
            heapq.heapreplace(self._min_heap, score)
        return self._min_heap[0]


# --- tests ----------------------------------------------------------------

class TestKthLargest(unittest.TestCase):
    def test_examples(self) -> None:
        tracker = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(tracker.add(3), 4)
        self.assertEqual(tracker.add(5), 5)
        self.assertEqual(tracker.add(10), 5)
        self.assertEqual(tracker.add(9), 8)
        self.assertEqual(tracker.add(4), 8)

    def test_edges(self) -> None:
        with self.assertRaises(ValueError):
            KthLargest(0, [1])

        single = KthLargest(1, [])
        self.assertEqual(single.add(-5), -5)
        self.assertEqual(single.add(-10), -5)
        self.assertEqual(single.add(0), 0)

        delayed = KthLargest(3, [1])
        self.assertEqual(delayed.add(2), 1)
        self.assertEqual(delayed.add(3), 1)
        self.assertEqual(delayed.add(4), 2)


if __name__ == "__main__":
    unittest.main()
