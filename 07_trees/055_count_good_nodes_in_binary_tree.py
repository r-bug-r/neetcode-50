# [055_count_good_nodes_in_binary_tree] root-path maxima count | invariant: O(n) time, O(h) space

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

def good_nodes(root: TreeNode | None) -> int:
    """Count nodes whose value is at least as large as every ancestor on their path."""
    if root is None:
        return 0
    return _count_visible(root, root.value)


# --- helpers --------------------------------------------------------------

def _count_visible(node: TreeNode | None, path_max: int) -> int:
    if node is None:
        return 0

    is_good = 1 if node.value >= path_max else 0
    next_max = node.value if node.value > path_max else path_max
    return is_good + _count_visible(node.left, next_max) + _count_visible(node.right, next_max)


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

class TestCountGoodNodes(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(good_nodes(_build_tree([3, 1, 4, 3, None, 1, 5])), 4)
        self.assertEqual(good_nodes(_build_tree([3, 3, None, 4, 2])), 3)
        self.assertEqual(good_nodes(_build_tree([1])), 1)

    def test_edges(self) -> None:
        self.assertEqual(good_nodes(None), 0)
        self.assertEqual(good_nodes(_build_tree([-1, -5, -2])), 1)


if __name__ == "__main__":
    unittest.main()
