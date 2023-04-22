# [060_serialize_and_deserialize_binary_tree] preorder tree codec | invariant: O(n) encode and decode

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


_NULL_TOKEN = "#"


# --- public api -----------------------------------------------------------

class Codec:
    """Stateless preorder codec for binary trees."""

    def serialize(self, root: TreeNode | None) -> str:
        """Encode a binary tree into a comma-separated preorder string."""
        tokens: list[str] = []
        _encode_preorder(root, tokens)
        # perf: single join avoids quadratic string concatenation
        return ",".join(tokens)

    def deserialize(self, encoded: str) -> TreeNode | None:
        """Decode a preorder string produced by serialize back into a binary tree."""
        if not encoded:
            return None
        token_iter = iter(encoded.split(","))
        return _decode_preorder(token_iter)


# --- helpers --------------------------------------------------------------

def _encode_preorder(node: TreeNode | None, tokens: list[str]) -> None:
    if node is None:
        tokens.append(_NULL_TOKEN)
        return
    tokens.append(str(node.value))
    _encode_preorder(node.left, tokens)
    _encode_preorder(node.right, tokens)


def _decode_preorder(token_iter: object) -> TreeNode | None:
    token = next(token_iter)  # type: ignore[arg-type]
    if token == _NULL_TOKEN:
        return None
    node = TreeNode(int(token))
    node.left = _decode_preorder(token_iter)
    node.right = _decode_preorder(token_iter)
    return node


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

class TestSerializeDeserializeBinaryTree(unittest.TestCase):
    def test_examples(self) -> None:
        codec = Codec()
        tree = _build_tree([1, 2, 3, None, None, 4, 5])
        round_tripped = codec.deserialize(codec.serialize(tree))
        self.assertEqual(_to_level_list(round_tripped), [1, 2, 3, None, None, 4, 5])

    def test_edges(self) -> None:
        codec = Codec()
        self.assertIsNone(codec.deserialize(codec.serialize(None)))
        self.assertIsNone(codec.deserialize(""))
        single = _build_tree([-42])
        self.assertEqual(_to_level_list(codec.deserialize(codec.serialize(single))), [-42])


if __name__ == "__main__":
    unittest.main()
