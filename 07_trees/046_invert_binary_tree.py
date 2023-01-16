# [046_invert_binary_tree] iterative mirror swap | invariant: O(n) time, O(h) stack space

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

def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """Invert a binary tree in place by swapping left and right children."""
    if root is None:
        return None

    # perf: iterative stack avoids recursion depth limits on skewed trees
    pending = [root]
    while pending:
        node = pending.pop()
        node.left, node.right = node.right, node.left
        if node.left is not None:
            pending.append(node.left)
        if node.right is not None:
            pending.append(node.right)

    return root


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


def _to_level_list(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []

    levels: list[int | None] = []
    queue: deque[TreeNode | None] = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            levels.append(None)
            continue
        levels.append(node.value)
        queue.append(node.left)
        queue.append(node.right)

    while levels and levels[-1] is None:
        levels.pop()
    return levels


# --- tests ----------------------------------------------------------------

class TestInvertBinaryTree(unittest.TestCase):
    def test_examples(self) -> None:
        tree = _build_tree([4, 2, 7, 1, 3, 6, 9])
        self.assertEqual(_to_level_list(invert_tree(tree)), [4, 7, 2, 9, 6, 3, 1])

        small = _build_tree([2, 1, 3])
        self.assertEqual(_to_level_list(invert_tree(small)), [2, 3, 1])

    def test_edges(self) -> None:
        self.assertIsNone(invert_tree(None))
        self.assertEqual(_to_level_list(invert_tree(_build_tree([5]))), [5])


if __name__ == "__main__":
    unittest.main()
