# [058_construct_binary_tree_from_preorder_and_inorder_traversal] O(n) tree rebuild | invariant: unique values

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

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """Reconstruct a binary tree from unique preorder and inorder traversals."""
    if len(preorder) != len(inorder):
        raise ValueError("preorder and inorder must have equal length")
    if not preorder:
        return None

    # perf: index map avoids O(n) inorder.index() scans inside recursion
    inorder_index = {value: idx for idx, value in enumerate(inorder)}
    return _build_slice(preorder, 0, 0, len(inorder) - 1, inorder_index)


# --- helpers --------------------------------------------------------------

def _build_slice(
    preorder: list[int],
    pre_root: int,
    in_left: int,
    in_right: int,
    inorder_index: dict[int, int],
) -> TreeNode | None:
    if in_left > in_right:
        return None

    root_value = preorder[pre_root]
    mid_idx = inorder_index[root_value]
    left_count = mid_idx - in_left

    root = TreeNode(root_value)
    root.left = _build_slice(preorder, pre_root + 1, in_left, mid_idx - 1, inorder_index)
    root.right = _build_slice(preorder, pre_root + 1 + left_count, mid_idx + 1, in_right, inorder_index)
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

class TestConstructBinaryTree(unittest.TestCase):
    def test_examples(self) -> None:
        tree = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        self.assertEqual(_to_level_list(tree), [3, 9, 20, None, None, 15, 7])
        self.assertEqual(_to_level_list(build_tree([-1], [-1])), [-1])

    def test_edges(self) -> None:
        self.assertIsNone(build_tree([], []))
        with self.assertRaises(ValueError):
            build_tree([1, 2], [1])


if __name__ == "__main__":
    unittest.main()
