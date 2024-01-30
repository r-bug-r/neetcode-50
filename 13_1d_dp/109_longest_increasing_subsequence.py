# [109_longest_increasing_subsequence] patience binary search | invariant: O(n log n) time

from bisect import bisect_left
import unittest


# --- public api -----------------------------------------------------------

def length_of_lis(nums: list[int]) -> int:
    """Return length of the longest strictly increasing subsequence in nums."""
    if not nums:
        return 0

    # invariant: tails[k] holds the smallest tail value of any increasing subsequence of length k + 1
    tails: list[int] = []

    for num in nums:
        slot = bisect_left(tails, num)
        if slot == len(tails):
            tails.append(num)
            continue
        tails[slot] = num

    return len(tails)


# --- tests ----------------------------------------------------------------

class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(length_of_lis([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(length_of_lis([7, 7, 7, 7, 7, 7, 7]), 1)

    def test_edges(self) -> None:
        self.assertEqual(length_of_lis([]), 0)
        self.assertEqual(length_of_lis([-5]), 1)
        self.assertEqual(length_of_lis([5, 4, 3, 2, 1]), 1)
        self.assertEqual(length_of_lis([1, 2, 3, 4, 5]), 5)


if __name__ == "__main__":
    unittest.main()
