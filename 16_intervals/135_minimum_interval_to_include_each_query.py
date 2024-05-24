# [135_minimum_interval_to_include_each_query] offline sweep with min-heap | invariant: O((n+q) log n)

import heapq
import unittest


# --- public api -----------------------------------------------------------

def min_interval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    """Return shortest interval length covering each query, or -1 if none."""
    if not queries:
        return []
    if not intervals:
        return [-1] * len(queries)

    ordered_intervals = sorted(intervals, key=lambda span: span[0])
    # perf: deduplicate queries once so duplicate lookups take O(1)
    sorted_queries = sorted(set(queries))
    active_heap: list[tuple[int, int]] = []
    answer_by_query: dict[int, int] = {}
    cursor = 0
    total = len(ordered_intervals)

    for query in sorted_queries:
        while cursor < total and ordered_intervals[cursor][0] <= query:
            left, right = ordered_intervals[cursor]
            heapq.heappush(active_heap, (right - left + 1, right))
            cursor += 1

        while active_heap and active_heap[0][1] < query:
            heapq.heappop(active_heap)

        answer_by_query[query] = active_heap[0][0] if active_heap else -1

    return [answer_by_query[query] for query in queries]


# --- tests ----------------------------------------------------------------

class TestMinimumInterval(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            min_interval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]),
            [3, 3, 1, 4],
        )
        self.assertEqual(
            min_interval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]),
            [2, -1, 4, 6],
        )

    def test_edges(self) -> None:
        self.assertEqual(min_interval([], [1, 2]), [-1, -1])
        self.assertEqual(min_interval([[1, 5]], []), [])
        self.assertEqual(min_interval([[5, 5], [1, 10]], [5, 5, 11]), [1, 1, -1])


if __name__ == "__main__":
    unittest.main()
