# [074_subsets_ii] deduplicated power set | invariant: sorted level-skip dedup

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    """Return all unique subsets of an integer list that may contain duplicates."""
    sorted_nums = sorted(nums)
    collected: list[list[int]] = []
    _extend_unique(0, sorted_nums, [], collected)
    return collected


# --- helpers --------------------------------------------------------------

def _extend_unique(
    start: int,
    sorted_nums: list[int],
    chosen: list[int],
    collected: list[list[int]],
) -> None:
    collected.append(chosen.copy())
    for idx in range(start, len(sorted_nums)):
        # invariant: skip duplicate values at the same recursion depth to avoid duplicate subsets
        if idx > start and sorted_nums[idx] == sorted_nums[idx - 1]:
            continue
        chosen.append(sorted_nums[idx])
        _extend_unique(idx + 1, sorted_nums, chosen, collected)
        chosen.pop()


# --- tests ----------------------------------------------------------------

class TestSubsetsII(unittest.TestCase):
    def test_examples(self) -> None:
        got = {tuple(sub) for sub in subsets_with_dup([1, 2, 2])}
        expected = {(), (1,), (1, 2), (1, 2, 2), (2,), (2, 2)}
        self.assertEqual(got, expected)

    def test_edges(self) -> None:
        self.assertEqual(subsets_with_dup([0]), [[], [0]])
        self.assertEqual(subsets_with_dup([2, 2, 2]), [[], [2], [2, 2], [2, 2, 2]])


if __name__ == "__main__":
    unittest.main()
