# [020_sliding_window_maximum] monotonic deque window maxima | invariant: O(n) time, O(k) space

from collections import deque
import unittest


# --- public api -----------------------------------------------------------

def max_sliding_window(nums: list[int], window_size: int) -> list[int]:
    """Return the maximum element for each contiguous window of length window_size."""
    if not nums or window_size <= 0 or window_size > len(nums):
        return []

    window_indices: deque[int] = deque()
    maxima: list[int] = []

    for idx, num in enumerate(nums):
        if window_indices and window_indices[0] <= idx - window_size:
            window_indices.popleft()
        # invariant: deque holds indices whose values are strictly decreasing
        while window_indices and nums[window_indices[-1]] <= num:
            window_indices.pop()
        window_indices.append(idx)
        if idx >= window_size - 1:
            maxima.append(nums[window_indices[0]])

    return maxima


# --- tests ----------------------------------------------------------------

class TestSlidingWindowMaximum(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(max_sliding_window([1], 1), [1])

    def test_edges(self) -> None:
        self.assertEqual(max_sliding_window([], 3), [])
        self.assertEqual(max_sliding_window([9, 11], 2), [11])
        self.assertEqual(max_sliding_window([7, 2, 4], 2), [7, 4])
        self.assertEqual(max_sliding_window([1, -1], 1), [1, -1])


if __name__ == "__main__":
    unittest.main()
