# [065_last_stone_weight] max-heap stone collision simulation | invariant: O(n log n) time

import heapq
import unittest


# --- public api -----------------------------------------------------------

def last_stone_weight(stones: list[int]) -> int:
    """Return the remaining stone weight after smashing the two heaviest repeatedly."""
    if not stones:
        return 0

    # perf: negate weights so Python's min-heap acts as a max-heap
    max_heap = [-weight for weight in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        heaviest = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)
        if heaviest != second:
            heapq.heappush(max_heap, -(heaviest - second))

    return -max_heap[0] if max_heap else 0


# --- tests ----------------------------------------------------------------

class TestLastStoneWeight(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(last_stone_weight([2, 7, 4, 1, 8, 1]), 1)
        self.assertEqual(last_stone_weight([1]), 1)

    def test_edges(self) -> None:
        self.assertEqual(last_stone_weight([]), 0)
        self.assertEqual(last_stone_weight([5, 5]), 0)
        self.assertEqual(last_stone_weight([10, 4, 2, 10]), 2)


if __name__ == "__main__":
    unittest.main()
