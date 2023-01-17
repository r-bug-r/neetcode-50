# [047_maximum_depth_of_binary_tree] iterative tree depth | invariant: O(n) time, O(h) space

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

def max_depth(root: TreeNode | None) -> int:
    """Return the number of nodes along the longest root-to-leaf path."""
    if root is None:
        return 0

    best_depth = 0
    pending: list[tuple[TreeNode, int]] = [(root, 1)]
    while pending:
        node, depth = pending.pop()
        if depth > best_depth:
            best_depth = depth
        if node.left is not None:
            pending.append((node.left, depth + 1))
        if node.right is not None:
            pending.append((node.right, depth + 1))

    return best_depth


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

class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(max_depth(_build_tree([3, 9, 20, None, None, 15, 7])), 3)
        self.assertEqual(max_depth(_build_tree([1, None, 2])), 2)

    def test_edges(self) -> None:
        self.assertEqual(max_depth(None), 0)
        self.assertEqual(max_depth(_build_tree([42])), 1)


if __name__ == "__main__":
    unittest.main()
