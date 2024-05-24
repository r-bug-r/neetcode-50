# [134_meeting_rooms_ii] min-heap concurrent room counter | invariant: O(n log n) time

import heapq
import unittest


# --- public api -----------------------------------------------------------

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """Return minimum conference rooms required to host all meetings."""
    if not intervals:
        return 0

    ordered = sorted(intervals, key=lambda span: span[0])
    active_ends: list[int] = []

    for start, end in ordered:
        # perf: reuse earliest ending room instead of allocating a new one
        if active_ends and active_ends[0] <= start:
            heapq.heapreplace(active_ends, end)
            continue
        heapq.heappush(active_ends, end)

    return len(active_ends)


# --- tests ----------------------------------------------------------------

class TestMeetingRoomsII(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]), 2)
        self.assertEqual(min_meeting_rooms([[7, 10], [2, 4]]), 1)

    def test_edges(self) -> None:
        self.assertEqual(min_meeting_rooms([]), 0)
        self.assertEqual(min_meeting_rooms([[1, 5]]), 1)
        self.assertEqual(min_meeting_rooms([[1, 5], [5, 10], [10, 15]]), 1)
        self.assertEqual(min_meeting_rooms([[1, 10], [2, 10], [3, 10]]), 3)


if __name__ == "__main__":
    unittest.main()
