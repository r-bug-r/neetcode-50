# [071_subsets] power set generation | invariant: O(n * 2^n) backtracking

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def subsets(nums: list[int]) -> list[list[int]]:
    """Return all distinct subsets (the power set) of unique integers."""
    collected: list[list[int]] = []
    _extend_subsets(0, nums, [], collected)
    return collected


# --- helpers --------------------------------------------------------------

def _extend_subsets(
    start: int,
    nums: list[int],
    chosen: list[int],
    collected: list[list[int]],
) -> None:
    collected.append(chosen.copy())
    for idx in range(start, len(nums)):
        chosen.append(nums[idx])
        _extend_subsets(idx + 1, nums, chosen, collected)
        chosen.pop()


# --- tests ----------------------------------------------------------------

class TestSubsets(unittest.TestCase):
    def test_examples(self) -> None:
        got = {tuple(sub) for sub in subsets([1, 2, 3])}
        expected = {(), (1,), (2,), (1, 2), (3,), (1, 3), (2, 3), (1, 2, 3)}
        self.assertEqual(got, expected)

    def test_edges(self) -> None:
        self.assertEqual(subsets([]), [[]])
        self.assertEqual({tuple(sub) for sub in subsets([0])}, {(), (0,)})


if __name__ == "__main__":
    unittest.main()
