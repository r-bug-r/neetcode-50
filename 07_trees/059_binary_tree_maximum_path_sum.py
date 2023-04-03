# [059_binary_tree_maximum_path_sum] bottom-up max path sum | invariant: O(n) time, O(h) space

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import unittest


# --- types ----------------------------------------------------------------

@dataclass(slots=True)
class TreeNode:
    """Binary tree node storing an integer value."""

    value: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


# --- public api -----------------------------------------------------------

def max_path_sum(root: TreeNode | None) -> int:
    """Return the maximum sum over any non-empty node-to-node path in the tree."""
    if root is None:
        raise ValueError("tree must contain at least one node")

    _, best_sum = _subtree_gains(root)
    return best_sum


# --- helpers --------------------------------------------------------------

def _subtree_gains(node: TreeNode) -> tuple[int, int]:
    left_gain = 0
    left_best = node.value
    if node.left is not None:
        raw_left_gain, left_best = _subtree_gains(node.left)
        left_gain = max(0, raw_left_gain)

    right_gain = 0
    right_best = node.value
    if node.right is not None:
        raw_right_gain, right_best = _subtree_gains(node.right)
        right_gain = max(0, raw_right_gain)

    # invariant: split_sum bridges left and right branches; branch_gain extends upward
    split_sum = node.value + left_gain + right_gain
    branch_gain = node.value + max(left_gain, right_gain)
    return branch_gain, max(split_sum, left_best, right_best)


def _build_tree(level_values: list[int | None]) -> TreeNode | None:
    if not level_values or level_values[0] is None:
        return None

    root = TreeNode(level_values[0])
    queue: deque[TreeNode] = deque([root])
    cursor = 1

    while queue and cursor < len(level_values):
        parent = queue.popleft()
        left_entry = level_values[cursor]
        cursor += 1
        if left_entry is not None:
            parent.left = TreeNode(left_entry)
            queue.append(parent.left)
        if cursor >= len(level_values):
            break
        right_entry = level_values[cursor]
        cursor += 1
        if right_entry is not None:
            parent.right = TreeNode(right_entry)
            queue.append(parent.right)

    return root


# --- tests ----------------------------------------------------------------

class TestBinaryTreeMaxPathSum(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(max_path_sum(_build_tree([1, 2, 3])), 6)
        self.assertEqual(max_path_sum(_build_tree([-10, 9, 20, None, None, 15, 7])), 42)

    def test_edges(self) -> None:
        self.assertEqual(max_path_sum(_build_tree([-3])), -3)
        self.assertEqual(max_path_sum(_build_tree([-2, -1])), -1)
        with self.assertRaises(ValueError):
            max_path_sum(None)


if __name__ == "__main__":
    unittest.main()
