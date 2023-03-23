# [057_kth_smallest_element_in_a_bst] iterative in-order selection | invariant: O(h + k) time

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import unittest


# --- types ----------------------------------------------------------------

@dataclass(slots=True)
class TreeNode:
    """Binary search tree node storing an integer value."""

    value: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


# --- public api -----------------------------------------------------------

def kth_smallest(root: TreeNode | None, rank: int) -> int:
    """Return the 1-indexed rank-th smallest value in a binary search tree."""
    if rank <= 0:
        raise ValueError("rank must be positive")

    stack: list[TreeNode] = []
    _push_left_spine(root, stack)
    remaining = rank

    while stack:
        node = stack.pop()
        remaining -= 1
        if remaining == 0:
            return node.value
        _push_left_spine(node.right, stack)

    raise ValueError("rank exceeds number of nodes in BST")


# --- helpers --------------------------------------------------------------

def _push_left_spine(node: TreeNode | None, stack: list[TreeNode]) -> None:
    curr_node = node
    while curr_node is not None:
        stack.append(curr_node)
        curr_node = curr_node.left


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

class TestKthSmallestInBST(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(kth_smallest(_build_tree([3, 1, 4, None, 2]), 1), 1)
        self.assertEqual(kth_smallest(_build_tree([5, 3, 6, 2, 4, None, None, 1]), 3), 3)

    def test_edges(self) -> None:
        with self.assertRaises(ValueError):
            kth_smallest(_build_tree([1]), 0)
        with self.assertRaises(ValueError):
            kth_smallest(_build_tree([1]), 2)


if __name__ == "__main__":
    unittest.main()
