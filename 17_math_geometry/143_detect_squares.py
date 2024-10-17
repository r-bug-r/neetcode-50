# [143_detect_squares] axis-aligned square counter | invariant: O(1) add, O(n) count

from collections import Counter, defaultdict
import unittest


# --- public api -----------------------------------------------------------

class DetectSquares:
    """Tracks 2D integer points and counts positive-area axis-aligned squares."""

    def __init__(self) -> None:
        self._counts: Counter[tuple[int, int]] = Counter()
        # perf: index distinct y-coords by x so count scans only collinear points
        self._y_counts_by_x: defaultdict[int, Counter[int]] = defaultdict(Counter)

    def add(self, point: list[int]) -> None:
        """Record a point occurrence in the multiset."""
        px, py = point
        self._counts[(px, py)] += 1
        self._y_counts_by_x[px][py] += 1

    def count(self, point: list[int]) -> int:
        """Return number of axis-aligned squares with one corner at point."""
        qx, qy = point
        collinear_ys = self._y_counts_by_x.get(qx)
        if not collinear_ys:
            return 0

        squares = 0
        for py, py_freq in collinear_ys.items():
            # edge: zero-area degenerate squares where py == qy are excluded
            if py == qy:
                continue
            side = abs(py - qy)
            left_x = qx - side
            right_x = qx + side
            left_pairs = self._counts[(left_x, qy)] * self._counts[(left_x, py)]
            right_pairs = self._counts[(right_x, qy)] * self._counts[(right_x, py)]
            squares += py_freq * (left_pairs + right_pairs)

        return squares


# --- tests ----------------------------------------------------------------

class TestDetectSquares(unittest.TestCase):
    def test_examples(self) -> None:
        detector = DetectSquares()
        detector.add([3, 10])
        detector.add([11, 2])
        detector.add([3, 2])
        self.assertEqual(detector.count([11, 10]), 1)
        self.assertEqual(detector.count([14, 8]), 0)
        detector.add([11, 2])
        self.assertEqual(detector.count([11, 10]), 2)

    def test_edges(self) -> None:
        detector = DetectSquares()
        self.assertEqual(detector.count([0, 0]), 0)
        # edge: duplicate points at query location itself do not form positive-area squares
        detector.add([0, 0])
        detector.add([0, 2])
        detector.add([2, 0])
        detector.add([2, 2])
        self.assertEqual(detector.count([0, 0]), 1)
        detector.add([-2, 0])
        detector.add([-2, 2])
        self.assertEqual(detector.count([0, 0]), 2)


if __name__ == "__main__":
    unittest.main()
