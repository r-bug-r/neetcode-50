# [127_merge_triplets_to_form_target_triplet] bounded axis-mask scan | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def merge_triplets(triplets: list[list[int]], target: list[int]) -> bool:
    """Return True when component-wise max of valid triplets can form target."""
    if not triplets or len(target) != 3:
        return False

    tx, ty, tz = target
    found_mask = 0

    for a, b, c in triplets:
        # invariant: triplets exceeding any target axis poison component-wise max and are skipped
        if a > tx or b > ty or c > tz:
            continue
        found_mask |= (a == tx) | ((b == ty) << 1) | ((c == tz) << 2)
        if found_mask == 7:
            return True

    return False


# --- tests ----------------------------------------------------------------

class TestMergeTriplets(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(merge_triplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))
        self.assertFalse(merge_triplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]))
        self.assertTrue(merge_triplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]))

    def test_edges(self) -> None:
        self.assertFalse(merge_triplets([], [1, 2, 3]))
        self.assertTrue(merge_triplets([[1, 2, 3]], [1, 2, 3]))
        self.assertFalse(merge_triplets([[2, 2, 3], [1, 3, 3]], [1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
