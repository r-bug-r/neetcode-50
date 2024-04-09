# [123_jump_game] greedy reachability frontier | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def can_jump(nums: list[int]) -> bool:
    """Return True when the last index is reachable from index 0."""
    if len(nums) <= 1:
        return True

    last_idx = len(nums) - 1
    farthest = 0

    for idx, step in enumerate(nums):
        if idx > farthest:
            return False
        reach = idx + step
        if reach > farthest:
            farthest = reach
        if farthest >= last_idx:
            return True

    return False


# --- tests ----------------------------------------------------------------

class TestJumpGame(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(can_jump([2, 3, 1, 1, 4]))
        self.assertFalse(can_jump([3, 2, 1, 0, 4]))

    def test_edges(self) -> None:
        self.assertTrue(can_jump([]))
        self.assertTrue(can_jump([0]))
        self.assertFalse(can_jump([0, 2, 3]))
        self.assertTrue(can_jump([2, 0, 0]))


if __name__ == "__main__":
    unittest.main()
