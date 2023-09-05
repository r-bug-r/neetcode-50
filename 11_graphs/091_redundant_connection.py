# [091_redundant_connection] cycle-closing edge detection | invariant: last-order DSU union

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    """Return the edge that closes a cycle in an N-node 1-indexed undirected graph."""
    node_count = len(edges)
    parents = list(range(node_count + 1))
    ranks = [0] * (node_count + 1)

    for u_node, v_node in edges:
        if not _union(parents, ranks, u_node, v_node):
            return [u_node, v_node]

    return []


# --- helpers --------------------------------------------------------------

def _find_root(parents: list[int], node: int) -> int:
    while parents[node] != node:
        parents[node] = parents[parents[node]]
        node = parents[node]
    return node


def _union(parents: list[int], ranks: list[int], u_node: int, v_node: int) -> bool:
    root_u = _find_root(parents, u_node)
    root_v = _find_root(parents, v_node)
    if root_u == root_v:
        return False

    if ranks[root_u] < ranks[root_v]:
        root_u, root_v = root_v, root_u
    parents[root_v] = root_u
    if ranks[root_u] == ranks[root_v]:
        ranks[root_u] += 1
    return True


# --- tests ----------------------------------------------------------------

class TestRedundantConnection(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(find_redundant_connection([[1, 2], [1, 3], [2, 3]]), [2, 3])
        self.assertEqual(
            find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]),
            [1, 4],
        )

    def test_edges(self) -> None:
        self.assertEqual(find_redundant_connection([[1, 2], [2, 3], [1, 3]]), [1, 3])
        self.assertEqual(find_redundant_connection([]), [])


if __name__ == "__main__":
    unittest.main()
