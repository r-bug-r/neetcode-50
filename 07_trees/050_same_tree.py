# [050_same_tree] structural and value equality check | invariant: O(n) time, O(h) space

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

def is_same_tree(left_root: TreeNode | None, right_root: TreeNode | None) -> bool:
    """Return True if both binary trees have identical topology and node values."""
    if left_root is None and right_root is None:
        return True
    if left_root is None or right_root is None:
        return False
    if left_root.value != right_root.value:
        return False

    return is_same_tree(left_root.left, right_root.left) and is_same_tree(
        left_root.right, right_root.right
    )


# --- helpers --------------------------------------------------------------

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

class TestSameTree(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(is_same_tree(_build_tree([1, 2, 3]), _build_tree([1, 2, 3])))
        self.assertFalse(is_same_tree(_build_tree([1, 2]), _build_tree([1, None, 2])))
        self.assertFalse(is_same_tree(_build_tree([1, 2, 1]), _build_tree([1, 1, 2])))

    def test_edges(self) -> None:
        self.assertTrue(is_same_tree(None, None))
        self.assertFalse(is_same_tree(None, _build_tree([0])))


if __name__ == "__main__":
    unittest.main()
