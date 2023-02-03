# [048_diameter_of_binary_tree] bottom-up longest path | invariant: O(n) time, O(h) stack space

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

def diameter_of_binary_tree(root: TreeNode | None) -> int:
    """Return the longest path length in edges between any two nodes."""
    _, best_diameter = _measure_subtree(root)
    return best_diameter


# --- helpers --------------------------------------------------------------

def _measure_subtree(node: TreeNode | None) -> tuple[int, int]:
    if node is None:
        return 0, 0

    left_height, left_diam = _measure_subtree(node.left)
    right_height, right_diam = _measure_subtree(node.right)
    # invariant: through-node path spans left_height + right_height edges
    local_diam = left_height + right_height
    best_diam = max(local_diam, left_diam, right_diam)
    return 1 + max(left_height, right_height), best_diam


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

class TestDiameterOfBinaryTree(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(diameter_of_binary_tree(_build_tree([1, 2, 3, 4, 5])), 3)
        self.assertEqual(diameter_of_binary_tree(_build_tree([1, 2])), 1)

    def test_edges(self) -> None:
        self.assertEqual(diameter_of_binary_tree(None), 0)
        self.assertEqual(diameter_of_binary_tree(_build_tree([7])), 0)


if __name__ == "__main__":
    unittest.main()
