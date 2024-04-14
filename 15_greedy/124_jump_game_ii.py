# [124_jump_game_ii] greedy BFS-layer horizon | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def jump(nums: list[int]) -> int:
    """Return minimum jumps needed to reach the last index, assuming it is reachable."""
    if len(nums) <= 1:
        return 0

    last_idx = len(nums) - 1
    jumps = 0
    layer_end = 0
    farthest = 0

    for idx in range(last_idx):
        reach = idx + nums[idx]
        if reach > farthest:
            farthest = reach
        if idx != layer_end:
            continue
        # invariant: finishing a layer commits one jump to the farthest discovered horizon
        jumps += 1
        layer_end = farthest
        if layer_end >= last_idx:
            return jumps

    return jumps


# --- tests ----------------------------------------------------------------

class TestJumpGameII(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(jump([2, 3, 1, 1, 4]), 2)
        self.assertEqual(jump([2, 3, 0, 1, 4]), 2)

    def test_edges(self) -> None:
        self.assertEqual(jump([]), 0)
        self.assertEqual(jump([0]), 0)
        self.assertEqual(jump([1, 2, 3]), 2)
        self.assertEqual(jump([5, 1, 1, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
