# [051_subtree_of_another_tree] subtree match traversal | invariant: O(n * m) worst-case time

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

def is_subtree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
    """Return True if sub_root matches any subtree rooted inside root."""
    # edge: an empty tree is a subtree of every tree
    if sub_root is None:
        return True
    if root is None:
        return False
    if _is_same_tree(root, sub_root):
        return True

    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


# --- helpers --------------------------------------------------------------

def _is_same_tree(left_node: TreeNode | None, right_node: TreeNode | None) -> bool:
    if left_node is None and right_node is None:
        return True
    if left_node is None or right_node is None:
        return False
    if left_node.value != right_node.value:
        return False

    return _is_same_tree(left_node.left, right_node.left) and _is_same_tree(
        left_node.right, right_node.right
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

class TestSubtreeOfAnotherTree(unittest.TestCase):
    def test_examples(self) -> None:
        main_tree = _build_tree([3, 4, 5, 1, 2])
        sub_tree = _build_tree([4, 1, 2])
        self.assertTrue(is_subtree(main_tree, sub_tree))

        extended = _build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
        self.assertFalse(is_subtree(extended, sub_tree))

    def test_edges(self) -> None:
        self.assertTrue(is_subtree(_build_tree([1]), None))
        self.assertFalse(is_subtree(None, _build_tree([1])))


if __name__ == "__main__":
    unittest.main()
