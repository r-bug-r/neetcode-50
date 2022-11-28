# [034_median_of_two_sorted_arrays] binary partition median search | invariant: O(log min(m, n)) time

from math import inf
import unittest


# --- public api -----------------------------------------------------------

def find_median_sorted_arrays(nums_a: list[int], nums_b: list[int]) -> float:
    """Return the median of two sorted integer arrays in logarithmic time."""
    if not nums_a and not nums_b:
        raise ValueError("arrays cannot both be empty")

    # perf: binary-search only the shorter array to bound steps to O(log min(m, n))
    if len(nums_a) > len(nums_b):
        nums_a, nums_b = nums_b, nums_a

    len_a, len_b = len(nums_a), len(nums_b)
    half_len = (len_a + len_b + 1) // 2
    lo, hi = 0, len_a

    while lo <= hi:
        cut_a = lo + (hi - lo) // 2
        cut_b = half_len - cut_a
        left_a = nums_a[cut_a - 1] if cut_a > 0 else -inf
        right_a = nums_a[cut_a] if cut_a < len_a else inf
        left_b = nums_b[cut_b - 1] if cut_b > 0 else -inf
        right_b = nums_b[cut_b] if cut_b < len_b else inf

        if left_a <= right_b and left_b <= right_a:
            return _compute_median(left_a, left_b, right_a, right_b, (len_a + len_b) % 2 == 1)
        if left_a > right_b:
            hi = cut_a - 1
            continue
        lo = cut_a + 1

    raise ValueError("input arrays must be sorted")


# --- helpers --------------------------------------------------------------

def _compute_median(
    left_a: float,
    left_b: float,
    right_a: float,
    right_b: float,
    is_odd: bool,
) -> float:
    left_max = max(left_a, left_b)
    if is_odd:
        return float(left_max)
    return (left_max + min(right_a, right_b)) / 2.0


# --- tests ----------------------------------------------------------------

class TestMedianSortedArrays(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(find_median_sorted_arrays([1, 3], [2]), 2.0)
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.5)

    def test_edges(self) -> None:
        self.assertEqual(find_median_sorted_arrays([], [1]), 1.0)
        self.assertEqual(find_median_sorted_arrays([2], []), 2.0)
        self.assertEqual(find_median_sorted_arrays([0, 0], [0, 0]), 0.0)
        with self.assertRaises(ValueError):
            find_median_sorted_arrays([], [])


if __name__ == "__main__":
    unittest.main()
