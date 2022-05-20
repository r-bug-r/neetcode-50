# [009_longest_consecutive_sequence] hash-set sequence starts | invariant: O(n) time, O(n) space

import unittest


# --- public api -----------------------------------------------------------

def longest_consecutive(nums: list[int]) -> int:
    """Return the length of the longest consecutive integer sequence."""
    if not nums:
        return 0

    num_set = set(nums)
    longest_run = 0

    for num in num_set:
        # perf: only expand from sequence starts to keep total steps O(n)
        if (num - 1) in num_set:
            continue

        run_len = 1
        while (num + run_len) in num_set:
            run_len += 1
        if run_len > longest_run:
            longest_run = run_len

    return longest_run


# --- tests ----------------------------------------------------------------

class TestLongestConsecutive(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_edges(self) -> None:
        self.assertEqual(longest_consecutive([]), 0)
        self.assertEqual(longest_consecutive([7]), 1)


if __name__ == "__main__":
    unittest.main()
