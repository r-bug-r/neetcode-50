# [049_balanced_binary_tree] bottom-up height balance check | invariant: O(n) time, O(h) space

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

def is_balanced(root: TreeNode | None) -> bool:
    """Return True if every node's subtrees differ in height by at most one."""
    return _balanced_height(root) != -1


# --- helpers --------------------------------------------------------------

def _balanced_height(node: TreeNode | None) -> int:
    # perf: -1 sentinel short-circuits imbalanced subtrees in one bottom-up pass
    if node is None:
        return 0

    left_height = _balanced_height(node.left)
    if left_height == -1:
        return -1

    right_height = _balanced_height(node.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)


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

class TestBalancedBinaryTree(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(is_balanced(_build_tree([3, 9, 20, None, None, 15, 7])))
        self.assertFalse(is_balanced(_build_tree([1, 2, 2, 3, 3, None, None, 4, 4])))

    def test_edges(self) -> None:
        self.assertTrue(is_balanced(None))
        self.assertTrue(is_balanced(_build_tree([1])))


if __name__ == "__main__":
    unittest.main()
