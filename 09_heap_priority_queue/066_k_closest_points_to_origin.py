# [066_k_closest_points_to_origin] bounded max-heap origin filter | invariant: O(n log k) time

import heapq
import unittest


# --- public api -----------------------------------------------------------

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """Return the k points closest to the origin (0, 0) in any order."""
    if k <= 0 or not points:
        return []
    if k >= len(points):
        return [list(point) for point in points]

    # perf: bounded max-heap of size k avoids sorting all n points
    max_heap: list[tuple[int, int, int]] = []
    for x, y in points:
        neg_sq_dist = -(x * x + y * y)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (neg_sq_dist, x, y))
        elif neg_sq_dist > max_heap[0][0]:
            heapq.heapreplace(max_heap, (neg_sq_dist, x, y))

    return [[x, y] for _, x, y in max_heap]


# --- tests ----------------------------------------------------------------

class TestKClosest(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(k_closest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        closest_two = k_closest([[3, 3], [5, -1], [-2, 4]], 2)
        self.assertEqual(sorted(closest_two), sorted([[3, 3], [-2, 4]]))

    def test_edges(self) -> None:
        self.assertEqual(k_closest([], 2), [])
        self.assertEqual(k_closest([[1, 2]], 0), [])
        self.assertEqual(k_closest([[1, 2], [3, 4]], 5), [[1, 2], [3, 4]])
        tied = k_closest([[0, 1], [1, 0], [2, 2]], 2)
        self.assertEqual(sorted(tied), sorted([[0, 1], [1, 0]]))


if __name__ == "__main__":
    unittest.main()
