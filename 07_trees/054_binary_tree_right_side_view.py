# [054_binary_tree_right_side_view] rightmost node per depth | invariant: O(n) time and space

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

def right_side_view(root: TreeNode | None) -> list[int]:
    """Return values of nodes visible from the right side, top to bottom."""
    if root is None:
        return []

    visible: list[int] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        visible.append(_advance_level(queue))

    return visible


# --- helpers --------------------------------------------------------------

def _advance_level(queue: deque[TreeNode]) -> int:
    # invariant: the last node popped in each BFS wave is the rightmost at that depth
    rightmost_value = 0
    for _ in range(len(queue)):
        node = queue.popleft()
        rightmost_value = node.value
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return rightmost_value


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

class TestBinaryTreeRightSideView(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(right_side_view(_build_tree([1, 2, 3, None, 5, None, 4])), [1, 3, 4])
        self.assertEqual(right_side_view(_build_tree([1, 2, 3, 4, None, None, None, 5])), [1, 3, 4, 5])
        self.assertEqual(right_side_view(_build_tree([1, None, 3])), [1, 3])

    def test_edges(self) -> None:
        self.assertEqual(right_side_view(None), [])
        self.assertEqual(right_side_view(_build_tree([1, 2, None, 3])), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
