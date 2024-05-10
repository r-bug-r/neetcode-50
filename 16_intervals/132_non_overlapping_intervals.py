# [132_non_overlapping_intervals] greedy earliest-end removal | invariant: O(n log n) time

import unittest


# --- public api -----------------------------------------------------------

def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """Return minimum intervals to remove so the remainder are non-overlapping."""
    if len(intervals) <= 1:
        return 0

    # perf: sorting by end time maximizes remaining room for subsequent intervals
    ordered = sorted(intervals, key=lambda span: span[1])
    kept_end = ordered[0][1]
    removals = 0

    for start, end in ordered[1:]:
        if start < kept_end:
            removals += 1
            continue
        kept_end = end

    return removals


# --- tests ----------------------------------------------------------------

class TestNonOverlappingIntervals(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
        self.assertEqual(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]), 2)
        self.assertEqual(erase_overlap_intervals([[1, 2], [2, 3]]), 0)

    def test_edges(self) -> None:
        self.assertEqual(erase_overlap_intervals([]), 0)
        self.assertEqual(erase_overlap_intervals([[1, 5]]), 0)
        self.assertEqual(erase_overlap_intervals([[-5, -2], [-3, 0], [0, 2]]), 1)


if __name__ == "__main__":
    unittest.main()
