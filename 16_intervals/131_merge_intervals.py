# [131_merge_intervals] coalesce overlapping intervals | invariant: O(n log n) time

import unittest


# --- public api -----------------------------------------------------------

def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Merge all overlapping intervals and return disjoint sorted spans."""
    if not intervals:
        return []

    ordered = sorted(intervals, key=lambda span: (span[0], span[1]))
    merged: list[list[int]] = [[ordered[0][0], ordered[0][1]]]

    for start, end in ordered[1:]:
        if start > merged[-1][1]:
            merged.append([start, end])
            continue
        merged[-1][1] = max(merged[-1][1], end)

    return merged


# --- tests ----------------------------------------------------------------

class TestMergeIntervals(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )
        self.assertEqual(merge([[1, 4], [4, 5]]), [[1, 5]])

    def test_edges(self) -> None:
        self.assertEqual(merge([]), [])
        self.assertEqual(merge([[5, 5]]), [[5, 5]])
        self.assertEqual(merge([[1, 4], [2, 3]]), [[1, 4]])
        self.assertEqual(merge([[4, 7], [1, 4]]), [[1, 7]])


if __name__ == "__main__":
    unittest.main()
