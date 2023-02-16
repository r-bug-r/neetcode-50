# [053_binary_tree_level_order_traversal] breadth-first level grouping | invariant: O(n) time and space

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

def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return node values grouped by depth from top to bottom, left to right."""
    if root is None:
        return []

    levels: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        levels.append(_drain_level(queue))

    return levels


# --- helpers --------------------------------------------------------------

def _drain_level(queue: deque[TreeNode]) -> list[int]:
    level_values: list[int] = []
    for _ in range(len(queue)):
        node = queue.popleft()
        level_values.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return level_values


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

class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def test_examples(self) -> None:
        tree = _build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(level_order(tree), [[3], [9, 20], [15, 7]])
        self.assertEqual(level_order(_build_tree([1])), [[1]])

    def test_edges(self) -> None:
        self.assertEqual(level_order(None), [])
        skewed = _build_tree([1, 2, None, 3])
        self.assertEqual(level_order(skewed), [[1], [2], [3]])


if __name__ == "__main__":
    unittest.main()
