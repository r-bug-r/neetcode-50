# [075_combination_sum_ii] bounded unique sum combinations | invariant: sorted level-skip dedup

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def combination_sum_ii(candidates: list[int], target: int) -> list[list[int]]:
    """Return unique combinations where each candidate is used at most once."""
    sorted_nums = sorted(candidates)
    matches: list[list[int]] = []
    _search_unique_sums(0, target, sorted_nums, [], matches)
    return matches


# --- helpers --------------------------------------------------------------

def _search_unique_sums(
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
        if idx > start and sorted_nums[idx] == sorted_nums[idx - 1]:
            continue
        candidate = sorted_nums[idx]
        if candidate > remaining:
            break
        chosen.append(candidate)
        _search_unique_sums(idx + 1, remaining - candidate, sorted_nums, chosen, matches)
        chosen.pop()


# --- tests ----------------------------------------------------------------

class TestCombinationSumII(unittest.TestCase):
    def test_examples(self) -> None:
        got = sorted(combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8))
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertEqual(got, expected)

    def test_edges(self) -> None:
        self.assertEqual(
            sorted(combination_sum_ii([2, 5, 2, 1, 2], 5)),
            [[1, 2, 2], [5]],
        )
        self.assertEqual(combination_sum_ii([3, 3], 2), [])


if __name__ == "__main__":
    unittest.main()
