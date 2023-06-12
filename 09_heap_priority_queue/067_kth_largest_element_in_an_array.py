# [067_kth_largest_element_in_an_array] bounded min-heap selection | invariant: O(n log k) time, O(k) space

import heapq
import unittest


# --- public api -----------------------------------------------------------

def find_kth_largest(nums: list[int], k: int) -> int:
    """Return the kth largest element in nums; raises ValueError if k is invalid."""
    if k <= 0 or k > len(nums):
        raise ValueError("k must be within [1, len(nums)]")

    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # perf: index loop avoids allocating a nums[k:] slice copy
    for idx in range(k, len(nums)):
        candidate = nums[idx]
        if candidate > min_heap[0]:
            heapq.heapreplace(min_heap, candidate)

    return min_heap[0]


# --- tests ----------------------------------------------------------------

class TestFindKthLargest(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_edges(self) -> None:
        with self.assertRaises(ValueError):
            find_kth_largest([], 1)
        with self.assertRaises(ValueError):
            find_kth_largest([1, 2], 3)

        self.assertEqual(find_kth_largest([-1, -5, -3], 1), -1)
        self.assertEqual(find_kth_largest([-1, -5, -3], 3), -5)


if __name__ == "__main__":
    unittest.main()
