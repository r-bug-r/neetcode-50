# [005_top_k_frequent_elements] bucket-sort top k frequencies | invariant: O(n) time, O(n) space

from collections import Counter
import unittest


# --- public api -----------------------------------------------------------

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent integers in nums."""
    if k <= 0 or not nums:
        return []

    freq_by_num = Counter(nums)
    # perf: frequency buckets avoid O(n log n) heap or full sort
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_by_num.items():
        buckets[freq].append(num)

    top_nums: list[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        if not buckets[freq]:
            continue
        top_nums.extend(buckets[freq])
        if len(top_nums) >= k:
            return top_nums[:k]

    return top_nums


# --- tests ----------------------------------------------------------------

class TestTopKFrequent(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])
        self.assertEqual(top_k_frequent([1], 1), [1])

    def test_edges(self) -> None:
        self.assertEqual(top_k_frequent([], 2), [])
        self.assertEqual(top_k_frequent([4, 4, 5, 5], 2), [4, 5])


if __name__ == "__main__":
    unittest.main()
