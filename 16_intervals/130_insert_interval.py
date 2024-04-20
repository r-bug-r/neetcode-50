# [130_insert_interval] sorted interval insertion with overlap merge | invariant: O(n) time

import unittest


# --- public api -----------------------------------------------------------

def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """Insert new_interval into sorted non-overlapping intervals and merge overlaps."""
    merged: list[list[int]] = []
    new_start, new_end = new_interval
    cursor = 0
    total = len(intervals)

    while cursor < total and intervals[cursor][1] < new_start:
        merged.append([intervals[cursor][0], intervals[cursor][1]])
        cursor += 1

    while cursor < total and intervals[cursor][0] <= new_end:
        new_start = min(new_start, intervals[cursor][0])
        new_end = max(new_end, intervals[cursor][1])
        cursor += 1

    merged.append([new_start, new_end])

    while cursor < total:
        merged.append([intervals[cursor][0], intervals[cursor][1]])
        cursor += 1

    return merged


# --- tests ----------------------------------------------------------------

class TestInsertInterval(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
        self.assertEqual(
            insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            [[1, 2], [3, 10], [12, 16]],
        )

    def test_edges(self) -> None:
        self.assertEqual(insert([], [5, 7]), [[5, 7]])
        self.assertEqual(insert([[3, 5]], [1, 2]), [[1, 2], [3, 5]])
        self.assertEqual(insert([[1, 2]], [3, 5]), [[1, 2], [3, 5]])
        # edge: touching boundary merges into a single interval
        self.assertEqual(insert([[1, 2], [5, 6]], [2, 5]), [[1, 6]])


if __name__ == "__main__":
    unittest.main()
