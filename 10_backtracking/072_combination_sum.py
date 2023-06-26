# [072_combination_sum] unbounded sum combinations | invariant: sorted pruning

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Return all unique combinations of positive candidates summing to target."""
    sorted_nums = sorted(candidates)
    matches: list[list[int]] = []
    _search_sums(0, target, sorted_nums, [], matches)
    return matches


# --- helpers --------------------------------------------------------------

def _search_sums(
    start: int,
    remaining: int,
    sorted_nums: list[int],
    chosen: list[int],
    matches: list[list[int]],
) -> None:
    if remaining == 0:
        matches.append(chosen.copy())
        return

    for idx in range(start, len(sorted_nums)):
        candidate = sorted_nums[idx]
        # perf: sorted order allows early break for the remaining branch
        if candidate > remaining:
            break
        chosen.append(candidate)
        _search_sums(idx, remaining - candidate, sorted_nums, chosen, matches)
        chosen.pop()


# --- tests ----------------------------------------------------------------

class TestCombinationSum(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            sorted(combination_sum([2, 3, 6, 7], 7)),
            [[2, 2, 3], [7]],
        )
        self.assertEqual(
            sorted(combination_sum([2, 3, 5], 8)),
            [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        )

    def test_edges(self) -> None:
        self.assertEqual(combination_sum([2], 1), [])
        self.assertEqual(combination_sum([], 5), [])


if __name__ == "__main__":
    unittest.main()
