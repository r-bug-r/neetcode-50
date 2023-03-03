# [056_validate_binary_search_tree] strict interval BST check | invariant: O(n) time, O(h) space

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

def is_valid_bst(root: TreeNode | None) -> bool:
    """Return True if every node satisfies strict BST ordering across its full subtree."""
    return _within_bounds(root, None, None)


# --- helpers --------------------------------------------------------------

def _within_bounds(node: TreeNode | None, low_bound: int | None, high_bound: int | None) -> bool:
    if node is None:
        return True
    if low_bound is not None and node.value <= low_bound:
        return False
    if high_bound is not None and node.value >= high_bound:
        return False

    return _within_bounds(node.left, low_bound, node.value) and _within_bounds(
        node.right, node.value, high_bound
    )


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

class TestValidateBinarySearchTree(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(is_valid_bst(_build_tree([2, 1, 3])))
        self.assertFalse(is_valid_bst(_build_tree([5, 1, 4, None, None, 3, 6])))

    def test_edges(self) -> None:
        self.assertTrue(is_valid_bst(None))
        self.assertFalse(is_valid_bst(_build_tree([2, 2, 2])))
        # edge: right subtree descendant 3 violates ancestor root 5
        self.assertFalse(is_valid_bst(_build_tree([5, 4, 6, None, None, 3, 7])))


if __name__ == "__main__":
    unittest.main()
