# [073_permutations] full permutation generation | invariant: O(n * n!) space-bounded

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def permute(nums: list[int]) -> list[list[int]]:
    """Return all permutations of a list of distinct integers."""
    perms: list[list[int]] = []
    used = [False] * len(nums)
    _build_perms(nums, used, [], perms)
    return perms


# --- helpers --------------------------------------------------------------

def _build_perms(
    nums: list[int],
    used: list[bool],
    chosen: list[int],
    perms: list[list[int]],
) -> None:
    if len(chosen) == len(nums):
        perms.append(chosen.copy())
        return

    for idx, candidate in enumerate(nums):
        if used[idx]:
            continue
        used[idx] = True
        chosen.append(candidate)
        _build_perms(nums, used, chosen, perms)
        chosen.pop()
        used[idx] = False


# --- tests ----------------------------------------------------------------

class TestPermutations(unittest.TestCase):
    def test_examples(self) -> None:
        got = {tuple(p) for p in permute([1, 2, 3])}
        expected = {
            (1, 2, 3), (1, 3, 2), (2, 1, 3),
            (2, 3, 1), (3, 1, 2), (3, 2, 1),
        }
        self.assertEqual(got, expected)

    def test_edges(self) -> None:
        self.assertEqual(permute([0, 1]), [[0, 1], [1, 0]])
        self.assertEqual(permute([1]), [[1]])


if __name__ == "__main__":
    unittest.main()
