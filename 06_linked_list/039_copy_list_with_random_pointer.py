# [039_copy_list_with_random_pointer] deep copy with random links | invariant: O(n) time, O(n) map space

from __future__ import annotations

from dataclasses import dataclass
import unittest


# --- types ----------------------------------------------------------------

@dataclass(eq=False, slots=True)
class RandomNode:
    """Linked list node with an optional random pointer; identity-hashed."""

    value: int = 0
    next_node: RandomNode | None = None
    random_node: RandomNode | None = None


# --- public api -----------------------------------------------------------

def copy_random_list(head: RandomNode | None) -> RandomNode | None:
    """Deep-copy a linked list with next and random pointers without mutating input."""
    if head is None:
        return None

    # perf: O(1) identity map links original nodes to clones in two linear passes
    clones: dict[RandomNode, RandomNode] = {}
    curr_node: RandomNode | None = head
    while curr_node is not None:
        clones[curr_node] = RandomNode(curr_node.value)
        curr_node = curr_node.next_node

    curr_node = head
    while curr_node is not None:
        clone = clones[curr_node]
        if curr_node.next_node is not None:
            clone.next_node = clones[curr_node.next_node]
        if curr_node.random_node is not None:
            clone.random_node = clones[curr_node.random_node]
        curr_node = curr_node.next_node

    return clones[head]


# --- helpers --------------------------------------------------------------

def _build_random_list(spec: list[tuple[int, int | None]]) -> RandomNode | None:
    if not spec:
        return None
    nodes = [RandomNode(value) for value, _ in spec]
    for idx, (_, random_idx) in enumerate(spec):
        if idx + 1 < len(nodes):
            nodes[idx].next_node = nodes[idx + 1]
        if random_idx is not None:
            nodes[idx].random_node = nodes[random_idx]
    return nodes[0]


def _serialize_random_list(head: RandomNode | None) -> list[tuple[int, int | None]]:
    nodes: list[RandomNode] = []
    index_by_node: dict[RandomNode, int] = {}
    curr_node = head
    while curr_node is not None:
        index_by_node[curr_node] = len(nodes)
        nodes.append(curr_node)
        curr_node = curr_node.next_node

    serialized: list[tuple[int, int | None]] = []
    for node in nodes:
        random_idx = index_by_node[node.random_node] if node.random_node is not None else None
        serialized.append((node.value, random_idx))
    return serialized


# --- tests ----------------------------------------------------------------

class TestCopyListWithRandomPointer(unittest.TestCase):
    def test_examples(self) -> None:
        spec = [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]
        source = _build_random_list(spec)
        cloned = copy_random_list(source)
        self.assertIsNot(cloned, source)
        self.assertEqual(_serialize_random_list(cloned), spec)

        pair_spec = [(1, 1), (2, 1)]
        self.assertEqual(_serialize_random_list(copy_random_list(_build_random_list(pair_spec))), pair_spec)

    def test_edges(self) -> None:
        self.assertIsNone(copy_random_list(None))
        self_ref_spec = [(3, 0)]
        source = _build_random_list(self_ref_spec)
        cloned = copy_random_list(source)
        assert cloned is not None
        self.assertIs(cloned.random_node, cloned)
        self.assertEqual(_serialize_random_list(cloned), self_ref_spec)


if __name__ == "__main__":
    unittest.main()
