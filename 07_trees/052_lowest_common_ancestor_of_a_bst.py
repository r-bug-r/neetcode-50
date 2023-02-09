# [052_lowest_common_ancestor_of_a_bst] iterative BST split search | invariant: O(h) time, O(1) space

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

def lowest_common_ancestor(
    root: TreeNode | None,
    first_node: TreeNode,
    second_node: TreeNode,
) -> TreeNode | None:
    """Return the lowest common ancestor of first_node and second_node in a BST."""
    low_target = min(first_node.value, second_node.value)
    high_target = max(first_node.value, second_node.value)
    curr_node = root

    while curr_node is not None:
        if high_target < curr_node.value:
            curr_node = curr_node.left
            continue
        if low_target > curr_node.value:
            curr_node = curr_node.right
            continue
        # invariant: curr_node lies in [low_target, high_target] so it is the split point
        return curr_node

    return None


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


def _find_node(root: TreeNode | None, target: int) -> TreeNode:
    curr_node = root
    while curr_node is not None:
        if target < curr_node.value:
            curr_node = curr_node.left
        elif target > curr_node.value:
            curr_node = curr_node.right
        else:
            return curr_node
    raise ValueError(f"target {target} not found in BST")


# --- tests ----------------------------------------------------------------

class TestLowestCommonAncestorBST(unittest.TestCase):
    def test_examples(self) -> None:
        bst = _build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        lca_root = lowest_common_ancestor(bst, _find_node(bst, 2), _find_node(bst, 8))
        assert lca_root is not None
        self.assertEqual(lca_root.value, 6)

        lca_left = lowest_common_ancestor(bst, _find_node(bst, 2), _find_node(bst, 4))
        assert lca_left is not None
        self.assertEqual(lca_left.value, 2)

    def test_edges(self) -> None:
        tiny = _build_tree([2, 1])
        lca_tiny = lowest_common_ancestor(tiny, _find_node(tiny, 2), _find_node(tiny, 1))
        assert lca_tiny is not None
        self.assertEqual(lca_tiny.value, 2)
        self.assertIsNone(lowest_common_ancestor(None, TreeNode(1), TreeNode(2)))


if __name__ == "__main__":
    unittest.main()
